# Journal Creation Workflow

1.  **Start from a GitHub Issue:** Identify the relevant GitHub issue containing the list of source URLs for the weekly journal.

2.  **Create a Temporary Working File:** Create a temporary markdown file (e.g., `temp_journal_sources.md`) to aggregate the summaries.

3.  **Process Each Source URL:** For each URL from the issue:
    a. Fetch the content of the URL.
    b. Generate a summary in Japanese, adhering to the persona defined in `EDITOR_PERSONALITY.md`.
    c. Structure the summary using the following template:

        ```markdown
        ## [Article Title](URL)

        **Catchy Headline in Japanese**

        (Summary Body in Japanese)

        **注目すべき理由 (Why it matters):**

        (Explanation of why the topic is important for developers, in Japanese)
        ```
    d. Append the formatted summary to the temporary working file.

4.  **Review and Refine:** Once all sources are summarized, review the collected content for consistency and quality.

5.  **Define the Journal Title:** Based on the collected content, decide on a final title for the journal entry.

6.  **Create the Final Journal File:** Create the final journal markdown file in the `journals/` directory with the format `YYYY-MM-DD-journal-title.md`.

7.  **Cleanup:** Delete the temporary working file.
