-- 'consumed' was the legacy pull_inbox status; the cloud pipeline made it
-- meaningless. Rebuild links without it (and without consumed_at).
CREATE TABLE links_new (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  url           TEXT NOT NULL UNIQUE,
  note          TEXT,
  status        TEXT NOT NULL DEFAULT 'new'
                CHECK (status IN ('new', 'queued', 'summarized', 'blocked', 'dismissed')),
  error         TEXT,
  summary_id    TEXT,
  submitted_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  processed_at  TEXT,
  fetch_ms      INTEGER,
  ai_ms         INTEGER,
  tokens_in     INTEGER,
  tokens_out    INTEGER
);
INSERT INTO links_new (id, url, note, status, error, summary_id, submitted_at, processed_at, fetch_ms, ai_ms, tokens_in, tokens_out)
  SELECT id, url, note, CASE WHEN status='consumed' THEN 'dismissed' ELSE status END,
         error, summary_id, submitted_at, processed_at, fetch_ms, ai_ms, tokens_in, tokens_out FROM links;
DROP TABLE links;
ALTER TABLE links_new RENAME TO links;
CREATE INDEX idx_links_status ON links (status, submitted_at DESC);
