# Publication Automation Playbook

Operational lessons for running the scripted journal cycle, captured from the
2026-08-29 cycle. These are corrections and refinements to the STEP docs and
skills — read them alongside the per-step docs, not instead of them.

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
