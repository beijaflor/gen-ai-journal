// GET /admin/summaries/:id (#173) — server-rendered summary detail page.
// The primary wall is Cloudflare Access on /admin/* (edge 302 before this
// runs); authorize() here is defense-in-depth only. Raw JSON stays at
// /api/summaries/:id — this page is the human view: content, link + run
// metrics, actions (dismiss / re-open / re-summarize), per-run event log.

import { authorize, type Env } from "../../_lib/auth";
import { renderErrorPage, renderSummaryPage, type LinkRow, type SummaryRow } from "../../_lib/summary_page";

function html(markup: string, status = 200): Response {
  return new Response(markup, { status, headers: { "content-type": "text/html; charset=utf-8" } });
}

export const onRequestGet: PagesFunction<Env> = async ({ request, env, params }) => {
  const who = await authorize(request, env);
  if (!who) return new Response("unauthorized", { status: 401 });

  const id = String(params.id);
  if (!/^\d{3,}$/.test(id)) return html(renderErrorPage(id, "Invalid id — expected a zero-padded NNN like 003."), 400);

  // The admin detail covers the current cycle: the workdesk row only.
  // Published rows remain reachable via /api/summaries/:id?journal_date=….
  const summary = await env.DB.prepare(
    "SELECT id, journal_date, url, content, status, pushed_at, updated_at FROM summaries WHERE id = ? AND journal_date IS NULL",
  )
    .bind(id)
    .first<SummaryRow>();
  if (!summary) {
    return html(renderErrorPage(id, "No workdesk summary with this NNN. Published rows: /api/summaries/" + id + "?journal_date=YYYY-MM-DD."), 404);
  }

  const link = await env.DB.prepare(
    "SELECT id, url, note, status, error, submitted_at, processed_at, fetch_ms, ai_ms, tokens_in, tokens_out FROM links WHERE summary_id = ? ORDER BY id DESC LIMIT 1",
  )
    .bind(id)
    .first<LinkRow>();

  return html(renderSummaryPage(summary, link ?? null));
};
