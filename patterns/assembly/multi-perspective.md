# Multi-Perspective Pattern

## When to Use

This pattern works best when:
- **Same topic, multiple equally valid viewpoints** with no single authoritative source
- **No clear hierarchy** among articles—all are peers
- **Reader benefits from seeing the full spectrum** before forming opinion
- The value is in **juxtaposition and dialogue** between perspectives

**Example scenarios:**
- Multiple developers sharing different approaches to same problem
- Various experts analyzing same trend from their domains
- Community split on controversial practice (no consensus)
- Multiple implementations of same concept (React vs Vue vs Svelte)

**NOT for:**
- One main article + reactions (use **Single-Focus** instead)
- Articles building on each other (use **Progressive-Sequence** instead)
- Direct opposing viewpoints creating debate (use **Debate-Contrast** instead)

## Structure

```
No hierarchy—articles presented as peers:

Article A (Perspective 1: e.g., startup CTO)
   ↕
Article B (Perspective 2: e.g., enterprise architect)
   ↕
Article C (Perspective 3: e.g., indie developer)
   ↕
Optional: Synthesis/Editor commentary
```

**Key principle:** Create dialogue through thoughtful ordering, not through hierarchy

## Assembly Guidelines

### Article Selection & Ordering

**Primary ordering strategies:**

1. **Accessibility-first**: Start with most approachable perspective
   - Tutorial/beginner-friendly article first
   - Advanced/esoteric perspective last
   - Helps readers build context progressively

2. **Contrast-driven**: Alternate between complementary and contrasting views
   - Optimistic → Skeptical → Pragmatic
   - Big company → Startup → Individual
   - Creates intellectual tension

3. **Scope progression**: Narrow to broad (or vice versa)
   - Specific implementation → General principles
   - Individual experience → Industry-wide trend
   - Micro → Macro perspective

4. **Temporal**: If relevant, follow time sequence
   - Early adopter experience → Mature usage patterns
   - Initial hype → Sober second thought
   - Past → Present → Future outlook

### What to Emphasize

- **Legitimacy of ALL perspectives**: No perspective is "wrong"
- **Complementary insights**: How different angles reveal fuller picture
- **Productive tensions**: Where perspectives disagree constructively
- **Synthesis opportunity**: What emerges from combining viewpoints

### Common Pitfalls

- ❌ Accidentally creating hierarchy (treating first article as "main")
- ❌ Grouping similar perspectives together (reduces diversity)
- ❌ Failing to show HOW perspectives differ (readers miss the point)
- ❌ Leaving tensions unresolved (synthesis is important)

## Narrative Flow

### Introduction Strategy

Establish the multi-faceted nature of the topic:

**Template approach:**
```
[Topic] については、[different groups] がそれぞれ異なる視点を持っている。
[Why multiple perspectives matter for this topic]
```

**Example:**
```
AI エージェント開発のアーキテクチャについては、
スタートアップ、大企業、個人開発者がそれぞれ異なる制約と
優先順位を持っており、「最適解」は文脈に依存する。
```

**Alternative frame:**
```
[Topic] は単一の正解がない領域だ。[Context why no single answer exists]
```

### Transition Strategies

**Moving between perspectives (non-hierarchical):**

1. **Additive transition** (perspectives complement):
```
別の角度から、[source] は [complementary insight] を示している。
→ "別の角度から、Google の SRE チームはスケーラビリティを重視している。"
```

2. **Contrasting transition** (perspectives differ):
```
対照的に、[source] は [different conclusion] と主張する。
→ "対照的に、indie developer は複雑さを避ける方を選んでいる。"
```

3. **Contextual transition** (perspective depends on context):
```
[Context] においては、[source] のアプローチが説得力を持つ。
→ "大規模システムにおいては、Stripe のマイクロサービス戦略が説得力を持つ。"
```

4. **Building transition** (perspectives layer):
```
この視点を補完するように、[source] は [additional dimension] を加える。
→ "この視点を補完するように、Paul Graham はスピードの重要性を加える。"
```

### Conclusion Strategy

Synthesize what the range of perspectives reveals:

**Questions to answer:**
1. What does the diversity of perspectives tell us about the topic's complexity?
2. Are there commonalities beneath surface differences?
3. What factors determine which perspective is "right" for a given context?
4. What does the conversation itself (not just content) reveal?

**Template approach:**
```
[Topic] をめぐる多様な視点は、[what diversity reveals about topic]。
[Common thread or meta-insight from synthesis]
重要なのは、[key decision factor] に応じて適切なアプローチを選ぶことだ。
```

**Example:**
```
AI エージェント設計をめぐる多様な視点は、
「普遍的ベストプラクティス」の限界を示している。
チーム規模、技術的負債、市場投入スピードという
3つの軸が最適解を大きく左右する。
重要なのは、自分の制約条件を正確に把握することだ。
```

## Example from Past Journals

### Journal 2025-12-27: Theme "プロンプトエンジニアリングの実践知"

**Pattern used:** Multi-Perspective

**Article structure:**
1. **Academic researcher**: 体系的手法とベンチマーク重視
2. **Startup founder**: 速度とコスト効率重視
3. **Enterprise AI team**: ガバナンスと監査重視
4. **Individual developer**: 実験と直感重視

**Why it worked:**
- 4つの視点すべてが正当で価値がある
- 優先順位の違いが文脈依存であることを示した
- 「正解」ではなく「選択の基準」を提供

**Narrative flow:**
- Intro: プロンプト設計に万能解はない
- Transitions: "研究の視点では..." → "一方、スタートアップでは..." → "対照的に企業では..." → "個人開発者は..."
- Conclusion: 制約条件によって最適解が変わる。自分の文脈を理解せよ。

---

### Journal 2025-12-13: Theme "コード生成 AI の限界と可能性"

**Pattern used:** Multi-Perspective (with temporal ordering)

**Article structure:**
1. **Early adopter (2023)**: 当初の期待と失望
2. **Current power user (2024)**: 洗練された使い方の発見
3. **Skeptic (2025)**: 依然として課題が多い
4. **Futurist (2025)**: 5年後の予測

**Why it worked:**
- 時系列に沿った視点の進化を示した
- 楽観/悲観のバランス
- 読者が自分の位置づけを見つけられる

**Customization:**
- 標準の Multi-Perspective に時間軸を追加
- Skeptic を排除せず、正当な視点として提示
- Futurist で締めて前向きな余韻

---

## Customization Examples

### Variation 1: Persona-Based Multi-Perspective

When perspectives align with clear personas:

**Modified structure:**
```
Theme: "AI ツール選定の基準"

1. CTO (enterprise): セキュリティと統制
2. Lead Developer (startup): 開発速度
3. Solo Founder (bootstrapped): コスト
4. Student/Learner: 学習曲線

→ Synthesis: あなたの立場はどれに近い?
```

**Use case:** Reader の文脈が多様で、セグメント別のアドバイスが必要な時

### Variation 2: Implementation Showcase

When multiple valid implementations exist:

**Modified structure:**
```
Theme: "RAG システムの実装パターン"

1. Simple (SQLite + embeddings)
2. Scalable (Pinecone + async processing)
3. Enterprise (Weaviate + governance layer)
4. Experimental (graph-based RAG)

→ Synthesis: Trade-offs の比較表
```

**Use case:** 技術選定で複数の選択肢を並列提示

### Variation 3: Geographic/Cultural Perspectives

When location/culture affects viewpoint:

**Modified structure:**
```
Theme: "AI 規制の影響"

1. US perspective (innovation focus)
2. EU perspective (regulation focus)
3. China perspective (national strategy)
4. Global South perspective (access concerns)

→ Synthesis: グローバル AI エコシステムの分断?
```

**Use case:** 地政学的文脈が重要なテーマ

---

## Decision Checklist

Use Multi-Perspective pattern when:

- [ ] Multiple articles address THE SAME topic/question
- [ ] No single article is more authoritative than others
- [ ] Perspectives are complementary or productively different
- [ ] Value is in seeing the RANGE of viewpoints
- [ ] Reader needs to choose approach based on their context

**Do NOT use** when:
- [ ] One article is clearly the "main" source → Use **Single-Focus**
- [ ] Articles build on each other sequentially → Use **Progressive-Sequence**
- [ ] Two direct opposing camps exist → Use **Debate-Contrast**
- [ ] Perspectives are too similar (redundant) → Consolidate or skip some

---

## Assembly Prompts for STEP_08

When using this pattern, answer these questions:

1. **What is the core question** all perspectives address?
2. **Why are these perspectives equal** (no hierarchy)?
3. **How do perspectives complement** each other?
4. **Where do perspectives productively disagree?**
5. **What determines which perspective is "right"** for a given reader?
6. **What synthesis emerges** from comparing all viewpoints?
7. **What meta-insight** does the conversation itself reveal?

---

## Pattern Maintenance

**Last updated:** 2026-02-15 (Pattern library creation)

**Recent examples:**
- 2025-12-27: プロンプトエンジニアリングの実践知
- 2025-12-13: コード生成 AI の限界と可能性

**Evolution notes:**
- Added "Customization Examples" section (2026-02-15)
- Future: Add more synthesis templates from real journals
- Future: Add guidance on when to include editor commentary vs let perspectives speak
