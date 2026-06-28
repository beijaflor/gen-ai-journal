# Editorial Plan - Journal 2026-06-27

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] Human review and refinement
- [x] APPROVED - Ready for STEP_04 curation

> **Revision v2** — テーマ選定を再構成。AIへの抵抗／人間中心への揺り戻し（#304・#305 等）を独立テーマとして追加し、純粋な「AI経済の持続可能性」テーマは抵抗テーマと annex に振り分けた。

---

## Overview

309 sources collected this week. The defining storyline は依然として **ループ／ハーネスエンジニアリング**（Armin Ronacher "The Coming Loop" ⭐）。ただし v2 では、これまで手薄だった「AIへの抵抗と人間中心への揺り戻し」を独立テーマとして立て、技術トレンド一辺倒ではなく**技術の加速とそれに対する社会・人間側の反応**という両面で週を捉える。

**Proposed main distribution: 8 themes / 25 articles.** Annex は STEP_05 にて、`export_curation_flags.py` 出力の 54 件プリフラグ候補から選定。

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual** (named anchors + single verb + substantive topic phrase).

### Theme 1: Armin Ronacher・サイバネティクス・メタハーネスが問うループエンジニアリングの理論と実装

**Articles (IDs):** 136, 161, 024

**Theme Introduction (Japanese):**
今週もっとも語られた概念が「ループ／ハーネスエンジニアリング」である。Armin Ronacher の "The Coming Loop"（⭐）はハーネスループの普及がソフトウェアを「理解可能な機械」から「有機体」へ変容させると論じ、別の論考は Norbert Wiener のサイバネティクスから読み解いて「理解債務」に警鐘を鳴らす。さらに特化型エージェントを束ねる「メタ・ハーネス」が主流になるとの予測が、この概念の射程を整理する。

**Editorial Notes:**
- 136 (⭐ LEAD): The Coming Loop — ハーネスループ普及によるソフトウェアの有機体化（Armin Ronacher）
- 161: ループエンジニアリングをサイバネティクスで読み解き理解債務に警告
- 024: 特化型エージェントと統合層＝メタ・ハーネスが主流化するとの予測
- *Promote candidates:* 299 (Polygraph メタハーネス製品), 099 (elvis 実践入門), 291 (Pi self-harness), 279 (反対論：自走時間より外部フィードバック)

---

### Theme 2: Martin Monperrus・Mitchell Hashimoto・ヘンリーが示すコードレビューの再定義

**Articles (IDs):** 140, 268, 155

**Theme Introduction (Japanese):**
AIエージェントが生成するコード量が人間のレビュー能力を上回るなか、レビューの主体そのものが問い直されている。Martin Monperrus はエージェントが人間検査を凌駕したとしてレビューからの人間排除を提唱し、ヘンリーは実際に AI へ Approve 権限を与えて PR を倍増させた。一方 Mitchell Hashimoto は、生成コードを理解せず通さない姿勢こそ一流の境界線だと説く。

**Editorial Notes:**
- 140: コードレビューの終焉 — 人間排除の提唱（Martin Monperrus）
- 268: AI に PR 承認権限を付与し PR 倍増・レビュー負荷減（ヘンリー）
- 155: AI 後も深く読む姿勢が一流の境界線（Mitchell Hashimoto）
- *Promote candidates:* 222 (コードレビュー人間幻想・広木大地), 111 (検証プロセス設計・松尾研), 248 (AI時代こそコードを読もう・LayerX), 286 (AIレビュー後に人間アサイン)

---

### Theme 3: mizchi・安宅和人が問うエンジニアの役割再定義と言語化の価値

**Articles (IDs):** 070, 010, 008

**Theme Introduction (Japanese):**
AI が一次的にコードを消費する時代に、人間のエンジニアの価値はどこへ向かうのか。mizchi は技術記事と言語化の意義、そして専門家としてのプログラマの価値が暗黙知の言語化に移ると論じる。受託開発の現場では、AI による供給過剰のなかでエンジニアの生存戦略が問われている。

**Editorial Notes:**
- 070 (⭐): 技術記事、専門家としてのプログラマ、言語化（mizchi）
- 010: AI 時代のプログラマ価値は暗黙知の言語化へ（mizchi）
- 008: AI 以後の受託システム開発はどうなるか（供給過剰と生存戦略）
- *Note:* 070 と 010 は同一著者（mizchi）の関連論考。片方を annex に回す選択も可。
- *Promote candidates:* 016 (ゼロイチの仕事の終わり), 226 (AI時代のリーダーシップ・安宅和人), 249 (正しそうな言葉への違和感), 287 (詳しくない領域でAIを使う・konifar), 309 (カオナビCTO — Theme 7 と重複可)

---

### Theme 4: GLM-5.2・アリババ蒸留問題・価格破壊が進める安価な知能への移行

**Articles (IDs):** 186, 081, 189

**Theme Introduction (Japanese):**
中国発オープンモデルが商用最先端に肉薄し、知能の価格が崩れ始めた。Nathan Lambert らは GLM-5.2 をオープンの転換点と評価し、実機比較では Claude Opus に劣るものの約 1/5 のコストで実用に達する。その裏で Anthropic は Alibaba による Claude の蒸留を米政府に告発し、HackerNews では中国トークン再販経済の実態と二重基準への賛否が交わされた。

**Editorial Notes:**
- 186: GLM-5.2 はオープンの転換点、安価な知能を普及（Nathan Lambert）
- 081: GLM-5.2 対 Claude Opus 4.8 — Opus が精度で圧勝、GLM は 1/5 コスト
- 189 (👍): アリババ蒸留主張への賛否と中国トークン再販経済の議論（HN）
- *Promote candidates:* 241 (AIモデル価格の劇的下落予測), 264 (OpenCode で中国製モデル活用), 187/188 (Anthropic の Alibaba 告発・一次報道), 211 (トークン支出が人件費超え)

---

### Theme 5: Mythos・Five Eyes・プリンシパルドリフトが突きつけるAIエージェントのセキュリティ課題

**Articles (IDs):** 260, 254, 168

**Theme Introduction (Japanese):**
攻撃側の AI が現実の脅威になりつつある。Anthropic の Mythos が米機密システムの脆弱性を数時間で発見し、Five Eyes は数ヶ月内に壊滅的な AI 悪用攻撃が起こりうると警告した。同時に、エージェントの権限と責任の乖離（プリンシパル・ドリフト）という構造的課題が、推論監査と新たなガバナンス組織の必要性を浮き彫りにする。

**Editorial Notes:**
- 260: Mythos が米機密システムの脆弱性を数時間で発見、規制と緊張高まる
- 254: Five Eyes が壊滅的 AI サイバー攻撃を警告（Claude Mythos / CISA）
- 168: プリンシパル・ドリフト — 権限と責任の乖離に推論監査を提唱
- *Promote candidates:* 144 (プロンプト注入＝ロール混同の根本原因), 134 (OpenAI Daybreak / GPT-5.5-Cyber), 156 (ZOZO の SOC 自動化), 247 (817スキル集)

---

### Theme 6: AI Resist List・Mindful Design・Krugmanに見るAIへの抵抗と人間中心への揺り戻し  ⟵ NEW

**Articles (IDs):** 305, 306, 304, 307

**Theme Introduction (Japanese):**
AI の急速な浸透に対し、明確な揺り戻しと抵抗の動きが可視化されている。Karen Hao らの「AI Resist List」は AI 帝国主義への抵抗運動と代替案を体系化し、Scott Riley は「人間による人間のためのデザイン」として AI を一切使わない宣言を掲げる。一方でデザインシステムの作者が AI へ移りガバナンスとトレーサビリティが崩れるという現場の危機が、「なぜ皆 AI を嫌うのか」（Paul Krugman）という問いと響き合う。

**Editorial Notes:**
- 305: AI Resist List — AI帝国主義への抵抗運動と代替案を体系化（Karen Hao, Nightshade, JMITU）
- 306: 人間による人間のためのデザイン — AIを一切使わない反AIデザイン宣言（Scott Riley, Mindful Design）
- 304: デザインシステムの新作者はAI — AIが書き手化しガバナンス・トレーサビリティが崩壊（Figma MCP, DESIGN.md）
- 307: なぜ皆AIを嫌うのか — 黙示録的マーケや強制導入など5要因の分析（Paul Krugman）
- *Promote candidates:* 275 (AIへの反発は始まったばかり・Economist), 091 (ソフト開発・採用市場の崩壊と尊厳喪失), 276 (AI業界が選挙に巨額投資・Blood in the Machine), 093 (AIのPR問題・David Rosenthal), 306/305 が leads

---

### Theme 7: カオナビ・グッドパッチ・Uzabaseに見る日本企業の組織的AI実装

**Articles (IDs):** 309, 258, 263

**Theme Introduction (Japanese):**
個人のツール活用から、組織としての AI 実装へと焦点が移っている。カオナビの CTO は AI 前提でエンジニアの役割が Why/What へ移ると語り、グッドパッチはデザイナー 15 人規模でコンテキストを集約して Claude Code を運用する。Uzabase は Claude スキルで SLO 違反調査を数時間から 25 分へ短縮した。

**Editorial Notes:**
- 309: カオナビ CTO が語る生存戦略 — 役割の Why/What への移行
- 258: デザイナー 15 人のコンテキスト集約による Claude Code 運用（グッドパッチ）
- 263: Claude スキルで SLO 対応を 25 分に短縮（Uzabase）
- *Promote candidates:* 203 (日本企業はAIを使いこなせるか・三つの壁), 069 (「動かす」で止まる日本・Japan AI Index), 156 (ZOZO SOC), 191 (LayerX 内製ロープレ)

---

### Theme 8: OpenAIが描く知識労働の変革とGPT-5.6 Sol新世代モデル

**Articles (IDs):** 269, 290, 272

**Theme Introduction (Japanese):**
OpenAI は、知識労働が単発の対話から長時間タスクの委譲へ移行するとのレポートを公表した（⭐）。同時に次世代モデル GPT-5.6 Sol/Terra/Luna をプレビュー発表したが（⭐）、トランプ政権の安全保障要請を受けて公開を限定プレビューへ切り替えるという、技術と地政学の交差も露わになった。

**Editorial Notes:**
- 269 (⭐): エージェントが仕事を革新する — 知識労働の長時間タスク委譲（OpenAI）
- 290 (⭐): GPT-5.6 Sol プレビュー発表 — 推論強化と ultra mode を備える3層
- 272: 安保要請で GPT-5.6 公開を限定プレビューへ切替
- *Single-focus theme:* OpenAI を軸とした 3 記事構成。STEP_08 では編集者の声で「フロンティアの動きと地政学」を補う。

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週の中心概念は「ループ／ハーネスエンジニアリング」である。Armin Ronacher の "The Coming Loop" は、ハーネスループの普及でソフトウェアが「理解可能な機械」から「有機体」へ変容すると論じ、これをサイバネティクスから読み解く論考やメタ・ハーネスの予測が一つの概念群を形成した。一方で「自走時間より外部フィードバックの情報量が重要」とする反対論もあり、熱狂と冷静が同居している。

この変化はコードレビューとエンジニアの役割を直撃する。Martin Monperrus は「コードレビューの終焉」を唱え、ヘンリーは AI に PR 承認権限を与えた。対して Mitchell Hashimoto は「生成コードを理解して通す」姿勢を一流の条件とし、mizchi は価値の源泉が暗黙知の言語化へ移ると説く。実装から検証・判断・言語化へ——人間の仕事の輪郭が引き直されている。

モデル経済も転換点にある。GLM-5.2 などオープン／中国系モデルが商用最先端に迫り知能の価格を崩す一方、Anthropic は Alibaba による Claude 蒸留を米政府に告発した。安価な知能の普及と、それを巡る正統性・地政学の緊張が同時に進行している。

そして今週は、加速する AI に対する**揺り戻し**がはっきりと姿を現した。Karen Hao らの「AI Resist List」や Scott Riley の反 AI デザイン宣言は人間中心の実践を掲げ、デザインシステムの作者が AI へ移りガバナンスが崩れる現場の不安が、「なぜ皆 AI を嫌うのか」という Krugman の問いと重なる。技術の前進と、それを受け止める人間・社会側の抵抗——その両面が今週の核である。

足元では実装と防御も進む。Anthropic の Mythos が米機密システムの脆弱性を数時間で見つけ、Five Eyes が警告を発する一方、カオナビ・グッドパッチ・Uzabase ら日本企業は組織としての AI 運用を具体化し、OpenAI は知識労働の変革レポートと GPT-5.6 を示しつつ安全保障による公開制限に直面した。

**Key Points to Cover:**
1. ループ／ハーネスエンジニアリングの理論化（Ronacher, サイバネティクス, メタハーネス）と反対論
2. コードレビューの再定義とエンジニアの役割（実装→検証・判断・言語化, mizchi）
3. GLM-5.2／安価な知能の台頭と Anthropic 対 Alibaba 蒸留問題
4. **AIへの抵抗と人間中心への揺り戻し（AI Resist List, 反AIデザイン, Krugman, AI著者化のガバナンス崩壊）**
5. AIエージェントのセキュリティ（Mythos・Five Eyes）と日本企業の組織的実装
6. OpenAI の知識労働変革と GPT-5.6、安全保障による公開制限

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 070 → Theme 3 (Lead)
- 136 → Theme 1 (Lead)
- 269 → Theme 8 (Lead)
- 290 → Theme 8 (Supporting)

**👍 Upvoted Articles Used:**
- 189 → Theme 4 (Supporting)

**👎 Downvoted Articles (excluded from main; annex/omit only):**
- 019, 060, 101, 122, 196, 201, 267, 282 — いずれも main 採用なし

**Omitted from planning:** export_curation_flags.py は omit フラグ 0 件。残り ~284 件は annex 候補（54件プリフラグ）＋ omitted として STEP_04/05 で振り分け。

**v1→v2 の主な変更:**
- 旧 Theme「IBM・OpenAI IPO延期・Krugmanに見るAI経済の持続可能性と社会的反発」を撤去
- 新 Theme 6「AIへの抵抗と人間中心への揺り戻し」(305, 306, 304, 307) を追加
- 307 (Krugman) を経済テーマ→抵抗テーマへ移動。経済系（139, 115, 239/271）は annex 候補へ

---

## Theme Coverage Summary

**Article Count by Theme (Planned):**
- Theme 1 (ループ/ハーネス): 3
- Theme 2 (コードレビュー再定義): 3
- Theme 3 (エンジニア役割/言語化): 3
- Theme 4 (安価な知能/蒸留): 3
- Theme 5 (エージェントセキュリティ): 3
- Theme 6 (AIへの抵抗/人間中心): 4
- Theme 7 (日本企業実装): 3
- Theme 8 (OpenAI/GPT-5.6): 3

**Total Planned for Main:** 25 articles
**Remaining for Annex:** ~54 pre-flagged candidates (curated in STEP_05); rest omitted

*Note: 各テーマに "Promote candidates" を併記。レビューで主要テーマを厚くしたい場合、これらを main に引き上げて 18–25 の範囲で調整可能。*

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-06-29
**Reviewer:** beijaflor

**Changes Made:**
- v2: AIへの抵抗／人間中心テーマを追加（#304, #305 を含む）。経済テーマを撤去。

**Approval:** ❌ NEEDS REVISION / ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
