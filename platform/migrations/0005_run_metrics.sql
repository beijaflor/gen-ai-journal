-- Per-link summarization run metrics (logging layer for the console/#161
-- and durable cost accounting). Overwritten on retry — latest run wins.
ALTER TABLE links ADD COLUMN processed_at TEXT;
ALTER TABLE links ADD COLUMN fetch_ms INTEGER;
ALTER TABLE links ADD COLUMN ai_ms INTEGER;
ALTER TABLE links ADD COLUMN tokens_in INTEGER;
ALTER TABLE links ADD COLUMN tokens_out INTEGER;
