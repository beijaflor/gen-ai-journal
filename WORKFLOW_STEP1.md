## Step 1: Prepare Initial Source List

This step creates the initial, temporary list of source URLs for the week in the `workdesk` directory.

- [ ] **Gather Sources:**
    - [ ] Identify the GitHub issue containing the list of source URLs for the weekly journal.
    - [ ] Use the `get_issue` tool to retrieve its content.
    - [ ] Copy the links into `workdesk/sources.md`, converting them into a checklist format.

- [ ] **Process Sources:**
    - [ ] Run `python3 process_sources.py workdesk/sources.md`. This script sanitizes the list in-place by:
        - Removing UTM parameters from links.
        - Removing duplicate links.
    - [ ] **Verify:**
        - [ ] Confirm that links in `workdesk/sources.md` are sanitized and unique.
