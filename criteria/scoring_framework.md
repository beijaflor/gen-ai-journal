# Link Scoring Framework

## Purpose

This framework provides objective criteria for scoring articles during summarization to support systematic curation decisions. Each article receives scores across 5 dimensions and 3 composite scores to guide inclusion in main journal or annex.

## Scoring Methodology

### 5 Core Dimensions (0-5 scale each)

#### 1. Signal Quality (信号品質)
**What it measures**: Source credibility, evidence basis, and information purity

**Scoring Guide**:
- **5**: Primary source (official announcements, first-party research, original author)
- **4**: High-quality secondary source with original analysis or direct attribution
- **3**: Reliable secondary source with proper sourcing and fact-checking
- **2**: Secondary source with some gaps in attribution or minor credibility issues
- **1**: Tertiary source, significant credibility concerns, or heavy reliance on speculation
- **0**: Unreliable source, misinformation, or pure speculation

**Examples**:
- 5: OpenAI official blog post about GPT-4 features
- 4: Thoughtful analysis by respected developer with clear methodology
- 3: Tech journalist article with proper source attribution
- 2: Blog post with some unsourced claims but generally reliable
- 1: Social media thread with interesting ideas but no backing
- 0: Marketing content disguised as journalism

#### 2. Technical Depth (技術的深度)
**What it measures**: Level of technical insight, architectural thinking, and first-principles analysis

**Scoring Guide**:
- **5**: Deep architectural insight, trade-off analysis, first principles reasoning
- **4**: Solid technical understanding with good depth and practical considerations
- **3**: Competent technical content with some depth and useful details
- **2**: Basic technical explanation with limited depth
- **1**: Surface-level technical content, mostly descriptive
- **0**: No meaningful technical content or technically incorrect

**Examples**:
- 5: Analysis of LLM architectural trade-offs with performance implications
- 4: Deep dive into AI tool integration patterns with workflow considerations
- 3: Technical tutorial with good explanation of underlying concepts
- 2: Basic how-to guide with limited technical context
- 1: High-level overview with buzzword usage
- 0: Marketing speak with no technical substance

#### 3. Uniqueness (独自性)
**What it measures**: Novel perspectives, non-obvious insights, and original thinking

**Scoring Guide**:
- **5**: Genuinely novel perspective or contrarian view that challenges conventional wisdom
- **4**: Fresh angle on known topic with significant new insights
- **3**: Solid original thinking with some new perspectives
- **2**: Mostly familiar ideas with minor new angles
- **1**: Common knowledge with slight variations
- **0**: Completely derivative content with no original thought

**Examples**:
- 5: "AI output is rude to show people" - novel etiquette perspective
- 4: "AI hype analysis" - contrarian view of industry discourse
- 3: Unique approach to implementing a common AI pattern
- 2: Personal experience with widely-used tools
- 1: Standard tutorial on well-known topics
- 0: Regurgitation of press releases

#### 4. Practical Value (実用的価値)
**What it measures**: Actionability, relevance to working engineers, and immediate applicability

**Scoring Guide**:
- **5**: Immediately actionable with high impact on daily development work
- **4**: Clearly actionable with significant practical benefits
- **3**: Useful guidance with moderate practical application
- **2**: Some practical value but limited immediate applicability
- **1**: Minimal practical relevance to working developers
- **0**: No practical value or actively misleading guidance

**Examples**:
- 5: Step-by-step guide for integrating AI tool into existing workflow
- 4: Best practices for AI code review with specific implementation tips
- 3: Analysis of tool performance with selection guidance
- 2: General principles that require adaptation for practical use
- 1: Theoretical discussion with distant practical implications
- 0: Abstract concepts with no implementation path

#### 5. Anti-Hype (ハイプ対策)
**What it measures**: Resistance to marketing influence, realistic claims, and substance over promotion

**Scoring Guide**:
- **5**: Strong resistance to hype, realistic assessment, evidence-based claims
- **4**: Generally realistic with minor promotional elements
- **3**: Balanced perspective with some hype but mostly substantial
- **2**: Noticeable hype elements but still contains substance
- **1**: Heavy promotional content with limited substance
- **0**: Pure hype, marketing disguised as content, unrealistic claims

**Examples**:
- 5: Critical analysis of AI limitations with realistic expectations
- 4: Honest tool review acknowledging both benefits and drawbacks
- 3: Enthusiastic but balanced coverage of new technology
- 2: Promotional but includes useful technical information
- 1: Marketing-heavy content with some technical details
- 0: Pure vendor marketing with no objective analysis

## Content Type Specific Weightings

### Main Journal Score Calculation

| Content Type | Signal | Depth | Unique | Practical | Anti-Hype |
|--------------|--------|-------|---------|-----------|-----------|
| 📰 News | 40% | 10% | 20% | 30% | 30% |
| 🔬 Research | 30% | 40% | 30% | 20% | 20% |
| 📖 Tutorial | 20% | 30% | 20% | 50% | 10% |
| 💭 Opinion | 20% | 30% | 40% | 20% | 30% |
| 🛠️ Technical | 30% | 35% | 25% | 30% | 15% |
| 📊 Industry | 35% | 15% | 25% | 25% | 25% |
| ⚙️ Tools | 25% | 30% | 30% | 40% | 15% |
| 🎭 AI Hype | 25% | 20% | 30% | 15% | 50% |
| 🤝 AI Etiquette | 25% | 30% | 40% | 30% | 20% |

### Annex Potential Score Calculation

| Content Type | Signal | Depth | Unique | Practical | Anti-Hype |
|--------------|--------|-------|---------|-----------|-----------|
| 📰 News | 25% | 15% | 35% | 25% | 35% |
| 🔬 Research | 25% | 35% | 40% | 15% | 25% |
| 📖 Tutorial | 15% | 25% | 40% | 35% | 15% |
| 💭 Opinion | 15% | 25% | 50% | 15% | 35% |
| 🛠️ Technical | 20% | 30% | 40% | 25% | 20% |
| 📊 Industry | 25% | 15% | 40% | 20% | 30% |
| ⚙️ Tools | 20% | 25% | 45% | 25% | 20% |
| 🎭 AI Hype | 20% | 15% | 35% | 10% | 55% |
| 🤝 AI Etiquette | 20% | 25% | 50% | 20% | 25% |

### Overall Quality Score
Simple average of all 5 dimensions × 20

## Decision Thresholds

### Main Journal Inclusion
- **80-100**: Essential - Must include, fits perfectly with journal goals
- **65-79**: Strong candidate - Very likely to include, high quality content
- **50-64**: Consider - Evaluate against weekly theme and available space
- **35-49**: Weak candidate - Unlikely unless exceptional thematic fit
- **0-34**: Reject - Do not include in main journal

### Annex Journal Consideration
- **70-100**: Strong annex candidate - High potential for annex inclusion
- **50-69**: Possible annex inclusion - Consider for annex if main journal rejected
- **0-49**: Not suitable for annex - Does not meet annex criteria

### Quality Assurance Guidelines

#### Score Validation Examples

**High-Quality Examples (from existing summaries)**:

**AI Hype Article (hidde.blog/ai-hype/)**:
- Signal: 5 (original analysis, first-party perspective)
- Depth: 3 (conceptual analysis, not deeply technical)
- Unique: 5 (contrarian view against AI hype)
- Practical: 4 (helps engineers avoid hype traps)
- Anti-Hype: 5 (literally about combating hype)
- **Expected Main Score**: ~85 (AI Hype weighted)
- **Expected Annex Score**: ~80

**AI Etiquette Article (distantprovince.by)**:
- Signal: 5 (thoughtful original analysis)
- Depth: 4 (UX/design implications clearly articulated)
- Unique: 5 (novel perspective on AI output sharing)
- Practical: 4 (direct implications for product design)
- Anti-Hype: 4 (realistic view of AI content value)
- **Expected Main Score**: ~88 (AI Etiquette weighted)
- **Expected Annex Score**: ~85

#### Consistency Checks
- **Cross-Type Comparison**: Similar quality articles should score within 10 points regardless of type
- **Threshold Validation**: Score should align with editorial intuition about inclusion
- **Hype Detection**: Articles with Anti-Hype scores below 3 should be scrutinized carefully

## Integration with Curation Workflow

### During Summarization (STEP_01)
1. Apply scoring framework during summary generation
2. Include scores in summary output for later reference
3. Flag articles with extreme scores (very high or very low)

### During Curation (STEP_04)
1. Use scores as starting point for inclusion decisions
2. Consider weekly theme and narrative coherence
3. Balance content type distribution
4. Apply final editorial judgment

### Quality Control
- Review score distribution across weekly batch
- Adjust thresholds if needed based on content quality patterns
- Maintain consistency across weekly iterations