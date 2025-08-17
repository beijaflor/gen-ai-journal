# GenAI Coding Journal

A weekly curated journal of AI and coding developments, featuring high-impact articles in the main journal and unique perspectives in the annex journal.

## Workflow Overview

This project follows a systematic workflow to create weekly journals using branch-based development:

```mermaid
graph LR
    A[00. Create Branch] --> B[01. Add Links]
    B --> C[02. Summarization]
    C --> D[03. Prepare Working Files]
    D --> E[04. Curate Main Journal]
    E --> F[05. Curate Annex Journal]
    F --> G[06. Create Focused Summaries]
    G --> H[07. Review & Refine]
    H --> I[08. Assemble Final Journals]
    I --> J[09. Verify URLs & Quality]
    J --> K[10. Archive & Cleanup]
    K --> L[11. Create Pull Request]
    L --> M[12. Tag & Publish]
```

## Workflow Steps

00. **[Create Branch](STEP_00_CREATE_BRANCH.md)** - Create dedicated branch for journal week
01. **[Add Links Individually](STEP_01_GATHER_SOURCES.md)** - Add and process links one by one with automatic summarization
02. **[Summarization](STEP_02_SUMMARIZE.md)** - Now integrated into link addition (documentation for special cases)
03. **[Prepare Working Files](STEP_03_PREPARE_JOURNAL.md)** - Set up journal templates and workspace
04. **[Curate Main Journal](STEP_04_CURATE_MAIN.md)** - Select 18-25 primary articles based on editorial criteria
05. **[Curate Annex Journal](STEP_05_CURATE_ANNEX.md)** - Select "B-side" articles with unique perspectives
06. **[Create Focused Summaries](STEP_06_CREATE_FOCUSED_SUMMARIES.md)** - Generate unified summaries for each journal
07. **[Review & Refine](STEP_07_REVIEW.md)** - Edit and polish selected summaries with editorial voice
08. **[Assemble Final Journals](STEP_08_ASSEMBLE.md)** - Create publication-ready main and annex journals
09. **[Verify URLs & Quality](STEP_09_VERIFY.md)** - Quality control, URL verification, and final checks
10. **[Archive & Cleanup](STEP_10_CLEANUP.md)** - Archive to journals/ directory and clean workspace
11. **[Create Pull Request](STEP_11_PULL_REQUEST.md)** - Create PR for completed journal (human handles merge)
12. **[Tag & Publish](STEP_12_TAG_PUBLISH.md)** - Tag release and publish journal after merge

## Quick Start

### Checking Links Before Adding
```bash
# Check if a link is valid and unique before adding
python3 scripts/check_link.py "https://example.com/article-about-ai"

# The script will:
# 1. Sanitize the URL (remove tracking params)
# 2. Check for duplicates in sources and summaries
# 3. Report if the URL is ready to be added
```

### Syncing to GitHub Issues
```
# Simply ask Claude Code to sync sources to GitHub issue
"Sync workdesk/sources.md to GitHub issue"

# Claude Code will automatically:
# - Analyze current sources and progress
# - Create or update weekly GitHub issue
# - Apply appropriate labels and formatting
```

### Prerequisites
- [ ] Python 3.x installed
- [ ] Gemini CLI configured (`gemini` command available)
- [ ] Git repository initialized
- [ ] `prompt.txt` file present in project root
- [ ] Claude Code with MCP GitHub integration (for automated issue sync)

## Key Files

### Curation Criteria
- **[Main Journal Criteria](criteria/curation_criteria.md)** - Selection standards for primary journal
- **[Annex Journal Criteria](criteria/annex_curation_criteria.md)** - Selection standards for annex journal

### Scripts
- `scripts/check_link.py` - Check if a URL is valid and unique before adding
- `process_sources.py` - Sanitizes URLs (removes UTM parameters, duplicates) and assigns numbered IDs
- `scripts/unite_summaries.py` - Gathers summaries from a list of URLs
- `scripts/call-gemini.py` - One-shot URL summarization using Gemini (supports --output for file output)
- `scripts/list_urls.py` - Extract URLs from markdown files
- `scripts/remove_urls.py` - Remove specific URLs from files (used with list_urls.py for workflow management)

### Output Structure
```
journals/
└── YYYY-MM-DD/
    ├── 00_weekly_journal_YYYY_MM_DD.md # Main journal
    ├── 01_annex_journal_YYYY_MM_DD.md  # Annex journal
    ├── 02_omitted_summaries.md         # Summaries of omitted articles
    ├── 99_unified_summaries.md         # All unified summaries (complete reference)
    ├── sources/
    │   ├── sources.md                   # Original source list with all URLs
    │   ├── curated_journal_sources.md  # Main journal selected URLs
    │   ├── curated_annex_journal_sources.md # Annex journal selected URLs
    │   └── omitted_sources.md          # Sources truly omitted from both journals
    └── summaries/
        └── [individual summary files]   # All individual AI-generated summaries
```

