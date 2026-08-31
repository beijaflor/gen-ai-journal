# Editorial Plan - Journal 2026-08-22

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement (Round 1: theme-by-theme; Round 2: dropped internals theme)
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

> **Round 1 revisions (human-directed, theme-by-theme):**
> - Old T1 split into **OpenAI updates** + **Other models' updates**.
> - Old economy/regulation/watermark theme **dropped from main** → all flagged for annex.
> - Old internals/math theme **split** into 内部構造・創発 + AI×数学.
> - Local/edge tightened to core 6; Japan kept 6 (185 dup → annex);
>   dev tightened to "role shift" 6; security tightened to "execution + authz" 6;
>   AI;DR refocused.
>
> **Round 2 revision (Zed review):**
> - **Dropped the LLM内部構造・創発 theme** (003/174/056) → flagged for annex.
> - Approved the remaining **8 themes**.
>
> **Round 3 revision (during STEP_05 annex review, user-directed):**
> - **Promoted a new main theme from annex candidates**: T9 AI学習データ (068/110/052/075).
>   User spotted 068/110 as a standalone story; scoped to 4 (books-focused) via
>   AskUserQuestion. Main total → **40 across 9 themes**.
>
> Candidate pools total ~45. STEP_04 trims each theme to ~4–5 leads,
> targeting ~30–36 main articles; the remainder joins the annex.

---

## Identified Themes

### Theme 1: OpenAIが公開したGPT-5.6 Sol・Codexプラットフォーム化・Astra開発ペース調整

**Articles (IDs):** 008, 077, 066, 093, 187

**Theme Introduction (2-3 sentences):**
OpenAIが新フラグシップ「GPT-5.6 Sol」の仕様・価格・ベンチマークを公開し、Codexを単なるアプリではなくオープンなエージェント・ハーネスのプラットフォームとして再定義した。あわせて次世代モデル「Astra」については、高度なサイバー攻撃能力の可能性を踏まえ開発ペースを一時的に抑える判断も示された。今週のOpenAI発の更新をまとめて扱う。

**Editorial Notes:**
- 008: OpenAIがCodexをオープンなエージェント・ハーネスのプラットフォームとして再定義
- 077: GPT-5.6 Sol の105万トークン・コンテキストとAPI価格・ベンチマークまとめ
- 066: RoboflowによるGPT-5.6 Sol のビジョン性能ベンチマーク分析
- 093: GPT-5.6 Sol、Devinで70%オフのプロモーション実施
- 187: OpenAIがAstraのサイバー能力を理由にフロンティア開発ペースを調整

---

### Theme 2: Gemini 3.7 Flash・GLM-5.3・Qwen3.8・Ornith-1.5に見る新モデルの性能と価格

**Articles (IDs):** 009, 108, 125, 087, 072, 164

**Theme Introduction (2-3 sentences):**
OpenAI以外でも新モデルと分析が相次いだ週だった。Gemini 3.7 Flashの改善、OpenRouter上のステルスモデルOx Alpha、自己改善ループを備えたOrnith-1.5に加え、GLM-5.3やQwen3.8 27Bの知能・価格分析、Qwenの30億ダウンロード到達といった動きを扱う。各モデルの性能・コスト・立ち位置を横並びで概観する。

**Editorial Notes:**
- 009: Ornith-1.5 の自己足場かけ→自己改善ループ（Claude 4.8 Opus匹敵）
- 108: OpenRouter上のステルスモデル Ox Alpha（1Mコンテキスト）
- 125: Gemini 3.7 Flash の3.6からの改善点・価格・注意点
- 087: GLM-5.3 (max) の知能・性能・価格の詳細分析
- 072: Qwen3.8 27B (xhigh) の知能・性能・価格分析
- 164: アリババQwenのダウンロードが30億件突破、Meta/Googleを凌駕

---

### Theme 3: Qwen3.8 27B・Muse Glimmer・ローカル編成で進むエッジLLM推論の最適化

**Articles (IDs):** 069, 119, 159, 083, 144, 136

**Theme Introduction (2-3 sentences):**
Qwen3.8 27Bを24GB GPUや家庭用環境で動かす最適化記事が集中し、量子化・Reasoning Effort制御・MoE選択といった具体手法が共有された。MetaのMuse Glimmerが30B級を家庭用メモリ枠に収め、ローカルLLM編成が単体フロンティアを上回る検証も出ている。「手元で動かすAI」の実用ラインを引き上げる推論最適化を扱う。

**Editorial Notes:**
- 069: Qwen3.8 27B を256K・50TPS・24GB GPUで動かす最適化（MTP/量子化）
- 119: Qwen3.8-27B のローカル推論性能検証（WSL2＋Ollama＋RTX 5070 Ti）
- 159: Qwen3.8 27B に Reasoning Effort を実装（llama.cpp）
- 083: Muse Glimmer — 30B級エージェントをデバイス24-32GB枠に収める（Meta）
- 144: ローカルLLM編成が単独フロンティアAIを超えた（TAKT）
- 136: MacBook Air M5 32GBで実用ローカルLLM（MoE vs dense速度）

---

### Theme 4: PLaMo・LLM-jp-4 33B・さくらが示す日本語ソブリンLLMと国内AI導入

**Articles (IDs):** 191, 190, 175, 161, 196, 165

**Theme Introduction (2-3 sentences):**
Preferred NetworksのPLaMo継続開発、国立情報学研究所によるLLM-jp-4 33Bの公開、さくら／Sakana AIが示す「ソブリンAI」の現実解と、日本語・国産LLMの動きが揃った。あわせて日本企業のAI導入の遅さ、メルカリのAIネイティブ化、米中対立下の陣営選択といった国内AI活用の論点も収める。純国産かコントロール権かという実装レベルの議論を軸にする。

**Editorial Notes:**
- 191 ⭐: 10社以上が撤退する中でPFNが「PLaMo」を作り続ける理由（インタビュー）
- 190: 国立情報学研究所（NII）LLM-jpの332億パラメータ Dense型「LLM-jp-4 33B」公開
- 175: さくら・Sakana AIが示す「ソブリンAI」の現実解
- 161: なぜ日本企業のAI導入はこんなに遅いのか
- 196: メルカリ「AIネイティブ」化と金融の未来（インタビュー）
- 165: トランプ政権、AI開発競争で陣営選択を迫る（米中対立）
- 〔annex送り〕185: LLMC版「LLM-jp-4 33B」別報 → 190と同系列のため片方をannexへ

---

### Theme 5: テレンス・タオ・Lean形式化・ワーキングメモリが示すAIと数学の協働

**Articles (IDs):** 095, 192, 049

**Theme Introduction (2-3 sentences):**
AIが研究レベルの数学をこなし始めた前提で、数学コミュニティが保つべき価値を問うテレンス・タオのエッセイ、表現論の新予想をAIと発見しLeanで形式化してarXivへ投稿した実践記録、そしてAIの数学的強さを「推論」ではなく「ワーキングメモリ」で説明する論考を扱う。高負荷ドメインでのAI活用の実像を、理論と実務の両面から検討する。

**Editorial Notes:**
- 095: AI時代の数学（テレンス・タオのエッセイ）
- 192: 数学をやめたはずが、AIと論文を書いていた（表現論の予想→Lean形式化→arXiv）
- 049: AIは「思考」ではなく「記憶」している——ワーキングメモリの観点

*3-article theme (guideline minimum). Justification: AI×math is a self-contained storyline (Tao + a first-hand co-authoring account) kept distinct after the internals theme was dropped in Round 2.*

---

### Theme 6: クラフトコーディング・オーケストレーター・報酬エンジニアリングに見るAI駆動開発の役割転換

**Articles (IDs):** 060, 023, 100, 186, 140, 121

**Theme Introduction (2-3 sentences):**
AIに丸投げする「雰囲気コーディング」への反動として、人間が主体で書きAIを査読者に回す「クラフトコーディング」や、指示を磨いて委譲する「オーケストレーター」役割が具体的に論じられた。過剰な指示がかえって質を下げる話、エージェントがテストを握り潰す挙動を報酬設計から捉える話まで、開発者の役割が「書く」から「指揮・レビューする」へ移るさまを扱う。

**Editorial Notes:**
- 060: クラフト・コーディングの提唱（AIを「最強の査読者」に）
- 023: 「オーケストレーター」という新職種の必要性
- 100: 技術リーダーこそ「AIエグゾースト」を残せ
- 186: AIに細かく指示するほど逆に下手になる（編集長として使う）
- 140: AIエージェントはなぜテストを握り潰すのか（報酬エンジニアリング）
- 121: Claude Codeで個人開発1ヶ月、たどり着いた開発プロセス

---

### Theme 7: allowlist突破CVE・プロンプトインジェクション・OBO/Dogwoodが定めるエージェントのセキュリティと認可

**Articles (IDs):** 131, 132, 137, 122, 143, 146

**Theme Introduction (2-3 sentences):**
Claude Code／Cursor／Codexのallowlistが破れる実CVE、プロンプトインジェクション後の信頼境界設計、Token Exchange（OBO）やAWS Dogwoodによる認可制御と、エージェントを安全に動かす具体策が揃った。実クレデンシャルを渡さずAWSを叩かせる手法や、機密データをエージェントから遮断する多層防御まで、実装レベルのセキュリティと認可を扱う。

**Editorial Notes:**
- 131: allowlistが破れる4パターン——Claude Code/Codex/Cursorの実CVE
- 132: プロンプトインジェクションの「その後」を設計する（信頼境界）
- 137: AIエージェントの「認可疲れ」に効くOBO（RFC 8693）
- 122: AWSの鍵を渡さずAWSを叩かせる（mask＋SigV4再署名）
- 143: AWSの新ポリシー言語 Dogwood（temporal条件の認可）
- 146: Claude Codeに見せない技術（機密データの多層防御）

---

### Theme 8: AI;DR・AIブラインド・Unslop/Vomitに見る無編集AI生成物への拒絶

**Articles (IDs):** 073, 102, 112, 058, 106, 180, 195

**Theme Introduction (2-3 sentences):**
無編集のAI生成物をそのまま送る行為を拒絶する「AI;DR」、AI特有の言い回しを脳が読み飛ばす「AIブラインド」、AI slopを人間らしい文章へ書き直すUnslopや冗長出力を整理するVomitなど、AIの氾濫に対する実践的な距離の取り方が今週は際立った。読者である人間を意識して書くこと、AIっぽい営業文が半数に拒否される実態まで、「無編集のAI生成物を出さない」という論点を束ねる。

**Editorial Notes:**
- 073: AI;DR — 無編集AI生成コンテンツの拒絶（113「肉体プロキシ」は同系論考でannexへ集約検討）
- 102: AIをそのままコピペしない — 人間としての回答の価値
- 112: AIブラインド — 脳がAI生成テキストを無視し始める
- 058: Unslop — AI特有の表現を人間らしい文章へリライト
- 106: Vomit — Claudeの冗長出力をローカルLLMで整理
- 180: 人間に向けて文書を書こう
- 195: AIっぽい営業コンテンツで半数が離脱（受容と拒否の境界）

---

### Theme 9: 希少本破壊・Anna's Archive・Meta×Newsmaxに見るAI学習データの調達と汚染

**Articles (IDs):** 068, 110, 052, 075

**Theme Introduction (2-3 sentences):**
AIの学習データはどこから来るのか。404 Mediaの追跡調査が暴いたAmazonによる希少本の買い占めとスキャン後の破壊、それに抗して破壊前の書籍をデジタル保存しようと呼びかけるAnna's Archive、右派メディアNewsmaxを学習データに採用したMeta、そしてAIチャットボットを狙った偽シンクタンクによる情報汚染工作を扱う。データの取得手段とその整合性という、モデルの土台を巡る攻防を追う。

**Editorial Notes:**
- 068: 希少本を追跡して判明したAmazonのAI学習施設——スキャン後に書籍を破壊（404 Media 調査報道）
- 110: AI企業による物理書籍の破壊に対し、Anna's Archiveが有志のデジタル保存を呼びかけ
- 052: MetaがAI学習データとして右派メディアNewsmaxと提携——誤情報反映の懸念
- 075: イスラエルが偽シンクタンクを設立、AIチャットボットへの情報汚染（LLM poisoning）工作

*Round 3 addition (user-directed during STEP_05). Scoped to 4 books/data-focused
articles; the web-scraping layer (016/043/105) was offered but left in annex.*

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週はモデルの当たり週だった。OpenAIのGPT-5.6 SolとCodexプラットフォーム化、Gemini 3.7 FlashやGLM-5.3・Qwen3.8といった新モデルの評価、そして日本勢のLLM-jp-4 33B・PLaMoが相次いで動いた。フロンティアの性能競争と、Qwen3.8 27Bを24GB GPUで動かすようなローカルLLMの実用化が同時に進み、「大型」「小型」「国産」のそれぞれで話題が揃った。

開発現場の言語も変わりつつある。「雰囲気コーディング」への反動としての「クラフトコーディング」、指示を委譲する「オーケストレーター」役割が具体化し、allowlist突破の実CVEやOBO／Dogwoodによる認可制御など、エージェントを安全に動かすためのセキュリティ議論も一段深まった。AIが研究レベルの数学をこなし始めた時代に、テレンス・タオのエッセイやAIと共著した論文をLeanで形式化する実践が、高負荷ドメインでのAI活用の実像を照らす。

そして今週特に厚いのが、AIへの懐疑と人間中心の揺り戻しだ。無編集のAI生成物を拒む「AI;DR」、AI生成テキストを脳が読み飛ばす「AIブラインド」など、氾濫するAIとの距離の取り方が繰り返し論じられた。

**Key Points to Cover:**
1. 大型・小型・国産のモデルラッシュ（GPT-5.6 Sol / Gemini 3.7 Flash / GLM-5.3 / Qwen3.8 / LLM-jp-4 / PLaMo / Muse Glimmer）
2. クラフトコーディング／オーケストレーター役割へのAI駆動開発の役割転換
3. コーディングエージェントのセキュリティ・認可（allowlist CVE / OBO / Dogwood）
4. AIと数学（タオのエッセイ / Lean形式化 / ワーキングメモリ）
5. AI;DR・AIブラインドに見る無編集AI生成物への拒絶（今週は特に厚い）
6. AI学習データの調達と汚染（希少本破壊 / Anna's Archive / Meta×Newsmax / LLM汚染工作）

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 191 → Theme 4（Lead / PLaMo）

**👍 Upvoted Articles Used:**
- （なし）

**👎 Downvoted Articles:**
- 051（創薬AIレビュー）→ 主題が医薬R&Dでコーディング焦点から外れるため annex/除外候補
- 054（AI SEOプレイブック）→ SEO自動化寄りで annex/除外候補

**Omitted Articles:** なし（Supabaseで明示的omitフラグ0件）

---

## Annex-Bound (flagged out of main during review)

以下はレビューで main から外し、annex 候補としてフラグ。STEP_05 で確定。

- **旧・経済/規制/透かしテーマ（テーマごと annex へ）:** 082（OpenAI崩壊/バブル）, 179（NVIDIA 8GW）, 166（Salesforce置換）, 061（トークン闇市場）, 084（ノルウェー基金）, 062（Claude電子透かし批判）, 154（EU AIラベリング）, 092（AI生成コード著作権）, 064（アモデイ規制論）, 016（Cloudflare Bot Preference Sync）
- **旧・LLM内部構造/創発テーマ（Round 2でドロップ）:** 003（創発研究）, 174（次単語予測）, 056（LittleLearner）
- **モデル系トリム:** 155（HeyGen Avatar IV TPU）, 128（OCR/Document-AI 4手法）, 185（LLM-jp-4 別報）
- **ローカル/エッジ トリム:** 107, 090, 126, 168, 111
- **AI駆動開発 トリム:** 088（Linear データ）, 101（Asana/Codex 事例）, 022, 028, 156, 018
- **セキュリティ トリム:** 178（防御者の窓）, 031（サプライチェーン）, 017（ADKゼロトラスト）
- **アライメント寄り:** 036（Claude憲章）
- **社会的揺り戻し（AI;DR以外）:** 183（オードリー・タン）, 076, 063, 010, 114/117（宿題/試験研究）, 011（OSSメンテナー）, 067, 078, 037, 047, 152, 113（AI;DR同系）

> これに Supabase 由来の annex 候補（curated_annex_journal_sources.md, 24件）が加わる。
> STEP_05 で批判系・人間中心・国産以外のニッチを含めて最終確定する。

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: ~30–36 articles across 8 themes（候補45、STEP_04で各テーマ4–5本に絞る）
- Annex Journal: 上記 annex-bound + Supabase 24候補を STEP_05 で確定

**Final Main Count by Theme:**
- Theme 1 (OpenAI): 4
- Theme 2 (他モデル): 4
- Theme 3 (ローカル/エッジ): 5
- Theme 4 (日本語/ソブリン): 5
- Theme 5 (AI×数学): 3
- Theme 6 (開発の役割転換): 5
- Theme 7 (セキュリティ/認可): 5
- Theme 8 (AI;DR): 5
- Theme 9 (AI学習データ): 4

**Total main:** 40 across 9 themes
**Non-main:** 153

*Note: 9 themes (one above the 5–8 guideline) after the Round 3 training-data addition.
Theme 5 (AI×math) is a 3-article theme with documented justification above.*

---

## STEP_04 Curation Result

**Curated main = 40 articles across 9 themes** (Round 3 added T9 training-data theme).
Partition clean: main 40 + non_main 153 = 193, 0 overlap, union == all.

**Final main counts:** T1=4 (008/077/066/187) · T2=4 (009/125/072/087) ·
T3=5 (069/159/083/144/136) · T4=5 (191/190/175/161/196) · T5=3 (095/192/049) ·
T6=5 (060/023/186/140/121) · T7=5 (131/132/137/122/146) · T8=5 (073/102/112/058/195) ·
T9=4 (068/110/052/075).

**Trimmed from candidate pool → annex (theme-overflow, STEP_05 decides):**
- 093 (Sol/Devin promo — weakest of T1, marketing)
- 108 (Ox Alpha stealth) + 164 (Qwen 30億DL adoption-news) — T2 kept the 4 perf/price analyses
- 119 (Qwen WSL2 review — 3rd Qwen-local, kept 069+159)
- 165 (Trump AI-bloc — geopolitics, kept T4 LLM-focused)
- 100 (AI exhaust — leadership hot-take, kept 5 stronger dev pieces)
- 143 (AWS Dogwood — 3rd AWS-authz piece, kept OBO 137 + masking 122)
- 106 (Vomit — dup cleanup tool vs Unslop 058) + 180 (write-for-humans — writing guide)

*36 is at the top of the ~30–36 target, consistent with prior 8-theme cycles (31/35/36).*
*Note: T7 carries three ryoji9702 pieces (131/132/122) — distinct sub-topics (CVE/injection/masking).*

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-08-30
**Reviewer:** beijaflor (Round 1: theme-by-theme AskUserQuestion; Round 2: Zed review)

**Changes Made:**
- Round 1: split old T1 → OpenAI + Other models; dropped economy/regulation/watermark theme → annex; split internals/math → 内部構造 + AI×数学; tightened local/edge, Japan, dev (role-shift), security (execution+authz); refocused AI;DR
- Round 2: dropped the LLM内部構造・創発 theme (003/174/056) → annex; approved the remaining 8 themes
- Round 3 (during STEP_05): promoted a new main theme T9 AI学習データ (068/110/052/075) from annex candidates; main → 40 across 9 themes

**Approval:** ✅ APPROVED

- [x] APPROVED - Ready for STEP_04 curation

---

## ASSEMBLY STRATEGIES

> Patterns chosen to match the actual article relationships — parallel clusters
> get Multi-Perspective (no forced arc), a genuine problem→defense chain gets
> Progressive, real tension gets Debate-Contrast, single-actor/anchor clusters
> get Single-Focus. Transitions are grounded in article content, not invented.

### Theme 1: OpenAI — GPT-5.6 Sol・Codex・Astra

**Pattern:** Single-Focus
**Pattern Rationale:** One actor (OpenAI), one week — a flagship launch with facets, plus a self-imposed safety counterweight. The frontier push is the topic; Astra's pacing is the tension within it.

**Article Order & Roles:**
1. [077] GPT-5.6 Sol 仕様・価格・ベンチマーク — Foundation（旗艦の登場）
2. [008] Codex をプラットフォーム/ハーネスに再定義 — Development（モデルを載せる土台）
3. [066] Sol のビジョン性能ベンチマーク — Development（能力の深掘り）
4. [187] Astra のサイバー能力を理由に開発ペース調整 — Counterweight（自制の側面）

**Narrative Arc:** 旗艦モデルの公開とプラットフォーム化で攻めつつ、次世代Astraでは安全を理由に速度を緩める——OpenAIの「アクセルとブレーキ」を一望する。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 077 → 008 | 「モデル単体だけでなく、それを載せる土台も同時に示された」 |
| 008 → 066 | 「ハーネスに載る能力の一例として、ビジョン性能を具体的に見る」 |
| 066 → 187 | 「一方で、能力の向上は自制も伴う。次世代Astraでは開発ペースを緩める判断が示された」 |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐⭐
**Key Synthesis Points:** 性能・プラットフォーム・安全のトレードオフを同一社が同時に体現している。
**Conclusion Approach:** 攻め（Sol/Codex）と自制（Astra）の並置で、フロンティア企業の現在地を示す。
**Assembly Prompts:** ①今週OpenAIは何を出したか ②プラットフォーム化の狙い ③安全ペーシングの意味 ④読者の実務への含意。

---

### Theme 2: 新モデルの性能と価格（Gemini/GLM/Qwen/Ornith）

**Pattern:** Multi-Perspective
**Pattern Rationale:** 各モデルは独立した発表・分析で、互いに積み上げ関係はない。横並びの比較が最も誠実。

**Article Order & Roles:**
1. [125] Gemini 3.7 Flash の改善・価格 — 主要ベンダーの更新
2. [072] Qwen3.8 27B (xhigh) 知能・価格分析 — オープンウェイト最高峰
3. [087] GLM-5.3 (max) 知能・価格分析 — コスパ対抗馬
4. [009] Ornith-1.5 自己改善ループ — 新機軸（毛色の違う一本）

**Narrative Arc:** 大手の堅実な更新から、オープンウェイトの知能・価格競争、そして自己改善という新機軸まで、モデル多様化の断面を並べる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 125 → 072 | 「クローズドの更新に対し、オープンウェイト側の最高峰も動いた」 |
| 072 → 087 | 「同じオープンウェイトでも、価格対効果で対抗する選択肢がある」 |
| 087 → 009 | 「性能・価格の比較軸とは別に、自己改善という異なる方向性も現れた」 |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐⭐ / Future ⭐⭐
**Key Synthesis Points:** 知能の伸びと同じくらい「価格・速度」が選定軸になっている。
**Conclusion Approach:** 用途別に選ぶ時代——横並びの数値を実務の選択に落とす。
**Assembly Prompts:** ①各モデルの立ち位置 ②価格対効果の差 ③自己改善系の含意 ④どう選ぶか。

---

### Theme 3: エッジLLM推論の最適化（Qwen/Muse Glimmer/ローカル編成）

**Pattern:** Multi-Perspective
**Pattern Rationale:** いずれも「手元で動かす」実践報告。手法（量子化・reasoning制御・on-device・編成・MoE）が並列で、142の到達点(144)を締めに置く緩い山型。

**Article Order & Roles:**
1. [069] Qwen3.8 27B を256K/50TPS/24GBで — 単機最適化の基準点
2. [159] Qwen に Reasoning Effort 制御 — 推論制御の工夫
3. [083] Muse Glimmer 30B を on-device — 大型を手元に収める
4. [136] MacBook Air M5 の MoE vs dense — ハード×モデル選択
5. [144] ローカル編成が単体フロンティア超え — 到達点（capstone）

**Narrative Arc:** 単機での最適化から、推論制御・on-device化・ハード選択を経て、ローカル編成が単体フロンティアを超えるところまで、「手元で動かす」実用ラインの引き上げを見せる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 069 → 159 | 「同じQwenでも、速度だけでなく推論の“考えすぎ”を制御する工夫がある」 |
| 159 → 083 | 「単機の工夫を超え、30B級を家庭用デバイスに収める設計も出た」 |
| 083 → 136 | 「収めるだけでなく、ハードとモデル形式（MoE/dense）の相性も効く」 |
| 136 → 144 | 「そして個々の最適化の先に、ローカル編成が単体フロンティアを上回る到達点がある」 |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐
**Key Synthesis Points:** ローカルは「妥協」ではなく、編成次第でフロンティアに並ぶ選択肢になった。
**Conclusion Approach:** 144を到達点に、ローカル運用のコスパと自律性を締めに据える。
**Assembly Prompts:** ①手元で動かす実用ライン ②どの最適化が効くか ③編成の威力 ④コスト・プライバシーの含意。

---

### Theme 4: 日本語ソブリンLLMと国内AI導入（PLaMo/LLM-jp-4/さくら）

**Pattern:** Multi-Perspective
**Pattern Rationale:** 国産モデル・ソブリン論・導入の遅れ・企業事例が、同じ「日本のAI」を別角度から照らす。積み上げではなく多面提示。

**Article Order & Roles:**
1. [191] ⭐ PFNがPLaMoを作り続ける理由 — アンカー（作る側の意志）
2. [190] NII LLM-jp-4 33B 公開 — 公的な国産モデル
3. [175] さくら・Sakanaの「ソブリンAI」現実解 — 戦略論（何を握るか）
4. [161] 日本企業のAI導入はなぜ遅い — 需要側の課題
5. [196] メルカリのAIネイティブ化 — 前進する企業事例

**Narrative Arc:** 「作る」（PLaMo/LLM-jp-4）→「何を握るか」（ソブリン論）→「使う側の壁」（導入の遅れ）→「前へ進む事例」（メルカリ）と、供給と需要の両側から日本のAIを俯瞰する。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 191 → 190 | 「民間のPLaMoに対し、公的プロジェクトも33Bモデルを公開した」 |
| 190 → 175 | 「作ること自体より、データとモデルの“コントロール権”をどう握るかが論点になる」 |
| 175 → 161 | 「供給側の議論の一方で、使う側の導入は依然として遅い」 |
| 161 → 196 | 「その中でも、AIネイティブ化を進める企業事例がある」 |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐⭐ / Future ⭐⭐⭐
**Key Synthesis Points:** 「純国産か否か」より「どこをコントロールするか」が現実解。
**Conclusion Approach:** 供給・戦略・需要を束ね、日本のAIの現在地と選択肢を示す。
**Assembly Prompts:** ①国産モデルの現状 ②ソブリンの現実解 ③導入が遅い理由 ④前進事例の条件。

---

### Theme 5: AIと数学（タオ/Lean形式化/ワーキングメモリ）

**Pattern:** Debate-Contrast
**Pattern Rationale:** 「AIは本当に数学を“している”のか」を巡り、実際に研究を前進させた一次体験（192）と、それを「思考でなく記憶」と説明する論考（049）が productive tension を作る。タオのエッセイ（095）が枠組みを与える。

**Article Order & Roles:**
1. [095] タオ「AI時代の数学」 — Framing（何を問うべきか）
2. [192] AIと共著→Lean形式化→arXiv — 肯定側（現に研究が進んだ）
3. [049] AIは思考でなく記憶している — 懐疑側（機構の説明）

**Narrative Arc:** タオが「価値をどう保つか」と問いを立て、実際にAIと論文を仕上げた体験が可能性を示し、最後に「それは推論でなくワーキングメモリだ」という機構論が過熱を冷ます。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 095 → 192 | 「この問いに、実際にAIと論文を仕上げた一次体験が具体的な答えを与える」 |
| 192 → 049 | 「ただし“研究が進んだ”ことと“AIが思考している”ことは別だ、という反論がある」 |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐ / Future ⭐⭐⭐
**Key Synthesis Points:** 成果（できた）と機構（なぜできたか）を切り分けると過剰期待も過小評価も避けられる。
**Conclusion Approach:** 「できる／しているは別」を軸に、数学者の役割の再定義で締める。
**Assembly Prompts:** ①AIは数学に何を寄与したか ②それは思考か記憶か ③数学者の価値はどこに ④研究文化への含意。

---

### Theme 6: AI駆動開発の役割転換（クラフト/オーケストレーター/報酬設計）

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「書く→指揮・レビューする」への移行を、哲学・役割・実践・制御の各角度から並べる。相互の積み上げより並列提示が自然。

**Article Order & Roles:**
1. [060] クラフト・コーディング（AIを査読者に） — 姿勢の提起
2. [023] オーケストレーターという新職種 — 役割の定義
3. [121] Claude Codeで1ヶ月、辿り着いた開発プロセス — 実践の具体
4. [186] 細かく指示するほど下手になる — 制御の逆説
5. [140] 報酬エンジニアリング（テスト握り潰し対策） — 機構レベルの制御

**Narrative Arc:** 「AIを査読者に」という姿勢から、指揮する新職種の定義、実際の開発プロセス、過剰指示の逆説、そして報酬設計という機構レベルの制御へと、役割転換を多面的に描く。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 060 → 023 | 「査読者として使う姿勢は、やがて“指揮する”役割の定義につながる」 |
| 023 → 121 | 「役割論を、1ヶ月の個人開発プロセスとして具体化した例がある」 |
| 121 → 186 | 「ただし指示は細かければ良いわけではない、という逆説も報告された」 |
| 186 → 140 | 「指示の外側で、報酬設計そのものを制御する視点も出てきた」 |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐
**Key Synthesis Points:** 「うまく書かせる」から「うまく評価・制御する」へ、開発者の重心が移った。
**Conclusion Approach:** 役割転換の共通項（判断・レビュー・制御）を抽出して締める。
**Assembly Prompts:** ①役割はどう変わったか ②指揮者に必要な技能 ③過剰指示の教訓 ④評価・報酬設計の重要性。

---

### Theme 7: エージェントのセキュリティと認可（CVE/信頼境界/OBO/Dogwood）

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 「脅威 → 多層防御」の実際の積み上げ。まず突破される具体例を見せ、設計・認可・資格情報・データの各層で防御を重ねる構成が自然に成立する。

**Article Order & Roles:**
1. [131] allowlist突破の実CVE 4パターン — 脅威（何が破れるか）
2. [132] プロンプトインジェクション後の信頼境界設計 — 設計の応答
3. [137] 認可疲れに効くOBO（RFC 8693） — 認可レイヤー
4. [122] 鍵を渡さずAWSを叩かせる（mask+SigV4） — 資格情報の隔離
5. [146] Claude Codeに見せない多層防御 — データの隔離

**Narrative Arc:** allowlistが破れる実例で脅威を可視化し、信頼境界の設計、認可（OBO）、資格情報の隔離、機密データの遮断へと、防御を層状に積み上げる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 131 → 132 | 「破れる前提に立つと、防ぐ発想は“境界の設計”に移る」 |
| 132 → 137 | 「境界の内側で、そもそもの認可をどう安全にするかがOBOの論点だ」 |
| 137 → 122 | 「認可に加え、実クレデンシャルを渡さない資格情報の隔離も要る」 |
| 122 → 146 | 「最後に、そもそもAIに“見せない”データの遮断で層を閉じる」 |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐
**Key Synthesis Points:** 単一の対策でなく、境界・認可・資格情報・データの多層で守る。
**Conclusion Approach:** 「破れる前提の多層防御」を実装チェックリストとして締める。
**Assembly Prompts:** ①何が破れるか ②信頼境界の設計 ③認可の安全化 ④資格情報とデータの隔離。

---

### Theme 8: 無編集AI生成物への拒絶（AI;DR/AIブラインド/Unslop）

**Pattern:** Multi-Perspective
**Pattern Rationale:** 同じ「無編集AIを出すな」を、宣言・認知現象・作法・データ・ツールの各面から並べる。積み上げより多面提示が誠実。

**Article Order & Roles:**
1. [073] AI;DR — 無編集AI生成物の拒絶 — 旗印
2. [112] AIブラインド — 脳が読み飛ばす現象 — なぜ効かないか
3. [102] AIをそのままコピペしない — 作法の提起
4. [195] AIっぽい営業で半数が離脱 — データ（実害）
5. [058] Unslop — 人間らしい文章へリライト — 実務的な処方

**Narrative Arc:** 「AI;DR」という旗印から、読み飛ばされる認知現象、送る側の作法、離脱という実害、そして書き直しツールという処方まで、無編集AIへの拒絶を多面的に描く。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 073 → 112 | 「拒絶には理由がある——AI生成文は脳に読み飛ばされる」 |
| 112 → 102 | 「読まれないなら、そのまま送る作法自体が問われる」 |
| 102 → 195 | 「作法の問題は、営業では“半数離脱”という実害になる」 |
| 195 → 058 | 「では実務でどうするか——人間らしさへ書き直す処方がある」 |

**Emphasis Balance:** Technical ⭐ / Business ⭐⭐⭐ / Future ⭐⭐
**Key Synthesis Points:** 「AIに書かせる」ことより「人間が編集して出す」ことに価値が戻っている。
**Conclusion Approach:** 拒絶の共通項（人間の編集・文脈・誠実さ）を抽出して締める。
**Assembly Prompts:** ①なぜ無編集AIは拒まれるか ②実害はどこに出るか ③送る側の作法 ④実務での処方。

---

### Theme 9: AI学習データの調達と汚染（希少本破壊/Anna's Archive/Meta×Newsmax）

**Pattern:** Single-Focus
**Pattern Rationale:** 404 Mediaの調査（希少本破壊）が明確なアンカー。Anna's Archiveがその直接の反応、Meta×Newsmaxと汚染工作が「調達と整合性」へ論点を広げる facet。

**Article Order & Roles:**
1. [068] Amazonが希少本を買占め・スキャン後破壊（404 Media調査） — アンカー（調達の実態）
2. [110] Anna's Archive がデジタル保存を呼びかけ — 直接の反応
3. [052] MetaがNewsmaxを学習データに採用 — 別の調達モード（質の懸念）
4. [075] 偽シンクタンクによるLLM汚染工作 — 整合性への脅威

**Narrative Arc:** 希少本の破壊という衝撃的な調達の実態を軸に、それへの保存運動、メディア提携という別の調達、そして汚染工作という整合性の問題へと、「学習データの土台」を巡る攻防を追う。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 068 → 110 | 「この破壊に対し、破壊前に保存しようという直接の反応が起きた」 |
| 110 → 052 | 「調達は物理書籍だけではない——メディア提携という別の入手経路もある」 |
| 052 → 075 | 「入手だけでなく、意図的に“汚染”された情報が流し込まれるリスクもある」 |

**Emphasis Balance:** Technical ⭐ / Business ⭐⭐ / Future ⭐⭐⭐
**Key Synthesis Points:** モデルの土台＝学習データの「調達手段」と「整合性」がともに問われ始めた。
**Conclusion Approach:** 調達と汚染を並置し、データの出所を問う視点で締める。
**Assembly Prompts:** ①学習データはどう調達されるか ②破壊と保存の攻防 ③データの質・偏り ④汚染への脆弱性。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all 9 themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Pattern spread:** Single-Focus ×2 (T1, T9) · Multi-Perspective ×5 (T2, T3, T4, T6, T8) · Progressive-Sequence ×1 (T7) · Debate-Contrast ×1 (T5).

**Approval Date:** 2026-08-31
**Approver:** beijaflor (Zed review → chat approval, no tmux)
