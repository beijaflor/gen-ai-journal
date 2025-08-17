# Step 11: Create Pull Request

## Overview
Create a pull request for the completed journal. The human reviewer will handle the merge to main branch after review.

## Pre-PR Checklist
- [ ] All journal files are in `journals/YYYY-MM-DD/` directory
- [ ] Workdesk is cleaned up (sources and summaries archived)
- [ ] URLs verified and working
- [ ] Editorial quality standards met
- [ ] All workflow steps completed

## Commands

### Commit final changes
```bash
git add journals/YYYY-MM-DD/
git commit -m "Complete journal for YYYY-MM-DD

- Main journal: X articles
- Annex journal: Y articles  
- All sources verified and archived

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Push branch and create PR
```bash
git push origin journal/YYYY-MM-DD

# Create pull request using GitHub CLI
gh pr create --title "Journal for YYYY-MM-DD" --body "$(cat <<'EOF'
## Summary
- Completed weekly journal for YYYY-MM-DD
- Main journal: X high-impact articles
- Annex journal: Y unique perspective articles

## Content Overview
- [Brief description of major themes/topics covered]

## Quality Checks
- [x] All URLs verified and working
- [x] Editorial standards applied
- [x] Files properly archived to journals/ directory
- [x] Workdesk cleaned up

🤖 Generated with [Claude Code](https://claude.ai/code)
EOF
)"
```

## What Happens Next

After creating the pull request:
1. **Human Review**: The human reviewer will examine the journal content and quality
2. **Merge Decision**: Human will merge the PR when ready to publish
3. **Publication**: After merge, proceed to [STEP_12_TAG_PUBLISH.md](STEP_12_TAG_PUBLISH.md) for tagging and publication

## Notes
- Pull request enables quality review and collaborative editing
- Human retains control over publication timing
- Branch will be cleaned up in STEP_12 after successful publication