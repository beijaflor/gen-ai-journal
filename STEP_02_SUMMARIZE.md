# Step 2: Summarization (Legacy - Now Integrated into Step 1)

**Note: As of the current workflow, summarization is now integrated into STEP_01_GATHER_SOURCES.md. This document is maintained for reference and special cases.**

## Overview

Summarization is now a manual process after checking links with `check_link.py`. This step documents how to generate summaries for your links when the automated process in Step 1 needs manual intervention.

## How to Generate Summaries

After checking a link with `check_link.py` and adding it to `sources.md`:

1. **Use the One-Shot Script**:
   ```bash
   uv run scripts/call-gemini.py --url "https://example.com/article" --output workdesk/summaries/001_example_com_article.md
   ```

2. **How It Works**:
   - Uses the @prompts/summarize.prompt template
   - Calls Gemini API to generate the summary
   - Outputs the summary to stdout (redirect to save)

3. **Update Progress** - Mark the link as processed in `workdesk/sources.md`

## Manual Summarization (If Needed)

If you need to re-summarize a link or summarize without the full workflow:

```bash
uv run scripts/call-gemini.py --url "https://example.com/article" --output workdesk/summaries/001_example_com_article.md
```

## Batch Processing Multiple Links

If you have multiple links in `workdesk/sources.md` that need summarization:

### Option 1: Process One by One
```bash
# For each unchecked link in sources.md
uv run scripts/call-gemini.py --url "https://example.com/article" --output workdesk/summaries/001_example_com_article.md
```

### Option 2: Use Batch Process
For batch processing multiple links, repeat Option 1 for each link, or use the main workflow in STEP_01_GATHER_SOURCES.md.

## Creating Unified Summaries

After adding all your links, create a unified summary file for easier review:

```bash
# Combine all summaries into one file
uv run scripts/unite_summaries.py workdesk/sources.md workdesk/summaries workdesk/unified_summaries.md
```

## Summary Quality Control

Check your summaries for:
- **Completeness** - Each summary should capture key points
- **Language** - Summaries should be in Japanese (as per editorial guidelines)
- **Structure** - Title, source URL, and main content should be present
- **Relevance** - Summary should relate to GenAI/coding topics

## Troubleshooting

### If Summarization Fails
1. Check internet connectivity
2. Verify Gemini CLI is configured: `gemini --help`
3. Check if the URL is accessible
4. Review error messages in the console

### Re-summarizing a Link
1. Delete the existing summary file
2. Run the summarize script again:
   ```bash
   uv run scripts/call-gemini.py --url "https://example.com/article" --output workdesk/summaries/001_example_com_article.md
   ```

## Next Steps

Once all links are added and summarized:
- Review `workdesk/unified_summaries.md` for overview
- Continue to [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md)