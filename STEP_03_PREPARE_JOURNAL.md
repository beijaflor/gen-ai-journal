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

### 3. Admin Review & Flagging (Optional with Supabase)

If using the Supabase admin system, you can now review and flag summaries before curation:

- [ ] Start development server:
  ```bash
  cd website && npm run dev
  ```

- [ ] Sign in at http://localhost:4321/auth/login with admin credentials

- [ ] Review workdesk summaries (accessible from homepage sidebar)

- [ ] For each summary, click "Edit Curation" and set flags:
  - **Annex flag**: Consider for annex journal (unique perspectives)
  - **Standout flag**: Exceptional content worth highlighting
  - **Omit flag**: Too specialized or low quality
  - **Upvote/Downvote**: Editorial endorsement or concerns

- [ ] Flags auto-save to Supabase database

**Benefits:**
- Pre-flag promising content before detailed curation
- Track editorial decisions with audit trail
- Export flagged summaries as curation starting points

**Note:** This is supplementary to the editorial workflow. Final curation decisions in STEP_04/STEP_05 remain manual based on established criteria.

See [SUPABASE_WORKFLOW_INTEGRATION.md](SUPABASE_WORKFLOW_INTEGRATION.md) for complete admin system documentation.

## Output

- **Files Created:** Empty journal files in workdesk for editing
- **Working Directory:** All files remain in workdesk for active editing workflow
- **Next Step:** [STEP_04_CURATE_MAIN.md](STEP_04_CURATE_MAIN.md)

## Note

Files will only be moved to the final `journals/YYYY-MM-DD/` directory structure in STEP_08 after all editing is complete. This keeps the active editing workflow contained in workdesk.

## Optional: Create Early Draft PR (Recommended)

After completing this step, you can optionally create a draft pull request to enable collaborative editing throughout the workflow:

```bash
# Commit initial journal structure
git add workdesk/weekly_journal_YYYY_MM_DD.md workdesk/annex_journal_YYYY_MM_DD.md
git commit -m "Initialize journal structure for YYYY-MM-DD

- Created empty journal files in workdesk
- Ready for content development (STEP_03 complete)
- N sources collected and summarized

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to remote
git push origin journal/YYYY-MM-DD

# Create draft PR (using GitHub MCP or gh CLI)
# See STEP_12_PULL_REQUEST.md for detailed PR creation instructions
```

**Benefits of Early PR Creation:**
- Continuous visibility into journal development
- Enable collaborative editing throughout workflow
- Track progress through commits
- Keep PR in draft status until STEP_11 complete
- Convert to "Ready for review" before final merge

See [GITHUB_SYNC.md](GITHUB_SYNC.md) for detailed pull request workflow.