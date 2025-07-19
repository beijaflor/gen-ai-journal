# Step 7A: Create Omitted Summaries

## Overview

This workflow creates unified summaries from URLs that were not included in the weekly journal, using the `scripts/unite_summaries.py` script.

## Steps

### 1. Read the Omitted URLs List

- **Input**: `workdesk/omitted_sources.md`
- **Action**: Read the complete list of URLs truly omitted from both main and annex journals
- **Tool**: Read tool
- **Result**: 114 omitted URLs identified

### 2. Execute Processing Script

- **Script**: `scripts/unite_summaries.py`
- **Command**: `python3 scripts/unite_summaries.py workdesk/omitted_sources.md workdesk/summaries workdesk/omitted_summaries_unified.md`
- **Action**: Run script to match URLs with summaries and create unified file
- **Tool**: Bash command execution

### 3. Script Processing Flow

- **URL Extraction**: Extract URLs from `workdesk/omitted_sources.md` using regex
- **Summary Scanning**: Scan `workdesk/summaries/` directory for matching files
- **Content Mapping**: Match URLs to their corresponding summary content
- **Missing Detection**: Identify URLs without summaries

### 4. Generate Unified Output

- **Output**: `workdesk/omitted_summaries_unified.md`
- **Content**: All found summaries combined with `---` separators
- **Structure**: Header + metadata + individual summaries
- **Tool**: Script file writing

### 5. Create Missing Report

- **Output**: Console output (script reports missing URLs)
- **Content**: URLs without corresponding summaries
- **Purpose**: Document gaps in summary coverage

## Processing Results

- **Total omitted URLs**
- **Summaries found**
- **Summaries missing**
- **Coverage**
- **Processing status**

## Benefits

1. **Comprehensive Coverage**: Captures all omitted content in one unified document
2. **Quality Control**: Identifies URLs without summaries for follow-up
3. **Editorial Transparency**: Documents what was excluded from both main and annex journals
4. **Content Audit**: Provides complete picture of all processed sources
5. **Automated Processing**: Uses existing script for consistent results
