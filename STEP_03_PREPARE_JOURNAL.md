# Step 3: Prepare Journal Directory

This step sets up the directory structure for the journal. No editorial decisions are made here - this is purely mechanical setup.

## Tasks

### 1. Create Journal Directory

- [ ] Create a new directory under `journals/` with format `YYYY-MM-DD`:
  ```bash
  mkdir -p journals/YYYY-MM-DD
  mkdir -p journals/YYYY-MM-DD/sources
  mkdir -p journals/YYYY-MM-DD/summaries
  ```
  
  Replace `YYYY-MM-DD` with the actual date (e.g., `2025-07-09`)

### 2. Create Empty Journal Files

- [ ] Create the main journal file:
  ```bash
  touch journals/YYYY-MM-DD/weekly_journal_YYYY_MM_DD.md
  ```

- [ ] Create the annex journal file:
  ```bash
  touch journals/YYYY-MM-DD/annex_journal_YYYY_MM_DD.md
  ```

### 3. Move Sources and Summaries

- [ ] Move the source list from workdesk to the journal directory:
  ```bash
  cp workdesk/sources.md journals/YYYY-MM-DD/sources/sources.md
  ```

- [ ] Move all summaries to the journal directory:
  ```bash
  cp workdesk/summaries/*.md journals/YYYY-MM-DD/summaries/
  cp workdesk/unified_summaries.md journals/YYYY-MM-DD/
  ```

## Verification

- [ ] Confirm directory structure:
  ```
  journals/YYYY-MM-DD/
  ├── weekly_journal_YYYY_MM_DD.md (empty)
  ├── annex_journal_YYYY_MM_DD.md (empty)
  ├── sources/
  │   └── sources.md
  ├── summaries/
  │   └── [individual summary files]
  └── unified_summaries.md
  ```

## Output

- **Directory Created:** `journals/YYYY-MM-DD/` with subdirectories
- **Files Created:** Empty journal markdown files
- **Files Moved:** Sources and summaries from workdesk to journal directory
- **Next Step:** [STEP_04_CURATE_MAIN.md](STEP_04_CURATE_MAIN.md)