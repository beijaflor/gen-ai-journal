# Conclusion — model selection for the cloud summarization pipeline

**Issue:** [#167](https://github.com/beijaflor/gen-ai-journal/issues/167) (closed 2026-07-06)
**Decision:** `gemini-3-flash-preview` via direct Gemini API (`GEMINI_API_KEY`
worker secret). Workers AI kept as a switchable fallback via the
`SUMMARIZE_MODEL` var (prefix routing: `@cf/*` → Workers AI, else Gemini);
best-known open fallback: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`.

## Why

1. **Workers AI is open-weight-only** — Gemini (the model behind all ~5k
   archived summaries) is not available on it. The editor's requirement was to
   keep Gemini.
2. **Free neuron budget insufficient**: screening exhausted the daily 10,000
   neurons after ~15–20 heavy calls (`AiError 4006`) ≈ 15–25 summaries/day vs
   ~300/week needed with bursts.

## Evidence

- **Screening** (6 Workers AI models × 5 articles, `report_20260706_0029.md`):
  only `llama-3.3-70b-instruct-fp8-fast` passed (5/5 schema-valid, title
  fidelity 1.0, ja detection 5/5). gpt-oss-120b / kimi-k2.6 / glm-5.2 emit
  differently-wrapped output (would need parser adapters); qwen3 / gemma-4
  untested (quota exhausted mid-run).
- **Validation** (20 archived articles through the live pipeline with Gemini,
  `report_20260706_0052.md`): 16/20 → 18/20 after removing an output-token cap
  the local pipeline never had (truncation bug, fixed in `de1371b`); language
  detection 20/20; title similarity median 1.00 (p25 0.84); bodies median 497
  chars vs archive reference 352; inference median 18s; ~12–13k prompt tokens
  per article.
- Known flaky: freefable.org (Gemini-side >90s → fails closed, retryable).

## Cost outcome

$0 change — same Gemini key and usage profile as the local pipeline.

## Follow-ups carried elsewhere

- Editor spot-check of `report_20260706_0052.md` side-by-sides → cutover-b
  criterion in #165.
- Re-run recipe: `uv run evaluations/2026-07-06-model-selection/run_model_eval.py
  --models <ids> --sample N` (needs `PLATFORM_API_TOKEN` in scripts/.env).
