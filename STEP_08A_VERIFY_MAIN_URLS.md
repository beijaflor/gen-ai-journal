# Step 8A: Verify Main Journal URLs

## Overview

This workflow verifies that all URLs in the weekly journal are properly sourced from the curated sources list.

## Steps

### 1. Read the Weekly Journal

- **Input**: `workdesk/weekly_journal_2025_07_12.md`
- **Action**: Read the entire journal content to access all URLs
- **Tool**: Read tool

### 2. Read the Sources List

- **Input**: `workdesk/sources.md`
- **Action**: Read the master list of curated sources
- **Tool**: Read tool

### 3. Extract URLs from Journal

- **Action**: Use grep to find all URLs in the journal
- **Pattern**: `^https://` (URLs at the beginning of lines)
- **Tool**: Grep tool with content output mode
- **Result**: URLs extracted

### 4. Cross-Reference URLs

- **Action**: Check each journal URL against sources.md
- **Method**: Use Task tool to systematically verify each URL
- **Result**: All URLs found in sources.md with their entry numbers

### 5. Generate Report

- **Output**: Verification summary showing:
  - ✅ All URLs that were found (with entry numbers)
  - ❌ Any URLs not found in sources
- **Result**: 100% match - all journal URLs are from sources.md

### 6. Export Curated URLs

- **Output**: `workdesk/curated_journal_sources.md`
- **Content**: Clean list of all URLs used in the journal
- **Tool**: Write tool

## Verification Results

- **Total URLs in journal**: 18
- **URLs found in sources.md**: 18
- **URLs not in sources.md**: 0
- **Verification status**: ✅ 100% PASS - All URLs verified

## Benefits

1. Ensures editorial integrity - all content is from vetted sources
2. Provides traceability - can track which sources were used
3. Enables quality control - identifies any unauthorized sources
4. Creates reusable list - curated URLs can be used for future reference

## Next Step

[STEP_08B_VERIFY_ANNEX_URLS.md](STEP_08B_VERIFY_ANNEX_URLS.md) - Verify annex journal URLs, then proceed to cleanup
