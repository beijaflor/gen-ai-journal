// Shared write path to the summary collection (#160).
// Used by BOTH the HTTP endpoints (fallback pushes) and the summarization
// pipeline (#166) — one code path to the table.

import type { Env } from "./auth";

export interface SummaryInput {
  id?: string; // per-cycle NNN; omit to allocate from the registry
  journalDate?: string | null;
  content: string; // raw file content: summary-v1 JSON text OR a "BLOCKED:" text stub
}

export interface WriteResult {
  ok: boolean;
  id?: string;
  status?: string;
  action?: "inserted" | "updated";
  error?: string;
}

export function isBlockedStub(raw: string): boolean {
  return raw.trimStart().startsWith("BLOCKED");
}

/** Parse and minimally validate summary-v1 JSON. Returns {url, title} or an error. */
export function inspectSummary(raw: string): { url?: string; title?: string; error?: string } {
  let parsed: any;
  try {
    parsed = JSON.parse(raw);
  } catch {
    return { error: "content is neither valid JSON nor a BLOCKED stub" };
  }
  const c = parsed?.content;
  if (!parsed?.metadata?.version) return { error: "missing metadata.version" };
  if (!c?.title) return { error: "missing content.title" };
  if (!c?.url) return { error: "missing content.url" };
  if (!c?.summaryBody) return { error: "missing content.summaryBody" };
  return { url: c.url, title: c.title };
}

/** Extract the source URL from a blocked stub ("- URL: https://..." line). */
export function blockedStubUrl(raw: string): string | null {
  const m = raw.match(/^- URL:\s*(\S+)/m);
  return m ? m[1] : null;
}

/** Atomically allocate the next NNN from the registry. Throws if no cycle is set. */
export async function allocateId(env: Env): Promise<string> {
  const row = await env.DB.prepare(
    "UPDATE settings SET value = CAST(value AS INTEGER) + 1 WHERE key = 'next_summary_id' RETURNING CAST(value AS INTEGER) - 1 AS allocated",
  ).first<{ allocated: number }>();
  if (!row) throw new Error("no active cycle — POST /api/cycle first");
  return String(row.allocated).padStart(3, "0");
}

export async function getCycle(env: Env): Promise<{ journalDate: string; nextId: number } | null> {
  const { results } = await env.DB.prepare(
    "SELECT key, value FROM settings WHERE key IN ('current_journal_date', 'next_summary_id')",
  ).all<{ key: string; value: string }>();
  const map = Object.fromEntries(results.map((r) => [r.key, r.value]));
  if (!map.current_journal_date) return null;
  return { journalDate: map.current_journal_date, nextId: Number(map.next_summary_id ?? "1") };
}

/**
 * Validate + upsert one summary. `id` must be supplied (fallback pushes) or
 * pre-allocated via allocateId() (pipeline). Upsert key: (id, journal_date).
 */
export async function writeSummary(env: Env, input: SummaryInput): Promise<WriteResult> {
  const raw = input.content;
  if (typeof raw !== "string" || !raw.trim()) return { ok: false, error: "content must be a non-empty string" };
  if (!input.id || !/^\d{3,}$/.test(input.id)) return { ok: false, error: "id must be a zero-padded number string" };

  let status: string;
  let url: string | null;
  if (isBlockedStub(raw)) {
    status = "blocked";
    url = blockedStubUrl(raw);
    if (!url) return { ok: false, error: "blocked stub has no '- URL:' line" };
  } else {
    const info = inspectSummary(raw);
    if (info.error) return { ok: false, error: info.error };
    status = "workdesk";
    url = info.url!;
  }

  const jd = input.journalDate ?? null;
  const now = new Date().toISOString();
  const updated = await env.DB.prepare(
    "UPDATE summaries SET url = ?, content = ?, status = ?, updated_at = ? WHERE id = ? AND ifnull(journal_date,'') = ifnull(?, '') RETURNING id",
  )
    .bind(url, raw, status, now, input.id, jd)
    .first();
  if (updated) return { ok: true, id: input.id, status, action: "updated" };

  await env.DB.prepare(
    "INSERT INTO summaries (id, journal_date, url, content, status, pushed_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
  )
    .bind(input.id, jd, url, raw, status, now, now)
    .run();
  return { ok: true, id: input.id, status, action: "inserted" };
}

/** Title for list views: JSON title, or the first line of a blocked stub. */
export function displayTitle(raw: string): string {
  if (isBlockedStub(raw)) return raw.trim().split("\n")[0].slice(0, 120);
  try {
    return JSON.parse(raw)?.content?.title ?? "(untitled)";
  } catch {
    return "(unparseable)";
  }
}
