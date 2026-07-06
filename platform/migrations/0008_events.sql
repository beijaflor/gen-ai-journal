-- Events audit trail (#172): every summarization-lifecycle interaction —
-- human or pipeline — recorded durably. Scope (per issue declaration):
-- link lifecycle, pipeline runs, summary flag flips, cycle rollovers.
-- Future journal events (rebuilds/publishes) arrive with #163.
-- Append-only: link rows may be deleted, their events stay.
CREATE TABLE events (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  ts          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  actor       TEXT NOT NULL,   -- 'editor' | 'pipeline' | 'system'
  event       TEXT NOT NULL,   -- e.g. link.submitted, summary.created, pipeline.blocked
  link_id     INTEGER,         -- subject link id, when applicable
  summary_id  TEXT,            -- subject NNN, when applicable
  detail      TEXT             -- JSON: reason, model, fetch_ms, ai_ms, tokens, …
);
CREATE INDEX idx_events_ts ON events (ts DESC);
CREATE INDEX idx_events_summary ON events (summary_id);
