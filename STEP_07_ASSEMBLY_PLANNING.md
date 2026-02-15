# Step 7: Assembly Planning

This step bridges editorial planning (STEP_03b) and final assembly (STEP_08) by determining **HOW** to assemble each theme using proven narrative patterns.

## Objective

For each theme identified in STEP_03b, select and customize assembly patterns that will guide the actual writing in STEP_08. Transform theme outlines into detailed assembly strategies with article ordering, narrative flow, and connection points.

## What Changed from Old STEP_07

**Old STEP_07**: Review and refine individual summaries for editorial voice
**New STEP_07**: Plan assembly strategy for each theme using pattern library

**Why the change?**
- Editorial voice review happens naturally during STEP_08 assembly
- Gap existed between theme planning (STEP_03b) and assembly (STEP_08)
- Assembly patterns codify institutional knowledge and improve consistency
- Clear assembly strategy speeds up STEP_08 and improves narrative quality

## Input Files

- **Editorial Plan:** `workdesk/editorial_plan_YYYY_MM_DD.md` (✅ APPROVED from STEP_03b)
  - Contains: Themes, article mappings, theme introductions, highlight outline
- **Curated Sources:** `workdesk/curated_journal_sources.md` (theme-organized article lists)
- **Article Summaries:** `workdesk/unified_summaries_main.md` (full article content)
- **Pattern Library:** `patterns/assembly/*.md` (available assembly patterns)

## Assembly Planning Process

### Phase 1: Pattern Library Review (AI-Driven)

**Objective:** Understand available assembly patterns before selecting

- [ ] Read all pattern definitions from `patterns/assembly/`:
  - `README.md` - Pattern library overview
  - `single-focus.md` - One major topic with reactions
  - `multi-perspective.md` - Multiple equal viewpoints
  - `progressive-sequence.md` - Articles building on each other
  - `debate-contrast.md` - Opposing viewpoints creating tension

- [ ] Understand pattern characteristics:
  - When each pattern works best
  - Structure and ordering principles
  - Narrative flow strategies
  - Example use cases from past journals

**Output:** Mental model of available patterns and their uses

---

### Phase 2: Theme-by-Theme Pattern Selection (AI + Human Collaboration)

**Objective:** For each theme, determine the best assembly pattern and customize it

**Process for each theme:**

#### Step 1: AI Proposes Pattern

AI analyzes:
- Theme title and introduction (from editorial plan)
- Mapped articles (from curated sources)
- Article content (from unified summaries)
- Relationships between articles

AI proposes:
```
Theme: [Theme Title from Editorial Plan]

Articles in theme:
- [001] Article Title
- [039] Article Title
- [146] Article Title
...

Suggested Pattern: [Pattern Name]

Rationale:
[Why this pattern fits - 2-3 sentences explaining the match]

Pattern Characteristics:
[How this theme exhibits pattern's characteristics]

Alternative Patterns to Consider:
- [Alternative 1]: [Why it could work]
- [Alternative 2]: [Why it could work]
```

#### Step 2: Human Reviews and Decides

Human can:
- ✅ Approve suggested pattern
- 🔄 Request different pattern from alternatives
- 💬 Propose customizations to suggested pattern
- ➕ Request hybrid pattern (combining elements)
- 🆕 Define new pattern if none fit

#### Step 3: Conversational Customization

**For approved pattern, AI and human discuss:**

1. **Article Order & Rationale**
   - Why this specific sequence?
   - What breaks if reordered?
   - What progression do articles show?

2. **Narrative Strategy**
   - Key question theme answers
   - Progression markers ("Building on this..." vs "In contrast...")
   - Emphasis points (technical depth? Business impact? Future implications?)

3. **Connection Points**
   - How does Article A → Article B transition?
   - Where do articles complement each other?
   - Where do articles create productive tension?

4. **Writing Prompts for STEP_08**
   - What questions should the assembled section answer?
   - What synthesis should emerge from combining articles?
   - What should readers take away from this theme?

**Example Customization Dialog:**

```
AI: For Theme 1 "コンテキスト爆発への処方箋", I suggest Progressive Sequence
    because articles show evolution from problem → solutions.

    Suggested order:
    1. [001] Power Prompts - Identifies context explosion problem
    2. [039] Agent Teams - First solution approach (multi-agent)
    3. [146] Playwright MCP - Optimization technique (90% reduction)
    4. [048] Agentic Search - Architectural rethinking
    5. [040] DMN Implementation - Advanced/future direction

    Rationale: Each article assumes/builds on previous knowledge.
    Reader journey: Problem awareness → Tactical fixes → Strategic solutions

Human: That makes sense\! I like the problem → solution arc.
        But should article [146] (Playwright - 90% reduction) come before
        [039] (Agent Teams)? The specific optimization seems more tactical
        than the broad multi-agent concept.

AI: Good point. Let me reconsider:

    Revised order:
    1. [001] Power Prompts - Problem identification
    2. [146] Playwright MCP - Immediate tactical solution (90% reduction)
    3. [039] Agent Teams - Architectural solution (multi-agent)
    4. [048] Agentic Search - Strategic rethinking
    5. [040] DMN - Advanced/future (AI thinking while idle)

    Rationale: Tactical → Architectural → Strategic → Visionary.
    Readers get immediate wins before conceptual shifts.

Human: Perfect. Let's use that order.
        What narrative strategy should we use for transitions?

AI: For Progressive Sequence, emphasize the "building" nature:

    Transitions:
    - [001] → [146]: "この課題に対する最も直接的な解決策は..."
    - [146] → [039]: "しかし個別最適化だけでは限界がある。根本的な構成の見直しが必要だ"
    - [039] → [048]: "マルチエージェント構成を前提とすると、検索アーキテクチャも再考が必要になる"
    - [048] → [040]: "これらの進展が示すのは、AIが休んでいる間も思考を続ける未来だ"

    Synthesis for conclusion:
    "コンテキスト管理は、個別最適化から構造的変革へと進化している。
     DMNの実装が示すのは、効率化の次の段階――AIが人間のように
     「考え続ける」システムの到来だ。"

Human: ✅ Approved. Let's move to Theme 2.
```

---

### Phase 3: Document Assembly Strategies

**Objective:** For each theme, create assembly strategy document that will guide STEP_08

**AI creates strategy document:**

For each theme, add to editorial plan:

```markdown
## Assembly Strategy - Theme 1: [Theme Title]

**Pattern:** Progressive Sequence

**Article Order:**
1. [001] Article Title - Role in narrative
2. [146] Article Title - Role in narrative
3. [039] Article Title - Role in narrative
...

**Narrative Arc:**
[2-3 sentences describing the progression/journey]

**Key Transitions:**
- [001] → [146]: [Transition strategy]
- [146] → [039]: [Transition strategy]
...

**Emphasis Points:**
- Technical depth: [High/Medium/Low + what to emphasize]
- Business impact: [High/Medium/Low + what to emphasize]
- Future implications: [High/Medium/Low + what to emphasize]

**Writing Prompts for STEP_08:**
1. What question does this theme answer?
2. What synthesis emerges from combining these articles?
3. What should readers take away?
4. Where is this area heading?

**Conclusion Strategy:**
[Template or approach for wrapping up this theme]
```

**Process:**

- [ ] For each theme in editorial plan:
  - AI proposes pattern (Phase 2 Step 1)
  - Human approves/refines (Phase 2 Step 2)
  - AI and human customize (Phase 2 Step 3)
  - AI documents assembly strategy

- [ ] Human reviews complete assembly plan

- [ ] Human approves: ✅ ASSEMBLY STRATEGIES APPROVED

---

## Assembly Strategy Template

**What gets added to `editorial_plan_YYYY_MM_DD.md`:**

```markdown
---

## ASSEMBLY STRATEGIES

### Theme 1: [Theme Title]

**Pattern:** [Pattern Name]
**Pattern Rationale:** [Why this pattern fits - 1-2 sentences]

**Article Order & Roles:**
1. [ID] Article Title - [Role: Foundation/Development/Advanced/Payoff]
2. [ID] Article Title - [Role]
...

**Narrative Arc:**
[Describe the progression/journey/debate that articles create together]

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [001] → [146] | [Japanese transition phrase/approach] |
| [146] → [039] | [Japanese transition phrase/approach] |
...

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (or High/Medium/Low)
- Business Impact: ⭐⭐
- Future Outlook: ⭐⭐⭐

**Key Synthesis Points:**
- [Insight that emerges from combining articles]
- [Connection that wouldn't be obvious from individual articles]
- [Broader implication for the field]

**Conclusion Approach:**
[How to wrap up this theme - template or specific direction]

**Assembly Prompts for STEP_08:**
1. [Question theme answers]
2. [Synthesis to create]
3. [Reader takeaway]
4. [Field trajectory]

---

### Theme 2: [Theme Title]

[Same structure repeats]

---

[Repeat for all themes]

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Approval Date:** [YYYY-MM-DD]
**Approver:** [Human Editor Name]
```

---

## Output Files

**Updated file:** `workdesk/editorial_plan_YYYY_MM_DD.md`

**Additions to editorial plan:**
- Assembly strategies section (one per theme)
- Pattern selections with rationale
- Article ordering with roles
- Transition strategies
- Writing prompts for STEP_08
- Assembly plan approval checkbox

**No new files created** - Assembly strategies are appended to existing editorial plan

---

## Quality Standards

**Good assembly strategy:**
- ✅ Clear pattern selection with rationale
- ✅ Article order is justified (not arbitrary)
- ✅ Transitions are specific (not generic "次に...")
- ✅ Synthesis points go beyond individual articles
- ✅ Writing prompts are actionable for STEP_08
- ✅ Conclusion approach creates satisfying payoff

**Warning signs:**
- ❌ Pattern feels forced or artificial
- ❌ Article order is arbitrary (could be reshuffled)
- ❌ No clear narrative arc emerges
- ❌ Transitions are vague or formulaic
- ❌ No synthesis - just article summaries
- ❌ Assembly strategy doesn't add value over editorial plan

**When to reconsider:**
- If pattern doesn't fit naturally → Try different pattern
- If articles don't connect → Reconsider theme grouping
- If no narrative emerges → Theme may need restructuring
- If strategy feels like busywork → Simplify or merge with STEP_08

---

## Pattern Evolution

**Learning from execution:**

After completing STEP_08:
- Note what worked well in assembly
- Identify what assembly strategy missed
- Refine patterns based on real writing experience
- Add examples to pattern library

**Pattern library maintenance:**
- Successful assemblies → Add to pattern examples
- Failed assemblies → Add to anti-patterns
- New insights → Create new pattern variations
- Common customizations → Codify as pattern templates

**Institutional knowledge:**
- Assembly strategies capture "how we write good themes"
- Patterns evolve based on journal execution
- New editors can learn from past assembly strategies
- Pattern library becomes shared editorial vocabulary

---

## Next Step

Once assembly strategies are approved:

➡️ **STEP_08: Assemble Journal Sections** - Write themed sections using assembly strategies as blueprint

See: `STEP_08_ASSEMBLE_SECTIONS.md`
