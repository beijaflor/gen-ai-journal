# Editorial Plan - Journal 2026-11-14

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

> Source pool: 249 summaries (IDs 1–251, gaps at 43/152).
> Human curation signals this cycle (from `curation_flags.md`): ⭐ 137 ／ 👎 056, 125, 127, 247 ／ no omit.
> Supabase annex pre-flags (16, from `curated_annex_journal_sources.md`): 047, 050, 063, 071, 087, 113, 148, 160, 171, 172, 186, 191, 202, 208, 217, 238.
> Draft scope: 8 main themes / 39 articles (inside the 6–9 / 30–40 spec). Order below = editorial priority (lead theme first). The remaining ~210 summaries route to annex/omit in STEP_04/05.
> 👎 056/125/127/247 are not used as leads or theme-drivers. No Supabase annex pre-flagged article is placed in main. (011 and 232 carry high *AI annexPotential scores* but no human annex flag.)
> **Rev.1 (human direction via gate):** (1) former Themes 5 & 6 united into one "AIとともにデザインする" theme (Theme 5, 8 articles); (2) former Theme 7 narrowed to focus on the Anthropic IPO (Theme 6); (3) former Theme 9 (Ubie/harness: 137, 079, 146, 064) moved to annex candidates per human decision — this demotes the ⭐ 137 standout out of main (recorded below), overriding the default "standout anchors a main theme" guidance.
> **Rev.2 (human direction, 2026-11-18):** Gemini 4 (Carbon/Hydrogen) + Antigravity promoted from annex candidates to a new main theme — **Theme 2**, 5 articles (045/159/219/220/167) — inserted right after Theme 1 (Fable 5.2). Former Themes 2–7 shift down to Themes 3–8. Main now **8 themes / 39 articles**. Thin npaka rehash 166 and the infra/feature pieces 241 (Pathways) / 242 (MaxText) / 243 (AI Studio×Maps) remain annex candidates. No third-party benchmark of Gemini 4 exists in the pool (167 Publickey is the one independent voice); no rival/eval framing was manufactured.

---

## Identified Themes (8 main themes / 39 articles)

**Reminder: titles are concrete, specific, factual — named anchors + single verb + substantive topic phrase.**
**Order below = editorial priority (lead theme first).**

### Theme 1: Claude Fable 5.2・Mythos 5.2 発表、Artificial Analysis首位評価と高コスト・プロンプト設計の実際

**Articles (IDs):** 033, 035, 103, 134

**Theme Introduction:**
Anthropicが新フラッグシップ「Claude Fable 5.2」と専門組織向け「Mythos 5.2」を発表し、前世代比で最大30%（ファストモードで2.5倍）の高速化とコーディング・推論・視覚処理の大幅な向上を打ち出した。第三者評価のArtificial Analysisはベンチマーク首位を認める一方で極めて高いコストと低速な推論を指摘しており、公式プロンプトガイドと国内実務者の検証は、エフォート調整やコード所有権の明示といった「超高性能モデルの使い所」を具体的に論じている。

**Editorial Notes:**
- 033: Anthropic公式発表。Fable 5.2/Mythos 5.2。1,000体エージェントによるフェルマーの最終定理の30時間形式化、ブラックホール物理の未解決問題、ハードウェア設計能力。Fableは一般向け、Mythosはサイバーセキュリティ・バイオ専門組織向け、アンチ蒸留技術を導入（リード・一次情報）
- 035: Artificial Analysis。Fable 5.2は知能ベンチで1位だが高コスト・低速な推論特化型という第三者評価
- 103: Anthropic公式プロンプトガイド。エフォート調整、タスク完遂指示、コード所有権の明示などFable 5.2向け設計手法
- 134: 国内実務者による公式プロンプトガイドの読み解き。エフォート設定・コード所有権・新セーフガードを整理し実務での使い所を考察

---

### Theme 2: Gemini 4 Carbon・Hydrogen・Antigravityが示すGoogleの次世代モデルとエージェント基盤

**Articles (IDs):** 045, 159, 219, 220, 167

**Theme Introduction:**
Fable 5.2と同じ週に、Googleも次世代モデル「Gemini 4」を2つの構成で公開した。サイバーセキュリティ・複雑なマルチステップのプログラミング・科学的推論に特化した「Carbon」と、高度な推論と実行速度を両立しエージェント/コーディングワークフローに最適化した「Hydrogen」で、Hydrogenは1Mトークンの統合コンテキストと推論制御「思考レベル」を備える。あわせてエージェント開発環境Antigravityが、高速モデルHydrogenと高推論モデルを動的に連携させるOrchestratorを導入し、ローカルPCの電源を切ってもクラウド上のVMで作業を続ける「リモートエージェント」機能を搭載するなど、モデルと実行基盤の両面が更新された。

**Editorial Notes:**
- 045: Google公式。Gemini 4 Carbon提供開始。サイバーセキュリティ・複雑なマルチステップのプログラミング・科学的推論で業界最高水準の性能を主張（リード・一次情報）
- 159: Google公式。Gemini 4 Hydrogen。高度な推論と実行速度を両立し、自律エージェント/コーディングワークフローに最適化した新モデル
- 219: Google AI Studio。Hydrogenの新機能。1Mトークンの統合コンテキストと推論制御「思考レベル」を整理
- 220: Google Antigravity。HydrogenとOrchestratorを発表。高速モデルと高推論モデルを動的に連携させ効率を最大化
- 167: Publickey（第三者・国内報道）。Antigravityの「リモートエージェント」。ローカルPCの電源を切ってもクラウドVMで開発・テストを自律継続

---

### Theme 3: Claude Fable・AlphaProof Code・PSIが示す形式証明・未解決問題・ゲノムでのAI活用

**Articles (IDs):** 144, 042, 097, 119, 156

**Theme Introduction:**
Fable 5.2の発表と同じ週に、AIが数学・科学の最前線で具体的な成果を出した事例が集中した。Fable 5.2を用いた1,000体のエージェントチームが自らSQLで作業を管理しフェルマーの最終定理をLeanで再現し、DeepMindのAlphaProof CodeはSignalプロトコルの実装コードを数学的に検証、PSIは量子計算の未解決問題「Aaronson-Ambainis予想」を証明した。別の事例ではClaudeがゲーデルの未公開ノートを解読し、DeepMindのAlphaGenome 2がゲノム解釈の精度を高めている。AlphaProof Codeでは人間のレビューが全体のわずか1%に絞られるなど、専門的な検証作業をAIが大きく肩代わりする構図が見える。

**Editorial Notes:**
- 144: claude.dev。Fable 5.2初期版の1,000体エージェントがフェルマーの最終定理の形式的証明をLeanで再現。エージェントが自らSQLに5テーブルを作り階層管理、トークン1/3・証明コード1/7に短縮、100万回超のツール呼び出しで深刻な規約違反ゼロ（リード）
- 042: Google DeepMind。AlphaProof Code。Gemini Carbon搭載エージェントがLeanで600万行超の証明を生成しSignalプロトコル実装を深層形式検証、人間のレビューはわずか1%、数年を4週間に短縮
- 097: Physical Superintelligence (PSI)。AI研究システムが量子計算の限界に関する2008年以来の未解決問題「Aaronson-Ambainis予想」を証明
- 119: Guardian。Claudeを用いてクルト・ゲーデルの難解な略記ノートから数百の未知の定理・歴史的発見を解読
- 156: Google DeepMind。AlphaGenome 2。1億以上の細胞プロファイルを学習し、細胞タイプ別のDNA変異影響を従来比2倍の精度で予測

---

### Theme 4: OpenAI Decisions・Gemini Decisions・Perplexity Deciderが広げる「判断特化型AI」

**Articles (IDs):** 248, 213, 114, 008

**Theme Introduction:**
文章を生成せず、分類・採点・判定のような「結果だけ」を返す判断特化型AIが、低コスト・高速な業務自動化の軸として急速に広がった。OpenAIのDecisions API（GPT-6 Luna基盤）、Gemini Decisions API、Perplexity Decider v1.3が相次いで登場し、VercelのAI Gateway統計では判断モデルが全リクエストの26%を占めるに至っている。汎用LLMと判断特化型を使い分ける設計が、エージェント制御やルーティングの標準になりつつある。

**Editorial Notes:**
- 248: Impress。判断特化型AIの俯瞰。TypeSafe AIのJev（8.7億ドル調達）、OpenAI Decisions（GPT-6 Luna、最大10倍高速）、Cloudflare Clef・Databricks ai_decide・AWS Strands Decider。処理費約88%削減・応答40倍高速の事例（リード・俯瞰）
- 213: Google。Gemini Decisions API。1回の推論で最大1,000件のマルチモーダル判定を150〜250msで処理、出力トークン無料
- 114: Perplexity。Decider v1.3。LLMアーキテクチャを活かした高速・高精度な分類/抽出特化の意思決定モデル
- 008: Vercel AI Gateway 2026年11月統計。安価な決定モデルが全リクエストの26%に急拡大、新規チーム獲得でAnthropicが2:1

---

### Theme 5: ARTEX以外の45ツール・GPT-6 Cyber・1Password Proverが示すAIセキュリティの攻防と機密漏洩

**Articles (IDs):** 153, 232, 072, 244, 022

**Theme Introduction:**
AIが攻撃と防御の双方を担い始め、セキュリティの前提が組み替わりつつある。GitGuardianやCloudflareはARTEXをはじめ数十の自律型ペンテストフレームワークの急拡大を報告し、OpenAIはアライメントを備えたGPT-6 Cyberを、1Passwordはリポジトリ全体を巡回するエージェント検証ステージ「Prover」を投入した。一方で、コーディングエージェントが機密を設定ファイルに保存しGitHubへ露出させる実態も明らかになり、攻防と漏洩が同じ技術基盤の上で進んでいる。

**Editorial Notes:**
- 153: GitGuardian。ARTEX以外の45のエージェント型AI攻撃フレームワークを調査し、秘密情報探索能力やShodan露出、防御リスクを整理（リード・攻撃動向）
- 232: Cloudflare。AI自律型攻撃フレームワークの急拡大に対抗する「モダンセキュリティモデル」6つの柱（防御の全体像）
- 072: OpenAI。GPT-6 Cyber。高い脆弱性発見・実証能力と、指定範囲を厳守するアライメントを両立したサイバーセキュリティ特化モデル
- 244: 1Password。セキュリティレビューSAGEに自律調査ステージ「Prover」を追加し、呼び出し元まで巡回して誤検知を大幅削減（防御）
- 022: Apiiro。Claude Code等がシークレット入りコマンドをローカル設定ファイルに保存し、GitHubへの誤配備で数千件が露出（漏洩の実態）

---

### Theme 6: デザイナーの価値・デザインシステムAIレディネス・A2UI/UI SDKが問い直すAIとともにデザインする役割とツール

**Articles (IDs):** 010, 013, 201, 198, 034, 124, 180, 011

**Theme Introduction:**
AIがデザインの生産性を一気に高め、一貫したUIを生成できるようになったことで、デザイナーに残る価値とデザインの作り方の両方が問い直されている。前半では、単なる「作業機械」に陥らないためのクラフト・審美眼・ビジネス理解の8要件、暗黙知と人間の品質保証を定義する「デザインシステムのAIレディネス」、AIを「新しい古い素材」として直接扱う姿勢、MCPとマニフェストで「本物のコード」のプロトタイプを生む実践が並ぶ。後半では、A2UI 1.0やVercel UI SDK、WebMCPといった、エージェント自身がネイティブなUIを構築・操作するための標準が登場し、「UIの操作はエージェントに任せる」前提への移行を示している。

**Editorial Notes:**
- 010: uxdesign。AIがデザインの生産性を高める中、デザイナーが「作業機械」に陥らないために磨くべきクラフト・審美眼・ビジネス理解など8つのスキル（リード）
- 013: seanvoisen。デザインシステムの「AIレディネス」とは機械可読な文書化ではなく、暗黙知の扱いと人間が品質を支える部分の定義であるという論考
- 201: uxdesign。MCPとマニフェストを用い、既存コンポーネントの模倣ではなく「本物のコード」で実用的プロトタイプを生成する実践ガイド
- 198: uxdesign。AIを「新しい古い素材」と定義し、静的モックを超えてコードで試行しモデル出力のばらつきを直接理解すべきだと提唱
- 034: killianc。「I Am Done Using Your UI」。人間が操作する時代からエージェントが代理消費する時代への移行と、エージェントフレンドリーな設計提言（概念軸・後半への橋渡し）
- 124: Vercel Labs。UI SDK。エージェントによるコンポーネント自動生成とAPI経由の直接操作を最適化するヘッドレスUIライブラリ
- 180: Google。A2UI 1.0。エージェントが各プラットフォーム固有のネイティブコンポーネントでUIを描画するオープンプロトコルの安定版
- 011: WebMCP。ブラウザ上のAIエージェントがWebページ機能を直接呼び出す新プロトコルをToDoアプリで解説（AI annexPotentialは高めだが human annex flag はなく主に配置）

---

### Theme 7: Anthropicのプロスペクタス・ロードショー・アモデイ発言が映すNasdaq上場（ANT）の実像と懐疑

**Articles (IDs):** 214, 044, 109

**Theme Introduction:**
AnthropicがNasdaq上場（ティッカーANT）に向けて動き出し、その財務と期待値が一気に可視化された。公式プロスペクタスは170億ドルの収益・前年比12倍超の成長・11,900社超の大口顧客を開示し、ロードショーは1株70〜78ドルで約8.25億株の売り出しを提示した。一方で、ダリオ・アモデイCEOの「10年以内にがんを克服する」という発言には、IPOを意識した誇大広告だとして医学界から懐疑の声が上がっている。

**Editorial Notes:**
- 214: Anthropic公式プロスペクタス。Nasdaq上場（ANT）。170億ドルの収益、前年比12倍超成長、11,900社超の大口顧客、楽天・Salesforce等の導入事例（リード・一次情報）
- 044: Anthropic公式。IPOロードショー開始。1株70〜78ドルで約8.25億株を売り出し（一次情報）
- 109: Business Insider。アモデイCEOの「10年以内にがん克服」提言に、IPO狙いの非現実的な誇大広告だと医学界・専門家が批判

**Note:** 市場・バブル系の121（NVIDIA循環取引）・224（HN AI crash）・025（OpenAI 1.25兆ドル）・016（AI株比較）は本テーマから外し、アネックス候補へ（下記）。

---

### Theme 8: 酒井邦嘉・ESLint・No AI Slopが示す生成AIへの抵抗と人間中心の視点

**Articles (IDs):** 030, 089, 233, 116, 154

**Theme Introduction:**
生成AIの普及に距離を取り、人間の判断・責任・信頼を問い直す論考が目立った。15年の開発経験を持つ著者による多面的な生成AI批判、成果物だけを見て専門職を「不要」と断じる風潮への反論、そしてAI生成物（スロップ）を拒絶し人間の理解・意図・責任を再定義する宣言が並ぶ。制度面ではESLintがAI生成PRの増加を理由に外部貢献者報酬制度を終了し、教育面では言語脳科学者が青少年のAI使用の全面禁止を提言するなど、現場・制度・教育の各面で抵抗が具体化している。

**Editorial Notes:**
- 030: estherweidauer。生成AIを技術的・環境的・認識論的・政治的観点から批判的に分析し、普及に反対する理由を論じる包括的論考（リード）
- 089: wtrclred。成果物だけを見て専門職の「不要」を断じる風潮に対し、判断・責任・リスク回避という仕事の本質の価値を説く
- 233: ESLint。AI生成PR・Issueの急増と「人間が作ったものか」の判別コストを理由に、5年続いた外部貢献者報酬制度（Contributor Pool、累計5.1万ドル超）を終了
- 116: slopmanifesto。AI生成物を無責任に公開・利用する「AIスロップ」を拒絶し、人間の理解・意図・責任を再定義する開発者向け宣言
- 154: 文春。言語脳科学者・酒井邦嘉東大教授が、脳発達・思考力への影響を理由に青少年のAI使用の全面禁止を提言
- 補足: 047（wake me up when AI can…）・113（Open Source Says No）・208（Life on Claude Nine）も同系統だが Supabase annex pre-flag のため annex 維持。主に入れたい場合は要相談。

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週はAnthropicが新フラッグシップ「Claude Fable 5.2」と専門組織向け「Mythos 5.2」を発表し、同じ週にGoogleも次世代モデル「Gemini 4」をCarbon（セキュリティ・科学的推論特化）とHydrogen（推論と速度を両立、エージェント/コーディング向け）の2構成で公開した一週間となった。1,000体規模のエージェントによるフェルマーの最終定理の形式化、DeepMindのAlphaProof CodeによるSignalプロトコルの数学的検証、PSIによる量子計算の未解決問題の証明、Claudeによるゲーデルのノート解読、DeepMindのAlphaGenome 2によるゲノム解釈の精度向上など、AIが数学・科学の最前線で具体的な成果を出す事例が集中した。AlphaProof Codeでは人間のレビューが全体のわずか1%に絞られるなど、専門的な検証作業をAIが肩代わりする構図が目立った。

一方で、文章を生成しない「判断特化型AI」が低コスト・高速の軸として台頭し（Vercel統計では全リクエストの26%）、セキュリティでは自律型ペンテストツールの急拡大と、エージェントによる先制防御・機密漏洩が同じ基盤の上で進んだ。Webとデザインの領域では、A2UIやUI SDK、WebMCPが「エージェント対応」の標準を定義し、デザイナーの価値がクラフトと審美眼へ再定義されつつある。Googleは次世代モデルGemini 4をCarbonとHydrogenの2構成で公開し、両者を動的に連携させるOrchestratorを備えたエージェント開発環境Antigravityを更新した。

市場面では、AnthropicがNasdaq上場（ティッカーANT）に向けて財務とロードショーを開示し、アモデイCEOの「10年以内にがん克服」発言への懐疑と合わせて、AI企業の期待値が可視化された。同時に、生成AI批判やESLintの貢献者報酬制度の終了、青少年のAI使用禁止提言といった人間中心の抵抗も具体化している。なお、NVIDIAの循環取引疑惑やUbieの内製エージェント基盤といった話題は、今回アネックス候補として別途扱う。

**Key Points to Cover:**
1. Claude Fable 5.2 / Mythos 5.2 の発表と、AIによる数学・科学の具体的成果
2. Gemini 4（Carbon/Hydrogen）とAntigravity — Googleの次世代モデルとエージェント実行基盤
3. 判断特化型AIの台頭と、AIセキュリティの攻防・漏洩
4. AIとともにデザインする — エージェント対応UIとデザイナー価値の再定義
5. AnthropicのNasdaq上場（ANT）と、生成AIへの人間中心の抵抗

---

## Curation Signal Summary

**⭐ Standout Articles — moved to annex per human direction (Rev.1):**
- 137 (Ubie Remoco/Uvin) → annex candidates. Default guidance anchors a main theme on the standout; this cycle the human directed its theme (former Theme 9) to annex, so 137 is not in main.

**👎 Downvoted Articles (not used as leads/drivers):**
- 056 → 候補外（Gemini→Claude移行体験、個人記録）
- 125 → 候補外（AI Model Chronicle、まとめ記事）
- 127 → 候補外（yomiyasu更新比較、ツール個別レビュー）
- 247 → 候補外（gizmodo Fable 5.2 一般向け反応）

**Supabase Annex Pre-flags (16) — all kept OUT of main:**
- 047, 050, 063, 071, 087, 113, 148, 160, 171, 172, 186, 191, 202, 208, 217, 238 → none placed in main. Closest-to-their-theme candidates: 238 (tak-dcxi「Agent Ready」→ Theme 6), 191 (Shopify Cyber Chaos Monkey → Theme 5); both promotable on request.
- Note: 011 (Theme 6) と 232 (Theme 5) は human annex flag ではなく AI annexPotential スコアが高いだけなので主に配置した。

**Omitted Articles:** none flagged for omission.

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 39 articles across 8 themes (inside the ~30–40 / 6–9 spec)
- Annex Journal: remaining ~210 summaries triaged in STEP_04/05 (annex pre-flags + unique perspectives)

**Article Count by Theme (Planned):**
- Theme 1 (Fable/Mythos 5.2 発表): 4
- Theme 2 (Gemini 4 Carbon/Hydrogen・Antigravity): 5
- Theme 3 (数学・科学でのAI活用): 5
- Theme 4 (判断特化型AI): 4
- Theme 5 (AIセキュリティ攻防・漏洩): 5
- Theme 6 (AIとともにデザインする): 8
- Theme 7 (Anthropic IPO): 3
- Theme 8 (生成AIへの抵抗・人間中心): 5

**Total Planned for Main:** 39 articles
**Remaining for Annex/Omit:** 210 summaries

**Strong annex clusters that could be promoted to main (noted for the human, as in prior cycles):**
- 内製エージェント基盤・ハーネス (Rev.1でmainから移動): 137 ⭐ (Ubie Remoco/Uvin), 079 (OSSハーネス5事例), 146 (Claude Code harness deep dive), 064 (Switchboard 2か月1,300PR) — 再昇格を望む場合は要相談
- AI市場・バブル (Rev.1でmainから移動): 121 (NVIDIA循環取引/WSJ), 224 (HN AI crash/Economist), 025 (OpenAI 1.25兆ドル), 016 (AI株 vs 過去暴落)
- Gemini 4 Carbon/Hydrogen・Antigravity: **Rev.2でmain（Theme 2）へ昇格（045/159/219/220/167）。** 残る 166 (npaka rehash)・241 (Pathways)・242 (MaxText)・243 (AI Studio×Maps) はannex候補のまま
- ローカル・オープンウェイトモデル: 092 (Ripple-65B), 140 (Kimi-K3.1-Pro), 018 (Arete-27B), 174 (llama.cpp v1.0), 102 (PLaMo 3 Translate), 120 (Qwen3.8), 157 (Claris Harbor), 093 (ソフトウェア産業消滅論)
- AI導入の現実・生産性のギャップ: 212 (shipping faster?), 169 (ActivTrak 労働時間+90分), 188 (unintended consequences), 236 (JetBrains 9事例), 145 (PwC AI店長), 189 (Sentry Slopware Factory)
- MCPエコシステム: 084, 186, 187, 190, 177, 249, 085
- Muse / パーソナルAI・新機能: 070/091/151/245 (Muse), 115 (Claude Meetings), 149 (Whiteboards/Sheets/Data), 122 (Projects), 099 (Zyphra MAIA), 168 (Memoket Gem)

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-11-17 (Rev.1) ／ 2026-11-18 (Rev.2)
**Reviewer:** beijaflor (via human-review-gate AskUserQuestion)

**Changes Made (Rev.1):**
- Merged former Themes 5 & 6 into one "AIとともにデザインする" theme (Theme 5, 8 articles)
- Narrowed former Theme 7 to focus on the Anthropic IPO (Theme 6): promoted 044 (roadshow) + 109 (Amodei backlash); moved 121/224/025/016 to annex candidates
- Moved former Theme 9 (Ubie/harness: 137/079/146/064) to annex candidates — ⭐137 standout out of main per human decision

**Changes Made (Rev.2):**
- Promoted Gemini 4 (Carbon/Hydrogen) + Antigravity from annex candidates to a new main **Theme 2** (5 articles: 045/159/219/220/167), inserted after Theme 1 (Fable 5.2)
- Renumbered former Themes 2–7 → Themes 3–8
- Main scope 7 themes / 34 → **8 themes / 39**; annex remainder 215 → 210
- Left thin 166 and infra/feature pieces 241/242/243 in annex candidates
- Updated highlight draft, Key Points, count table, and the annex-cluster list to match

**Approval:** Rev.1 ✅ APPROVED ／ Rev.2 ✅ APPROVED

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES (STEP_07)

> Patterns from `patterns/assembly/`. **Article order = the editorial-priority order in `curated_journal_sources.md`** (the STEP_08 writers receive that order; no reorder is introduced here). Transitions are grounded in the actual article bodies (`unified_summaries_main.md`) — no invented connections; articles presented as-is. The STEP_08 writers run in parallel and cannot see each other's sections, so shared facts are assigned a single owning section below.

**Cross-theme fact ownership (parallel writers can't see each other):**
- **フェルマーの最終定理の形式化** → owned by **Theme 3 / 144** (full account: 1,000体、自作SQL階層、Langlands-Tunnell、トークン1/3; precise figure **28.7時間**). Theme 1 / 033 mentions it only as a one-line Fable launch highlight and does **not** state a conflicting hour figure (033 rounds to「30時間」).
- **AlphaProof Code（Signal実装の深層形式検証）** → owned by **Theme 3 / 042** (Gemini Carbon、600万行Lean、人間レビュー1%、数年→4週間). Theme 2 / 045 mentions it only as a one-line Carbon science result.
- **サイバーセキュリティ特化モデル** → each stays in its own theme: Mythos 5.2 (T1/033, 一行「専門組織向け」), Gemini 4 Carbon (T2/045, Carbonの一能力), GPT-6 Cyber (T5/072, 専用テーマで詳述). No cross-theme model comparison.

---

### Theme 1: Claude Fable 5.2・Mythos 5.2 発表、Artificial Analysis首位評価と高コスト・プロンプト設計の実際

**Pattern:** Single-Focus
**Pattern Rationale:** Fable 5.2 / Mythos 5.2 の公式発表(033)という単一イベントに、第三者評価(035)・公式ガイド(103)・実務者の読み解き(134)が反応として連なる。明確なリードと階層がある。

**Article Order & Roles:**
1. 033 — Lead（何が出たか）: 公式発表。フェルマー等は一行の見出しのみ（詳細は Theme 3/144、時間数は述べない）
2. 035 — 批判的評価（so-what）: 知能ベンチ1位だが入力$8/出力$40・推論平均44分という高コスト低速の第三者評価
3. 103 — 公式 how-to（now-what）: エフォート5段階・コード所有権・Finish work・旧モデル向け指示の削除
4. 134 — 実務者の読み解き: 103 を読み、effort 挙動・コード所有権・新拒否カテゴリ(frontier_llm 等)を整理。「性能値より使い心地が選択基準に」で締め

**Narrative Arc:** 発表（何ができるか）→ 第三者評価が突きつけるコスト・速度の現実 → 公式＋実務のプロンプト設計で「超高性能モデルの使い所」に着地。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 033 → 035 | 「この飛躍的な性能を第三者はどう測ったか」→ Artificial Analysis の定量評価へ |
| 035 → 103 | 「高コスト・低速というトレードオフを踏まえ、どう使いこなすか」→ 公式ガイドへ |
| 103 → 134 | 「公式の指針を実務者はどう読んだか」→ effort・コード所有権の実感と展望へ |

**Emphasis Balance:** Technical High / Business Medium / Future Medium

**Key Synthesis Points:**
- ベンチ1位と高コスト低速は同じ記事(035)が示す表裏——「使い所を選ぶモデル」である
- 103/134 が共通して挙げる「コード所有権」「effort 調整」が、超高性能モデルを実務に載せる具体策
- 134 の「性能値より使い心地」が、035 の高コスト低速への実務的回答になっている

**Conclusion Approach:** 絶対性能の頂点と、それを日常ワークフローに載せる難しさを並置。選定基準が「賢さ」から「使い心地（速度・指示追従）」へ移るという 134 の観測で締める。

**Assembly Prompts for STEP_08:**
1. Fable 5.2 は何を達成し、何を代償にしたか
2. 第三者評価と公式/実務ガイドを束ねると、どんな「使い所」像が立つか
3. 実務者は明日どう設定を変えるか
4. モデル選定基準はどこへ向かうか

---

### Theme 2: Gemini 4 Carbon・Hydrogen・Antigravityが示すGoogleの次世代モデルとエージェント基盤

**Pattern:** Single-Focus（Multi-Event variation）
**Pattern Rationale:** 単一の発表元(Google)による複数の関連リリース——Carbon(045)と Hydrogen(159/219)という2モデル、それらが動く Antigravity(220/167)——が一つの Gemini 4 ローンチ物語を作る。外部の反応記事がない一次情報中心なので、締めは「意義の一般化」ではなく**出荷された具体（仕様・価格・提供範囲）**に置く。

**Article Order & Roles:**
1. 045 Carbon — Lead: フラッグシップ。先行 Argon を凌駕、セキュリティ/エージェント/科学推論特化、$2/$10、/swarm。Signal証明(AlphaProof)は一行のみ（詳細 Theme 3/042）
2. 159 Hydrogen — 第2の柱: 推論と速度を橋渡し、3.8 Flash比2.5倍、$1.50/$7.50、4段階 Thinking Levels。Orchestrator は一行（詳細 220）
3. 219 Hydrogen API詳細 — **OWNS**: 1M統合コンテキスト、新「xhigh」思考レベル、ハルシネーション5倍減、Managed Agents デフォルト
4. 220 Antigravity — **OWNS Orchestrator**: Carbon↔Hydrogen 動的切替、成功率維持で速度+19%/クォータ-24%
5. 167 Antigravity remote — **OWNS**: リモートエージェント（PCオフラインでもクラウドVM継続、スマホ承認）。第三者(Publickey)視点

**Narrative Arc:** フラッグシップ Carbon → 速度と推論を橋渡しする Hydrogen（と API 上の新機能）→ 両モデルを動的に束ねる Antigravity(Orchestrator) → PC を切っても続くリモートエージェント。モデルから実行基盤へ。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 045 → 159 | 「最上位 Carbon に対し、日常タスクには速度が要る」→ Hydrogen へ |
| 159 → 219 | 「開発者から見た Hydrogen の新機能」→ AI Studio/API の詳細へ |
| 219 → 220 | 「この Carbon と Hydrogen をどう使い分けるか」→ Antigravity Orchestrator の動的連携へ |
| 220 → 167 | 「エージェントの実行場所自体も変わる」→ クラウドで継続するリモートエージェントへ |

**Emphasis Balance:** Technical High / Business Medium / Future Low

**Key Synthesis Points:**
- Carbon(推論)と Hydrogen(速度)を、Orchestrator(220)がタスク進行に応じて動的に切り替える
- 219 は1Mコンテキスト・xhigh・ハルシネーション5倍減、220 は速度+19%/クォータ-24% を、それぞれ個別仕様として報告
- 167 は Antigravity のリモートエージェント機能（PCオフラインでもクラウドVMで継続）——モデルでなく実行環境側の更新

**Conclusion Approach:** 意義の一般化や競合比較の煽りを避け、出荷された具体——Carbon/Hydrogen の価格、1Mコンテキスト、Orchestrator の +19%/-24%、リモートエージェントの提供範囲(AI Pro/Ultra)——を並べて締める。

**Assembly Prompts for STEP_08:**
1. Gemini 4 は「何を」出荷したか（2モデル＋基盤）
2. Carbon と Hydrogen の役割分担を Orchestrator はどう自動化するか
3. 読者（Google AI Pro/Ultra 利用者）が今使えるものは何か
4. （一般化した将来予測はせず、事実で締める）

---

### Theme 3: Claude Fable・AlphaProof Code・PSIが示す形式証明・未解決問題・ゲノムでのAI活用

**Pattern:** Multi-Perspective
**Pattern Rationale:** 数学・科学の最前線で並行して起きた5つの独立成果。相互の優劣・依存はなく、領域の広がり（形式証明/コード検証/計算量理論/数学史/ゲノム）を並置することに価値がある。

**Article Order & Roles:**
1. 144 Fermat — **OWNS** フェルマー形式化の全貌: Fable 5.2、1,000体、**28.7時間**、自作SQL階層、Langlands-Tunnell、トークン1/3
2. 042 AlphaProof — **OWNS**: Gemini Carbon、Signal実装の深層形式検証、600万行 Lean、人間レビュー1%、数年→4週間
3. 097 PSI — Aaronson-Ambainis予想(2008〜)の証明、非公開 Anthropic モデル、Lean 検証
4. 119 Gödel — Claude がゲーデルの未公開ノート(ガーベルスベルガー式)を解読、663定理（約400を Coq 確認）、選択公理独立性の先取り
5. 156 AlphaGenome 2 — 1.07億細胞プロファイル、細胞タイプ別 DNA 変異影響を従来2倍精度

**Narrative Arc:** 形式証明（144 Fermat / 042 Signal / 097 量子予想）→ 数学史の再発見（119 Gödel）→ 生命科学（156 genome）。「AIが専門的検証・発見を肩代わりする」広がり。共通項: 144/042/097 はいずれも Lean で検証される。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 144 → 042 | 数学の証明に続き、ソフトウェア実装の形式検証へ（ともに Lean 検証） |
| 042 → 097 | 実装の検証に続き、未解決の理論問題の証明へ（同じく Lean 検証） |
| 097 → 119 | 新しい証明に続き、過去の未公開ノートの解読へ |
| 119 → 156 | 「数学から生命科学へ」→ ゲノム解釈の精度向上へ |

**Emphasis Balance:** Technical High / Business Low / Future Medium

**Key Synthesis Points:**
- 144/042/097 がいずれも Lean で形式検証——「AIの発見を厳密に検証できる」点が共通の信頼基盤
- 042 では人間の役割が「仕様策定と1%のレビュー」に凝縮する
- 119 と 156 は、生成（新証明）だけでなく解釈・予測（過去ノート・DNA）にも及ぶ広がりを示す

**Conclusion Approach:** 144/042/097 は形式検証を伴う証明、119 は過去の成果を数日で解読、156 は予測精度を倍増——5領域の並置が示すのは、AIが専門的な検証・発見・予測を大きく肩代わりする段階に入ったこと。多様な視点が一つの結論を補強する。

**Assembly Prompts for STEP_08:**
1. これら5つに共通する「AIができるようになったこと」は何か
2. Lean/Coq による形式検証が果たす役割は
3. 人間に残る役割（仕様・レビュー）はどう変わるか
4. 生成と解釈・予測の双方に及ぶ含意は

---

### Theme 4: OpenAI Decisions・Gemini Decisions・Perplexity Deciderが広げる「判断特化型AI」

**Pattern:** Single-Focus
**Pattern Rationale:** 「判断特化型AI」という単一トレンドを、俯瞰記事(248)がリードし、個別プロダクト(213/114)と市場データ(008)が裏づける。248 に明確な俯瞰の権威。

**Article Order & Roles:**
1. 248 — Lead/俯瞰: 判断特化型AIとは何か。TypeSafe Jev($870M)、OpenAI Decisions(GPT-6 Luna・10倍高速)、Cloudflare/Databricks/AWS、処理費88%減・応答40倍
2. 213 Gemini Decisions API — 1推論で最大1,000判定、150-250ms、出力トークン無料、約5倍コスト効率
3. 114 Perplexity Decider v1.3 — 双方向アテンション、locate 抽出、Qwen 27B 蒸留、HF Apache 公開
4. 008 Vercel統計 — Payoff/市場証拠: 決定モデルが全リクエスト26%、コスト1/70、新規チーム Anthropic 2:1、モデル半減期6週間

**Narrative Arc:** 「文章を生成しないAI」とは何か(248) → 具体プロダクト2つ(213 Google / 114 Perplexity) → 市場で既に26%という実証(008)。概念→実装→市場。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 248 → 213 | 「この判断特化という考え方を各社はどう製品化したか」→ Gemini Decisions へ |
| 213 → 114 | 「同じく逐次生成しない設計を、Perplexity は蒸留と抽出機能で」→ Decider へ |
| 114 → 008 | 「では市場はどう動いたか」→ 全リクエスト26%という Vercel 統計へ |

**Emphasis Balance:** Technical Medium / Business High / Future Medium

**Key Synthesis Points:**
- 213 も 114 も「トークンを逐次生成せず1回のフォワードパスでスコアリング」という同じアーキテクチャ思想——低レイテンシ・低コストの源
- 248 の事例(88%減/40倍)と 008 の市場データ(26%/コスト1/70)が、トレンドの実在を定量裏づけ
- 汎用LLMと判断特化型の「使い分け」がエージェント制御の標準になりつつある

**Conclusion Approach:** 判断特化型は実験でなく既に市場の約1/4を占める実運用層。生成と判断の使い分けが設計の前提になった、と締める。

**Assembly Prompts for STEP_08:**
1. 判断特化型AIとは何で、なぜ今か
2. 各製品に共通する設計思想は
3. 市場データ(008)は何を証明するか
4. 設計者は何を使い分けるべきか

---

### Theme 5: ARTEX以外の45ツール・GPT-6 Cyber・1Password Proverが示すAIセキュリティの攻防と機密漏洩

**Pattern:** Multi-Perspective
**Pattern Rationale:** AIがセキュリティの攻防を組み替える局面を、攻撃ツール調査(153)・防御モデル(232)・攻防両用モデル(072)・エージェント検証(244)・漏洩の実態(022)という複数の facet から描く。単一の権威も二項対立もなく、同じ地殻変動の各面。

**Article Order & Roles:**
1. 153 GitGuardian — 攻撃側ランドスケープ: ARTEX以外45フレームワーク、秘密情報スキャナ、Shodan 1,400件露出
2. 232 Cloudflare — 防御側全体像: 攻撃30倍急増、モダンセキュリティモデル6本柱、ID中心防御
3. 072 GPT-6 Cyber — 攻防両用モデル: ExploitGym 48.5%、Firefox 81件・Linux 948エクスプロイト、範囲遵守100%、Daybreak
4. 244 1Password Prover — エージェント防御: SAGE に Prover 追加、誤検知86中85抑制・真の脆弱性100%保持
5. 022 Apiiro — 漏洩の実態（底流）: Claude Code が `.claude/settings.local.json` に機密保存→GitHub露出2,539件、1.1%

**Narrative Arc:** 攻撃ツールの氾濫(153) → 防御側の再設計(232) → 攻撃能力とアライメントを両立する専用モデル(072) → コードレビューを巡回するエージェント防御(244) → その足元で起きている機密漏洩(022)。攻撃・防御・漏洩が同じ技術基盤上で同時進行。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 153 → 232 | 「氾濫する攻撃ツールに防御側はどう構えるか」→ モダンセキュリティモデルへ |
| 232 → 072 | 「攻撃能力そのものを、範囲遵守とともに提供する」→ GPT-6 Cyber へ |
| 072 → 244 | 「攻撃だけでなく、レビューを巡回するエージェント防御も」→ 1Password Prover へ |
| 244 → 022 | 「高度な攻防の足元で、基本的な機密漏洩が起きている」→ Apiiro の実態調査へ |

**Emphasis Balance:** Technical High / Business Medium / Future Medium

**Key Synthesis Points:**
- 232 は攻撃が「推論速度で並列にエクスプロイトを量産する」規模(30倍増)に達したと報告——153 はその担い手(45フレームワーク)を、072 はそうした能力を持つ専用モデルを示す
- 072 と 244 は対照的に「アライメント/ガードレール（範囲遵守・読み取り専用サンドボックス）」で危険な能力を飼い慣らす
- 攻防が高度化する一方(022)、漏洩の原因はエージェントの設定ファイルという地味な運用——高度な脅威と基本的衛生が同居

**Conclusion Approach:** 攻撃・防御・漏洩が同じエージェント技術の上で同時に進む。封じ込め前提のID中心防御(232)と能力を縛るアライメント(072/244)が鍵だが、足元の設定衛生(022)を欠けば崩れる、と締める。

**Assembly Prompts for STEP_08:**
1. AIはセキュリティの何を変えたか
2. 攻撃・防御・漏洩はどう連関するか
3. アライメント/ガードレールは何を守るか
4. 読者が明日見直すべき運用は（`settings.local.json` 等）

---

### Theme 6: デザイナーの価値・デザインシステムAIレディネス・A2UI/UI SDKが問い直すAIとともにデザインする役割とツール

**Pattern:** Progressive-Sequence（hybrid — 各半内は peers、034 を境に scope shift）
**Pattern Rationale:** 前半(010/013/201/198＝デザイナーの価値と作り方)→ 034(橋渡し)→ 後半(124/180/011＝エージェントがUIを作り操作する標準)へと、焦点が「人間デザイナーの価値」から「エージェント・ネイティブUI」へ移る scope progression。ただし各半の記事は相互依存せず peers なので、半内は「別の角度から」でつなぎ、半をまたぐ 034 でのみ「ここで前提が変わる」と明示する。

**Article Order & Roles:**
1. 010 — Foundation: AIがデザインを凌駕する中でデザイナーに残る8要件（クラフト/審美眼/ビジネス等）
2. 013 — デザインシステムの「AIレディネス」＝暗黙知と人間の品質保証の定義（機械可読化ではない）
3. 201 — 実践: MCP＋マニフェストで「本物のコード」プロトタイプ（shadcn 模倣の壁を越える）
4. 198 — AIを「新しい古いデザイン素材」として直接扱う（同一プロンプト50回で最悪ケースを見る）
5. 034 — **Pivot/橋渡し**: 「UIの時代は終わった」人間操作→エージェント代理消費へ
6. 124 — Vercel UI SDK: behavior と Agent Bridge でエージェントが生成・直接操作
7. 180 — A2UI 1.0: エージェントがネイティブUIを描画するオープンプロトコル
8. 011 — WebMCP（Payoff）: ブラウザのエージェントがページ機能を直接呼ぶ（「見る」から「機能を呼ぶ」へ）

**Narrative Arc:** 前半＝AIが生産性を上げる中で「デザイナーの価値(010/013)」と「AIとの作り方(201/198)」を問い直す。034 で視点が反転——人間が操作する前提そのものが終わる。後半＝エージェントがUIを生成・操作する標準(124/180/011)。人間中心の設計からエージェント・ネイティブな設計へ。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 010 → 013 | 「デザイナー個人の力に続き、デザインシステム側のAI対応とは」（別角度・peers） |
| 013 → 201 | 「“AIレディ”を実装に落とすと」MCP＋マニフェストの実践へ（別角度・peers） |
| 201 → 198 | 「AIを模倣対象でなく“素材”として直接扱うと」（別角度・peers） |
| 198 → 034 | ここまでは人間がAIと設計する話。034 で視点が変わる——AIエージェントが利用者になる側へ（scope shift） |
| 034 → 124 | 「エージェントが使う側になるなら、UIはどう作るか」→ UI SDK へ |
| 124 → 180 | 「同じエージェント・ネイティブUIを、プラットフォーム横断の標準に」→ A2UI へ |
| 180 → 011 | 「“描画”の次は、ページ機能の直接呼び出し」→ WebMCP へ |

**Emphasis Balance:** Technical Medium / Business Medium / Future High

**Key Synthesis Points:**
- 前半は「デザイナーに残る価値」、後半は「エージェントがUIを作る標準」——034 を境に「誰のためのUIか」の焦点が移る（因果の積み上げではない）
- 013 の暗黙知/人間の品質保証、124/180/011 のエージェント操作は、「人間はどこで品質を担保するか」という同じ問いの別フェーズ
- 124(Agent Bridge)/180(A2UI双方向)/011(WebMCP) はいずれも「エージェントが画面解析でなく機能を直接呼ぶ」——同じ転換の3標準

**Conclusion Approach:** UIが「人間が操作する画面」から「エージェントが呼ぶ機能」へ移る大きな流れの中で、デザイナーの価値は審美眼・暗黙知・品質保証の設計に残る、と締める（前半と後半は同じ流れの別フェーズであり、一方が他方の帰結だとは描かない）。

**STEP_08 note:** 相互依存の無い peers を「〜を発展させ」等でつながないこと（偽の積み上げ回避）。半内は並置、034 でのみ転換を明示。

**Assembly Prompts for STEP_08:**
1. AI時代にデザイナーに残る価値は（前半）
2. エージェント・ネイティブUIの標準は何を変えるか（後半）
3. 034 の反転点は何を意味するか
4. 人間はどこで品質を担保し続けるか

---

### Theme 7: Anthropicのプロスペクタス・ロードショー・アモデイ発言が映すNasdaq上場（ANT）の実像と懐疑

**Pattern:** Single-Focus
**Pattern Rationale:** Anthropic の Nasdaq 上場(ANT)という単一イベントを、一次情報(214 プロスペクタス / 044 ロードショー)がリードし、懐疑(109 アモデイ発言批判)が contrarian view として締める。

**Article Order & Roles:**
1. 214 — Lead/一次: プロスペクタス。170億ドル収益、前年比12倍超、11,900社、楽天/Salesforce等、11/19取引開始
2. 044 — 一次: ロードショー。70-78ドル×約8.25億株、Goldman/Morgan Stanley 主幹事、S-1段階
3. 109 — Contrarian: アモデイの「10年以内にがん克服」に医学界が誇大広告と批判。時価総額1兆ドル狙い

**Narrative Arc:** 財務と条件の開示(214/044) → その期待値への懐疑(109)。数字が示す実像と、IPOを意識した誇大広告への批判を並置。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 214 → 044 | 「開示された財務に続き、具体的な売出条件は」→ ロードショーへ |
| 044 → 109 | 「しかしロードショーでの発言には批判も」→ アモデイのがん発言へ |

**Emphasis Balance:** Technical Low / Business High / Future Medium

**Key Synthesis Points:**
- 214 の12倍成長・11,900社という実数と、109 の「1兆ドル・がん克服」という物語は、同じIPOの two faces——実績と期待煽り
- 109 はアモデイがリスク強調から「奇跡の時代」強調へ転じた点を指摘——上場が語り口を変える

**Conclusion Approach:** 勝者を決めず、開示された数字(実像)とロードショーの誇大広告(懐疑)の緊張を示して締める。読者は実績と期待のどちらに重きを置くかを問われる。

**Assembly Prompts for STEP_08:**
1. 214/044 は何を開示したか
2. 109 の懐疑は何を突くか
3. 実績と期待のギャップはどこか
4. 読者はこのIPOをどう読むべきか

---

### Theme 8: 酒井邦嘉・ESLint・No AI Slopが示す生成AIへの抵抗と人間中心の視点

**Pattern:** Multi-Perspective
**Pattern Rationale:** 生成AIへの抵抗・人間中心の視点を、思想的批判(030)・専門職擁護(089)・制度(233)・運動/宣言(116)・教育脳科学(154)という複数ドメインの peers として並置。単一の権威も二項対立もなく、各面で抵抗が具体化している範囲を見せる。

**Article Order & Roles:**
1. 030 — Foundation/思想: 生成AIを技術/環境/認識論/政治から包括批判（統計モデル、環境負荷、TESCREAL）
2. 089 — 専門職擁護: 成果物だけで「不要」と断じる風潮に、判断・責任・リスク回避という仕事の本質で反論
3. 233 — 制度: ESLint が AI生成PR増を理由に貢献者報酬制度(累計$51k)を終了
4. 116 — 運動/宣言: No AI Slop マニフェスト、5つの価値、「生成は安価・レビューは高価」の非対称
5. 154 — 教育/脳科学: 酒井教授、青少年のAI使用全面禁止を提言（文法中枢の発達阻害）

**Narrative Arc:** 思想的な全体批判(030) → 専門職の価値擁護(089) → 制度の実際の変更(233) → 開発者の集団的宣言(116) → 教育・脳科学からの警告(154)。個人の思想から制度・運動・教育へ、抵抗が各ドメインで具体化。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 030 → 089 | 「技術そのものへの批判に続き、“専門職不要論”への反論」（別角度・peers） |
| 089 → 233 | 「個人の主張を超え、制度が実際に変わった例」→ ESLint へ |
| 233 → 116 | 制度の変化に続き、開発者コミュニティ自身の規範宣言へ（別の事例） |
| 116 → 154 | 「現場・制度に続き、教育・脳科学からの警告」→ 酒井教授へ |

**Emphasis Balance:** Technical Low / Business Low / Societal High

**Key Synthesis Points:**
- 089/116/154 に共通するのは「人間の判断・理解・責任」を価値の中心に置く点——抵抗の芯は反テクノロジーでなく人間中心
- 116 の「生成は安価・レビューは高価」という非対称は、233（判別コスト増で ESLint が撤退）と同じ構造を別角度から示す
- 030 のマクロ批判から 154 の脳発達というミクロまで、抵抗が複層で具体化

**Conclusion Approach:** 多様な抵抗が示すのは、反AIというより「人間の判断・責任・思考をどこで守るか」という共通の問い。現場・制度・教育の各面で、その線引きが始まっている、と締める。

**Assembly Prompts for STEP_08:**
1. 各抵抗に共通する価値は何か
2. 制度(233)と宣言(116)の非対称構造の一致は
3. 反テクノロジーと人間中心はどう違うか
4. 読者は自分の現場でどこに線を引くか

---

### Annex（カタログ）Assembly

**Format（EDITOR_PERSONALITY カタログモード）:** 1件80-120語の統合ナラティブ。「読むべきか？」に答える decision-focused。批評的要点は地の文に織り込む（別建ての「なぜ重要か」等は作らない）。英語記事は原題を併記。カテゴリは非自明な文脈を足すときだけ。独自・論争的な角度は末尾で前景化。

**Sections（8 — curator's organisation in `curated_annex_selected.md`）:**
1. 内製エージェント基盤・開発ハーネス (137/079/071)
2. ローカル・オープンウェイト／オンデバイスAI (092/140/018/174/102/157/087)
3. AI導入の現実・生産性のギャップ (212/169/188/236/145/189)
4. Gemini 4 周辺（解説・学習基盤） (166/241) — 承認済の改称（旧「…main Theme 2 非収録分」）
5. MCPエコシステム (084/186/187)
6. エージェント対応Web・UI（agent-ready） (238/202/160)
7. 論考・研究・その他（独立トピック） (047/050/113/148/171/172/217/191)
8. その他の実践・論考 (218/020/086/176/098/090/207/230/075) — 承認済の改称（旧「全非掲載スイープ…」）

**Note:** 160(main 124 と近接)・166(main Theme 2 と近接) は curator 判断で annex 採用。カタログ文では main を繰り返さず annex 独自の角度を前景化（160＝フレームワーク非依存の behavior ライブラリ実装、166＝npaka 解説の入門視点）。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes (8 main + annex)
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

> The agent leaves `ASSEMBLY PLAN APPROVED` **unchecked**; it is flipped to `[x]` only after the human approves through the `human-review-gate` skill (AskUserQuestion). The STEP_03b approval `[x] APPROVED - Ready for STEP_04 curation` above still stands and is unaffected.

**Pattern distribution:** Single-Focus ×4 (T1/T2/T4/T7) ・ Multi-Perspective ×3 (T3/T5/T8) ・ Progressive-Sequence ×1 (T6). No Debate-Contrast (no main theme has two opposing camps).

**Approval Date:** 2026-11-19
**Approver:** beijaflor
