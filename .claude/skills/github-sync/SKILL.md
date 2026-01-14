---
name: github-sync
description: Sync entire workdesk/ directory to GitHub issues and pull requests for comprehensive workflow progress tracking across all steps.
allowed-tools: Read, Bash, Grep, Glob, Edit, mcp__github-server__list_issues, mcp__github-server__create_issue, mcp__github-server__update_issue, mcp__github-server__search_issues, mcp__github-server__list_pull_requests, mcp__github-server__get_pull_request, mcp__github-server__update_pull_request, mcp__github-server__create_pull_request
---

# GitHub Sync Skill

Syncs the entire `workdesk/` directory to GitHub issues and pull requests for comprehensive workflow progress tracking.

## When to Use This Skill

Use this skill ONLY when:
- User explicitly says "sync to GitHub" or "sync workdesk to GitHub"
- User says "update workflow issue" or "sync workflow progress"
- User says "create workflow PR" or "update workflow PR"
- User wants to sync workflow progress with team

**Do NOT use this skill when**:
- User asks to create PR for code changes (not workflow tracking)
- User asks to update issues unrelated to workflow tracking
- General GitHub operations not related to workdesk sync

## Core Workflow

### 1. Analyze Workdesk State

Scan workdesk directory to gather metrics:

```bash
# Count sources
grep -c "^- \[.\]" workdesk/sources.md
grep -c "^- \[x\]" workdesk/sources.md
grep -c "^- \[ \]" workdesk/sources.md

# Count summaries
find workdesk/summaries -name "*.md" -type f | wc -l

# Check for key files
ls workdesk/unified_summaries.md
ls workdesk/editorial_plan_*.md
ls workdesk/curated_journal_sources.md
ls workdesk/non_main_sources.md
```

Extract:
- Journal date from `workdesk/sources.md` title
- Total/checked/unchecked link counts
- Summary file counts
- Presence of workflow milestone files
- Current workflow stage (reference STEP_* docs if needed)

### 2. Commit Pending Changes

**CRITICAL**: Commit all workdesk changes before updating GitHub.

```bash
# Check status
git status --porcelain workdesk/

# Commit by category if changes exist
git add workdesk/summaries/
git commit -m "Add summaries for journal [DATE]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push to branch
git push
```

### 3. Update GitHub Issue

1. **Get repository info**: Extract owner/repo from `git remote get-url origin`
2. **Search for issue**: Use `mcp__github-server__search_issues` for title pattern `"Journal Workflow - Week of YYYY-MM-DD"`
3. **Create or update**:
   - If not found: Use `issue-template.md` to create new issue
   - If found: Update issue with current metrics
4. **Apply labels**: `workflow-tracking`, `journal-YYYY-MM-DD`, `step-XX`

### 4. Create or Update Pull Request

1. **Get current branch**: `git branch --show-current`
2. **Search for PR**: Use `mcp__github-server__list_pull_requests` with head filter
3. **If PR not found**: Create new draft PR using `mcp__github-server__create_pull_request`
4. **If PR found**:
   - Check PR status with `mcp__github-server__get_pull_request`
   - Update if open/draft using `mcp__github-server__update_pull_request`
   - Skip if closed (report to user)
5. **Use `pr-template.md`** for PR description

### 5. Report Results

Provide summary with:
- Issue and PR links
- Current workflow stage
- Key metrics (sources, summaries, completion %)
- What was committed

## Templates

Use separate template files for content:
- **Issue body**: See `issue-template.md`
- **PR description**: See `pr-template.md`

Read these files and populate with current metrics.

## Key Responsibilities

- ✅ Analyze entire workdesk/ directory
- ✅ Determine current workflow stage
- ✅ Commit all pending changes
- ✅ Create/update GitHub issues
- ✅ Create draft PR if not exists
- ✅ Update open/draft PRs
- ✅ Calculate completion metrics

## What This Does NOT Do

- ❌ Close pull requests or issues
- ❌ Update closed PRs
- ❌ Modify workdesk files
- ❌ Execute workflow steps

## Error Handling

- **Git conflicts**: Report, ask user to resolve
- **Closed PR**: Report, skip update
- **GitHub API errors**: Report error, suggest retry

## Project Standards

- Use relative paths from repository root
- Issue title: `Journal Workflow - Week of YYYY-MM-DD`
- PR title: `Journal YYYY-MM-DD - [Current Stage]`
- Always commit before GitHub operations
- Create draft PRs by default
- Never expose absolute paths from user's computer

You are thorough and systematic, analyzing workdesk to provide complete workflow visibility. You commit changes safely, update GitHub accurately, and create PRs when needed to enable collaborative editing.
