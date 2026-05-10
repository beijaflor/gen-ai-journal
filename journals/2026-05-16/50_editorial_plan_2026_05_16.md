# Editorial Plan - Journal 2026-05-16

## Planning Status
- [x] Initial theme identification (AI-assisted, hybrid version)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Organizing Principle (Hybrid)

This plan combines two angles:
- **Topic-cluster integrity** (from the original draft): keeps Agent Skills as a dedicated theme, keeps platform announcements together, keeps a standalone "industry/migration" theme.
- **Decision-oriented sharpness** (from the alt draft): promotes token economics to a top-level theme; merges validation+security as "evidence-based verification"; surfaces "delegation boundary" as its own theme spanning critical pieces.

Net result: 7 themes, ~48 candidate articles → STEP_04 will trim to 18-25 main, rest to annex.

---

## Identified Themes

### Theme 1: Addy Osmani・Perplexity・技術評論社が示すAgent Skills設計原則

**Articles (IDs):** 003, 013, 020, 064, 118, 155

**Theme Introduction (2-3 sentences in Japanese):**
今週はAgent Skillsの設計論が一気に体系化された週となった。Addy OsmaniとPerplexityがそれぞれ独立に設計原則を公開し、Makefile形式の代替仕様、依存関係を扱うローカルCLI、既存コードからの抽出ワークフロー、そして技術評論社からの公式入門書まで、設計・運用・配布・教育が同時並行で立ち上がった。

**Editorial Notes:**
- 003: Addy Osmani Agent Skills — プロセス重視・反正当化テーブル・段階的開示・スコープ規律の5原則
- 013: Perplexity Designing Skills — 「Zen of Skills」、3階層構造、「Load when...」、評価セット重視
- 020: SKILL.mk — Makefile形式での依存関係表現、トークン85%削減
- 064: 既存コードからAgent Skills抽出 — skill-creatorによるレガシー資産のスキル化
- 118: sklock — ローカルでのスキル依存関係管理CLI、lockfile/グラフ可視化
- 155: 技術評論社『Claude Codeで学ぶAgent Skills入門』— 日本初の体系的解説書

---

### Theme 2: DeepSeek V4・GitHub・Claude Code WebFetchで見える実質トークンコスト

**Articles (IDs):** 099, 117, 130, 063, 068, 019

**Theme Introduction (2-3 sentences in Japanese):**
トークン消費と価格構造、そしてエージェント内部の処理経路が、今週は具体的な数値で語られている。DeepSeek V4のキャッシュヒット時の極端な低価格、GitHubが自社運用で達成した62%削減、VSCode 1.118のキャッシュ利用率93%、Claude CodeのWebFetchが裏でHaiku要約を挟んでいるという仕様暴露は、いずれも「実質トークンコスト」と「裏で何が動いているか」という共通指標で読み解ける。

**Editorial Notes:**
- 099: DeepSeek V4 1786倍 — キャッシュヒット時のClaude Opus比1786倍コスト差の試算
- 117: DeepSeek V4 公式pricing — 1Mトークンcontextと特別価格の一次情報
- 130: GitHub Agentic Workflows 62%削減 — APIプロキシ計測、CLI代替、Effective Tokens（👍）
- 063: VSCode 1.118 — Copilotサブエージェント分離、Chronicle、キャッシュ93%
- 068: Claude Code WebFetch — Haikuが裏で要約していた挙動と切り捨て仕様
- 019: Simon Willison DeepSeek V4 — フロンティア性能と低価格の分析

---

### Theme 3: Kimi K2.6・Gemma 4・antirez ds4が押し上げるローカル実行のフロンティア性能

**Articles (IDs):** 029, 084, 097, 141, 160, 148, 007

**Theme Introduction (2-3 sentences in Japanese):**
クラウドAPIに依存しないモデル選択肢が、性能と実装の両面で具体性を増した週である。中国Moonshot AIのKimi K2.6がプログラミング競技でGPT-5.5・Claude・Geminiを破り、Gemma 4は日本語性能とMTPによる3倍高速化を両立、SubQはサブクアドラティック構造で100万トークンを線形処理、antirez氏はApple Silicon特化の推論エンジンを公開した。

**Editorial Notes:**
- 029: Kimi K2.6 — プログラミング競技でフロンティアモデルを上回るオープンウェイトモデル
- 084: Gemma 4シリーズ — 31B/26B/E4B/E2B、日本語能力、MCP対応
- 097: Gemma 4 MTP — Multi-Token Predictionで3倍高速化
- 141: antirez ds4 — Apple Silicon Metal特化のDeepSeek V4 Flash推論エンジン
- 160: SubQ — 初のフル・サブクアドラティックLLM、100万トークン線形処理
- 148: Gemma 4ファインチューニング — Colab+LoRA+Unslothで20分FT
- 007: O'Reilly Local AI — ローカル実行の現状とフロンティア性能差の縮小

---

### Theme 4: Linear・Anthropic・Stripeが進めるエージェント業務基盤の標準装備化

**Articles (IDs):** 153, 002, 062, 055, 158, 053, 152

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントを「使える場所」がアプリ単体から業務基盤全体へ広がった一週間。AnthropicのDreaming/Outcomes/Multiagent Orchestration、Linearの「Issue tracking is dead」宣言、StripeのMPP/Tempo/Link Agent Wallets、Supabase公式ChatGPTアプリ、GPT-5.5 Instantのハルシネーション50%削減、Anthropicの金融エージェント、MUFG×Google AP2が相次いだ。

**Editorial Notes:**
- 153: Claude Managed Agents — Dreaming/Outcomes/Multiagent Orchestration
- 002: Linear — Issue tracking is dead宣言、Linear Agent/Skills/Coding Agent統合
- 062: Stripe Sessions 2026 — MPP/Tempo/Link Agent Wallets、AIエージェント決済OS
- 055: GPT-5.5 Instant — ハルシネーション52.5%削減、メモリソース機能
- 158: Supabase公式ChatGPTアプリ — 29種類のツールでDB/Edge Functions操作
- 053: Anthropic金融エージェント — 10種テンプレート、Microsoft 365統合、Opus 4.7 64.37%
- 152: MUFG×Google AP2/A2A — 自律型金融サービスPoC

---

### Theme 5: GitHub Dominator・OWASP Juice Shop・SPECAが示すエージェント動作の証拠ベース検証

**Articles (IDs):** 105, 121, 093, 145, 140, 157

**Theme Introduction (2-3 sentences in Japanese):**
非決定的なエージェントが「成功した」と報告したとき、それを何で確かめるか。GitHubはドミネータ分析で自己評価82.2%に対し精度100%を達成、Claude Code内蔵スキャンはOWASP Juice ShopでCritical級を80%以上検出、SPECAは仕様書からの監査でSherlockコンテストの新規バグ4件を発見した。Plan Mode盲信の回避手法、決定論的制御フロー論、ツールレジストリ構築論も同じ問題系に並ぶ。

**Editorial Notes:**
- 105: GitHub Dominator分析 — グラフ理論で必須通過点抽出、自己評価82.2%→100%
- 121: Claude security scan + OWASP Juice Shop — Critical級80%以上検出（👍、リード候補）
- 093: SPECA — 仕様書からの証明試行型監査、Sherlockで4件の新規バグ発見
- 145: AIのPlan Mode盲信しない — 既存情報から条件候補抽出、4観点レビュー
- 140: Agents need control flow — プロンプトではなくコードで決定論的制御
- 157: O'Reilly AIツールレジストリ — 88%が経験するエージェントセキュリティ事故

---

### Theme 6: Uncle Bob・Addy Osmani・Simon Willisonが問うAIコーディング委譲の認知コスト

**Articles (IDs):** 032, 057, 115, 039, 149, 051, 045

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントへの委譲をどこで止めるかという議論が、複数の論者から独立に提示された週である。Uncle Bobの「終わった」宣言、Addy Osmaniの「認知放棄」、Simon WillisonのVibe coding境界曖昧化への懸念、larsfaye氏の監視のパラドックス、川島氏の認知負債、idiallo氏の「DBを消したのはAIではない」、Ricky Yean氏のタスク開始時の意志論は、それぞれ立場が異なるものの、「人間の理解と責任の所在」という共通の論点を扱っている。

**Editorial Notes:**
- 032: Uncle Bob "It's over" — Vibe Coding時代到来宣言とコミュニティ反応
- 057: Cognitive Surrender (Addy Osmani) — オフロードとサレンダーの違い、理解の負債
- 115: Simon Willison — Vibe codingとAgentic engineeringの境界消失への懸念
- 039: Agentic Coding is a Trap — 監視のパラドックス、スキル萎縮、ベンダーロックイン
- 149: 認知負債 (川島) — 技術負債・認知負債・意図負債の3層整理
- 051: idiallo / DBを消したのは — ツール責任転嫁批判、ガードレール設計責任
- 045: What do we lose when AI does our work — タスク開始時の意志の投資

---

### Theme 7: Atlantic・GPU担保融資・「Claude Is Dead」が突きつけるAI業界の収益性と移行先選択

**Articles (IDs):** 043, 035, 033, 144, 067, 122, 070, 113, 127

**Theme Introduction (2-3 sentences in Japanese):**
AI業界の収益・負債・信頼性の議論と、開発者側の移行先選択が同時期に並んだ週である。AtlanticはAnthropicの収益急増を根拠に「もうバブルではないかもしれない」と論じ、一方でGPU担保融資の構造リスクや「Claude Is Dead」性能劣化批判も並んだ。Codex入門・OpenCode Goといった移行先の具体的な選択肢、OpenClawの不安定化謝罪、OpenAI会長の法廷証言、Grokのユーザー減も、「AIサービスの信頼性をどう評価するか」という同じ文脈で読める。

**Editorial Notes:**
- 043: Javier Tordable「Claude Is Dead」— レート制限・推論能力低下批判
- 035: The Atlantic — Maybe AI Isn't a Bubble After All（Anthropic収益）
- 033: AIインフラ金融バブル — GPU担保融資と2026年の負債の壁
- 144: OpenClaw rough week — 一週間の混乱とLTS版への舵切り
- 067: Claude Code → Codex入門 — 移行ガイド、permissionモードの違い
- 122: OpenCode Go + pi-coding-agent — 月10ドルでDeepSeek V4 Pro/Kimi K2.6
- 070: AIと資本主義 — 100兆円投資と倫理崩壊の構造
- 113: OpenAI会長グレッグ・ブロックマンが法廷で日記朗読
- 127: Grokユーザー減少、Claude/Geminiとの差拡大

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週はAgent Skillsの設計論が一気に体系化された。Addy OsmaniとPerplexityがそれぞれ独立に5原則と「Zen of Skills」を公開し、SKILL.mkがMakefile形式でトークン85%削減を実証、sklockがローカル依存管理を、既存コード抽出が暗黙知の言語化を、そして技術評論社からの公式入門書が日本語の体系的リファレンスを提供した。設計・運用・配布・教育の四方向が同じ週に揃ったのは初めてに近い。

トークンと内部挙動の数値化も鮮明になった。DeepSeek V4はキャッシュヒット時にClaude Opusの1786分の1という極端な低価格を提示し、GitHubは自社運用で62%削減、VSCode 1.118はキャッシュ利用率93%以上、そしてClaude CodeのWebFetchが裏でHaikuに要約させていた挙動も明らかになった。モデル側ではKimi K2.6がプログラミング競技でGPT-5.5やClaudeを破り、Gemma 4が日本語性能とMTPによる3倍高速化を両立、SubQはサブクアドラティック構造で100万トークン線形処理を達成、antirez氏はApple Silicon特化の推論エンジンを公開した。クラウドAPIに依存しない選択肢が、性能・コスト・実装の三方向で実用ラインに到達している。

プラットフォーム側ではClaude Managed AgentsのDreaming/Outcomes、Linearの「Issue tracking is dead」宣言、StripeのMPP発表、Supabase公式ChatGPTアプリ、GPT-5.5 Instantが相次ぎ、エージェントが「使える場所」が業務基盤全体へ広がった。検証面ではGitHubがドミネータ分析でエージェント検証を100%精度に到達させ、Claude Code内蔵スキャンはOWASP Juice ShopでCritical級80%以上を検出、SPECAは仕様書からの監査で新規バグ4件を発見した。

「コードを書くこと」自体への問い直しも続いている。Uncle Bobの「It's over」宣言、Simon WillisonによるVibe codingとAgentic engineeringの境界消失観察、Addy Osmaniの認知放棄論、larsfaye氏の監視のパラドックス、川島氏の認知負債が同時期に並んだ。一方でAtlantic「もうバブルではない」論とGPU担保融資の負債の壁、「Claude Is Dead」批判、Codex/OpenCode Goへの移行ガイドが揃い、AI業界の収益・信頼性と開発者の移行先選択が同じ文脈で語られた週でもある。

---

## Curation Signal Summary

**⭐ Standout Articles Used:** 該当なし（Supabase上で標準フラグ未設定）

**👍 Upvoted Articles Used:**
- 121 → Theme 5 (Lead候補) — OWASP Juice Shopでの検証
- 130 → Theme 2 (Lead候補) — 62%削減
- 059 (Playwright CLI) → Annex候補（テーマに合致せず）

**👎 Downvoted Articles:**
- 037 deepclaude → Annex候補（031補足案も検討）
- 018 Governor for Claude Code → Annex候補
- 071 OpenCode + Gemma 4 → Annex（122・094で代替）
- 074 SKILL.md整理ノート → Annex候補
- 131 AIエージェントPRレビュー → Theme 5またはAnnex（短く扱う）

**Omitted Articles:** Supabaseで明示的omit指定なし

---

## Theme Coverage Summary

| Theme | Articles | Count |
|-------|----------|-------|
| 1. Addy Osmani・Perplexity・SKILL.mk・sklock・公式入門書 | 003, 013, 020, 064, 118, 155 | 6 |
| 2. DeepSeek V4 1786倍・GitHub 62%削減・VSCode 93%・WebFetch裏Haiku | 099, 117, 130, 063, 068, 019 | 6 |
| 3. Kimi K2.6・Gemma 4 MTP・SubQ・antirez ds4 | 029, 084, 097, 141, 160, 148, 007 | 7 |
| 4. Claude Managed Agents・Linear・Stripe MPP・Supabase ChatGPT・GPT-5.5 Instant | 153, 002, 062, 055, 158, 053, 152 | 7 |
| 5. GitHub Dominator・OWASP Juice Shop・SPECA | 105, 121, 093, 145, 140, 157 | 6 |
| 6. Uncle Bob・Cognitive Surrender・Vibe coding境界・認知負債・DBを消したのは | 032, 057, 115, 039, 149, 051, 045 | 7 |
| 7. Claude Is Dead・Atlantic Bubble・GPU負債の壁・OpenClaw・Codex/OpenCode Go移行 | 043, 035, 033, 144, 067, 122, 070, 113, 127 | 9 |

**Total Planned for Main:** 49 article slots → STEP_04で18-25に絞り込み
**Remaining for Annex:** Supabaseフラグ済み32件 + 残り

*Note: Themes 3, 5, 6, 7 have multiple candidates. STEP_04でleadと2-3 supportingに絞り、残りはannex候補またはomit。*

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-05-10
**Reviewer:** beijaflor

**Changes Made:**
- Theme 5: removed article #136 (Mozilla Firefox 271件) — moved to annex; refined title and intro accordingly
- All 7 theme titles iterated through 5 rounds before settling on the "[named anchors] [verb] [substantive topic phrase]" pattern
- Guidance captured back into STEP_03b_PLAN_THEMES.md for future journals

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal) — done, 24 articles
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## Assembly Strategies (STEP_07)

#### Assembly Strategy (STEP_07) - Theme 1

**Pattern:** Multi-Perspective

**Rationale:** 4本の記事はいずれも独立した著者・媒体がAgent Skillsの設計論を提示しており、明確な「lead」となる一次発表は存在しない。Addy Osmaniは規律論、Perplexityは社内運用論、SKILL.mkは記法仕様、技術評論社書籍は教育用入門という、いずれも対等な立場からの貢献である。Single-Focusを選ぶと公式announcementの不在で構造が破綻し、Progressive-Sequenceを当てはめると「依存関係」を捏造することになるためMulti-Perspectiveが最も誠実。

**Article Order & Role:**
1. [003] Addy Osmani Agent Skills — **Peer (規律フレーム)**: 5原則（プロセス重視・反正当化・段階的開示・スコープ規律など）を最も汎用的・抽象的に提示しており、読者の入り口として機能する
2. [013] Perplexity Designing Skills — **Peer (運用知)**: 自社プロダクションでの運用から得た「Zen of Skills」「3階層構造」「評価セット」と、抽象論からスケールする現場知を提供
3. [020] SKILL.mk — **Peer (記法選択肢)**: Markdown規範に対するMakefile形式という代替仕様を提示し、設計原則がフォーマット選択にどう波及するかを示す
4. [155] 技術評論社『Claude Codeで学ぶ Agent Skills入門』— **Peer (体系化・日本語化)**: 設計論を日本語の体系的リファレンスへ落とし込んだ位置づけ

**Narrative Arc:**
- Opening question: Agent Skillsを設計する際、どの粒度・どの形式・どの評価軸で記述するべきか
- Progression: 規律原則 → 運用での洗練 → 記法の選択肢 → 教育的体系化（複雑性の段階的展開だが、依存関係はない）
- Key synthesis: 4本に共通するのは「段階的開示によるトークン効率」と「明示的な呼び出し条件」。設計原則が独立に収束した点が重要

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 003 | 013 | Additive | 別の角度から、Perplexityは自社運用の現場知として近い結論に到達している |
| 013 | 020 | Contextual | 設計原則を踏まえると、記述フォーマット自体の選択も論点になる |
| 020 | 155 | Building | これらの設計論を日本語で体系的に学ぶための土台も整った |

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (5原則・3階層構造・Makefile DAG・段階的開示の具体)
- Business impact: ⭐⭐ (トークン85%削減という運用コスト指標)
- Future implications: ⭐⭐ (設計原則の収束が示す標準化の方向)

**Key Synthesis Points:**
1. Addy OsmaniとPerplexityが独立に「段階的開示」「明示的な呼び出し条件」に到達している
2. Markdown対Makefileという記法論争の背後に、依存関係をどう表現するかという共通課題がある
3. 評価セット重視（Perplexity）と反正当化テーブル（Osmani）はいずれも「エージェントの逸脱を構造で抑える」発想
4. 日本語の体系的入門書の登場は、設計論が論文・ブログから書籍化される段階に達したことを示す

**Conclusion Approach:** 4本の独立した提案が同じ設計課題に収束した事実を強調し、読者には「自分のチームの制約条件に合わせて原則を選び直すこと」を促す。

**Assembly Prompts for STEP_08:**
1. 4つの視点が「同じ問題に独立に」到達した点をどう示すか？
2. 各ソースの貢献領域（規律・運用・記法・教育）をどう区別して紹介するか？
3. 段階的開示・呼び出し条件・評価セットという共通語彙をどう統合的に提示するか？
4. 読者が自分の文脈で原則を取捨選択するための判断軸をどう与えるか？
5. SKILL.mkの記法提案を、メインライン（Markdown）に対する選択肢として公平に扱えているか？

---

#### Assembly Strategy (STEP_07) - Theme 2

**Pattern:** Multi-Perspective

**Rationale:** 3本の記事はいずれも「実質トークンコスト」「裏で何が動いているか」を別の角度から数値で開示している独立した観察である。GitHub（自社運用62%削減）、DeepSeek（API価格1786倍差）、Claude Code WebFetch（Haiku要約による情報切り捨て）は、序列化できる関係ではない。Progressive-Sequenceを当てはめると「因果」を捏造することになり、Single-Focusの主役不在もあるためMulti-Perspectiveが妥当。

**Article Order & Role:**
1. [130] GitHub Agentic Workflows 62%削減 — **Peer (運用最適化視点)**: APIプロキシ計測・Effective Tokens指標・MCPツール整理という、自社運用で獲得した方法論を提示
2. [099] DeepSeek V4 1786倍 — **Peer (価格構造視点)**: キャッシュヒット時のコスト差を数値化し、プロンプト配置によるキャッシュ最大化手法を解説
3. [068] Claude Code WebFetch — **Peer (内部挙動視点)**: ユーザーから見えない裏のHaiku要約と切り捨て仕様を暴露し、「実質的に何が読まれているか」を問う

**Narrative Arc:**
- Opening question: 公称トークン数とAPIの請求書、そしてエージェントの内部動作の間にあるギャップをどう測るか
- Progression: 自社運用の最適化 → モデル側の価格構造 → ツール内部の不可視動作（測定の対象が外側から内側へ移る）
- Key synthesis: 「表示されるトークン」と「実質的に処理されているトークン」が乖離している、という共通の発見

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 130 | 099 | Contextual | 計測手法に続いて、モデル側の価格構造そのものを精査した分析を見ていく |
| 099 | 068 | Contrasting | 価格と請求は数値で見えるが、エージェントの内部処理は数値化されにくい |

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (Effective Tokens定義、KVキャッシュ仕組み、Haiku要約パイプライン)
- Business impact: ⭐⭐⭐ (62%削減・1786倍差という具体的なコスト指標)
- Future implications: ⭐⭐ (実質コスト指標の標準化が必要という暗黙の問題提起)

**Key Synthesis Points:**
1. 「Effective Tokens」「キャッシュヒット率」「内部要約による情報損失」はいずれも公称価格表からは読み取れない指標
2. 自社測定（GitHub）と公開価格（DeepSeek）と挙動暴露（WebFetch）が組み合わさって「実質コスト」の輪郭が見える
3. キャッシュ最適化のプロンプト配置（静的を先頭に）は、ベンダー横断で通用する手法として浮上
4. WebFetchの仕様暴露は、エージェントの「ブラックボックス化」がコスト・精度の双方に影を落とすことを示す

**Conclusion Approach:** 3つの観察を統合し、「公称トークン価格」だけでコスト評価する時代が終わりつつあることを指摘。読者には自分のワークフローで内部挙動を測定する具体策を促す。

**Assembly Prompts for STEP_08:**
1. 3つの異なる測定対象（運用・価格・内部挙動）をどう一つの「実質コスト」フレームに束ねるか？
2. 数値（62%、1786倍）を主張のために使うのか、文脈の中で読ませるのか？
3. 序列化を避けながら、3本の発見が補完的であることをどう伝えるか？
4. 読者が自分のスタックで実践できる第一歩をどう提示するか？

---

#### Assembly Strategy (STEP_07) - Theme 3

**Pattern:** Multi-Perspective

**Rationale:** 4本はいずれも「クラウドAPIに依存しない選択肢」のフロンティアを別の方向から押し上げている。Kimi K2.6（オープンウェイトの競技性能）、Gemma 4（日本語性能と速度両立）、antirez ds4（Apple Silicon特化推論）、SubQ（線形スケーリング新アーキテクチャ）は、技術的な前提も達成内容も異なる。Progressive-Sequenceは「歴史的進化」を要求するが、これらは同時並行の独立した進展なのでMulti-Perspectiveが適切。

**Article Order & Role:**
1. [029] Kimi K2.6 — **Peer (競技性能視点)**: オープンウェイトモデルがフロンティア商用モデルを破ったという最も話題性の高い結果。読者の入り口として機能
2. [084] Gemma 4 — **Peer (実用性能視点)**: 日本語ネイティブ品質・MTPによる高速化・MCP対応というユーザー視点での実用ライン到達
3. [141] antirez ds4 — **Peer (実装視点)**: 推論エンジン側の最適化（Apple Silicon Metal特化、独自2bit量子化、Disk KV Cache）。モデルではなくランタイムの貢献
4. [160] SubQ — **Peer (アーキテクチャ視点)**: Transformer二乗計算量を打破するサブクアドラティック構造で、長コンテキスト処理の前提を変える

**Narrative Arc:**
- Opening question: ローカル/オープンの選択肢は、性能・コスト・実装のどの軸でフロンティアに追いついているのか
- Progression: ベンチマーク → 実用品質 → 実装最適化 → アーキテクチャ刷新（粒度を変えながらの並列観察）
- Key synthesis: 4方向の進展が同時に起きており、ローカル実行の制約は単一のボトルネックではなくなった

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 029 | 084 | Additive | ベンチマークでの勝利だけでなく、日常利用品質でも実用ラインに到達したモデルがある |
| 084 | 141 | Contextual | モデル側の進歩と並んで、推論ランタイム自体を作り直す動きも出てきた |
| 141 | 160 | Building | 実装最適化の延長で、計算量そのものの前提を変えるアーキテクチャ提案も登場している |

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (MoE 2bit量子化、MTP、サブクアドラティック構造)
- Business impact: ⭐⭐ (クラウドAPI依存からの解放という選択肢拡大)
- Future implications: ⭐⭐⭐ (アーキテクチャ・ランタイム・モデルの三層が同時に動く意味)

**Key Synthesis Points:**
1. 性能（Kimi K2.6）・実用品質（Gemma 4）・実装最適化（ds4）・アーキテクチャ（SubQ）の4軸が同時並行で進んでいる
2. オープンウェイト×特化推論×新アーキテクチャの組み合わせで、ローカル実行のフロンティア距離が急速に縮まっている
3. SubQの線形スケーリングは、RAG/チャンキングという従来回避策の前提を揺るがす
4. antirez ds4が示すように、特定モデル特化の最適化はllama.cppの汎用主義とは別の道を切り開く

**Conclusion Approach:** 4つの独立した進展を並列に提示し、それぞれが補完的であることを示す。読者には自分のユースケース（速度優先、品質優先、長文優先など）に応じて選択肢を評価する視点を提供。

**Assembly Prompts for STEP_08:**
1. 4本を「ローカル実行のフロンティア」という大屋根の下にどう束ねるか？
2. ベンチマーク数値（競技順位、RULER 95%、52倍高速）を文脈に埋め込めているか？
3. SubQのアーキテクチャ刷新を他の3本（既存Transformer系の最適化）と区別して扱えているか？
4. 読者が「自分のラップトップ/サーバーで何が試せるか」の判断材料を得られるか？

---

#### Assembly Strategy (STEP_07) - Theme 4

**Pattern:** Multi-Perspective

**Rationale:** Linear（プロダクト開発OS）、Anthropic（管理型エージェント機能）、Stripe（決済プロトコル）、OpenAI（GPT-5.5 Instant）はいずれも独立したベンダーの同時期発表であり、相互に依存しない。「業務基盤の標準装備化」という観察軸では並列に並ぶ4つの事例として扱うのが正確で、Single-FocusやProgressive-Sequenceを当てはめると因果や序列を捏造することになる。

**Article Order & Role:**
1. [002] Linear "Issue tracking is dead" — **Peer (開発業務視点)**: Issue trackingという開発の中核プロセスをエージェント前提で再定義した宣言。読者にとって最も身近な切り口
2. [153] Claude Managed Agents — **Peer (基盤機能視点)**: Dreaming/Outcomes/Multiagent Orchestrationという、エージェント運用基盤側の機能群
3. [062] Stripe Sessions 2026 — **Peer (経済インフラ視点)**: 決済プロトコル（MPP）・ブロックチェーン（Tempo）・委任ウォレットという、エージェントが「お金を動かす」ための基盤
4. [055] GPT-5.5 Instant — **Peer (モデル基盤視点)**: ハルシネーション52.5%削減・メモリソース・パーソナライズという、エージェントが乗るモデル側の品質向上

**Narrative Arc:**
- Opening question: 「エージェントが使える場所」が、特定のアプリから業務基盤全体へ広がるとき、どこで標準化が起きているか
- Progression: 開発業務 → 運用基盤 → 経済インフラ → モデル基盤（業務スタックの異なるレイヤーを並列に）
- Key synthesis: 4社が独立に「エージェント前提の機能」を発表したこと自体が、エージェントが業務スタックの標準前提になりつつあることを示す

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 002 | 153 | Contextual | プロダクト側の再定義に対して、エージェント運用基盤側でも機能拡充が進む |
| 153 | 062 | Building | エージェントが業務を回すなら、決済・経済インフラ側の対応も必要になる |
| 062 | 055 | Contextual | 業務・運用・経済の各層を支えるモデル側でも、信頼性とパーソナライズが強化された |

**Emphasis Balance:**
- Technical depth: ⭐⭐ (各製品の機能名・仕様レベル)
- Business impact: ⭐⭐⭐ (業務基盤・経済インフラへの統合という大きな商業的含意)
- Future implications: ⭐⭐⭐ (エージェント前提の業務スタックが標準化される方向)

**Key Synthesis Points:**
1. 4社の発表が同時期に並んだこと自体が、エージェント機能の「標準装備化」フェーズを示すシグナル
2. 業務（Linear）・運用（Anthropic）・経済（Stripe）・モデル（OpenAI）という4つのレイヤーが同時に動いている
3. Stripeの「マシン間決済」とAnthropicの「Multiagent Orchestration」は、エージェント同士のインタラクションを前提にした設計
4. GPT-5.5 Instantの52.5%ハルシネーション削減は、業務基盤に乗せるための信頼性閾値を引き上げる

**Conclusion Approach:** 4つの独立した発表が同じ構造的傾向を示していることを指摘し、読者には「自分のスタックのどのレイヤーがエージェント対応を要求されるか」という観察軸を提供。

**Assembly Prompts for STEP_08:**
1. 4社の発表を並列に並べるとき、それぞれの「レイヤー貢献」をどう区別するか？
2. 「標準装備化」という観察軸を、どの記事の具体に紐づけて根拠づけるか？
3. Stripeの決済インフラ刷新を、開発者向けジャーナルの読者にどう関連付けるか？
4. GPT-5.5 Instantの数値（52.5%削減、30%簡潔化）をモデル品質の文脈にどう収めるか？

---

#### Assembly Strategy (STEP_07) - Theme 5

**Pattern:** Progressive-Sequence ⚠️ *human-review flag: Multi-Perspective is a defensible alternative*

**Rationale:** 3本の記事は「エージェント動作の証拠ベース検証」という共通課題に対し、検証粒度が段階的に深化する自然な進行を持つ。GitHub Dominatorは「振る舞い検証」の方法論、OWASP Juice Shopは「セキュリティ検出」の実測、SPECAは「仕様書からの監査」というさらに上位の検証層。粒度の異なる検証戦略が積み上がる構造のためProgressive-Sequenceが適合する。ただし完全な「依存関係」ではなく、各記事は独立にも読める点は明示すべきで、forced感はやや残る。

**Article Order & Role:**
1. [105] GitHub Dominator分析 — **Foundation**: 非決定的エージェントの「振る舞い検証」という基本問題を提起し、グラフ理論ベースの解決手法を示す
2. [121] Claude security scan + OWASP Juice Shop — **Development**: 実際のツール（Claude内蔵スキャン）が実環境（OWASP Juice Shop）で何を検出できるかという実測ベースの評価。Critical級80%以上、全体11%という具体的な検出率で前段の「証拠ベース」を実装に落とし込む
3. [093] SPECA — **Advanced/Synthesis**: コードパターンではなく仕様書から監査するという、より上位の検証層を提示。Sherlockコンテストで4件の新規バグ発見という結果を持つ

**Narrative Arc:**
- Opening question: エージェントが「成功した」と報告するとき、それを何で確かめるか
- Progression: 振る舞い検証の方法論 → 実環境での検出率実測 → 仕様書からの監査という上位層
- Key synthesis: 検証は「動作」「実検出」「仕様適合」の三層で考える必要があり、いずれも証拠（数値・実環境・仕様）に紐づくべき

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 105 | 121 | Foundation→Development | 振る舞い検証の理論的枠組みに対し、実環境での検出率を実測した報告が出ている |
| 121 | 093 | Development→Advanced | 実装レベルの検出に加え、仕様書を起点とした監査というアプローチもある |

**Emphasis Balance:**
- Technical depth: ⭐⭐⭐ (ドミネータ分析、Prefix Tree Acceptor、証明試行型推論)
- Business impact: ⭐⭐ (CI/CDパイプラインへの統合という運用含意)
- Future implications: ⭐⭐⭐ (エージェント検証の標準化方向)

**Key Synthesis Points:**
1. エージェント検証は「自己評価」（82.2%）では不十分で、外部の数学的・実証的根拠が必要
2. Critical級80%以上検出（121）と全体11%（121）の落差が示すように、「何を検出できるか」を粒度別に把握することが重要
3. SPECAの仕様書起点アプローチは、コードパターン依存の限界を超える方向性
4. 三本に共通するのは「人間が見逃すもの／エージェントが見逃すもの／パターンが見逃すもの」をそれぞれ補う設計

**Conclusion Approach:** 検証の三層（振る舞い・実検出・仕様）が揃いつつあることを示し、読者には「自分のエージェント運用でどの層の検証が欠けているか」を問い直す視点を提供。

**Assembly Prompts for STEP_08:**
1. 3本を「進行」として読ませる構造が、各記事の独立した価値を損なっていないか？
2. ドミネータ分析の理論的概念を、開発者にとってアクセスしやすい言葉でどう説明するか？
3. 121の検出率（80%/11%）の二面性を、楽観論にも悲観論にも傾けず誠実に示せているか？
4. SPECAの「仕様書からの監査」を実装レベルの検証と区別して位置づけられているか？
5. 三層の検証が「揃いつつある」と書くとき、それは観察事実か著者の解釈か？

---

#### Assembly Strategy (STEP_07) - Theme 6

**Pattern:** Multi-Perspective

**Rationale:** 3本の記事はいずれも「AIへの委譲とその認知コスト」という共通主題を、それぞれ独立した立場から論じている。Addy Osmaniは認知科学・教育の観点、Uncle Bobは挑発的な役割転換論、Simon Willisonは実務家としての境界線消失観察。立場・トーン・前提が異なるが、対立というより並列の問題提起。Debate-Contrastを選ぶと無理に「賛成 vs 反対」を作ることになるためMulti-Perspectiveが適切。Uncle Bobの記事は「終わった」という挑発的フックよりも、その背後の役割転換の議論（Vibe Coding時代における監督・レビュー役へのシフト）を要旨として扱う必要がある。

**Article Order & Role:**
1. [057] Cognitive Surrender (Addy Osmani) — **Peer (認知科学視点)**: 「オフロードとサレンダーの違い」「理解の負債」という概念枠を提供。読者の問題認識を組み立てる
2. [032] Uncle Bob "It's over" — **Peer (役割転換視点)**: コードを書く役割から監督・レビュー役への移行という議論。Reddit上の反応（懐疑論含む）も併せて、コミュニティが何を論争しているかを示す
3. [115] Simon Willison Vibe coding境界 — **Peer (実務家視点)**: VibeコーディングとAgentic engineeringの境界が消失しつつある実務観察、「逸脱の正常化」リスクへの警鐘

**Narrative Arc:**
- Opening question: AIに委譲するとき、人間の理解と責任はどこに残るのか
- Progression: 概念枠（オフロード／サレンダーの区別）→ 役割転換の議論 → 実務での境界消失観察
- Key synthesis: 3者は同じ問題（理解の所在）を、認知科学・職業論・実務観察という異なる語彙で言語化している

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 057 | 032 | Contextual | 認知の放棄という枠組みは、職業としてのコーディングの再定義論にもつながる |
| 032 | 115 | Additive | 役割の議論に加え、実務家からは境界線そのものの消失が観察されている |

**Emphasis Balance:**
- Technical depth: ⭐ (技術的詳細より概念整理が中心)
- Business impact: ⭐⭐ (チーム運営・スキル形成への含意)
- Future implications: ⭐⭐⭐ (人間の理解と責任の所在という長期的問い)

**Key Synthesis Points:**
1. Osmaniの「サレンダー対オフロード」、Uncle Bobの「役割転換」、Willisonの「境界消失」はいずれも同じ現象を異なる粒度で観察している
2. Uncle Bobの「終わった」は挑発的フックだが、Reddit上の懐疑論を含めると論点は「監督役の質をどう保つか」に収斂する
3. Willisonが指摘する「成果物がもはや品質の証拠ではない」は、Osmaniの「理解の負債」と同じ不安を別角度から捉える
4. 3者とも「ツールの問題ではなく姿勢の問題」という結論に独立に到達している

**Conclusion Approach:** 3つの異なる語彙が同じ問題を指していることを示し、読者には「自分が今、どの種類の委譲をしているか」を問い直す具体策（Osmaniのヒューリスティクス等）を提供。

**Assembly Prompts for STEP_08:**
1. Uncle Bobの記事は挑発的フックではなく、その背後の役割転換論として扱えているか？
2. 3者を「対立」ではなく「並列の問題提起」として読ませる構造になっているか？
3. Osmaniの具体的ヒューリスティクスを、抽象論で終わらせない形でどう紹介するか？
4. Willisonの「逸脱の正常化」リスクを、軽率な悲観論に陥らずに伝えられているか？
5. 「理解の負債」「認知の放棄」「境界消失」という3つの語彙の関係をどう整理するか？

---

#### Assembly Strategy (STEP_07) - Theme 7

**Pattern:** Multi-Perspective

**Rationale:** 3本の記事は「AI業界の収益性と信頼性」という大屋根の下にあるが、結論が対立しているわけではなく、むしろ別の観察対象（Anthropic収益・Claude Code品質・GPU融資構造）を扱っている。Atlanticは楽観的観察、Tordableは現場での失望、GPU担保融資は構造的リスク。Debate-Contrastにすると「楽観 vs 悲観」という単純化に陥り、各記事の固有の観察対象を見失うのでMulti-Perspectiveが適切。3つの視点が同時に成立しうる（収益増・品質劣化・債務リスク）ことを示すのが本質。

**Article Order & Role:**
1. [035] The Atlantic "Maybe AI Isn't a Bubble After All" — **Peer (収益視点)**: Anthropic収益急増（年換算300億ドル）を根拠にバブル論の再考を促す観察
2. [043] "Claude Is Dead" — **Peer (現場品質視点)**: 同じAnthropicの主力製品Claude Codeに対する利用制限・推論能力低下の批判。収益と現場体感の乖離を示す
3. [033] GPU Debt Wall — **Peer (構造リスク視点)**: 収益・品質の議論とは別軸の、インフラ融資側の構造的リスク（2026年返済の壁）

**Narrative Arc:**
- Opening question: AI業界の収益・品質・財務構造は、それぞれどう評価されるべきか
- Progression: 収益（マクロ楽観）→ 製品品質（ミクロ悲観）→ 構造リスク（財務）の3つの観察軸を並列に
- Key synthesis: 楽観論・悲観論は対立しているのではなく、別の対象を別の指標で見ているにすぎない

**Transition Strategy:**

| From | To | Type | Japanese phrase |
|------|-----|------|------|
| 035 | 043 | Contrasting | 収益面での楽観的見立てに対し、製品品質の現場では別の評価が出ている |
| 043 | 033 | Contextual | 収益と品質の議論とは別軸で、インフラ融資側の構造リスクも指摘されている |

**Emphasis Balance:**
- Technical depth: ⭐ (財務・経済の議論が中心)
- Business impact: ⭐⭐⭐ (収益・債務・移行先選択という直接的な商業含意)
- Future implications: ⭐⭐⭐ (2026年「負債の壁」という時間軸を持った予測)

**Key Synthesis Points:**
1. 「収益増（35）」「品質劣化（43）」「債務リスク（33）」は対立する主張ではなく、別の指標による別の観察である
2. 同じAnthropicが収益急増（35）と現場での品質批判（43）を同時に集めている事実が、収益と顧客体験の乖離を示す
3. GPU担保融資の構造（33）は、収益と品質のどちらが先に変化しても影響を受けるシステミック・リスク
4. 読者にとっての含意は「自分の依存先（モデル/ベンダー）を、収益・品質・財務の3軸で見るべき」

**Conclusion Approach:** 3つの観察軸を統合し、「楽観 vs 悲観」の二元論を超えて、AI業界を多軸で評価する読み方を読者に提示。移行先選択の判断材料として位置づける。

**Assembly Prompts for STEP_08:**
1. 35と43を「対立」ではなく「別対象の観察」として読ませる構造になっているか？
2. Anthropicが両記事に登場することの含意を、誇張せずどう書くか？
3. GPU Debt Wallの2026年予測を、確定的な未来として扱わずに紹介できているか？
4. 読者が「自分の依存先を3軸で評価する」という視点を持って読み終われるか？
5. 各記事の数値（300億ドル、レート制限、2026年）を文脈の中で機能させているか？

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected for all 7 themes (6× Multi-Perspective, 1× Progressive-Sequence)
- [x] Phase 3: Assembly strategies drafted
- [x] APPROVED - Ready for STEP_08

**Approved:** 2026-05-10 by beijaflor

**Drafted:** 2026-05-10

**Notes for human reviewer:**
- 6 of 7 themes selected **Multi-Perspective** because the curated articles are genuinely independent observations rather than chains of reasoning. Grounded in unified summaries — articles share themes but not dependencies.
- **Theme 5** is the only Progressive-Sequence selection. Softer fit than ideal: the three articles do show progressive depth (behavior → detection → spec) but are also independently readable. Multi-Perspective is a defensible alternative.
- **Theme 6** could plausibly be Debate-Contrast (Uncle Bob vs. Osmani/Willison), but per project memory the satirical hook ("It's over") should not anchor the framing. Actual theses converge ("posture matters"), so Multi-Perspective is more honest.
- **Theme 7** also tempts Debate-Contrast (bubble vs. not-bubble), but the three articles measure different things (revenue, product quality, debt structure). Forcing a debate would misrepresent the source material.
- Transition phrases avoid manufactured connectors ("並ぶ", "同週発表", "反論", "を巡る論争").
