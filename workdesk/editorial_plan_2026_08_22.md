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

**Candidate Count by Theme (pre-trim):**
- Theme 1 (OpenAI): 5
- Theme 2 (他モデル): 6
- Theme 3 (ローカル/エッジ): 6
- Theme 4 (日本語/ソブリン): 6
- Theme 5 (AI×数学): 3
- Theme 6 (開発の役割転換): 6
- Theme 7 (セキュリティ/認可): 6
- Theme 8 (AI;DR): 7

**Total candidate pool:** 45
**Planned Main after STEP_04 trim:** ~30–36

*Note: 8 themes, within the 5–8 guideline. Theme 5 (AI×math) is a 3-article theme with documented justification above.*

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-08-30
**Reviewer:** beijaflor (Round 1: theme-by-theme AskUserQuestion; Round 2: Zed review)

**Changes Made:**
- Round 1: split old T1 → OpenAI + Other models; dropped economy/regulation/watermark theme → annex; split internals/math → 内部構造 + AI×数学; tightened local/edge, Japan, dev (role-shift), security (execution+authz); refocused AI;DR
- Round 2: dropped the LLM内部構造・創発 theme (003/174/056) → annex; approved the remaining 8 themes

**Approval:** ✅ APPROVED

- [x] APPROVED - Ready for STEP_04 curation
