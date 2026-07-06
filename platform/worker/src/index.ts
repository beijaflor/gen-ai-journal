// gen-ai-journal-pipeline (#166): cloud summarization as a Durable Object.
//
// The Pages project binds SummarizerDO (script_name: gen-ai-journal-pipeline)
// and calls /enqueue after each link submission. The DO debounces via its
// alarm, then processes one link per alarm firing: fetch → extract
// (HTMLRewriter) → min-chars gate → Workers AI (summary-v1 json_schema) →
// validate → allocate NNN → write to the collection via the shared helper.
// Content failures fail closed (link status=blocked + reason, no NNN spent);
// infra failures rethrow so the alarm's built-in retry/backoff handles them.

import { DurableObject } from "cloudflare:workers";
import { allocateId, getCycle, writeSummary } from "../../functions/_lib/summaries";
import { logRun, summarizeUrl, tokensFromUsage, type LinkRow, type SummarizeMeta, type SummarizeResult } from "./core";

export interface PipelineEnv {
  DB: D1Database;
  AI: Ai;
  SUMMARIZER: DurableObjectNamespace;
  SUMMARIZE_MODEL: string;
  MIN_CONTENT_CHARS: string;
  MAX_CONTENT_CHARS: string;
  API_BEARER_TOKEN?: string; // enables the /eval route (#167)
  GEMINI_API_KEY?: string; // required when SUMMARIZE_MODEL is a gemini-* model
}

const DEBOUNCE_MS = 20_000;
const NEXT_LINK_DELAY_MS = 2_000;
const STALE_QUEUED_MIN = 15;
export class SummarizerDO extends DurableObject<PipelineEnv> {
  async fetch(request: Request): Promise<Response> {
    const path = new URL(request.url).pathname;
    if (path === "/enqueue") {
      const current = await this.ctx.storage.getAlarm();
      if (current === null) await this.ctx.storage.setAlarm(Date.now() + DEBOUNCE_MS);
      return new Response(JSON.stringify({ scheduled: true }), { status: 202 });
    }
    if (path === "/tick") {
      // Manual kick (console retry / debugging)
      await this.ctx.storage.setAlarm(Date.now() + 100);
      return new Response(JSON.stringify({ scheduled: true }), { status: 202 });
    }
    return new Response("not found", { status: 404 });
  }

  async alarm(): Promise<void> {
    const link = await this.claimNext();
    if (!link) return; // queue drained

    try {
      await this.processLink(link);
    } catch (e) {
      // Infra-level failure (D1/AI outage): release the claim and rethrow so
      // the alarm retry (with backoff) picks it up again.
      await this.env.DB.prepare("UPDATE links SET status = 'new' WHERE id = ? AND status = 'queued'")
        .bind(link.id)
        .run();
      throw e;
    }

    const more = await this.env.DB.prepare("SELECT COUNT(*) AS n FROM links WHERE status = 'new'").first<{ n: number }>();
    if (more && more.n > 0) await this.ctx.storage.setAlarm(Date.now() + NEXT_LINK_DELAY_MS);
  }

  private async claimNext(): Promise<LinkRow | null> {
    // Recover links stuck in 'queued' by a crashed run before claiming new work.
    await this.env.DB.prepare(
      `UPDATE links SET status = 'new' WHERE status = 'queued' AND submitted_at < datetime('now', '-${STALE_QUEUED_MIN} minutes')`,
    ).run();
    return this.env.DB.prepare(
      "UPDATE links SET status = 'queued' WHERE id = (SELECT id FROM links WHERE status = 'new' ORDER BY submitted_at ASC LIMIT 1) RETURNING id, url, status, summary_id",
    ).first<LinkRow>();
  }

  private async block(linkId: number, reason: string, meta?: Partial<SummarizeMeta>): Promise<void> {
    await this.recordRun(linkId, meta);
    await this.env.DB.prepare("UPDATE links SET status = 'blocked', error = ? WHERE id = ? AND status = 'queued'")
      .bind(reason.slice(0, 500), linkId)
      .run();
  }

  private async recordRun(linkId: number, meta?: Partial<SummarizeMeta>): Promise<void> {
    const t = tokensFromUsage(meta?.usage);
    await this.env.DB.prepare(
      "UPDATE links SET processed_at = ?, fetch_ms = ?, ai_ms = ?, tokens_in = ?, tokens_out = ? WHERE id = ?",
    )
      .bind(new Date().toISOString(), meta?.fetchMs ?? null, meta?.aiMs ?? null, t.tokensIn, t.tokensOut, linkId)
      .run();
  }

  private async processLink(link: LinkRow): Promise<void> {
    const cycle = await getCycle(this.env as never);
    if (!cycle) {
      await this.block(link.id, "no active cycle — POST /api/cycle first");
      return;
    }

    const out = await summarizeUrl(this.env, link.url);
    logRun(link, out);
    if (!out.ok) {
      await this.block(link.id, out.reason, out.meta);
      return;
    }

    // Reuse the link's existing NNN on re-summarize (retry/re-open of a
    // previously summarized link must never double-spend an ID); otherwise
    // allocate — IDs are only spent on success.
    const id = link.summary_id ?? (await allocateId(this.env as never));
    const result = await writeSummary(this.env as never, { id, content: out.raw });
    if (!result.ok) {
      await this.block(link.id, `BLOCKED: store rejected — ${result.error}`, out.meta);
      return;
    }
    await this.recordRun(link.id, out.meta);
    // Guarded on 'queued' so a dismissal that raced this run wins.
    await this.env.DB.prepare(
      "UPDATE links SET status = 'summarized', summary_id = ?, error = NULL WHERE id = ? AND status = 'queued'",
    )
      .bind(id, link.id)
      .run();
  }
}

export default {
  // POST /eval {url, model?} — run the exact pipeline path WITHOUT persisting
  // anything (no NNN spent, no D1 writes). Bearer-protected. Used by the
  // model-quality eval (#167).
  async fetch(request: Request, env: PipelineEnv): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/eval" && request.method === "POST") {
      const auth = request.headers.get("authorization") ?? "";
      if (!env.API_BEARER_TOKEN || auth !== `Bearer ${env.API_BEARER_TOKEN}`) {
        return Response.json({ error: "unauthorized" }, { status: 401 });
      }
      let body: { url?: string; model?: string };
      try {
        body = await request.json();
      } catch {
        return Response.json({ error: "body must be JSON: {url, model?}" }, { status: 400 });
      }
      if (!body.url) return Response.json({ error: "url is required" }, { status: 400 });
      const result = await summarizeUrl(env, body.url, body.model);
      logRun({ id: -1, url: body.url, status: "eval" }, result);
      return Response.json(result, { status: result.ok ? 200 : 422 });
    }
    return new Response("gen-ai-journal-pipeline: Durable Object host", { status: 404 });
  },
};
