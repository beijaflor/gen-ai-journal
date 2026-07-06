// GET /api/pipeline (#161) — joined operational view for the admin console:
// cycle state, per-status counts, token totals, and all links with run metrics.

import { authorize, type Env } from "../_lib/auth";
import { error, json } from "../_lib/util";
import { getCycle } from "../_lib/summaries";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  const [cycle, links, summaryCount] = await Promise.all([
    getCycle(env as never),
    env.DB.prepare(
      "SELECT id, url, note, status, error, summary_id, submitted_at, processed_at, fetch_ms, ai_ms, tokens_in, tokens_out FROM links ORDER BY submitted_at DESC",
    ).all(),
    env.DB.prepare("SELECT status, COUNT(*) AS n FROM summaries GROUP BY status").all<{ status: string; n: number }>(),
  ]);

  const counts: Record<string, number> = {};
  let tokensIn = 0;
  let tokensOut = 0;
  let lastProcessed: string | null = null;
  for (const l of links.results as Record<string, never>[]) {
    counts[l.status as string] = (counts[l.status as string] ?? 0) + 1;
    tokensIn += (l.tokens_in as number) ?? 0;
    tokensOut += (l.tokens_out as number) ?? 0;
    const p = l.processed_at as string | null;
    if (p && (!lastProcessed || p > lastProcessed)) lastProcessed = p;
  }

  return json({
    cycle: cycle ? { journal_date: cycle.journalDate, next_summary_id: cycle.nextId } : null,
    counts,
    tokens: { in: tokensIn, out: tokensOut },
    last_processed_at: lastProcessed,
    summaries: Object.fromEntries((summaryCount.results ?? []).map((r) => [r.status, r.n])),
    links: links.results,
  });
};
