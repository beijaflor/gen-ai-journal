# Step 9: Verify URLs & Quality

This step performs comprehensive quality control, URL verification, and final checks before archiving the completed journals.

## Objective

Ensure all URLs work correctly, verify content accuracy, and perform final quality checks on the assembled journals.

## Input Files

- **Main Journal:** `workdesk/weekly_journal_YYYY_MM_DD.md`
- **Annex Journal:** `workdesk/annex_journal_YYYY_MM_DD.md`
- **Main Sources:** `workdesk/curated_journal_sources.md`
- **Annex Sources:** `workdesk/curated_annex_journal_sources.md`
- **Omitted Summaries:** `workdesk/omitted_summaries_unified.md`

## Verification Process

### 1. URL Verification

#### Main Journal URLs
- [ ] Extract all URLs from `workdesk/weekly_journal_YYYY_MM_DD.md`
- [ ] Cross-reference against `workdesk/curated_journal_sources.md`
- [ ] Test each URL for accessibility (200 status)
- [ ] Verify no broken or redirect links
- [ ] Ensure all referenced articles are included

#### Annex Journal URLs
- [ ] Extract all URLs from `workdesk/annex_journal_YYYY_MM_DD.md`
- [ ] Cross-reference against `workdesk/curated_annex_journal_sources.md`
- [ ] Test each URL for accessibility
- [ ] Verify no broken or redirect links
- [ ] Ensure all referenced articles are included

### 2. Content Quality Checks

#### Editorial Standards
- [ ] **Voice Consistency:** Verify editorial persona throughout both journals
- [ ] **Language Quality:** Ensure proper Japanese throughout
- [ ] **Technical Accuracy:** Check for accurate technical references
- [ ] **Flow & Structure:** Confirm logical progression and smooth transitions

#### Completeness Checks
- [ ] **Main Journal:** Verify 18-25 articles included
- [ ] **Annex Journal:** Confirm B-side character maintained
- [ ] **All Summaries:** Check that every curated URL has corresponding content
- [ ] **No Duplicates:** Ensure no overlap between main and annex journals

### 3. Format Verification

- [ ] **Markdown Syntax:** Valid markdown formatting
- [ ] **Heading Hierarchy:** Consistent heading levels (# ## ###)
- [ ] **Link Formatting:** Proper link syntax and working URLs
- [ ] **Japanese Text:** Correct character encoding and display

### 4. Archive Preparation

- [ ] **File Naming:** Confirm correct YYYY_MM_DD format
- [ ] **Directory Structure:** Verify workdesk organization
- [ ] **Supporting Files:** Ensure all curation files present
- [ ] **Omitted Summaries:** Confirm omitted_summaries_unified.md is complete

## Verification Commands

```bash
# Extract and test URLs from main journal
grep -o 'https://[^)]*' workdesk/weekly_journal_YYYY_MM_DD.md | sort -u > temp_main_urls.txt

# Extract and test URLs from annex journal  
grep -o 'https://[^)]*' workdesk/annex_journal_YYYY_MM_DD.md | sort -u > temp_annex_urls.txt

# Compare against curated sources
diff temp_main_urls.txt workdesk/curated_journal_sources.md
diff temp_annex_urls.txt workdesk/curated_annex_journal_sources.md

# Clean up temporary files
rm temp_main_urls.txt temp_annex_urls.txt
```

## Quality Checklist

Final verification ensures:

- [ ] All URLs in journals work and match curated source lists
- [ ] No broken links or inaccessible content
- [ ] Editorial voice consistent throughout
- [ ] Japanese language correct and natural
- [ ] Technical content accurate and insightful
- [ ] Proper markdown formatting
- [ ] Complete coverage of curated articles
- [ ] No duplicate content between journals
- [ ] Ready for archiving and publication

## Error Resolution

If issues are found:
- **Broken URLs:** Return to Step 4/5 to replace with working alternatives
- **Content Issues:** Return to Step 7 for editorial revision
- **Format Problems:** Fix formatting in Step 8
- **Missing Articles:** Verify curation lists and regenerate summaries if needed

## Output

- **Verified Journals:** Ready for archiving
- **Quality Report:** Issues identified and resolved
- **URL Status:** All links confirmed working

## Next Step

[STEP_10_CLEANUP.md](STEP_10_CLEANUP.md) - Archive completed journals and clean workspace