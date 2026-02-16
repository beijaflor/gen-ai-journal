# Editorial Plan - Assembly Strategy Template

This template shows the structure that gets **added to** `editorial_plan_YYYY_MM_DD.md` during STEP_07 (Assembly Planning).

Assembly strategies are appended to each theme section in the existing editorial plan.

---

## Example: Theme with Assembly Strategy (Added in STEP_07)

### Theme 1: [Original Theme Title from STEP_03b]

**Articles (Candidate Titles):**
- [001] Article Title
- [039] Article Title
- [146] Article Title
...

**Theme Introduction (2-3 sentences in Japanese):**
[Original introduction from STEP_03b]

**Editorial Notes:**
- Key insights: [Original notes from STEP_03b]
- Connections: [Original connections from STEP_03b]
- Challenges: [Original challenges from STEP_03b]

---

#### Assembly Strategy (Added in STEP_07)

**Pattern Selected:** Progressive Sequence (Customized)

**Rationale:**
Articles show clear evolution from problem identification → tactical solutions → strategic rethinking → future direction. Each article builds on previous knowledge, making Progressive Sequence the natural fit. Customization: Emphasize "problem → solution" arc with explicit token cost metrics.

**Article Order & Role:**
1. [001] Power Prompts - **Foundation**: Establishes context explosion as THE problem
2. [039] Agent Teams - **Development**: First solution approach (multi-agent architecture)
3. [146] Playwright MCP - **Optimization**: Tactical fix (90% token reduction case study)
4. [048] Agentic Search - **Strategic Shift**: Architectural rethinking beyond band-aids
5. [040] DMN Implementation - **Future Vision**: Advanced concept (continuous AI思考)

**Narrative Arc:**
- **Opening question**: How do we scale AI agents without token budget explosion?
- **Progression**: Problem awareness → Quick fixes → Systemic solutions → Future paradigm
- **Key synthesis**: From reactive optimization to proactive architecture

**Transition Strategy:**

| From | To | Transition Type | Japanese Phrase Example |
|------|-----|-----------------|-------------------------|
| [001] | [039] | Problem → Solution | この課題に対し、Agent Teams というアプローチが登場した |
| [039] | [146] | Amplification → Mitigation | しかし、マルチエージェントは新たなトークン消費を生む。これを90%削減した事例が... |
| [146] | [048] | Tactical → Strategic | 最適化だけでは限界がある。根本的なアーキテクチャの再考が必要だ |
| [048] | [040] | Current → Future | そして最終的に到達するのは、「休んでいる間も思考する」AI の実現だ |

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (具体的な実装手法を重視)
- Business impact: ⭐⭐ (コスト削減を明示)
- Future implications: ⭐⭐⭐ (DMN で未来像を示す)

**Key Synthesis Points:**
1. Context explosion is not just a technical problem but a cost/scale problem
2. Solutions range from tactical (Hooks, MCP) to strategic (agentic search, DMN)
3. The field is moving from "prompt optimization" to "architecture design"
4. Future: AI that thinks continuously, not just on-demand

**Conclusion Approach:**
End with forward-looking question: "From reactive context management to proactive AI architecture—where does this trajectory lead?" Position DMN as glimpse of AI's next evolution.

**Assembly Prompts for STEP_08:**
1. What maturity curve do these articles show? (Problem → Tactical → Strategic → Visionary)
2. Where is the field heading based on this progression?
3. What should readers understand about their own context management strategy?
4. How do we make technical details serve the narrative (not overwhelm it)?

**Status:**
- [ ] Pattern selected and rationale documented
- [ ] Article order finalized
- [ ] Transitions strategy defined
- [ ] Ready for STEP_08 assembly

---

## Template Structure Reference

Use this structure for each theme's assembly strategy:

```markdown
#### Assembly Strategy (Added in STEP_07)

**Pattern Selected:** [Pattern Name] ([Variation if customized])

**Rationale:**
[2-3 sentences explaining why this pattern fits this theme.
What characteristics of the articles make this pattern appropriate?]

**Article Order & Role:**
1. [ID] Title - **[Role in pattern]**: [Why this position]
2. [ID] Title - **[Role in pattern]**: [Why this position]
...

**Narrative Arc:**
- **Opening question**: [What question does theme answer?]
- **Progression**: [How does theme build/develop?]
- **Key synthesis**: [What emerges from combining articles?]

**Transition Strategy:**

| From | To | Transition Type | Japanese Phrase Example |
|------|-----|-----------------|-------------------------|
| [ID] | [ID] | [Type] | [Example phrase] |
...

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (adjust rating and note)
- Business impact: ⭐⭐ (adjust rating and note)
- Future implications: ⭐⭐⭐ (adjust rating and note)

**Key Synthesis Points:**
1. [Synthesis point 1]
2. [Synthesis point 2]
3. [Synthesis point 3]

**Conclusion Approach:**
[How should this theme section end? What final thought/question?]

**Assembly Prompts for STEP_08:**
1. [Question that assembly should answer]
2. [Question that assembly should answer]
3. [Question that assembly should answer]

**Status:**
- [ ] Pattern selected and rationale documented
- [ ] Article order finalized
- [ ] Transitions strategy defined
- [ ] Ready for STEP_08 assembly
```

---

## Pattern-Specific Variations

### For Single-Focus Pattern:

**Article Order & Role:**
1. [ID] Main Article - **Lead**: Primary source/announcement
2. [ID] Technical Analysis - **Supporting**: Technical perspective
3. [ID] Business View - **Supporting**: Business/impact perspective
4. [ID] Critical Response - **Contrarian** (if exists): Challenge assumptions

**Transition Strategy:**
- Lead → First Support: "この発表を受け、X の視点から..."
- Between Supports: "一方で、Y の角度では..."
- To Contrarian: "しかし、Z は警鐘を鳴らす..."

### For Multi-Perspective Pattern:

**Article Order & Role:**
1. [ID] Perspective A - **Peer**: [Which viewpoint/context]
2. [ID] Perspective B - **Peer**: [Which viewpoint/context]
3. [ID] Perspective C - **Peer**: [Which viewpoint/context]

**Transition Strategy:**
- Between peers: "別の角度から..." / "対照的に..." / "この視点を補完するように..."
- No hierarchy, create dialogue through ordering

### For Debate-Contrast Pattern:

**Article Order & Role:**
1. [ID] Position A - **Thesis**: [What they argue]
2. [ID] Position B - **Antithesis**: [Counter-argument]
3. [ID] Analysis (optional) - **Synthesis**: [Meta-insight]

**Transition Strategy:**
- Thesis → Antithesis: "これに対し、Y は真っ向から異を唱える..."
- To Synthesis: "この対立が浮き彫りにするのは..."

---

## Notes on Using This Template

1. **Adapt, don't copy verbatim**: Each theme is unique; customize strategy to fit
2. **Transitions are guidelines**: Actual Japanese in STEP_08 can vary; these are starting points
3. **Emphasis balance**: Helps editor know what to highlight during assembly
4. **Assembly prompts**: Critical questions to answer while writing; ensures synthesis
5. **Status checkboxes**: Track completion of assembly planning for each theme

---

## When Assembly Strategy is Complete

After all themes have assembly strategies documented:

1. **Update Editorial Plan Status:**
```markdown
## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation
- [x] **Assembly strategies defined (STEP_07)** ← ADD THIS
```

2. **Proceed to STEP_08:**
With detailed assembly strategies, STEP_08 assembly becomes:
- Faster (clear direction for each theme)
- More consistent (pattern guidelines ensure quality)
- More narrative-driven (connection points and transitions defined)
- Easier to verify (assembly prompts provide success criteria)

3. **Pattern Library Evolution:**
Note which patterns worked well, which needed heavy customization, and why. Update pattern library with insights for future journals.
