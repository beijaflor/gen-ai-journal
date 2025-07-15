# Step 8: Cleanup and Archive

This step cleans up the workspace and archives temporary files after successful journal creation.

## Objective

- Remove temporary working files
- Archive important artifacts
- Prepare workspace for next week's journal
- Verify all final outputs are in correct locations

## Pre-Cleanup Verification

Before cleaning up, confirm final outputs are complete:

- [ ] `journals/YYYY-MM-DD/weekly_journal_YYYY_MM_DD.md` exists and is complete
- [ ] `journals/YYYY-MM-DD/annex_journal_YYYY_MM_DD.md` exists and is complete
- [ ] All source files are properly saved in `journals/YYYY-MM-DD/sources/`
- [ ] All summaries are saved in `journals/YYYY-MM-DD/summaries/`

## Cleanup Tasks

### 1. Clean Workdesk Directory

Remove temporary files:

- [ ] Remove or archive `workdesk/sources.md` (content now in journal directory)
- [ ] Remove `workdesk/summaries/*.md` (content now in journal directory)
- [ ] Remove `workdesk/unified_summaries.md` (content now in journal directory)
- [ ] Remove `workdesk/generated_prompt.txt` (temporary file)
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