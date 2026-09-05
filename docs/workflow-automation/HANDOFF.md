# Workflow Automation — Implementation Handoff

**Status:** planned · **Owner:** TBD · **Base:** `main` @ `87c84e8a`
**Visual plan (interactive):** https://claude.ai/code/artifact/84669b56-ec06-40f1-9e27-70e95f1e907c
**Proof-of-correctness plan:** see [`EVAL.md`](./EVAL.md) in this folder.

This document is self-contained: an engineer with no prior context can execute the whole
workflow-automation update from it. It pairs with `EVAL.md`, which proves each phase works.

---

## 1. Why

Running the 14-step weekly-journal workflow end-to-end (see `README.md`, `STEP_01`…`STEP_14`)
is sound in **structure** but heavy in **mechanics**: the same commit→push→label→comment ritual
repeats ~11× per cycle, several steps are hand-written Python each time, and a handful of tooling
rough-edges recur. This update scripts the mechanics and leaves every editorial decision and human
review gate exactly where it is.

**Guiding principle: automate the mechanics, never the judgment.** Theme identification, article
curation, annex selection, pattern choice, the editorial writing, and the three review gates
(STEP_03b themes, STEP_05 annex, STEP_07 assembly) stay human. Scripts only orchestrate plumbing
around them.

## 2. Tracking

| Issue | Scope | Phase |
|---|---|---|
| #201 #202 #203 | tooling bug fixes (shipped in **PR #208**, open/mergeable) | 0 |
| #204 | `sync_step.py` + shared `scripts/workflow/` lib | 1 |
| #205 | mechanical-step wrapper scripts | 2 |
| #209 | fold STEP_11 metadata into STEP_10 | 2 |
| #206 | STEP_08 assembly assist (stitch + prompt-gen) | 3 |
| #207 | workflow doc refinements | 4 |
| #210 | mid-cycle theme-revision spec | 4 |

## 3. Working conventions (apply to every phase)

- **One PR per phase**, based on `main`, reviewed independently. Branch names: `feat/workflow-p1-sync-step`, etc.
- **Python** runs via `uv run scripts/<name>.py`. New scripts live in `scripts/` (wrappers) and
  `scripts/workflow/` (the shared package).
- **Tests** are self-contained `unittest` files: `scripts/test_<name>.py`, runnable as
  `uv run scripts/test_<name>.py`. No pytest config; no network in tests.
- **Git auth is gh-cred HTTPS** (SSH is down on this machine):
  `GITHUB_TOKEN="" git -c credential.helper='!gh auth git-credential' <push|fetch> https://github.com/beijaflor/gen-ai-journal.git <ref>`
  `gh` CLI calls use the `GITHUB_TOKEN=""` prefix so they use the keyring auth.
- **Commit trailer** (end every commit message with):
  ```
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
  ```
- **Idempotent + `--dry-run`**: any script touching git/gh/Supabase must be safe to re-run and
  must support `--dry-run` (print the plan, mutate nothing). Live runs are interactive with a confirm.
- **The partition invariant is the backbone**: for any cycle,
  `main ∪ annex ∪ omitted = all sources`, pairwise disjoint. Every script that reshapes these sets
  re-asserts it (via `scripts/workflow/partition.py` once Phase 1 lands).

## 4. Existing pieces the scripts wrap (do not reinvent)

- `scripts/unite_summaries.py <sources.md> <summaries/> <out.md>` — aggregates summaries.
- `scripts/list_urls.py <file>` / `scripts/remove_urls.py <in> <out>` (stdin) — URL set ops.
- `scripts/export_curation_flags.py` — Supabase flags → curated/omitted files.
- `scripts/mark_published.py <date> [--all-null] [--yes]` — stamps Supabase `journal_date` (scoped).
- `scripts/bulk_add_links.py`, `scripts/bulk_summarize.py`, `scripts/call-gemini.py` — STEP_01/02.

The archived cycle `journals/2026-08-22/` is the **golden reference** used throughout `EVAL.md`.

---

## 5. Phase specs

Each phase lists: **files**, **behavior**, **acceptance criteria** (what "done" means), **tests**,
**dependencies**. Signatures are the target; adjust names if the repo already has a better fit.

### Phase 0 — Tooling bug fixes  *(shipped, PR #208 — reference only)*

Already implemented on branch `fix/workflow-tooling-rough-edges` (PR #208, open, mergeable):
- `scripts/remove_urls.py` — exact whole-URL match (extracted `filter_lines()`), fixes prefix-collision.
- `scripts/export_curation_flags.py` — always writes `omitted_sources.md`, even at 0 omits.
- `scripts/mark_published.py` — `--yes`/`-y` flag (extracted `parse_args()`).
- Tests: `test_remove_urls.py` (7), `test_export_curation_flags.py` (2), `test_mark_published.py` (6).

**Acceptance:** PR #208 merged. Phases 1–2 assume `--yes` and exact-match exist; if #208 is not yet
merged, rebase these phases on it or include the equivalents.

---

### Phase 1 — Foundation + `sync_step`  *(#204)*

The shared library everything reuses, and the one command that replaces the sync ritual.

**Files (new):**
- `scripts/workflow/__init__.py`
- `scripts/workflow/urls.py`
  - `URL_PATTERN` (the regex `list_urls.py` uses), `clean_url(u)`, `urls_in_line(line)`,
    `exact_filter(lines, remove_set) -> kept_lines`.
  - Refactor `scripts/list_urls.py` and `scripts/remove_urls.py` to import these (single source of the regex).
- `scripts/workflow/partition.py`
  - `read_ids(path) -> set[str]` (parses `- [ ] NNN. url` lines).
  - `assert_partition(all_ids, main, annex, omitted)` → raises `PartitionError` naming the exact
    overlap and/or missing IDs; returns None on success.
  - `verify(date, workdesk=Path('workdesk'))` → reads the curated files for a cycle and asserts.
- `scripts/workflow/git_gh.py`
  - `push(ref, *, dry_run=False)`, `ensure_label(name, *, color='ededed')`,
    `swap_label(issue, frm, to)`, `comment(issue, body)`.
  - All shell out through the gh-cred HTTPS pattern above; each honors `dry_run`.
- `scripts/workflow/journal_paths.py`
  - `Paths(date)` with `.dir` (`journals/2026-08-22`), `.weekly`/`.annex`/`.plan`
    (underscore filenames), `.summaries`, `.blob(name)` (the `blob/<date>/…` URL).

**Files (new script):**
- `scripts/sync_step.py`
  - CLI: `sync_step <NN> "<msg>" [files...] [--issue N] [--no-comment] [--dry-run]`.
  - Behavior: stage `files` (or all changed under `workdesk/`/`journals/`) → `git commit` with the
    trailer → `git_gh.push(current branch)` → `git_gh.ensure_label('step-<NN>')` →
    `git_gh.swap_label(issue, 'step-<prev>', 'step-<NN>')` → `git_gh.comment(issue, msg)`.
  - Idempotent (a no-op commit is skipped, not an error). `--dry-run` prints each action, mutates nothing.

**Acceptance:**
- `list_urls`/`remove_urls` behavior unchanged (their existing/added tests pass) but now import `urls.py`.
- `partition.verify('2026-08-22')` passes on the archived golden cycle and raises on an injected overlap.
- `sync_step … --dry-run` prints a correct plan and makes no git/gh calls (assert via mocked runner).

**Tests:** `test_workflow_urls.py`, `test_workflow_partition.py` (clean / overlap / gap),
`test_sync_step.py` (arg parse + dry-run plan; `git_gh` runner monkeypatched).

**Dependencies:** none (goes first). **Unblocks:** Phases 2–3, and #210's guardrail.

---

### Phase 2 — Mechanical-step scripts  *(#205 + #209)*

Each deterministic step becomes one idempotent script; all reuse Phase-1 lib.

**Files (new):**
- `scripts/build_focused.py <date>`  *(STEP_06)*
  - 3× `unite_summaries`: `curated_journal_sources.md`→`unified_summaries_main.md`;
    `curated_annex_selected.md`→`unified_summaries_annex.md`;
    `omitted_urls.md`→`omitted_summaries_unified.md`. Then `partition.verify`.
- `scripts/verify_journal.py <date>`  *(STEP_09; verify-only, exit-code)*
  - Concurrent URL health over the two journals' source URLs (200 / known-403 list / broken);
    coverage (参考リンク IDs == curated; every curated source URL present as plain text);
    leak scan (no `原題`/score-objects in the weekly; no `news.ycombinator`/`web.archive.org`/`fortune.com`);
    heading-hierarchy counts; encoding (`U+FFFD`, control chars). Non-zero exit on any real failure.
- `scripts/archive_journal.py <date> [--dry-run]`  *(STEP_10 **+** STEP_11 via #209)*
  - mkdir `journals/<date>/{sources,summaries}`; copy `00/01/50` (underscore names) + the 6 `sources/`
    files + all `summaries/*.json`; build `99_unified_summaries.md` and `02_omitted_summaries.md`
    **fresh from JSON in Python** (format: `## {id_domain}` / `**title**` / `出典: url` / body / `---`);
    write + validate `journal-metadata.json` (`total`/`main`/`annex`/`omitted`, counted from the
    assembled `00/01` files, asserting `main+annex+omitted==total`); `mark_published --yes <date>`;
    clean `workdesk` with `git rm` (bulk `rm` is blocked by the sandbox classifier) → leave `.gitkeep`.
- `scripts/release_journal.py <date> [--dry-run]`  *(STEP_13/14)*
  - Verify PR merged (`gh pr view`); ff local `main`; annotated tag `<date>`; delete the feature branch;
    create a **draft** GitHub release from the 2-section template (compute the Japanese 曜日);
    verify the 6 links (3 GitHub-Pages + 3 `blob/<date>/…`).

**Also:** deprecate `STEP_11_GENERATE_METADATA.md` (its work now lives in `archive_journal.py`);
update `STEP_10_CLEANUP.md` to call the script.

**Acceptance:**
- `build_focused 2026-08-22` reproduces the archived `unified_summaries_{main,annex}.md` +
  `omitted_summaries_unified.md` counts (40 / 34 / 119) and passes `partition.verify`.
- `verify_journal 2026-08-22` exits 0 on the golden journal (matching the STEP_09 record:
  73×200 / 1×403 openai / 0 broken).
- `archive_journal 2026-08-22 --dry-run` prints a plan whose file set equals the archived tree;
  a real run into a temp dir reproduces `journals/2026-08-22/` byte-for-byte for `00/01/50/sources/summaries`
  and semantically for `99/02` (same entries), and produces the same `journal-metadata.json`.
- `release_journal … --dry-run` prints the correct tag + release body + 6 URLs.

**Tests:** `test_build_focused.py`, `test_verify_journal.py` (fixture journal: a good one passes, a
seeded leak/broken-link/hierarchy fault fails), `test_archive_metadata.py` (99/02 builder + metadata
math on a fixture), plus dry-run plan assertions for archive/release.

**Dependencies:** Phase 1 (partition, journal_paths, git_gh, mark_published `--yes`).

---

### Phase 3 — Assembly assist  *(#206)*

Automate STEP_08's scaffolding; the editorial writing stays with the subagents.

**Files (new):**
- `scripts/gen_writer_prompts.py <date>`
  - Read `curated_journal_sources.md` (themes + IDs) and `editorial_plan_<date>.md`
    (each theme's intro + its `## ASSEMBLY STRATEGIES` block); resolve `summaries/NNN_*.json` per ID.
  - Emit, to `scratchpad/`, the ~N theme-writer + M annex-section-writer prompts, each carrying the
    format-spec path, the theme intro + assembly strategy, the article JSON paths, and the output path.
    (The dispatch itself stays with the orchestrator — or a Workflow, per decision 4.)
- `scripts/stitch_qa.py <date>`
  - Concatenate `scratchpad/{main_theme_N,annex_sec_N}.md` + orchestrator-written header / ハイライト /
    おわりに / annex header / 編集後記 in order → `weekly_journal_<date>.md`, `annex_journal_<date>.md`.
  - Run the full QA (same checks as `verify_journal` but on the assembled files pre-archive):
    参考リンク IDs == curated, metadata/recovery-URL leak, hierarchy, encoding. Non-zero exit on fault.

**Acceptance:** `stitch_qa` on the golden cycle's scratchpad reproduces the archived `00/01` structure
(9 themes/40, 5 sections/34) and passes QA; `gen_writer_prompts` output is stable (snapshot) for the
golden `editorial_plan`.

**Tests:** `test_stitch_qa.py` (fixture assembled journal passes; seeded leak fails),
`test_gen_writer_prompts.py` (snapshot vs a committed fixture plan).

**Dependencies:** Phase 1 (partition/paths). **Decision 4** governs manual-dispatch vs a Workflow.

---

### Phase 4 — Docs + revision spec  *(#207 + #210)*  — docs only, runs last

**#207 — doc refinements** (edit the STEP files + skill + CLAUDE.md to match reality):
- `human-review-gate` skill + `STEP_03b`/`STEP_05`/`STEP_07`: document the **Zed / AskUserQuestion**
  gate path as first-class (tmux is the exception, not the default).
- `STEP_04`: change the target from "18–25 articles" to "~30–40 across 6–9 themes".
- `STEP_08`: adjust theme-count guidance (weekly up to ~9, annex ~5–6) to observed ranges.
- `STEP_10`: replace the jq loop for `99/02` with the Python builder; use `git rm` not bulk `rm`;
  note underscore-filename vs hyphen-dir; note `mark_published --yes`.
- Add a note that the editorial plan's "Identified Themes" article lists go **stale** after STEP_04
  trims — STEP_08 writers use `curated_journal_sources.md`, not the plan's candidate lists.
- Insert the new script commands (`sync_step`, `build_focused`, `verify_journal`, `archive_journal`,
  `release_journal`) into each relevant step.

**#210 — mid-cycle theme-revision spec** (new doc, e.g. `STEP_04b_THEME_REVISION.md` or an appendix):
- Trigger → **re-scan the whole corpus** for siblings (not just the spotted 1–2) → re-gate (numbered
  round) → **fixed cascade order**: (a) add theme to `editorial_plan`; (b) add articles to
  `curated_journal_sources.md`; (c) **remove them from the annex pool/selected**; (d) regenerate
  `non_main_sources.md` (+ `non_main_unified` if past STEP_05); (e) **re-assert the partition**.
  Mirror for demotion (main→annex).
- Guardrail: step (e) calls `scripts/workflow/partition.py`, so the invariant can't silently break.

**Acceptance:** docs build/read cleanly; the revision spec's cascade is executable by following it; a
reviewer can trace the 2026-08-22 book-destruction promotion (068/110 → +052/075) against the spec.

**Dependencies:** Phase 1 (`partition.py` for the guardrail). Runs last so it documents Phases 1–3.

---

## 6. Sequencing & open decisions

```
Phase 0 (PR #208, merge anytime) → Phase 1 → Phase 2 → Phase 3 → Phase 4
```
Phases 2–3 depend on the Phase-1 lib; Phase 4 documents them. **Four calls needed before Phase 1:**

1. **Shared lib** `scripts/workflow/`? (recommended: yes — kills the duplicated-regex bug class and hosts the guardrail.)
2. **One PR per phase** (recommended) vs one mega-PR.
3. **git/gh/Supabase scripts default to live-with-confirm** (recommended) vs `--dry-run` by default.
4. **STEP_08 dispatch:** keep manual orchestration vs a `Workflow` script (parallel/resumable, more tokens, opt-in).

## 7. Definition of done (overall)

- All phase PRs merged; every `scripts/test_*.py` green.
- The golden-cycle checks in `EVAL.md` pass (the scripts reproduce `journals/2026-08-22/`).
- The next real cycle runs end-to-end using the scripts, producing a journal that passes `verify_journal`
  with the human gates and editorial judgment unchanged.
- STEP docs match the scripted workflow; 14 → 13 steps (metadata folded into STEP_10).
