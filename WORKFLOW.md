# Journal Creation Workflow

1.  **Step 1: Prepare Initial Source List**
    - See `WORKFLOW_STEP1.md`.
    - **Result:** `workdesk/sources.md` is created with the initial list of URLs.

2.  **Step 1.5: Curate Sources & Prepare Journal Directory**
    - See `WORKFLOW_STEP1.5.md`.
    - **Result:**
        - A `journals/YYYY-MM-DD/` directory is created.
        - Curated source lists are created within it: `curated_journal_sources.md`, `curated_annex_journal_sources.md`, and `omitted_sources.md`.
        - Empty journal files are created: `weekly_journal_YYYY_MM_DD.md` and `annex_journal_YYYY_MM_DD.md`.
        - `workdesk/sources.md` is now empty.

3.  **Step 2: Summarize All Curated Sources**
    - See `SUMMARIZE_STEP.md`. This step uses the curated source lists from the `journals/YYYY-MM-DD/` directory.
    - **Result:**
        - Individual summaries are created in `journals/YYYY-MM-DD/summaries/`.
        - A unified summary file (e.g., `z_unified_summaries.md`) is created in the same directory for review.

4.  **Step 3: Review and Refine Summaries**
    - Review the aggregated content in the unified summary file (e.g., `z_unified_summaries.md`).
    - Make final edits to the summaries directly in this file.

5.  **Step 4: Assemble Final Journals**
    - Use the refined content from the unified summary file to write the introductory sections and structure the final content within `weekly_journal_YYYY_MM_DD.md` and `annex_journal_YYYY_MM_DD.md`.

6.  **Step 5: Final Cleanup**
    - Clean up any remaining temporary files from the `workdesk/` directory. All final artifacts are already in their correct `journals/YYYY-MM-DD/` location.
