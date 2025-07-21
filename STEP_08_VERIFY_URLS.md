# Step 8: Verify URLs

This step performs quality control checks on the assembled journal documents by verifying that all URLs used are properly sourced from the curated sources lists.

## Objective

Ensure editorial integrity by verifying that:
- All main journal URLs come from `workdesk/sources.md`
- All annex journal URLs come from `workdesk/curated_annex_journal_sources.md`
- No unauthorized or unvetted sources are included

## Input Files

- **Main Journal:** `workdesk/weekly_journal_YYYY_MM_DD.md`
- **Annex Journal:** `workdesk/annex_journal_YYYY_MM_DD.md`
- **Main Sources:** `workdesk/sources.md`
- **Annex Sources:** `workdesk/curated_annex_journal_sources.md`

## Process

### 8A. Verify Main Journal URLs

Execute [STEP_08A_VERIFY_MAIN_URLS.md](STEP_08A_VERIFY_MAIN_URLS.md):

- [ ] Extract all URLs from the main journal
- [ ] Cross-reference against `workdesk/sources.md`
- [ ] Generate verification report
- [ ] Create clean curated sources list

### 8B. Verify Annex Journal URLs

Execute [STEP_08B_VERIFY_ANNEX_URLS.md](STEP_08B_VERIFY_ANNEX_URLS.md):

- [ ] Extract all URLs from the annex journal
- [ ] Cross-reference against `workdesk/curated_annex_journal_sources.md`
- [ ] Generate verification report
- [ ] Confirm editorial integrity

## Quality Standards

- **100% Match Required:** All journal URLs must be found in their respective source lists
- **Traceability:** Each URL can be tracked back to its original curation decision
- **No Unauthorized Sources:** No URLs should appear that weren't properly vetted

## Output

- **Verification Reports:** Success/failure status for both journals
- **Updated Source Lists:** Clean lists of actually used URLs
- **Quality Assurance:** Confirmation that editorial standards are maintained

## Benefits

1. **Editorial Integrity:** Ensures all content follows proper curation process
2. **Quality Control:** Catches any inadvertent inclusion of unvetted sources
3. **Audit Trail:** Provides complete traceability of source selection
4. **Publication Ready:** Confirms journals meet quality standards

## Next Step

[STEP_09_CLEANUP.md](STEP_09_CLEANUP.md) - Archive files and clean workspace