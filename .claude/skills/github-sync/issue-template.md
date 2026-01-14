# GitHub Issue Template

Use this template when creating or updating workflow tracking issues.

## Title Format

```
Journal Workflow - Week of YYYY-MM-DD
```

## Body Template

```markdown
## Workflow Progress

**Current Stage**: STEP_XX - [Stage Name]

**Overall Progress**: X/14 steps completed (Y%)

---

## STEP_01-02: Source Collection & Summaries

### Sources (workdesk/sources.md)
- **Total Links**: X
- **Processed (Checked)**: Y (Z%)
- **Pending (Unchecked)**: N

### Summaries (workdesk/summaries/)
- **Files Generated**: X/Y
- **Status**: [✅ Complete / ⏳ In Progress / ❌ Not Started]

---

## STEP_03: Unified Summaries

### Main Summaries (workdesk/unified_summaries.md)
- **Status**: [✅ Generated / ⏳ Pending / ❌ Not Started]
- **Word Count**: X words (if generated)
- **Summary Count**: Y summaries (if generated)

---

## STEP_03b: Editorial Planning

### Editorial Plan (workdesk/editorial_plan_*.md)
- **Status**: [✅ Approved / 📝 Draft / ❌ Not Started]
- **Themes Identified**: X themes (if exists)
- **Approval Status**: [APPROVED / PENDING REVIEW / N/A]

---

## STEP_04-05: Journal Curation

### Main Journal (workdesk/curated_journal_sources.md)
- **Status**: [✅ Complete / ⏳ In Progress / ❌ Not Started]
- **Articles Selected**: X articles (if exists)

### Non-Main Sources (workdesk/non_main_sources.md)
- **Status**: [✅ Complete / ⏳ In Progress / ❌ Not Started]
- **Annex Articles**: X articles (if exists)

### Annex Summaries (workdesk/unified_summaries_annex.md)
- **Status**: [✅ Generated / ⏳ Pending / ❌ Not Started]

---

## STEP_06-14: Journal Assembly & Publication

[Note presence of any advanced stage files if detected]

---

## Workdesk Files

<details>
<summary>View all workdesk files (X files)</summary>

```
[Output of: tree workdesk/ or ls -R workdesk/]
```

</details>

---

## Next Steps

- [ ] [Next action based on current stage]
- [ ] [Blocking issues or dependencies]

---

## Source Links

<details>
<summary>View all source URLs (X total, Y processed)</summary>

[Complete contents of workdesk/sources.md]

</details>

---

**Last Updated**: [ISO 8601 timestamp]
**Branch**: [current-branch-name]
**Commit**: [short SHA]
```

## Labels to Apply

- `workflow-tracking`
- `journal-YYYY-MM-DD` (extract date from sources.md)
- `step-XX` (current step number)

## Dynamic Content Instructions

Replace placeholders:
- `YYYY-MM-DD`: Extract from `# Sources for Journal YYYY-MM-DD` in sources.md
- `X/14 steps`: Count completed workflow milestones
- Link counts: Parse `- [x]` vs `- [ ]` in sources.md
- File statuses: Check file existence with `ls` or Read tool
- Word/summary counts: Parse files if they exist
- Timestamps: Use ISO 8601 format
- Branch/commit: From `git branch --show-current` and `git rev-parse --short HEAD`
