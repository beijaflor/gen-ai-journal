# Step 12: Create Pull Request

## Overview
Create a pull request for the completed journal. In the modern workflow, pull requests are typically created early in the process (after Step 3 or when significant work begins) to enable collaborative editing and continuous review.

## When to Create PR
**Early Creation (Recommended):**
- Create PR after Step 3 (Prepare Journal) when structure is ready
- Allows for collaborative editing throughout the workflow
- Enables continuous review and feedback

**Late Creation (Legacy):**
- Create PR after Step 10 (Archive & Cleanup) when journal is complete
- Traditional approach for final review only

## Pre-PR Checklist
- [ ] All journal files are in `journals/YYYY-MM-DD/` directory
- [ ] Workdesk is cleaned up (sources and summaries archived)
- [ ] URLs verified and working
- [ ] Editorial quality standards met
- [ ] Metadata file generated (`journal-metadata.json`)
- [ ] All workflow steps completed

## Commands

### For Early PR Creation (Recommended)
After Step 3 when journal structure is ready:

```bash
# Create initial commit with journal structure
git add journals/YYYY-MM-DD/
git commit -m "Initialize journal structure for YYYY-MM-DD

- Created journal directory structure
- Ready for content development

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push and create draft PR
git push origin journal/YYYY-MM-DD
gh pr create --draft --title "Journal for YYYY-MM-DD (WIP)" --body "$(cat <<'EOF'
## Summary
- Weekly journal for YYYY-MM-DD (Work in Progress)
- Journal structure created and ready for content development

## Progress Checklist
- [x] Journal structure created
- [ ] Sources curated
- [ ] Content reviewed and refined
- [ ] Final quality checks completed

## Content Overview
- Content will be added as workflow progresses

🤖 Generated with [Claude Code](https://claude.ai/code)
EOF
)"
```

### For Final PR Update (Complete Journal)
When journal is complete after Step 10:

```bash
# Commit final changes
git add journals/YYYY-MM-DD/
git commit -m "Complete journal for YYYY-MM-DD

- Main journal: X articles
- Annex journal: Y articles
- Total sources processed: Z articles
- All sources verified and archived
- Metadata file generated

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push and update PR (convert from draft if needed)
git push origin journal/YYYY-MM-DD
gh pr ready  # Convert from draft to ready for review

# Or create new PR if not created early
gh pr create --title "Journal for YYYY-MM-DD" --body "$(cat <<'EOF'
## Summary
- Completed weekly journal for YYYY-MM-DD
- Main journal: X high-impact articles
- Annex journal: Y unique perspective articles
- Total sources processed: Z articles

## Content Overview
- [Brief description of major themes/topics covered]

## Quality Checks
- [x] All URLs verified and working
- [x] Editorial standards applied
- [x] Files properly archived to journals/ directory
- [x] Workdesk cleaned up
- [x] Metadata file generated
- [x] Complete coverage of curated sources

🤖 Generated with [Claude Code](https://claude.ai/code)
EOF
)"
```

## What Happens Next

### For Early PR Creation:
1. **Continuous Development**: Continue with Steps 4-10, committing progress regularly
2. **Collaborative Editing**: Team members can review and contribute throughout development
3. **Draft Status**: PR remains in draft until journal is complete
4. **Final Review**: Convert to ready-for-review when Step 10 is complete

### For Complete Journal:
1. **Human Review**: The human reviewer will examine the journal content and quality
2. **Merge Decision**: Human will merge the PR when ready to publish
3. **Publication**: After merge, proceed to [STEP_13_TAG_PUBLISH.md](STEP_13_TAG_PUBLISH.md) for tagging and publication

## Workflow Integration

**Modern Recommended Flow:**
```
Step 01 → Step 02 → Step 03 → CREATE DRAFT PR → Steps 04-11 → CONVERT TO READY → Human Review → Merge → Step 13
```

**Legacy Flow:**
```
Steps 01-11 → CREATE PR → Human Review → Merge → Step 13
```

## Notes
- **Early PR Creation** enables better collaboration and continuous feedback
- **Draft PRs** keep development visible without requesting immediate review
- **Human retains control** over publication timing regardless of PR creation method
- **Branch cleanup** happens in STEP_13 after successful publication
- **Continuous commits** during development help track progress and enable rollback if needed