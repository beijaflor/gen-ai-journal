# Step 2A: Orchestration - Manage Summarization Process

This step orchestrates the batch summarization of all sources, managing the overall process and aggregation.

## Setup

- [ ] Ensure `workdesk/sources.md` exists with sanitized URLs
- [ ] Create the `workdesk/summaries/` directory if it doesn't exist:
  ```bash
  mkdir -p workdesk/summaries
  ```

## Orchestration Process

### 1. Batch Processing

A script typically orchestrates this process, iterating through all unchecked URLs automatically. The script should:

- Read all unchecked URLs from `workdesk/sources.md`
- For each URL, follow the individual summarization process (see [STEP_02B_INDIVIDUAL_SUMMARIZE.md](STEP_02B_INDIVIDUAL_SUMMARIZE.md))
- Use `gemini-2.5-flash` model for summarization
- Generate summary files with naming convention: `[number]_[sanitized_url].md`
- Track progress by updating checkboxes in `workdesk/sources.md` (`[x]` for success, `[!]` for failure)
- Handle failures gracefully with retry logic

### 2. Progress Tracking

- [ ] Monitor completion status in `workdesk/sources.md`
- [ ] Verify that each successful URL (`[x]`) has a corresponding summary file in `workdesk/summaries/`
- [ ] Check for any failed summarizations (`[!]`) that need retry
- [ ] Ensure failed URLs are properly marked with `[!]` after retry attempts

### 3. Quality Control

- [ ] Verify all summary files are non-empty (minimum 100 characters of content)
- [ ] Check that summary filenames match the expected format: `[number]_[sanitized_url].md`
- [ ] Ensure link numbers correspond to sources.md entries
- [ ] Validate that summaries contain expected format (Japanese content, proper structure)
- [ ] Remove any empty files and mark corresponding entries with `[!]` in `workdesk/sources.md`
- [ ] Ensure all checkboxes in `workdesk/sources.md` are marked: `[x]` for valid summaries, `[!]` for failures

## Aggregation

After all sources are processed:

- [ ] Aggregate all summaries into a unified file:
  ```bash
  awk 'FNR==1 && NR!=1 {print "\n\n---\n\n"} 1' workdesk/summaries/*.md > workdesk/unified_summaries.md
  ```

## Output

- **Directory Populated:** `workdesk/summaries/` containing individual summary files
- **File Created:** `workdesk/unified_summaries.md` (aggregated summaries)
- **File Updated:** `workdesk/sources.md` (with completed checkboxes)
- **Next Step:** [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md)

## Automation Notes

- Process takes significant time (several minutes per URL)
- Consider running in batches to manage resources
- Monitor for rate limiting or API failures
- Maintain backup of intermediate results