# Step 5: Curate Annex Journal

This step selects unique, non-obvious articles from the omitted sources for the annex journal - the "B-side" collection.

## Objective

Find articles that provide:
- Advanced tactics and unconventional wisdom
- Substantive critiques and contrarian views
- Niche explorations and deep dives
- Unique perspectives not covered in mainstream sources

## Input Files

- **Source Pool:** `workdesk/omitted_sources.md` (rejected from main)
- **Summaries:** `workdesk/unified_summaries.md` (for review)
- **Criteria:** `criteria/annex_curation_criteria.md`

## Curation Process

### 1. Review Omitted Sources

For each URL in `omitted_sources.md`, reconsider with annex criteria:

- **Originality:** Does it offer a unique perspective or novel knowledge?
- **Practical Value:** Does it provide actionable insights for experienced practitioners?
- **Critical Thinking:** Does it challenge consensus or explore second-order effects?
- **Niche Appeal:** Does it deep-dive into specialized topics?

### 2. Select and Annotate

For articles that meet annex criteria:

- [ ] Add to `workdesk/curated_annex_journal_sources.md`
- [ ] **Include editorial comment** explaining why it's valuable for the annex

Example format:
```markdown
# Curated Annex Journal Sources

- [ ] https://example.com/unconventional-approach
  - 従来のベストプラクティスに挑戦する斬新なアプローチ。実装の複雑さとトレードオフを詳細に解説

- [ ] https://example.com/niche-deep-dive
  - ニッチだが重要な技術領域への深い洞察。メインストリームでは見過ごされがちな視点を提供
```

### 3. Maintain High Standards

The annex is NOT for:
- Leftover content that didn't make the main journal
- Basic tutorials or getting-started guides
- Pure speculation without substance
- Marketing material

It IS for:
- Hidden gems with unique insights
- Advanced techniques for experienced practitioners
- Well-reasoned contrarian viewpoints
- Deep technical explorations

## Output File

Create or update:

- [ ] `workdesk/curated_annex_journal_sources.md`
  - Must include brief Japanese comments explaining each selection
  - Comments should highlight what makes each article annex-worthy

## Verification

- [ ] Each selected article has a clear editorial comment
- [ ] Selected articles offer genuine "B-side" value
- [ ] No overlap with main journal selections

## Next Step

[STEP_05B_CREATE_FOCUSED_SUMMARIES.md](STEP_05B_CREATE_FOCUSED_SUMMARIES.md) - Create focused summary collections for each journal