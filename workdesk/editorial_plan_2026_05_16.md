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
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
