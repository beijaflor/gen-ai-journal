// GET /api/events (#172) — the summarization audit trail, newest-first.
//   ?limit=       default 50, max 200
//   ?event=       exact event name (e.g. pipeline.blocked)
//   ?summary_id=  full history for one NNN
//   ?link_id=     full history for one link

import { authorize, type Env } from "../_lib/auth";
import { error, json } from "../_lib/util";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  const q = new URL(request.url).searchParams;
  const limit = Math.min(Math.max(Number(q.get("limit") ?? "") || 50, 1), 200);
  const conds: string[] = [];
  const binds: (string | number)[] = [];
  const event = q.get("event");
  if (event) {
    conds.push("event = ?");
    binds.push(event);
  }
  const summaryId = q.get("summary_id");
  if (summaryId) {
    conds.push("summary_id = ?");
    binds.push(summaryId);
  }
  const linkId = q.get("link_id");
  if (linkId) {
    if (!/^\d+$/.test(linkId)) return error("link_id must be an integer", 400);
    conds.push("link_id = ?");
    binds.push(Number(linkId));
  }
  const where = conds.length ? ` WHERE ${conds.join(" AND ")}` : "";
  const { results } = await env.DB.prepare(
    `SELECT id, ts, actor, event, link_id, summary_id, detail FROM events${where} ORDER BY id DESC LIMIT ?`,
  )
    .bind(...binds, limit)
    .all();
  return json({ events: results, count: results.length });
};
