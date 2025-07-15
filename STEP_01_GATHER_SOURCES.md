# Step 1: Gather Sources

This step creates the initial list of source URLs for the week in the `workdesk` directory.

## Tasks

### 1. Gather Sources from GitHub Issue

- [ ] Identify the GitHub issue containing the list of source URLs for the weekly journal
- [ ] Use the `get_issue` tool to retrieve its content (if using automated tools)
- [ ] Copy all links into `workdesk/sources.md` in checklist format:
  ```markdown
  - [ ] https://example.com/article1
  - [ ] https://example.com/article2
  ```

### 2. Process and Sanitize Sources

- [ ] Run the source processing script:
  ```bash
  python3 process_sources.py workdesk/sources.md
  ```
  
  This script performs:
  - Removes UTM parameters from URLs
  - Removes duplicate links
  - Maintains checklist format

### 3. Verify Results

- [ ] Confirm that `workdesk/sources.md` contains:
  - Sanitized URLs (no tracking parameters)
  - No duplicate entries
  - Proper checklist format for tracking progress

## Output

- **File Created/Updated:** `workdesk/sources.md`
- **Format:** Markdown checklist of unique, sanitized URLs
- **Next Step:** [STEP_02_SUMMARIZE.md](STEP_02_SUMMARIZE.md)