# Step 6: Create Focused Summaries

This step generates unified summary documents for each journal (main and annex) from the curated source lists.

## Objective

Create focused, unified summary documents that contain only the summaries for articles selected for each journal.

## Input Files

- **Main Journal Sources:** `workdesk/curated_journal_sources.md`
- **Annex Journal Sources:** `workdesk/curated_annex_journal_sources.md`
- **All Summaries Directory:** `workdesk/summaries/`
- **Original Unified Summaries:** `workdesk/unified_summaries.md` (reference)

## Process

### 1. Create Main Journal Focused Summaries

Generate a unified summary file containing only the main journal articles:

```bash
python3 scripts/unite_summaries.py workdesk/curated_journal_sources.md workdesk/summaries workdesk/unified_summaries_main.md
```

### 2. Create Annex Journal Focused Summaries

Generate a unified summary file containing only the annex journal articles:

```bash
python3 scripts/unite_summaries.py workdesk/curated_annex_journal_sources.md workdesk/summaries workdesk/unified_summaries_annex.md
```

### 3. Create Omitted Sources List

Generate a list of URLs that were not selected for either journal:

- [ ] Compare original `workdesk/sources.md` with curated lists
- [ ] Create `workdesk/omitted_urls.md` with unselected URLs
- [ ] Generate omitted summaries:
  ```bash
  python3 scripts/unite_summaries.py workdesk/omitted_urls.md workdesk/summaries workdesk/omitted_summaries_unified.md
  ```

## Quality Checks

- [ ] Verify `unified_summaries_main.md` contains only main journal article summaries
- [ ] Verify `unified_summaries_annex.md` contains only annex journal article summaries
- [ ] Confirm no overlap between main and annex summaries
- [ ] Check that all curated sources have corresponding summaries
- [ ] Ensure omitted summaries capture all non-selected articles

## Output Files

- **Main Focus:** `workdesk/unified_summaries_main.md`
- **Annex Focus:** `workdesk/unified_summaries_annex.md`
- **Omitted URLs:** `workdesk/omitted_urls.md`
- **Omitted Summaries:** `workdesk/omitted_summaries_unified.md`

## Next Step

[STEP_07_REVIEW.md](STEP_07_REVIEW.md) - Review and refine the focused summaries