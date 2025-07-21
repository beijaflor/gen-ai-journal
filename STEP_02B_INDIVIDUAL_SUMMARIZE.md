# Step 2B: Individual Summarization Process

This step details the process for summarizing a single source URL. This is typically called repeatedly by the orchestration process.

## Prerequisites

- Target URL identified from `workdesk/sources.md`
- `workdesk/summaries/` directory exists
- Gemini CLI configured and available

## Individual Summarization Steps

### Option 1: Using the Shell Script (Recommended)

Use the provided shell script for one-shot summarization:

```bash
./scripts/summarize-url.sh "https://example.com/article"
```

The script outputs the summary to stdout, which can be captured and processed.

### Option 2: Manual Process

#### 1. Generate Prompt File

Replace `YOUR_ARTICLE_URL_HERE` with the target URL:

```bash
sed 's|%%URL%%|YOUR_ARTICLE_URL_HERE|g; s|%%FILENAME%%|workdesk/temp_summary.md|g' \
/Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt > \
/Users/shootani/Dropbox/github/gen-ai-journal/workdesk/generated_prompt.txt
```

**Example:**
```bash
# For URL: https://example.com/article
sed 's|%%URL%%|https://example.com/article|g; s|%%FILENAME%%|workdesk/temp_summary.md|g' \
/Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt > \
/Users/shootani/Dropbox/github/gen-ai-journal/workdesk/generated_prompt.txt
```

#### 2. Run Gemini CLI

Execute the summarization with the specified model:

```bash
cat workdesk/generated_prompt.txt | gemini -m "gemini-2.5-flash" --sandbox
```

### Option 3: One-Line Command

For a single command without intermediate files:

```bash
sed "s|%%URL%%|YOUR_URL_HERE|g" /Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt | \
gemini -m "gemini-2.5-flash" --sandbox
```

**Important Notes:**
- Use `gemini-2.5-flash` model (not `gemini-2.5-flash-lite-preview-06-17` which has thinking config issues)
- This process takes time (several minutes per URL)
- Wait for completion before proceeding
- If it fails with no summary, retry the command
- Capture the stdout output for saving

### 3. Save Summary

- **Capture Output:** Save the stdout from the Gemini command (or use Claude to parse if using the shell script)
- **Validate Content:** Check that the output is not empty and contains meaningful content
- **Generate Filename:** Create filename with link number prefix and sanitized URL
- **Save Location:** `workdesk/summaries/[number]_[sanitized_filename].md`

**Filename Convention:**
- Start with 3-digit link number from sources.md (001, 002, etc.)
- Add underscore separator
- Replace special characters with underscores
- Use domain and path components
- Ensure `.md` extension
- Example: `001. https://example.com/article/title` → `001_example_com_article_title.md`
- Example: `042. https://qiita.com/user/items/abc123` → `042_qiita_com_user_items_abc123.md`

### 4. Mark Complete

Update the corresponding line in `workdesk/sources.md`:
- **Success:** Change from `- [ ] 001. https://example.com/article` to `- [x] 001. https://example.com/article`
- **Failure:** Change from `- [ ] 001. https://example.com/article` to `- [!] 001. https://example.com/article`

## Error Handling

### Common Issues:
- **Network timeouts:** Retry after delay
- **Empty summaries:** Retry with same URL, do not mark as complete if summary is empty
- **Rate limiting:** Wait and retry
- **Bot protection/Paywalls:** Mark with `[!]` after retry attempts fail
- **Invalid URLs:** Mark with `[!]`, skip
- **Empty output files:** Do not save empty files; retry summarization

### Retry Logic:
- Maximum 3 retry attempts per URL
- Exponential backoff (30s, 60s, 120s)
- After all retries fail: Mark with `[!]` in sources.md
- Log failures for manual review

## Output for Single URL

- **File Created:** `workdesk/summaries/[sanitized_filename].md` (on success only)
- **File Updated:** `workdesk/sources.md` (checkbox marked `[x]` for success, `[!]` for failure)
- **Status:** Ready for next URL or aggregation

## Integration

This process is typically called by:
- Orchestration scripts for batch processing
- Manual execution for individual URLs
- Retry mechanisms for failed summarizations
- Claude Code when using `./scripts/summarize-url.sh` for automated parsing and saving