-- Pipeline states for links (#166). SQLite cannot alter CHECK constraints,
-- so rebuild the table. consumed/dismissed kept for the parallel-run tools.
CREATE TABLE links_new (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  url           TEXT NOT NULL UNIQUE,
  note          TEXT,
  status        TEXT NOT NULL DEFAULT 'new'
                CHECK (status IN ('new', 'queued', 'summarized', 'blocked', 'consumed', 'dismissed')),
  error         TEXT,           -- failure reason when blocked
  summary_id    TEXT,           -- NNN assigned on successful summarization
  submitted_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  consumed_at   TEXT
);

INSERT INTO links_new (id, url, note, status, submitted_at, consumed_at)
  SELECT id, url, note, status, submitted_at, consumed_at FROM links;

DROP TABLE links;
ALTER TABLE links_new RENAME TO links;
CREATE INDEX idx_links_status ON links (status, submitted_at DESC);
