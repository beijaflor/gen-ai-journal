// /api/summaries — the summary collection (#160)
//   POST: bulk upsert (bearer/Access) — the fallback-push loading dock
//   GET:  list (public; summaries are public on the site today)

import { authorize, type Env } from "../../_lib/auth";
import { error, json } from "../../_lib/util";
import { displayTitle, writeSummary, type SummaryInput } from "../../_lib/summaries";

const VALID_STATUSES = ["workdesk", "published", "blocked", "dismissed"] as const;

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  let body: { summaries?: SummaryInput[] };
  try {
    body = await request.json();
  } catch {
    return error("body must be JSON: {summaries: [{id, journalDate?, content}]}", 400);
  }
  const items = body.summaries;
  if (!Array.isArray(items) || items.length === 0) return error("summaries must be a non-empty array", 400);
  if (items.length > 500) return error("max 500 summaries per request", 400);

  const results = [];
  for (const item of items) {
    try {
      results.push(await writeSummary(env, item));
    } catch (e) {
      results.push({ ok: false, id: item?.id, error: String(e) });
    }
  }
  const failed = results.filter((r) => !r.ok).length;
  return json({ results, count: results.length, failed }, failed ? 207 : 200);
};

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const params = new URL(request.url).searchParams;
  const status = params.get("status");
  const journalDate = params.get("journal_date");
  if (status && !VALID_STATUSES.includes(status as never)) {
    return error(`status must be one of: ${VALID_STATUSES.join(", ")}`, 400);
  }

  const where: string[] = [];
  const binds: string[] = [];
  if (status) {
    where.push("status = ?");
    binds.push(status);
  }
  if (journalDate !== null) {
    // journal_date= (empty) selects workdesk rows (NULL journal_date)
    if (journalDate === "") where.push("journal_date IS NULL");
    else {
      where.push("journal_date = ?");
      binds.push(journalDate);
    }
  }
  const sql =
    "SELECT id, journal_date, url, content, status, pushed_at, updated_at FROM summaries" +
    (where.length ? ` WHERE ${where.join(" AND ")}` : "") +
    " ORDER BY id ASC";
  const { results } = await env.DB.prepare(sql).bind(...binds).all<Record<string, string>>();

  return json({
    summaries: results.map((r) => ({
      id: r.id,
      journal_date: r.journal_date,
      url: r.url,
      title: displayTitle(r.content),
      status: r.status,
      pushed_at: r.pushed_at,
      updated_at: r.updated_at,
    })),
    count: results.length,
  });
};
