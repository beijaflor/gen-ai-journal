# GitHub Issue Sync Workflow

This document describes how to sync `workdesk/sources.md` to GitHub issues for progress tracking using Claude Code's MCP GitHub integration.

## Overview

The sync workflow creates/updates a weekly GitHub issue that tracks:
- Total links collected
- Processing progress (completed vs pending)
- Complete source list with checkboxes
- Next steps for journal preparation

## Usage

### MCP-Based Sync Process

Claude Code can directly sync `workdesk/sources.md` to GitHub issues using its built-in MCP server integration:

1. **Automated Analysis**: Claude Code analyzes `workdesk/sources.md` to:
   - Count total links and categorize by section
   - Determine processing status (checked vs unchecked)
   - Calculate completion percentage
   - Generate appropriate week identifier

2. **GitHub Integration**: Using MCP server, Claude Code will:
   - Search for existing weekly issue by title pattern
   - Create new issue if none exists, or update existing issue
   - Apply appropriate labels automatically
   - Format content with proper markdown structure

### Simple Command

To sync sources to GitHub issue, simply ask Claude Code:

```
"Sync workdesk/sources.md to GitHub issue"
```

Claude Code will handle:
- Issue title generation (e.g., "Weekly Journal Sources - Week of 2025-07-21")
- Label assignment (e.g., "weekly-sources,journal-2025-07-21")
- Content formatting and progress tracking
- Issue creation or updates

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

The MCP-based sync can be triggered at any time to update progress:
- After adding new links to `workdesk/sources.md`
- After completing summaries (marked with [x])
- Before starting curation process
- At end of weekly collection period

Simply request: `"Sync workdesk/sources.md to GitHub issue"` and Claude Code handles the rest.

## Benefits

- **Simplified Workflow**: No manual script execution required
- **Intelligent Updates**: Claude Code determines whether to create or update issues
- **Consistent Formatting**: Automated markdown structure and labeling
- **Real-time Analysis**: Dynamic progress calculation and status tracking
- **Visibility**: Team/collaborators can see current progress
- **Planning**: Clear overview of collected sources
- **History**: Weekly issues serve as archive of collection periods
- **Integration**: Seamless GitHub project management integration