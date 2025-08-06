# Project Overview

This repository creates weekly curated journals about Generative AI in coding, following a systematic 8-step workflow.

# Editorial Guidelines

## Language Requirements
- **Journal content**: ALWAYS write in Japanese
- **Documentation/prompts**: Write in English
- **Editorial voice**: @EDITOR_PERSONALITY.md - read and adopt this persona when editing journal content

## File Organization
- Journal entries: `journals/YYYY-MM-DD/` directory structure
- Workflow steps: `STEP_01_*.md` through `STEP_08_*.md` files
- Curation criteria: `criteria/` directory

# Code Style & Tools

## File Formatting
- Use standard Markdown for all content
- Use 2-space indentation for nested lists
- Follow consistent heading hierarchy (# ## ###)

## Scripts & Commands
- Use `uv run` for processing scripts
- Key scripts: `process_sources.py`, `scripts/unite_summaries.py`
- Always use absolute paths when referencing files

## Frequently Used Commands
```bash
# Create journal directory structure
mkdir -p journals/YYYY-MM-DD/{sources,summaries}

# Process and sanitize source URLs
uv run process_sources.py workdesk/sources.md

# One-shot URL summarization
uv run scripts/call-gemini.py --url "https://example.com/article" --output summary.md

# Aggregate summaries
uv run scripts/unite_summaries.py workdesk/sources.md workdesk/summaries workdesk/unified_summaries.md

# Generate non-main sources after main journal curation (STEP_04)
uv run scripts/list_urls.py workdesk/curated_journal_sources.md | uv run scripts/remove_urls.py workdesk/sources.md workdesk/non_main_sources.md

# Generate unified summaries for non-main sources (STEP_05)
uv run scripts/unite_summaries.py workdesk/non_main_sources.md workdesk/summaries workdesk/non_main_unified_summaries.md

# Search for URL in markdown files
grep -l "YOUR_URL_HERE" **/*.md

# Sanitize URL (remove tracking params and fragments)
uv run scripts/sanitize_url.py "URL_HERE"
```

# Workflow Management

## Step Execution
- Follow workflow steps sequentially: STEP_01 → STEP_08
- Update TodoWrite frequently to track progress
- Mark steps complete only when fully finished

## File Updates
- When updating workflow: modify README.md workflow section AND relevant STEP_XX files
- Keep documentation synchronized across all related files
- Use Edit tool for existing files, Write tool only for new files

## Quality Standards
- Verify all links work before finalizing journals
- Ensure consistent editorial voice throughout
- Maintain separation between main journal (essential) and annex journal (unique insights)