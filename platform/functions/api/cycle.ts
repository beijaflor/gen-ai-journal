// /api/cycle — the cycle/ID registry (#160)
//   GET:  current journal date + next NNN (public — no secrets)
//   POST: rollover {date, next_id?} (bearer/Access)

import { authorize, type Env } from "../_lib/auth";
import { error, json } from "../_lib/util";
import { getCycle } from "../_lib/summaries";

export const onRequestGet: PagesFunction<Env> = async ({ env }) => {
  const cycle = await getCycle(env);
  if (!cycle) return json({ active: false });
  return json({ active: true, journal_date: cycle.journalDate, next_summary_id: cycle.nextId });
};

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const who = await authorize(request, env);
  if (!who) return error("unauthorized", 401);

  let body: { date?: string; next_id?: number };
  try {
    body = await request.json();
  } catch {
    return error("body must be JSON: {date, next_id?}", 400);
  }
  const date = body.date ?? "";
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return error("date must be YYYY-MM-DD", 400);
  const nextId = body.next_id ?? 1;
  if (!Number.isInteger(nextId) || nextId < 1) return error("next_id must be a positive integer", 400);

  // During parallel-run, seed next_id from the real sources.md max ID + 1
  // to keep the counter collision-free with locally assigned IDs.
  await env.DB.batch([
    env.DB.prepare(
      "INSERT INTO settings (key, value) VALUES ('current_journal_date', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
    ).bind(date),
    env.DB.prepare(
      "INSERT INTO settings (key, value) VALUES ('next_summary_id', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
    ).bind(String(nextId)),
  ]);
  return json({ active: true, journal_date: date, next_summary_id: nextId });
};
