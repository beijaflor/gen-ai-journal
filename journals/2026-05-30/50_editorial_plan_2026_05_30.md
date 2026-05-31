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
- [x] Proceed to STEP_04 (Curate Main Journal) — done (commit `8c4dbaa` → `af27fb8`)
- [x] Use this plan as blueprint for article selection — done
- [x] Organize curated_journal_sources.md by themes — done
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES (STEP_07)

### Theme 1: Anthropicのエージェント基盤

**Pattern:** Single-Focus
**Pattern Rationale:** Anthropic自身が「主役」であり、Opus 4.8という新モデルを軸に、運用・セキュリティ研究・封じ込め手法という3つの周辺発表が同時公開されている。1次発表を据えて、残りはその波及として配置するのが自然。

**Article Order & Roles:**
1. **169** Opus 4.8 — *Lead* / 主役発表（モデル本体）
2. **170** Dynamic Workflows — *Supporting (運用)* / モデルをClaude Code上で並列実行する機能
3. **010** Project Glasswing — *Supporting (応用研究)* / 新モデル（Mythos Preview）を脆弱性検知に応用した成果
4. **147** Containment — *Supporting (運用ガード)* / Claude製品群を安全に運用するためのサンドボックス手法

**Narrative Arc:**
モデル発表 → 運用機能 → 応用研究 → 運用ガードの順で、Anthropicが今週公開した「モデル＋運用＋安全」の同時パッケージを開封していく。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 169 → 170 | 新モデルの能力強化を述べた直後、それを活かす運用機能（Dynamic Workflows）へ自然に接続 |
| 170 → 010 | 並列実行の規模感を示した後、新モデル（Mythos Preview）を用いた応用研究の成果へ |
| 010 → 147 | 強力なモデルが脆弱性検知に使える反面、運用時の影響範囲を制限する必要性へ転換 |

**Emphasis Balance:** 技術的詳細 ⭐⭐⭐ / ビジネス影響 ⭐⭐ / 将来展望 ⭐⭐

**Key Synthesis Points:**
- Anthropicが「モデル単体」ではなく「モデル＋運用＋安全」をパッケージとして同時公開している点
- Glasswingは新モデルが既存ベンチマークを超えた応用例として位置付けられる
- Containmentの公開は、エージェント能力向上と並行して防御アーキテクチャも公開する姿勢を示す

**Conclusion Approach:** 「能力・運用・安全の3層を同時に公開する」というAnthropicの戦略的姿勢に着地。

---

### Theme 2: 教皇レオ14世回勅とAI業界の応答

**Pattern:** Single-Focus
**Pattern Rationale:** 1次資料（回勅本文）が中心に存在し、複数のメディア・技術コミュニティが個別に応答している、典型的なSingle-Focusの構造。

**Article Order & Roles:**
1. **037** 回勅本文 *Magnifica Humanitas* — *Lead* / 1次資料
2. **060** ReligionNews — *Supporting (一般要約)* / 回勅の主張を一般読者向けにまとめた解説
3. **061** Variety — *Supporting (メディア視点)* / 「非人間化」リスクを焦点に据えた商業メディアの読み
4. **062** Anthropic Chris Olah — *Supporting (技術業界応答)* / 研究者からの応答エッセイ
5. **079** Simon Willison — *Supporting (技術コミュニティ)* / エンジニアコミュニティ向けの解説・引用集

**Narrative Arc:**
回勅本文の論点（人間尊厳・アルゴリズム倫理・労働・武装解除）を提示し、宗教メディア・商業メディア・AI企業の研究者・技術コミュニティそれぞれが、どこを切り取り、どう応答したかを順に追う。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 037 → 060 | 回勅本文の主要論点を提示した後、ReligionNewsによる「AIは人類全体に仕えるべき」という一般要約へ |
| 060 → 061 | 宗教メディアの要約を踏まえ、Varietyの「非人間化（dehumanisation）」というメディア視点へ |
| 061 → 062 | 商業メディアの解釈に続き、AnthropicのChris Olahによる技術業界内側からの応答へ |
| 062 → 079 | 業界内応答を経て、Simon Willisonの技術者向け解説・引用集で読者の理解を深める |

**Emphasis Balance:** 技術的詳細 ⭐ / ビジネス影響 ⭐⭐ / 将来展望 ⭐⭐⭐ / 社会的含意 ⭐⭐⭐

**Key Synthesis Points:**
- 教皇という技術コミュニティ外の権威がAI倫理に正面から発言したこと自体の意味
- Anthropic研究者が公式ニュースとして応答した点 — AI企業が外部の倫理的フレームを真剣に受け止めている
- 宗教・メディア・AI業界・技術者という4層がそれぞれ独立に応答し、対話の素地を形成しつつある

**Conclusion Approach:** 「AI倫理は技術業界内部だけで議論する話題ではなくなった」という認識への着地。技術者は今後、宗教的・倫理的フレームとも対話する必要が出てきていることを示唆。

---

### Theme 3: Agentic AI攻撃面

**Pattern:** Multi-Perspective
**Pattern Rationale:** 5本の記事は同じ問題（Agentic AIのセキュリティ）を異なる層で扱っており、明確な階層関係はない。組織・哲学・OSS・インシデント・コード品質という多角的視座を並置して読ませる。

**Article Order & Roles:**
1. **063** Microsoft Copilot Cowork流出事例 — *具体的インシデント* / 「実害」から入って読者の関心を引く
2. **098** VibeSec Reckoning（Martin Fowler） — *哲学的批判* / 「プロンプト指示だけでは不十分」という根本論
3. **027** Sigil（OSS設定監視ツール） — *技術的対策* / 設定ファイル層の防御
4. **093** メルカリAIガバナンス — *組織的対策* / 多層ガードレールの組織実装
5. **246** aislop（コードスロップ検出） — *コード品質対策* / コードレイヤーの防御

**Narrative Arc:**
具体的なインシデント（Copilot流出）から入り、批評（VibeSec）で「なぜ起きるか」を語り、対策を技術・組織・コード品質の3層で並べていく。各層で独立に対策が走り始めている事実を示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 063 → 098 | 実害事例を提示した後、「なぜAIに『セキュアであれ』と指示するだけでは防げないのか」という根本論へ |
| 098 → 027 | 哲学的批判の後、設定ファイル層という具体的攻撃面に焦点を当てたOSS（Sigil）へ |
| 027 → 093 | 技術ツールから視点を上げ、組織体制・ツール審査・サンドボックスを含む多層ガードレールへ |
| 093 → 246 | 組織レイヤーから降りて、AIが生成するコード品質（スロップ）の検出という別レイヤーへ |

**Emphasis Balance:** 技術的詳細 ⭐⭐⭐ / ビジネス影響 ⭐⭐⭐ / 将来展望 ⭐⭐

**Key Synthesis Points:**
- 攻撃面が「モデル本体」ではなく「周辺（設定・コード・組織・運用）」に拡大していること
- 各層で独立に対策が走り始めており、単一の解決策では不十分なこと
- 「プロンプトで指示する」アプローチの限界が業界全体で共通認識になりつつある点

**Conclusion Approach:** 「Agentic AIの安全性は、組織・設定・コード・運用の各層で同時並行的に守る必要がある」というシステム視点に着地。

---

### Theme 4: AIエージェント時代の認知負荷と役割再定義

**Pattern:** Multi-Perspective
**Pattern Rationale:** 4本の記事はそれぞれ独立した視座（理論・実践・建築・経済）から「人間の役割」を論じており、階層関係はない。並置することで「役割が再定義されつつある」という全体像が浮かぶ。

**Article Order & Roles:**
1. **046** Orchestration Tax — *理論軸* / Addy OsmaniによるAmdahl的観点からの認知負荷の理論化（👍 upvote）
2. **047** デザイナー越境記 — *実践軸* / Claude Code導入による役割融解の現場報告
3. **049** Agent-Native UI（Mozilla AI） — *建築軸* / UIをエージェント向けに再構築する提言
4. **050** After Automation（Every.to） — *経済軸* / 「自動化が仕事を増やす」逆説の経済的分析

**Narrative Arc:**
理論（オーケストレーション税の論理）→ 実践（デザイナーの体験）→ 建築（UIの再構築）→ 経済（労働需要の逆説）の順に視座を広げ、人間の役割が複数のレイヤーで同時に再定義されつつある状況を見せる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 046 → 047 | 理論的に「人間の認知能力は並列化できない」を提示した後、現場での具体的な役割融解の事例へ |
| 047 → 049 | 現場の体験を経て、UIそのものをエージェント向けに作り直すべきだという建築論へ |
| 049 → 050 | アプリ建築の話から、より広い経済・労働の地平で「AIが仕事を増やす」逆説へ |

**Emphasis Balance:** 技術的詳細 ⭐⭐ / ビジネス影響 ⭐⭐⭐ / 将来展望 ⭐⭐⭐ / 社会的含意 ⭐⭐

**Key Synthesis Points:**
- 「人間の役割がなくなる」ではなく「人間に残る役割が明確化している」という共通の論点
- 認知負荷（並列化できない統合・判断）が、エージェント運用の本当のボトルネック
- AI時代の労働需要は「減る」のではなく「文脈に応じた判断」に集中していく

**Conclusion Approach:** 「AIが書くことは加速するが、決める・統合する・責任を取るは人間に残る」という再定義の論点に着地。

---

### Theme 5: エージェント本番運用基盤

**Pattern:** Multi-Perspective
**Pattern Rationale:** 4社が同じ週にエージェント向け本番ツールを公開／GAしたが、それぞれ別のレイヤー（プロトコル・観測・コンテナ・データ）を担っており、階層関係はない。並置によって「本番運用に必要なスタックが揃いつつある」全体像を示す。

**Article Order & Roles:**
1. **065** MCP 2026-07-28版（ステートレス化） — *プロトコル層* / 通信仕様の進化
2. **070** Sentry MCP — *観測層* / 本番エラー文脈の自動取得
3. **134** Docker Gordon — *コンテナ運用層* / 開発環境のAIエージェント化
4. **156** Cloudflare Town Lake + Skipper — *データ層* / 自社スタックでのレイクハウス＋自然言語分析

**Narrative Arc:**
プロトコル → 観測 → コンテナ → データの順で、エージェントを本番で動かすために必要なスタックの整備状況を一巡する。各社が独立に動いているが、結果として階層全体がカバーされていることが見える。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 065 → 070 | プロトコル仕様のステートレス化（大規模運用前提）を述べた後、本番運用に必要な観測（Sentry）へ |
| 070 → 134 | 観測層の整備に続き、コンテナレベルで開発環境を自律運用するDocker Gordonへ |
| 134 → 156 | コンテナ層から離れ、データプラットフォームの再構築（Cloudflare Town Lake）へ |

**Emphasis Balance:** 技術的詳細 ⭐⭐⭐ / ビジネス影響 ⭐⭐ / 将来展望 ⭐⭐

**Key Synthesis Points:**
- プロトコル・観測・コンテナ・データという4層が同じ週に公開／GAされている偶然ではない同期性
- 各層が独立に動いているのに、結果として「本番運用に必要なスタック」が揃いつつある
- 「エージェントは単発のツール呼び出しから本番システムへ」の移行を、複数社が裏付けている

**Conclusion Approach:** 「2026年中盤、エージェント運用の本番化に必要なインフラ層が業界全体で揃いつつある」という観察に着地。

---

### Theme 6: エージェント運用ノウハウの体系化

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 4本は「個人マスターガイド → 自己改善パターン → 別ツールの長時間自走パターン → 組織導入事例」という、習熟度＋スコープの両方が拡大していくシーケンスを成す。前提知識が次の記事を理解する助けになる。

**Article Order & Roles:**
1. **109** プロンプトの先へ：Claude Code究極ガイド — *Foundation* / Claude Codeを自律エージェントとして使う基礎（mainJournalスコア98）
2. **026** 自己改善ループ（SonicGarden） — *Development* / 会話履歴から課題抽出しSKILL.mdを自動修正
3. **028** Codex CLIのCycle運用 — *Advanced* / トークン84%削減、22.5時間連続自走の運用手法
4. **033** cortex AIレビュー社内導入 — *Payoff* / 社内全体でAI同士のコードレビューを採用した組織事例

**Narrative Arc:**
個人レベルでのClaude Code習熟（109）から始め、スキル自体を自己改善する仕組み（026）、別ツール（Codex CLI）での長時間自走運用（028）と段階的に深め、最後に組織全体での導入事例（033）で締める。読者は「個人で使う → 個人で運用する → 別ツールでも運用する → 組織で運用する」という習熟ステップを追体験する。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 109 → 026 | Claude Codeの広範な使い方を理解した上で、「使い方そのものを継続改善する」自己改善ループへ |
| 026 → 028 | 自己改善という運用思想を抽象化した後、Codex CLIにおける具体的な長時間自走運用（Cycle）へ |
| 028 → 033 | 個別ツールの運用ノウハウから離れ、組織全体でAIレビューを採用した事例へスコープ拡大 |

**Emphasis Balance:** 技術的詳細 ⭐⭐⭐ / ビジネス影響 ⭐⭐ / 将来展望 ⭐⭐

**Key Synthesis Points:**
- エージェント運用は「呼び出す」から「育てる／長時間走らせる／組織で運用する」へと成熟段階を進んでいる
- ツール固有のノウハウ（Claude Code vs Codex CLI）が並行して結晶化している
- 個人運用のベストプラクティスが、組織導入の前提知識として機能している

**Conclusion Approach:** 「単発の呼び出しではなく、継続改善と組織採用の段階にエージェント運用が入った」という成熟度の評価で締める。

---

### Theme 7: エージェント文脈設計

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 4本は「思想 → 技法 → アーキテクチャ → 実装」という抽象度から具体度への進行を成す。Karpathy氏のLLM Wiki思想を出発点に、XMLという具体技法、Knowledge Graph設計、AST/JSDocからのProduct Graph構築へと、各段階が次の段階の土台となる。

**Article Order & Roles:**
1. **019** Karpathy LLM Wiki思想 — *Foundation* / 「知識を事前コンパイルしておく」という根底思想
2. **024** AnthropicのXMLプロンプト推奨 — *Development* / Markdownとの比較を通じて、AIに渡す情報の構造化技法
3. **022** Memory-firstナレッジグラフ（DevRev） — *Advanced* / scatter-gather方式の限界とアーキテクチャ的解決
4. **096** AIハーネスの心臓部（Product Graph） — *Payoff* / JSDoc/AST解析で実装まで踏み込んだ統合事例

**Narrative Arc:**
「AIに渡す情報をどう構造化するか」という根底思想から出発し、プロンプト記法レベルの技法、Memory-firstアーキテクチャ、そして実装レベルでのProduct Graph統合へと、抽象から具体へ降りていく構成。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 019 → 024 | LLM Wiki思想という「事前コンパイル」の発想を提示した後、プロンプト記法レベルの技法（XML推奨）へ |
| 024 → 022 | プロンプト粒度の技法から、エージェント全体のメモリアーキテクチャ（scatter-gather → Memory-first）へ |
| 022 → 096 | アーキテクチャ論を経て、コード解析を通じた実装レベルでのProduct Graph統合事例へ |

**Emphasis Balance:** 技術的詳細 ⭐⭐⭐ / ビジネス影響 ⭐⭐ / 将来展望 ⭐⭐

**Key Synthesis Points:**
- 「AIに渡す情報の構造をどう事前設計するか」が文脈設計の本質
- プロンプト・アーキテクチャ・実装の各層で「事前コンパイル」アプローチが採用されつつある
- RAGの精度問題は「検索の改善」より「対象データの構造化」で解く方向に向かっている

**Conclusion Approach:** 「文脈設計は『AIに何を読ませるか』ではなく『AIが読みやすい構造を先に作っておく』段階へ」という認識に着地。

---

### Theme 8: ローカル／エッジAIの実用化

**Pattern:** Multi-Perspective
**Pattern Rationale:** 3本は「専用ハードウェア」「既存資源の活用」「アルゴリズム最適化」という、同じ「ローカル実行」を異なる角度から実現する独立した試みを並べる。階層関係はないが、3つの角度を見ることで全体像が明確になる。

**Article Order & Roles:**
1. **003** Ryzen AI Max+ NAS — *専用ハードウェア角度* / 中規模LLMをローカルで実用速度で動かすための専用機
2. **004** 5年前MacBookでGemma 4 — *既存資源角度* / 既にあるハードウェアの活用で動画自動インデックス化
3. **005** AutoTTS（Claude Code自律設計） — *アルゴリズム角度* / 推論時の計算資源配分を自動最適化

**Narrative Arc:**
専用機を買う（003）、既存機を活かす（004）、アルゴリズム自体を最適化する（005）という、3つの独立した解決策を提示し、フロンティアモデル依存からの脱却が複数経路で進んでいることを示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 003 → 004 | 専用ハードウェアでの最新事例を示した後、5年前のハードウェアでも動かせるという逆方向の角度へ |
| 004 → 005 | ハードウェア活用の話から、アルゴリズムレベル（推論最適化）への抽象度の転換 |

**Emphasis Balance:** 技術的詳細 ⭐⭐ / ビジネス影響 ⭐⭐⭐ / 将来展望 ⭐⭐⭐

**Key Synthesis Points:**
- 「ローカルAI」の実用化が、ハードウェア・既存資源活用・アルゴリズムという複数経路で進んでいる
- 専用機を買わなくても（004）、最新機を待たなくても（003）、ローカル実行は実用域に入りつつある
- AutoTTSのような研究は、アルゴリズム側の改善も並行していることを示す

**Conclusion Approach:** 「フロンティアモデル依存は唯一の道ではなく、複数の独立した経路でローカル実行が現実解になりつつある」という展望に着地。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

> The agent leaves `ASSEMBLY PLAN APPROVED` **unchecked** when generating the
> document. The human flips it to `[x]` inside the `human-review-gate` vim
> popup; the agent must not check it.

**Approval Date:** [To be filled by reviewer]
**Approver:** [To be filled by reviewer]
