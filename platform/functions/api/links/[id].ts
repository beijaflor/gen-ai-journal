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
  if (status !== "new" && status !== "consumed" && status !== "dismissed") {
    return error("status must be one of: new, consumed, dismissed", 400);
  }

  const consumedAt = status === "consumed" ? new Date().toISOString() : null;
  const res = await env.DB.prepare(
    "UPDATE links SET status = ?, consumed_at = ?, error = CASE WHEN ? = 'new' THEN NULL ELSE error END WHERE id = ? RETURNING id, url, status, consumed_at",
  )
    .bind(status, consumedAt, status, id)
    .first();
  if (!res) return error("link not found", 404);
  if (status === "new") {
    const kick = enqueueSummarization(env);
    if (kick) waitUntil(kick);
  }
  return json(res);
};
