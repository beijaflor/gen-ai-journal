# Step 2: Summarize All Sources

This step generates summaries for ALL sources before curation, allowing informed selection decisions.

## Overview

This step has been split into two complementary processes:

### 1. Orchestration Process
**File:** [STEP_02A_ORCHESTRATION.md](STEP_02A_ORCHESTRATION.md)

Manages the overall batch summarization process:
- Setup and directory preparation
- Batch processing coordination
- Progress tracking and quality control
- Aggregation of all summaries
- Final output generation

### 2. Individual Summarization Process
**File:** [STEP_02B_INDIVIDUAL_SUMMARIZE.md](STEP_02B_INDIVIDUAL_SUMMARIZE.md)

Details the process for summarizing a single URL:
- Prompt generation for specific URLs
- Gemini CLI execution with `gemini-2.5-flash` model
- Summary file creation with `[number]_[sanitized_url].md` naming convention
- Progress marking
- Error handling and retry logic

## Workflow

1. **Start with Orchestration:** Follow [STEP_02A_ORCHESTRATION.md](STEP_02A_ORCHESTRATION.md) to set up and manage the overall process
2. **Individual Processing:** The orchestration process calls [STEP_02B_INDIVIDUAL_SUMMARIZE.md](STEP_02B_INDIVIDUAL_SUMMARIZE.md) for each URL
3. **Completion:** Return to orchestration for final aggregation and output

## Output

- **Directory Created:** `workdesk/summaries/` containing individual summary files with `[number]_[sanitized_url].md` naming
- **File Created:** `workdesk/unified_summaries.md` (aggregated summaries)
- **File Updated:** `workdesk/sources.md` (with `[x]` for successful summaries, `[!]` for failed URLs)
- **Next Step:** [STEP_03_PREPARE_JOURNAL.md](STEP_03_PREPARE_JOURNAL.md)

## Key Updates

- **Model:** Use `gemini-2.5-flash` (not `gemini-2.5-flash-lite-preview-06-17`)
- **Naming:** Summary files now include link numbers: `001_domain_com_article.md`