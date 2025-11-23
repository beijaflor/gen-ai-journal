# Step 11: Generate Journal Metadata

This step creates the mandatory `journal-metadata.json` file containing summary statistics for the journal. This file is **required** for the website to build correctly.

### Process

1. **Navigate to journal directory**
   ```bash
   cd journals/YYYY-MM-DD/
   ```

2. **Count summary statistics**
   - Count total summaries: 
     - New structure: `ls -1 summaries/*.md | wc -l`
     - Old structure: `ls -1 sources/*.md | grep -v "sources.md" | wc -l`
   - Count main journal URLs: `grep -c "https://" sources/curated_journal_sources.md` 
   - Count annex journal URLs: `grep -c "https://" sources/curated_annex_journal_sources.md`
   - Calculate omitted: total - main - annex

3. **Create metadata file**
   Create `journal-metadata.json` in the journal root directory:
   ```json
   {
     "date": "YYYY-MM-DD",
     "totalSummaries": TOTAL_COUNT,
     "statistics": {
       "mainSummaries": MAIN_COUNT,
       "annexSummaries": ANNEX_COUNT,
       "omittedSummaries": OMITTED_COUNT
     }
   }
   ```

### Example

For journal `2025-08-23`:
- Total summaries: 208
- Main journal URLs: 21  
- Annex journal URLs: 18
- Omitted summaries: 169

```json
{
  "date": "2025-08-23",
  "totalSummaries": 208,
  "statistics": {
    "mainSummaries": 21,
    "annexSummaries": 18,
    "omittedSummaries": 169
  }
}
```

### Validation

1. **JSON syntax**: Validate the JSON is properly formatted
2. **Math check**: Ensure mainSummaries + annexSummaries + omittedSummaries = totalSummaries
3. **File location**: Place file in journal root directory (same level as journal .md files)

### Automated Script (Optional)

```bash
#!/bin/bash
# Generate metadata for current directory

# Determine which directory structure is used and count summaries
if [ -d "summaries" ]; then
  # New structure: count all .md files in summaries/
  TOTAL=$(ls -1 summaries/*.md 2>/dev/null | wc -l)
elif [ -d "sources" ]; then
  # Old structure: count all .md files in sources/ excluding sources.md files
  TOTAL=$(ls -1 sources/*.md 2>/dev/null | grep -v "sources.md" | wc -l)
else
  echo "Error: Neither summaries/ nor sources/ directory found"
  exit 1
fi

MAIN=$(grep -c "https://" sources/curated_journal_sources.md 2>/dev/null || echo 0)
ANNEX=$(grep -c "https://" sources/curated_annex_journal_sources.md 2>/dev/null || echo 0)
OMITTED=$((TOTAL - MAIN - ANNEX))
DATE=$(basename $(pwd))

cat > journal-metadata.json << EOF
{
  "date": "$DATE",
  "totalSummaries": $TOTAL,
  "statistics": {
    "mainSummaries": $MAIN,
    "annexSummaries": $ANNEX,
    "omittedSummaries": $OMITTED
  }
}
EOF

echo "Generated metadata: Total=$TOTAL, Main=$MAIN, Annex=$ANNEX, Omitted=$OMITTED"
```

### Integration

- **When to run**: After STEP_10 (archive & cleanup) and before creating pull request
- **Requirement**: This file is mandatory - the website will not build without it
- **Workflow**: Generate metadata before pull request so it's included in the PR

## Next Step

Proceed to [STEP_12_PULL_REQUEST.md](STEP_12_PULL_REQUEST.md) to create the pull request for review.