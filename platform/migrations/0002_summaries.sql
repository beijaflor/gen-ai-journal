-- Summary collection (#160): summary JSONs pushed from the local pipeline
CREATE TABLE summaries (
  id            TEXT NOT NULL,          -- "136" — matches sources.md numbering
  journal_date  TEXT,                   -- NULL while in workdesk, set on publish
  url           TEXT NOT NULL,
  content       TEXT NOT NULL,          -- full summary-v1 JSON (source of truth)
  status        TEXT NOT NULL DEFAULT 'workdesk'
                CHECK (status IN ('workdesk', 'published', 'blocked')),
  pushed_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  updated_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  PRIMARY KEY (id, journal_date)
);

CREATE INDEX idx_summaries_status ON summaries (status, pushed_at DESC);
CREATE INDEX idx_summaries_url ON summaries (url);
