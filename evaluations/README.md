# evaluations/ — one-shot investigations

Each investigation is a **self-contained dated folder**: its runner script, raw
results, human-readable report, and a `CONCLUSION.md` recording the decision it
produced. Investigations are point-in-time artifacts — they are kept for
provenance and re-runnable inspiration, not maintained as product code.

```
evaluations/
  README.md                          ← this file
  YYYY-MM-DD-<topic>/
    run_*.py                         ← the harness (self-contained, uv run)
    results_*.jsonl                  ← raw per-call records
    report_*.md                      ← metrics + side-by-side samples
    CONCLUSION.md                    ← the decision + where it was recorded
```

## Ground rules

- **No product code imports from here.** Investigations may import repo code
  and call live endpoints, never the reverse.
- The platform's stable seam for pipeline investigations is the worker's
  bearer-protected `POST /eval` route (`{url, model?}` → summary + timings +
  token usage, **no persistence**: no D1 writes, no NNN spend).
- New investigation = new dated folder + a CONCLUSION.md when it resolves.
  Reference the GitHub issue it feeds.

## Index

| Investigation | Question | Outcome |
|---|---|---|
| [2026-07-06-model-selection](./2026-07-06-model-selection/) | Which model should the cloud summarization pipeline (#166) use? (#167) | `gemini-3-flash-preview` via direct Gemini API; Workers AI open-weight-only + free neuron cap insufficient — see CONCLUSION.md |
