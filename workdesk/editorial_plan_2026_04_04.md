# Editorial Plan - Journal 2026-04-04

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

### Theme 1: Claude Code 51万行流出：内部構造の解析とDMCA・AIリライト問題

**Articles (IDs):** 072, 253, 233, 174

**Theme Introduction (2-3 sentences in Japanese):**
Claude Codeのソースコード51万行超がnpmソースマップから流出した。内部のエージェントループ構造や未公開機能の技術分析に加え、DMCA濫用への批判やAIリライトによる著作権回避の問題も取り上げる。

**Editorial Notes:**
- 072, 253: 技術面の分析記事
- 233: ドクトロウによる著作権・DMCA批判
- 174: AIリライトによる言語変換の法的問題

---

### Theme 2: 「Conviction Collapse」とCopilot PR広告挿入、ソフトウェアの変容を問う論考

**Articles (IDs):** 147, 121, 231

**Theme Introduction (2-3 sentences in Japanese):**
ハーパー・リードが提唱する「確信の崩壊（Conviction Collapse）」、CopilotがPRに広告を挿入した事件、O'Reillyによる「ウィンチェスター・ミステリー・ハウス」型開発モデルの提唱。ソフトウェアの在り方に関する異なる視点の記事を集めた。

**Editorial Notes:**
- 147: Conviction Collapse概念の紹介（O'Reilly）
- 121: CopilotのPR広告挿入事件
- 231: 大伽藍・バザールに次ぐ第3の開発モデル提唱（O'Reilly）

---

### Theme 3: Martin Fowler・Addy Osmani発、ハーネスエンジニアリングの具体手法

**Articles (IDs):** 189, 082, 182, 176, 134

**Theme Introduction (2-3 sentences in Japanese):**
Martin Fowlerによる「ハーネスエンジニアリング」の提唱をはじめ、AIエージェントの制御手法に関する記事が今週複数登場した。Addy Osmaniのオーケストレーション論、NLAH、VSDD方式など、それぞれ異なるアプローチを紹介する。

**Editorial Notes:**
- 189: Martin Fowlerのハーネスエンジニアリング（ガイド＋センサーの多層制御）
- 082⭐: Addy Osmaniのコードエージェント・オーケストラ
- 182: エージェントハーネスをビジネス完成品として捉える視点
- 176: NLAH（自然言語ハーネス定義、SWE-benchで既存超え）
- 134: VSDD方式（Builder/Adversary役割分離）

---

### Theme 4: Cursor 3再設計・Copilot /fleet・Codex連携、そしてJSSE

**Articles (IDs):** 202, 148, 122, 077

**Theme Introduction (2-3 sentences in Japanese):**
Cursor 3のエージェント中心UI再設計、Copilot CLIの/fleet並列実行、Codex×Claude Code相互運用プラグインなど、主要エージェント型開発ツールの新展開を取り上げる。JSSEプロジェクト（AIのみでRust製JSエンジン構築）も紹介する。

**Editorial Notes:**
- 202⭐: Cursor 3のゼロからの再設計、ローカル/クラウド連携
- 148: Copilot CLI /fleet（タスク自動分解＋並列実行）
- 122: Claude CodeからCodexを呼び出すプラグイン
- 077⭐: JSSE（人間実働4時間、test262を100%パス）

---

### Theme 5: Agents of Chaosレッドチーミング、CSRF漏洩、エージェント経済のセキュリティ課題

**Articles (IDs):** 115, 065, 256, 155

**Theme Introduction (2-3 sentences in Japanese):**
エージェント経済に必要なインフラの欠落を論じるO'Reilly記事、自律型AIエージェントの脆弱性を実証したレッドチーミング調査、AIツールが見落としたCSRFトークン漏洩、AIによるVim/EmacsのRCE脆弱性発見など、セキュリティ関連の記事を集めた。

**Editorial Notes:**
- 115⭐: エージェント経済の欠落した仕組み（O'Reilly）
- 065⭐: Agents of Chaos（11の脆弱性を実証）
- 256: Claude Code/Codexが見落としたCSRFトークン漏洩
- 155: AIがVim/EmacsのRCE脆弱性を発見

---

### Theme 6: ChatGPT断ち4日間調査・AI語彙の浸透・「AI疲れ」

**Articles (IDs):** 228, 149, 021, 064

**Theme Introduction (2-3 sentences in Japanese):**
KAISTの「ChatGPT断ち4日間」調査、AI語彙の人間への浸透による認知的萎縮の懸念、「AIの話に飽きた」というエンジニアの声、執筆をAIに委ねることへの批判など、AI依存と人間の認知に関する記事を集めた。

**Editorial Notes:**
- 228: KAISTの日記調査（LLMのインフラ化を実証）
- 149: AI語彙の浸透と言語均質化
- 021⭐: 「AIの話に飽きた」（Standout + Upvoted）
- 064: 執筆を委ねるべきでない理由

---

### Theme 7: LayerX・DMM・食べログのAIエージェント組織実装

**Articles (IDs):** 244, 181, 222

**Theme Introduction (2-3 sentences in Japanese):**
LayerXの「Agentic Nervous System」組織モデル、DMMのClaude Code×MCPによる技術的負債の自動計測CI、食べログのMCP活用による実装コスト削減事例など、日本企業によるAIエージェント実装の実例を紹介する。

**Editorial Notes:**
- 244: LayerXの組織モデル（AIエージェントを「神経系」として埋め込み）
- 181: DMMの技術的負債可視化CI（120名規模組織での運用）
- 222: 食べログのMCP活用（実装コスト4分の1に削減）

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週はClaude Codeのソースコード流出が大きな話題となった。51万行超の内部実装が公開され、技術分析や著作権問題に関する議論が多数発生した。

エージェント型開発ツールでは、Cursor 3の再設計、Copilot CLIの/fleet並列実行機能、Codex×Claude Code相互運用プラグインなど、主要プレイヤーから新機能が相次いで発表された。JSSEプロジェクトではAIエージェントのみでRust製JSエンジンが構築された。

Martin Fowlerが「ハーネスエンジニアリング」を提唱し、AIエージェントの制御手法に関する議論が活発化した。O'Reillyからはエージェント経済の構造的課題、Conviction Collapse概念、ウィンチェスター型開発モデルなど複数の論考が公開された。

AI依存の影響についても注目すべき記事が複数あり、KAISTのChatGPT断ち調査やAI語彙の浸透問題、CopilotのPR広告挿入事件など、技術進歩の副作用に関する議論も見られた。

**Key Points to Cover:**
1. Claude Code流出：技術分析と著作権問題
2. エージェント型開発ツールの新展開
3. ハーネスエンジニアリングとエージェント制御手法
4. エージェント経済のセキュリティ課題
5. AI依存と認知への影響
6. 日本企業のエージェント実装事例

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 072 → Theme 1 (Lead)
- 253 → Theme 1 (Supporting)
- 147 → Theme 2 (Lead)
- 121 → Theme 2 (Supporting)
- 082 → Theme 3 (Supporting)
- 202 → Theme 4 (Lead)
- 077 → Theme 4 (Synthesis)
- 115 → Theme 5 (Lead)
- 065 → Theme 5 (Supporting)
- 021 → Theme 6 (Supporting)

**👍 Upvoted Articles Used:**
- 021 → Theme 6 (Supporting) — also ⭐

**⭐ Standout Articles NOT used in Main (Annex candidates):**
- 076 (Storybook MCP) → Annex: ツール・実験
- 080 (Agent Community design course) → Annex: 教育・学習
- 179 (NDLOCR-Lite Web AI) → Annex: ニッチ・深堀り
- 194 (Claude Code leak analysis) → Could merge with Theme 1 if needed

**👎 Downvoted Articles:** Excluded from theme planning (22 articles listed in curation_flags.md)

**Omitted Articles:** 247

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 25 articles across 7 themes
- Annex Journal: Remaining ~220 articles (to be curated in STEP_05)

**Article Count by Theme (Planned):**
- Theme 1 (Claude Code流出): 4 articles
- Theme 2 (Conviction Collapse・PR広告): 3 articles
- Theme 3 (ハーネスエンジニアリング): 5 articles
- Theme 4 (Cursor 3・/fleet・Codex・JSSE): 4 articles
- Theme 5 (Agents of Chaos・セキュリティ): 4 articles
- Theme 6 (ChatGPT断ち・AI疲れ): 4 articles
- Theme 7 (LayerX・DMM・食べログ): 3 articles

**Total Planned for Main:** 27 articles (to be refined to 25 in STEP_04)
**Remaining for Annex:** ~220 articles (to be curated to ~25-35 in STEP_05)

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-04-10
**Reviewer:** Human Editor

**Changes Made:**
- Toned down theme titles from dramatic/narrative to concrete/factual
- Simplified theme introductions to present articles as-is
- Removed manufactured narrative connections
- Updated workflow documents (STEP_03b, STEP_08) to reflect editorial tone preference

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
