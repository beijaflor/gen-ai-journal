# Step 4: Curate Main Journal

This step selects the most important and valuable articles for the main journal based on established criteria.

## Objective

Select articles that provide essential insights, significant developments, and high-value content for the primary audience.

## Input Files

- **Source List:** `journals/YYYY-MM-DD/sources/sources.md` (all URLs)
- **Summaries:** `journals/YYYY-MM-DD/unified_summaries.md` (for review)
- **Criteria:** `criteria/curation_criteria.md`

## Curation Process

### 1. Review Each Article

For each URL in the source list, review its summary and evaluate against the main journal criteria:

- **Thematic Core:** Does it align with this week's main themes?
- **Signal Strength:** Is it a primary source or deep analysis?
- **Uniqueness:** Does it provide unique insights not found elsewhere?
- **Technical Depth:** Does it discuss trade-offs and architectural perspectives?
- **Lasting Value:** Will it remain relevant beyond this week?

### 2. Make Selection Decisions

- **✅ Accept:** Article meets the criteria for main journal
  - Add URL to `journals/YYYY-MM-DD/sources/curated_journal_sources.md`
  
- **❌ Reject:** Article doesn't meet main journal standards
  - Add URL to `journals/YYYY-MM-DD/sources/omitted_sources.md`

### 3. Avoid Common Pitfalls

Do NOT include:
- Surface-level tutorials or "getting started" guides
- Pure marketing content or hype pieces
- Duplicate coverage of the same topic
- Personal diary-style blog posts without broader insights

## Output Files

Create or update:

- [ ] `journals/YYYY-MM-DD/sources/curated_journal_sources.md`
  ```markdown
  # Curated Main Journal Sources
  
  - [ ] https://example.com/important-article-1
  - [ ] https://example.com/significant-development-2
  ```

- [ ] `journals/YYYY-MM-DD/sources/omitted_sources.md`
  ```markdown
  # Omitted Sources
  
  - [ ] https://example.com/basic-tutorial
  - [ ] https://example.com/marketing-piece
  ```

## Verification

- [ ] Confirm main journal sources represent the week's most important content
- [ ] Verify no duplicate topics in curated list
- [ ] Ensure omitted sources are saved for annex consideration

## Next Step

[STEP_05_CURATE_ANNEX.md](STEP_05_CURATE_ANNEX.md) - Review omitted sources for annex journal