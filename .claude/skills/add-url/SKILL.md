---
name: add-url
description: Add source URLs to workdesk/sources.md one-by-one with validation and duplication checking. Use when user provides links to add to the journal. Does NOT generate summaries.
allowed-tools: Read, Edit, Bash, Grep, Glob
---

# Add URL to Gen AI Journal

This skill validates and adds URLs to `workdesk/sources.md` one-by-one. It performs duplication checking but does NOT generate summaries. Use the `summarize-source` skill separately for summary generation.

## When to Use This Skill

Use this skill when the user:
- Provides URLs to add to the journal
- Says "add this link" or "add these URLs"
- Mentions "add to sources" or "gather these links"
- Provides article links for the weekly journal

## Workflow Per URL

**CRITICAL: Always ensure you're in the repository root directory before executing any commands.**

```bash
cd /Users/shootani/Dropbox/github/gen-ai-journal
```

For each URL provided, execute these steps in sequence:

### 1. Validate and Check for Duplicates

```bash
uv run scripts/check_link.py "URL_HERE"
```

This script:
- Validates and sanitizes the URL (removes tracking parameters)
- Checks for duplicates in:
  - `workdesk/sources.md`
  - `workdesk/summaries/` directory
  - Published journals (`journals/*/sources/*.md`)
- Returns the sanitized URL if unique

**If duplicate found**: Report which file contains it and skip to next URL

**If unique**: Note the sanitized URL and proceed to step 2

### 2. Add to sources.md (Unchecked)

1. Read `workdesk/sources.md` to determine the next available ID
2. Add the sanitized URL under "## Main List" section with unchecked checkbox:
   ```markdown
   - [ ] XXX. https://sanitized-url-here.com
   ```
3. Use Edit tool to insert the new entry
4. IDs should be zero-padded 3-digit numbers (001, 002, etc.)

### 3. Report Progress

After processing each URL, report:
- **Success**: "✓ Added as ID XXX (unchecked, ready for summarization)"
- **Duplicate**: "✗ Skipped - duplicate found in [location]"
- **Error**: "✗ Failed - [error message]"

## Batch Processing Strategy

When given multiple URLs:

1. Process each URL completely before moving to next
2. Create TodoWrite entries to track progress (e.g., "Add URLs 1-5", "Add URLs 6-10")
3. Provide running count: "Added 3/10 URLs so far..."
4. At the end, provide summary:
   - Total URLs processed
   - Successfully added (with ID range)
   - Duplicates skipped
   - Any errors

### Ordering Guarantee (Input Order Preservation)

When the user supplies an ordered list of URLs, the IDs assigned in
`workdesk/sources.md` MUST reflect that input order. This is a hard contract,
not a best-effort behavior — downstream STEP_02 verification cross-checks
summaries against the original input list by ID.

**Rules:**

1. **Strict input order.** URLs are validated and appended to `sources.md`
   strictly sequentially in the order received. Do NOT validate or append
   multiple URLs in parallel (no parallel `Bash` tool calls for `check_link.py`
   across different URLs in the same batch, no parallel `Edit` calls to
   `sources.md`). Finish one URL fully — validate, then append (or skip) — before
   touching the next.
2. **Duplicates and failures do not consume IDs.** If a URL is a duplicate
   (`check_link.py` reports it already exists) or fails validation, skip it and
   move to the next URL. The next ID is reserved only when an entry is actually
   committed to `sources.md`.
3. **Assigned IDs strictly increase in input order.** Given input
   `[URL_A, URL_B, URL_C]` where `URL_B` is a duplicate, the result is:
   - `URL_A` → lowest new ID (e.g. `213`)
   - `URL_B` → skipped (no ID consumed)
   - `URL_C` → next ID (`214`)

   `URL_C` MUST NOT receive an ID lower than `URL_A`'s.

**Why it matters:** STEP_02 (summarization) and any manual spot-check against
the user's original URL list rely on `ID order == input order`. Any
out-of-order assignment forces manual re-alignment downstream and is treated as
a bug (see issue #120).

The `scripts/bulk_add_links.py` helper, when used, encodes this same contract:
URLs are processed one at a time and the next ID is only assigned after the
previous URL has been committed to `sources.md`.

## What This Skill Does NOT Do

- ❌ Does NOT generate summaries
- ❌ Does NOT mark URLs as checked/processed
- ❌ Does NOT call call-gemini.py or batch_summarize.py

Use the `summarize-source` skill after adding URLs to generate summaries.

## Key Responsibilities

1. **URL Validation**: Use check_link.py to validate and sanitize URLs
2. **Duplication Checking**: Prevent adding duplicate URLs
3. **ID Management**: Maintain sequential ID numbering
4. **File Organization**: Add URLs under "## Main List" section with consistent formatting
5. **Progress Tracking**: Use TodoWrite for batch operations
6. **Error Handling**: Report failures clearly, continue with remaining URLs

## Project Standards

- Use absolute paths when referencing files
- Maintain 2-space indentation for Markdown lists
- IDs must be zero-padded 3-digit numbers (001, 002, 003, etc.)
- All new entries start as unchecked `- [ ]`
- Documentation in English, journal content in Japanese

## File Locations

- **Sources list**: `workdesk/sources.md`
- **Validation script**: `scripts/check_link.py`
- **Workflow docs**: `workflow/STEP_01_GATHER_SOURCES.md`

## Error Handling

- If URL validation fails, report the error and skip to next URL
- If duplicate found, report which file contains it
- If Edit operation fails, report and continue with remaining URLs
- Always complete the workflow for valid, unique URLs

## Examples

**User provides URLs**:
```
Add these to the journal:
- https://example.com/ai-news
- https://github.com/blog/copilot
```

**Skill activates and**:
1. ✓ Validates both URLs using check_link.py
2. ✓ Checks for duplicates (none found)
3. ✓ Adds to sources.md as 089 and 090 (unchecked)
4. ✓ Reports: "Added 2 URLs (089-090). Use summarize-source skill to generate summaries."

**Next step (separate)**:
User or skill invokes `summarize-source` skill to generate summaries for the unchecked URLs.

## Programmatic Usage

For batch URL addition without interactive mode:

```bash
# NOT RECOMMENDED - Use the skill for one-by-one addition
# For bulk operations, manually edit sources.md or use the skill in a loop
```

This skill is optimized for interactive, one-by-one URL addition with immediate validation feedback.

## Relationship to Other Skills

- **After add-url**: Use `summarize-source` skill to generate summaries
- **Before add-url**: URLs are typically gathered from various sources (RSS, newsletters, manual curation)

You are detail-oriented and systematic, ensuring each URL is validated and added with proper ID sequencing. You proactively identify duplicates and broken links, preventing issues downstream.
