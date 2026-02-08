---
name: summarize-source
description: Generate summaries for unchecked sources in workdesk/sources.md. Supports single URL or batch processing. Use after adding URLs with add-url skill.
allowed-tools: Read, Edit, Bash, Grep, Glob
---

# Summarize Source URLs

This skill generates Japanese summaries for unchecked URLs in `workdesk/sources.md`. It can process a single URL by ID or batch-process all unchecked URLs at once.

## When to Use This Skill

Use this skill when:
- User says "summarize the sources" or "generate summaries"
- After adding URLs with `add-url` skill
- User wants to process unchecked URLs in sources.md
- Need to generate summary for a specific ID

## Workflow Options

**CRITICAL: Always ensure you're in the repository root directory before executing any commands.**

```bash
cd /Users/shootani/Dropbox/github/gen-ai-journal
```

### Option 1: Batch Process All Unchecked URLs (JSON Format - Default)

This is the most common workflow for processing multiple unchecked sources. **Now generates structured JSON summaries by default.**

```bash
uv run scripts/bulk_summarize.py
```

**What it does**:
1. Scans `workdesk/sources.md` for unchecked entries `- [ ] XXX. URL`
2. For each unchecked URL:
   - Generates **structured JSON summary** using Gemini AI with schema validation
   - Validates against JSON v1.0 schema (scores, topics, metadata)
   - Saves to `workdesk/summaries/XXX_domain.json`
   - Marks as checked `- [x]` in sources.md
3. Uses context caching for efficiency (automatic)
4. Provides progress updates and final summary

**Format options**:
```bash
# JSON format (default, recommended)
uv run scripts/bulk_summarize.py

# Markdown format (legacy)
uv run scripts/bulk_summarize.py --format markdown
```

**When to use**: Processing 2+ unchecked URLs at once

### Option 2: Single URL by ID

For processing a specific URL when you need more control.

**Steps**:

1. **Find the URL in sources.md**:
   ```bash
   grep "- \[ \] 089\." workdesk/sources.md
   ```

2. **Extract the URL** from the output

3. **Generate summary** (JSON format):
   ```bash
   uv run scripts/call-gemini.py --url "URL_HERE" --format json --output workdesk/summaries/089_domain_name.json
   ```

   Or markdown format (legacy):
   ```bash
   uv run scripts/call-gemini.py --url "URL_HERE" --format markdown --output workdesk/summaries/089_domain_name.md
   ```

4. **Validate JSON** (automatic for --format json):
   - Schema validation happens automatically
   - Script exits with error if validation fails
   - Check stderr for validation error details

5. **Mark as checked** in sources.md:
   - Use Edit tool to change `- [ ] 089.` to `- [x] 089.`

**When to use**:
- Processing a single specific URL
- Retrying a failed summary
- Testing summary generation

### Option 3: Batch Process Specific Range

For processing a subset of unchecked URLs.

```bash
# First, manually mark the URLs you DON'T want to process as checked temporarily
# Then run bulk_summarize.py
# After processing, uncheck the temporarily checked ones if needed
```

**Note**: This is more complex and usually not needed. Prefer Option 1 or Option 2.

## Progress Tracking

For batch operations:

1. Create TodoWrite entry before starting: "Batch summarize unchecked sources"
2. Let the script run (it provides its own progress output)
3. Monitor output for any failures
4. Mark todo as completed when script finishes
5. Report: "Generated X summaries, Y failed (if any)"

## Summary File Naming Convention

Summaries are saved to `workdesk/summaries/` with this pattern:

```
XXX_domain_name.json  (JSON format - default)
XXX_domain_name.md    (Markdown format - legacy)
```

Where:
- `XXX` = 3-digit ID (001, 002, 089, etc.)
- `domain_name` = simplified domain (example_com, github_com, etc.)
- Extension = `.json` or `.md` based on format

Examples:
- `089_example_com.json` (structured JSON with scores and topics)
- `090_github_com.json` (JSON format)
- `091_qiita_com.md` (markdown format, if explicitly requested)

## What This Skill Does

- ✅ Generates structured JSON summaries for URLs (default)
- ✅ Validates JSON against v1.0 schema (scores, topics, metadata)
- ✅ Generates Japanese summaries using Gemini AI
- ✅ Marks URLs as checked/processed after successful summary
- ✅ Handles batch processing efficiently with context caching
- ✅ Reports progress and errors
- ✅ Creates summary files in workdesk/summaries/ (.json or .md)
- ✅ Supports both JSON (structured) and markdown (legacy) formats

## What This Skill Does NOT Do

- ❌ Does NOT add new URLs to sources.md (use `add-url` skill)
- ❌ Does NOT validate or check for duplicates (done by `add-url`)
- ❌ Does NOT modify the URL itself

## Key Responsibilities

1. **Summary Generation**: Call Gemini AI to generate high-quality Japanese summaries
2. **File Management**: Save summaries to correct location with proper naming
3. **Status Updates**: Mark URLs as checked after successful summary
4. **Error Handling**: Report failures, continue with remaining URLs
5. **Efficiency**: Use batch processing and context caching when possible

## Project Standards

- Summaries MUST be in Japanese (as per EDITOR_PERSONALITY.md)
- Use absolute paths when referencing files
- Summary filenames: lowercase, underscores, descriptive
- Always verify summary file was created before marking as checked
- Documentation in English, summaries in Japanese

## File Locations

- **Sources list**: `workdesk/sources.md`
- **Summaries**: `workdesk/summaries/XXX_filename.json` (or `.md` for legacy)
- **JSON schema**: `schema/summary-v1-schema.json`
- **Batch script**: `scripts/bulk_summarize.py`
- **Single script**: `scripts/call-gemini.py`
- **Validation script**: `scripts/validate_summaries.py`
- **JSON prompt**: `prompts/summarize-json.prompt`
- **Markdown prompt**: `prompts/summarize.prompt`
- **Workflow docs**: `workflow/STEP_02_GENERATE_SUMMARIES.md`

## JSON Validation

When using JSON format (default), summaries are automatically validated against the v1.0 schema:

**Validation checks**:
- ✓ Required fields present (title, url, scores, topics, etc.)
- ✓ Version = "1.0"
- ✓ Dimension scores in range 0-5 (signal, depth, uniqueness, practical, antiHype)
- ✓ Composite scores in range 0-100 (mainJournal, annexPotential, overall)
- ✓ Topics array has 1-5 elements
- ✓ String length constraints (title: 1-200, summaryBody: 100-1200, etc.)

**If validation fails**: Script exits with error message, URL remains unchecked, no file written.

### Manual Validation

To validate existing JSON summaries:

```bash
# Validate all summaries in workdesk
uv run scripts/validate_summaries.py workdesk/summaries

# Validate specific file
uv run scripts/validate_summaries.py workdesk/summaries/001_example.json

# Verbose mode (show all files)
uv run scripts/validate_summaries.py workdesk/summaries --verbose

# Quiet mode (only summary)
uv run scripts/validate_summaries.py workdesk/summaries --quiet
```

**Use cases**:
- Verify summaries after batch generation
- Check integrity before committing
- Validate after manual edits
- CI/CD pipeline integration

## Error Handling

- If summary generation fails, report the error but continue with remaining URLs
- If network timeout occurs, retry once or skip and report
- If file write fails, report and continue
- Never mark a URL as checked if summary generation failed
- Always provide a final summary of successes and failures

## Examples

### Example 1: Batch Process All Unchecked (JSON Format)

**User says**: "Generate summaries for all unchecked sources"

**Skill activates and**:
1. ✓ Runs `uv run scripts/bulk_summarize.py` (defaults to JSON format)
2. ✓ Script finds 15 unchecked URLs
3. ✓ Generates 15 JSON summaries with validation (progress shown)
4. ✓ All 15 summaries pass schema validation
5. ✓ Marks all 15 as checked
6. ✓ Reports: "Generated 15 JSON summaries successfully"

### Example 2: Single URL with JSON

**User says**: "Generate summary for ID 089"

**Skill activates and**:
1. ✓ Finds URL in sources.md for ID 089
2. ✓ Runs call-gemini.py with --format json
3. ✓ Validates JSON structure against v1.0 schema
4. ✓ Saves summary to workdesk/summaries/089_example_com.json
5. ✓ Marks ID 089 as checked in sources.md
6. ✓ Reports: "Generated JSON summary for ID 089"

### Example 3: After Using add-url Skill

**Workflow**:
1. User adds 5 URLs with `add-url` skill → IDs 089-093 (unchecked)
2. User says "now summarize them"
3. `summarize-source` skill activates
4. Runs bulk_summarize.py → generates 5 JSON summaries
5. All 5 summaries validated and saved as .json files
6. All 5 IDs now checked in sources.md

## Performance Notes

- **Context caching**: Automatically enabled in bulk_summarize.py for faster processing
- **Rate limits**: Gemini API has rate limits; bulk_summarize.py handles this
- **Timeout**: Default 120 seconds per URL; adjustable in scripts
- **Retries**: Scripts have built-in retry logic for transient failures

## Troubleshooting

**Issue**: Summary generation times out
**Solution**: Increase timeout in call-gemini.py or retry manually

**Issue**: Some summaries failed in batch
**Solution**: Re-run bulk_summarize.py (it will skip already-checked URLs)

**Issue**: Summary file created but not marked as checked
**Solution**: Manually mark as checked using Edit tool

**Issue**: JSON validation fails
**Solution**:
1. Check error message for specific validation failure
2. Common issues: score out of range, topics array wrong size, missing required field
3. Re-run generation - Gemini will try again with schema enforcement

**Issue**: Want to re-generate a summary
**Solution**:
1. Uncheck the URL in sources.md
2. Delete the old summary file (.json or .md)
3. Run bulk_summarize.py or call-gemini.py

**Issue**: Need markdown format instead of JSON
**Solution**: Use `--format markdown` flag explicitly

## Relationship to Other Skills

- **Before summarize-source**: Use `add-url` skill to add URLs
- **After summarize-source**: Proceed to STEP_03 (curate main journal)

You are efficient and thorough, ensuring all unchecked sources are summarized and marked as processed. You monitor for errors and provide clear progress updates.
