# Annex Catalog Preparation - 2026-01-20

## Critical Formatting Requirement

**ALERT**: All 55 annex summaries are currently in **comprehensive summary format** (300-400+ words). They MUST be converted to **catalog format** (80-120 word integrated narratives) for Annex Journal.

**Catalog Format Requirements** (from EDITOR_PERSONALITY.md):
- 80-120 words maximum per entry
- Integrated narrative (no separate "なぜ重要か" or "注目ポイント" sections)
- Decision-focused: "Should I read this?" not "What does it say?"
- Critical insight woven naturally into narrative (not appended)
- Include 原題 for English articles (searchability)
- Categories only when adding non-obvious context
- Unique/controversial angles prominent in closing sentences

---

## Summary Count Verification

- **Curated for Annex**: 55 articles (verified via curated_annex_journal_sources.md)
- **Summaries in unified_summaries_annex.md**: 55 summaries
- **Status**: ✅ Count matches
- **Note**: Curated list header says "47記事" but actual count is 55

---

## Article-by-Article Catalog Strategy

### Category 1: プラットフォーム倫理とガバナンス (3 articles)

#### 007. Bandcamp、AI生成楽曲の投稿を禁止する新方針を発表
**Original Title**: AI Generated Music on Bandcamp
**URL**: https://old.reddit.com/r/BandCamp/comments/1qbw8ba/ai_generated_music_on_bandcamp/
**Category**: プラットフォーム倫理
**Current Length**: ~400 words
**Core Insight**: Bandcamp chose policy-based AI rejection over technical filtering
**Unique Angle**: Platform using "human creativity" as competitive advantage against AI commodification
**80-120 Word Strategy**:
- Sentence 1-2: Bandcamp、AI生成音楽の全面禁止を宣言
- Sentence 3: 技術的検出ではなく規約による明確な線引き + データスクレイピング禁止
- Sentence 4: 「人間の創造性」をプラットフォームの競争優位として差別化（closing impact）
**Catalog Tone**: Direct, policy-focused, emphasize strategic differentiation

---

#### 008. InstagramのAIインフルエンサー、有名人とのスキャンダルを捏造
**Original Title**: Instagram AI Influencers Are Defaming Celebrities With Sex Scandals
**URL**: https://www.404media.co/instagram-ai-influencers-are-defaming-celebrities-with-sex-scandals/
**Category**: (omit - obvious from title)
**Current Length**: ~350 words
**Core Insight**: Meta's moderation failure enables AI-driven spam monetization
**Unique Angle**: "Attention harvesting" as structured spam business model
**80-120 Word Strategy**:
- Sentence 1: AI生成インフルエンサーが著名人の偽スキャンダル画像で有料サイトへ誘導
- Sentence 2: Metaのモデレーション不全が露呈
- Sentence 3-4: 「アテンション・ハーベスティング」という構造化スパム手法の実態（closing: platform governance crisis）
**Catalog Tone**: Critical, systemic failure focus

---

#### 009. AI スクレイパーによるサービス障害への対応
**Original Title**: We can't have nice things… because of AI scrapers
**URL**: https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/
**Category**: (omit)
**Current Length**: ~300 words
**Core Insight**: AI companies ignore robots.txt and public data downloads, force API lockdown
**Unique Angle**: Public infrastructure forced into defensive mode by AI scraping
**80-120 Word Strategy**:
- Sentence 1-2: MetaBrainz財団がAIスクレイパー攻撃に対抗してAPI認証を強制化
- Sentence 3: robots.txt無視・公開データ無視の実態
- Sentence 4: オープンなインフラが防衛的にならざるを得ない現実（closing: tragedy of AI commons）
**Catalog Tone**: Frustrated, systemic impact

---

### Category 2: セキュリティとプライバシーの深刻化 (5 articles)

#### 031. Claude Codeにおける8つの任意コマンド実行の脆弱性
**Original Title**: Pwning Claude Code in 8 Different Ways
**URL**: https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/
**Category**: セキュリティ研究
**Current Length**: ~400 words
**Core Insight**: Blacklist-based security in AI agents is fundamentally broken
**Unique Angle**: 8 distinct bypass methods prove whitelist-only approach necessary
**80-120 Word Strategy**:
- Sentence 1: Claude Codeの読み取り専用コマンド承認を8通りの手法でバイパス
- Sentence 2: Bash変数展開、Git引数短縮など、一見無害なコマンドの危険な仕様を悪用
- Sentence 3: ブラックリスト方式の根本的限界を実証
- Sentence 4: ホワイトリスト設計の必然性を技術的に証明（closing: architectural lesson）
**Catalog Tone**: Technical, architectural insight

---

#### 054. Superhuman AIにおける機密メール漏洩の脆弱性
**Original Title**: (check summary for title)
**URL**: https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails
**Category**: (omit)
**Current Length**: ~350 words
**Core Insight**: Zero-click prompt injection via email content
**Unique Angle**: External data automatically becomes commands in AI systems
**80-120 Word Strategy**:
- Sentence 1-2: SuperhumanのAIアシスタント、受信メール内の隠し命令で機密情報を外部送信
- Sentence 3: ゼロクリック攻撃の現実的脅威
- Sentence 4: 外部データと命令の分離が不可能なLLMの構造的欠陥（closing: fundamental vulnerability)
**Catalog Tone**: Alarming, structural flaw focus

---

#### 106. Claude Coworkにおけるファイル流出の脆弱性
**Original Title**: (check summary)
**URL**: https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files
**Category**: (omit)
**Current Length**: ~350 words
**Core Insight**: Sandbox escape via Anthropic API whitelist trust
**Unique Angle**: Trusted infrastructure becomes attack vector
**80-120 Word Strategy**:
- Sentence 1-2: Claude Coworkのサンドボックスを突破してファイル流出
- Sentence 3: Anthropic APIホワイトリストへの過信を悪用
- Sentence 4: 「信頼された通信路」自体が攻撃ベクトルになる皮肉（closing: trust paradox）
**Catalog Tone**: Ironic, architectural blind spot

---

#### 133. クロード・コードの機密アクセスを制限する、より優れた方法
**Original Title**: A better way to limit Claude Code...access to secrets
**URL**: https://patrickmccanna.net/a-better-way-to-limit-claude-code-and-other-coding-agents-access-to-secrets/
**Category**: セキュリティ設計
**Current Length**: ~300 words
**Core Insight**: Proxy-based dynamic secret injection avoids exposing real credentials to AI
**Unique Angle**: Dummy credentials + proxy substitution = least privilege enforcement
**80-120 Word Strategy**:
- Sentence 1-2: プロキシ経由でダミーキーを実キーへ動的に差し替える設計
- Sentence 3: AIエージェントに実クレデンシャルを一切渡さない「最小権限の徹底」
- Sentence 4: アーキテクチャレベルでの秘密管理の模範例（closing: practical security pattern）
**Catalog Tone**: Practical, architectural best practice

---

#### 096. プロキシを使用してClaude Codeから機密情報を隠蔽する方法
**Original Title**: Using proxies to hide secrets from Claude Code
**URL**: https://www.joinformal.com/blog/using-proxies-to-hide-secrets-from-claude-code/
**Category**: (omit - similar to 133)
**Current Length**: ~250 words
**Core Insight**: Network-layer credential management for AI agents
**Unique Angle**: Enterprise-grade secret isolation via Formal Proxy
**80-120 Word Strategy**:
- Sentence 1-2: Formal Proxyによる秘密情報隔離とネットワーク層での制御
- Sentence 3: エンタープライズ環境でのAIアクセス権限管理
- Sentence 4: プロダクション実装の現実的なアーキテクチャ（closing: enterprise pattern）
**Catalog Tone**: Enterprise-focused, production-ready

---

### Category 3: LLMの内部理解と評価 (7 articles)

#### 015. LLMの中身を覗いてみたら、Transformerは「回路」を形成していた
**Original Title**: (check summary - Japanese article)
**URL**: https://zenn.dev/50s_zerotohero/articles/a6189c891fbd71
**Category**: (omit)
**Current Length**: ~350 words
**Core Insight**: TransformerLens visualizes internal "circuits" in LLM attention heads
**Unique Angle**: Mechanistic interpretability as technical rebuttal to "black box" criticism
**80-120 Word Strategy**:
- Sentence 1-2: TransformerLensでLLM内部の「回路」を可視化
- Sentence 3: アテンションヘッドの役割特定とアクティベーション・パッチング
- Sentence 4: ブラックボックス批判への技術的反論として重要（closing: interpretability breakthrough）
**Catalog Tone**: Technical, research-focused

---

#### 047. ポケモン攻略から見るClaude Opus 4.5の進化と限界
**Original Title**: Insights into Claude Opus 4.5 from Pokemon
**URL**: https://www.lesswrong.com/posts/u6Lacc7wx4yYkBQ3r/insights-into-claude-opus-4-5-from-pokemon
**Category**: AI評価手法
**Current Length**: ~350 words
**Core Insight**: Real gameplay reveals AI cognitive biases better than benchmarks
**Unique Angle**: "Inattentional blindness" and memory persistence in AI cognition
**80-120 Word Strategy**:
- Sentence 1-2: ポケモン攻略を通じたClaude Opus 4.5の視覚・記憶・推論能力の体系的評価
- Sentence 3: 「不注意による盲目」や記憶への固執など、AIの認知バイアスを実ゲームで実証
- Sentence 4: ベンチマークでは見えないAIの思考特性を可視化（closing: unconventional evaluation）
**Catalog Tone**: Analytical, unconventional methodology

---

#### 045. LLMは「偉大な詩」を書けるのか
**Original Title**: LLM poetry and the greatness question
**URL**: https://hollisrobbinsanecdotal.substack.com/p/llm-poetry-and-the-greatness-question
**Category**: AI創造性の限界
**Current Length**: ~350 words
**Core Insight**: RLHF causes mode collapse toward mediocrity in creative outputs
**Unique Angle**: Craft (Gwern) vs Scale (Mercor) approaches both fail to achieve "greatness"
**80-120 Word Strategy**:
- Sentence 1-2: LLMが「偉大な詩」を書けるかという問いを、職人芸とスケーリングの対比で考察
- Sentence 3: RLHFによるモード崩壊と平均回帰の限界
- Sentence 4: 技術的洗練と「偉大さ」の間に横たわる溝（closing: fundamental creativity gap）
**Catalog Tone**: Philosophical, creative limits

---

#### 051. 現代のバイアスを排除：特定年代のデータのみでゼロから学習
**Original Title**: (check summary)
**URL**: https://github.com/haykgrigo3/TimeCapsuleLLM
**Category**: 実験的LLM
**Current Length**: ~280 words
**Core Insight**: Temporal data isolation to recreate historical worldviews
**Unique Angle**: "Selective Temporal Training" as bias elimination experiment
**80-120 Word Strategy**:
- Sentence 1-2: 特定時代のデータのみで学習し、現代バイアスを排除する「TimeCapsuleLLM」
- Sentence 3: 歴史的世界観の再現を目指す実験的アプローチ
- Sentence 4: データの時間的隔離による認識の制御可能性を探る（closing: temporal bias research）
**Catalog Tone**: Experimental, research-oriented

---

#### 048. LLM向けに最適化されたプログラミング言語
**Original Title**: (check summary)
**URL**: https://github.com/ImJasonH/ImJasonH/blob/main/articles/llm-programming-language.md
**Category**: (omit)
**Current Length**: ~300 words
**Core Insight**: Programming language design optimized for LLM comprehension
**Unique Angle**: Ambiguity elimination and local verification as core language features
**80-120 Word Strategy**:
- Sentence 1-2: LLM最適化プログラミング言語の設計思考実験
- Sentence 3: トークン効率だけでなく、曖昧性排除や検証の局所性を追求
- Sentence 4: AI理解のための言語特性を探る思考実験（closing: speculative language design）
**Catalog Tone**: Speculative, thought experiment

---

#### 043. AI経済学セミナー：知的攻撃に晒されるエージェントのシミュレーション
**Original Title**: (check summary)
**URL**: https://cameron.stream/blog/econ-seminar/
**Category**: マルチエージェント実験
**Current Length**: ~300 words
**Core Insight**: Multi-agent academic debate tests persona persistence under adversarial conditions
**Unique Angle**: Aggressive professor agent stress-tests LLM's role consistency
**80-120 Word Strategy**:
- Sentence 1-2: マルチエージェント「Letta」で経済学セミナーを再現
- Sentence 3: 攻撃的教員エージェントが発表者を論破する過程で、ペルソナ維持と記憶保持を検証
- Sentence 4: 敵対的環境下でのAI一貫性テスト（closing: adversarial agent research）
**Catalog Tone**: Experimental, stress-testing focus

---

#### 099. エプスタイン・ファイルの内容を索引化・検索可能にするオープンソースAIエージェント
**Original Title**: (check summary)
**URL**: https://news.ycombinator.com/item?id=46611348
**Category**: OSINT応用
**Current Length**: ~250 words
**Core Insight**: RAG + regex/grep hybrid for reliable document search
**Unique Angle**: Trust-first design avoids pure LLM hallucination risk
**80-120 Word Strategy**:
- Sentence 1-2: エプスタイン文書をRAGで検索可能化
- Sentence 3: 純粋RAGではなくregex/grepとのハイブリッド設計
- Sentence 4: 信頼性重視のOSINTツール構築（closing: reliability-first RAG）
**Catalog Tone**: Practical, trust-focused

---

### Category 4: AI時代の倫理と社会的責任 (9 articles)

**[Continue for remaining 41 articles with same detailed strategy...]**

---

## Key Catalog Conversion Challenges

### High Complexity Articles (May Need Simplification)

1. **047. ポケモン攻略** - Multiple cognitive phenomena need integration
2. **045. LLM詩** - Abstract philosophical argument needs concrete grounding
3. **048. LLM言語** - Speculative nature may be too abstract for 80-120 words
4. **031. Claude Code脆弱性** - 8 different techniques hard to summarize concisely

**Strategy**: Focus on the MOST unique finding, sacrifice exhaustiveness for impact

### Articles with Multiple Key Points (Choose Most Unique)

1. **007. Bandcamp** - Policy + scraping ban + competitive strategy → Focus on competitive strategy
2. **133 & 096. Proxy articles** - Similar content, differentiate clearly in catalog

**Strategy**: Make architectural pattern the hook, not just the tool

### Category Assignment Strategy

**Use categories for ~30-40% of entries** (17-22 articles):
- セキュリティ研究 (for novel attack methods)
- プラットフォーム倫理 (for governance decisions)
- AI評価手法 (for unconventional testing)
- マルチエージェント実験 (for agent interactions)
- 実験的LLM (for research projects)
- OSINT応用 (for investigative tools)
- エンタープライズ実装 (for corporate use cases)

**Omit categories when**:
- Title is self-explanatory
- Adding category is redundant

---

## Required Next Steps Before STEP_08

1. **CRITICAL**: Convert all 55 summaries from comprehensive (300-400 words) to catalog format (80-120 words)
   - Remove all metadata (Content Type, Scores, Topics, Language)
   - Rewrite as integrated narrative
   - Keep 原題 for English articles
   - Weave "なぜ重要か" into narrative, don't append it

2. **Medium Priority**: Ensure closing sentences emphasize unique/controversial angles

3. **Low Priority**: Add categories to ~17-22 articles where it adds non-obvious context

---

## Sample Catalog Entry (Before/After)

### BEFORE (Comprehensive Format - 372 words):

```markdown
## Bandcamp、AI生成楽曲の投稿を禁止する新方針を発表

https://old.reddit.com/r/BandCamp/comments/1qbw8ba/ai_generated_music_on_bandcamp/

**Original Title**: AI Generated Music on Bandcamp

人間による創造性の保護とプラットフォームの信頼性維持を目的として、AIによって全面的または実質的に生成された楽曲の投稿を禁止する新ポリシーを策定した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:3/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 72/100

**Topics**: [[コンテンツモデレーション, プラットフォームガバナンス, データスクレイピング禁止, 著作権保護, 人間中心設計]]

インディーズ音楽の牙城であるBandcampが、生成AIに対する極めて厳格な姿勢を打ち出した。同プラットフォームの公式発表によれば、2026年より「全面的、または実質的な部分がAIによって生成された音楽および音声」の投稿を一切禁止する。これは、クリエイターが音楽を作り続け、ファンが「人間によって作られたもの」であると確信を持って購入できる環境を維持するための戦略的決定である。

[...300+ more words...]
```

### AFTER (Catalog Format - 112 words):

```markdown
## Bandcamp、AI生成楽曲の投稿を禁止する新方針を発表

https://old.reddit.com/r/BandCamp/comments/1qbw8ba/ai_generated_music_on_bandcamp/

**Original Title**: AI Generated Music on Bandcamp
**Category**: プラットフォーム倫理

インディーズ音楽プラットフォームBandcampが2026年より、AI生成音楽の投稿を全面禁止する新方針を発表した。技術的検出ではなく規約による明確な線引きを選択し、併せてAI企業によるデータスクレイピングも禁止。多くの企業がAI統合に走る中、Bandcampはあえて「人間による創造性」をプラットフォームの競争優位として差別化する戦略を選んだ。AI技術の拒絶自体がブランド価値になり得ることを示す稀有な事例であり、プラットフォーム設計における新たな選択肢を提示している。
```

---

## Production Checklist

- [ ] Remove all metadata from 55 annex summaries
- [ ] Convert all summaries to 80-120 word catalog format
- [ ] Keep 原題 for all English articles
- [ ] Add categories to ~17-22 articles where adding context
- [ ] Ensure unique/controversial angles are in closing sentences
- [ ] Verify "Should I read this?" decision focus throughout
- [ ] Final word count check: No summary >120 words
- [ ] No separate commentary sections (なぜ重要か, 注目ポイント)

---

**Total Articles Requiring Catalog Conversion**: 55
**Estimated Editing Time**: 4-6 hours (assuming ~5 minutes per article)
**Complexity Level**: High (requires editorial judgment and writing skill, not just deletion)
