// Link detail page renderer (#173) — pure HTML-building for
// /admin/links/<id>. Keyed by link id so EVERY submitted link — blocked and
// failed runs included, which never earn an NNN — has an inspectable page
// with its per-run summarization log. Kept out of the route file so vitest
// can pin the invariants (dismissed hides body, user content is escaped)
// without a D1.
//
// Everything that originates from the DB or the LLM goes through esc();
// the only unescaped interpolations are safeJson() (for the client script)
// and fixed literals.

export interface SummaryRow {
  id: string;
  journal_date: string | null;
  url: string | null;
  content: string;
  status: string; // workdesk | published | blocked | dismissed
  pushed_at: string | null;
  updated_at: string | null;
}

export interface LinkRow {
  id: number;
  url: string;
  note: string | null;
  status: string; // new | queued | summarized | blocked | dismissed
  error: string | null;
  summary_id: string | null;
  submitted_at: string | null;
  processed_at: string | null;
  fetch_ms: number | null;
  ai_ms: number | null;
  tokens_in: number | null;
  tokens_out: number | null;
}

export function esc(v: unknown): string {
  return String(v ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** JSON for inline <script> consts — <-escaped so "</script>" can't break out. */
function safeJson(v: unknown): string {
  return JSON.stringify(v).replace(/</g, "\\u003c");
}

function isHttpUrl(u: unknown): boolean {
  return typeof u === "string" && /^https?:\/\//i.test(u);
}

/** Clickable only when it looks like http(s); otherwise plain escaped text. */
function urlHtml(u: unknown): string {
  if (!u) return "–";
  return isHttpUrl(u)
    ? `<a href="${esc(u)}" target="_blank" rel="noreferrer">${esc(u)}</a>`
    : esc(u);
}

function fmtMs(ms: number | null | undefined): string {
  if (ms == null) return "–";
  return ms >= 1000 ? (ms / 1000).toFixed(1) + "s" : ms + "ms";
}

function fmtTs(ts: string | null | undefined): string {
  return ts ? esc(ts.slice(0, 19).replace("T", " ")) : "–";
}

const SCORE_KEYS = ["signal", "depth", "uniqueness", "practical", "antiHype", "mainJournal", "annexPotential", "overall"] as const;

const STYLE = `
    :root { --accent: #d96b0b; --line: #ddd8ce; --muted: #6a6f7a; --ok: #22633c; --bad: #a33326; }
    body { font-family: system-ui, sans-serif; max-width: 860px; margin: 5vh auto; padding: 0 20px 60px; color: #21252d; line-height: 1.6; }
    h1 { font-size: 22px; margin: 0 0 4px; display: flex; align-items: center; gap: 10px; }
    h1 .nnn { font-size: 15px; color: var(--accent); }
    p.sub { color: var(--muted); margin: 0 0 20px; font-size: 13.5px; }
    section { border: 1px solid var(--line); border-radius: 6px; padding: 16px 20px; margin-bottom: 16px; background: #fff; }
    section h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .07em; color: var(--muted); margin: 0 0 10px; }
    .title { font-size: 18px; font-weight: 700; margin: 0 0 2px; }
    .orig { color: var(--muted); font-size: 13px; margin: 0 0 10px; }
    .chips { margin: 0 0 12px; }
    .chip { display: inline-block; font-size: 11.5px; padding: 1px 10px; border-radius: 20px; background: #f2efe9; margin: 0 5px 5px 0; }
    .chip.kind { background: #e8eef5; color: #33567a; }
    .lead { border-left: 3px solid var(--accent); padding: 2px 12px; margin: 0 0 14px; font-weight: 600; }
    .body p { margin: 0 0 10px; font-size: 14.5px; }
    .pill { font-size: 11px; padding: 1px 9px; border-radius: 20px; background: #eee; white-space: nowrap; font-weight: 400; }
    .pill.workdesk, .pill.summarized { background: #e8eef5; color: #33567a; }
    .pill.published, .pill.new { background: #e7f2ea; color: var(--ok); }
    .pill.queued { background: #fdf3e4; color: #8a5307; }
    .pill.blocked { background: #fbe9e7; color: var(--bad); }
    .pill.dismissed { background: #f0f0ee; color: #888; }
    .notice { border: 1px dashed var(--line); border-radius: 6px; background: #faf9f6; color: var(--muted); padding: 14px 18px; font-size: 14px; margin-bottom: 16px; }
    pre.raw { background: #faf9f6; border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; font-size: 12.5px; overflow-x: auto; white-space: pre-wrap; word-break: break-word; }
    table { border-collapse: collapse; width: 100%; font-size: 13px; }
    th { text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); padding: 5px 10px 5px 0; border-bottom: 1px solid var(--line); white-space: nowrap; }
    td { padding: 5px 10px 5px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
    td.num { font-variant-numeric: tabular-nums; white-space: nowrap; }
    .kv td:first-child { color: var(--muted); white-space: nowrap; width: 120px; }
    .kv td { word-break: break-all; }
    .tbl-wrap { overflow-x: auto; }
    .err { color: var(--bad); }
    .actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
    .actions button { font-size: 13px; border: 1px solid var(--line); background: #fff; border-radius: 5px; padding: 5px 14px; cursor: pointer; }
    .actions button.warn { border-color: var(--accent); color: var(--accent); font-weight: 600; }
    .actions .hint { font-size: 12px; color: var(--muted); align-self: center; }
    #log td.ts { white-space: nowrap; color: var(--muted); font-variant-numeric: tabular-nums; }
    #log td.ev { font-family: ui-monospace, monospace; font-size: 11.5px; white-space: nowrap; }
    #log .pill.editor { background: #e8eef5; color: #33567a; }
    #log .pill.pipeline { background: #fdf3e4; color: #8a5307; }
    #log .pill.system { background: #f0f0ee; color: #888; }
    #log td.detail { color: #444; font-size: 12.5px; word-break: break-word; }
    nav { margin-top: 22px; font-size: 13.5px; }
    nav a { color: var(--accent); margin-right: 16px; }
`;

function shell(title: string, body: string): string {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>${esc(title)}</title>
  <style>${STYLE}</style>
</head>
<body>
${body}
</body>
</html>
`;
}

export function renderErrorPage(subject: string, message: string): string {
  return shell(
    `${subject} — gen-ai-journal`,
    `  <h1>${esc(subject)}</h1>
  <div class="notice">${esc(message)}</div>
  <nav><a href="/admin/pipeline">console</a><a href="/inbox">inbox</a><a href="/admin/logs">events log</a></nav>`,
  );
}

/** Rich render of summary-v1 JSON; falls back to <pre> for stubs/unparseable.
 * Pure content — show or nothing; all status messaging lives in the result
 * overview. Callers skip this entirely for dismissed summaries. */
function contentHtml(s: SummaryRow): string {
  const raw = s.content ?? "";
  if (raw.trimStart().startsWith("BLOCKED")) {
    return `<section><h2>Blocked stub</h2><pre class="raw">${esc(raw)}</pre></section>`;
  }
  let c: Record<string, unknown> | null = null;
  try {
    c = (JSON.parse(raw) as { content?: Record<string, unknown> })?.content ?? null;
  } catch {
    /* fall through to raw */
  }
  if (!c) {
    return `<section><h2>Stored content (unparseable as summary-v1)</h2><pre class="raw">${esc(raw)}</pre></section>`;
  }

  const chips: string[] = [];
  if (c.language) chips.push(`<span class="chip kind">lang: ${esc(c.language)}</span>`);
  if (c.contentType) chips.push(`<span class="chip kind">${esc(c.contentType)}</span>`);
  for (const t of Array.isArray(c.topics) ? c.topics : []) chips.push(`<span class="chip">${esc(t)}</span>`);

  const paragraphs = String(c.summaryBody ?? "")
    .split(/\n{2,}/)
    .filter((p) => p.trim())
    .map((p) => `<p>${esc(p.trim()).replace(/\n/g, "<br>")}</p>`)
    .join("\n      ");

  const scores = (c.scores ?? {}) as Record<string, unknown>;
  const scoreTable = `<div class="tbl-wrap"><table>
      <thead><tr>${SCORE_KEYS.map((k) => `<th>${k}</th>`).join("")}</tr></thead>
      <tbody><tr>${SCORE_KEYS.map((k) => `<td class="num">${esc(scores[k] ?? "–")}</td>`).join("")}</tr></tbody>
    </table></div>`;

  return `<section>
    <div class="title">${esc(c.title ?? "(untitled)")}</div>
    ${c.originalTitle ? `<div class="orig">原題: ${esc(c.originalTitle)}</div>` : ""}
    <div class="chips">${chips.join("")}</div>
    ${c.oneSentenceSummary ? `<div class="lead">${esc(c.oneSentenceSummary)}</div>` : ""}
    <div class="body">
      ${paragraphs || "<p>(empty summaryBody)</p>"}
    </div>
    <h2 style="margin-top:14px">Scores</h2>
    ${scoreTable}
  </section>`;
}

/** Result overview — the run's outcome at a glance, shown FIRST (before the
 * log): status headline for every state (blocked reason, success NNN,
 * dismissed, generating/queued) plus the last-run metrics. */
function resultOverviewHtml(link: LinkRow, summary: SummaryRow | null): string {
  let headline: string;
  if (link.status === "blocked") {
    headline = `<div class="notice"><span class="err" style="font-weight:600">blocked</span> —
    fail-closed: no summary was written, no NNN spent. Retry below, or regenerate locally and push (#168).</div>`;
  } else if (link.status === "dismissed") {
    headline = summary
      ? `<div class="notice">Dismissed — content hidden while dismissed. Re-open below to restore it instantly (no regeneration, no token spend; the row still exists).</div>`
      : `<div class="notice">Dismissed before a summary was produced — re-open below to queue it.</div>`;
  } else if (summary) {
    headline = `<div class="notice">Summarized into <span class="nnn">NNN ${esc(summary.id)}</span> — content below the log.</div>`;
  } else {
    headline = `<div class="notice">No summary yet — the pipeline ${link.status === "queued" ? "has queued this link" : "will pick this link up shortly"}.</div>`;
  }

  const rows: string[] = [];
  if (link.status === "blocked") {
    rows.push(`<tr><td>reason</td><td class="err">${esc(link.error ?? "(no reason recorded)")}</td></tr>`);
  }
  if (summary) {
    rows.push(
      `<tr><td>summary</td><td><span class="nnn">NNN ${esc(summary.id)}</span> <span class="pill ${esc(summary.status)}">${esc(summary.status)}</span></td></tr>`,
    );
  }
  if (link.processed_at) {
    rows.push(
      `<tr><td>last run</td><td>${fmtTs(link.processed_at)} · fetch ${fmtMs(link.fetch_ms)} + ai ${fmtMs(link.ai_ms)} · tokens ${link.tokens_in != null ? `${esc(link.tokens_in)}/${esc(link.tokens_out ?? "–")}` : "–"}</td></tr>`,
    );
  }

  return `<section id="result"><h2>Result</h2>
    ${headline}${rows.length ? `\n    <table class="kv"><tbody>\n      ${rows.join("\n      ")}\n    </tbody></table>` : ""}
  </section>`;
}

function actionButtons(link: LinkRow): string {
  const btn = (label: string, status: string, confirmMsg: string, warn = false) =>
    `<button data-status="${esc(status)}" data-confirm="${esc(confirmMsg)}"${warn ? ' class="warn"' : ""}>${esc(label)}</button>`;

  const btns: string[] = [];
  let hint = "";
  if (link.status === "dismissed") {
    btns.push(btn("re-open", "new", ""));
    hint = "re-open restores a dismissed summary instantly (no regeneration, no token spend)";
  } else {
    if (link.status === "summarized") {
      btns.push(
        btn(
          "re-summarize",
          "new",
          "Re-run the pipeline for this link?\n\nThis OVERWRITES the content under the same NNN and spends tokens.",
          true,
        ),
      );
    }
    if (link.status === "blocked") {
      btns.push(btn("retry", "new", "Retry summarization for this link? It spends tokens.", true));
    }
    btns.push(btn("dismiss", "dismissed", ""));
    if (link.status === "summarized") hint = "dismiss is a reversible flag; re-summarize reuses this NNN";
  }
  return `<div class="actions">${btns.join("")}${hint ? `<span class="hint">${esc(hint)}</span>` : ""}</div>`;
}

function linkSectionHtml(link: LinkRow): string {
  const label = link.status === "new" ? "generating" : link.status;
  return `<section><h2>Link</h2>
    <table class="kv"><tbody>
      <tr><td>url</td><td>${urlHtml(link.url)}</td></tr>
      <tr><td>link</td><td>L${Number(link.id)} <span class="pill ${esc(link.status)}">${esc(label)}</span></td></tr>
      ${link.note ? `<tr><td>note</td><td>${esc(link.note)}</td></tr>` : ""}
      <tr><td>submitted</td><td>${fmtTs(link.submitted_at)}</td></tr>
    </tbody></table>
    ${actionButtons(link)}
  </section>`;
}

// Client script: fixed code — the only dynamic value is the PAGE const,
// injected via safeJson(). Log rows are built with textContent (no innerHTML).
const CLIENT_SCRIPT = `
    async function act(status, confirmMsg) {
      if (confirmMsg && !window.confirm(confirmMsg)) return;
      const res = await fetch("/api/links/" + PAGE.linkId, {
        method: "PATCH",
        headers: { "content-type": "application/json" },
        credentials: "same-origin",
        body: JSON.stringify({ status }),
      });
      if (!res.ok) { alert("action failed (" + res.status + ")"); return; }
      location.reload();
    }
    document.querySelectorAll(".actions button").forEach((b) => {
      b.onclick = () => { b.disabled = true; act(b.dataset.status, b.dataset.confirm).finally(() => { b.disabled = false; }); };
    });

    function fmtDetail(raw) {
      if (!raw) return "";
      let obj;
      try { obj = JSON.parse(raw); } catch { return raw; }
      return Object.entries(obj)
        .filter(([, v]) => v !== null && v !== undefined && v !== "")
        .map(([k, v]) => { const s = String(v); return k + "=" + (s.length > 110 ? s.slice(0, 110) + "…" : s); })
        .join(" · ");
    }

    async function loadLog() {
      const qs = ["link_id=" + PAGE.linkId];
      if (PAGE.summaryId != null) qs.push("summary_id=" + encodeURIComponent(PAGE.summaryId));
      const lists = await Promise.all(qs.map(async (q) => {
        const res = await fetch("/api/events?limit=200&" + q, { credentials: "same-origin" });
        return res.ok ? (await res.json()).events : [];
      }));
      const seen = new Set();
      const events = [];
      for (const e of lists.flat()) {
        if (seen.has(e.id)) continue;
        seen.add(e.id);
        events.push(e);
      }
      events.sort((a, b) => b.id - a.id); // newest first
      const rows = document.getElementById("log-rows");
      rows.innerHTML = "";
      document.getElementById("log-empty").hidden = events.length !== 0;
      for (const e of events) {
        const tr = document.createElement("tr");
        const ts = document.createElement("td"); ts.className = "ts"; ts.textContent = (e.ts || "").slice(0, 19).replace("T", " ");
        const actor = document.createElement("td");
        const pill = document.createElement("span"); pill.className = "pill " + e.actor; pill.textContent = e.actor;
        actor.appendChild(pill);
        const ev = document.createElement("td"); ev.className = "ev"; ev.textContent = e.event;
        const detail = document.createElement("td"); detail.className = "detail"; detail.textContent = fmtDetail(e.detail);
        tr.appendChild(ts); tr.appendChild(actor); tr.appendChild(ev); tr.appendChild(detail);
        rows.appendChild(tr);
      }
    }
    loadLog();
`;

export function renderLinkPage(link: LinkRow, summary: SummaryRow | null): string {
  const page = { linkId: link.id, summaryId: summary ? summary.id : null };
  const label = link.status === "new" ? "generating" : link.status;
  const sub = summary
    ? `${summary.journal_date ? `journal ${esc(summary.journal_date)}` : "workdesk (current cycle)"} · summary <span class="pill ${esc(summary.status)}">${esc(summary.status)}</span> · pushed ${fmtTs(summary.pushed_at)} · updated ${fmtTs(summary.updated_at)} · <a href="/api/summaries/${esc(summary.id)}" target="_blank" style="color:var(--accent)">raw JSON</a>`
    : `no NNN allocated${link.status === "blocked" ? " (fail-closed — nothing spent)" : ""} · submitted ${fmtTs(link.submitted_at)}`;
  const body = `  <h1>L${Number(link.id)} <span class="pill ${esc(link.status)}">${esc(label)}</span>${summary ? ` <span class="nnn">NNN ${esc(summary.id)}</span>` : ""}</h1>
  <p class="sub">${sub}</p>

${resultOverviewHtml(link, summary)}

  <section id="log"><h2>Summarization log</h2>
    <div class="tbl-wrap"><table>
      <thead><tr><th>time (UTC)</th><th>actor</th><th>event</th><th>detail</th></tr></thead>
      <tbody id="log-rows"></tbody>
    </table></div>
    <div id="log-empty" hidden style="color:var(--muted);font-size:13px;padding:10px 0 0">No events recorded for this link.</div>
  </section>

${summary && summary.status !== "dismissed" ? contentHtml(summary) : ""}

${linkSectionHtml(link)}

  <nav><a href="/admin/pipeline">console</a><a href="/inbox">inbox</a><a href="/admin/logs">events log</a><a href="/submit">submit</a></nav>

  <script>
    const PAGE = ${safeJson(page)};
${CLIENT_SCRIPT}  </script>`;
  return shell(`Link L${Number(link.id)} — gen-ai-journal`, body);
}
