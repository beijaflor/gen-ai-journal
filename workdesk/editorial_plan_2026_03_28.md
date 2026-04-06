# Editorial Plan - Journal 2026-03-28

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

### Theme 1: ハーネスエンジニアリング成熟宣言：CLAUDE.mdからSkills・Hooks・Channelsへの大転換

**Articles (IDs):** 004, 032, 039, 048, 050, 052, 065, 155, 165, 172, 184, 199, 207, 212, 230, 236, 242

**Theme Introduction (2-3 sentences in Japanese):**
今週、ハーネスエンジニアリングは単なるバズワードから実装パターンへと決定的に転換した。CLAUDE.mdによる静的な指示から、Skills・Hooks・Channelsを組み合わせた動的な制御アーキテクチャへ――Claude Codeの進化は「AIエージェントをどう飼いならすか」という問いに対する具体的な回答を次々と提示している。5段階の習熟度モデルからコグニティブ・アーキテクチャまで、開発者がエージェントを「同僚」として扱うための設計言語が急速に整備されつつある。

**Editorial Notes:**
- Key insights to emphasize: ハーネスエンジニアリングが「概念」から「実践体系」に移行した転換点
- Connections between articles: 032/039/048が理論、050/165/172/242が実装パターン、052/236が成熟度・チーム論
- Potential challenges: 記事数が多すぎるため、最も本質的な5-6本に絞る必要あり
- Lead candidates: 048 (Agent Autonomy), 212 (運用設計), 242 (Hooks 3層プロンプト)

---

### Theme 2: LiteLLM侵害とROT脅威：AIサプライチェーンが開いたパンドラの箱

**Articles (IDs):** 055, 072, 099, 111, 133, 144, 187, 196, 237

**Theme Introduction (2-3 sentences in Japanese):**
3月24日に発覚したLiteLLMのサプライチェーン侵害は、AIエージェント時代のセキュリティが「理論的リスク」から「現実の脅威」に変わった象徴的事件だ。ROT（Rogue Operator Threat）、NHI（Non-Human Identity）管理、AIエージェント専用サンドボックス――今週の記事群は、自律的に動くエージェントが持つ「認証情報」と「実行権限」をどう守るかという、従来のセキュリティモデルでは対応しきれない新しい課題を浮き彫りにしている。

**Editorial Notes:**
- Key insights to emphasize: LiteLLM侵害は具体例、ROT/NHI/sandboxは構造的対策
- Connections between articles: 072が事件報告、055が脅威モデル、099/144がサンドボックス、196がNHI管理
- Potential challenges: セキュリティ記事は技術的に深くなりがちだが読者のレベル感に合わせる
- Lead candidates: 072 (LiteLLM侵害), 055 (ROT脅威)

---

### Theme 3: Taktの5敗に学ぶ：マルチエージェント協調は「オーケストラ」ではなく「ジャズセッション」

**Articles (IDs):** 010, 014, 043, 053, 082, 092, 108, 121

**Theme Introduction (2-3 sentences in Japanese):**
マルチエージェント協調は今週、華々しい成功談よりも「失敗から学んだ設計原則」が際立った。Taktが5回の失敗から導いたオーケストレーション設計、131行のPythonで実現する汎用エージェント、そしてエージェント同士のペアプログラミング――これらは「複雑なDAGを組む」のではなく、「シンプルな協調プロトコルを見つける」ことの重要性を示唆している。

**Editorial Notes:**
- Key insights to emphasize: 失敗からの学びが最も実践的な知見を提供している点
- Connections between articles: 014が失敗事例、108がミニマリスト実装、092がペアプロ、053/121がプロジェクト管理
- Potential challenges: 「マルチエージェント」の定義が記事によって異なる
- Lead candidates: 014 (Takt 5 failures), 108 (131 lines agent)

---

### Theme 4: 「AIに飽きた」とガートナー50%拒否：ハイプ疲れが暴く本当の価値

**Articles (IDs):** 021, 068, 093, 098, 127, 131, 142, 146, 178, 201

**Theme Introduction (2-3 sentences in Japanese):**
BlackRockはAIが格差を拡大すると警告し、ガートナー調査では消費者の50%が生成AIを拒否し、あるエンジニアは「AIパーティーから去る」と宣言した。今週のAI批評記事群は、単なるアンチAIではなく「ハイプが隠してきた構造的問題」を正面から突いている。経営層とICの温度差、若者のキャリアへの影響、AIを使うほど判断力が落ちるという逆説――これらの声を無視することは、もはやできない。

**Editorial Notes:**
- Key insights to emphasize: 批判の「質」が変わった――感情的ではなく構造的・データドリブンになっている
- Connections between articles: 201/142がデータ駆動批判、021/093が現場感覚、098が組織論、178が認知科学
- Potential challenges: 批判記事を並べるだけでは暗くなるので、建設的な視点を入れる
- Lead candidates: 201 (ガートナー50%), 142 (BlackRock), 098 (経営層 vs IC温度差)

---

### Theme 5: 100Mトークンの衝撃とAegis 1/12圧縮：コンテキストエンジニアリング最前線

**Articles (IDs):** 006, 025, 028, 040, 054, 112, 194

**Theme Introduction (2-3 sentences in Japanese):**
Memory Sparse Attentionが100Mトークンのコンテキストを現実的なものにする一方、Aegisはトークン使用量を1/12に圧縮するDAGツールで逆方向からの最適化を提示している。「コンテキストウィンドウを広げる」と「必要な情報だけを精密に送る」という二つのアプローチは、対立するように見えて実は補完的だ。コンテキストエンジニアリングは今週、LLM活用の最も実践的なフロンティアとして確立した。

**Editorial Notes:**
- Key insights to emphasize: 拡張と圧縮の両面アプローチが同時に進行している構造
- Connections between articles: 028が拡張側、040/112が圧縮側、006/025/054がメモリ・ナレッジ管理
- Potential challenges: 技術的に深い記事が多いので、読者にアクセシブルな解説が必要
- Lead candidates: 028 (100M token), 040 (Aegis 1/12), 112 (40% token reduction)

---

### Theme 6: 国産LLM三国志：RakutenAI 3.0・PLaMo 3.0 Prime・Sakana「Namazu」の本気度

**Articles (IDs):** 219, 223, 227, 239, 243

**Theme Introduction (2-3 sentences in Japanese):**
楽天のRakutenAI 3.0がDeepSeek V3と互角のベンチマークを叩き出し、Preferred NetworksのPLaMo 3.0 Primeは「長考」で推論精度を高め、SakanaのDoc-to-LoRAは1秒未満でドキュメントをモデルに反映させる。日本発のLLMは「OpenAIの後追い」から脱却し、それぞれが独自の技術的ニッチを確立しつつある。国産LLMは生き残れるのか――今週の成果は、その問いに対する最も具体的な回答だ。

**Editorial Notes:**
- Key insights to emphasize: 各社が異なる技術的アプローチで差別化している点
- Connections between articles: 239/243がRakutenAI比較、219がPLaMo長考、223/227がSakana技術
- Potential challenges: ベンチマーク比較だけにならないよう「なぜ重要か」の視点を入れる
- Lead candidates: 239 (RakutenAI), 219 (PLaMo Prime)

---

### Theme 7: 非エンジニアの「コード革命」：経営者・マーケター・研究者がClaude Codeで手に入れた武器

**Articles (IDs):** 023, 074, 177, 182, 183, 232

**Theme Introduction (2-3 sentences in Japanese):**
プログラミング経験ゼロの経営者がClaude Codeで業務自動化を実現し、マーケターが300%の成長を達成し、物理学の大学院生がClaudeで研究を加速させている。これらは「素人がAIでコードを書けた」という単純な美談ではない――専門知識を持つ非エンジニアが、AIを「翻訳層」として活用することで、従来はエンジニアに依頼するしかなかったタスクを自律的に完了している。プログラミングのデモクラタイゼーションが、具体的な事例として結実した一週間だ。

**Editorial Notes:**
- Key insights to emphasize: 「素人がコードを書けた」ではなく「ドメイン専門家がAIで自律した」という構造変化
- Connections between articles: 023/182/183が非エンジニア事例、074が研究者、232がマーケター
- Potential challenges: 成功バイアスに注意――失敗事例や限界も触れるべき
- Lead candidates: 182 (経営者の業務自動化), 074 (物理研究)

---

## Annex Journal Theme Candidates

### Annex Theme A: Vibe Coding再考：Go言語最適論からコーディングは確率ゲームまで
**Articles:** 106, 128, 134, 153

### Annex Theme B: AIと「味」の問題：クラフト喪失・労働疎外・ロゼッタストーンの意図
**Articles:** 057, 059, 086, 090, 115, 125

### Annex Theme C: Figmaエージェントから GenUIまで：デザイン×AIの現在地
**Articles:** 002, 066, 073, 076, 089, 101, 189, 215

### Annex Theme D: 軍事AIとAI倫理：イラン爆撃・パランティア・AIセラピスト問題
**Articles:** 046, 069, 094, 097, 185, 200, 206

### Annex Theme E: NotebookLM・RAG・ドキュメントAI：知識管理ツールの進化
**Articles:** 030, 067, 104, 157, 180, 208, 209

### Annex Theme F: AI実装の現場報告：ぐるなび・朝日新聞・ドラクエX・三菱重工
**Articles:** 011, 017, 038, 188, 204, 211, 221, 241

---

## Highlight Draft ("今週のハイライト")

**Main Narrative Arc:**

今週のGenAIコーディング界は、「成熟」と「反動」という二つの力が同時に表面化した一週間だった。

一方では、ハーネスエンジニアリングがCLAUDE.mdの静的指示を超えてSkills・Hooks・Channelsという動的制御アーキテクチャへと進化し、コンテキストエンジニアリングは100Mトークンの拡張と1/12圧縮という両面から最適化が進み、国産LLMはそれぞれ独自のニッチを確立しつつある。AIコーディングの「技術基盤」は、明らかに成熟のフェーズに入った。

しかし他方では、ガートナー調査で消費者の50%がAIを拒否し、BlackRockはAIが格差を拡大すると警告し、LiteLLMのサプライチェーン侵害がAIエージェント時代のセキュリティ脆弱性を白日の下に晒した。そしてTaktのマルチエージェント協調は5回の失敗を経てようやく実用的な設計原則を見出し、非エンジニアのClaude Code活用事例は「プログラミングのデモクラタイゼーション」が美談だけでは語れない複雑さを示している。

この「成熟」と「反動」は矛盾ではなく、技術が本格的に社会実装されるフェーズで必然的に生じる緊張関係だ。ハイプが去った後に残るのは、セキュリティ・組織・倫理という「面倒だが不可避な」課題群であり、今週の記事群はまさにその課題に正面から取り組む具体的な試みの集積である。

**Key Points to Cover:**
1. ハーネスエンジニアリングの「概念→実践」転換が決定的になった
2. LiteLLM侵害は「AIエージェントのセキュリティは後回しにできない」ことの証明
3. マルチエージェントの「失敗から学ぶ」フェーズは健全な兆候
4. 消費者・開発者双方の「AI疲れ」は構造的問題の露呈であり一過性ではない

**Cross-Cutting Insights:**
- ハーネスエンジニアリングの成熟とセキュリティ脅威は表裏一体：エージェントの自律性が増すほど、悪用リスクも増大する
- 「非エンジニアのコード革命」とAI批評は同じコインの裏表：AIの力が広がるほど、その影響を問う声も大きくなる
- 国産LLMの差別化戦略は「コンテキストエンジニアリング」の視点で理解すると、単なるベンチマーク競争ではない意味を持つ

---

## Curation Signal Summary

**⭐ Standout Articles (No curation flags available - based on editorial judgment):**
- 072 → Theme 2 (Lead) — LiteLLM侵害：具体的事件で説得力が高い
- 014 → Theme 3 (Lead) — Takt 5つの失敗：失敗事例の赤裸々な共有
- 201 → Theme 4 (Lead) — ガートナー50%拒否：データドリブンな批判
- 028 → Theme 5 (Lead) — 100Mトークン：技術的ブレイクスルー

**👍 Upvoted (editorial judgment):**
- 048, 212, 242 → Theme 1 (Core articles)
- 055, 196 → Theme 2 (Supporting)
- 108 → Theme 3 (Supporting)
- 098, 142 → Theme 4 (Supporting)
- 040, 112 → Theme 5 (Supporting)
- 219, 223 → Theme 6 (Core)
- 182, 074 → Theme 7 (Core)

**Omitted Articles:** None flagged (no curation_flags.md available)

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 22-25 articles across 7 themes
- Annex Journal: Remaining ~30-40 articles across 6 themes

**Article Count by Theme (Planned):**
- Theme 1 (ハーネスエンジニアリング): 5-6 articles (selected from 17 candidates)
- Theme 2 (セキュリティ): 4 articles (selected from 9 candidates)
- Theme 3 (マルチエージェント): 3-4 articles (selected from 8 candidates)
- Theme 4 (ハイプ疲れ): 3-4 articles (selected from 10 candidates)
- Theme 5 (コンテキスト): 3 articles (selected from 7 candidates)
- Theme 6 (国産LLM): 3 articles (selected from 5 candidates)
- Theme 7 (非エンジニア): 3 articles (selected from 6 candidates)

**Total Planned for Main:** ~24 articles
**Remaining for Annex:** ~225 articles (further curation in STEP_05)

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-04-05
**Reviewer:** Human editor

**Changes Made:**
- Reviewed and approved as-is

**Approval:** ✅ APPROVED

---

## STEP_04 Curation Deviations

**Theme 6 corrections:** Original plan referenced IDs 219/223/227/239/243 which were mostly mis-assigned. Corrected to actual Japanese LLM articles:
- Added 255 (RakutenAI 3.0 炎上考察), 225 (PLaMo 3.0 Prime), 235 (Sakana Doc-to-LoRA)
- Kept 230 (Sakana Namazu) — moved from Theme 1

**Theme 3:** Replaced 108 with 114 (the actual "131 lines of Python" article). Dropped 098 (agent-to-agent pair programming) to keep at 3 articles.

**Theme 5:** Trimmed to 3 articles (dropped 120 Aegis enterprise case).

**Theme 7:** Trimmed to 3 articles (dropped 183 frontend-slides repo as weakest fit).

**ID corrections:** Several IDs in the original plan were mis-assigned due to bulk analysis errors. All corrected in curated_journal_sources.md.

**Final distribution:** 26 main articles across 7 themes, 223 remaining for annex.

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
