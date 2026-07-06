// GET /api/summaries/:id — full summary content (public read).
// Default: the workdesk row (journal_date IS NULL); ?journal_date=YYYY-MM-DD for published rows.

import type { Env } from "../../_lib/auth";
import { error, json } from "../../_lib/util";
import { isBlockedStub } from "../../_lib/summaries";

export const onRequestGet: PagesFunction<Env> = async ({ request, env, params }) => {
  const id = String(params.id);
  if (!/^\d{3,}$/.test(id)) return error("invalid id", 400);
  const journalDate = new URL(request.url).searchParams.get("journal_date");

  const row = await env.DB.prepare(
    "SELECT id, journal_date, url, content, status, pushed_at, updated_at FROM summaries WHERE id = ? AND ifnull(journal_date,'') = ifnull(?, '')",
  )
    .bind(id, journalDate || null)
    .first<Record<string, string>>();
  if (!row) {
    // Numbering is confusing enough to deserve a self-explaining 404 (NNN is
    // per-cycle and only assigned on successful summarization).
    const scope = journalDate ? `journal_date=${journalDate}` : "the workdesk (no journal_date)";
    const { results } = await env.DB.prepare(
      "SELECT id FROM summaries WHERE ifnull(journal_date,'') = ifnull(?, '') ORDER BY id",
    )
      .bind(journalDate || null)
      .all<{ id: string }>();
    return json(
      {
        error: `no summary ${id} in ${scope}`,
        hint: "NNN ids are per-cycle and exist only after successful summarization; gaps mean a retracted (dismissed) summary. For published journals pass ?journal_date=YYYY-MM-DD.",
        available_ids: results.map((r) => r.id),
      },
      404,
    );
  }

  let content: unknown = row.content;
  if (!isBlockedStub(row.content)) {
    try {
      content = JSON.parse(row.content);
    } catch {
      // stored verbatim; return as string if unparseable
    }
  }
  return json({
    id: row.id,
    journal_date: row.journal_date,
    url: row.url,
    status: row.status,
    pushed_at: row.pushed_at,
    updated_at: row.updated_at,
    content,
  });
};
