// Events audit trail (#172): one INSERT helper shared by the Pages Functions
// and the pipeline DO (which imports across the boundary, like summaries.ts).
// Fire-and-forget: the audit trail must never break the operation it records,
// so logEvent swallows every error. Reads live in /api/events.

export interface EventInput {
  actor: "editor" | "pipeline" | "system";
  // link.submitted | link.dismissed | link.reopened
  // summary.created | summary.updated | summary.dismissed | summary.restored
  // pipeline.run_started | pipeline.fetched | pipeline.extracted |
  //   pipeline.model_requested | pipeline.model_responded | pipeline.blocked
  //   (step events + the closing event share a `run` marker in detail — #178)
  // cycle.rolled
  event: string;
  linkId?: number | null;
  summaryId?: string | null;
  detail?: Record<string, unknown> | null;
}

export async function logEvent(db: D1Database, e: EventInput): Promise<void> {
  try {
    await db
      .prepare("INSERT INTO events (actor, event, link_id, summary_id, detail) VALUES (?, ?, ?, ?, ?)")
      .bind(e.actor, e.event, e.linkId ?? null, e.summaryId ?? null, e.detail ? JSON.stringify(e.detail) : null)
      .run();
  } catch (err) {
    console.log(JSON.stringify({ evt: "logEvent.failed", event: e.event, error: String(err).slice(0, 200) }));
  }
}
