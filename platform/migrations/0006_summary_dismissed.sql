-- Dismiss becomes a reversible flag on the summary (no deletion). SQLite
-- can't alter CHECKs → rebuild.
CREATE TABLE summaries_new (
  id            TEXT NOT NULL,
  journal_date  TEXT,
  url           TEXT NOT NULL,
  content       TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'workdesk'
                CHECK (status IN ('workdesk', 'published', 'blocked', 'dismissed')),
  pushed_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  updated_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  PRIMARY KEY (id, journal_date)
);
INSERT INTO summaries_new SELECT * FROM summaries;
DROP TABLE summaries;
ALTER TABLE summaries_new RENAME TO summaries;
CREATE INDEX idx_summaries_status ON summaries (status, pushed_at DESC);
CREATE INDEX idx_summaries_url ON summaries (url);
CREATE UNIQUE INDEX idx_summaries_id_cycle ON summaries (id, ifnull(journal_date, ''));
