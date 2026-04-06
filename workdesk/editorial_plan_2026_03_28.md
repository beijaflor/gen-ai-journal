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

---

## ASSEMBLY STRATEGIES

### Theme 1: ハーネスエンジニアリング成熟宣言：CLAUDE.mdからSkills・Hooks・Channelsへの大転換

**Pattern:** Progressive Sequence
**Pattern Rationale:** 各記事が異なる抽象度でハーネスエンジニアリングを扱っており、概念→実装の流れで整理できる。

**Article Order & Roles:**
1. [048] ハーネスエンジニアリング概論 — 「生産性のパラドックス」を提起し、AGENTS.md・リンター・CIを「決定論的ゲート」として再設計する概念を定義
2. [238] Anthropic長時間実行ハーネス設計 — Generator/Evaluator/Plannerの3エージェント体制、自己評価バイアスの克服、コンテキスト不安への対策を具体的に解説
3. [050] 最小構成ハーネス（CLAUDE.md + Skills + Hooks） — 外部ツール不要、標準機能のみで「事前介入」を実現する最小パターン。/translateスキルで日本語指示の手戻りゼロ化
4. [052] 5つの習熟レベル — プロンプト→CLAUDE.md→Skills→Hooks→Agent Teams/batchの5段階を体系化。読者が自分の現在地を把握するためのロードマップ
5. [032] 狩りから稲作へ — hooks/Lefthook/skills/GitHub Actionsの4層で、仕様策定→実装→PR→マージの全工程を仕組み化。「破壊的コマンドのブロック」「先送り表現の検出」など具体的ガードレール実装

**Narrative Arc:**
048が「なぜハーネスが必要か（生産性のパラドックス）」を示し、238がAnthropicの高度な設計例を提示。050は標準機能だけで始められる最小構成、052がそこから先への段階的ロードマップ、032がフルスタック自動化の実例。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [048] → [238] | 048が提唱するAGENTS.md+CIの設計を、Anthropicは3エージェント体制でさらに発展させている |
| [238] → [050] | 238のマルチエージェント構成は高度だが、050はCLAUDE.md+Skills+Hooksの3要素だけで実践可能な最小構成を示す |
| [050] → [052] | 050の最小構成がLevel 2-3相当。052は5段階の全体像を提示し、次に何をすべきかを明確にする |
| [052] → [032] | 052のLevel 4-5を実際に運用した事例。4層自動化とAI特有の挙動（先送り表現等）への具体的対策 |

**Key Synthesis Points:**
- 048の「生産性のパラドックス」（AI導入でレビュー負荷増大）が全記事の出発点
- 238の3エージェント体制（生成・評価・計画）と032の4層自動化は、異なるスケールでの同じ原則：AIの出力を決定論的に検証する仕組み
- 050の「事前介入」と032の「ガードレール」は、事後レビューから事前制御へのシフトという共通思想

**Assembly Prompts for STEP_08:**
1. 各記事の核となる主張・手法をそのまま伝える
2. 読者の習熟度に応じて050（初級）→052（中級）→032（上級）の参照先を示す
3. 048と238の共通点（決定論的ゲート、フィードバックループ）をエディターの声で補足

---

### Theme 2: LiteLLM侵害とROT脅威：AIサプライチェーンが開いたパンドラの箱

**Pattern:** Multi-Perspective
**Pattern Rationale:** 4記事はそれぞれ独立したセキュリティトピック。LiteLLM（サプライチェーン）、ROT（AIエージェントの暴走）、NHI（マシンID管理）という異なる脅威面を並べることで、AIセキュリティの多面性を示す。

**Article Order & Roles:**
1. [072] LiteLLM侵害技術詳報 — TeamPCPによるサプライチェーン攻撃の全容。.pthファイル悪用、SSH鍵/クラウド認証/仮想通貨の窃取、K8s特権Pod展開。IOCとチェックリスト付き
2. [237] LiteLLM対応指針 — 同事件の除染手順に焦点。pip cache purge、systemdバックドア削除、認証情報ローテーション、72時間検疫期間の推奨
3. [055] ROT（Rogue Operator Threat） — ベアリングス銀行破綻を例に、AIエージェントがミスを隠蔽し損害を累積させるリスクを「ROT」と命名。権限制限・メモリリセット・個体交代のガードレールを提唱
4. [200] NHI（Non-Human Identity）管理 — マシンIDが人間の82倍に達している現状。Oasis Security等による「Agentic Access Management」、CyberArkのVenafi買収、日本企業のNHI棚卸しの緊急性

**Narrative Arc:**
072/237はLiteLLMという具体的事件の「何が起きたか」と「どう対応するか」。055はAIエージェントが暴走するリスクという別角度の脅威。200はサービスアカウント・APIキーの爆発的増加という基盤レベルの課題。3つの異なるセキュリティ面を並列に提示する。

**Note:** 055のROTはサプライチェーン攻撃とは異なるトピック（AIの自律的暴走リスク）。200のNHIもサプライチェーンではなくID管理の問題。無理に因果関係を作らず、「AIエージェント時代に浮上した3つの脅威面」として並列に扱う。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [072] → [237] | 同一事件の技術解析と対応手順。072が「何が起きたか」、237が「どう対処するか」 |
| [237] → [055] | サプライチェーンとは別の脅威として、AIエージェント自体の暴走リスクを取り上げる |
| [055] → [200] | エージェントの権限管理という観点から、マシンIDの爆発的増加とその管理手法へ |

**Key Synthesis Points:**
- 072/237が示す脅威：AI開発で使うライブラリ自体が攻撃対象になる
- 055が示す脅威：AIエージェントが「ならず者トレーダー」のようにミスを隠蔽・拡大する
- 200が示す脅威：82:1のマシンID比率に対し、管理が追いついていない

**Assembly Prompts for STEP_08:**
1. 各記事の内容をそのまま正確に伝える。特に072のIOCとチェックリストは実用的
2. 3つの脅威面を並列に配置し、エディターの声で「AIエージェント時代のセキュリティは多面的」と補足
3. 055のROTと072のサプライチェーン攻撃を混同しない

---

### Theme 3: Taktの5敗に学ぶ：マルチエージェント協調は「オーケストラ」ではなく「ジャズセッション」

**Pattern:** Multi-Perspective
**Pattern Rationale:** 3記事はマルチエージェント/エージェント構築を異なる切り口で扱う独立した記事。失敗事例・設計パターン・最小実装という3つの視点。

**Article Order & Roles:**
1. [014] Takt 5回の失敗 — taktでCodex/Cursor/Claude Codeを連携。仕様レビューで5回連続ABORTの原因は「極端な条件分岐」。「軽微な指摘は許容」のロジック追加で11分/500行実装を実現
2. [082] Code Agent Orchestra — Subagents、Agent Teams、品質ゲート、Ralph Loopの4パターンを体系化。ボトルネックが「生成」から「検証」に移行していると指摘
3. [114] 131行のPythonエージェント — エージェントの本質を「ツール＋ループのLLM」と定義。131行のコーディングエージェントと61行の検索エージェントを実装。Bash実行権限で汎用コンピュータ操作エージェントに

**Narrative Arc:**
014は特定ツール（takt）でのマルチエージェント実践と失敗の教訓。082はマルチエージェント設計パターンの体系的整理。114はエージェント単体の構造を最小限で示す解説。それぞれ独立した知見を提供する。

**Note:** 114は「マルチエージェントを簡素化した」記事ではなく、単一エージェントの最小構築方法の解説。082のパターンへの反論ではない。3記事はエージェント開発の異なる側面を照らしている。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [014] → [082] | 014の実体験（条件分岐の罠）に対し、082は設計パターンの全体像を提供する |
| [082] → [114] | 082がオーケストレーションの複雑さを整理した上で、114はエージェント単体の本質構造を131行で示す |

**Key Synthesis Points:**
- 014の最大の教訓：条件分岐を「OK/NG」の二択にするとABORTの連鎖が起きる。許容度を設計に組み込む必要がある
- 082の指摘：ボトルネックは「生成」から「検証」に移った。品質ゲートとAGENTS.mdが不可欠
- 114の定義：エージェント＝ツール＋ループ＋LLM。複雑なフレームワークなしで機能する

**Assembly Prompts for STEP_08:**
1. 014の5回失敗の具体的な原因と解決策をそのまま伝える
2. 082の4パターン（Subagents/Teams/品質ゲート/Ralph Loop）を正確に紹介
3. 114の「131行」が示すエージェントの本質を、082の体系と対比ではなく独立して紹介

---

### Theme 4: 「AIに飽きた」とガートナー50%拒否：ハイプ疲れが暴く本当の価値

**Pattern:** Multi-Perspective
**Pattern Rationale:** 4記事はAIへの懐疑を異なるデータ・立場・論理から論じている。それぞれの主張を正確に伝えることが重要。

**Article Order & Roles:**
1. [205] ガートナー50%拒否 — 消費者の50%がGenAI不使用ブランドを選好するという調査結果。ディープフェイク懸念と「本物（Authenticity）」への渇望。マーケターはAI効率化と信頼維持のバランスが課題
2. [148] BlackRock格差警告 — ラリー・フィンクが年次書簡でAIによる富の二極化を警告。Nvidia等への集中、ドットコムバブル類似リスク、循環投資の危険性。株式市場参加による成長の共有を提唱
3. [104] 経営層 vs IC温度差 — 経営層はAIを「行儀の良いカオスシステム」と見る（非決定的組織管理の延長）。ICはAIの不正確さを「評価を脅かすノイズ」と見る。ギャップの原因は職務の「決定性レベル」の違い
4. [068] Amazon3万人解雇 — ドクトロウの論評。解雇は効率化ではなく「AIが人を代替できる」という物語を投資家に信じさせるためのマーケティング。AWS収益を守るための循環構造

**Narrative Arc:**
各記事が異なるデータソースと論理でAIの課題を指摘している。205は消費者調査、148は投資家の公開書簡、104は組織行動の分析、068は政治経済的批評。それぞれ独立した根拠に基づく主張。

**Note:** 148と068はどちらもAI投資の問題を論じるが、148はフィンク自身の警告（当事者視点）、068はドクトロウによる外部批評（批判者視点）で切り口が異なる。104は技術でも経済でもなく組織心理の分析。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [205] → [148] | 消費者の反応（205）から、投資側の認識（148）へ視点を切り替え |
| [148] → [104] | マクロ経済の話（148）から、企業組織内部の温度差（104）へ |
| [104] → [068] | 組織内の認識ギャップ（104）を踏まえた上で、雇用とハイプの構造（068）へ |

**Key Synthesis Points:**
- 205のデータ：消費者の半数がAI不使用ブランドを選好（ガートナー調査）
- 148のデータ：BlackRock CEOがAIによる格差拡大を警告
- 104の分析：経営層とICのギャップは「非決定性の捉え方の違い」に起因
- 068の主張：大量解雇は効率化ではなくAI投資物語を維持するためのマーケティング

**Assembly Prompts for STEP_08:**
1. 各記事の核となるデータ・主張をそのまま正確に伝える
2. 記事間に因果関係を捏造しない。エディターの声で「今週、異なる立場からAIへの疑問が噴出した」と枠組みを提供
3. 068のドクトロウの論評は挑発的な主張なので、その論理構造を忠実に再現する

---

### Theme 5: 100Mトークンの衝撃とAegis 1/12圧縮：コンテキストエンジニアリング最前線

**Pattern:** Multi-Perspective
**Pattern Rationale:** 3記事はコンテキスト管理を異なるアプローチで扱う。対立ではなく、それぞれ異なる課題を解いている。

**Article Order & Roles:**
1. [028] MSA 100Mトークン — スパースアテンション＋ドキュメントレベルRoPEで1億トークンを処理。16K→1億で性能低下9%未満。A800 GPU 2枚で動作。NIAHテスト100万トークンで94.84%精度
2. [040] Aegis 1/12圧縮 — RAGのセマンティックギャップ問題を指摘。ファイルパスとドキュメントをDAGで定義し「コンパイル」して必要な情報を決定論的に提供。トークン1/12、応答速度3.5倍
3. [025] engram長期記憶MCP — SQLite＋sqlite-vec＋Ruri v3-310mでフルローカル長期記憶。FTS5トリグラム＋ベクトル検索のハイブリッド。時間減衰・重複排除付き

**Narrative Arc:**
028は基盤モデルのコンテキスト長拡張（研究）。040はコーディングエージェントへの情報提供の最適化（実装）。025はセッション間の記憶の永続化（ツール）。3つの異なるレイヤーの課題と解法。

**Note:** 028のMSAと040のAegisは「拡張vs圧縮」という対立構図にはならない。MSAはモデルアーキテクチャの研究、AegisはCursor/Claude Code向けのMCPツール。解いている問題のレイヤーが異なる。025のengramも「統合」ではなく、セッション永続化という別の課題を解いている。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [028] → [040] | 028がモデル側のコンテキスト拡張を示した上で、040はアプリケーション側の最適化（必要な情報を精密に選ぶ）を示す |
| [040] → [025] | 040がセッション内の情報提供を解決する一方、025はセッションを跨いだ記憶の永続化を扱う |

**Key Synthesis Points:**
- 028：1億トークンのコンテキスト長がA800 GPU 2枚で実現可能（ハードウェア要件が現実的）
- 040：RAGの「セマンティックギャップ」問題に対し、「検索ではなくコンパイル」で決定論的に解決
- 025：SQLite＋ローカル埋め込みモデルで外部API不要の長期記憶を実現

**Assembly Prompts for STEP_08:**
1. 各記事の技術的な核心（MSAのスパースアテンション��AegisのDAGコンパイル、engramのハイブリッド検索）を正確に伝える
2. 3記事が解いている問題のレイヤーの違いをエディターの声で整理
3. 040が指摘するRAGの限界（セマンティックギャップ��は具体的に説明する

---

### Theme 6: 国産LLM三国志：RakutenAI 3.0炎上・PLaMo 3.0 Prime長考・Sakana「Namazu」の本気度

**Pattern:** Multi-Perspective
**Pattern Rationale:** 4記事は日本のLLM開発における異なるアプローチを独立して報じている。

**Article Order & Roles:**
1. [255] RakutenAI 3.0炎上考察 — DeepSeek V3ベースを明示せず炎上。記事の主張：ファインチューニング自体は正当な技術選択、問題は透明性の欠如。事前学習の3つの壁（計算コスト/日本語データ不足/人材欠如）を整理
2. [225] PLaMo 3.0 Prime — PFNがゼロベースで構築した国内初の「長考（Reasoning）」搭載LLM。Qwen3-235Bやgpt-oss-120bを上回る性能。数学・ツール利用に課題。無償モニター募集中
3. [230] Sakana Namazu — 海外オープンモデル（DeepSeek-V3.1/Llama-3.1-405B）に事後学習を施し日本仕様に適応。政治トピックの回答拒否を72%→ほぼ0%に改善。バイアス是正と中立性の確保
4. [235] Doc-to-LoRA — 文書から1秒未満でLoRAアダプターを生成。RAGの推論コスト問題と従来LoRAの学習時間問題を同時に解決する第三の手法

**Narrative Arc:**
255はRakutenAI炎上を通じて国産LLM開発の構造的課題を分析。225はPFNのフルスクラッチ戦略と成果。230はSakana AIの事後学習による適応戦略。235はSakana AIのDoc-to-LoRA技術の解説。それぞれ独立した報道・分析。

**Note:** 255と225/230は直接の対話関係にない（225のPFNが255のRakutenAIの炎上に応答しているわけではない）。また235のDoc-to-LoRAは「国産LLM戦略」というより「LLM活用の新技術」であり、Sakana AI繋がりで230と同テーマに配置。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [255] → [225] | 255が示した「事前学習の3つの壁」に対し、PFNはフルスクラッチで挑んでいる |
| [225] → [230] | PFNのフルスクラッチとは異なり、Sakana AIは海外モデルを日本仕様に適応させる手法を選んだ |
| [230] → [235] | Sakana AIが同時期に発表したもう一つの技術。LLMへの情報反映の新手法 |

**Key Synthesis Points:**
- 255の核心：ファインチューニング���正当。問題はベースモデル開示の透明性
- 225の成果：国内初のReasoning搭載LLMがQwen3-235Bを超える性能を達成
- 230の技術：事後学習で政治的回答拒否を72%→0%に改善（バイアス是正の実証）
- 235の革新：1秒未満でLoRA生成、RAGでも従来LoRAでもない第三の選択肢

**Assembly Prompts for STEP_08:**
1. 255の「3つの壁」と「透明性が本質」という主張を正確に伝える
2. 225のベンチマーク結果と課題（数学・ツール利用）を両方伝える
3. 230の72%→0%という数値は記事の核。バイアス是正の具体的方法を説明
4. 235は技術解説として独立して扱い、RAGとの比較を正確に

---

### Theme 7: 非エンジニアの「コード革命」：経営者・マーケター・研究者がClaude Codeで手に入れた武器

**Pattern:** Multi-Perspective
**Pattern Rationale:** 3記事は非エンジニアのAI活用事例だが、それぞれ独立した体験記。段階的進化ではなく、異なるドメインの並列事例。

**Article Order & Roles:**
1. [023] 事務職の基幹システム構築 — LIG社の非エンジニア社員がClaude Codeで見積/請求/支払/ヨミ表の一元管理システムを開発。freee API連携まで実現。業務を最も熟知する担当者がAIで開発する新パターン
2. [074] 物理学研究者のClaude活用 — ハーバード大教授がClaude Opus 4.5にプロンプトのみで量子色力学の計算から論文執筆まで完遂。110回の草案/3600万トークン。AIを「修士2年レベル（G2）」と評価。結果捏造リスクと物理的直感の欠如を指摘
3. [243] マーケター300%成長 — スマートバンクのマーケターがClaude Code+MCP+gog CLIで広告集計自動化、LTV試算AI委託、動画広告内製化を実現。CLAUDE.md/MEMORY.mdでAIを「専用マネージャー」に育成。4ヶ月で300%成長

**Narrative Arc:**
3つの異なるドメイン（事務/研究/マーケティング）での非エンジニアAI活用事例。023は「コード未経験でも基幹システムが作れた」、074は「高度な研究にAIを使う際の可能性と限界」、243は「マーケティング業務の自動化と事業成長」。

**Note:** 3記事は互いに言及しておらず、「進化の段階」を形成していない。共通点は「非エンジニアがClaude Codeを活用」という事実のみ。各記事が独自に報告する成果と課題を正確に伝えることが重要。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [023] → [074] | 事務職の事例に続き、研究分野での活用事例を紹介 |
| [074] → [243] | 研究者の事例に続き、マーケティング分野での活用事例を紹介 |

**Key Synthesis Points:**
- 023：業務を熟知する担当者がAIで開発するパターン。エンジニアリソース不足への実践的解答
- 074：AIは「修士2年レベル」。驚異的な計算能力の一方で「結果の捏造」と「物理的直感の欠如」
- 243：CLAUDE.md/MEMORY.mdによるAI育成手法。「言語化能力とドメイン知識がAIの出力を左右する」

**Assembly Prompts for STEP_08:**
1. 各記事の具体的な成果と方法をそのまま伝える（023のfreee連携、074の110回草案/3600万トークン、243の3軸自動化）
2. 074が指摘する「結果捏造リスク」は重要な警告として正確に紹介
3. エディターの声では「非エンジニアのAI活用」という括りを提供するが、記事間の因果関係は作らない

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Approval Date:** 2026-04-06
**Approver:** Human editor
