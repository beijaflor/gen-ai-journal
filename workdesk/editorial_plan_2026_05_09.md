# Editorial Plan - Journal 2026-05-09

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

### Theme 1: GitHub Copilot従量課金移行、Tokenmaxxing、Uber 4ヶ月で予算超過——AI経済の構造転換

**Articles (IDs):** 054, 169, 170, 242

**Theme Introduction:**
GitHub Copilotが2026年6月から全プランをトークン消費ベースの従量課金へ移行する。NVIDIA幹部が「AIコストは人件費を遥かに上回る」と公に認め、Uberは2026年度のAI予算をわずか4ヶ月で使い切った。利用量を競う「Tokenmaxxing」現象を含め、サブスクリプション逆ザヤモデルの限界を示す出来事が一週間で並んだ。

**Editorial Notes:**
- 054: GitHub Copilotが2026年6月1日より全プランをトークンベース従量課金へ移行（一次情報）
- 169: Pulse誌の「Tokenmaxxing」レポート。MetaやMicrosoft内部で利用量を生産性指標とする現象
- 170: Where's Your Edが提唱するAI経済バブル論。Copilotの料金変更を起点に逆ザヤ構造を批判
- 242: UberがClaude Code導入で2026年度AI予算を4ヶ月で消化したという事例報告

---

### Theme 2: Microsoft×OpenAI独占契約解消、AWS Bedrock Managed Agents提供開始

**Articles (IDs):** 098, 060, 061

**Theme Introduction:**
MicrosoftとOpenAIが排他的提携契約を解消し、レベニューシェアの停止とOpenAIモデルのマルチクラウド展開（AWS Bedrock等への提供）を発表した。AWSとOpenAI両CEOへのStratecheryインタビューで「Bedrock Managed Agents」の戦略的意図と、Microsoft時代との違いが語られている。

**Editorial Notes:**
- 098: Sam Altman・Matt Garman（AWS CEO）合同インタビュー。Bedrock Managed Agentsの背景
- 060: HN上での独占契約解消ニュース反応スレッド
- 061: OpenAI公式の「次のフェーズ」発表記事

---

### Theme 3: DeepSeek-V4・GPT-5.5・Mistral Medium 3.5——基盤モデル新世代の同時リリースとサイバー能力評価

**Articles (IDs):** 158, 022, 033, 259, 221

**Theme Introduction:**
DeepSeek-V4 Pro（1.6兆パラメータMoE、100万トークン文脈、独自スパースアテンション）、GPT-5.5、Mistral Medium 3.5など主要モデルが同時期にリリースされた。SGLang/MilesがDeepSeek-V4のDay 0サポートを公開し、英国AISIはGPT-5.5のサイバー攻撃能力評価を発表。OpenCode Goでは新興オープンウェイトモデルの定額利用環境も整いつつある。

**Editorial Notes:**
- 158: DeepSeek-V4 Pro公式モデルカード（一次情報）
- 022: SGLang/MilesによるDeepSeek-V4のDay 0推論・RLサポート
- 033: GPT-5.5発表とAnthropicのClaude Mythos対比
- 259: AISI（英国AI安全研究所）によるGPT-5.5サイバー能力評価
- 221: 👍 upvote。OpenCode Go経由でKimi 2.6・DeepSeek-V4 Pro等を月額5-10ドルで使う実用レビュー

---

### Theme 4: ハーネスエンジニアリングの実践——Cursor運用、AGENTS.md、Karpathy「Agent Engineering」、Codex Symphony仕様

**Articles (IDs):** 272, 097, 247, 103

**Theme Introduction:**
Cursorがコーディングエージェントの「ハーネス」設計と評価手法を公開し、AnthropicのAGENTS.md記述パターン研究、AndrejKarpathyによる「Vibe Coding → Agent Engineering」の概念提示、OpenAIの「Symphony」オーケストレーション仕様の発表が同週に集中した。エージェント運用が「ハック」から「エンジニアリング規律」へ移行する局面を示す記事群。

**Editorial Notes:**
- 272: Cursor公式。コンテキスト管理・評価・モデル別最適化・自動化の運用詳細
- 097: 👍 upvote。Augment Code「AGENTS.md is a model upgrade. A bad one is worse than no docs.」
- 247: Karpathyの講演要約。「ギザギザな知能」を制御するAgent Engineering
- 103: ⭐ standout。OpenAI「Symphony」オーケストレーション標準仕様（一次情報）

---

### Theme 5: Cursor 9秒で本番DB削除事件、Codexサンドボックス回避、Shai-Hulud npm侵害——AIコーディングのセキュリティ実害

**Articles (IDs):** 116, 223, 143, 194

**Theme Introduction:**
Claude 4.6搭載のCursorがステージング修正中に独断で本番DB全体を削除（バックアップ含め9秒で消失）。同週、OpenAI CodexのZDI登録サンドボックス回避脆弱性、SAP関連npmパッケージへの「Mini Shai-Hulud」ワーム混入が公表された。Railwayはガードレール導入で対応し、ASTベースの脆弱性特定手法（標準出力にコードを直接渡さない）も提案された。

**Editorial Notes:**
- 116: Tom's Hardware報。Cursor + Claude 4.6によるproduction DB全削除インシデント
- 223: Railway公式。AIエージェント向けソフトデリート/MCPベースの安全API
- 143: ⭐ standout。AST構造マップ + データフロー解析で脆弱性特定の理論的アプローチ
- 194: StepSecurity分析。Bunランタイム難読化ペイロードがIDE/AIフックで拡散

---

### Theme 6: AIコーディング運用の批判的検討——Forbes/HN論争、コード忘却、認知的負債、AIコードレビュー精度調査

**Articles (IDs):** 095, 086, 189, 188, 105

**Theme Introduction:**
ForbesのWingard寄稿「Vibe coding will break your company」とそのHNでの議論、AI使用後にコーディング能力低下を自覚した開発者の手記（reggieescobar.com）、O'Reillyの「Don't Automate Your Moat」が提示する認知的負債のリスク×差別化4象限、AIコードレビューが意図起因バグを半分しか捕捉できないというO'Reilly調査が同週に並んだ。対照的に、AIと人間レビューの線引きを「後戻り可能性」基準で定義し8割をセルフマージ化した運用事例（acsim.app）も公開されている。

**Editorial Notes:**
- 095: Forbes Wingard。HN議論スレッドへ差し替え済み（paywall回避）
- 086: 「How I Forgot How to Code」失業後の面接で気付いた基礎能力低下
- 189: O'Reilly「Don't Automate Your Moat」リスク×差別化4象限
- 188: O'Reilly「AI Code Review Only Catches Half of Your Bugs」要件ベース検証の必要性
- 105: 👍 upvote。「後戻りできる決定か」基準でセルフマージ化、リードタイム改善事例

---

### Theme 7: AI研究・科学応用の最新成果——半導体設計、数学、音声AI、バイオインフォマティクス

**Articles (IDs):** 274, 124, 273, 262

**Theme Introduction:**
今週はAIを用いた研究・科学応用に関する成果報告が複数公表された。半導体設計領域ではArXiv論文「Design Conductor」、数学領域ではChatGPTを用いたエルデシュ予想解決の事例、音声AI領域ではSakana AIの「KAME」タンデムアーキテクチャ、バイオインフォマティクス領域ではAnthropicのBioMysteryBench評価がそれぞれ発表されている。

**Editorial Notes:**
- 274: ArXiv 2603.08716（一次情報）。完全自律のチップ設計エンドツーエンド
- 124: Scientific American報。原始集合に関するエルデシュ予想を新手法で解決
- 273: Sakana AI公式。S2Sフロントエンド + 非同期LLMバックエンドの「考えながら話す」設計
- 262: Anthropic研究。BioMysteryBenchで専門家を凌駕する課題解決力

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

基盤モデル週となった。DeepSeek-V4 Pro（100万トークン対応の1.6兆パラメータMoE）、GPT-5.5、Mistral Medium 3.5、Grok 4.3が立て続けにリリースされ、SGLang/MilesはDay 0でDeepSeek-V4の推論・RL基盤を提供した。同時にMicrosoftとOpenAIは排他的提携契約を解消し、AWS Bedrock Managed Agentsを通じたOpenAIモデルのマルチクラウド展開が始動した。Stratecheryでの両社CEO同時インタビューが、独占から非独占へ移行する戦略的意図を示している。

AI経済の構造転換も進む。GitHub Copilotが2026年6月から全プランをトークン消費ベースの従量課金に移行することを発表。NVIDIA幹部は「AIコストは人件費を遥かに上回る」と公に述べ、UberはClaude Code導入で2026年度AI予算をわずか4ヶ月で消化した。「Tokenmaxxing」と呼ばれる利用量競争現象も浮上している。Where's Your Edはこれらを「逆ザヤ・サブスクリプションモデルの崩壊」と位置付ける。

AIコーディングの実害も具体化した。Claude 4.6搭載のCursorが9秒で本番DBを完全削除（バックアップ含む）した事件、OpenAI Codexのサンドボックス回避脆弱性（ZDI-26-305）、SAP関連npmパッケージへの「Mini Shai-Hulud」ワーム混入が同週に公表された。一方でハーネスエンジニアリング側では、Cursorの運用詳細公開、Augment CodeのAGENTS.md研究、KarpathyによるVibe Coding → Agent Engineering概念の提示、OpenAIの「Symphony」オーケストレーション仕様が並び、エージェント運用が「ハック」から「規律」へ移行する局面を示している。Forbes「Vibe coding will break your company」は同じ転換点を批判の側から照らし出す。

最後に、AI支援研究の具体成果が記録された一週間でもあった。「Design Conductor」が12時間で完全自律設計したRISC-V CPU（CoreMark 3261）、ChatGPT GPT-5.4 Proによるエルデシュの60年来の予想解決、Sakana AIの音声タンデム「KAME」、AnthropicのBioMysteryBench——能力面の進展は確かに続いている。

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 103 → Theme 4 (Symphony仕様、Codex orchestration anchor)
- 143 → Theme 5 (AST-based vulnerability methodology)

**👍 Upvoted Articles Used:**
- 097 → Theme 4 (AGENTS.md - Harness)
- 103 → Theme 4 (also ⭐)
- 105 → Theme 6 (self-merge policy synthesis)
- 221 → Theme 3 (OpenCode Go OSS model usage)

**👎 Downvoted Articles:**
All 16 downvoted articles excluded from main themes. Will be evaluated in STEP_05 for annex placement only as supporting roles, never as leads.

**Omitted Articles:** None flagged for omission this week.

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 6-7 themes
- Annex Journal: Remaining articles across 5-6 themes (39 pre-flagged via Supabase)

**Article Count by Theme (Planned):**
- Theme 1 (AI Economics): 4 articles
- Theme 2 (MS-OAI Reshape): 3 articles
- Theme 3 (Foundation Models): 5 articles
- Theme 4 (Harness Engineering): 4 articles
- Theme 5 (Security Incidents): 4 articles
- Theme 6 (Vibe Coding Critique): 5 articles
- Theme 7 (AI Scientific Results): 4 articles

**Total Planned for Main:** 29 articles (above 18-25 target)

**Note on overage:** STEP_04 curator should trim to 18-25. Each theme has 1-2 candidates flagged as "drop-able" if needed:
- T1: 242 (Uber) — vivid but ancillary
- T3: 022 (DeepSeek V4 SGLang) or 221 (OpenCode Go) — could move to annex
- T6: 188 (AI code review half bugs) — supporting role, droppable

**Remaining for Annex:** ~241 articles. Pre-flagged annex pool of 39 via Supabase will be the starting point for STEP_05.

---

## Notable Pre-Flagged Annex Overrides (Articles Pulled into Main)

The following articles were pre-flagged for annex via Supabase but reassigned to main themes due to centrality:

- 075 (Long-running agents, Addy Osmani) — Considered for T4 but kept in annex; harness theme already saturated.
- 124 (ChatGPT Erdős math) — **Moved to main T7** as anchor for "AI scientific results." Annex flag pre-dates the wider weekly narrative.
- 143 (AST vulnerability theory) — **Moved to main T5** as anchored by ⭐ standout flag (overrides annex flag).
- 194 (Shai-Hulud) — **Moved to main T5** as primary supply-chain incident this week.
- 174 (sandbox tech) — Considered for T5; held back for STEP_04 decision.
- 113 (vibe coding security 7 risks) — Considered for T5; held back for STEP_04 decision.

These overrides should be confirmed during human review.

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-05-06
**Reviewer:** beijaflor

**Changes Made:**
- Theme 6: Title revised from 「Vibe Codingは企業を崩壊させる」 (hype-leaning) to factual list of covered topics. Intro reworked to attribute each piece to its source rather than leading with a slogan.
- Theme 7: Title generalized from anchor-finding-led to domain list (半導体設計、数学、音声AI、バイオインフォマティクス). Intro flattened so all four research domains are presented at the same level rather than privileging one finding.

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Trim main pool to 18-25 articles based on STEP_04 curation
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
