# Step 10: Archive & Cleanup

This final step archives the completed journals and source materials to the permanent directory structure and cleans the workspace.

## Objective

Move completed journals and supporting materials to the permanent archive structure and prepare the workspace for the next weekly cycle.

## Input Files

- **Completed Journals:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`
- **Source Materials:**
  - `workdesk/curated_journal_sources.md`
  - `workdesk/curated_annex_journal_sources.md`
  - `workdesk/omitted_urls.md`
- **Summary Files:**
  - `workdesk/summaries/` directory
  - `workdesk/omitted_summaries_unified.md`

## Archive Process

### 1. Create Archive Directory

```bash
# Create the dated journal directory
mkdir -p journals/YYYY-MM-DD/{sources,summaries}
```

### 2. Archive Journals

Move completed journal files:

```bash
# Archive main and annex journals with proper naming
mv workdesk/weekly_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/00_weekly_journal_YYYY_MM_DD.md
mv workdesk/annex_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/01_annex_journal_YYYY_MM_DD.md
```

### 3. Archive Source Materials

Move curation and source files:

```bash
# Archive source lists
mv workdesk/curated_journal_sources.md journals/YYYY-MM-DD/sources/
mv workdesk/curated_annex_journal_sources.md journals/YYYY-MM-DD/sources/
mv workdesk/omitted_urls.md journals/YYYY-MM-DD/sources/omitted_sources.md

# Archive original sources if available
if [ -f workdesk/sources.md ]; then
    cp workdesk/sources.md journals/YYYY-MM-DD/sources/original_sources.md
fi
```

### 4. Archive Summaries

Move summary files and create archive summaries:

```bash
# Archive all individual summaries
mv workdesk/summaries/* journals/YYYY-MM-DD/summaries/

# Archive unified summaries (complete reference)
if [ -f workdesk/unified_summaries.md ]; then
    mv workdesk/unified_summaries.md journals/YYYY-MM-DD/99_unified_summaries.md
fi

if [ -f workdesk/omitted_summaries_unified.md ]; then
    mv workdesk/omitted_summaries_unified.md journals/YYYY-MM-DD/02_omitted_summaries.md
fi
```

### 5. Clean Workspace

Remove temporary and working files:

```bash
# Clean workdesk of completed work
rm -f workdesk/unified_summaries.md
rm -f workdesk/unified_summaries_main.md
rm -f workdesk/unified_summaries_annex.md
rm -f workdesk/reviewed_*.md
rm -f workdesk/*.md

# Remove empty summaries directory
rmdir workdesk/summaries 2>/dev/null || true

# Keep workdesk directory for next cycle
```

## Final Archive Structure

The completed archive should look like:

```
journals/YYYY-MM-DD/
├── 00_weekly_journal_YYYY_MM_DD.md   # Main journal (publication-ready)
├── 01_annex_journal_YYYY_MM_DD.md    # Annex journal (publication-ready)
├── 02_omitted_summaries.md           # Summaries of omitted articles
├── 99_unified_summaries.md           # All unified summaries (complete reference)
├── sources/
│   ├── original_sources.md           # Original source list with all URLs
│   ├── curated_journal_sources.md    # Main journal selected URLs
│   ├── curated_annex_journal_sources.md  # Annex journal selected URLs
│   └── omitted_sources.md            # URLs not included in either journal
└── summaries/
    └── [individual summary files]     # All individual AI-generated summaries
```

## Quality Verification

- [ ] **Archive Complete:** All expected files moved to journals/YYYY-MM-DD/
- [ ] **File Naming:** Consistent naming convention followed
- [ ] **Structure:** Proper directory organization
- [ ] **Clean Workspace:** workdesk cleaned but preserved for next cycle
- [ ] **Access:** Archived files readable and properly formatted

## Git Commit

Consider committing the archived journal to version control:

```bash
# Add archived journal
git add journals/YYYY-MM-DD/

# Commit with descriptive message
git commit -m "Add weekly journal for YYYY-MM-DD

- Main journal: [brief description of main themes]
- Annex journal: [brief description of annex themes]
- Total sources processed: [number]
- Main articles: [number]
- Annex articles: [number]"
```

## Workspace Ready

After cleanup, the workspace is ready for the next weekly cycle:
- `workdesk/` directory empty and ready
- Archive safely stored in `journals/YYYY-MM-DD/`
- Git repository updated with new journal
- Ready to start Step 1 for next week

## Next Cycle

Begin the next weekly journal cycle with [STEP_01_GATHER_SOURCES.md](STEP_01_GATHER_SOURCES.md).