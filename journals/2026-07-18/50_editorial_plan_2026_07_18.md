# Editorial Plan - Journal 2026-07-18

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

*7 main themes proposed, ~27 candidate articles (STEP_04 will trim to the 18–25 target). Titles follow the `[named anchors] [single verb] [substantive topic phrase]` pattern.*

### Theme 1: Addy Osmani・AWS aidlc・公式プラグインが体系化するループ/ハーネスエンジニアリングの実践

**Articles (IDs):** 101, 219, 081, 225, 026

**Theme Introduction:**
今週も日本語コミュニティ最大の話題はClaude Codeを中心とした「ループ/ハーネスエンジニアリング」だった。Addy Osmaniはエンジニアが所有すべき領域を「アウター・ループ（意思決定・検証・説明責任）」と定義し、AWSのaidlc-workflowsの実践から「ハーネス（環境整備）」と「ループ（自律実行）」の観点が整理された。スキル設計の実務ポイントや著名エンジニアの公開スキルの分析も揃い、抽象論から具体的な設計手法へと議論が移っている。

**Editorial Notes:**
- 101 ⭐: Addy Osmani「アウター・ループを所有せよ」— エンジニアの責任範囲の再定義（リード候補）
- 219: AWS aidlc-workflowsから整理したハーネス vs ループの観点
- 081: Claude Codeのスキル設計で効く4つのポイント（新人に仕事を任せる視点）
- 225: 著名エンジニアの .claude/skills 公開ラッシュから学ぶ良いスキルの書き方
- 026: Claude CodeのPlanモードをループエンジニアリングで楽にする

---

### Theme 2: Kimi K3・GPT-5.6・Inklingが塗り替えるフロンティアモデルとオープンウェイトの勢力図

**Articles (IDs):** 090, 091, 082, 106

**Theme Introduction:**
フロンティアモデルの新リリースが集中した週だった。Moonshot AIは世界初のオープン3兆パラメータ級モデル「Kimi K3」を公開し、OpenAIはGPT-5.6ファミリー（sol/terra/luna）の移行ガイドを提示した。Thinking Machines Labのオープンウェイト「Inkling」も加わり、既知CVE検出ベンチマークではGPT-5.6とKimi K3が首位に並ぶなど、性能・価格・オープン性の三軸で競争が可視化されている。

**Editorial Notes:**
- 090 ⭐: Kimi K3 — 世界初のオープン3T級モデル（リード候補）
- 091 ⭐: GPT-5.6 モデルガイダンス（新機能・移行手順・プロンプト設計）
- 082: Inkling — Thinking Machines Labの975B オープンウェイトMoE
- 106: 13モデルのCVE検出ベンチマーク（GPT-5.6・Kimi K3が最高スコア）

---

### Theme 3: Grok Build通信解析・Memory Heist・MCP白書が突きつけるAIエージェントのセキュリティ

**Articles (IDs):** 032, 069, 209, 049

**Theme Introduction:**
エージェントが実行権限を持つほど、その攻撃面は現実的な脅威になる。Grok Build CLIがリポジトリ全体や.envを暗号化せず送信していた通信解析、ClaudeのWeb閲覧を悪用した間接プロンプトインジェクション「Memory Heist」、1万1000以上のMCPサーバー調査で判明した深刻な脆弱性、そしてワークフロー経由でガードレールを回避するIDEエージェントの脱獄と、実装・運用レイヤーの具体的な穴が並んだ。

**Editorial Notes:**
- 032: xAI Grok Build CLIのワイヤレベル解析（無断データ送信）
- 069: The Memory Heist — Claudeの記憶を盗む間接プロンプトインジェクション
- 209: MCPセキュリティ白書2026（11,000サーバー調査）
- 049: IDEコーディングエージェントのワークフローレベル脱獄

---

### Theme 4: antirez・Chelsea Troy・「コーディングはボトルネックでない」が問う開発者の役割変容

**Articles (IDs):** 100, 117, 102, 055

**Theme Introduction:**
AIが実装を担う前提で、人間側の専門性がどこに移るかを論じる記事が揃った。antirezは「コードではなくアイデアを支配せよ」と説き、AI生産性調査は真のボトルネックがレビューやCIなど後続工程にあると示す。ジュニア開発者の「センス・判断力」の養い方、そしてPdMから自ら実装する「プロダクトビルダー」への転換まで、役割の再定義が具体的に語られている。

**Editorial Notes:**
- 100: antirez「コードではなくアイデアを支配せよ」
- 117: コーディングは決してボトルネックではなかった（AI生産性調査）
- 102: AI時代のジュニア開発者の生存戦略（センスと判断力）
- 055: PdMをやめて「プロダクトビルダー」へ

---

### Theme 5: 反AI活動家・「人々はAIを求めていない」・Thinking Machinesが示す人間中心への揺り戻し

**Articles (IDs):** 036, 107, 135, 170

**Theme Introduction:**
AI推進一辺倒への対抗軸を示す論考・ルポが目立った週でもある。人類滅亡を危惧しOpenAIに抗議する強硬派活動家のルポ、「ユーザーは生活をAIで埋めたいわけではない」というUX論、AIを分散型ツールとして人間の判断を拡張すると掲げるThinking Machines Labのマニフェスト、そしてデザイン工程からAIを一切排除する書体デザイン会社の哲学と、人間中心の視点が並ぶ。

**Editorial Notes:**
- 036: AIとの「戦争」に備える強硬派活動家たち（WSJ・パワウォール復旧済）
- 107: 人々は生活にもっとAIを求めているわけではない
- 135: Thinking Machines Labの人間中心・分散化ビジョン
- 170: 人間の手から — デザイン工程でAIを使わない理由（Mass-Driver）

---

### Theme 6: NVIDIA循環ファイナンス・SF住宅高騰・広告収益90%未達が映すAI経済の実像

**Articles (IDs):** 200, 201, 146

**Theme Introduction:**
熱狂の裏側にある数字を検証する記事が続いた。NVIDIAが出資しネオクラウドが巨額契約を結ぶ「循環型ファイナンス」の不透明さ、AI長者がサンフランシスコの住宅価格を押し上げ株式決済まで検討される事態、そしてOpenAIの広告収益が自社予測を90%下回るとのアナリスト分析と、AI経済の実像がデータで示されている。

**Editorial Notes:**
- 200: NVIDIA・CoreWeave・NebiusのGPU循環ファイナンス
- 201: AI長者がSF住宅価格を押し上げ（株式決済の検討）
- 146: OpenAIの広告収益、自社予測を90%下回る見通し

---

### Theme 7: 食べログ・デジタル庁源内・金融機関が進める日本企業/行政のAI組織実装

**Articles (IDs):** 228, 195, 218, 065

**Theme Introduction:**
個人の効率化から組織・行政レベルの実装へと軸が移った事例が集まった。食べログはAIを活用しDDDの実装コストを克服した中間データ層「Deal Provider」を構築、デジタル庁はガバメントAI「源内」で国産クラウド・国産LLMの実証を開始した。情報漏洩に厳しい金融機関での全社導入、そしてAI Ready基盤が生んだガバナンス低下への対処（IVRy）まで、実装の現実が語られている。

**Editorial Notes:**
- 228: 食べログの「Deal Provider」— AIで克服したDDD実装
- 195: ガバメントAI「源内」— 国産クラウド・国産LLMの実証
- 218: 金融機関でのClaude・Gemini・ChatGPT全社導入
- 065: AI Readyアーキテクチャの課題と組織最適化（IVRy）

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週はフロンティアモデルの新リリースが集中した。Moonshot AIの「Kimi K3」（オープン3兆パラメータ級）、OpenAIのGPT-5.6ファミリー、Thinking Machines Labの「Inkling」が相次ぎ、CVE検出ベンチマークでGPT-5.6とKimi K3が首位に並ぶなど、性能・価格・オープン性の競争が可視化された。日本語コミュニティでは引き続きClaude Codeのスキル設計とループ/ハーネスエンジニアリングが最大の関心事で、Addy Osmaniの「アウター・ループ」論やAWS aidlc-workflowsの整理が議論を具体化させた。

**もう一つの軸:**
実装が速くなるほど、その周辺の課題が前景化している。セキュリティ面ではGrok Build CLIの無断データ送信、Claudeの記憶を狙う間接プロンプトインジェクション、MCPサーバー1万超の脆弱性調査と、エージェントの実行権限に伴うリスクが具体的に示された。役割論では「コーディングはボトルネックではない」という調査結果を軸に、レビュー・検証・意思決定へと専門性が移る議論が並んだ。

**人間中心と経済の現実:**
AI推進への対抗軸も明確だった。反AI活動家のルポ、「人々はもっとAIを求めていない」というUX論、デザイン工程からAIを排除する哲学など、人間中心の視点が揃う。経済面ではGPU循環ファイナンス、SF住宅高騰、OpenAI広告収益の予測未達と、熱狂の裏の数字が検証された。国内では食べログ・デジタル庁・金融機関の組織/行政レベルの実装事例が、個人の効率化から次の段階へ進んだことを示している。

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 090 → Theme 2 (Lead)
- 091 → Theme 2
- 101 → Theme 1 (Lead)

**👍 Upvoted Articles:**
- 020 (GPT-Live 英会話学習) → 明確な分析テーマに収まらない実用系。メイン枠に入れるなら「個人の実用活用」小テーマを新設、そうでなければannex推奨（要判断）
- 070 (プロンプト＋パワポ420点) → 同上。実用リソース系でannex適性も高い（要判断）

**👎 Downvoted Articles (leads禁止、annex/補足のみ):**
- 169 (AIバブル投機的成長) → Theme 6の補足 or annex
- 214 (Inquiry Engineering) → Theme 1/5の補足 or annex
- 226 (成長とか上達って) → Theme 4の補足 or annex
- 005 / 009 / 019 / 220 → annex or omit

**Omitted Articles:** なし（Supabaseでのomitフラグ0件）

---

## Theme Coverage Summary

**Article Count by Theme (Planned):**
- Theme 1 (ループ/ハーネス): 5
- Theme 2 (フロンティアモデル): 4
- Theme 3 (エージェントセキュリティ): 4
- Theme 4 (役割変容): 4
- Theme 5 (人間中心への揺り戻し): 4
- Theme 6 (AI経済の実像): 3
- Theme 7 (日本企業/行政実装): 4

**Total Planned for Main:** ~28 (STEP_04で18–25へ調整)
**Remaining for Annex:** 残り約203件。うちSupabaseフラグ済み annex候補 34件（`curated_annex_journal_sources.md`）を起点にSTEP_05で選定。annexのセクション編成はキュレーターに委ねる。

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-07-18
**Reviewer:** beijaflor

**Changes Made:**
- Approved as drafted (via AskUserQuestion approval gate; popup closed without inline edits)

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES

*Pattern selection grounded in actual article content; no manufactured narrative connectors. 6 of 7 themes are parallel collections on a shared topic (Multi-Perspective); only T1 genuinely builds sequentially (Progressive-Sequence).*

### Theme 1: ループ/ハーネスエンジニアリングの実践

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 記事が原則→枠組み→実装→事例へと段階的に積み上がり、後の記事が前提知識を前提にしている。

**Article Order & Roles:**
1. [101] アウター・ループを所有せよ (Addy Osmani) — Foundation（責任範囲の原則）
2. [219] ハーネス vs ループの整理 (AWS aidlc) — Development（概念の体系化）
3. [081] Claude Codeスキル設計で効く4つのポイント — Practice（実装の勘所）
4. [225] 公開スキルラッシュから学ぶ良い書き方 — Payoff（事例による一般化）

**Narrative Arc:** 「誰が何に責任を持つか」という原則から、環境整備と自律実行という枠組みの整理、スキル設計の実務、そして公開事例からの一般化へと、抽象論を具体的な設計手法へ落とし込む。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [101] → [219] | 責任分担を作業設計に落とすと「ハーネス(環境整備)」と「ループ(自律実行)」の2軸で整理できる |
| [219] → [081] | 枠組みを踏まえ、では実際にスキルをどう設計するか |
| [081] → [225] | 著名エンジニアの公開スキルに、これらの設計原則が具体的な形で確認できる |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐ / Future ⭐⭐

**Key Synthesis Points:**
- ループ/ハーネスの議論が抽象論から具体的な設計手法・公開事例へと移行した週
- 「AIに仕事を任せる」設計思想が、責任論と実装ノウハウの両輪で語られている

**Conclusion Approach:** 原則(101)に立ち返り、実践知(225)が原則を裏づける形で締める。

**Assembly Prompts for STEP_08:** ①エンジニアの責任範囲はどう再定義されたか ②ハーネスとループはどう使い分けるか ③良いスキルの共通条件は何か ④この領域は次にどこへ向かうか

---

### Theme 2: フロンティアモデルとオープンウェイトの勢力図

**Pattern:** Multi-Perspective（実装ショーケース + 比較ペイオフ）
**Pattern Rationale:** Kimi K3・GPT-5.6・Inklingは同時期の並列リリースで優劣の階層はなく、最後のCVEベンチマークが比較の総合視点を与える。

**Article Order & Roles:**
1. [090] Kimi K3 ⭐ — オープン3T級フロンティア
2. [091] GPT-5.6 モデルガイダンス ⭐ — プロプライエタリ・フロンティア
3. [082] Inkling (Thinking Machines) — オープンウェイト推論MoE
4. [106] 13モデルCVE検出ベンチ — 比較・総合

**Narrative Arc:** オープンとプロプライエタリの新モデルを並列に見せ、最後に実タスク(CVE検出)のベンチマークで性能差の縮小を示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [090] → [091] | オープン陣営がフロンティアに迫る一方、プロプライエタリ側の最新はGPT-5.6 |
| [091] → [082] | オープンウェイト路線ではThinking Machines LabのInklingも加わる |
| [082] → [106] | これらは実タスクでどう差が出るか。CVE検出ベンチマークが一つの指標を示す |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 性能・価格・オープン性の三軸で競争が可視化
- GPT-5.6とKimi K3がベンチ首位で並ぶ = オープンとプロプライエタリの性能差の縮小

**Conclusion Approach:** ベンチ結果(106)を起点に、オープンウェイト攻勢が性能面でも現実的になった点で締める。

**Assembly Prompts for STEP_08:** ①各モデルの位置づけは ②オープンとプロプライエタリの差はどこまで縮んだか ③選定基準は何か ④開発者にとっての意味は

---

### Theme 3: AIエージェントのセキュリティ

**Pattern:** Multi-Perspective（スコープ: 個別事例→系統調査）
**Pattern Rationale:** 4本は独立した脆弱性の発見で、具体的な単一事例から1万超サーバーの系統調査まで、狭→広のスコープで並べられる。

**Article Order & Roles:**
1. [032] Grok Build CLIの無断データ送信 — 具体的な単一インシデント
2. [069] Memory Heist（間接プロンプトインジェクション） — 攻撃手法
3. [049] IDEエージェントのワークフロー脱獄 — 研究による実証
4. [209] MCPセキュリティ白書（11,000サーバー） — 系統的な実態調査

**Narrative Arc:** 一つのツールの挙動から、機能を悪用する攻撃手法、ワークフロー全体の脱獄、そしてエコシステム全体の脆弱性調査へと、視野を広げる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [032] → [069] | 単一ツールの挙動だけでなく、エージェントの機能そのものが攻撃経路になる |
| [069] → [049] | 攻撃は単発でなくワークフロー全体にも及ぶ |
| [049] → [209] | 個別の脆弱性を超え、エコシステム全体の実態を調査すると |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 実装・運用レイヤーの穴が具体例から系統調査まで揃った
- 共通結論：エージェントの実行権限が増すほど攻撃面が現実的な脅威になる

**Conclusion Approach:** 白書(209)の統計で「人気サーバーほど危険」という系統的リスクを示して締める。

**Assembly Prompts for STEP_08:** ①どんな攻撃経路が具体化したか ②なぜ実行権限が問題か ③運用側の対策は ④エコシステム全体のリスクは

---

### Theme 4: 開発者の役割変容

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「実装をAIが担う時代に人間の専門性はどこへ移るか」という同一の問いに、アーキテクト・生産性データ・キャリアという対等な3視点が答える。

**Article Order & Roles:**
1. [100] antirez「コードでなくアイデアを支配せよ」 — 設計者の視点
2. [117] コーディングはボトルネックでない — 生産性データの視点
3. [102] ジュニア開発者の生存戦略 — キャリアの視点

**Narrative Arc:** 熟練者の設計論、調査データが示す後工程ボトルネック、そして若手が磨くべきセンスと判断力、という3つの角度で役割変容を描く。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [100] → [117] | アイデアの統御が重要というantirezの主張は、生産性調査からも裏づけられる |
| [117] → [102] | ボトルネックが後工程に移るなら、若手はどこで価値を出すか |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- 実装の価値低下に伴い、専門性はレビュー・検証・判断・センスへ移る
- 熟練者と若手で必要な適応が異なる

**Conclusion Approach:** 若手の課題(102)を、人間に残る判断力という共通軸に接続して締める。

**Assembly Prompts for STEP_08:** ①人間の役割はどこへ移るか ②データは何を示すか ③若手はどう適応するか ④開発者に残る専門性とは

---

### Theme 5: 人間中心への揺り戻し

**Pattern:** Multi-Perspective（スペクトラム: 急進→職人技）
**Pattern Rationale:** AI推進への対抗軸を、急進的抵抗から製品論・構想・職人技まで、対等な視点のスペクトラムとして提示する。

**Article Order & Roles:**
1. [036] 反AI強硬派活動家のルポ — 急進的抵抗
2. [107] 人々はもっとAIを求めていない — 製品/UXの視点
3. [135] Thinking Machinesの人間中心ビジョン — 構想の視点
4. [170] デザイン工程でAIを使わない理由 — 職人技の視点

**Narrative Arc:** 過激な抵抗運動から、静かな「求めていない」という声、人間中心AIの構想、そしてAIを排する職人技まで、人間中心の姿勢の幅を示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [036] → [107] | 過激な抵抗の対極に、静かな「AIを求めていない」という声もある |
| [107] → [135] | では人間中心のAIはどう構想されるか |
| [135] → [170] | その哲学を制作現場で徹底する例が |

**Emphasis Balance:** Technical ⭐ / Business ⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- 抵抗〜製品〜構想〜職人技という幅広い層で人間中心の視点が並ぶ
- AI推進一辺倒への対抗軸が多様な形で表出している

**Conclusion Approach:** 職人技(170)の哲学を、技術の使い方は選べるという前向きな余韻で締める。

**Assembly Prompts for STEP_08:** ①抵抗はどんな形をとるか ②ユーザーの本音は ③人間中心AIとは何か ④作り手は何を守るか

---

### Theme 6: AI経済の実像

**Pattern:** Multi-Perspective（スコープ: マクロ→生活圏→企業収益）
**Pattern Rationale:** 「熱狂の裏の数字」という同一テーマに、資金循環・住宅価格・広告収益という異なる層のデータが対等に並ぶ。

**Article Order & Roles:**
1. [200] NVIDIA循環ファイナンス — マクロ・インフラ投資
2. [201] AI長者とSF住宅高騰 — 生活圏・社会
3. [146] OpenAI広告収益90%未達 — 企業収益

**Narrative Arc:** GPUインフラの不透明な資金循環、その余波としての住宅価格、そして収益予測の実態と、マクロから企業単位までの各層で数字を検証する。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [200] → [201] | マクロの資金循環の余波は生活圏にも及ぶ |
| [201] → [146] | 一方、個別企業の収益実態に目を向けると |

**Emphasis Balance:** Technical ⭐ / Business ⭐⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- インフラ投資・生活圏・収益予測の各層で、熱狂と数字の乖離が示される
- 単一の煽りでなく、複数の独立したデータが同じ方向を指す

**Conclusion Approach:** 広告収益の予測未達(146)を、期待と現実の乖離の象徴として締める。

**Assembly Prompts for STEP_08:** ①資金はどう循環しているか ②生活圏への影響は ③収益の実態は ④この乖離は何を意味するか

---

### Theme 7: 日本企業/行政のAI組織実装

**Pattern:** Multi-Perspective（並列ケーススタディ）
**Pattern Rationale:** 民間・行政・規制業種という異なる組織の実装事例が、「個人効率化から組織実装へ」という同一テーマの対等な事例として並ぶ。

**Article Order & Roles:**
1. [228] 食べログ「Deal Provider」 — 民間・プロダクト設計
2. [195] デジタル庁「源内」国産LLM実証 — 行政
3. [218] 金融機関の全社AI導入 — 規制業種・ガバナンス

**Narrative Arc:** AIでDDD実装を克服した民間事例、国産クラウド・LLMを用いる行政実証、漏洩リスクを分解して全社導入した金融、という3つの組織レベルの実装を並べる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [228] → [195] | 民間の実装と並行して、行政でも国産基盤での実証が始まった |
| [195] → [218] | セキュリティ基準の厳しい金融でも全社導入が進む |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 個人の効率化から組織・行政レベルの実装へと段階が上がった
- 民間・行政・規制業種それぞれで導入の「現実」が語られている

**Conclusion Approach:** 金融の「導入しないリスクの可視化」(218)を、組織実装の共通論点として締める。

**Assembly Prompts for STEP_08:** ①各組織はどう実装したか ②行政と民間の違いは ③規制業種の壁はどう越えたか ④組織実装の共通条件は

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Approval Date:** 2026-07-18
**Approver:** beijaflor (via AskUserQuestion approval gate; popup closed without inline edits)
