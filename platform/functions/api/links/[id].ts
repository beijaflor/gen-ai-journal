// PATCH /api/links/:id — update status (new | consumed | dismissed).
// Setting a blocked link back to "new" is the RETRY path: the error is
// cleared and the summarization DO is kicked (#161).

import { authorize, type Env } from "../../_lib/auth";
import { enqueueSummarization } from "../../_lib/enqueue";
import { error, json } from "../../_lib/util";

export const onRequestPatch: PagesFunction<Env> = async ({ request, env, params, waitUntil }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  const id = Number(params.id);
  if (!Number.isInteger(id) || id < 1) return error("invalid id", 400);

  let body: { status?: string };
  try {
    body = await request.json();
  } catch {
    return error("body must be JSON: {status}", 400);
  }
  const status = body.status;
  if (status !== "new" && status !== "dismissed") {
    return error("status must be one of: new, dismissed", 400);
  }

  const res = await env.DB.prepare(
    "UPDATE links SET status = ?, error = CASE WHEN ? = 'new' THEN NULL ELSE error END WHERE id = ? RETURNING id, url, status, summary_id",
  )
    .bind(status, status, id)
    .first<{ id: number; url: string; status: string; summary_id: string | null }>();
  if (!res) return error("link not found", 404);

  if (status === "dismissed" && res.summary_id) {
    // Dismiss is a reversible flag — the summary row stays, marked dismissed.
    // Published rows are never touched.
    await env.DB.prepare("UPDATE summaries SET status = 'dismissed' WHERE id = ? AND journal_date IS NULL AND status = 'workdesk'")
      .bind(res.summary_id)
      .run();
  }
  if (status === "new") {
    if (res.summary_id) {
      // Re-open of a summarized link just flips the flag back — never regenerates.
      const flipped = await env.DB.prepare(
        "UPDATE summaries SET status = 'workdesk' WHERE id = ? AND journal_date IS NULL AND status = 'dismissed' RETURNING id",
      )
        .bind(res.summary_id)
        .first();
      if (flipped) {
        await env.DB.prepare("UPDATE links SET status = 'summarized' WHERE id = ?").bind(id).run();
        return json({ ...res, status: "summarized" });
      }
    }
    const kick = enqueueSummarization(env); // blocked/never-summarized: real retry
    if (kick) waitUntil(kick);
  }
  return json(res);
};
