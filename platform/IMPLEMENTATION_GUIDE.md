# Cloud Summarization Platform — Implementation Guide

Knowledge document for the `platform/` Cloudflare implementation (epic #155):
architecture, decisions, semantics, and the lessons learned building it. Read
this before extending or debugging the platform. `platform/README.md` is the
terse operational reference; **this file is the "why" and "how it was built".**

---

## 1. What it is (mental model)

The platform ports **STEP_02 (gather + summarize) to the cloud** so a URL
submitted from any device becomes a stored Japanese summary with no laptop
involved. Editorial work (STEP_03 onward — curation, assembly) stays local.

**The design is hub-and-spoke. The summary collection (D1) is the hub:**

- **Producers** write summaries in: the cloud pipeline (default), and
  `push_summaries.py` (local fallback for what the cloud fails closed on — #168).
- **Consumers** read summaries out: the admin console, the detail page, the
  website (#162), and `generate_sources.py` (the STEP_03 handoff — #168).

Producers and consumers never talk to each other directly. This is why the
model is swappable and why each piece could ship independently.

---

## 2. Architecture

Two worlds, one seam (the D1 collection):

```
LOCAL (editorial, unchanged)          CLOUDFLARE (gather · summarize · store · serve)
────────────────────────────          ──────────────────────────────────────────────
Claude Code STEP_03+                   Pages project "gen-ai-journal"
curation / assembly                      functions/  = HTTP API (Pages Functions, TS)
generate_sources.py (#168) ◄──reads──    public/     = submit · inbox · admin console/logs
call-gemini.py (fallback) ──pushes──►    D1 "gen-ai-journal-db" = links · summaries · settings · events
                                       Worker "gen-ai-journal-pipeline"
                                         SummarizerDO = alarm-driven summarization queue
                                       Gemini API (summarization model — see §7)
```

**Two separately deployed Cloudflare units, one shared D1:**

1. **Pages project `gen-ai-journal`** (`platform/`) — static admin pages +
   `functions/` HTTP API. Deploy: `npm run deploy`.
2. **Worker `gen-ai-journal-pipeline`** (`platform/worker/`) — hosts the
   `SummarizerDO` Durable Object. Deploy: `npm run deploy:worker`.

The Pages project binds the DO by `script_name` (cross-deployable binding),
so link submission can kick the pipeline while the two stay independent.

**Why a separate Worker at all:** Pages Functions cannot host Durable Object
classes or cron. The pipeline needs a durable, alarm-driven queue (debounce +
serial processing + retry), so it lives in a companion Worker. Everything
user-facing (API, pages, Access) stays on Pages.

---

## 3. Infrastructure inventory (reproducible)

Created once via `wrangler` (authenticated as `syo.online@gmail.com`, account
"Gen AI Journal" `b3c944b809c5ca6678d2cc26fbb3c57c`). All free tier.

| Resource | Identifier | Created with |
|---|---|---|
| Pages project | `gen-ai-journal` → gen-ai-journal.pages.dev | `wrangler pages project create` |
| Worker | `gen-ai-journal-pipeline` | `wrangler deploy` (from worker/) |
| D1 database | `gen-ai-journal-db` `41a485fb-…` | `wrangler d1 create` |
| KV namespace | `REBUILD_THROTTLE` `1d583e69…` | `wrangler kv namespace create` (for #163) |
| Zero Trust team | `gentle-hill-7034` | dashboard onboarding (one-time) |
| Access application | walls `/submit` `/inbox` `/admin/*` | dashboard, allow-email policy, One-time PIN |
| workers.dev subdomain | `gen-ai-journal` | required before first `wrangler deploy` |

**Secrets** (never in git; set via `wrangler … secret put`):
- `API_BEARER_TOKEN` — on Pages **and** the worker (worker uses it for `/eval`).
  Mirror value in `scripts/.env` as `PLATFORM_API_TOKEN` for local tooling.
- `GEMINI_API_KEY` — on the worker (summarization inference).

Non-secret config is in the two `wrangler.jsonc` `vars` blocks (team domain,
Access `POLICY_AUD`, `SUMMARIZE_MODEL`, char limits).

**wrangler's OAuth token has NO Zero Trust scope** — the Access app must be
configured in the dashboard (or with a separately-minted API token), not the CLI.

### Staging environment (#177)

A full staging mirror lives entirely in Cloudflare, isolated from production at
the data plane (its own D1 — the hub). Compute is the Pages **`preview`**
environment plus the Worker's **`staging`** wrangler environment; config is the
two `env` blocks in the `wrangler.jsonc` files (`env.preview` on Pages,
`env.staging` on the worker). All free tier.

| Resource (staging) | Identifier |
|---|---|
| D1 database | `gen-ai-journal-db-staging` `8217e2ac-…` |
| KV namespace | `REBUILD_THROTTLE_staging` `65760529…` |
| Worker | `gen-ai-journal-pipeline-staging` (deploy: `--env staging`) |
| Pages env | `preview` → staging.gen-ai-journal.pages.dev (deploy: `--branch staging`) |
| Access application | **separate app**, own AUD `86817f76…`, walls the same paths on `staging.…` |

- **The isolation seam is `staging Worker → staging D1`.** The `SummarizerDO`
  writes through the worker's own `DB` binding, so the one thing that must never
  leak is the worker's D1 id. The Pages `env.preview` DO binding therefore sets
  `script_name: gen-ai-journal-pipeline-staging` — the staging UI enqueues into
  the staging pipeline, never prod.
- **`POLICY_AUD` differs per environment.** Staging has its own Access
  application (the prod app's 5-destination limit forced the split), so
  `env.preview.POLICY_AUD` = the staging app's AUD, verified in-function against
  the staging-issued JWT. `TEAM_DOMAIN` stays the same (one Zero Trust team).
- **Secrets are per-environment and NOT shared:** `GEMINI_API_KEY` +
  `API_BEARER_TOKEN` on the worker `--env staging`; `API_BEARER_TOKEN` on the
  Pages **Preview** scope. Keep the staging bearer separate from prod (mirror it
  locally as `PLATFORM_API_TOKEN_STAGING` in `scripts/.env`).
- Seed the staging cycle once after first deploy: `POST /api/cycle {date, next_id}`
  (else every submission fails closed on "no active cycle").

---

## 4. Repository layout

```
platform/
  wrangler.jsonc              Pages config: D1 + KV + DO bindings, Access vars
  package.json / tsconfig     npm run check (tsc) · test (vitest) · deploy · deploy:worker
  migrations/NNNN_*.sql        D1 schema, applied in order (idempotent tracking table)
  functions/                   Pages Functions = the HTTP API
    _lib/auth.ts               authorize() → "bearer" | Access email | null (§8)
    _lib/summaries.ts          THE write path: validate, blocked-stub detect, upsert, allocateId
    _lib/util.ts               sanitizeUrl/validateUrl (mirror scripts/check_link.py)
    _lib/enqueue.ts            kick the SummarizerDO
    _lib/events.ts             logEvent() fire-and-forget audit emitter
    _lib/summary_page.ts       pure HTML renderer for the detail page (unit-tested)
    api/links/{index,[id]}.ts  submit+list · PATCH (dismiss/reopen/retry)
    api/summaries/{index,[id]} bulk upsert · list · detail (dismissed→content:null)
    api/cycle.ts               registry state · rollover
    api/pipeline.ts            console feed (joined view)
    api/events.ts              audit query
    admin/links/[id].ts        server-rendered detail page (#173), keyed by link id
    admin/summaries/[id].ts    NNN → 302 redirect to /admin/links/<id>
  public/                      submit/ inbox/ admin/pipeline/ admin/logs/  (static)
  worker/
    wrangler.jsonc             Worker config: D1 + AI + DO binding
    src/index.ts               SummarizerDO (queue) + default fetch (/eval seam)
    src/core.ts                summarizeUrl(): the pipeline steps, shared with /eval
    src/prompt.generated.ts    GENERATED — uv run scripts/build_prompt_module.py
  tests/unit.test.ts           vitest over the pure logic
```

Local companions in `scripts/`: `pull_inbox.py` (legacy parallel-run tool),
`build_prompt_module.py` (regenerates the worker prompt from
`prompts/summarize-json.prompt` + criteria + persona).

---

## 5. The pipeline (how a URL becomes a summary)

1. `POST /api/links` — sanitize + validate + dedupe → insert `links` row
   (`status=new`), then (if `AUTO_SUMMARIZE=true`) kick the DO via `waitUntil`.
2. **SummarizerDO** debounces (~20s alarm), then processes one link per alarm
   firing (2s spacing), recovering stale `queued` claims (15 min).
3. `summarizeUrl()` (worker/src/core.ts): fetch (25s timeout) → **charset-aware
   decode** → HTMLRewriter text extraction → min-chars gate (200) → model call
   (Gemini, §7) with the summary-v1 JSON schema → validate → enforce invariants
   in code (verbatim URL, drop `originalTitle` for `ja`, stamp metadata).
4. On success: **allocate NNN** from the registry (or reuse the link's existing
   `summary_id`) → `writeSummary()` upsert → link `status=summarized`.
5. On any content failure: **fail closed** — link `status=blocked` + reason, no
   NNN spent. Infra failures (D1/AI outage) rethrow so the alarm retries.
6. Every run emits events (`summary.created` / `pipeline.blocked`) and updates
   the link's run-metric columns (fetch_ms, ai_ms, tokens).

**Fail-closed cases** (all become `blocked`, never a hallucinated summary):
PDF (Content-Type/`.pdf` → regenerate locally, #168), non-HTML, HTTP error,
thin extraction (bot-blocked/JS pages), model error, invalid model output,
no active cycle.

---

## 6. Numbering & status semantics (the part that caused the most confusion)

**Two numbers exist — keep them straight:**

- **NNN** (`summaries.id`) — the journal's number, the ONLY one with editorial
  meaning. **Per-cycle** (resets at rollover), zero-padded, assigned **only on
  successful summarization**, **reused** on re-summarize, **stays spent** on
  dismissal (gaps are honest). Used in filenames, `sources.md`, site URLs
  `/journals/<date>/<NNN>/`, and `/api/summaries/<NNN>`. **This is the only
  number with editorial meaning in the UI.**
- **link id** (`links.id`, shown discreetly as `L<n>`) — a technical row id.
  Assigned at submission, counts everything ever (incl. dismissed/blocked/tests),
  never resets. Its only job: a stable target for actions (`PATCH /api/links/7`),
  the subject key in `/admin/logs`, and the key of the admin detail page
  (`/admin/links/<id>`) — keyed by link id for process observability, so
  blocked/failed runs that never earned an NNN are inspectable too
  (`/admin/summaries/<NNN>` just redirects; NNN remains the editorial number).
  **Zero editorial meaning.**

The registry (`settings` table: `current_journal_date`, `next_summary_id`)
makes the cloud the ID authority. `POST /api/cycle` rolls over and seeds the
counter (during parallel-run, seed from the real `sources.md` max + 1).

**Link statuses:** `new` (shown as *generating*) → `queued` → `summarized` /
`blocked`; `dismissed`. (`consumed` was removed in migration 0007 — it was a
dead pull-based-design leftover; publication is tracked on *summaries* via
`journal_date`, not on links.)

**Summary statuses:** `workdesk` → `published` (at journal time, via
`journal_date`); `blocked`; `dismissed`.

**Dismiss is a reversible flag, content-hidden-only** (settled through several
iterations):
- Dismissing a link flags its summary `dismissed` — the row **stays**, nothing
  is deleted.
- The detail endpoint returns dismissed summaries with **`content: null`** but
  all metadata intact; `?status=workdesk` excludes them; `?status=dismissed`
  lists them.
- Re-open **flips the flag back instantly** — no regeneration, no token spend.
  Regeneration only happens for `blocked`/never-summarized links (real retry),
  or an explicit **re-summarize** (detail page) which reuses the same NNN.

---

## 7. Model decision (#167)

**`gemini-3-flash-preview` via the direct Gemini API** — the same model as the
entire archive, so quality parity is by construction and cost is unchanged
($0 delta; same key/usage as the local pipeline).

Why not Workers AI (the reflex choice for "AI on Cloudflare"):
1. **Open-weight only** — Gemini/GPT/Claude aren't on it. The requirement is to
   keep Gemini.
2. **Free neuron budget too small** — screening exhausted the daily 10k neurons
   after ~15–20 heavy calls (`AiError 4006`) ≈ 15–25 summaries/day vs ~300/week.

The pipeline routes by model prefix: `gemini-*` → Gemini `generateContent`
(structured output via `responseSchema`); `@cf/*` → Workers AI. Switchable via
the `SUMMARIZE_MODEL` var with **no code change** — Workers AI stays a viable
fallback (best open model screened: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`).
Full evidence: `evaluations/2026-07-06-model-selection/CONCLUSION.md`.

---

## 8. Auth model

| Caller | Mechanism |
|---|---|
| Local scripts / eval | `Authorization: Bearer <API_BEARER_TOKEN>` |
| Browser (submit/inbox/admin) | Cloudflare Access wall on those paths; the `CF_Authorization` JWT is **signature-verified in-function** (`_lib/auth.ts`, team JWKS + `aud`/`iss`/`exp`) for the `/api/*` calls those pages make |
| Readers | public GETs on summaries/cycle only |

**`/api/*` is deliberately NOT behind the Access wall** — machines must reach
it. So each API handler calls `authorize()` itself; anonymous `/api/*` → 401.
The pages under `/admin/*` `/submit` `/inbox` ARE walled (a new `/admin/…` path
is covered automatically). `authorize()` returns `"bearer"`, the Access email,
or `null`.

---

## 9. Deploy & dev workflow

```bash
# from platform/
npm run check          # tsc --noEmit (strict) — ALWAYS before deploy; esbuild does NOT typecheck
npm test               # vitest unit tests (pure logic)
npm run deploy         # Pages (functions + static)
npm run deploy:worker  # pipeline Worker (DO)
npm run deploy:staging         # Pages preview → staging.gen-ai-journal.pages.dev (#177)
npm run deploy:worker:staging  # staging pipeline Worker (Worker env.staging)

# schema change: add migrations/NNNN_name.sql, then apply to BOTH DBs (#177 —
# migrations now fan out; the staging mirror uses the Pages env.preview binding):
wrangler d1 migrations apply gen-ai-journal-db --local
wrangler d1 migrations apply gen-ai-journal-db --remote
wrangler d1 migrations apply gen-ai-journal-db-staging --remote --env preview

# local dev of the whole stack (local D1 + .dev.vars bearer):
wrangler pages dev --port 8788

# live structured run logs:
wrangler tail gen-ai-journal-pipeline
```

Deploy is direct-upload (doesn't consume the Pages Git-build quota). Each
deploy is an immutable snapshot; `--branch main` also makes it production.

---

## 10. Lessons learned (gotchas that cost real time)

- **esbuild strips types without checking them.** A type error deploys happily.
  `npm run check` (tsc) is the safety net — run it before every deploy.
- **Never cap Gemini output tokens.** A `maxOutputTokens: 4096` cap truncated
  the JSON mid-string on long articles → parse failures. The local pipeline has
  no cap; the cloud one must not either.
- **Japanese sites serve Shift_JIS / EUC-JP.** HTMLRewriter assumes UTF-8, so
  the body must be re-decoded by declared charset (header + `<meta>` sniff)
  first, or titles come out as mojibake. Found via itmedia.co.jp.
- **SQLite treats NULLs as distinct in a PRIMARY KEY.** Workdesk rows have
  `journal_date IS NULL`, so upserts need a `UNIQUE (id, ifnull(journal_date,''))`
  index guard (migration 0003).
- **SQLite can't alter CHECK constraints.** Extending a status enum means a
  table rebuild (copy → drop → rename), as in migrations 0004/0006/0007.
- **Workers AI structured output ≠ Gemini's.** Different models wrap JSON
  differently; only some honor `response_format`/`json_schema`.
- **Access can't be scripted with wrangler's token** — dashboard or a scoped
  API token only.
- **Pages secrets apply only to NEW deployments.** `wrangler pages secret put …
  --env preview` updates the project store but does NOT reach the currently-live
  deployment — a Function keeps seeing the old (or `undefined`) value until you
  redeploy. A freshly-set staging `API_BEARER_TOKEN` 401'd every `/api/*` call
  until `npm run deploy:staging` re-ran (#177). (Contrast Worker `secret put`,
  which takes effect immediately.)
- **Audit events outlive their subject** — deleting a link keeps its events by
  design; test/cleanup artifacts linger in `/admin/logs` (annotate test actions
  with `detail.note`).

---

## 11. Evaluations convention

One-shot investigations live under `evaluations/<YYYY-MM-DD-topic>/`
(self-contained: runner + raw results + report + `CONCLUSION.md`), indexed in
`evaluations/README.md`. **Product code never imports from `evaluations/`.**
The stable seam for pipeline investigations is the worker's bearer-protected
`POST /eval {url, model?}` — it runs the exact `summarizeUrl()` path **without
persisting** (no D1 write, no NNN spent), returning summary + timings + tokens.

---

## 12. How to extend

- **New API endpoint**: add `functions/api/<name>.ts` (or `[id].ts` for a
  param); call `authorize()` first for writes; return via `json()`/`error()`
  from `_lib/util.ts`.
- **New DB column/table**: add the next `migrations/NNNN_*.sql`; apply local +
  remote; rebuild the table if you're touching a CHECK constraint.
- **New event type**: emit via `logEvent()` — it's fire-and-forget and shared
  with the worker.
- **Change the model**: set `SUMMARIZE_MODEL` in `worker/wrangler.jsonc` (add
  `GEMINI_API_KEY` for gemini-*, nothing for `@cf/*`); re-eval via `/eval`
  before trusting a new one (see §11).
- **Change the prompt/criteria**: edit `prompts/summarize-json.prompt` (or the
  criteria/persona files it includes), then
  `uv run scripts/build_prompt_module.py` to regenerate `prompt.generated.ts`.

---

## 13. Status & roadmap (epic #155)

Done: link intake (#159), collection store + registry (#160), pipeline (#166),
model decision (#167), console (#161), events + `/admin/logs` (#172), detail
page (#173), plus a polish pass (#171). Pending: site reads the collection
(#162), rebuild automation (#163), local bridge scripts (#168), and the staged
cutover governance (#165) — the current local workflow stays canonical until
#165's criteria pass. See the epic for the live checklist.
