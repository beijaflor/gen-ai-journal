# Step 8: Assemble Final Journals

This step transforms the refined summaries into complete, publication-ready journal documents with proper structure, introductions, and editorial flow.

## Objective

Create publication-ready journals that match the format of published examples (see `journals/2025-12-06/00_weekly_journal_2025_12_06.md` for reference).

## Input Files

- **Editorial Plan with Assembly Strategies:** `workdesk/editorial_plan_YYYY_MM_DD.md`
  - ✅ APPROVED themes and structure (from STEP_03b)
  - 📋 Assembly strategies for each theme (from STEP_07)
    - Pattern selections and rationales
    - Article order and connection points
    - Narrative strategies and writing prompts
- **Pattern Library:** `patterns/assembly/*.md` (reference for assembly strategies)
- **Article Summaries:**
  - `workdesk/unified_summaries_main.md` (18-25 articles)
  - `workdesk/unified_summaries_annex.md` (remaining articles)
- **Source Lists:**
  - `workdesk/curated_journal_sources.md` (theme-organized from STEP_04)
  - `workdesk/curated_annex_journal_sources.md`
- **Empty Templates:**
  - `workdesk/weekly_journal_YYYY_MM_DD.md`
  - `workdesk/annex_journal_YYYY_MM_DD.md`

## Assembly Process Overview

STEP_08 is a **manual editorial process** split into 3 sub-steps:

- **STEP_08a**: Organize content and create thematic structure
- **STEP_08b**: Generate journal draft with editorial content
- **STEP_08c**: Polish and verify completeness

---

## STEP_08a: Review Assembly Strategies & Prepare

**Note:** Theme organization (STEP_03b/STEP_04) and assembly planning (STEP_07) are complete. This step prepares for actual writing by reviewing strategies.

### 1. Read Assembly Strategies from STEP_07

- [ ] Read `workdesk/editorial_plan_YYYY_MM_DD.md` completely, focusing on:
  - **Assembly Strategy sections** for each theme (added in STEP_07)
  - Pattern names and rationales
  - Article order and why
  - Narrative strategies
  - Connection points between articles
  - Writing prompts for assembly

- [ ] Read corresponding pattern definitions from `patterns/assembly/`:
  - For each theme's selected pattern, review pattern guidelines
  - Understand transition strategies for that pattern
  - Review narrative flow recommendations
  - Check example from past journals

- [ ] Read all article summaries
  - [ ] Read `workdesk/unified_summaries_main.md` completely
  - [ ] Read `workdesk/unified_summaries_annex.md` completely
  - Familiarize yourself with article content before assembly

### 2. Verify Assembly Strategies Make Sense

**For Main Journal** (6-7 themes with assembly strategies):

- [ ] Review each theme's assembly strategy in editorial plan:
  - Does the pattern choice still make sense?
  - Is the article order logical?
  - Are connection points clear?
  - Are transition strategies actionable?

- [ ] If adjustments needed:
  - [ ] Document what changed and why
  - [ ] Update assembly strategy in editorial plan
  - [ ] Re-review pattern guidelines if switching patterns

**Note:** Only make changes if articles or understanding has evolved since STEP_07. Assembly strategies should be mostly final.

**For Annex Journal** (target: 5-6 sections):
- [ ] Group articles emphasizing B-side character
- [ ] Create descriptive Japanese section titles
- [ ] Common annex themes:
  - Advanced Tactics & Unconventional Wisdom
  - Substantive Critique & Contrarian Views
  - Niche Explorations & Deep Dives
  - Failed Experiments & Cautionary Tales
  - Security Risks & Technical Debt

### 3. Refine Meta-Commentary

- [ ] Review "今週のハイライト" outline from editorial plan
- [ ] Polish to final form (3-4 paragraphs)
- [ ] Ensure it reflects actual curated articles (not just planned ones)
- [ ] Plan "おわりに" conclusion themes
- [ ] Note cross-cutting insights from editorial plan

---

## STEP_08b: Assemble Journal Following Strategies

### Main Journal Assembly (Theme-by-Theme Following STEP_07 Strategies)

#### 1. Header & Introduction

Create `workdesk/weekly_journal_YYYY_MM_DD.md` with:

```markdown
# GenAI週刊 YYYY年MM月DD日号

今週のAI・コーディング関連の重要な動向をお届けします。

## 今週のハイライト

[Use polished version from editorial_plan_YYYY_MM_DD.md - 3-4 paragraphs covering:
- Week's main narrative arc and themes (from planning document)
- Contradictions or tensions between developments
- Significant shifts in industry thinking
- Why this week matters to developers]

---
```

#### 2. Assemble Each Theme Section

**IMPORTANT:** For each theme, follow the assembly strategy documented in STEP_07.

**Process for each theme:**

1. **Read the theme's assembly strategy** from editorial plan
   - Review pattern name, article order, connection points
   - Read the pattern's guidelines from `patterns/assembly/[pattern-name].md`
   - Understand transition strategies and writing prompts

2. **Assemble theme section** following the strategy:

**For each theme from editorial plan (following assembly strategy):**

```markdown
## [Sequential Number]. [Theme Title from Editorial Plan]

[Optional: Theme introduction paragraph from editorial_plan_YYYY_MM_DD.md
 - Use the 2-3 sentence introduction if it helps readers understand the section
 - Omit if the theme title is self-explanatory and articles speak for themselves]

### [Article Japanese Title]

[Article URL - plain text, not markdown link]

[Clean article summary - 300-600 words in Japanese]
[Include: technical concepts, business context, why it matters]
[Exclude: metadata, scores, content type, language, topics tags]

---

### [Next Article in Same Theme...]
```

**Theme Assembly Guidance:**

- **Article order**: Use the sequence from STEP_07 assembly strategy
  - Order was determined based on pattern guidelines
  - Only reorder if you discover a better flow (document why in comments)

- **Transitions**: Follow the transition strategies from selected pattern
  - **Progressive Sequence**: "Building on this..." / "Taking this further..."
  - **Multi-Perspective**: "From another angle..." / "Contrasting with this..."
  - **Single-Focus**: "In response to this..." / "Analyzing this further..."
  - **Debate-Contrast**: "However, critics argue..." / "On the other hand..."

- **Narrative arc**: Answer the writing prompts from assembly strategy
  - What question does this theme answer?
  - What synthesis emerges from these articles together?
  - What should readers take away?

- **Connection points**: Use the documented connections between articles
  - Explicitly link Article A → Article B where noted
  - Highlight complementary vs. contrasting viewpoints

**Critical transformation rules**:
- **Include**: Theme title from plan, Japanese article title (##見出し from unified summary), URL, polished summary
- **Exclude**: Original Title, Content Type, Language, Scores, Topics tags, metadata
- **Edit**: Refine summary for editorial voice (see EDITOR_PERSONALITY.md) AND pattern narrative flow
- **Format**: Use `---` separator between articles
- **Theme Intro**: Use introduction from editorial plan (refined in STEP_07 if pattern-specific intro needed)

#### 3. Verify Assembly Strategy Execution

After assembling each theme section, verify:

- [ ] **Pattern adherence**: Does the section follow the selected pattern's structure?
- [ ] **Article order**: Are articles in the documented sequence (or changes justified)?
- [ ] **Transitions**: Do transitions use the pattern's recommended strategies?
- [ ] **Writing prompts**: Have the assembly prompts been addressed?
  - Core question answered?
  - Synthesis present?
  - Reader takeaway clear?
- [ ] **Connection points**: Are documented article connections explicit in text?
- [ ] **Narrative flow**: Does the theme section read as coherent narrative (not list)?

**If pattern doesn't feel right during assembly:**
- Note what's not working in editorial notes
- Consider if different pattern would work better
- Update pattern library with insights for future journals

#### 4. Conclusion

```markdown
## おわりに

[Write 2-3 paragraphs reflecting on:
- Week's significance
- Forward-looking perspective
- Connection to ongoing trends
- Call to ongoing learning]

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
```

### Annex Journal Assembly (Catalog Format)

**Philosophy**: The annex journal is a **catalog of unique perspectives**, not comprehensive summaries. Each entry is an ultra-concise 80-120 word narrative that helps readers decide "Should I read this?"

#### 1. Header & Catalog Philosophy

Create `workdesk/annex_journal_YYYY_MM_DD.md` with:

```markdown
# GenAI週刊 Annex YYYY年MM月DD日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事のカタログです。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深堀りを提供する厳選された「B面」コレクションです。

各記事は**カタログ形式**で紹介されています。80-120語の簡潔な要約で、記事の核心と注目すべき視点を統合的に提示します。読むべきかを素早く判断できる構成です。

[Explain this week's B-side character: experimental insights, critical perspectives, niche technical dives]

---
```

#### 2. Catalog Entry Structure

**Format for each article**:

```markdown
### [Japanese Title]
**原題**: [Original English Title] (omit if article is in Japanese or title not translated)
**カテゴリー**: [Category] (OPTIONAL - include only when adds non-obvious context)
**URL**: https://example.com/article

[3-4 sentences integrating: problem/context + key insight + critical takeaway. 80-120 words total. The most compelling point (former 注目ポイント) should be woven naturally into the narrative - either as a powerful closing sentence or integrated throughout. Make the unique/controversial angle prominent.]

---
```

#### 3. Category Taxonomy (8 Core Categories)

Use categories **only when they add non-obvious value** (aim: 30-40% of entries):

1. **ツール・実験** - New/experimental tools, DIY projects, tool comparisons
2. **セキュリティ・リスク** - Vulnerabilities, attack vectors, security practices
3. **批判的分析** - Contrarian views, hype critiques, industry criticism
4. **アーキテクチャ・設計** - System design, trade-offs, technical patterns
5. **パフォーマンス・最適化** - Speed, efficiency, resource management
6. **ビジネス・戦略** - Industry dynamics, investment trends, organizational impact
7. **ニッチ・深堀り** - Specialized topics, edge cases, forgotten histories
8. **教育・学習** - Teaching methods, learning approaches, skill development

**When to include category**:
- Article's topic is non-obvious from title
- Category provides important context (e.g., "セキュリティ・リスク" when security is buried in content)
- Reader would benefit from filtering signal

**When to omit category**:
- Title clearly indicates topic
- URL domain signals content type
- Category would be redundant
- **Default**: When uncertain, omit for cleaner format

#### 4. Catalog Writing Guidelines

**Length Target**: 80-120 words (3-4 sentences)

**Content Structure**:
1. **Opening sentence(s)**: Establish problem/context - "What question does this answer?"
2. **Middle sentence(s)**: Convey key insight - "What's the core finding/argument?"
3. **Closing sentence(s)**: Deliver critical takeaway - "Why does this matter?" / unique angle

**Key Principles**:
- **Ultra-concise**: Every word earns its place
- **Decision-focused**: Answers "Should I read this?" not "What does it say?"
- **Integrated storytelling**: Critical takeaway woven into narrative, not separate
- **Original title transparency**: English articles show 原題 for searchability
- **No filler**: Remove redundant phrases, meta-commentary, editorial notes

**Transformation Rules**:
- **From**: 300+ word comprehensive summary with separate 注目ポイント
- **To**: 80-120 word integrated narrative with compelling angle prominent
- **Exclude**: Editor's notes, meta-commentary, "なぜ重要か" headers
- **Include**: Core insight + most controversial/unique perspective naturally integrated

#### 5. Edge Case Handling

**Complex Articles** (resist 80-120 word summary):
→ Focus on SINGLE most important insight, state WHAT it proves (not HOW)
→ Use final sentence to deliver the powerful takeaway

**Multiple Key Points**:
→ Choose most UNIQUE/CONTROVERSIAL point for emphasis in closing
→ If equally important, weave both into narrative; combine max 2 points naturally

**Highly Technical Articles**:
→ Lead with result/capability enabled
→ Name specific technologies for searchability
→ Reserve technical details for closing emphasis

**Opinion/Essay Articles**:
→ State thesis clearly in opening
→ Include one strongest supporting evidence in middle
→ Close with most provocative claim

**Category Ambiguity**:
→ Decision matrix: What makes readers most interested? Which annex pillar?
→ Default: Omit category unless it adds non-obvious context
→ When must choose: 批判的分析 > ツール・実験 > セキュリティ・リスク > ニッチ・深堀り > others

#### 6. Example Transformation

**BEFORE (Current Format - 300+ words)**:
```markdown
### Silaute Code: 実践して見えたAIエージェントの限界

https://qiita.com/Yu_yukk_Y/items/0a61b4f1a6784981f2a9

著者がCursor AIの代替として「Silaute Code」という新興AIエージェントツールを試用した結果、期待とは裏腹に実用レベルに達していないという率直な評価を報告しています。

試用の結果、コード生成の精度が低く、プロジェクトの文脈理解が不十分で、生成されたコードが実際には動作しないケースが頻発しました。特に、既存のコードベースとの整合性を保ちながら新機能を追加するタスクでは、エラーが多発し、手動での修正に多くの時間を費やす結果となりました。

著者は、この失敗体験から重要な教訓を導き出しています。AIツールの宣伝文句を鵜呑みにせず、自社のユースケースで実際に検証することの重要性、そして、成熟したツール(CursorやGitHub Copilot)の安定性と精度の高さを改めて評価する機会となったと述べています。

失敗事例の共有は、成功事例よりも貴重な学びを提供します。この記事は、新しいAIツールを導入する際の慎重さと、現実的な期待値設定の重要性を思い出させてくれます。
```

**AFTER (New Catalog Format - 98 words, integrated)**:
```markdown
### Silaute Code実践レビュー：AIエージェントの失敗から学ぶ教訓
**原題**: Silaute Code: Practical Lessons from AI Agent Failure
**カテゴリー**: ツール・実験
**URL**: https://qiita.com/Yu_yukk_Y/items/0a61b4f1a6784981f2a9

Cursor AIの代替として新興AIエージェント「Silaute Code」を実践検証したが、コード生成精度が低く文脈理解が不十分で実用レベルに未達。既存コードベースとの整合性を保つタスクでエラーが頻発し、手動修正に多大な時間を要した結果、開発効率が大幅に低下。AIツール導入時は宣伝を鵜呑みにせず、自社の実際のユースケースで徹底的に検証することが不可欠という教訓を提示。失敗事例の共有こそが成功事例より貴重な学び――成熟ツール(Cursor、GitHub Copilot)の真価を再認識させる実践レポート。

---
```

#### 7. Thematic Sections (5-6 Sections)

Group articles by annex themes (target: 5-6 sections):
- Advanced Tactics & Unconventional Wisdom
- Substantive Critique & Contrarian Views
- Niche Explorations & Deep Dives
- Failed Experiments & Cautionary Tales
- Security Risks & Technical Debt

**Format**:
```markdown
## [Sequential Number]. [Theme Title in Japanese]

[Optional: 1-2 sentence theme introduction if needed for context]

### [Article 1 in Catalog Format]
...

---

### [Article 2 in Catalog Format]
...

---
```

#### 8. Annex Conclusion

```markdown
## 編集後記

[Write 2-3 paragraphs reflecting on:
- Why these B-side perspectives matter
- Complementary value to main journal (catalog format enables quick scanning)
- Encouragement for deeper exploration based on reader interests]

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
```

#### 9. Quality Verification Checklist

**Per Entry**:
- [ ] Integrated summary: 80-120 words (3-4 sentences)
- [ ] Original title (原題) included for English articles
- [ ] Category included only when adds non-obvious context
- [ ] First sentences establish: "What problem/question?"
- [ ] Middle sentences convey: "What's the key insight?"
- [ ] Final sentence(s) deliver: "Why this matters" / unique angle
- [ ] No filler words or redundant phrases
- [ ] Critical takeaway woven naturally into narrative (not separate)
- [ ] Most compelling/controversial point is prominent

**Complete Annex**:
- [ ] 5-6 thematic sections maintained
- [ ] All curated_annex_journal_sources.md articles included
- [ ] No overlap with main journal
- [ ] Catalog philosophy explained in header
- [ ] 編集後記 reflects catalog format
- [ ] Consistent format throughout

---

## STEP_08c: Polish & Verify

### 1. Editorial Voice Check

- [ ] Consistent tone: friendly, technical, startup-minded (see EDITOR_PERSONALITY.md)
- [ ] Smooth transitions between articles
- [ ] Japanese language quality and clarity
- [ ] Technical accuracy maintained

### 2. Source Coverage Verification

**Main Journal**:
```bash
# Extract URLs from journal
grep -o 'https://[^[:space:]]*' workdesk/weekly_journal_YYYY_MM_DD.md | sort -u > temp_main_journal_urls.txt

# Extract URLs from curated sources
grep -o 'https://[^[:space:]]*' workdesk/curated_journal_sources.md | sort -u > temp_main_sources.txt

# Compare - should be identical
diff temp_main_journal_urls.txt temp_main_sources.txt

# Clean up
rm temp_main_journal_urls.txt temp_main_sources.txt
```

**Annex Journal**:
```bash
# Same process for annex
grep -o 'https://[^[:space:]]*' workdesk/annex_journal_YYYY_MM_DD.md | sort -u > temp_annex_journal_urls.txt
grep -o 'https://[^[:space:]]*' workdesk/curated_annex_journal_sources.md | sort -u > temp_annex_sources.txt
diff temp_annex_journal_urls.txt temp_annex_sources.txt
rm temp_annex_journal_urls.txt temp_annex_sources.txt
```

- [ ] All curated sources appear in corresponding journal
- [ ] No URLs missing
- [ ] No duplicate URLs

### 3. Format & Polish

- [ ] Consistent heading levels (# for title, ## for sections, ### for articles)
- [ ] Proper `---` separators between articles
- [ ] Clean markdown syntax
- [ ] All URLs are plain text (not markdown links)
- [ ] No metadata remnants (scores, tags, content type)

### 4. Final Quality Check

- [ ] Engaging introductions that set context
- [ ] Logical flow from article to article
- [ ] "今週のハイライト" provides meta-analysis, not just summary
- [ ] "おわりに" offers reflection and forward perspective
- [ ] Ready for publication without further editing

---

## Example Reference

**Study these published journals for format guidance**:
- `journals/2025-12-06/00_weekly_journal_2025_12_06.md` - Main journal format
- `journals/2025-12-06/01_annex_journal_2025_12_06.md` - Annex journal format

**Key patterns to replicate**:
- Section structure (6-7 sections for main, 5-6 for annex)
- Article format (title, URL, summary with no metadata)
- Meta-commentary style in highlights and conclusions
- Editorial voice and tone

---

## Automation Support (Optional)

For teams preferring script-assisted assembly:

```python
# Pseudocode for extraction script
def extract_clean_summary(unified_summary_file):
    articles = []
    for article in parse_markdown(unified_summary_file):
        # Extract
        title_ja = article.title_japanese
        url = article.url
        summary = article.summary_content

        # Clean - remove metadata
        clean_summary = remove_metadata(summary)

        articles.append({
            'title': title_ja,
            'url': url,
            'summary': clean_summary
        })
    return articles

# Human still organizes into themes and writes meta-content
```

---

## Output Files

- **Main Journal**: `workdesk/weekly_journal_YYYY_MM_DD.md` (complete, publication-ready)
- **Annex Journal**: `workdesk/annex_journal_YYYY_MM_DD.md` (complete, publication-ready)

## Quality Standards

Final journals must:
- [ ] Match format of published journal examples
- [ ] Include ALL URLs from curated source lists
- [ ] Have no metadata remnants (scores, tags, etc.)
- [ ] Contain 3-4 paragraph "今週のハイライト" meta-analysis
- [ ] Organize articles into 5-7 thematic sections
- [ ] Maintain consistent editorial voice throughout
- [ ] Be ready for direct publication

## Next Step

[STEP_09_VERIFY.md](STEP_09_VERIFY.md) - Verify URLs and perform final quality checks
