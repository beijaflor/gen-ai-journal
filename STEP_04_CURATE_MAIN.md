# Step 4: Curate Main Journal

This step selects the most important and valuable articles for the main journal based on established criteria.

## Objective

Select articles that provide essential insights, significant developments, and high-value content for the primary audience.

## Input Files

- **Source List:** `workdesk/sources.md` (all URLs with checkboxes)
- **Summaries:** `workdesk/unified_summaries.md` (for review)
- **Criteria:** `criteria/curation_criteria.md`

## Curation Process

**IMPORTANT** Read entire sources and pick from them and **NEVER** make up falsy URL.

### 0. Prepare

- [ ] Read and adopt the editorial persona from `EDITOR_PERSONALITY.md`
  - Adopt the role of a **technical web application engineer** with startup mindset
  - Focus on "why it matters" beyond just "what happened"
  - Apply editorial judgment that is **visionary but grounded**

### 1. Review Each Article

For each URL in the source list, review its summary and evaluate against the main journal criteria:

- **Thematic Core:** Does it align with this week's main themes?
- **Signal Strength:** Is it a primary source or deep analysis?
- **Uniqueness:** Does it provide unique insights not found elsewhere?
- **Technical Depth:** Does it discuss trade-offs and architectural perspectives?
- **Lasting Value:** Will it remain relevant beyond this week?

### 2. Make Selection Decisions

- **✅ Accept:** Article meets the criteria for main journal
  - Add URL to `workdesk/curated_journal_sources.md`
- Selection should be counted from 18 to 25.

### 3. Avoid Common Pitfalls

Do NOT include:

- Surface-level tutorials or "getting started" guides
- Pure marketing content or hype pieces
- Duplicate coverage of the same topic
- Personal diary-style blog posts without broader insights

## Output Files

Create or update:

- [ ] `workdesk/curated_journal_sources.md`

  ```markdown
  # Curated Main Journal Sources

  - [ ] https://example.com/important-article-1
  - [ ] https://example.com/significant-development-2
  ```

## Verification

- [ ] Confirm main journal sources represent the week's most important content
- [ ] Verify no duplicate topics in curated list

## Next Step

[STEP_05_CURATE_ANNEX.md](STEP_05_CURATE_ANNEX.md) - Review non-main sources for annex journal
