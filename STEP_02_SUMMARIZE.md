# Step 2: Summarize All Sources

This step generates summaries for ALL sources before curation, allowing informed selection decisions.

## Setup

- [ ] Ensure `workdesk/sources.md` exists with sanitized URLs
- [ ] Create the `workdesk/summaries/` directory if it doesn't exist:
  ```bash
  mkdir -p workdesk/summaries
  ```

## Process

### For Each URL in `workdesk/sources.md`:

1. **Generate Prompt File**
   
   Replace `YOUR_ARTICLE_URL_HERE` with the target URL:
   ```bash
   sed 's|%%URL%%|YOUR_ARTICLE_URL_HERE|g; s|%%FILENAME%%|workdesk/temp_summary.md|g' \
   /Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt > \
   /Users/shootani/Dropbox/github/gen-ai-journal/workdesk/generated_prompt.txt
   ```

2. **Run Gemini CLI**
   
   Execute the summarization with the specified model:
   ```bash
   cat workdesk/generated_prompt.txt | gemini -m "gemini-2.5-flash-lite-preview-06-17" --sandbox
   ```
   
   **Note:** This process takes time. Wait for completion. If it fails with no summary, retry.

3. **Save Summary**
   
   - Capture the stdout output from the Gemini command
   - Save to `workdesk/summaries/[sanitized_filename].md`
   - Filename should be derived from the URL (e.g., `example_com_article_title.md`)

4. **Mark Complete**
   
   - Update the checkbox in `workdesk/sources.md` from `- [ ]` to `- [x]`

## Automation Note

A script typically orchestrates this process, iterating through all unchecked URLs automatically.

## Aggregation

After all sources are processed:

- [ ] Aggregate all summaries into a unified file:
  ```bash
  awk 'FNR==1 && NR!=1 {print "\n\n---\n\n"} 1' workdesk/summaries/*.md > workdesk/unified_summaries.md
  ```

## Output

- **Directory Created:** `workdesk/summaries/` containing individual summary files
- **File Created:** `workdesk/unified_summaries.md` (aggregated summaries)
- **File Updated:** `workdesk/sources.md` (with completed checkboxes)
- **Next Step:** [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md)