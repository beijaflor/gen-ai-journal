# Kickoff prompt (`/goal`)

Paste the block below into `/goal` to drive the implementation. Decisions are resolved and baked in
(sub-PR per phase into the feature branch; shared lib; scripts run live with `--dry-run` available;
all four phases then report). It points the agent at [`HANDOFF.md`](./HANDOFF.md) (the spec) and
[`EVAL.md`](./EVAL.md) (the proof).

**State when this was written:** `experimental-workflow-improvement` is branched off `main`; Phase 0
(the PR #208 tooling fixes) is already merged into it. Implementation starts at Phase 1.

---

```
/goal Build the journal-workflow automation onto the integration branch
`experimental-workflow-improvement` (already branched off main; Phase 0 tooling fixes from PR #208 are
already merged into it). Implement Phases 1–4 from docs/workflow-automation/HANDOFF.md, proving each
against docs/workflow-automation/EVAL.md.

Branching model: each phase is its own branch off experimental-workflow-improvement, opened as a PR
INTO experimental-workflow-improvement, and merged once its tests + the EVAL.md golden checks pass. Do
NOT target main — the whole feature branch PRs to main once, at the very end.

Phases (in order; 2–4 depend on Phase 1's lib):
- Phase 1 (#204): scripts/workflow/ shared lib — urls.py, partition.py, git_gh.py, journal_paths.py —
  plus sync_step.py. Refactor list_urls.py and remove_urls.py to import urls.py. Unit tests for each.
- Phase 2 (#205 + #209): build_focused.py, verify_journal.py, archive_journal.py (fold STEP_11 metadata
  in via #209), release_journal.py — idempotent, with --dry-run. Deprecate STEP_11_GENERATE_METADATA.md;
  update STEP_10 to call archive_journal.py.
- Phase 3 (#206): gen_writer_prompts.py + stitch_qa.py. (The subagent dispatch stays a runtime choice —
  build the scripts either way.)
- Phase 4 (#207 + #210): STEP-doc refinements + a mid-cycle theme-revision spec (annex<->main).

Conventions:
- Shared lib scripts/workflow/. git/gh/Supabase scripts run LIVE with an interactive confirm and a
  --dry-run flag available.
- Automate mechanics only; never touch editorial judgment or the three human review gates
  (STEP_03b themes, STEP_05 annex, STEP_07 assembly).
- Enforce the partition invariant (main + annex + omitted = all sources, pairwise disjoint) via
  scripts/workflow/partition.py wherever these sets are reshaped.
- uv run for scripts; tests are self-contained unittest files scripts/test_*.py; commit trailer
  "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"; push/fetch via gh-cred HTTPS
  (GITHUB_TOKEN="" git -c credential.helper='!gh auth git-credential' ...), since SSH is down.

Autonomy: implement all four phases, then report once. Run the EVAL.md golden reproduction against the
published cycle journals/2026-08-22/ (main/annex/omitted = 40/34/119; verify_journal exit 0:
73x200 / 1x403 / 0 broken; 0 leaks) read-only into temp dirs; every --dry-run must make zero mutations.

Definition of done: all scripts/test_*.py green; the golden checks pass; docs match the scripted
workflow (14 -> 13 steps after the STEP_11 fold); each phase merged into experimental-workflow-improvement.
```

---

## Variant — one phase at a time

If you'd rather drive a single phase, use its line as the goal, e.g. Phase 1:

```
/goal Implement Phase 1 (#204) from docs/workflow-automation/HANDOFF.md onto a branch off
experimental-workflow-improvement, PR'd back into it: the scripts/workflow/ shared library
(urls, partition, git_gh, journal_paths) and sync_step.py, refactoring list_urls/remove_urls onto
urls.py. Add unit tests (scripts/test_workflow_*.py, test_sync_step.py). Prove it per EVAL.md §4 Phase 1:
partition.verify('2026-08-22') passes, an injected overlap raises, sync_step --dry-run makes zero
git/gh calls. Automate mechanics only; do not touch editorial judgment or the review gates.
```
