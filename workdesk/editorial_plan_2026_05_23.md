# Editorial Plan - Journal 2026-05-23

## Planning Status
- [ ] Initial theme identification (AI-assisted)
- [ ] Human review and refinement
- [ ] Theme introductions drafted
- [ ] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

### Theme 1: Addy Osmani・dely・Codex・Google Skillsが具体化するハーネス／Agent Skills設計

**Articles (IDs):** 057, 065, 154, 254, 077

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントの性能はモデル単体ではなく「ハーネス」と「Skills」の設計で決まるという議論が、Addy OsmaniのO'Reilly寄稿、クラシルのRailsチームによる失敗のチームルール昇格、Codexサブエージェントによる実装・レビュー分業、Google公式Agent Skillsリポジトリ、子ども向けアプリ開発における「作らない判断」など、複数の実装事例として共有された週となった。理論と現場実装の両面からハーネス／Skills時代の設計原則を確認する。

**Editorial Notes:**
- 057: dely_jp 👍 – `FAILURES.md`蓄積と`/failure-promote`コマンドでルール昇格する仕組み
- 065: mrksye 👍 – AIの提案に対し人間が「責務」で引き算を決める設計思想
- 154: acro-engineer 👍 – Codexサブエージェントによる実装・レビュー分業の設定方法
- 254: O'Reilly – Addy Osmani「Agent = Model + Harness」の体系的整理
- 077: Google Cloud – `npx skills install`で導入可能なAgent Skills公式リポジトリ

---

### Theme 2: Agent View・Fast Mode・VS Code 1.120・Anthropic公式ガイド・cafleetが拡張するエージェント実行環境

**Articles (IDs):** 106, 162, 247, 252, 259

**Theme Introduction (2-3 sentences in Japanese):**
Claude Codeの「Agent View」「Fast Mode」、VS Code 1.120のAgentsウィンドウStable化、Anthropic公式の大規模コードベース向け運用ガイド、そしてTmux+SQLiteで自作されたマルチエージェント協調ツール「cafleet」と、複数エージェントの並列実行と監視を整える機能・知見が同時期に揃った。個別ツールが追従する周辺機能と、自作で補う実装パターンの両方を確認できる構成。

**Editorial Notes:**
- 106: himkt 👍 – Tmux+SQLiteで自作したClaude Code/Codex対応の協調ツール「cafleet」
- 162: Anthropic – `claude agents`コマンドとPeek機能による複数セッション一括管理
- 247: Anthropic – Opusの応答を2.5倍に高速化する「Fast Mode」のコスト体系と管理機能
- 252: Microsoft – VS Code 1.120でマルチプロジェクト対応Agentsウィンドウが安定版に
- 259: Anthropic – 数百万行規模コードベース向けの5つのハーネス拡張ポイントとLSP統合

---

### Theme 3: antirez DS4・nowokay・jolaが示すローカルLLMの「実用域」到達

**Articles (IDs):** 019, 049, 196, 294

**Theme Introduction (2-3 sentences in Japanese):**
DeepSeek V4 FlashをローカルでホストするantirezのDS4プロジェクト、家庭用GPU環境での3年間の進化を振り返るnowokay氏の解説、24GB M4 MacBook ProでのQwen 3.5-9B運用、ローカルLLMハードウェア選定ガイドの各記事が、ローカルLLMが対話の成立から商用品質の代替へと到達したことを示している。ハード・モデル・ツールの3面から到達点を確認する。

**Editorial Notes:**
- 019: gizmodo – Qwen3.5やGemma 4を中心とするローカルLLMのエージェント運用の現状
- 049: jola.dev – M4 MacBook Pro 24GBで実用的なQwen 3.5-9B環境を構築する手順
- 196: nowokay – 32GB基準のSoC／GPU別ハードウェア選定ガイド（2026年想定）
- 294: antirez – 2/8ビット非対称量子化と96GB+RAMでフロントエンド級モデルが稼働

---

### Theme 4: LayerX・グロービス・モノタロウ・aircloset・ubieが報告するClaude Code/エージェント本番運用

**Articles (IDs):** 137, 146, 199, 269, 280

**Theme Introduction (2-3 sentences in Japanese):**
LayerXの「バクラク給与」立ち上げ、グロービスのClaude Code 1000セッション分析、モノタロウの内製化プロジェクトのAI視点での振り返り、エアークローゼットによるハーネス整備済みプラットフォーム「cortex」、UbieがLayerXの社内検索向けに構築したAgentic Search VFSと、実際にClaude Codeおよび社内エージェントを運用に乗せた組織からの実装報告が並んだ。コストや精度、組織設計の具体数値を含む知見が確認できる。

**Editorial Notes:**
- 137: LayerX – バクラク給与の立ち上げでAIと人間の責務を切り分け2ヶ月前倒し
- 146: aircloset – ハーネス整備により月間PRマージ数を22倍にしたcortex連載総論
- 199: monotaro – AI時代のレビュー集中とコード理解教育のボトルネックを振り返り
- 269: LayerX – OpenSearch上にbash相当の仮想ファイルシステムを構築しRecall 15.3→41.5%
- 280: globis – Hookで承認待ち40%を削減しリードタイム10%短縮

---

### Theme 5: twada・404 Media・sshh.io・O'Reillyが論じるAI生産性の実像と認知負債

**Articles (IDs):** 012, 088, 122, 175

**Theme Introduction (2-3 sentences in Japanese):**
和田卓人氏のScrum Fest Niigata資料、404 Mediaによる現場開発者の声、Shrivu Shankar氏のAI生産性失敗論、O'RadarのBurnout and Cognitive Debtが、それぞれ異なる立場から「AIによる生成速度と人間の理解速度の乖離」を指摘した。経営層が掲げる効率化の指標と現場が直面する保守負担・スキル衰退の論点を並べて検証する。

**Editorial Notes:**
- 012: twada – `Programming as Theory Building`を引き、認知負債を最大のリスクとして指摘
- 088: sshh.io – 個人・組織の設計不備がAI生産性を阻む構造をデバッグした論考
- 122: O'Reilly – AIエージェント時代のバーンアウトと「動くが理解できない」コード問題
- 175: 404 Media – 大手テック幹部の主張と現場開発者の声の乖離をルポ

---

### Theme 6: 安野貴博・3メガバンク・NIST・OpenMythosが描くClaude Mythosを軸とした攻防の構造変化

**Articles (IDs):** 008, 167, 185, 197, 251

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが攻撃能力を持つ推論特化型モデル「Claude Mythos」の限定公開を進めるなか、日本政府の対応の遅さに苦言を呈する安野貴博党首の発言、3メガバンクのアクセス権取得、NISTによる中国製DeepSeek V4 Proの定量評価、22歳エンジニアによる「OpenMythos」の再現公開、ラックによる構造変化の見解までが同週に並んだ。攻撃・防御・能力評価・再現性のそれぞれの側面から、Mythos登場後の地政学的・技術的な動きを俯瞰する。

**Editorial Notes:**
- 008: itmedia – 安野氏が政府のMythos対応の遅さを批判し、迅速な危機管理体制を要求
- 167: NIST – DeepSeek V4 Proは中国製最高性能だが米国最先端から約8ヶ月遅れと評価
- 185: 日経 – 3メガバンクがMythosのアクセス権を確保、サイバー防衛での日米連携
- 197: sbbit – Kye Gomez氏が公開論文からMythos構造を推定した「OpenMythos」を公開
- 251: ラック – Mythosで攻撃リードタイムが激減し防御側もAI化が急務との提言

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

開発側では、AIエージェントの性能はモデル単体ではなく「ハーネス」「Agent Skills」の設計で決まるという議論が、O'ReillyのAddy Osmani寄稿、クラシルの失敗自動昇格パイプライン、Codexのサブエージェント分業、Google公式Skillsリポジトリといった具体実装として並んだ。同時に、Claude CodeのAgent View／Fast Mode、VS Code 1.120のAgentsウィンドウStable化、Anthropic公式の大規模コードベース運用ガイドなど、複数エージェントの並列実行と監督を整える機能群が出揃った。

実装事例では、LayerXのバクラク給与立ち上げ、グロービスの1000セッション分析、モノタロウの振り返り、エアークローゼットのcortex、Ubie/LayerXのAgentic Search VFSなど、Claude Code／社内エージェントを本番運用に乗せた組織からの知見が共有された。一方で、和田卓人氏、404 Media、sshh.io、O'Reillyが揃って「AI生成速度と人間の理解速度の乖離」「認知負債」「保守コスト爆発」を論じており、生産性の数字と現場の感覚の落差が改めて可視化された。

セキュリティ側では、Anthropicの攻撃能力を備えた推論モデル「Claude Mythos」の限定公開を巡る各国・各社の動きが目立った。安野貴博氏が政府対応の遅さを批判し、3メガバンクがアクセス権を確保した一方で、NISTは中国製DeepSeek V4 Proを「米国最先端から8ヶ月遅れ」と定量評価し、22歳のエンジニアKye Gomez氏は公開論文だけから「OpenMythos」を再現公開した。攻撃・防御・能力評価・再現性が同時に動いた週として記録される。

**Key Points to Cover:**
1. ハーネス／Agent Skills設計が「現場の具体例」を伴って体系化された週
2. 複数エージェントの並列実行と監視を支える機能群（Agent View/Fast Mode/VS Code 1.120/公式ガイド/cafleet）
3. ローカルLLM（DS4・Qwen 3.5・M4 Mac等）が「商用代替」の実用域に到達
4. LayerX・グロービス・モノタロウなど本番運用事例の蓄積
5. AI生産性に対する現場視点の懐疑論（認知負債・保守コスト・スキル空洞化）
6. Mythos登場後の各国・各社・各セキュリティ研究者の同時並行的な動き

---

## Curation Signal Summary

**⭐ Standout Articles Used:** （該当なし — 標準は👍のみ）

**👍 Upvoted Articles Used:**
- 033: 未使用（→ annex候補。Lighthouse Agentic Browsingは独立トピックとして annex 向き）
- 057 → Theme 1（中核アンカー）
- 065 → Theme 1（設計判断面のアンカー）
- 106 → Theme 2（自作ツール面の事例）
- 154 → Theme 1（Codex側のアンカー）

**👎 Downvoted Articles:**
- 032, 053, 062, 064, 093, 131, 149, 198, 200, 218, 272, 273, 279 → 全てメインから除外（annexまたはスキップ）

**Omitted Articles:** 297

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 6-7 themes
- Annex Journal: Remaining articles across 5-6 themes

**Article Count by Theme (Planned):**
- Theme 1: 5 articles (Harness/Skills)
- Theme 2: 5 articles (Tooling UI extension)
- Theme 3: 4 articles (Local LLM)
- Theme 4: 5 articles (Enterprise implementation)
- Theme 5: 4 articles (Cognitive debt)
- Theme 6: 5 articles (Mythos cluster)

*Note: 各テーマ4-5記事構成。最小テーマ4記事のため単一記事テーマの個別justificationは不要。*

**Total Planned for Main:** 28 articles
**Remaining for Annex:** Approximately 230 articles including the 39 already flagged via Supabase

*Note: Main is slightly over 25; suggest dropping 1-2 articles during STEP_04 curation if 24-25 target is strict (candidates to drop: 251 from Theme 6 if LAC overlaps Mythos coverage; 077 from Theme 1 if Google Skills overlaps with 254 manifesto; 049 from Theme 3 if M4 Mac too narrow).*

---

## Review Notes (Human Editor)

**Date Reviewed:** [pending]
**Reviewer:** [pending]

**Changes Made:**
- [pending review]

**Approval:** ⏳ PENDING

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
