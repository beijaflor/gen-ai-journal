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

## One-time setup

```bash
uv sync                                   # repo .venv (assertions/prompt fns run in it)
cd evals && npm install && cd ..          # pins promptfoo
export GEMINI_API_KEY=...                 # already required by the pipeline
```

promptfoo's google provider reads `GOOGLE_API_KEY` by default; the
configs set `apiKeyEnvar: GEMINI_API_KEY`, but if your promptfoo version
ignores it, bridge with: `export GOOGLE_API_KEY="$GEMINI_API_KEY"`.

Fixtures and `response-schema.json` are committed — rebuild only when
the dataset or `get_gemini_schema()` changes:

```bash
uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py   # --refresh to re-fetch
uv run evals/tools/gen_response_schema.py
```

## Daily commands (from evals/)

| Command | What it does | Live calls |
|---|---|---|
| `npm run eval` | Layer-① regression on the current prompt | ~11 |
| `npm run eval:compare` | current vs `candidates/summarize-json.candidate.prompt`, side-by-side | ~22 |
| `npm run eval:judge` | Layer-② rubrics on judge_subset fixtures, ×3 repeats | ~12 + grader |
| `npm run view` | Web UI (side-by-side columns, per-assertion reasons) | 0 |

Typical prompt-change workflow (`evals/candidates/` is gitignored —
it's your local experiment scratch, never committed):

```bash
mkdir -p evals/candidates
cp prompts/summarize-json.prompt evals/candidates/summarize-json.candidate.prompt
# edit the candidate…
cd evals && npm run eval:compare && npm run view
# happy? copy the candidate back over prompts/summarize-json.prompt and PR it
```

Repeat runs are free: the promptfoo cache (`evals/.promptfoo-cache/`,
gitignored) keys on rendered prompt + provider; editing the candidate
only invalidates that column. Use `npx promptfoo eval -c … --no-cache`
to force fresh calls.

## Assertion semantics (mirrors the production repair layer)

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

## Judge layer (advisory until calibrated)

`npm run eval:judge` grades judge_subset fixtures on three single-criterion
rubrics (`assertions/rubrics/`): faithfulness, thesis-anchoring, editorial
quality — grader pinned to Gemini. **Judge scores are advisory-only until
calibrated**: fill `calibration/human_labels.yaml` from a run you reviewed
yourself, then

```bash
uv run --with pyyaml evals/calibration/agreement.py results/latest-judge.json
```

Gate: percent agreement ≥ 0.8 AND Cohen's κ ≥ 0.4 per rubric before any
judge score is used for gating decisions. κ ≈ 0 = the judge is random for
that rubric; rewrite the rubric.

**Known flake**: `gemini-3-flash-preview` occasionally hangs generating
for a fixture (observed on the thin-content stress fixture; requests
abort after ~15 min and promptfoo retries). promptfoo also caches the
resulting error row — if a fixture keeps showing the same timeout error
with an old request id, re-run just that fixture with the cache bypassed:

```bash
npx promptfoo eval -c promptfooconfig.judge.yaml --filter-pattern "011" --no-cache
```

## Growing the dataset (append-mostly)

When a weekly cycle catches a bad summary — hallucination, wrong thesis
anchor, blocked-page fabrication — append it to `fixtures/selection.yaml`
with `added:` date and `reason:`, rebuild fixtures, commit the new
article text. Never silently replace existing entries; frozen article
text is what keeps runs comparable over time.

## No CI (deliberate)

Prompt changes are rare and evals make live Gemini calls (with
occasional multi-minute hangs — see the known flake above), so there is
no automated trigger: run `npm run eval` / `npm run eval:compare`
manually whenever `prompts/`, `criteria/`, `EDITOR_PERSONALITY.md`, or
the schema change. The network-free guard can be run any time:

```bash
uv run python -m unittest tests.test_promptfoo_bridge
```

Revisit CI (or a pre-commit hook for the parity test) only if prompt
churn increases enough that manual runs get forgotten.

## Out of scope / deferred

- **Online eval**: requires tracing/observability over production runs
  first. Start when the pipeline gets tracing; sampled production
  summaries would then flow into `fixtures/selection.yaml`.
- Red-teaming plugins; unifying the three schema copies
  (`schema/summary-v1-schema.json`, `get_gemini_schema()`,
  `response-schema.json`) behind codegen.
