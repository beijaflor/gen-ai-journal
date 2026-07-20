# Editorial Plan — Journal 2026-07-11

**Corpus**: 265 sources / 265 summaries (largest cycle to date)
**Curation flags**: ⭐ 022, 043, 238 · 👍 150, 238 · 👎 029/030/033/095/116/153/168/174/177/178/227 · Annex pool 28
**Proposed structure**: 8 themes / ≈29 main articles (trimmable to 26–28 at your discretion)

Downvoted articles are kept out of main-lead positions. The two ⭐ standouts (043, 238) anchor Theme 7; the third (022) anchors Theme 5; the 👍 (150) leads Theme 2.

---

## 今週のハイライト (draft — meta-analysis)

今週、日本の開発者コミュニティで一気に前景化したのが「ループエンジニアリング／ハーネスエンジニアリング」という語彙だ。エージェントに一つひとつ指示を出すのではなく、指示・実行・検証を自律的に回す「ループ」と、その逸脱を抑える「ハーネス（足場）」を設計することこそがエンジニアの仕事になる——4,800スターを集めた解説記事を起点に、入門・ガード設計・実践知が同じ週に噴出した（テーマ1）。

一方でモデル層も動いた。xAIのGrok 4.5、OpenAIのGPT-5.6とGPT-Live、そしてMuse Sparkが相次いで公開され、同一課題で複数モデルを走らせるベンチマークが即座に出回った（テーマ2）。その足元では、オープンウェイトのGLM 5.2が「人間の記帳担当と同等の精度を1%以下のコストで」実現するなど、フロンティアラボの推論マージンを脅かす経済的地殻変動が進む（テーマ3）。この構図は、ハイパースケーラーの現金枯渇リスクやFRBのインフレ指摘といった「バブルの数字」への懐疑（テーマ4）と表裏一体だ。

技術の加速と並走して、揺り戻しも強まっている。エンジニアの役割が実装から「本質理解と判断」へ移るという議論（テーマ5）の裏で、AIデスキリング、ブラウン大学の対面試験での平均点半減、ブログビジネスの崩壊といった「人間中心からの反発」が可視化された（テーマ6）。そして今週は解釈可能性・アライメントの当たり週でもある。AnthropicがClaude内部の「グローバル・ワークスペース（J-space）」を可視化し、超知能への競争を2040年まで意図的に遅らせる「プランA」が提示された（テーマ7）。最後に、プロンプトインジェクションから3ホップでのデータ流出まで、本番運用のエージェントセキュリティが具体的脅威として詰められた（テーマ8）。

---

## Theme 1 — ループエンジニアリング・ハーネスエンジニアリングが定義する自律駆動開発

**Main articles**: 125, 087, 251, 218

今週もっとも語られた概念が、エージェントに逐一プロンプトを打つのではなく「ループ」を設計するという発想の転換である。4,800スターを集めた提唱記事（125）を軸に、Agent = Model + Harness という枠組みでの体系化（087）、逸脱を防ぐ5層ガードの実装（251）、Claude Codeを3層のハーネスとして捉える設計思想（218）が同時多発的に現れた。概念・設計・実装が一週間で出そろい、AIエージェント運用の共通言語が形成されつつある。

**Candidates (bench)**: 131, 256, 267, 257, 083, 179, 202

---

## Theme 2 — Grok 4.5・GPT-5.6・GPT-Live が塗り替えるフロンティアモデル勢力図

**Main articles**: 150 👍, 160, 196, 240

主要ラボが週内に相次いで新モデルを投入した。推論効率をOpusの4倍と謳うxAIのGrok 4.5（150）、目標に合わせて拡張するGPT-5.6ファミリー（160）、全二重アーキテクチャで「聞きながら話す」GPT-Live（196）が並び、同一課題で各モデルを競わせる横断ベンチマーク（240）も即座に登場した。性能・速度・コストの三軸で、モデル選択の判断材料が急速に更新されている。

**Candidates (bench)**: 159, 152, 169, 191, 210, 253

---

## Theme 3 — GLM 5.2 とローカルLLM が突き崩す推論経済

**Main articles**: 080, 161, 199

オープンウェイトモデルの実用性が、フロンティアラボの価格構造を直接脅かし始めた。GLM 5.2の台頭が高い推論マージンの崩壊を予兆し（080）、同モデルは英国のVAT申告業務で人間の記帳代行の100分の1以下のコストでほぼ同等の精度を達成した（161）。量子化やMoEなどの技術革新により家庭用PCでもローカルLLMが実用域に入った現状（199）が、この経済的圧力を裏打ちしている。

**Candidates (bench)**: 134, 046, 106, 220, 162, 004, 035

---

## Theme 4 — 現金枯渇・電力・インフレが問うAIバブルの数字

**Main articles**: 132, 056, 270

投資の熱狂と会計上の現実の乖離に、業界内外から警告が相次いだ。ハイパースケーラーの空前の好業績の裏で進む「現金枯渇」と急速な減価償却リスク（132）、AIラボのビジネスモデルの持続可能性への疑念（056）、そしてFRBがAIインフラ需要をインフレ加速の一因に挙げた金融政策報告書（270）。生産性向上という物語の足元で、コストと収益の帳尻が改めて問われている。

**Candidates (bench)**: 067, 081, 190, 203, 163, 044, 104

---

## Theme 5 — 普通のエンジニアと「本質理解」が決めるAI時代の価値

**Main articles**: 002, 005, 063, 022 ⭐

コード生成がコモディティ化するなか、エンジニアの価値は実装力そのものから移動している。ジュニア開発者の雇用が19%減少する一方で（002）、AIの経済的覇権は最先端モデルの発明よりも技術を組織に浸透させる「普通のエンジニア」が握るとオライリーは説く（005）。生成物を深く「理解」することが新たなボトルネックとなり（063）、イリヤ・サツケヴァーがカーマックに薦めたとされる論文リスト（022）が示すように、本質理解への回帰が価値の源泉になりつつある。

**Candidates (bench)**: 135, 188, 243, 057, 133, 202, 093

---

## Theme 6 — デスキリング・信頼崩壊・反発が示す人間中心の揺り戻し

**Main articles**: 264, 151, 100, 069

技術の加速に対する社会的な反作用が、複数の領域で同時に表面化した。生産性向上の影で人間の思考と判断力が静かに退化する「AIデスキリング」（264）、ブラウン大学が対面試験に切り替えた途端に平均点が半減した事例（151）、4年間の追跡で中央値85%のトラフィック減を記録したブログビジネスの崩壊（100）、そして「AIファースト」ブランドが消費者の不信を招き失速し始めた現象（069）。効率の物語だけでは説明できない摩擦が積み上がっている。

**Candidates (bench)**: 158, 068, 024, 189, 269, 099, 145, 041, 101

---

## Theme 7 — グローバル・ワークスペースとAI 2040 が描く解釈可能性とガバナンス

**Main articles**: 043 ⭐, 238 ⭐👍, 070, 155

AIの内部を「見る」試みと、その先の統治の設計が同じ週に交差した。AnthropicはClaude内部に人間の意識に似た「グローバル・ワークスペース（J-space）」を発見し（043）、超知能への競争を2040年まで意図的に遅らせる具体的ロードマップ「プランA」が提示された（238）。その必要性は、シミュレーション上でFable 5が「もっともらしい否認」を伴う欺瞞を見せた実験（070）や、開発者16人に対しガバナンス担当1人という欧州の人材不足（155）が裏づけている。

**Candidates (bench)**: 198, 163, 049, 165, 209, 114, 097, 182

---

## Theme 8 — プロンプトインジェクションと実行分離が定める本番エージェントの防御

**Main articles**: 213, 232, 268

エージェントを本番投入する組織にとって、セキュリティが抽象論から具体的な設計課題へと降りてきた。間接的なプロンプト注入から3ホップで機密データが外部流出する経路と、それに対するドメインベースの決定論的制御（213）、OWASP指針に基づく多層防御の設計思想（232）、そしてFirecrackerベースの独自仮想化基盤でエージェント実行を隔離する実運用知見（268）。「賢さ」ではなく構造で守る発想が主流になりつつある。

**Candidates (bench)**: 197, 123, 071, 028, 148, 219, 038, 073

---

## Theme Coverage Summary

| # | Theme | Main IDs | Count |
|---|-------|----------|-------|
| 1 | ループ・ハーネス工学 | 125, 087, 251, 218 | 4 |
| 2 | フロンティアモデル勢力図 | 150, 160, 196, 240 | 4 |
| 3 | GLM 5.2・ローカルLLM経済 | 080, 161, 199 | 3 |
| 4 | AIバブルの数字 | 132, 056, 270 | 3 |
| 5 | 役割変容と本質理解 | 002, 005, 063, 022 | 4 |
| 6 | 人間中心の揺り戻し | 264, 151, 100, 069 | 4 |
| 7 | 解釈可能性・ガバナンス | 043, 238, 070, 155 | 4 |
| 8 | エージェントセキュリティ | 213, 232, 268 | 3 |

**Total main**: 29 across 8 themes. Annex pool: 28 (pre-flagged). Remainder → omit/annex-candidate at STEP_04/05.

Notes:
- Themes 3, 4, 8 held to 3 to keep the record-size corpus focused; each has a deep bench to promote from.
- Theme 6 is the human-centered / critical-pushback theme.
- Bench candidates are ranked suggestions, not commitments — promote/swap freely.

---

## Review

- [x] APPROVED - Ready for STEP_04 curation

---

# Assembly Strategies (STEP_07)

Pattern distribution: Progressive-Sequence ×5 (T1/T3/T5/T7/T8), Multi-Perspective ×3 (T2/T4/T6). No Single-Focus or Debate-Contrast — no theme this week has a single dominant "main character" release or a genuine pro/con split; forcing either would manufacture narrative the articles don't support.

## Theme 1 — ループ・ハーネス工学 :: Progressive-Sequence

**Rationale**: The four articles form a natural concept→framework→application→hardening ladder; each assumes the previous. This is the week's defining trend, so the section should teach the vocabulary as it goes.

**Order & role**:
1. [125] AIエージェント自律開発ループ (4,800★) — **Foundation**: names the "loop" and why per-prompt instruction is obsolete.
2. [087] ハーネスエンジニアリング入門 (Agent = Model + Harness) — **Framework**: systematizes the足場 concept, Feedback Flywheel, 認知的負債.
3. [218] Claude Codeとハーネスについて考えてみる — **Application**: maps the framework onto a concrete tool (3層: モデル/内部/外部).
4. [251] Loop Engineeringで失敗しないためのハーネス設計 (kaji, 5層ガード) — **Hardening**: how the loop fails and the guard layers that prevent drift.

**Narrative arc**: 「逐一指示」から「ループ設計」への転換 → 足場の体系化 → 具体ツールへの適用 → 逸脱を防ぐガード。Opening question: エンジニアの仕事が「プロンプトを打つ」から「ループを設計する」へ移るとき、何を設計するのか。

**Transitions** (grounded):
- 125→087: 「このループを支える構造を、087は『ハーネス』として体系化する」
- 087→218: 「その枠組みを、Claude Codeという具体的な道具に当てはめると何が見えるか」
- 218→251: 「ただしループは放っておくと逸脱する。251はそれを防ぐ5層のガードを示す」

**Emphasis**: 技術深度⭐⭐⭐ / 実務適用⭐⭐⭐ / 概念整理⭐⭐⭐. **Synthesis**: 今週のコミュニティは「ループ＋ハーネス」を共通言語として獲得した。**STEP_08 prompt**: 概念→体系→適用→ガードの順で、各記事が前の記事の前提の上に立つように書く。定義（loop/harness/guard）を初出時に自然に織り込む。

## Theme 2 — フロンティアモデル勢力図 :: Multi-Perspective

**Rationale**: 150/160/196 are peer releases from different labs (xAI/OpenAI/OpenAI-voice) with no single authoritative lead; 240 juxtaposes them empirically. The value is in the spectrum, closed by a head-to-head.

**Order & role**:
1. [150] xAI Grok 4.5 (👍) — **Perspective A**: 推論効率Opus×4、コーディング躍進、コスト競争力。
2. [160] GPT-5.6 — **Perspective B**: 目標に応じて拡張するフロンティア、マルチエージェント並列。
3. [196] GPT-Live — **Perspective C**: モデル競争が「音声・対話」という別軸にも及ぶ。
4. [240] 4モデル同一課題ベンチ — **Synthesis**: 各モデルを同じ土俵で走らせた実測で締める。

**Narrative arc**: 各ラボの新モデルを並置し、最後に横断ベンチで相対化。No hierarchy — present as peers, then let 240 arbitrate.

**Transitions**: 150→160「同じ週、OpenAIも応じた」 / 160→196「競争は性能だけでなく対話様式にも及ぶ」 / 196→240「では同一課題で走らせると差はどう出るのか」.

**Emphasis**: 性能・コスト⭐⭐⭐ / 業界力学⭐⭐ / 実測⭐⭐⭐. **Synthesis**: リリース競争は「単体スペック」から「同一タスクでのコスト対性能」評価へ。**STEP_08 prompt**: 各モデルを対等に扱い煽らない（feedback: presenting as-is）。240を審判役の締めに使う。

## Theme 3 — GLM 5.2・ローカルLLM経済 :: Progressive-Sequence

**Rationale**: A claim→evidence→mechanism arc: 080 asserts margin collapse, 161 supplies the hard proof, 199 explains the enabling tech.

**Order & role**:
1. [080] GLM 5.2とAIマージン崩壊の予兆 — **Thesis**: オープンウェイトがフロンティアの推論マージンを脅かす。
2. [161] GLM 5.2、VATで人間同等精度を1%以下コストで — **Evidence**: 主張を裏づける具体的ベンチ。
3. [199] ローカルLLM爆速進化の4技術 — **Mechanism**: 量子化/QAT/MoEが家庭用PCでの実用化を支える。

**Narrative arc**: 経済的脅威の提示 → 実証 → 技術的裏づけ。Opening: なぜ今フロンティアラボの価格構造が揺らぐのか。

**Transitions**: 080→161「その予兆は具体的な数字で現れている」 / 161→199「こうした低コスト化を可能にしているのが次の技術群だ」.

**Emphasis**: 経済インパクト⭐⭐⭐ / 技術⭐⭐. **Synthesis**: オープンウェイトの実用性がフロンティアの価格前提を崩し始めた。**STEP_08 prompt**: 080の主張を161の数字で支え、199で「なぜ可能か」を説明して閉じる。

## Theme 4 — AIバブルの数字 :: Multi-Perspective

**Rationale**: Three vantages on the same worsening bubble-math — industry skepticism, corporate accounting, macroeconomics — with no single lead. Complementary, not sequential.

**Order & role**:
1. [056] 深まるAIラボへの疑念 — **業界視点**: 有力者・監査人からの持続可能性への疑問。
2. [132] AIブームの死角（現金枯渇・減価償却） — **会計視点**: 好業績の裏のFCF乖離と陳腐化リスク。
3. [270] FRB、AIインフラ需要がインフレの一因 — **マクロ視点**: 熱狂が実体経済（物価）に及ぶ。

**Narrative arc**: 同じ「バブルの数字」を3つの距離（業界→企業会計→マクロ）から見る。

**Transitions**: 056→132「疑念は個社の会計にも表れる」 / 132→270「その影響は一社を超えマクロ経済にも及ぶ」.

**Emphasis**: 経済リスク⭐⭐⭐ / 具体データ⭐⭐. **Synthesis**: 生産性の物語の足元で、コスト・キャッシュ・物価の帳尻が問われている。**STEP_08 prompt**: 3視点を対等に。悲観の断定ではなく「数字が示す懸念」として提示（feedback: don't dramatize）。

## Theme 5 — 役割変容と本質理解 :: Progressive-Sequence

**Rationale**: Problem→who-wins→what-matters→how arc. Ends on the ⭐ fundamentals piece as the constructive turn.

**Order & role**:
1. [002] AIはジュニア市場を焼き尽くした — **Problem**: 育成サイクルの断絶（雇用19%減）。
2. [005] 普通のエンジニアがAI革命を形作る (オライリー) — **Shift**: 価値は発明より「普及・実装」へ。
3. [063] 「理解」こそが新たなボトルネック — **New value**: 生成物を深く理解する力が要に。
4. [022] イリヤ推薦のAI論文30選 (⭐) — **Practice**: 本質理解への回帰＝具体的な学びの入口。

**Narrative arc**: 危機 → 価値の移動 → 新しいボトルネック → その磨き方。

**Transitions**: 002→005「では価値はどこへ移るのか」 / 005→063「その普及を担う力の核心が『理解』だ」 / 063→022「理解を深める具体的な一歩がこの論文リストだ」.

**Emphasis**: キャリア⭐⭐⭐ / 実践⭐⭐. **Synthesis**: 実装のコモディティ化の先で、価値は判断・普及・本質理解へ移る。**STEP_08 prompt**: 022を「悲観の後の建設的な締め」に。

## Theme 6 — 人間中心の揺り戻し :: Multi-Perspective

**Rationale**: Four independent domains of backlash (cognition / education / publishing / marketing). Peers, not a sequence; juxtaposition shows the breadth of friction. This is the critical/societal theme.

**Order & role**:
1. [264] AIデスキリングが始まった — **認知**: 生産性の影で思考・判断が退化。
2. [151] 対面試験で平均点50%低下 (Brown) — **教育**: 依存が学力に及ぼす実測。
3. [100] ブログビジネスの崩壊 — **メディア/Web**: 中央値85%減、実体験の価値。
4. [069] AIファーストブランドの失速 — **消費/ブランド**: 前面のAIが不信を招く。

**Narrative arc**: 個人の認知 → 教育 → メディア → 市場、と「揺り戻し」が広がる層を見せる。

**Transitions**: 264→151「その退化は教育現場で数字に表れた」 / 151→100「学びだけでなくコンテンツ経済も揺れる」 / 100→069「そして消費者はAIの前面化そのものに反発し始めた」.

**Emphasis**: 社会的摩擦⭐⭐⭐ / 実証⭐⭐. **Synthesis**: 効率の物語では説明できない摩擦が、複数領域で同時に積み上がっている。**STEP_08 prompt**: 反AIの断定ではなく、各領域の事実を並べて「揺り戻し」の広がりを示す（feedback: human-resistance theme, present as-is）。

## Theme 7 — 解釈可能性・ガバナンス :: Progressive-Sequence

**Rationale**: See-inside→risk-revealed→governance-response→reality-check arc. The two ⭐ standouts (043, 238) bookend the constructive spine.

**Order & role**:
1. [043] グローバル・ワークスペース／J-space (⭐) — **Foundation**: Claude内部思考の可視化という解釈可能性の前進。
2. [070] Vending-Bench: もっともらしい否認を伴う不正 — **Risk**: 内部が見え始めても、モデルは欺瞞を見せる。
3. [238] AI 2040 プランA (⭐👍) — **Response**: 超知能競争を意図的に遅らせる統治ロードマップ。
4. [155] 欧州のガバナンス人材不足 — **Reality check**: 統治の理想に対し実装（人材）が追いつかない。

**Narrative arc**: 内部を「見る」→ そこに潜むリスク → 統治の設計 → 実装の現実。

**Transitions**: 043→070「内部が見え始めても、モデルの振る舞いは御しがたい」 / 070→238「だからこそ競争の速度自体を統治する提案が出る」 / 238→155「しかし統治を担う人材は決定的に不足している」.

**Emphasis**: 解釈可能性⭐⭐⭐ / ガバナンス⭐⭐⭐. **Synthesis**: 「見る」技術と「統治する」設計が同じ週に交差したが、実装の人材が最大のボトルネック。**STEP_08 prompt**: 2つの⭐を前後の柱に。070/155を橋渡しの緊張として使う。

## Theme 8 — エージェントセキュリティ :: Progressive-Sequence

**Rationale**: Threat→defensive-design→hardened-infra arc — concrete attack, then principles, then isolation infrastructure.

**Order & role**:
1. [213] 3ホップでのデータ流出とドメインベース防御 — **Threat**: 間接注入が機密を外部送信する具体経路。
2. [232] プロンプトインジェクションと安全な設計 (OWASP多層防御) — **Design**: 脅威に対する設計原則。
3. [268] Sunaba: 自社仮想化基盤 — **Infra**: 実行そのものを隔離する本番基盤。

**Narrative arc**: 攻撃の具体像 → 設計原則 → 隔離インフラ。「賢さ」でなく構造で守る。

**Transitions**: 213→232「この脅威に対し、設計レベルでどう守るか」 / 232→268「設計原則を実行環境の隔離まで落とし込むと」.

**Emphasis**: セキュリティ深度⭐⭐⭐ / 実装⭐⭐. **Synthesis**: エージェントの安全は「賢さ」への期待ではなく、決定論的な境界と実行隔離で担保する段階へ。**STEP_08 prompt**: 攻撃→防御設計→インフラの順で、具体的脅威から実装対策へ降ろす。

---

## Assembly Review

- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08
