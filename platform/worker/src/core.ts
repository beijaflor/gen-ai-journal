// Pipeline core (#166): the summarization path shared by the Durable Object
// (persisting) and the /eval route (non-persisting, #167). No D1 access here —
// callers own persistence.

import { inspectSummary } from "../../functions/_lib/summaries";
import { SUMMARIZE_PROMPT_TEMPLATE } from "./prompt.generated";
import type { PipelineEnv } from "./index";

const FETCH_TIMEOUT_MS = 25_000;
const USER_AGENT = "Mozilla/5.0 (GenAI Journal Summarizer; +https://gen-ai-journal.pages.dev)";

export interface LinkRow {
  id: number;
  url: string;
  status: string;
  summary_id?: string | null;
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

/** Optional per-step event emitter (#178). The DO passes one backed by
 *  logEvent (adding link_id + the run marker); /eval passes nothing, so eval
 *  runs persist no events. Fire-and-forget: emitter failures are swallowed
 *  here so a step event can never fail a run. */
export type StepEmitter = (event: string, detail: Record<string, unknown>) => void | Promise<void>;

/** The full summarization core — used by the DO (persisting) and /eval (non-persisting). */
export async function summarizeUrl(
  env: PipelineEnv,
  url: string,
  modelOverride?: string,
  onStep?: StepEmitter,
): Promise<SummarizeResult> {
  const model = modelOverride ?? env.SUMMARIZE_MODEL;
  const emit = async (event: string, detail: Record<string, unknown>): Promise<void> => {
    try {
      await onStep?.(event, detail);
    } catch {
      /* step events must never fail or slow the run */
    }
  };

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

  // 2. Decode (charset-aware) + extract main text (streaming, CPU-cheap)
  const { html, bytes, charset } = await decodeBody(res);
  await emit("pipeline.fetched", { status: res.status, ms: Date.now() - t0, bytes, charset });
  const { title, text } = await extractText(html);
  const fetchMs = Date.now() - t0;
  await emit("pipeline.extracted", { chars: text.length });
  const minChars = Number(env.MIN_CONTENT_CHARS);
  if (text.length < minChars) {
    return {
      ok: false,
      reason: `BLOCKED: extracted ${text.length} chars < ${minChars} — likely bot-blocked or JS-rendered`,
      meta: { extractChars: text.length, fetchMs },
    };
  }
  const content = text.slice(0, Number(env.MAX_CONTENT_CHARS));

  // 3. Structured summary-v1 generation.
  //    Model routing (#167 decision): gemini-* → Gemini API (same model as the
  //    whole archive — quality parity by construction, and Workers AI's free
  //    neuron budget can't carry the weekly volume at 70B quality);
  //    @cf/* → Workers AI (kept as fallback/eval path).
  const prompt = SUMMARIZE_PROMPT_TEMPLATE.replace("{{url}}", url).replace("{{content}}", `# ${title}\n\n${content}`);
  await emit("pipeline.model_requested", { model, input_chars: prompt.length });
  const t1 = Date.now();
  let parsed: Record<string, never>;
  let usage: unknown;
  try {
    if (model.startsWith("@cf/")) {
      const result = (await env.AI.run(model as never, {
        messages: [{ role: "user", content: prompt }],
        max_tokens: 4096,
        response_format: { type: "json_schema", json_schema: SUMMARY_JSON_SCHEMA },
      } as never)) as { response?: unknown; usage?: unknown };
      usage = result.usage;
      const out = result.response ?? result;
      parsed = (typeof out === "object" && out !== null ? out : JSON.parse(String(out))) as Record<string, never>;
    } else {
      const g = await runGemini(env, model, prompt);
      parsed = g.parsed as Record<string, never>;
      usage = g.usage;
    }
  } catch (e) {
    return {
      ok: false,
      reason: `BLOCKED: model call failed — ${String(e).slice(0, 300)}`,
      meta: { model, extractChars: content.length, fetchMs },
    };
  }
  const aiMs = Date.now() - t1;
  const tk = tokensFromUsage(usage);
  await emit("pipeline.model_responded", { ms: aiMs, tokens_in: tk.tokensIn, tokens_out: tk.tokensOut });

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
async function decodeBody(res: Response): Promise<{ html: string; bytes: number; charset: string }> {
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
    return { html: new TextDecoder(charset).decode(buf), bytes: buf.byteLength, charset };
  } catch {
    return { html: new TextDecoder("utf-8").decode(buf), bytes: buf.byteLength, charset: "utf-8" };
  }
}

/** Gemini structured-output call — mirrors get_gemini_schema() in scripts/call-gemini.py. */
async function runGemini(
  env: PipelineEnv,
  model: string,
  prompt: string,
): Promise<{ parsed: unknown; usage: unknown }> {
  if (!env.GEMINI_API_KEY) throw new Error("GEMINI_API_KEY secret not set on the pipeline worker");
  const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-goog-api-key": env.GEMINI_API_KEY },
    body: JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      // No maxOutputTokens: mirror the local pipeline (model default), which
      // never truncates — a 4096 cap produced unterminated-JSON failures.
      generationConfig: {
        responseMimeType: "application/json",
        responseSchema: toGeminiSchema(SUMMARY_JSON_SCHEMA),
      },
    }),
    signal: AbortSignal.timeout(90_000),
  });
  if (!res.ok) throw new Error(`Gemini HTTP ${res.status}: ${(await res.text()).slice(0, 300)}`);
  const data = (await res.json()) as {
    candidates?: { content?: { parts?: { text?: string }[] } }[];
    usageMetadata?: unknown;
  };
  const text = data.candidates?.[0]?.content?.parts?.map((p) => p.text ?? "").join("");
  if (!text) throw new Error("Gemini returned no candidates");
  return { parsed: JSON.parse(text), usage: data.usageMetadata };
}

/** Convert our JSON-Schema-style shape to Gemini's REST schema (uppercase types). */
function toGeminiSchema(node: Record<string, unknown>): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  if (typeof node.type === "string") out.type = (node.type as string).toUpperCase();
  if (node.enum) out.enum = node.enum;
  if (node.required) out.required = node.required;
  if (node.items) out.items = toGeminiSchema(node.items as Record<string, unknown>);
  if (node.properties) {
    out.properties = Object.fromEntries(
      Object.entries(node.properties as Record<string, Record<string, unknown>>).map(([k, v]) => [
        k,
        toGeminiSchema(v),
      ]),
    );
  }
  return out;
}

async function extractText(html: string): Promise<{ title: string; text: string }> {
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


export function tokensFromUsage(usage: unknown): { tokensIn: number | null; tokensOut: number | null } {
  const u = (usage ?? {}) as Record<string, number>;
  // Gemini: usageMetadata.{promptTokenCount,candidatesTokenCount}; Workers AI: {prompt_tokens,completion_tokens}
  return {
    tokensIn: u.promptTokenCount ?? u.prompt_tokens ?? null,
    tokensOut: u.candidatesTokenCount ?? u.completion_tokens ?? null,
  };
}

/** One structured log line per pipeline run — visible via `wrangler tail` and Workers Logs. */
export function logRun(link: LinkRow, out: SummarizeResult): void {
  const meta = out.ok ? out.meta : out.meta;
  const t = tokensFromUsage(meta?.usage);
  console.log(
    JSON.stringify({
      evt: "summarize",
      linkId: link.id,
      url: link.url,
      outcome: out.ok ? "ok" : "blocked",
      reason: out.ok ? undefined : out.reason,
      model: meta?.model,
      fetchMs: meta?.fetchMs,
      aiMs: meta?.aiMs,
      extractChars: meta?.extractChars,
      tokensIn: t.tokensIn,
      tokensOut: t.tokensOut,
    }),
  );
}
