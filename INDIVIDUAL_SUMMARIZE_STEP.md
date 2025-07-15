# Individual Link Summarization

This document describes the process for summarizing a single source link.

*   **Goal**: Generate a concise, high-quality summary for a given article URL, adhering to the project's editorial standards.
*   **Action**: The summarization is performed by a script that executes a `gemini` CLI command.
*   **Process**:
    1.  A source URL is provided (either selected from `workdesk/sources.md` or directly specified).
    2.  **Generate Prompt File**: Create the prompt file using the following command, replacing `YOUR_ARTICLE_URL_HERE` with the desired URL:
        Example command:
        ```bash
        sed 's|%%URL%%|YOUR_ARTICLE_URL_HERE|g; s|%%FILENAME%%|workdesk/temp_summary.md|g' 
        /Users/shootani/Dropbox/github/gen-ai-journal/prompt.txt > /Users/shootani/Dropbox/github/gen-ai-journal/workdesk/generated_prompt.txt
        ```
    3.  **Run Gemini CLI**: Execute the `gemini` command with model **"gemini-2.5-flash-lite-preview-06-17"** to output the summary to the console. The command will extract only the summary content. It takes time to process. Wait until you get result. If command fail with no summary, try again.
        ```bash
        cat workdesk/generated_prompt.txt | gemini -m "gemini-2.5-flash-lite-preview-06-17" --sandbox
        ```

    4.  **Verify Output**: After running the command, check stdout and save it as summary file. If command return with error, retry.

    5.  The `gemini` sub-process, guided by the prompt, fetches the article, summarizes it in Japanese according to the persona in `EDITOR_PERSONALITY.md`, and saves the result to the specified temporary file.
