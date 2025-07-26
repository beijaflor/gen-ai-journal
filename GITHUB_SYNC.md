# GitHub Issue Sync Workflow

This document describes how to sync `workdesk/sources.md` to GitHub issues for progress tracking.

## Overview

The sync workflow creates/updates a weekly GitHub issue that tracks:
- Total links collected
- Processing progress (completed vs pending)
- Complete source list with checkboxes
- Next steps for journal preparation

## Usage

### 1. Generate Issue Content

```bash
./scripts/sync_to_github.sh
```

This will output:
- Issue title (e.g., "Weekly Journal Sources - Week of 2025-07-21")
- Suggested labels (e.g., "weekly-sources,journal-2025-07-21")
- Formatted issue body with progress summary

### 2. Create/Update GitHub Issue

Use Claude Code's GitHub integration to:

1. **Search for existing issue**:
   - Look for title containing the week identifier (e.g., "Week of 2025-07-21")
   
2. **If issue exists**:
   - Update the issue body with new content
   - Progress tracking will be automatically updated
   
3. **If no issue exists**:
   - Create new issue with the generated title and body
   - Add suggested labels for organization

## Issue Structure

The generated GitHub issue includes:

### Progress Summary
- Total links collected
- Number processed (with summaries)
- Number pending
- Completion percentage

### Source Links
- Complete contents of `workdesk/sources.md`
- Checkbox format for easy progress tracking
- Organized by category (Main List, Slides, etc.)

### Next Steps
- Automated checklist for journal workflow
- Links to relevant workflow steps

## Automation

The sync can be run at any time to update progress:
- After adding new links
- After completing summaries
- Before starting curation
- At end of weekly collection period

## Benefits

- **Visibility**: Team/collaborators can see current progress
- **Planning**: Clear overview of collected sources
- **History**: Weekly issues serve as archive of collection periods
- **Integration**: Links to broader GitHub project management