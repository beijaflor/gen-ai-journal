# Step 5B: Create Focused Summary Collections

This step creates separate unified summary files for the main journal and annex journal based on the curated selections from previous steps.

## Objective

Generate focused summary collections that contain only the summaries for articles selected for each journal, making it easier to work with during review and assembly phases.

## Input Files

- **Main Journal Sources:** `workdesk/curated_journal_sources.md`
- **Annex Journal Sources:** `workdesk/curated_annex_journal_sources.md`
- **All Individual Summaries:** `workdesk/summaries/*.md`

## Process

### 1. Extract Selected Article Numbers

- [ ] Parse `workdesk/curated_journal_sources.md` to extract article numbers for main journal
- [ ] Parse `workdesk/curated_annex_journal_sources.md` to extract article numbers for annex journal

### 2. Create Main Journal Unified Summary

- [ ] Aggregate only the summaries that correspond to URLs in `curated_journal_sources.md`
- [ ] Output to `workdesk/unified_summaries_main.md`

Example command pattern:
```bash
# Extract article numbers from curated sources and aggregate corresponding summaries
# This is a conceptual example - actual implementation may vary
```

### 3. Create Annex Journal Unified Summary

- [ ] Aggregate only the summaries that correspond to URLs in `curated_annex_journal_sources.md`
- [ ] Output to `workdesk/unified_summaries_annex.md`

### 4. Verify Output

- [ ] Confirm `workdesk/unified_summaries_main.md` contains only main journal summaries
- [ ] Confirm `workdesk/unified_summaries_annex.md` contains only annex journal summaries
- [ ] Verify no summaries are missing from either collection

## Output Files

- **Main Journal Collection:** `workdesk/unified_summaries_main.md`
  - Contains only summaries for articles selected for the main journal
  - Maintains the same format as the original summaries
  - Separates each summary with `---` divider

- **Annex Journal Collection:** `workdesk/unified_summaries_annex.md`
  - Contains only summaries for articles selected for the annex journal
  - Maintains the same format as the original summaries
  - Separates each summary with `---` divider

## Benefits

- **Focused Review:** Reviewers only see summaries relevant to each journal
- **Efficient Assembly:** Assembly process can work with pre-filtered content
- **Clear Separation:** Main and annex content are clearly separated
- **Easier Navigation:** Smaller files focused on specific journal content

## Next Step

[STEP_06_REVIEW.md](STEP_06_REVIEW.md) - Review and refine the selected summaries