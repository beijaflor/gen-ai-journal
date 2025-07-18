# Step 3: Prepare Working Journal Files

This step prepares the working journal files in the workdesk directory for editing. No editorial decisions are made here - this is purely mechanical setup. All files remain in workdesk during the editing process.

## Tasks

### 1. Create Working Journal Files

- [ ] Create the main journal file in workdesk:
  ```bash
  touch workdesk/weekly_journal_YYYY_MM_DD.md
  ```

- [ ] Create the annex journal file in workdesk:
  ```bash
  touch workdesk/annex_journal_YYYY_MM_DD.md
  ```
  
  Replace `YYYY-MM-DD` with the actual date (e.g., `2025-07-16`)

### 2. Verify Working Files

- [ ] Confirm all required files exist in workdesk:
  - `workdesk/sources.md` (with completed checkboxes)
  - `workdesk/summaries/` directory with individual summary files
  - `workdesk/unified_summaries.md` (aggregated summaries)
  - `workdesk/weekly_journal_YYYY_MM_DD.md` (empty, ready for editing)
  - `workdesk/annex_journal_YYYY_MM_DD.md` (empty, ready for editing)

## Output

- **Files Created:** Empty journal files in workdesk for editing
- **Working Directory:** All files remain in workdesk for active editing workflow
- **Next Step:** [STEP_04_CURATE_MAIN.md](STEP_04_CURATE_MAIN.md)

## Note

Files will only be moved to the final `journals/YYYY-MM-DD/` directory structure in STEP_08 after all editing is complete. This keeps the active editing workflow contained in workdesk.