# GenAI Coding Journal

A weekly curated journal of AI and coding developments, featuring high-impact articles in the main journal and unique perspectives in the annex journal.

## Workflow Overview

This project follows a systematic workflow to create weekly journals:

```mermaid
graph LR
    A[1. Gather Sources] --> B[2. Summarize ALL]
    B --> C[3. Prepare Journal]
    C --> D[4. Curate Main]
    D --> E[5. Curate Annex]
    E --> F[5B. Create Focused Summaries]
    F --> G[6. Review]
    G --> H[7. Assemble]
    H --> I[8. Cleanup]
```

## Workflow Steps

1. **[Gather Sources](STEP_01_GATHER_SOURCES.md)** - Collect URLs from structured GitHub issue with numbered IDs
2. **[Summarize](STEP_02_SUMMARIZE.md)** - Generate summaries for ALL sources
3. **[Prepare Journal](STEP_03_PREPARE_JOURNAL.md)** - Set up working files in workdesk
4. **[Curate Main Journal](STEP_04_CURATE_MAIN.md)** - Select primary articles using summaries
5. **[Curate Annex Journal](STEP_05_CURATE_ANNEX.md)** - Select "B-side" articles from omitted sources
5B. **[Create Focused Summaries](STEP_05B_CREATE_FOCUSED_SUMMARIES.md)** - Generate separate unified summaries for each journal
6. **[Review Summaries](STEP_06_REVIEW.md)** - Edit and refine selected summaries
7. **[Assemble Journals](STEP_07_ASSEMBLE.md)** - Create final journal documents
8. **[Cleanup](STEP_08_CLEANUP.md)** - Archive to journals/ directory and clean workspace

## Quick Start Checklist

- [ ] GitHub issue with structured source URLs identified (Main List, Slides, Might Be Hype, Better to be Omitted)
- [ ] Python environment ready (for `process_sources.py`)
- [ ] Gemini CLI configured (`gemini` command available)
- [ ] Git repository up to date

## Key Files

### Curation Criteria
- **[Main Journal Criteria](criteria/curation_criteria.md)** - Selection standards for primary journal
- **[Annex Journal Criteria](criteria/annex_curation_criteria.md)** - Selection standards for annex journal

### Scripts
- `process_sources.py` - Sanitizes URLs (removes UTM parameters, duplicates) and assigns numbered IDs
- `scripts/unite_summaries.py` - Gathers summaries from a list of URLs

### Output Structure
```
journals/
└── YYYY-MM-DD/
    ├── weekly_journal_YYYY_MM_DD.md    # Main journal
    ├── annex_journal_YYYY_MM_DD.md     # Annex journal
    ├── sources/
    │   ├── curated_journal_sources.md
    │   ├── curated_annex_journal_sources.md
    │   └── omitted_sources.md
    └── summaries/
        └── [individual summary files]
```

