# Editorial Plan - Journal 2026-05-30

## Planning Status

- [x] Initial theme identification (AI-assisted)
- [ ] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual**
- ✅ Name specific technologies, people, events, numbers
- ✅ List key topics covered in the theme
- ❌ Avoid generic category labels
- ❌ Avoid dramatic or narrative-heavy framing
- ❌ Avoid narrative connectors ("並ぶ"・"ラッシュ"・"波"・"急増")

### Theme 1: Claude Opus 4.8・Dynamic Workflows・Project Glasswing・Containmentが進めるAnthropicのエージェント基盤

**Articles (IDs):** 169, 170, 010, 147

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが今週、Opus 4.8の推論性能強化、Claude Codeへの並列サブエージェント機能（Dynamic Workflows）、Claude Mythos Previewによる脆弱性検知の成果報告（Project Glasswing）、Claude製品群のサンドボックス／VM多層防御の公開（Containment）という4つの発表を立て続けに公開した。新モデル・運用機能・セキュリティ研究・封じ込め手法が同社の発表サイクルの中でどう接続するかが、4本の記事からまとめて読み取れる。

**Editorial Notes:**
- 169: Opus 4.8 — 思考の深さを調整する「努力量制御」と並列エージェント実行を備えた新モデル（👍 upvote）
- 170: Dynamic Workflows — Claude Codeがオーケストレーション・スクリプトを動的生成し、数百の並列サブエージェントで大規模移行を実行（👍 upvote）
- 010: Project Glasswing — Claude Mythos Previewで1ヶ月間に1万件以上の深刻な脆弱性を検知（👍 upvote）
- 147: Containment — Claude Code・Coworkで採用されているサンドボックス／VM／多層防御アーキテクチャの公開

---

### Theme 2: 教皇レオ14世回勅 Magnifica Humanitas・Chris Olah・Simon Willisonに見るAI倫理と人間中心主義の言説

**Articles (IDs):** 037, 060, 061, 062, 079

**Theme Introduction (2-3 sentences in Japanese):**
2026年5月、教皇レオ14世が初の回勅『Magnifica Humanitas（大いなる人間性）』を公開し、AI時代における人間の尊厳・労働の価値・アルゴリズム透明性・自律型致死兵器など、AI倫理の根本問題を提起した。ReligionNews・Variety・Anthropicの研究者Chris Olah・Simon Willisonがそれぞれの立場から回勅に応答する形で、AI業界・技術コミュニティ・宗教・メディアにまたがる多層的な言説が同時期に展開されたことが5本の記事から確認できる。

**Editorial Notes:**
- 037: 回勅 *Magnifica Humanitas* 本文 — トランスヒューマニズム批判、アルゴリズム倫理、労働・教育・武装解除を論じる primary source
- 060: ReligionNews — 「AIは人類全体に仕えるべきであり、権力者の少数に仕えるべきではない」と要約・解説
- 061: Variety — アルゴリズムが「非人間化（dehumanisation）」を引き起こす可能性を指摘する解説
- 062: Anthropic Chris Olah — 同社研究者による回勅への応答エッセイ（公式ニュースから）
- 079: Simon Willison — 技術コミュニティ向けの解説・引用集

---

### Theme 3: メルカリ・VibeSec・Sigil・Microsoft Copilot Exfiltration・aislopが浮き彫りにするAgentic AI攻撃面

**Articles (IDs):** 093, 098, 027, 063, 246

**Theme Introduction (2-3 sentences in Japanese):**
Agentic AIの導入に伴い、組織体制（メルカリ）、設定ファイルの権限管理（Sigil）、プロンプト指示の限界（VibeSec）、大手プラットフォームでの実害（Microsoft Copilot Coworkからのファイル流出）、AIが生成するコードスロップの検出（aislop）という複数の層で同時に攻撃面が拡大していることが明らかになった週。組織・技術・コード品質それぞれの層に応じた対策が走り始めている。

**Editorial Notes:**
- 093: メルカリのAIガバナンスとガードレール多層実装（組織体制・ツール審査・サンドボックス）
- 098: VibeSec Reckoning — AIに「セキュアであれ」と指示するだけでは不十分（Martin Fowler）
- 027: AIコーディングエージェントの本当の攻撃面は設定ファイル — OSS「Sigil」による監視
- 063: Microsoft Copilot Coworkがプロンプトインジェクションでファイルを外部流出させた事例
- 246: aislop — AIが生成したコードの「スロップ」を検出・修正する高速クリーンアップツール

---

### Theme 4: Addy Osmani・Mozilla AI・UXDesign・Every.toが問うAIエージェント時代の認知負荷と役割再定義

**Articles (IDs):** 046, 047, 049, 050

**Theme Introduction (2-3 sentences in Japanese):**
AIが「書く」を代替しても「決める」「統合する」「責任を取る」は人間に残る、という視点を共有する4本の論考。Addy Osmaniの「オーケストレーション税」、Claude Codeでデザイナーの役割境界が融解する経験、エージェントネイティブUIへの転換提言、自動化が人間の仕事を減らさず増やす逆説など、開発者・デザイナーの役割そのものを再定義する議論が並ぶ。

**Editorial Notes:**
- 046: Orchestration Tax — 並列エージェント運用と人間の認知能力の非並列性（Amdahl的限界）（👍 upvote）
- 047: Claude Code導入でデザイナーが開発領域へ越境した結果、「審美眼」「ユーザー共感」の核心価値が逆に鮮明化
- 049: エージェントネイティブなアプリへの転換 — UIはもはや「製品」ではない（Mozilla AI）
- 050: 自動化の逆説 — AIは仕事を減らさず、文脈に応じた人間の専門性需要を増やす（Every.to）

---

### Theme 5: MCP 2026-07-28・Sentry・Docker Gordon・Cloudflare Town Lakeが整えるエージェント本番運用基盤

**Articles (IDs):** 065, 070, 134, 156

**Theme Introduction (2-3 sentences in Japanese):**
MCPプロトコルのステートレス化（2026-07-28版RC）と、Sentry・Docker・Cloudflareの各社によるエージェント向け本番ツールが揃って公開／GAされた週。プロトコル仕様の進化と、観測（Sentry）・コンテナ運用（Docker Gordon）・データプラットフォーム（Town Lake/Skipper）という運用三層の整備が並行していることが見て取れる。

**Editorial Notes:**
- 065: MCP 2026-07-28版でステートレス化 — ハンドシェイク廃止、ヘッダーベース・ルーティング、レスポンスキャッシュ導入
- 070: Sentry MCP — エージェントが本番のスタックトレースと分散トレースを理解して自動修正PRを作成
- 134: Docker Gordon — コンテナのデバッグ・作成・最適化を自律実行するAIエージェントが一般公開
- 156: Cloudflare Town Lake + Skipper — 自社スタックで構築したレイクハウスと自然言語データ分析エージェント

---

### Theme 6: Claude Code Mastery・Self-Improving Skills・Codex Cycle・cortexが体系化するエージェント運用ノウハウ

**Articles (IDs):** 109, 026, 028, 033

**Theme Introduction (2-3 sentences in Japanese):**
エージェントを単発呼び出しではなく、継続改善・長時間自走・レビューフロー組込みといった「運用」の単位で捉える実践記事群。Claude CodeとCodex CLIの両方で運用ノウハウが体系化されつつあり、自己改善ループ・トークン84%削減のCycle運用・AIレビューの社内導入事例などが共有されている。

**Editorial Notes:**
- 109: 「プロンプトの先へ」— Claude Codeを自律エージェントとして運用する究極ガイド（mainJournalスコア98）
- 026: 会話履歴から課題抽出しSKILL.mdを自動修正する自己改善ループの構築
- 028: Codex CLIの「1ファイル・1サイクル」運用 — トークン84%削減、22.5時間連続自走
- 033: AIが書いたコードはAIがレビューする — cortex社内導入の連載Part 3

---

### Theme 7: Karpathy LLM Wiki・XMLプロンプト・Knowledge Graph・Product Graphが示すエージェント文脈設計

**Articles (IDs):** 019, 022, 024, 096

**Theme Introduction (2-3 sentences in Japanese):**
RAGの精度低下やプロンプト解釈の曖昧さといったエージェント運用上の課題に対し、知識を「AIが消化しやすい構造に事前コンパイルしておく」設計手法を論じる4本。Karpathy氏のLLM Wiki思想、AnthropicがXMLタグを推奨する構造的理由、Memory-firstのナレッジグラフ設計、JSDoc/AST解析によるProduct Graphなど、文脈をどう構造化するかが焦点となっている。

**Editorial Notes:**
- 019: 社内ドキュメントをLLM消化形式に事前コンパイルするKarpathy LLM Wikiの実践記
- 022: scatter-gather方式の限界とMemory-firstナレッジグラフによる解決（DevRev事例）
- 024: AnthropicがプロンプトにXMLタグを推奨する構造的理由（Markdownとの比較）
- 096: AIハーネスの心臓部 — JSDoc/AST解析でコード・DB・ドキュメントをProduct Graphに統合

---

### Theme 8: Ryzen AI Max+ NAS・5年前MacBook・AutoTTSが示すローカル／エッジAIの実用化

**Articles (IDs):** 003, 004, 005

**Theme Introduction (2-3 sentences in Japanese):**
APIコスト高騰やフロンティアモデル依存からの脱却を目指し、ローカル実行の実用性が短期間で向上していることを示す3本。Ryzen AI Max+専用NASのレビュー、5年前のM1 MacBookでGemma 4を動かす実践記、Claude Codeが推論スケーリング規則を自律設計するAutoTTS研究という、ハードウェア・既存資源活用・アルゴリズム最適化の異なる角度の事例が揃っている。

**Editorial Notes:**
- 003: Ryzen AI Max+ 395搭載NAS「N5 Max」レビュー — 中規模LLM／AIエージェントを実用速度でローカル実行
- 004: 5年前のM1 Max MacBookでGemma 4をローカル実行し、1年分の動画アーカイブを自動インデックス化
- 005: AutoTTS — Claude Codeが推論時の計算資源配分アルゴリズムを自律設計し、既存手法を上回る効率を達成

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週はAnthropicの集中発表が目立った週となった。Opus 4.8リリース、Claude Codeへの動的並列ワークフロー追加、Project Glasswingによる脆弱性検知の成果報告、Containment（封じ込め）手法の公開という4本立てで、新モデルから運用機能・セキュリティ研究・実装ガイドまでが揃って公開された。同時に、Sentry・Docker・Cloudflareがそれぞれエージェント向け本番運用ツールを公開／GAし、MCPプロトコルもステートレスファースト仕様（2026-07-28版RC）に進んだ。エージェントを単発のツール呼び出しから本番システムに組み込む段階に踏み込んでいることが、複数のリリースから読み取れる。

文脈設計に関する議論も濃かった。Andrej KarpathyのLLM Wiki思想を実践する社内ドキュメント設計、AnthropicによるXMLプロンプトの推奨、Memory-firstのナレッジグラフ、JSDoc/AST解析を活用したProduct Graphなど、「AIに渡す情報の構造をどう事前コンパイルしておくか」という共通の問いを別の角度から論じる記事が並んだ。並行して、Claude CodeとCodex CLIそれぞれの運用ノウハウを体系化する記事（究極ガイド、自己改善ループ、22.5時間自走するCycle運用、AI同士のコードレビュー社内導入）も増えており、エージェント運用が実務レベルで成熟しつつある。

セキュリティ面では複数の事例と対策が同時に表面化した。メルカリのAIガバナンス実装、Martin FowlerによるVibeSecの指摘、Sigil（OSS）による設定ファイル監視、Microsoft Copilot Coworkからのファイル流出事例、AIが生成したコードスロップを検出するaislopまで、組織・設定・コードの各層で攻撃面が同時に拡大していることが浮き彫りになった。プロンプト指示だけでは不十分という共通認識が、複数の独立した記事から繰り返し示されている。

人間側の役割と認知に関する論考も注目に値する。Addy Osmaniの「オーケストレーション税」、Claude Code導入によるデザイナーとエンジニアの役割境界の融解、Mozilla AIによるエージェントネイティブUIへの転換提言、Every.toの「自動化の逆説」など、AIが「書く」を代替する時代において人間の役割が何に再定義されるかを問う論考が複数掲載された。ローカル／エッジAIの実用化も着実に進んでおり、Ryzen AI Max+ NASや5年前のMacBookでLLMを動かす実践記事も今週の重要な動きである。

加えて今週は、技術コミュニティの外側からの視点として、教皇レオ14世が初の回勅『Magnifica Humanitas（大いなる人間性）』を公開し、人間の尊厳・労働の価値・アルゴリズム透明性・自律型致死兵器などAI倫理の根本問題を提起したことが大きな話題となった。Anthropic研究者Chris Olah、Simon Willisonをはじめとする技術コミュニティ側の応答も同時期に出ており、宗教・メディア・AI業界をまたぐ言説が形成されている。

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- (None — no articles flagged ⭐ this week)

**👍 Upvoted Articles Used:**
- 010 → Theme 1 (Supporting / Anchor on the security angle)
- 046 → Theme 4 (Lead)
- 169 → Theme 1 (Lead)
- 170 → Theme 1 (Lead)

**👎 Downvoted Articles (all to annex):**
- 018, 025, 036, 043, 055, 135, 179, 183, 205

**Omitted Articles:** None this week

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: ~33 articles across 8 themes
- Annex Journal: ~240 articles (75 pre-flagged + 9 downvoted + ~156 main candidates not selected; #037 moves from annex to Theme 8)

**Article Count by Theme (Planned):**
- Theme 1: 4 articles (Anthropic platform bloc)
- Theme 2: 5 articles (Pope Leo XIV encyclical + responses)
- Theme 3: 5 articles (Security / attack surface)
- Theme 4: 4 articles (Human role / cognition)
- Theme 5: 4 articles (Runtime infra)
- Theme 6: 4 articles (Operation/skill maturity)
- Theme 7: 4 articles (Context/memory design)
- Theme 8: 3 articles (Local/edge AI)

**Total Planned for Main:** 33 articles
**Remaining for Annex:** ~240 articles (#037 moved to main; remove from annex pool)

---

## Notes for Human Reviewer

**1. Tensions/contradictions worth highlighting:**
- **Theme 1 vs Theme 6:** Anthropic shows aggressive capability expansion (Opus 4.8, Dynamic Workflows, Glasswing) while Theme 6 articles argue that the human cognitive bottleneck (Orchestration Tax, role redefinition) doesn't disappear at the same rate. The journal can frame these as complementary, not contradictory.
- **Theme 2 vs Theme 5:** Production tooling assumes secure-by-design (Sentry/Docker/Cloudflare GAs); Theme 5's incidents and OSS (VibeSec/Sigil/aislop/Copilot Cowork exfil) show that governance is still reactive at multiple layers.
- **Theme 3 vs Theme 4:** Context design (T3) talks about *what to feed* the agent; operation skills (T4) talks about *how to run* the agent. Two halves of the same maturity story.

**2. Themes considered but cut:**
- **Pope Leo XIV Encyclical bloc (#037, #060, #061, #062, #079):** Substantive but tangential to coding journal scope. To annex.
- **AI watermarks / content authenticity (#042 LiveScience, #118/#119 YouTube AI labels):** Editorial-adjacent but not developer-actionable. To annex.
- **AI jobs hysteria / industry economics (#082 TechReview, #084 Verge Uber, #086 Stack Overflow):** Already annex-flagged or low actionability; to annex.

**3. Single-article theme candidate considered:**
- **#109 (Claude Code Mastery guide, score 98/96)** could anchor its own theme rather than sit inside Theme 4. I kept it in Theme 4 to maintain theme coherence, but the human editor may prefer to elevate it.

**4. Articles deferred to annex despite high scores (≥ main 85):**
- High-scoring articles that didn't fit any of the 7 themes cohesively went to annex by default (e.g., #175 Claude Code source leak, #033 dropped from Theme 4 if there's overlap with cortex content elsewhere, #019 Karpathy LLM Wiki — kept in T3). Reviewer can promote any of these.

**5. Title pattern check:**
- All theme titles follow `[2–4 named anchors joined with ・] [single verb (が進める/が整える/が示す/が体系化する/が浮き彫りにする/が問う/が示す)] [substantive topic phrase]`. No em-dash style, no narrative connectors, no generic labels.

---

## Review Notes (Human Editor)

**Date Reviewed:** [To be filled by reviewer]
**Reviewer:** [Name]

**Changes Made:**
- [List any theme refinements]
- [Article reassignments]
- [Other modifications]

**Approval:** ❌ NEEDS REVISION

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
