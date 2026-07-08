// PATCH /api/links/:id — update status (new | consumed | dismissed).
// Setting a blocked link back to "new" is the RETRY path: the error is
// cleared and the summarization DO is kicked (#161).

import { authorize, type Env } from "../../_lib/auth";
import { enqueueSummarization } from "../../_lib/enqueue";
import { logEvent } from "../../_lib/events";
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

  // Prior status decides which trigger event the log gets (retry vs
  // re-summarize vs re-open) — RETURNING only yields post-update values.
  const prior = await env.DB.prepare("SELECT status FROM links WHERE id = ?")
    .bind(id)
    .first<{ status: string }>();
  if (!prior) return error("link not found", 404);

  const res = await env.DB.prepare(
    "UPDATE links SET status = ?, error = CASE WHEN ? = 'new' THEN NULL ELSE error END WHERE id = ? RETURNING id, url, status, summary_id",
  )
    .bind(status, status, id)
    .first<{ id: number; url: string; status: string; summary_id: string | null }>();
  if (!res) return error("link not found", 404);

  if (status === "dismissed") {
    let flagged = null;
    if (res.summary_id) {
      // Dismiss is a reversible flag — the summary row stays, marked dismissed.
      // Published rows are never touched.
      flagged = await env.DB.prepare(
        "UPDATE summaries SET status = 'dismissed' WHERE id = ? AND journal_date IS NULL AND status = 'workdesk' RETURNING id",
      )
        .bind(res.summary_id)
        .first();
    }
    await logEvent(env.DB, {
      actor: "editor",
      event: "link.dismissed",
      linkId: id,
      summaryId: res.summary_id,
      detail: { url: res.url, by: who },
    });
    if (flagged) {
      await logEvent(env.DB, { actor: "editor", event: "summary.dismissed", linkId: id, summaryId: res.summary_id, detail: { by: who } });
    }
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
        await logEvent(env.DB, { actor: "editor", event: "link.reopened", linkId: id, summaryId: res.summary_id, detail: { url: res.url, by: who } });
        await logEvent(env.DB, { actor: "editor", event: "summary.restored", linkId: id, summaryId: res.summary_id, detail: { by: who } });
        return json({ ...res, status: "summarized" });
      }
    }
    // The trigger event names the editor's intent (#178): retry of a blocked
    // link, re-summarize of a live one, or a plain re-open/requeue.
    const event =
      prior.status === "blocked"
        ? "link.retried"
        : prior.status === "summarized"
          ? "link.resummarize_requested"
          : "link.reopened";
    await logEvent(env.DB, {
      actor: "editor",
      event,
      linkId: id,
      summaryId: res.summary_id,
      detail: { url: res.url, by: who, requeued: true },
    });
    const kick = enqueueSummarization(env); // blocked/never-summarized: real retry
    if (kick) waitUntil(kick);
  }
  return json(res);
};
