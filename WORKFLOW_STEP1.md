## Step 1: Start from a GitHub Issue and Prepare Sources

Begin by identifying the GitHub issue that contains the list of source URLs for the weekly journal. Use the `get_issue` tool to retrieve its content. Copy these links into `workdesk/sources.md`, converting them into a checklist format.

- [ ] Run `python3 process_sources.py workdesk/sources.md`. This script will:
    - Sanitize links by removing UTM parameters.
    - Remove duplicate links.
- [ ] **Verify:**
    - [ ] Confirm that UTM parameters have been removed from links.
    - [ ] Confirm that no duplicate links remain.