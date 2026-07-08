# platform/ — Cloudflare content platform

Cloud side of the online migration (epic #155): link intake (#159), summary
store + cycle/ID registry (#160), cloud summarization pipeline (#166, model
decided in #167), admin console (#161). The journal website is NOT hosted
here yet — see the epic for later phases.

Live: **https://gen-ai-journal.pages.dev** · Pipeline worker: `gen-ai-journal-pipeline`
Staging (#177): **https://staging.gen-ai-journal.pages.dev** · worker `gen-ai-journal-pipeline-staging` · isolated D1 `gen-ai-journal-db-staging`

## Layout

```
wrangler.jsonc        Pages project: D1/KV/DO bindings, Access vars
migrations/           D1 schema (wrangler d1 migrations apply gen-ai-journal-db)
functions/            Pages Functions = the HTTP API
  _lib/auth.ts        bearer-token + Cloudflare Access JWT verification
  _lib/summaries.ts   THE write path: validation, blocked-stub detect, upsert, NNN allocation
  _lib/util.ts        URL sanitize/validate (mirrors scripts/check_link.py)
  _lib/enqueue.ts     kick the summarization DO
  _lib/events.ts      logEvent(): fire-and-forget audit-trail INSERT (#172),
                      shared with the pipeline DO
  api/links/          POST (submit+auto-enqueue), GET, PATCH /:id (retry re-enqueues;
                      dismiss RETRACTS the link's workdesk summary — NNN stays spent)
  api/summaries/      POST bulk upsert (fallback pushes), GET list / :id (public reads)
  api/cycle.ts        GET registry state, POST rollover (seed counter per #165 rule)
  api/pipeline.ts     joined operational view for the console
  api/events.ts       GET audit trail: ?limit= (≤200) &event= &summary_id= &link_id=
  admin/summaries/    GET /admin/summaries/:id — server-rendered summary detail
                      page (#173): content, link + run metrics, actions
                      (dismiss / re-open / re-summarize), per-run event log
  _lib/summary_page.ts  pure HTML renderer for the detail page (unit-tested)
public/               static, Access-protected where sensitive
  submit/ inbox/      link intake UI + bookmarklet (+ latest-events panel)
  admin/pipeline/     operations console: states, errors, metrics, retry, rollover
  admin/logs/         events log: full audit trail, filterable, auto-refresh
                      Lists are read-mostly (#173): NNN links navigate to the
                      detail page; only retry-on-blocked stays on the console
worker/               companion Worker "gen-ai-journal-pipeline"
  src/index.ts        SummarizerDO: alarm-driven queue (debounce 20s, serial,
                      stale-claim recovery, infra-retry via alarm backoff)
  src/core.ts         summarizeUrl(): fetch → charset-aware decode → HTMLRewriter
                      extract → min-chars gate → model call → validate.
                      Model routing: gemini-* → Gemini API, @cf/* → Workers AI
  src/prompt.generated.ts  GENERATED — uv run scripts/build_prompt_module.py
tests/                vitest unit tests for the pure logic
```

## Commands

```bash
npm run check          # tsc --noEmit (run before every deploy)
npm test               # vitest unit tests
npm run deploy         # Pages (functions + static)
npm run deploy:worker  # pipeline worker (DO)
npm run deploy:staging         # staging Pages preview (#177)
npm run deploy:worker:staging  # staging pipeline worker
wrangler d1 migrations apply gen-ai-journal-db --remote                 # after adding migrations/NNNN_*.sql
wrangler d1 migrations apply gen-ai-journal-db-staging --remote --env preview  # …and the staging mirror (#177)
wrangler tail gen-ai-journal-pipeline                     # live structured run logs
```

## Auth model

| Caller | Mechanism |
|---|---|
| Local scripts | `Authorization: Bearer` = `PLATFORM_API_TOKEN` in `scripts/.env` (Pages secret `API_BEARER_TOKEN`, same on the worker for `/eval`) |
| Browser pages | Cloudflare Access wall (team `gentle-hill-7034`) on `/submit` `/inbox` `/admin/*`; the `CF_Authorization` JWT is signature-verified in-function for `/api/*` calls |
| Readers | public GETs on summaries/cycle only; every write is authenticated |
| Evaluations | worker `POST /eval` {url, model?} — full pipeline path, NO persistence (see `evaluations/README.md`) |

## Semantics worth remembering

- NNN IDs are spent **only on successful summary writes**; retry/re-open of a
  summarized link **reuses** its NNN (never double-spends).
- Dismiss is a **reversible flag**: the summary row stays, marked `dismissed`
  (excluded from `status=workdesk` consumers; published rows never touched).
  Re-open flips it back instantly — no regeneration, no token spend.
- **Re-summarize** (detail page, confirm-gated): PATCH the summarized link
  back to `new` while its summary is NOT dismissed → the pipeline re-runs and
  overwrites the content under the same NNN (token spend, `updated_at` moves).
- Blocked = fail-closed with a reason on the link; PDFs & bot-blocked pages
  are regenerated locally and pushed (#168, permanent fallback path).
- Every summarization-lifecycle interaction lands in the append-only `events`
  table (#172): link submitted/dismissed/reopened, summary created/dismissed/
  restored, pipeline blocked (with metrics), cycle rolled. Events survive link
  deletion; scope is summarization only until the publish phase (#163) adds
  journal events. View at `/admin/logs`, query via `GET /api/events`.
- Secrets: `API_BEARER_TOKEN` (Pages + worker), `GEMINI_API_KEY` (worker).
