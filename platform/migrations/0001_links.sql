-- Link inbox (#159): manually submitted candidate URLs
CREATE TABLE links (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  url           TEXT NOT NULL UNIQUE,   -- sanitized: tracking params/fragments stripped
  note          TEXT,
  status        TEXT NOT NULL DEFAULT 'new'
                CHECK (status IN ('new', 'consumed', 'dismissed')),
  submitted_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  consumed_at   TEXT
);

CREATE INDEX idx_links_status ON links (status, submitted_at DESC);
