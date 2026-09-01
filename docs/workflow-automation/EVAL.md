# Workflow Automation — Evaluation & Proof

**Pairs with:** [`HANDOFF.md`](./HANDOFF.md) · **Visual plan:** https://claude.ai/code/artifact/84669b56-ec06-40f1-9e27-70e95f1e907c

This document defines how we **prove** the automation works before trusting it on a live cycle.
Nothing here mutates production: reproductions run into a temp dir, and every git/gh/Supabase path is
exercised in `--dry-run`.

---

## 1. Strategy

Four layers of evidence, strongest last:

1. **Unit tests** — pure logic per module (`uv run scripts/test_*.py`), no I/O beyond temp files.
2. **Dry-run safety** — the git/gh/Supabase scripts print a correct plan and make **zero** mutations.
3. **Golden-fixture reproduction** — run the new scripts against the inputs of a **known-good, already
   published** cycle and assert the outputs match what was produced by hand.
4. **End-to-end replay** — a full-cycle dry run wiring the scripts together, asserting the partition
   invariant and QA hold at every hand-off.

The golden fixture is the real, published cycle **`journals/2026-08-22/`**. Because it was assembled,
verified, archived, and released by hand and is live on the site, "the script reproduces it" is direct
proof the script does the human's job correctly.

## 2. Golden reference — `journals/2026-08-22/`

| Fact | Value | Where it's checked |
|---|---|---|
| Total sources / summaries | **193** | archive `summaries/*.json` count |
| Main / Annex / Omitted | **40 / 34 / 119** (sum 193) | `journal-metadata.json`, partition |
| Main themes / Annex sections | **9 / 5** | `## ` headings in `00`/`01` |
| Weekly headings | `#`×1, `##`×11, `###`×40, `####`×9 | `verify_journal` |
| Annex headings | `#`×1, `##`×7, `###`×34 | `verify_journal` |
| URL health (77 curated URLs) | **73×200, 1×403** (openai anti-bot), 0 broken | `verify_journal` |
| Metadata leaks / recovery-URL leaks / encoding | 0 / 0 / 0 | `verify_journal` |
| `mark_published 2026-08-22` | 193/193 rows | (scoped; **do not** re-run on prod in eval) |

These numbers are the pass/fail oracle for the golden reproductions below.

## 3. Fixtures

- **`journals/2026-08-22/`** — the committed golden cycle (inputs **and** expected outputs).
- **`tests/fixtures/mini-journal/`** *(new, small)* — a hand-built 6-source micro-cycle
  (2 main / 2 annex / 2 omitted, 2 themes) used by fast unit/integration tests so they need no network
  and run in <1s. Include one deliberately-faulty variant per check (a metadata leak, a broken internal
  link, a partition overlap) to prove the checks actually **fail** when they should.

---

## 4. Per-phase eval

### Phase 0 — tooling fixes  *(PR #208)*
```
uv run scripts/test_remove_urls.py          # 7 tests, incl. prefix-collision regression
uv run scripts/test_export_curation_flags.py # 2 tests, incl. 0-omit writes file
uv run scripts/test_mark_published.py        # 6 tests, --yes/-y parse
uv run scripts/test_sanitize_url.py && uv run scripts/test_canonicalize_url.py  # no regression
```
**Pass:** all green. **Golden check:** on the 2026-08-22 `sources.md`, `list_urls curated | remove_urls`
yields exactly **153** non-main URLs (matches the archived `sources/non_main_sources.md`), and the
HF-variant prefix pair is not mis-dropped.

### Phase 1 — foundation + `sync_step`  *(#204)*
```
uv run scripts/test_workflow_urls.py
uv run scripts/test_workflow_partition.py    # clean passes; overlap & gap raise PartitionError
uv run scripts/test_sync_step.py             # arg-parse + dry-run plan; git_gh runner mocked
uv run scripts/list_urls.py <f> ; uv run scripts/remove_urls.py ...   # unchanged behavior after refactor
```
**Golden checks:**
- `python -c "from scripts.workflow import partition; partition.verify('2026-08-22')"` → **passes**
  (40 ∩ 34 ∩ 119 = ∅, union = 193). Inject a duplicate ID into a copy → **raises**, naming the ID.
- `uv run scripts/sync_step.py 06 "test" --dry-run` prints stage/commit/push/label/comment steps and
  the mocked runner records **0** real git/gh invocations.

### Phase 2 — mechanical scripts  *(#205 + #209)*
Reproduce into a temp dir, compare to the archived golden (never touch the real archive):
```
# focused summaries (STEP_06) — from the golden cycle's curated inputs
uv run scripts/build_focused.py 2026-08-22 --out /tmp/eval06
diff <(grep -c '^## ' /tmp/eval06/unified_summaries_main.md)  <(echo 40)
diff <(grep -c '^## ' /tmp/eval06/unified_summaries_annex.md) <(echo 34)
diff <(grep -c '^## ' /tmp/eval06/omitted_summaries_unified.md) <(echo 119)

# verify (STEP_09) — on the golden journals
uv run scripts/verify_journal.py 2026-08-22      # exit 0; report: 73×200 / 1×403 / 0 broken; 0 leaks
#   then run against tests/fixtures/mini-journal/faulty → exit non-zero (proves it catches faults)

# archive + metadata (STEP_10 + #209) — into a temp dir
uv run scripts/archive_journal.py 2026-08-22 --into /tmp/eval10 --dry-run   # plan == archived file set
uv run scripts/archive_journal.py 2026-08-22 --into /tmp/eval10            # real run, temp target
diff -r /tmp/eval10/2026-08-22/00_weekly_journal_2026_08_22.md journals/2026-08-22/00_...   # identical
diff /tmp/eval10/2026-08-22/journal-metadata.json journals/2026-08-22/journal-metadata.json # identical
#   99/02: assert every archived '## NNN_domain' header is reproduced and counts are 193 / 119

# release (STEP_13/14) — dry-run only
uv run scripts/release_journal.py 2026-08-22 --dry-run   # tag=2026-08-22; body = 2 sections; 6 URLs listed
```
**Pass:** copied files byte-identical; `99/02` semantically identical (same entries, same order);
`journal-metadata.json` identical (`{193,40,34,119}`); `verify_journal` exit 0 on golden and non-zero on
the faulty fixture; every dry-run makes zero mutations. **`--into`/`--out` are eval-only flags** so the
real archive is never overwritten.

### Phase 3 — assembly assist  *(#206)*
```
uv run scripts/stitch_qa.py 2026-08-22 --scratch tests/fixtures/2026-08-22-scratch --out /tmp/eval08
#   → reproduces 9 themes/40 (## ×11, ### ×40, 参考リンク ×9) and 5 sections/34; QA exit 0
uv run scripts/test_gen_writer_prompts.py   # snapshot vs a committed fixture editorial_plan
```
(The golden cycle's per-theme scratchpad drafts are committed under the fixture path so stitch is
reproducible without re-running the writer subagents.)
**Pass:** stitched structure matches the archived `00/01`; QA exit 0; prompt-gen snapshot stable.

### Phase 4 — docs + revision spec  *(#207 + #210)*
Docs have no runtime, so the eval is a review checklist:
- Every STEP doc that names a scripted step shows the `uv run scripts/<name>.py` command.
- STEP_04 target reads ~30–40 / 6–9 themes; STEP_10 shows the Python 99/02 builder + `git rm` + `--yes`.
- The revision spec's 5-step cascade is followed to re-derive the 2026-08-22 book-destruction promotion
  (068/110 → +052/075) on a scratch copy; `partition.verify` passes after step (e). Demotion mirror likewise.

---

## 5. End-to-end replay (full cycle, dry)

A single harness stitches the scripts in order against the golden cycle's committed inputs, into temp
dirs, asserting the invariant at each hand-off:
```
uv run scripts/eval_golden.py 2026-08-22     # (optional harness) runs 06→09→10(dry)→13/14(dry)
```
It asserts, in sequence: partition after STEP_06 = {40,34,119}; `verify_journal` exit 0; archive dry-run
plan == archived tree; release dry-run body + links correct. Any deviation from the golden numbers fails
the run with a diff. This is the closest thing to "run the whole pipeline and prove it still lands the
same published journal" without mutating anything.

## 6. Regression guarantees

- **URL set ops:** `list_urls`/`remove_urls` refactored to `scripts/workflow/urls.py` keep identical
  output on the golden `sources.md` (non_main == 153); the prefix-collision case is a permanent test.
- **Partition invariant** holds at STEP_04/05/06/10 and after any #210 revision — enforced by
  `partition.py`, not by memory.
- **QA parity:** `verify_journal` and `stitch_qa` run the *same* checks the human ran this cycle
  (link-IDs, leak scan, hierarchy, encoding); the golden journal passing them is the parity proof.
- **No editorial drift:** the scripts touch only mechanical outputs; the themed/curated/assembled
  content is unchanged (the golden `00/01` reproduce exactly).

## 7. Safety evals (must all hold)

- Every git/gh/Supabase script in `--dry-run` performs **0** mutations (asserted via a mocked runner
  that records calls).
- `archive_journal`/`stitch_qa`/`build_focused` write only to their `--into`/`--out`/temp targets in eval
  mode; the real `journals/`, `workdesk/`, and Supabase are never written during eval.
- `mark_published` stays **scoped** (URL-matched to this date) — its blanket `--all-null` path is never
  used in eval and is not invoked by `archive_journal`.

## 8. Merge gate (per phase PR)

A phase PR merges only when:
1. all `scripts/test_*.py` are green (new + existing, no regressions), and
2. the phase's **golden checks** in §4 pass, and
3. every `--dry-run` shows zero mutations, and
4. `EVAL.md` §5 end-to-end replay still reproduces the golden numbers.

## 9. Running the whole eval

```
# fast: unit + fixtures (no network)
for t in scripts/test_*.py; do uv run "$t" || exit 1; done

# golden reproductions (read-only against journals/2026-08-22, temp outputs)
uv run scripts/build_focused.py  2026-08-22 --out  /tmp/eval06
uv run scripts/verify_journal.py 2026-08-22
uv run scripts/archive_journal.py 2026-08-22 --into /tmp/eval10 --dry-run
uv run scripts/release_journal.py 2026-08-22 --dry-run
# (optional) uv run scripts/eval_golden.py 2026-08-22
```
Green across all of the above = the automation reproduces a real published cycle, the invariant holds,
and nothing mutates outside temp — sufficient proof to run it live on the next journal.
