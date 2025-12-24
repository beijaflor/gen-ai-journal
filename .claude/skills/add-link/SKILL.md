---
name: add-link
description: Process and add source URLs to the Gen AI journal following STEP_01_GATHER_SOURCES workflow. Use when user provides links, mentions gathering sources, or wants to add articles to the journal workdesk.
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# Add Link to Gen AI Journal

This skill processes URLs and adds them to the Gen AI journal workdesk, including validation, deduplication, and automatic summary generation.

## When to Use This Skill

Use this skill when the user:
- Provides URLs to add to the journal
- Says "add these links" or "gather these sources"
- Mentions "add to journal" or "process these URLs"
- Provides a list of article links for the weekly journal

## Complete Workflow

For each URL provided, execute these steps in sequence:

### 1. Check and Validate URL

```bash
uv run scripts/check_link.py "URL_HERE"
```

- Validates and sanitizes the URL (removes tracking parameters)
- Checks for duplicates in:
  - `workdesk/sources.md`
  - `workdesk/summaries/` directory
  - Published journals (`journals/*/sources/*.md`)
- If duplicate, report and skip to next URL
- Note the sanitized URL for adding to sources.md

### 2. Add to sources.md

- Read `workdesk/sources.md` to determine the next available ID
- Add the sanitized URL with proper ID formatting:
  ```markdown
  - [ ] XXX. https://example.com
  ```
- Use Edit tool to add the URL under the "Main List" section (default)

### 3. Generate Summary

- Create appropriate filename: `XXX_domain_title.md` (e.g., `001_github_blog_copilot.md`)
- Run:
  ```bash
  uv run scripts/call-gemini.py --url "SANITIZED_URL" --output workdesk/summaries/XXX_filename.md
  ```
- Wait for summary generation to complete
- Verify the summary file was created successfully

### 4. Mark as Processed

- Update the checkbox in `workdesk/sources.md` from `[ ]` to `[x]` for this URL
- Use Edit tool to mark the specific line

### 5. Report Progress

- After processing each URL, report: ID, status (success/failed), and any issues
- Continue to next URL

## Batch Processing Strategy

When given multiple URLs:

1. Create TodoWrite entries to track batches (e.g., "Process URLs 1-5")
2. Check all URLs first to identify duplicates
3. Process each unique URL completely (add → summarize → mark) before moving to next
4. Update TodoWrite after completing each batch
5. Provide final summary: total processed, duplicates found, any errors

## Key Responsibilities

1. **URL Management**: Sanitize URLs, remove tracking parameters, check for duplicates
2. **File Organization**: Maintain proper ID numbering, consistent formatting
3. **Summary Generation**: Generate summaries for ALL unique URLs
4. **Progress Tracking**: Use TodoWrite to track batches of URLs being processed
5. **Error Handling**: Report failures clearly, continue with remaining URLs

## Project Standards

- Use absolute paths when referencing files
- Maintain 2-space indentation for Markdown lists
- Summary filenames: lowercase, underscores, descriptive
- Always check for existing summaries before generating
- Documentation in English, journal content in Japanese

## File Locations

- **Sources list**: `workdesk/sources.md`
- **Summaries**: `workdesk/summaries/XXX_filename.md`
- **Validation script**: `scripts/check_link.py`
- **Summary script**: `scripts/call-gemini.py`
- **Workflow docs**: `workflow/STEP_02_GATHER_SOURCES.md`

## Error Handling

- If URL validation fails, report the error and skip to next URL
- If summary generation fails, report but don't block other URLs
- If duplicate found, report which file contains it
- Always complete the workflow for valid, unique URLs

## Programmatic Usage

For batch processing without interactive mode, use the bulk script:

```bash
# From file (one URL per line)
uv run scripts/bulk_add_links.py urls.txt

# From stdin
cat urls.txt | uv run scripts/bulk_add_links.py

# Dry run (check without adding)
uv run scripts/bulk_add_links.py urls.txt --dry-run

# Skip summary generation
uv run scripts/bulk_add_links.py urls.txt --no-summarize
```

## Examples

**User provides URLs**:
"Add these to the journal: https://example.com/ai-news, https://github.com/blog/copilot"

**Skill activates and**:
1. ✓ Validates both URLs
2. ✓ Checks for duplicates
3. ✓ Adds to sources.md as 001 and 002
4. ✓ Generates Japanese summaries
5. ✓ Marks as processed
6. ✓ Reports: "Added 2 new sources (001-002)"

You are detail-oriented and systematic, ensuring each source is completely processed (including summarization) according to the workflow. You proactively identify issues like broken links, duplicate entries, or sources that don't meet curation standards.
