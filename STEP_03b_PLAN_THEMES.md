# Step 3b: Plan Editorial Themes

This step introduces strategic editorial planning by identifying weekly themes BEFORE article curation. This ensures theme-driven selection rather than theme-discovery-after-the-fact.

## Objective

Analyze all collected summaries, identify 5-8 cohesive themes, and create an editorial roadmap that guides subsequent curation and assembly steps.

## Prerequisites

- [ ] STEP_03 completed (empty journal files created)
- [ ] All sources summarized (workdesk/summaries/ populated)
- [ ] unified_summaries.md exists with all article summaries

## Input Files

- **All Summaries:** `workdesk/unified_summaries.md`
- **Source List:** `workdesk/sources.md`
- **Editorial Persona:** `EDITOR_PERSONALITY.md`
- **Curation Criteria:** `criteria/curation_criteria.md`

## Process

### Part A: AI-Assisted Theme Discovery

#### 1. Read and Adopt Editorial Persona

- [ ] Read `EDITOR_PERSONALITY.md` and adopt the role
  - Technical web application engineer perspective
  - Startup-minded, visionary but grounded
  - Focus on "why it matters" beyond "what happened"

#### 2. Comprehensive Summary Analysis

- [ ] Read ALL summaries in `workdesk/unified_summaries.md`
- [ ] Note recurring topics, technologies, and perspectives
- [ ] Identify contradictions and tensions between articles
- [ ] Look for narrative arcs and industry shifts

#### 3. Generate Initial Theme Proposals

**AI Task:** Identify 5-8 potential themes based on:

- **Thematic Core Criteria** (from curation_criteria.md):
  - What are this week's main storylines?
  - Which clusters of articles tell a cohesive story?
  - What tensions or contradictions exist?

- **Common Theme Categories** (reference only):
  - Critical AI Perspectives & Industry Analysis
  - Real-World Implementation & Case Studies
  - New Tools & Platform Updates
  - Developer Experience & Methodology
  - Security & Compliance
  - Context Engineering & Architecture
  - Business & Economic Impact
  - Experimental & Failed Attempts (Annex-focused)
  - Contrarian Views & Substantive Critique (Annex-focused)

**Theme Title Guidelines - Be Concrete, Not Generic:**

Theme titles should be **specific, provocative, and attention-grabbing** rather than generic category labels.

✅ **GOOD (Concrete):**
- "コンテキスト爆発への処方箋：段階的開示とマルチエージェント構成"
- "Tailwind解雇75%の衝撃：AIがもたらすビジネスモデルの破壊"
- "プロンプトインジェクションとゼロクリック攻撃：自律性とセキュリティのトレードオフ"
- "AI至上主義と完全拒絶の同居：OpenAI凋落とYarn Spinnerの倫理宣言"

❌ **BAD (Generic):**
- "AIエージェントの実装戦略" → Too abstract
- "開発ツールとワークフロー" → Too broad
- "セキュリティ問題" → Too vague
- "ビジネスへの影響" → Too general

**Four Principles for Concrete Titles:**

1. **Name Specific Technologies/Events**
   - Bad: "新しいプロトコル"
   - Good: "UCPとMCPサンプリングが描くWebの再定義"

2. **Include Shocking Facts/Numbers**
   - Bad: "AIの雇用影響"
   - Good: "Tailwind解雇75%の衝撃：価値のシフト"

3. **Highlight Contradictions/Tensions**
   - Bad: "AIへの批判"
   - Good: "AI至上主義と完全拒絶の同居：OpenAI凋落とYarn Spinnerの倫理宣言"

4. **Pose Provocative Questions**
   - Bad: "開発者体験の管理"
   - Good: "認知負荷の科学的管理：開発者は「考える係」に徹するべきか"

**Title Structure Patterns:**

- **[Problem]: [Solution]** - "コンテキスト爆発への処方箋：段階的開示とマルチエージェント構成"
- **[Shocking Event]: [Implication]** - "Tailwind解雇75%の衝撃：ビジネスモデルの破壊"
- **[Contradiction]: [Examples]** - "AI至上主義と完全拒絶の同居：OpenAI凋落とYarn Spinnerの倫理宣言"
- **[Specific Tech]: [Broader Impact]** - "UCPとMCPサンプリングが描くWebの再定義"
- **[Topic]: [Provocative Question]** - "認知負荷の科学的管理：開発者は「考える係」に徹するべきか"

**Why Concrete Titles Matter:**
- Immediately communicate the theme's value proposition
- Create curiosity and reading motivation
- Make the narrative arc visible at a glance
- Differentiate from generic tech news aggregation
- Reflect the "visionary but grounded" editorial persona

#### 4. Map Articles to Themes

- [ ] For each proposed theme, list candidate article IDs
- [ ] Ensure coverage: aim for 18-25 articles in main journal themes
- [ ] Flag articles for annex journal (unique perspectives, niche topics)
- [ ] Identify articles that span multiple themes

#### 5. Draft Theme Introductions

For each theme:
- [ ] Write 2-3 sentence introduction (Japanese)
- [ ] Explain what the theme covers
- [ ] Articulate why it matters this week
- [ ] Note connections between articles in this theme

#### 6. Draft "今週のハイライト" Outline

- [ ] Write 3-4 paragraph outline analyzing:
  - Week's main narrative arc
  - Contradictions/tensions between developments
  - Significant industry shifts
  - Why this week matters to developers
  - Forward-looking perspective

#### 7. Create Planning Document

- [ ] Generate `workdesk/editorial_plan_YYYY_MM_DD.md` from template below
- [ ] Fill in all identified themes
- [ ] Add article-to-theme mappings
- [ ] Include highlight outline
- [ ] Add editorial notes for each theme

---

### Part B: Human Review Gate (REQUIRED)

**⚠️ WORKFLOW STOPS HERE - HUMAN APPROVAL REQUIRED ⚠️**

#### 8. Review and Refine Editorial Plan

**Human Editor Tasks:**

- [ ] Review proposed themes for coherence and narrative strength
- [ ] Verify article-to-theme mappings make editorial sense
- [ ] Refine theme titles for clarity and impact
- [ ] Edit theme introductions for editorial voice
- [ ] Adjust highlight outline to capture week's essence
- [ ] Reassign articles between themes as needed
- [ ] Decide which articles belong in main vs. annex

**Quality Checks:**

- [ ] Do themes tell a cohesive weekly story?
- [ ] Are contradictions and tensions highlighted?
- [ ] Does the plan reflect EDITOR_PERSONALITY.md voice?
- [ ] Are theme titles concrete and specific (not generic category labels)?
  - Check: Do titles name specific technologies, events, or numbers?
  - Check: Do titles highlight contradictions or pose questions?
- [ ] Are theme introductions engaging and insightful?
- [ ] Is the article distribution appropriate (18-25 main, rest annex)?
- [ ] Do themes align with curation_criteria.md principles?

#### 9. Mark Plan as Approved

- [ ] Update "Planning Status" section in editorial_plan_YYYY_MM_DD.md
- [ ] Check ✅ "APPROVED - Ready for STEP_04 curation"
- [ ] Add review notes documenting any changes
- [ ] Commit planning document to git

```bash
git add workdesk/editorial_plan_YYYY_MM_DD.md
git commit -m "Complete editorial theme planning for YYYY-MM-DD

Identified X themes:
- [Theme 1 title]
- [Theme 2 title]
- [etc.]

Planned distribution: XX main journal, YY annex journal

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Planning Document Template

When creating `workdesk/editorial_plan_YYYY_MM_DD.md`, use this structure:

```markdown
# Editorial Plan - Journal YYYY-MM-DD

## Planning Status
- [ ] Initial theme identification (AI-assisted)
- [ ] Human review and refinement
- [ ] Theme introductions drafted
- [ ] Article-to-theme mapping complete
- [ ] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and attention-grabbing**
- ✅ Name specific technologies, events, numbers
- ✅ Highlight contradictions or pose questions
- ❌ Avoid generic category labels

### Theme 1: [Concrete Japanese Theme Title]

**Articles (IDs):** 007, 012, 023, 034

**Theme Introduction (2-3 sentences in Japanese):**
[Draft introduction explaining what this theme covers and why it matters this week]

**Editorial Notes:**
- Key insights to emphasize:
- Connections between articles:
- Potential challenges:

---

### Theme 2: [Japanese Theme Title]

**Articles (IDs):** 001, 015, 029

**Theme Introduction (2-3 sentences in Japanese):**
[Draft introduction]

**Editorial Notes:**
- Key insights:
- Connections:
- Challenges:

---

[Repeat for 5-8 themes total for main journal]
[Repeat for 5-6 themes total for annex journal if planning annex]

---

## Highlight Draft ("今週のハイライト")

**Main Narrative Arc:**
[2-3 paragraphs analyzing the week's overarching story]

**Key Points to Cover:**
1. Contradictions or tensions between developments
2. Significant shifts in industry thinking
3. Why this week matters to developers
4. Forward-looking perspective

**Cross-Cutting Insights:**
- [Insight that ties multiple themes together]
- [Another cross-cutting observation]

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 6-7 themes
- Annex Journal: Remaining articles across 5-6 themes

**Article Count by Theme (Planned):**
- Theme 1: 4 articles
- Theme 2: 3 articles
- Theme 3: 5 articles
- Theme 4: 4 articles
- Theme 5: 3 articles
- Theme 6: 3 articles
- [etc.]

**Total Planned for Main:** XX articles
**Remaining for Annex:** YY articles

---

## Review Notes (Human Editor)

**Date Reviewed:** YYYY-MM-DD
**Reviewer:** [Name]

**Changes Made:**
- [List any theme refinements]
- [Article reassignments]
- [Other modifications]

**Approval:** ✅ APPROVED / ❌ NEEDS REVISION

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
```

---

## Output

- **Planning Document:** `workdesk/editorial_plan_YYYY_MM_DD.md` (APPROVED)
- **Git Commit:** Theme planning committed to branch

## Verification

- [ ] Planning document exists and is well-formed
- [ ] All themes have article mappings
- [ ] Theme introductions are drafted
- [ ] Highlight outline captures week's narrative
- [ ] Planning Status shows "APPROVED"
- [ ] Human editor has reviewed and approved

## Next Step

[STEP_04_CURATE_MAIN.md](STEP_04_CURATE_MAIN.md) - Use approved editorial plan to curate main journal articles

---

## Notes

**Why This Step Matters:**

1. **Coherent Storytelling:** Themes are identified BEFORE curation, ensuring the journal tells a cohesive story rather than being a random collection
2. **Intentional Selection:** Article selection is theme-driven, making editorial decisions more defensible and consistent
3. **Efficient Assembly:** STEP_08 becomes much faster because themes and introductions are already planned
4. **Human Oversight:** The review gate ensures editorial quality and strategic direction align with journal goals
5. **Reusable Blueprint:** The planning document serves as a reference throughout STEP_04-08

**AI-Human Collaboration:**

- AI excels at: Pattern recognition across many summaries, clustering articles, drafting initial themes
- Human excels at: Strategic editorial judgment, narrative coherence, voice consistency, final theme selection
- This step leverages both strengths effectively

**Archive Note:**

After STEP_10 (Archive & Cleanup), consider archiving the editorial plan to `journals/YYYY-MM-DD/editorial_plan.md` for future reference and process improvement.
