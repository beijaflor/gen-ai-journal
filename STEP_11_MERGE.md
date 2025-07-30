# Step 11: Merge to Main

## Overview
Create a pull request and merge the completed journal to the main branch after final review.

## Pre-merge Checklist
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

### Merge and cleanup
```bash
# After PR approval, merge and cleanup
gh pr merge --squash
git checkout main
git pull origin main
git branch -d journal/YYYY-MM-DD
```

## Alternative: Direct merge (if no review needed)
```bash
git checkout main
git merge journal/YYYY-MM-DD
git push origin main
git branch -d journal/YYYY-MM-DD
```

## Post-merge Tasks
- [ ] Verify journal appears correctly on main branch
- [ ] Clean up any remaining local branches
- [ ] Update tracking/status files if needed

## Notes
- Use pull request for quality review and team collaboration
- Squash merge keeps clean history on main branch
- Branch deletion prevents accumulation of stale branches