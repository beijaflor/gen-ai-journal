# Step 1: Gather Sources

This step creates the initial list of source URLs for the week in the `workdesk` directory.

## Tasks

### 1. Gather Sources from GitHub Issue

- [ ] Identify the GitHub issue containing the list of source URLs for the weekly journal
- [ ] Use the `get_issue` tool to retrieve its content (if using automated tools)
- [ ] Copy all links into `workdesk/sources.md` in structured format with numbered IDs:
  ```markdown
  ## Main List
  - [ ] 001. https://example.com/article1
  - [ ] 002. https://example.com/article2
  
  ## Slides
  - [ ] 003. https://example.com/slide1
  
  ## Might Be Hype
  - [ ] 004. https://example.com/hype1
  
  ## Better to be Omitted
  - [ ] 005. https://example.com/omitted1
  ```

**Important Notes:**
- Preserve the section structure from the GitHub issue
- Assign sequential numbered IDs (001, 002, etc.) to each link for easy tracking
- Include all sections even if some are empty
- Maintain checkbox format for progress tracking

### 2. Process and Sanitize Sources

- [ ] Run the source processing script:
  ```bash
  python3 process_sources.py workdesk/sources.md
  ```
  
  This script performs:
  - Removes UTM parameters from URLs
  - Removes duplicate links within and across sections
  - Maintains structured format with section headers
  - Preserves numbered IDs and checklist format

### 3. Verify Results

- [ ] Confirm that `workdesk/sources.md` contains:
  - Sanitized URLs (no tracking parameters)
  - No duplicate entries within or across sections
  - Proper structured format with section headers
  - Sequential numbered IDs for all links (001, 002, etc.)
  - Proper checklist format for tracking progress

## Output

- **File Created/Updated:** `workdesk/sources.md`
- **Format:** Structured markdown with section headers, numbered IDs, and checklists of unique, sanitized URLs
- **Next Step:** [STEP_02_SUMMARIZE.md](STEP_02_SUMMARIZE.md)