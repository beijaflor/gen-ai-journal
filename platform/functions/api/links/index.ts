// /api/links — link inbox (#159)
//   POST: submit a URL (form/bookmarklet via Access cookie, or bearer)
//   GET:  list links, ?status=new|consumed|dismissed (default: all)

import { authorize, type Env } from "../../_lib/auth";
import { error, json, sanitizeUrl, validateUrl } from "../../_lib/util";

const VALID_STATUSES = ["new", "queued", "summarized", "blocked", "consumed", "dismissed"] as const;

function enqueueSummarization(env: Env): Promise<unknown> | null {
  if (env.AUTO_SUMMARIZE !== "true" || !env.SUMMARIZER) return null;
  const stub = env.SUMMARIZER.get(env.SUMMARIZER.idFromName("main"));
  return stub.fetch("https://summarizer/enqueue", { method: "POST" }).catch(() => {});
}

export const onRequestPost: PagesFunction<Env> = async ({ request, env, waitUntil }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  let body: { url?: string; note?: string };
  try {
    body = await request.json();
  } catch {
    return error("body must be JSON: {url, note?}", 400);
  }
  const rawUrl = (body.url ?? "").trim();
  if (!rawUrl) return error("url is required", 400);
  const invalid = validateUrl(rawUrl);
  if (invalid) return error(invalid, 400);
  const note = (body.note ?? "").trim().slice(0, 500) || null;

  const url = sanitizeUrl(rawUrl);

  // The duplicate decision happens inside the INSERT (UNIQUE url), so two
  // concurrent submissions of the same URL can't race a separate pre-check.
  const res = await env.DB.prepare(
    "INSERT INTO links (url, note) VALUES (?, ?) ON CONFLICT (url) DO NOTHING RETURNING id, submitted_at",
  )
    .bind(url, note)
    .first<{ id: number; submitted_at: string }>();
  if (!res) {
    const existing = await env.DB.prepare("SELECT id, status FROM links WHERE url = ?")
      .bind(url)
      .first<{ id: number; status: string }>();
    if (!existing) return error("insert conflict — please retry", 500);
    return json({ duplicate: true, id: existing.id, status: existing.status, url }, 200);
  }
  const enqueue = enqueueSummarization(env);
  if (enqueue) waitUntil(enqueue);
  return json({ duplicate: false, id: res.id, url, note, status: "new", submitted_at: res.submitted_at }, 201);
};

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  const status = new URL(request.url).searchParams.get("status");
  if (status && !VALID_STATUSES.includes(status as never)) {
    return error(`status must be one of: ${VALID_STATUSES.join(", ")}`, 400);
  }

  const stmt = status
    ? env.DB.prepare(
        "SELECT id, url, note, status, error, summary_id, submitted_at, consumed_at FROM links WHERE status = ? ORDER BY submitted_at ASC",
      ).bind(status)
    : env.DB.prepare(
        "SELECT id, url, note, status, error, summary_id, submitted_at, consumed_at FROM links ORDER BY submitted_at DESC",
      );
  const { results } = await stmt.all();
  return json({ links: results, count: results.length });
};
