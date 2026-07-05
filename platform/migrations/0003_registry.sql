-- Cycle/ID registry (#160): the cloud becomes the NNN authority.
CREATE TABLE settings (
  key    TEXT PRIMARY KEY,
  value  TEXT NOT NULL
);

-- SQLite treats NULLs as distinct in the (id, journal_date) primary key, so
-- workdesk rows (journal_date IS NULL) need this guard for upsert semantics.
CREATE UNIQUE INDEX idx_summaries_id_cycle ON summaries (id, ifnull(journal_date, ''));
