// GET /admin/summaries/:NNN (#173) — legacy entry point. The detail page is
// keyed by link id (/admin/links/:id) so blocked/failed runs are inspectable
// too; this route resolves the NNN to its latest link and 302s there.
// Raw JSON stays at /api/summaries/:NNN — untouched.

import { authorize, type Env } from "../../_lib/auth";
import { renderErrorPage } from "../../_lib/summary_page";

function html(markup: string, status = 200): Response {
  return new Response(markup, { status, headers: { "content-type": "text/html; charset=utf-8" } });
}

export const onRequestGet: PagesFunction<Env> = async ({ request, env, params }) => {
  const who = await authorize(request, env);
  if (!who) return new Response("unauthorized", { status: 401 });

  const id = String(params.id);
  if (!/^\d{3,}$/.test(id)) return html(renderErrorPage(`Summary ${id}`, "Invalid id — expected a zero-padded NNN like 003."), 400);

  const link = await env.DB.prepare("SELECT id FROM links WHERE summary_id = ? ORDER BY id DESC LIMIT 1")
    .bind(id)
    .first<{ id: number }>();
  if (!link) {
    return html(
      renderErrorPage(
        `Summary ${id}`,
        "No link references this NNN (deleted, or pushed via the local fallback). Raw JSON: /api/summaries/" + id + ".",
      ),
      404,
    );
  }

  return new Response(null, { status: 302, headers: { location: `/admin/links/${link.id}` } });
};
