# Step 2: Summarization

## Overview

Summarization is now a manual process after checking links with `check_link.py`. This step documents how to generate summaries for your links.

## How to Generate Summaries

After checking a link with `check_link.py` and adding it to `sources.md`:

1. **Use the One-Shot Script**:
   ```bash
   ./scripts/summarize-url.sh "https://example.com/article" > workdesk/summaries/001_example_com_article.md
   ```

2. **How It Works**:
   - Reads `prompt.txt` and replaces `%%URL%%` with your URL
   - Calls `gemini -m "gemini-2.5-flash"` to generate the summary
   - Outputs the summary to stdout (redirect to save)

3. **Update Progress** - Mark the link as processed in `workdesk/sources.md`

## Manual Summarization (If Needed)

If you need to re-summarize a link or summarize without the full workflow:

```bash
./scripts/summarize-url.sh "https://example.com/article" > workdesk/summaries/001_example_com_article.md
```

## Batch Processing Multiple Links

If you have multiple links in `workdesk/sources.md` that need summarization:

### Option 1: Process One by One
```bash
# For each unchecked link in sources.md
./scripts/summarize-url.sh "https://example.com/article" > workdesk/summaries/001_example_com_article.md
```

### Option 2: Use Batch Process
Follow the batch processing workflow in:
- [STEP_02A_ORCHESTRATION.md](STEP_02A_ORCHESTRATION.md) - For orchestrating batch summaries
- [STEP_02B_INDIVIDUAL_SUMMARIZE.md](STEP_02B_INDIVIDUAL_SUMMARIZE.md) - For individual processing

## Creating Unified Summaries

After adding all your links, create a unified summary file for easier review:

```bash
# Combine all summaries into one file
awk 'FNR==1 && NR!=1 {print "\n\n---\n\n"} 1' workdesk/summaries/*.md > workdesk/unified_summaries.md
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
   ./scripts/summarize-url.sh "https://example.com/article" > workdesk/summaries/001_example_com_article.md
   ```

## Next Steps

Once all links are added and summarized:
- Review `workdesk/unified_summaries.md` for overview
- Continue to [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md)