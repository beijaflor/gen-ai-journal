# Step 13: Tag & Publish

## Overview
After the pull request has been merged by human review, tag the release and perform any publication tasks. This final step completes the journal publication workflow.

## Prerequisites
- [ ] Pull request from STEP_12 has been merged to main branch by human reviewer
- [ ] Journal files are now on main branch in `journals/YYYY-MM-DD/` directory
- [ ] Ready to publish and tag the journal release

## Publication Workflow

### 1. Switch to Main and Update
```bash
# Switch to main branch and get latest changes
git checkout main
git pull origin main
```

### 2. Verify Journal Publication
```bash
# Verify the journal files are present on main
ls -la journals/YYYY-MM-DD/
```

### 3. Create Release Tag
```bash
# Create semantic version tag based on journal date
git tag -a "YYYY-MM-DD" -m "Weekly GenAI Journal - [Month Day, Year]

## Summary
- Main journal: X high-impact articles
- Annex journal: Y unique perspective articles
- Total sources processed: Z articles

## Highlights
- [Brief description of major themes/topics covered]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push the tag to remote
git push origin YYYY-MM-DD
```

### 4. Cleanup Feature Branch
```bash
# Delete the feature branch (both local and remote)
git branch -d journal/YYYY-MM-DD
git push origin --delete journal/YYYY-MM-DD
```

### 5. Optional: Create GitHub Release
```bash
# Create a GitHub release from the tag (optional)
gh release create YYYY-MM-DD \
  --title "GenAI Weekly Journal - [Month Day, Year]" \
  --notes "Weekly curated journal of AI and coding developments. See journals/YYYY-MM-DD/ for full content."
```

## Post-Publication Tasks

### Verification
- [ ] **Tag Created**: Verify tag exists with `git tag -l`
- [ ] **Branch Cleaned**: Confirm feature branch is deleted
- [ ] **Files Accessible**: Check journal files are accessible on main branch
- [ ] **Release Published**: Verify GitHub release (if created)

### Workspace Preparation
- [ ] **Workdesk Ready**: Confirm workdesk is clean for next cycle
- [ ] **Next Branch**: Ready to start next journal cycle with STEP_00

## Tag Naming Convention

Use date-based versioning for journal releases:
- Format: `YYYY-MM-DD`
- Examples:
  - `2025-08-16` for August 16, 2025 journal
  - `2025-08-23` for August 23, 2025 journal
  - `2025-12-31` for December 31, 2025 journal

## Alternative Publication Methods

### Direct Publication (No GitHub Release)
```bash
# Minimal publication - just tag and cleanup
git tag -a "YYYY-MM-DD" -m "Weekly journal for YYYY-MM-DD"
git push origin YYYY-MM-DD
git branch -d journal/YYYY-MM-DD
```

### Extended Publication (With Deployment)
```bash
# If you have additional deployment steps
# Add deployment commands here, e.g.:
# ./deploy.sh journals/2025-08-16/
# rsync -av journals/2025-08-16/ user@server:/var/www/journals/
```

## Next Cycle

After successful publication:
1. **Ready for Next Week**: Workspace is prepared for new journal cycle
2. **Start Fresh**: Begin next journal with [STEP_01_CREATE_BRANCH.md](STEP_01_CREATE_BRANCH.md)
3. **Continuous Cycle**: The workflow continues weekly

## Notes
- Human controls the merge timing in STEP_12
- This step handles the technical publication aspects
- Tags provide permanent references to journal releases
- Branch cleanup prevents repository bloat
- Workspace remains ready for immediate next cycle start