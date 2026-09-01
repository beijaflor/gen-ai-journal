# Kickoff prompt (`/goal`)

Paste this into `/goal` to drive the implementation. It is intentionally self-contained
and points the agent at [`HANDOFF.md`](./HANDOFF.md) (the spec) and [`EVAL.md`](./EVAL.md) (the proof).

---

```
/goal Implement the journal-workflow automation in docs/workflow-automation/HANDOFF.md, one phase at a
time, proving each phase against docs/workflow-automation/EVAL.md before opening its PR.

Order (each is one PR off latest main):
- Phase 1 (#204): scripts/workflow/ shared lib — urls.py, partition.py, git_gh.py, journal_paths.py —
  plus sync_step.py. Refactor list_urls.py and remove_urls.py to import urls.py. Unit tests for each.
- Phase 2 (#205 + #209): build_focused.py, verify_journal.py, archive_journal.py (fold STEP_11 metadata
  in via #209), release_journal.py. Every git/gh/Supabase script is idempotent and supports --dry-run.
  Deprecate STEP_11_GENERATE_METADATA.md; update STEP_10 to call archive_journal.py.
- Phase 3 (#206): gen_writer_prompts.py + stitch_qa.py.
- Phase 4 (#207 + #210): STEP-doc refinements + a mid-cycle theme-revision spec (annex<->main).

Hard rules:
- Automate mechanics only. Never touch editorial judgment or the three human review gates
  (STEP_03b themes, STEP_05 annex, STEP_07 assembly).
- Enforce the partition invariant (main + annex + omitted = all sources, pairwise disjoint) via
  scripts/workflow/partition.py wherever these sets are reshaped.
- Conventions: uv run for scripts; tests are self-contained unittest files scripts/test_*.py; commit
  trailer "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"; git push/fetch via gh-cred HTTPS
  (GITHUB_TOKEN="" git -c credential.helper='!gh auth git-credential' ... ) since SSH is down.

Proof / definition of done (per EVAL.md):
- All scripts/test_*.py green (new + existing, no regressions).
- The scripts reproduce the golden published cycle journals/2026-08-22/ (main/annex/omitted = 40/34/119,
  verify_journal exit 0: 73x200 / 1x403 / 0 broken, 0 leaks), running read-only into temp dirs.
- Every --dry-run makes zero mutations.
- Docs match the scripted workflow (14 -> 13 steps after the STEP_11 fold).

Before starting Phase 1, confirm the four decisions in HANDOFF.md section 6:
(1) shared lib scripts/workflow/? (2) one PR per phase? (3) git/gh scripts live-with-confirm vs
--dry-run by default? (4) STEP_08 dispatch: manual orchestration vs a Workflow script?
```

---

## Variant — per-phase goals

If you'd rather drive one phase at a time, use the phase line above as its own goal, e.g.:

```
/goal Implement Phase 1 (#204) from docs/workflow-automation/HANDOFF.md: the scripts/workflow/ shared
library (urls, partition, git_gh, journal_paths) and sync_step.py, refactoring list_urls/remove_urls
onto urls.py. Add unit tests (scripts/test_workflow_*.py, test_sync_step.py). Prove it with EVAL.md
section 4 Phase 1: partition.verify('2026-08-22') passes, injected overlap raises, sync_step --dry-run
makes zero git/gh calls. Open one PR off main. Do not touch editorial judgment or the review gates.
```
