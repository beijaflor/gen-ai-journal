# Pull Request Description Template

Use this template when creating or updating PR descriptions for workflow tracking.

## PR Title Format

```
Journal YYYY-MM-DD - [Current Stage]
```

Examples:
- `Journal 2026-01-20 - WIP: Gathering Sources`
- `Journal 2026-01-20 - Draft: Curation in Progress`
- `Journal 2026-01-20 - Ready for Review`

## PR Description Template

```markdown
## Journal YYYY-MM-DD - Workflow Progress

**Current Stage**: STEP_XX - [Stage Name]

**Overall Progress**: X/14 steps (Y%)

---

### Recent Updates

- [List recent changes since last PR update]
- [What files were added/modified]
- [What milestones were reached]

---

### Workflow Checklist

**Source Collection & Summaries**
- [x] STEP_01: Gather sources (X links)
- [x] STEP_02: Generate summaries (Y summaries)
- [x] STEP_03: Create unified summaries

**Editorial Planning & Curation**
- [ ] STEP_03b: Plan editorial themes
- [ ] STEP_04: Curate main journal
- [ ] STEP_05: Identify non-main sources

**Journal Assembly**
- [ ] STEP_06-11: [Assembly steps]
- [ ] STEP_12: Final review
- [ ] STEP_13-14: Publication

---

### Current Metrics

| Metric | Count | Status |
|--------|-------|--------|
| Total Sources | X | - |
| Processed Sources | Y | Z% |
| Summaries Generated | N | - |
| Main Articles Curated | M | [Status] |
| Annex Articles | A | [Status] |

---

### Workdesk Status

- `workdesk/sources.md`: X links (Y checked)
- `workdesk/summaries/`: N files
- `workdesk/unified_summaries.md`: [✅ / ⏳ / ❌]
- `workdesk/editorial_plan_*.md`: [✅ / ⏳ / ❌]
- `workdesk/curated_journal_sources.md`: [✅ / ⏳ / ❌]

---

### Next Steps

1. [Next immediate action]
2. [Upcoming milestone]
3. [Any blockers or dependencies]

---

**Related Issue**: #XXX (Weekly workflow tracking issue)

**Branch**: `[branch-name]`
**Last Updated**: [ISO 8601 timestamp]
```

## PR Creation Settings

When creating a new PR:

```json
{
  "draft": true,
  "base": "main",
  "head": "[feature-branch]",
  "title": "Journal YYYY-MM-DD - WIP: [Current Stage]",
  "body": "[Use template above]"
}
```

## Dynamic Content Instructions

Replace placeholders:
- `YYYY-MM-DD`: Extract from sources.md title
- `STEP_XX`: Current workflow step
- `X/14 steps`: Count completed milestones
- Checklist: Mark completed steps with `[x]`, pending with `[ ]`
- Metrics table: Fill with current counts from workdesk analysis
- Recent updates: Compare with previous commit messages or list what changed
- Related issue: Link to weekly tracking issue
- Branch name: From `git branch --show-current`
- Timestamp: ISO 8601 format

## PR Update Strategy

- **Draft status**: Keep as draft until STEP_12 (final review)
- **Title updates**: Update stage name as workflow progresses
- **Description**: Update entire description with current state
- **Never update**: Closed PRs (report to user instead)
