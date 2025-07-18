# Step 8: Cleanup and Archive

This step cleans up the workspace and archives temporary files after successful journal creation.

## Objective

- Remove temporary working files
- Archive important artifacts
- Prepare workspace for next week's journal
- Verify all final outputs are in correct locations

## Pre-Cleanup Verification

Before cleaning up, confirm final outputs are complete in workdesk:

- [ ] `workdesk/weekly_journal_YYYY_MM_DD.md` exists and is complete
- [ ] `workdesk/annex_journal_YYYY_MM_DD.md` exists and is complete
- [ ] All working files are properly saved in workdesk

## Archive to Journal Directory

### 1. Create Final Journal Directory

- [ ] Create the final archive directory:
  ```bash
  mkdir -p journals/YYYY-MM-DD
  mkdir -p journals/YYYY-MM-DD/sources
  mkdir -p journals/YYYY-MM-DD/summaries
  ```

### 2. Move Completed Files to Archive

- [ ] Move completed journal files:
  ```bash
  cp workdesk/weekly_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/
  cp workdesk/annex_journal_YYYY_MM_DD.md journals/YYYY-MM-DD/
  ```

- [ ] Move working files to archive:
  ```bash
  cp workdesk/sources.md journals/YYYY-MM-DD/sources/
  cp workdesk/curated_journal_sources.md journals/YYYY-MM-DD/sources/
  cp workdesk/curated_annex_journal_sources.md journals/YYYY-MM-DD/sources/
  cp workdesk/omitted_sources.md journals/YYYY-MM-DD/sources/
  cp workdesk/summaries/*.md journals/YYYY-MM-DD/summaries/
  cp workdesk/unified_summaries.md journals/YYYY-MM-DD/
  ```

## Cleanup Tasks

### 3. Clean Workdesk Directory

Remove temporary files:

- [ ] Remove `workdesk/sources.md` (now archived in journal directory)
- [ ] Remove `workdesk/summaries/*.md` (now archived in journal directory)
- [ ] Remove `workdesk/unified_summaries.md` (now archived in journal directory)
- [ ] Remove `workdesk/curated_journal_sources.md` (now archived)
- [ ] Remove `workdesk/curated_annex_journal_sources.md` (now archived)
- [ ] Remove `workdesk/omitted_sources.md` (now archived)
- [ ] Remove `workdesk/weekly_journal_YYYY_MM_DD.md` (now archived)
- [ ] Remove `workdesk/annex_journal_YYYY_MM_DD.md` (now archived)
- [ ] Remove `workdesk/generated_prompt*.txt` (temporary files)
- [ ] Remove any other temporary files created during process

### 2. Optional Archive

If you want to keep workdesk files for reference:

```bash
mkdir -p archives/YYYY-MM-DD-workdesk
mv workdesk/* archives/YYYY-MM-DD-workdesk/
# or
tar -czf archives/workdesk-YYYY-MM-DD.tar.gz workdesk/
rm -rf workdesk/*
```

### 3. Prepare for Next Week

- [ ] Ensure `workdesk/` directory is empty and ready
- [ ] Verify journal directory structure is complete:
  ```
  journals/YYYY-MM-DD/
  ├── weekly_journal_YYYY_MM_DD.md    ✓
  ├── annex_journal_YYYY_MM_DD.md     ✓
  ├── sources/
  │   ├── sources.md                   ✓
  │   ├── curated_journal_sources.md   ✓
  │   ├── curated_annex_journal_sources.md ✓
  │   └── omitted_sources.md           ✓
  └── summaries/
      ├── [individual summaries]       ✓
      └── unified_summaries.md         ✓
  ```

## Final Verification

- [ ] All journal content is properly saved
- [ ] Workdesk is clean for next iteration
- [ ] No important files were accidentally deleted
- [ ] Git repository is ready for commit (if using version control)

## Optional: Git Commit

If using git for version control:

```bash
git add journals/YYYY-MM-DD/
git commit -m "Complete journal for YYYY-MM-DD

- Main journal: [brief description]
- Annex journal: [brief description]
- [X] articles processed"
```

## Completion

✅ **Workflow Complete!**

The weekly journal creation process is now finished. All artifacts are properly organized and the workspace is ready for the next iteration.

## Next Week

When ready for the next journal, start over with [STEP_01_GATHER_SOURCES.md](STEP_01_GATHER_SOURCES.md).