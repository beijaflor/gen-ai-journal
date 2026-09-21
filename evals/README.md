# Prompt Evaluation Harness (promptfoo)

Offline evaluation for `prompts/summarize-json.prompt` — the repo's one
LLM surface. Implements the Evaluation component of the LLMOps loop:
deterministic assertions (Layer ①) on every fixture, LLM-as-a-Judge
rubrics (Layer ②) on a curated subset, and human calibration of the
judge (Layer ③). Replaces the hand-rolled `experiments/` A/B process.

Prompts are rendered through the **production assembly path**
(`_build_url_mode_prompt_with_text` in `scripts/call-gemini.py`, loaded
via `lib/call_gemini_bridge.py`), so what the eval sends is byte-identical
to production. `tests/test_promptfoo_bridge.py` guards that parity.

## One-time setup (per machine)

```bash
uv sync                                   # repo .venv (assertions/prompt fns run in it)
cd evals && npm install && cd ..          # pins promptfoo
export GEMINI_API_KEY=...                 # already required by the pipeline
```

promptfoo's google provider reads `GOOGLE_API_KEY` by default; the
configs set `apiKeyEnvar: GEMINI_API_KEY`, but if your promptfoo version
ignores it, bridge with: `export GOOGLE_API_KEY="$GEMINI_API_KEY"`.

Fixtures and `response-schema.json` are committed — nothing else is
needed. Regenerate the schema copy only when `get_gemini_schema()`
changes:

```bash
uv run evals/tools/gen_response_schema.py
```

## Workflows

### A — Regression check

When you touch anything prompt-adjacent (`criteria/*.md`,
`EDITOR_PERSONALITY.md`, `schema/`) and want to confirm nothing broke:

```bash
cd evals && npm run eval && npm run view
```

~11 Gemini calls, ~1.5 min (2 s on a cached rerun). Hard assertions
(schema, enums, originalTitle invariant) should stay green; compare the
soft metrics against the baseline (2026-07-29, gemini-3-flash-preview:
`url_fidelity` ≈ 4/11, `hallucination_clean` ≈ 9/11).

### B — Prompt experiment (A/B compare)

The candidate file is your local workbench — `evals/candidates/` is
gitignored and never committed; only the winning change to
`prompts/summarize-json.prompt` gets PR'd.

```bash
mkdir -p evals/candidates    # first time on a machine
cp prompts/summarize-json.prompt evals/candidates/summarize-json.candidate.prompt
# …edit the candidate…
cd evals && npm run eval:compare && npm run view
```

The `view` UI shows current vs candidate as two columns over the same
fixtures — per-fixture pass/fail and named metrics side by side.
Iterate and re-run: only the candidate column re-hits the API (current
is cached). When the candidate wins:

```bash
cp evals/candidates/summarize-json.candidate.prompt prompts/summarize-json.prompt
# commit + PR the production prompt change
```

### C — Judge + calibration

Three single-criterion `llm-rubric` graders (`assertions/rubrics/`):
faithfulness, thesis-anchoring, editorial quality — grader pinned to
Gemini, applied only to the `judge_subset` fixtures.

```bash
cd evals && npm run eval:judge        # rubrics ×3 repeats on the judge subset
npm run view                           # read the outputs YOURSELF, form your own verdicts
# record your pass/fail per (fixture × rubric) in calibration/human_labels.yaml
uv run --with pyyaml evals/calibration/agreement.py results/latest-judge.json
```

**Judge scores are advisory-only until calibrated.** Gate per rubric:
percent agreement ≥ 0.8 AND Cohen's κ ≥ 0.4 against your labels. κ ≈ 0
means the judge is effectively random for that rubric — rewrite the
rubric, don't trust it.

### D — Growing the dataset (append-mostly)

When a weekly cycle catches a bad summary — hallucination, wrong thesis
anchor, blocked-page fabrication — append it to `fixtures/selection.yaml`
with `added:` date and `reason:`, then:

```bash
uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py   # fetches only the new entry
git add evals/fixtures/    # frozen article text + manifest are committed
```

Never silently replace existing entries; frozen article text is what
keeps runs comparable over time (`--refresh` re-fetches deliberately).
This is the failure-feedback loop: the dataset grows from real errors,
and every future experiment is tested against every past failure.

## Reference

### Commands & cost

| Command (from evals/) | What it does | Live calls |
|---|---|---|
| `npm run eval` | Layer-① regression, all fixtures | ~11 |
| `npm run eval:compare` | current vs candidate, side-by-side | ~22 |
| `npm run eval:judge` | Layer-② rubrics on judge subset, ×3 repeats | ~12 + grader |
| `npm run view` | Web UI | 0 |
| `uv run python -m unittest tests.test_promptfoo_bridge` | prompt-parity guard | 0 |

### Assertion semantics (mirrors the production repair layer)

Production (`scripts/call-gemini.py:1011-1057`) silently repairs some
model mistakes. The assertions encode that asymmetry — things production
ships broken **hard-fail**; things it silently fixes are **soft metrics**
(the assertion always returns `pass: true` and reports drift via its
0/1 score) so drift is visible without failing rows:

| Check | Kind | Why |
|---|---|---|
| `schema_valid` (via `scripts/validate_summary.py`) | hard | production exits 1 too |
| `language_enum`, `content_type_enum` | hard | gaps validate_summary never covered; failures usually mean schema-copy drift, not prompt regression |
| `original_title_invariant` | asymmetric | non-ja + missing ships broken → hard; ja + present is silently stripped → soft |
| `url_fidelity` | soft metric | production pins the URL; metric measures how often the prompt's #1 CRITICAL rule is honored |
| `hallucination_clean` (via `scripts/summary_review.py`) | soft metric | heuristic — human-review signal by contract |

### Caching

The promptfoo cache (`evals/.promptfoo-cache/`, gitignored) keys on
rendered prompt + provider; unchanged reruns are free, and editing the
candidate only invalidates that column. `--no-cache` forces fresh calls.

**Known flake**: `gemini-3-flash-preview` occasionally hangs generating
for a fixture (observed on the thin-content stress fixture; requests
abort after ~15 min and promptfoo retries). promptfoo also caches the
resulting error row — if a fixture keeps showing the same timeout error
with an old request id, re-run just that fixture with the cache bypassed:

```bash
npx promptfoo eval -c promptfooconfig.judge.yaml --filter-pattern "011" --no-cache
```

## No CI (deliberate)

Prompt changes are rare and evals make live Gemini calls (with the
occasional hang above), so there is no automated trigger — run workflow
A/B manually whenever prompt-affecting files change. The network-free
parity guard can run any time. Revisit CI (or a pre-commit hook for the
parity test) only if prompt churn increases enough that manual runs get
forgotten.

## Out of scope / deferred

- **Online eval**: requires tracing/observability over production runs
  first. Start when the pipeline gets tracing; sampled production
  summaries would then flow into `fixtures/selection.yaml`.
- Red-teaming plugins; unifying the three schema copies
  (`schema/summary-v1-schema.json`, `get_gemini_schema()`,
  `response-schema.json`) behind codegen.
