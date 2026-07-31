// GET /admin/links/:id (#173) — server-rendered link detail page, keyed by
// the technical link id so EVERY submitted link — blocked/failed runs that
// never earned an NNN included — is inspectable: status, content (when
// summarized), actions (dismiss / re-open / retry / re-summarize), per-run
// event log. The primary wall is Cloudflare Access on /admin/* (edge 302
// before this runs); authorize() here is defense-in-depth only.

import { authorize, type Env } from "../../_lib/auth";
import { renderErrorPage, renderLinkPage, type LinkRow, type SummaryRow } from "../../_lib/summary_page";

function html(markup: string, status = 200): Response {
  return new Response(markup, { status, headers: { "content-type": "text/html; charset=utf-8" } });
}

export const onRequestGet: PagesFunction<Env> = async ({ request, env, params }) => {
  const who = await authorize(request, env);
  if (!who) return new Response("unauthorized", { status: 401 });

  const raw = String(params.id);
  if (!/^\d+$/.test(raw)) return html(renderErrorPage(`Link ${raw}`, "Invalid id — expected a numeric link id like 7."), 400);
  const id = Number(raw);

  const link = await env.DB.prepare(
    "SELECT id, url, note, status, error, summary_id, submitted_at, processed_at, fetch_ms, ai_ms, tokens_in, tokens_out FROM links WHERE id = ?",
  )
    .bind(id)
    .first<LinkRow>();
  if (!link) return html(renderErrorPage(`Link L${id}`, "No link with this id — it may have been deleted. Events survive at /admin/logs."), 404);

  // The admin detail covers the current cycle: the workdesk row only.
  // Published rows remain reachable via /api/summaries/:id?journal_date=….
  let summary: SummaryRow | null = null;
  if (link.summary_id) {
    summary =
      (await env.DB.prepare(
        "SELECT id, journal_date, url, content, status, pushed_at, updated_at FROM summaries WHERE id = ? AND journal_date IS NULL",
      )
        .bind(link.summary_id)
        .first<SummaryRow>()) ?? null;
  }

  return html(renderLinkPage(link, summary));
};
