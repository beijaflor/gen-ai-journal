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
import { allocateId, getCycle, inspectSummary, writeSummary } from "../../functions/_lib/summaries";
import { SUMMARIZE_PROMPT_TEMPLATE } from "./prompt.generated";

export interface PipelineEnv {
  DB: D1Database;
  AI: Ai;
  SUMMARIZER: DurableObjectNamespace;
  SUMMARIZE_MODEL: string;
  MIN_CONTENT_CHARS: string;
  MAX_CONTENT_CHARS: string;
  API_BEARER_TOKEN?: string; // enables the /eval route (#167)
}

const DEBOUNCE_MS = 20_000;
const NEXT_LINK_DELAY_MS = 2_000;
const STALE_QUEUED_MIN = 15;
const FETCH_TIMEOUT_MS = 25_000;
const USER_AGENT = "Mozilla/5.0 (GenAI Journal Summarizer; +https://gen-ai-journal.pages.dev)";

interface LinkRow {
  id: number;
  url: string;
  status: string;
}

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
      "UPDATE links SET status = 'queued' WHERE id = (SELECT id FROM links WHERE status = 'new' ORDER BY submitted_at ASC LIMIT 1) RETURNING id, url, status",
    ).first<LinkRow>();
  }

  private async block(linkId: number, reason: string): Promise<void> {
    await this.env.DB.prepare("UPDATE links SET status = 'blocked', error = ? WHERE id = ?")
      .bind(reason.slice(0, 500), linkId)
      .run();
  }

  private async processLink(link: LinkRow): Promise<void> {
    const cycle = await getCycle(this.env as never);
    if (!cycle) {
      await this.block(link.id, "no active cycle — POST /api/cycle first");
      return;
    }

    const out = await summarizeUrl(this.env, link.url);
    if (!out.ok) {
      await this.block(link.id, out.reason);
      return;
    }

    // Allocate NNN and write via the shared path (IDs only spent on success)
    const id = await allocateId(this.env as never);
    const result = await writeSummary(this.env as never, { id, content: out.raw });
    if (!result.ok) {
      await this.block(link.id, `BLOCKED: store rejected — ${result.error}`);
      return;
    }
    await this.env.DB.prepare("UPDATE links SET status = 'summarized', summary_id = ?, error = NULL WHERE id = ?")
      .bind(id, link.id)
      .run();
  }
}

export interface SummarizeMeta {
  model: string;
  extractChars: number;
  fetchMs: number;
  aiMs: number;
  usage?: unknown; // whatever AI.run reports (token counts where available)
}

export type SummarizeResult =
  | { ok: true; raw: string; meta: SummarizeMeta }
  | { ok: false; reason: string; meta?: Partial<SummarizeMeta> };

/** The full summarization core — used by the DO (persisting) and /eval (non-persisting). */
async function summarizeUrl(env: PipelineEnv, url: string, modelOverride?: string): Promise<SummarizeResult> {
  const model = modelOverride ?? env.SUMMARIZE_MODEL;

  // 1. Fetch (fail closed on anything that isn't a readable HTML page)
  const t0 = Date.now();
  let res: Response;
  try {
    res = await fetch(url, {
      redirect: "follow",
      signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
      headers: { "user-agent": USER_AGENT, accept: "text/html,application/xhtml+xml" },
    });
  } catch (e) {
    return { ok: false, reason: `BLOCKED: fetch failed — ${String(e).slice(0, 200)}` };
  }
  if (!res.ok) return { ok: false, reason: `BLOCKED: fetch returned HTTP ${res.status}` };
  const ctype = (res.headers.get("content-type") ?? "").toLowerCase();
  if (ctype.includes("application/pdf") || new URL(url).pathname.toLowerCase().endsWith(".pdf")) {
    return { ok: false, reason: "BLOCKED-PDF: PDF detected — regenerate locally via summarize-pdf (#168)" };
  }
  if (!ctype.includes("html")) {
    return { ok: false, reason: `BLOCKED: unsupported content-type ${ctype.slice(0, 80)}` };
  }

  // 2. Extract main text (streaming, CPU-cheap)
  const { title, text } = await extractText(res);
  const fetchMs = Date.now() - t0;
  const minChars = Number(env.MIN_CONTENT_CHARS);
  if (text.length < minChars) {
    return {
      ok: false,
      reason: `BLOCKED: extracted ${text.length} chars < ${minChars} — likely bot-blocked or JS-rendered`,
      meta: { extractChars: text.length, fetchMs },
    };
  }
  const content = text.slice(0, Number(env.MAX_CONTENT_CHARS));

  // 3. Workers AI, summary-v1 via json_schema
  const prompt = SUMMARIZE_PROMPT_TEMPLATE.replace("{{url}}", url).replace("{{content}}", `# ${title}\n\n${content}`);
  const t1 = Date.now();
  let parsed: Record<string, never>;
  let usage: unknown;
  try {
    const result = (await env.AI.run(model as never, {
      messages: [{ role: "user", content: prompt }],
      max_tokens: 4096,
      response_format: { type: "json_schema", json_schema: SUMMARY_JSON_SCHEMA },
    } as never)) as { response?: unknown; usage?: unknown };
    usage = result.usage;
    const out = result.response ?? result;
    parsed = (typeof out === "object" && out !== null ? out : JSON.parse(String(out))) as Record<string, never>;
  } catch (e) {
    return {
      ok: false,
      reason: `BLOCKED: model call failed — ${String(e).slice(0, 300)}`,
      meta: { model, extractChars: content.length, fetchMs },
    };
  }
  const aiMs = Date.now() - t1;

  // 4. Enforce invariants the prompt alone can't guarantee
  const doc = parsed as { metadata?: Record<string, unknown>; content?: Record<string, unknown> };
  doc.metadata = {
    ...(doc.metadata ?? {}),
    version: "1.0",
    generatedAt: new Date().toISOString(),
    generatedBy: model,
  };
  if (doc.content) {
    doc.content.url = url; // URL RULE enforced in code, not trust
    if (doc.content.language === "ja") delete doc.content.originalTitle;
  }
  const raw = JSON.stringify(doc, null, 2);
  const check = inspectSummary(raw);
  if (check.error) {
    return {
      ok: false,
      reason: `BLOCKED: model output invalid — ${check.error}`,
      meta: { model, extractChars: content.length, fetchMs, aiMs, usage },
    };
  }
  return { ok: true, raw, meta: { model, extractChars: content.length, fetchMs, aiMs, usage } };
}

/** Decode the body honoring its declared charset (Japanese sites often serve
 *  Shift_JIS / EUC-JP; HTMLRewriter assumes UTF-8, so garbled input must be
 *  re-decoded before parsing — found via itmedia.co.jp in the first e2e run). */
async function decodeBody(res: Response): Promise<string> {
  const buf = await res.arrayBuffer();
  let charset =
    /charset=["']?([\w-]+)/i.exec(res.headers.get("content-type") ?? "")?.[1]?.toLowerCase() ?? null;
  if (!charset) {
    const head = new TextDecoder("latin1").decode(buf.slice(0, 2048));
    charset =
      /<meta[^>]+charset=["']?([\w-]+)/i.exec(head)?.[1]?.toLowerCase() ??
      /<meta[^>]+content=["'][^"']*charset=([\w-]+)/i.exec(head)?.[1]?.toLowerCase() ??
      "utf-8";
  }
  try {
    return new TextDecoder(charset).decode(buf);
  } catch {
    return new TextDecoder("utf-8").decode(buf);
  }
}

async function extractText(res: Response): Promise<{ title: string; text: string }> {
  const html = await decodeBody(res);
  const chunks: string[] = [];
  let title = "";
  let inTitle = false;
  const collect = {
    text(t: { text: string; lastInTextNode: boolean }) {
      if (t.text) chunks.push(t.text);
      if (t.lastInTextNode) chunks.push("\n");
    },
  };
  const rewriter = new HTMLRewriter()
    .on("title", {
      element() {
        inTitle = true;
      },
      text(t) {
        if (inTitle) title += t.text;
        if (t.lastInTextNode) inTitle = false;
      },
    })
    .on("p", collect)
    .on("h1", collect)
    .on("h2", collect)
    .on("h3", collect)
    .on("li", collect)
    .on("blockquote", collect)
    .on("td", collect);
  await rewriter.transform(new Response(html)).arrayBuffer(); // drive the stream (UTF-8 by construction)
  const text = chunks.join("").replace(/[ \t]+/g, " ").replace(/\n{3,}/g, "\n\n").trim();
  return { title: title.trim(), text };
}

// summary-v1 shape for Workers AI structured output (mirrors get_gemini_schema
// in scripts/call-gemini.py; scores kept permissive — schema enforces shape,
// criteria in the prompt define meaning).
const SUMMARY_JSON_SCHEMA = {
  type: "object",
  required: ["metadata", "content"],
  properties: {
    metadata: {
      type: "object",
      required: ["version", "generatedAt", "generatedBy"],
      properties: {
        version: { type: "string" },
        generatedAt: { type: "string" },
        generatedBy: { type: "string" },
      },
    },
    content: {
      type: "object",
      required: ["title", "url", "language", "contentType", "oneSentenceSummary", "summaryBody", "topics", "scores"],
      properties: {
        title: { type: "string" },
        originalTitle: { type: "string" },
        url: { type: "string" },
        language: { type: "string", enum: ["ja", "en", "zh", "ko", "other"] },
        contentType: { type: "string" },
        oneSentenceSummary: { type: "string" },
        summaryBody: { type: "string" },
        topics: { type: "array", items: { type: "string" } },
        scores: {
          type: "object",
          required: ["signal", "depth", "uniqueness", "practical", "antiHype", "mainJournal", "annexPotential", "overall"],
          properties: {
            signal: { type: "integer" },
            depth: { type: "integer" },
            uniqueness: { type: "integer" },
            practical: { type: "integer" },
            antiHype: { type: "integer" },
            mainJournal: { type: "integer" },
            annexPotential: { type: "integer" },
            overall: { type: "integer" },
          },
        },
      },
    },
  },
} as const;

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
      return Response.json(result, { status: result.ok ? 200 : 422 });
    }
    return new Response("gen-ai-journal-pipeline: Durable Object host", { status: 404 });
  },
};
