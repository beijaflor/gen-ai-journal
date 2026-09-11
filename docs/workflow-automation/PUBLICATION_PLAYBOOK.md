# Publication Automation Playbook

Operational lessons for running the scripted journal cycle, captured from the
2026-08-29 and 2026-09-05 cycles. These are corrections and refinements to the
STEP docs and skills — read them alongside the per-step docs, not instead of them.

## QA: schema-valid is not the same as correct

`validate_summary.py` only checks the JSON **schema**. Four things it does *not*
check, that must be verified separately (see the post-generation QA checklist in
`.claude/skills/summarize-source/SKILL.md`):

1. **Not a dead link (404).** `verify_urls.py` / `check_link.py`. A 401/403 is
   usually a paywall or anti-bot wall, **not** a dead link.
2. **Title matches the original article.** Cross-check the page's real `<title>`
   against the summary's `title`/`originalTitle`; a domain-name-shaped title
   ("Qiitaの記事") means the fetch failed.
3. **Not paywall/anti-bot blocked.** `summary_review.py --only-suspicious` +
   an interstitial-signature grep.
4. **summaryBody renders cleanly.** Run **`scripts/check_summary_format.py`** —
   schema validation misses literal-`\n`, mid-line `###`, and mashed one-line
   markdown. In the 2026-08-29 cycle this class hit **13** summaries that all
   passed schema validation.

## Retry in a real browser before declaring "blocked"

A cold-session `curl`/headless fetch can get a **transient 403** from a page
that loads fine in a real browser (this cycle: the NYT article was filed as
"blocked" on the first fetch, then loaded normally on retry). Before writing a
`BLOCKED-*` stub or omitting a source, retry via the Playwright MCP browser
(`navigate` → `() => document.body.innerText`) and feed the captured text back
with `call-gemini.py --url <URL> --content <captured.txt>`. Only genuinely gated
bodies (FT "Subscribe to read", a persistent NYT 403) stay blocked.

## Dedup catches redirect-aliases, not just exact strings

Two different URLs can be the **same article** (this cycle: the Gates essay at a
long `/reader/…` path and its short-URL alias resolved to the same page and
title). Exact-string dedup misses these. When two sources share a title/canonical
after fetching, keep one and remove/omit the other — and prefer *removing* a true
duplicate from the source pool over carrying it as an omitted entry.

## Rebuild 99/02 with archive_journal, never standalone

`archive_journal.py`'s `build_99`/`build_02` are the canonical builders
(sorted-by-ID, fixed formatting). Rebuilding `99_unified_summaries.md` with a
standalone `unite_summaries.py` call formats/orders entries differently and
produces a ~900-line churn diff. After editing any summary in an archived cycle,
regenerate 99/02 by **re-running `archive_journal.py`**, not `unite_summaries`.

## archive_journal does not prune deleted summaries (gotcha)

`archive_journal.py` copies `workdesk/summaries/` into the archive and rebuilds
metadata from the archive's file count — but it does **not** delete summaries
that were removed. After removing a source (e.g. a duplicate), delete the stale
`journals/<date>/summaries/<id>_*.json` **before** re-archiving, or the metadata
`total` will exceed `main+annex+omitted` and the run aborts on the math check.
*(Follow-up: teach `archive_journal.py` to prune to match the sources set.)*

## Keep the journal PR clean of tooling (stack instead)

A journal branch cut from the workflow-tooling branch carries the entire tooling
delta in its PR diff. Keep the publication PR focused on `journals/<date>/`:

- Land the tooling via its own umbrella PR to `main` first.
- Then **merge `main` into the journal branch** — this dedups the tooling out of
  the journal PR's diff, leaving it journal-only.
- Going forward, **stack** the next journal branch on top of the pending tooling
  branch so the dependency is explicit, and rebase onto `main` once the tooling
  lands.

## Create a per-cycle tracking issue

Past cycles have a `Journal Workflow - Week of <date>` issue (#194, #196, #198…).
An autonomous run that uses the draft PR as the `sync_step --issue` target skips
this. Create the tracking issue at STEP_01 for consistency and cross-link the PR,
tag, and release to it.

## Editorial notes reaffirmed this cycle

- **Theme structure can change at Gate 2.** The human may restructure themes
  after STEP_03b approval (this cycle: split off local-LLM-execution and
  org-adoption as main themes, moved infra to annex). Handle as numbered rounds
  and cascade through STEP_04/05.
- **Annex sizing:** when asked to trim, rank candidates by confidence and show
  the low-confidence tail for the curator to cut; defer to the curator's section
  organization rather than a fixed count.
- **Present articles as-is** in theme intros; do not manufacture narrative.
  Anchor satirical/thought-experiment pieces on the thesis, not the hook.

---

## Lessons from the 2026-09-05 cycle

### A schema-invalid summary silently 404s the site — now gated in verify_journal

The website's `json-v1` parser **silently drops** any summary that fails v1.0
validation; its `/journals/<date>/<id>/` page then **404s with no error** ("the
article doesn't show up"). The schema requires, in `content`:
`title, url, language (enum), contentType (enum), oneSentenceSummary,
summaryBody (100–1200 chars), topics (1–5), scores{signal,depth,uniqueness,
practical,antiHype 0–5; mainJournal,annexPotential,overall 0–100}`. Any summary
written **outside `validate_summary.py`** can miss these — hand-made blocked-source
stubs are the usual offenders (this cycle: 049/055/223 stubs lacked
`language/contentType/topics/scores` and had a <100-char body, so all three pages
404'd). Fix: **`verify_journal.py` now runs the v1.0 validator on every summary**
(new gate `schema: all summaries valid v1.0`), so an incomplete summary fails the
pre-archive check instead of on the live site. **Never hand-write a summary JSON
without running `scripts/validate_summary.py` on it.**

### Blocked/omit sources: recover → replace → drop, never fabricate a stub

`validate_summary.py` checks **structure, not truth**: a placeholder that invents
`contentType`/`topics`/zeroed `scores` *passes* validation while being
semantically empty. So don't leave fabricated stubs. In order of preference:

1. **Recover** the text in a real browser (Playwright MCP `navigate` →
   `() => document.body.innerText`), feed via
   `call-gemini.py --url <URL> --content <captured.txt>`. This cycle recovered 8
   pages this way (JS-rendered SPA shells: LessWrong, OpenAI; paywall *teasers*
   that still carry the thesis: Economist, Springer).
2. **Replace** with an accessible source on the same story. Find an HN thread by
   URL via the Algolia API:
   `https://hn.algolia.com/api/v1/search?query=<url-or-slug>&restrictSearchableAttributes=url&tags=story`
   (NYT school-AI-ban → a 220-pt HN thread, kept as a **main** source); or swap
   outlets (FT's paywalled "Astra = AGI" → TechCrunch's accessible coverage).
3. **Drop** the source if its story is already covered elsewhere (this cycle the
   empty FT→HN thread was removed once the FT was replaced; deleting a source
   means: summary file + `sources.md`/`omitted_sources.md`/`non_main_sources.md`
   lines + Supabase row + metadata counts, then rebuild 99/02).

### Cloudflare challenge pages get summarized *as* the article

uxdesign.cc / medium.com front articles with a `cf-mitigated: challenge`. The
block page carries enough text to clear the length threshold, so it is summarized
as if it were the article — tell-tale title like
"Cloudflareによるアクセス制限の通知". The Playwright auto-fallback only fires
*under* the char threshold, so these pass schema-valid and slip through. Detect by
the interstitial title/signature and re-fetch via the Playwright MCP. (This cycle:
4 uxdesign/medium summaries were block-page artifacts, recovered on retry.)

### verify_journal: HN-leak false-positive, and coverage catches corruption

- **HN "recovery-host" leak is a false-positive for a deliberate HN main source.**
  When a blocked primary is intentionally replaced by its HN discussion *as a main
  article* (this cycle: NYT → its 220-pt thread), the hard-coded `news.ycombinator`
  leak rule flags it. Decide per case: keep and accept the flag (document it), move
  the HN source to the annex (rule not enforced there), or swap to a primary URL.
  *(Follow-up: allowlist an HN URL that is a curated main source.)*
- **Coverage catches content corruption, not just missing articles.** The
  `every curated main URL present in weekly` check surfaced a stray-keystroke edit
  this cycle — an editor artifact had overwritten one article's URL line in
  `00_weekly` with a single character, dropping its URL. Re-run `verify_journal.py`
  after any manual edit to an archived journal; the coverage + schema gates catch
  corruption a visual skim misses.

### git push fallback when the ssh-agent drops its key

If `git push` to an `ssh://`/`git@` remote starts failing with
`Permission denied (publickey)` / `Could not read from remote repository` mid-session,
check `ssh-add -l` (often "The agent has no identities" after an idle/refresh).
Push over HTTPS with the keyring instead:
`GITHUB_TOKEN="" git push https://github.com/<owner>/<repo>.git <branch>`. Note this
does **not** update the local `origin/<branch>` tracking ref, so `git status` may
show a false "unpushed" — confirm the real remote state with
`git ls-remote https://github.com/<owner>/<repo>.git <branch>`.
