# Summarization Orchestration Workflow

This document outlines the process for orchestrating the summarization of all sources.

1.  **Setup**:
    - Ensure `workdesk/sources.md` exists.
    - Create the `workdesk/summaries/` directory if it doesn't exist.

2.  **Execution**: A script will iterate through each unchecked URL in `workdesk/sources.md`. For each URL, it will:
    a. Execute the individual link summarization process detailed in `INDIVIDUAL_SUMMARIZE_STEP.md`.
    b. Save the final summary to a corresponding file in the `workdesk/summaries/` directory.
    c. Mark the URL as complete (`[x]`) in `workdesk/sources.md`.

3.  **Aggregation**: After all sources are processed, a separate action will aggregate all individual summaries from `workdesk/summaries/` into `workdesk/temp_journal_sources.md` for final review.
