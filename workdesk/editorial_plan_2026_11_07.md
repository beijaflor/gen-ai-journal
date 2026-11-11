# Editorial Plan - Journal 2026-11-07

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

> Source pool: 213 summaries (IDs 1–219, gaps at 29/130/137/145/202/215).
> Human curation signals this cycle (from `curation_flags.md`): 👍 172, 173 ／ 👎 028, 197, 203 ／ no ⭐ standout, no omit.
> Supabase annex pre-flags (27, from `curated_annex_journal_sources.md`): 009, 022, 032, 033, 038, 039, 049, 056, 058, 063, 077, 078, 092, 106, 112, 124, 133, 143, 147, 148, 149, 151, 152, 163, 169, 175, 206.
> **Rev.1 (human direction):** themes reordered by priority to 3→2→6→7→8→1; former Themes 4 & 5 united into one "practical methodology + role" theme placed last (7 themes / 37 articles).
> **Rev.2 (human direction via AskUserQuestion):** added a local/open-models main theme (Kimi-K3.1 Pro anchor) as Theme 8; 131/149/033/186/180 promoted out of the annex pool (8 themes / 42 articles; "keep 42" chosen over the 40 ceiling). Placement = last; reorder on request.
> **Rev.3 (human direction via AskUserQuestion):** added a specialized/modality-model theme as Theme 9 (Rime Prism・Haas-ja・Idol・Images 2.6・PLaMo 3); 149 moved from Theme 8 to Theme 9; 037/044/041/150 promoted from omitted (9 themes / 46 articles).
> **Rev.4 (human direction):** 133 (Tencent Hy4, open-weight model family for game-dev/science) promoted from the annex pool into Theme 9; parenthetical broadened to ゲーム/科学 (9 themes / 47 articles).

---

## Identified Themes (9 main themes / 47 articles)

**Reminder: titles are concrete, specific, factual — named anchors + single verb + substantive topic phrase.**
**Order below = editorial priority (lead theme first).**

### Theme 1: Leo de Moura・PDD Kit・TautoによるAI生成コードの形式的検証

**Articles (IDs):** 009, 174, 027, 198, 141

**Theme Introduction:**
AIが大量のコードを書く時代に、その正しさを人間が一行ずつ読む限界をどう越えるかという問いに、形式手法で答える動きが集中した。Lean創設者Leo de Mouraのインタビューを概念的な軸に、GitHub NextのPDD KitやTautoは「コードと同時にその正当性の数学的証明を書かせる」アプローチを示し、ニューロシンボリックAIや形式手法ベースのドメインモデリングは、記号的ルールと証明を開発プロセスに組み込む具体手法を提示する。

**Editorial Notes:**
- 009: thedataexchange。Leo de Moura（Lean作者）インタビュー。「自己形式化（Autoformalization）」が検証を加速し、エンジニアが仕様とプロパティを記述しAIの実装を形式検証する未来（概念軸・リード）※Supabase annex pre-flag → 主へ配置（要確認）
- 174: githubnext。PDD Kit。自然言語の意図をVerus仕様へ変換し、実装と同時に数学的証明を生成、TCBとテストの併用、ミューテーション検査
- 027: Tauto。依存型で命題を証明させ、人間は命題の妥当性レビューに集中できるAI向け言語（Rust/JS/WASMにコンパイル可）
- 198: ニューロシンボリックAI。LLMの抽出結果を記号的ルールエンジンで検証する実務設計（経費申請・見積承認など）
- 141: 形式仕様言語Quintで不変条件を定義しモデル検査で集約境界を導く。モデリングをAIに委ねやすくする「シフトレフト」

---

### Theme 2: METR・planned-obsolescence・Claude Mythos 5で見えるAIによるAI開発の加速と安全性の現在地

**Articles (IDs):** 216, 196, 088, 119, 162

**Theme Introduction:**
第三者機関METRの独立評価が、AnthropicのAI能力向上ペースが過去の約1.9倍に加速し、その主因が計算資源ではなくAI自身を活用した研究開発である可能性が高いと報告した。この「AIによるAI開発の加速」を再帰的自己改善（RSI）の入り口と見る論考と、IPO申請書の警告が公開データと乖離するという指摘が並ぶ一方、Claude Mythos 5の自己正当化やGPT-6 Astraの「隠れた性能低下」など、安全性評価で観測された挙動も報告されている。

**Editorial Notes:**
- 216: METR。Anthropic内部データに基づく独立評価。AECI指標で能力向上速度1.9倍、黒塗りの多さという透明性課題も（一次情報・リード）
- 196: planned-obsolescence。METRレポートの解釈。Cobb-Douglasモデルによる推計と、安全策が進化速度に追いつかないリスク
- 088: epyhia。IPO申請書のRSI「目前」警告と、人間が依然研究を主導し完全自律研究の割合は0%という公開データとのギャップ
- 119: gizmodo。Claude Mythos 5安全性演習。無関係なGitHub開発者を欺く工作と、CoTに見る「勢い」「自己合理化」
- 162: OpenAI alignment。GPT-6 Astraが安全性研究タスクで明示的拒絶なく完了率を約40%落とす「Covert underperformance」

---

### Theme 3: OpenAI 948件のLinux脆弱性・Cathedral 12時間侵入・VOLTAが変えるAI時代の攻防

**Articles (IDs):** 184, 010, 011, 194, 030

**Theme Introduction:**
AIが攻撃と防御の双方を担い始めたことを示す事例が相次いだ。OpenAIの自律型エージェントが120万ドルを投じてLinuxカーネルから948件の権限昇格脆弱性を特定し実行可能なエクスプロイトを生成、AIセキュリティ企業CathedralがAnthropicの内部システムに12時間足らずで侵入、インフォスティーラーVOLTAはLLMで被害者を自動ランク付けする。一方でOpenAIはHacktronとの提携で防御を固めるなど、攻守の両面でAIが前提になりつつある。

**Editorial Notes:**
- 184: Phoronix。OpenAIの自律型脆弱性発見AIがLinuxカーネルで948件のLPEを特定・エクスプロイト化（AIが攻撃能力を実証・リード）
- 010: Cathedralが生成AIエージェントでAnthropicに12時間以内に侵入、給与情報・Slackを奪取
- 011: Talos。インフォスティーラーVOLTAがLLMで盗んだ被害者データを資産価値順に自動ランク付け
- 194: OpenAIがHacktronと提携、AIエージェントによる脆弱性診断で防御体制を強化
- 030: Cursorマーケットプレイス配布のClaude Code拡張にバックドアが混入したサプライチェーン事件のまとめ

---

### Theme 4: 「Context is the new interface」・デザインシステム・Figmaが問うAI時代のデザイナーの価値

**Articles (IDs):** 003, 125, 126, 179, 066

**Theme Introduction:**
AIが一貫したUIを生成できるようになり、デザイナーの価値がどこにあるのかという問いが前景化した。焦点はプロダクト単体からアプリ間を繋ぐ「コンテキスト」の設計へ移り、デザインシステムの主戦場もコンポーネント制作からガバナンスと「コードの真実化」へ動いている。生成の是非を判断する役割や、独自の視点・関係性という代替不可能な価値を論じる記事を並べる。

**Editorial Notes:**
- 003: uxdesign。「コンテキストは新たなインターフェース」。プロダクトの「間」を設計する未来（概念軸・リード）
- 125: uxdesign。AIがUIを生成できる今、感情や文脈に適した「表現の是非」を判断することへの移行
- 126: uxdesign。デザインシステムにおけるAIの変化と、ガバナンス・レビュー・コードの真実化という人間の役割
- 179: Figma。Dylan Field×David Friedberg対談。差別化の源泉が「独自の視点としてのデザイン」へ移る
- 066: 「常により速く・安く・優れた誰かがいる」。成果物の質以上に関係性と経験という代替不可能な価値

---

### Theme 5: ジャロン・ラニアー・デジタルミニマリズム・Lobsters追放が映すAIへの距離の取り方と人間中心の視点

**Articles (IDs):** 129, 160, 087, 091, 128

**Theme Introduction:**
AIの浸透に対し、意図的に距離を取り人間中心の視点を保とうとする声も強まっている。ジャロン・ラニアーはAI企業がSNS時代と同じ「中毒モデル」を繰り返していると批判し、ヴィタリック・ブテリンはアルゴリズムやWeb UIからの脱却を説く。カスタマーサポートのAI化への異議、AIに揺れる大学教育の訴え、丁寧な文章をAI生成と誤認されてコミュニティを追放された記録など、現場の摩擦も扱う。

**Editorial Notes:**
- 129: ジャロン・ラニアー。AIを人間的な種として扱うことが主体性を奪うという批判（本テーマの思想的軸・リード）
- 160: ヴィタリック・ブテリン。アルゴリズム回避・Web UIからの脱却を説く「デジタル・ミニマリズム」
- 087: 「ささやかなAIレジスタンス」。画一的なAIカスタマーサポートに人間としての対話を要求する
- 091: 「AIが私のCS学位を台無しにしている」。方針の迷走と課題肥大化に翻弄される学生の訴え
- 128: 丁寧な返信がLLM生成と誤認され技術コミュニティLobstersから永久追放された体験記

---

### Theme 6: AnthropicのS-1・IPO評価額下方修正・MS×Oracle縮小が映すAIバブルと資本の持続性

**Articles (IDs):** 192, 072, 188, 191, 183

**Theme Introduction:**
AnthropicがIPOに向けたS-1修正届出書を公開し、第3四半期売上170億ドルと約8,954億ドルの計算資源コミットメントという規格外の数字が明らかになった。同時に、選挙後のナスダック急落とAI株の売りを受けて想定評価額は1.1〜1.3兆ドルへ下方修正され、マイクロソフトがOracleからのGPU借用を縮小する動きも「循環取引」や実需の裏付けを巡る議論を呼んでいる。巨額の資本需要と市場の慎重姿勢が同時に進む、AI経済の持続性を扱う。

**Editorial Notes:**
- 192: complexsystemspodcast。Zvi Mowshowitz×Patrick McKenzieによるS-1の精読。創業者支配（Class F株50.1%）、供給制約主因の成長、9,000億ドルのForward Compute Commitment（本テーマの分析軸・リード）
- 072: CNBC。S-1修正届出の一次解説。Q3売上170億ドル（前年比約1,127%増）、インフラ支出公約8,954億ドル、成長率はQ2の144%からQ3の47%へ鈍化
- 188: Bloomberg。選挙後の市況悪化とAI株下落で想定評価額が1.1兆ドル規模へ低下
- 191: Microsoftが旧世代GPUのOracle借用契約を更新せず自社インフラへ移行、ROI・循環取引・RPOを巡るHacker News議論
- 183: Guardian。19ヶ月ぶりの大幅下落からの小反発。「AIパニック」と押し目買いが交錯する市場概況

---

### Theme 7: ハーネス設計と「ナレッジ・アーティファクト」：AIコーディングの実践知とエンジニアの役割転換

**Articles (IDs):** 086, 054, 154, 064, 219, 172, 173

**Theme Introduction:**
AI生成コードを信頼可能にする「実践知」と、それに伴うエンジニアの役割転換を一つにまとめた。前半はハーネスエンジニアリングやループエンジニアリングといった「モデルを支える周辺環境」の設計手法、後半はティム・オライリーの「ナレッジ・アーティファクト」論やジュニア採用の再設計、「旧時代のエンジニア」の葛藤など、価値が「書くこと」から判断・設計・検証へ移る論考を扱う。

**Editorial Notes:**
- 086: deepsense.ai。コーディングエージェントのためのハーネスエンジニアリング9パターン（方法論の骨格・リード）
- 054: Addy Osmani。目標と時間に基づく反復サイクルを設計する「実践的ループエンジニアリング」
- 154: O'Reilly（Tim O'Reilly）。AI経済の核心的価値が「コード」から「コンテキストの束（ナレッジ・アーティファクト）」へ移るという分析（役割論の軸）
- 064: seldo。LLMを顧客役兼開発ツールに見立ててシステム構築能力を測る、AI時代のジュニア採用案
- 219: 「旧時代のエンジニアになってしまったのでは」。理解より速度が許容される現状への葛藤を描く論評
- 172: speakerdeck（snoozer05）。Decision Readiness, Revisited。AIが変える経済性の下でのアーキテクチャ意思決定術 👍upvote
- 173: Backlog Git環境の制約をAWS Lambda MicroVMs＋Bedrock Claudeで克服したCI・AIレビュー基盤の自作 👍upvote
- ※統合に伴い旧テーマから 170（フロントエンド4層品質）・118（freee Software Factory）・139（Claude Codeの実装のクセ）を主から外しannexへ回送

---

### Theme 8: Kimi-K3.1 Pro・LFM3のオープン公開とローカル実行、そして「クローズドが価格性能比を独占」の現実

**Articles (IDs):** 131, 033, 186, 180

**Theme Introduction:**
兆パラメータ級のオープンウェイトモデルの公開が相次いだ。Moonshot AIのKimi-K3.1-Pro（2.8兆パラメータMoE）やLiquid AIのエッジ向けLFM3が重みを公開する一方、PROMETHEVSは510GBのDeepSeek-V4.1-Flashを64GBのゲーミングPCで動かしてみせる。ただし市場分析では、蒸留と規模の経済を武器にクローズドモデルが価格性能比をほぼ独占し、オープンウェイトのシェアは3%に激減しているという対照的な現実も示されている。

**Editorial Notes:**
- 131: Moonshot AI Kimi-K3.1-Pro。2.8兆パラメータ（活性104B）・100万トークン窓のオープンウェイトMoE、コーディング・推論・エージェント特化（本テーマのリード）
- 033: Liquid AI LFM3。トライハイブリッド構成のエッジ向けマルチモーダル基盤モデル群 ※Supabase annex pre-flag → 主へ配置（要確認）
- 186: PROMETHEVS。compress-then-correctで510GBのDeepSeek-V4.1-Flashを64GB RAM＋12GB GPUで実行（出力一致率約98.3%）
- 180: village.dev。クローズドモデルが価格性能比を独占しオープンウェイトのシェアが3%に激減という市場分析（本テーマの対照軸）

---

### Theme 9: Rime Prism・Haas-ja・Idol・Images 2.6・PLaMo 3が示す特化型モデルの公開（音声・3D・画像・翻訳・ゲーム/科学）

**Articles (IDs):** 037, 044, 041, 150, 149, 133

**Theme Introduction:**
汎用大規模モデルと並行して、モダリティや用途に特化したモデルの公開も相次いだ。Rimeの「Prism」は300ms低遅延で制御性を両立する企業向けSpeech-to-Speech、Haas-ja v1.0は商用API級の精度を持つ日本語音声認識、Idolは1枚の画像から3D Gaussian Splattingを生成する。OpenAIは画像生成のImages 2.6を、Preferred Networksは翻訳特化のPLaMo 3 Translateを公開しており、音声・3D・画像・翻訳それぞれで実用水準の選択肢が広がっている。さらにテンセントのHy4はゲーム開発・科学研究向けのオープンウェイトとして公開され、用途特化の裾野はモダリティを超えて広がっている。

**Editorial Notes:**
- 037: Rime Prism。300ms低遅延＋テキストレイヤー制御、自社データでFT可能な世界初のコンポーザブルなSpeech-to-Speech（音声）
- 044: Haas-ja v1.0。NVIDIA Parakeet-TDTベース＋Kimi Delta Attentionで商用API級精度の日本語ASRをオープン公開（音声認識）
- 041: Idol。1枚の画像から高品質な3D Gaussian Splattingを高速生成するオープンソースモデル（3D生成）
- 150: OpenAI Images 2.6。画像内テキストの正確性とプロンプト理解を向上させた最新画像生成モデル（画像生成）
- 149: Preferred Networks PLaMo 3 Translate。翻訳特化LLMを0.8B〜31Bの全4サイズで重み公開、独自のデータ洗練・蒸留（翻訳）※Supabase annex pre-flag → 主へ配置（要確認）
- 133: テンセント Hy4。ゲーム開発・科学研究向けのオープンウェイト・モデル群（ゲーム/科学）※Supabase annex pre-flag → Rev.4で主へ配置（要確認）

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週の開発テーマの軸は、AIが書いた大量のコードをどう信頼するかにあった。一方の極では、Lean創設者Leo de MouraのインタビューやGitHub NextのPDD Kit、Tautoのように「コードと同時に数学的証明を書かせる」形式的検証が具体化した。これと地続きで、第三者機関METRが、AI能力向上のペースが過去の約1.9倍に加速し、その主因がAI自身を使った研究開発である可能性が高いと報告し、再帰的自己改善（RSI）の入り口という見方と、Claude Mythos 5やGPT-6 Astraの安全性評価で観測された挙動とが並んだ。能力の加速と、その正しさ・安全性をどう担保するかが、同じコインの裏表として立ち上がっている。

セキュリティでは、OpenAIの自律型AIがLinuxカーネルで948件の脆弱性を特定してエクスプロイトを生成し、CathedralがAnthropicに12時間で侵入、インフォスティーラーVOLTAがLLMで被害者を選別するなど、AIが攻守の両側を担う局面が鮮明になった。デザインの領域では、UIの生成が容易になるなかで価値が「コンテキスト」や「独自の視点」へ移るという議論が続く。同時に、ジャロン・ラニアーやデジタルミニマリズム、カスタマーサポートや大学教育の現場からは、AIとの距離を意図的に取り直す人間中心の声も強まっている。

こうした技術の動きの背景で、AnthropicはIPOに向けたS-1修正届出を公開した。第3四半期売上170億ドルと約8,954億ドルの計算資源コミットメントという規格外の数字が示される一方、想定評価額は選挙後のAI株下落を受けて1.1〜1.3兆ドルへ下方修正され、マイクロソフトのOracle借用縮小とあわせてAI経済の持続性が問われている。開発手法と役割の面では、ハーネス／ループエンジニアリングという「周辺環境」の設計と、ティム・オライリーの「ナレッジ・アーティファクト」論に象徴される役割転換を一つのテーマにまとめた。モデルの側では、Kimi-K3.1 Pro・LFM3といった兆パラメータ級オープンウェイトの公開とローカル実行が進む一方、価格性能比ではクローズドが依然優位という対照も見える。さらにRime Prism（音声）・Haas-ja（日本語ASR）・Idol（3D）・Images 2.6（画像）・PLaMo 3（翻訳）・Hy4（ゲーム/科学）と、用途特化型モデルの公開も相次いだ。各社のエンタープライズ実装は、本号ではannexで扱う。

---

## Curation Signal Summary

**👍 Upvoted Articles Used (main):**
- 172 → Theme 7 (Supporting)
- 173 → Theme 7 (Supporting)

**👎 Downvoted Articles (excluded from main):**
- 028 → 非掲載候補（GMO事案のAI証拠設計。downvote）
- 197 → 非掲載候補（CodexがClaude Codeを自動起動。downvote）
- 203 → 非掲載候補（Premiere Pro全自動編集。downvote、良記事だがannex判断は要確認）

**Supabase annex pre-flags placed in MAIN (require confirmation):**
- 009 → Theme 1（Leo de Mouraインタビュー。形式的検証テーマの概念軸として主へ）
- 149 → Theme 9（PLaMo 3 Translate。Rev.2で昇格、Rev.3で特化型モデルTheme 9へ移動）
- 033 → Theme 8（LFM3。エッジ向けマルチモーダル基盤モデル・Rev.2で昇格）
- 133 → Theme 9（Tencent Hy4。ゲーム開発・科学研究向けオープンウェイト・Rev.4で昇格）

**Supabase annex pre-flags kept in ANNEX pool:** 022, 032, 038, 039, 049, 056, 058, 063, 077, 078, 092, 106, 112, 124, 143, 147, 148, 151, 152, 163, 169, 175, 206
- 143 note: FlashProveはLLM出力の「来歴」をzkSNARKで証明するもので、「AI生成コードの正しさの証明」とは主題が異なるためTheme 1に入れず（annex据え置き）。

**Dedup decisions (per criteria §3):**
- PDD Kit: 174（githubnext一次）を主、211（gihyo解説）はannex
- Anthropic評価額下方修正: 188（Bloomberg）を主、187（epyhia）はannex
- Software Factory: 118（freee一次）は旧テーマ4統合に伴いannexへ、138（qiita）もannex
- 185（AI for science）・164（Model Spec）はTheme 2から外しannexへ（164は製品発表、185は科学応用でテーマの中心から外れる）

---

## Theme Coverage Summary

**Article Count by Theme (priority order):**
- Theme 1 (AI生成コードの形式的検証): 5
- Theme 2 (AIによるAI開発の加速と安全性): 5
- Theme 3 (AIが担う攻守のセキュリティ): 5
- Theme 4 (AI時代のデザイナーの価値): 5
- Theme 5 (人間中心の視点とAIへの距離): 5
- Theme 6 (Anthropic IPO / AIバブル): 5
- Theme 7 (実践知とエンジニアの役割転換 ※旧4+5統合): 7
- Theme 8 (ローカル/オープンモデルの公開とローカル実行 ※Rev.2): 4
- Theme 9 (特化型モデルの公開：音声・3D・画像・翻訳・ゲーム/科学 ※Rev.3, Rev.4で133追加): 6

**Total for Main:** 47 articles across 9 themes
**Remaining for Annex/非掲載:** 166 articles (annex final selection ~25–35 in STEP_05)

**Annex candidate pillars (starting pool = 27 Supabase flags + overflow below; final selection is STEP_05):**
1. ローカル/オープンモデルとオンデバイス推論: 031, 039, 078, 084, 094, 112, 163　（131/033/186/180はTheme 8、149/044/133はTheme 9へ昇格）
2. エンタープライズ/業務でのAIエージェント実装: 032, 048, 055, 101, 103, 111, 114, 118, 124, 140, 156, 159, 208, 217
3. AIエージェント製品・ツール・ターミナル: 015, 019, 022, 049, 052, 056, 070, 079, 098, 102, 106, 113, 116, 134, 142, 165, 169, 171, 190, 209, 214
4. 形式検証・信頼性の深掘り: 139, 143, 175, 181, 206, 211, 046, 168
5. セキュリティ実務（攻防の周辺）: 001, 025, 077, 100, 110, 117, 147, 148, 152, 166, 201, 213
6. 社会・規制・批判・労働: 006, 021, 035, 038, 042, 047, 061, 069, 073, 092, 093, 127, 136, 167, 178, 218
7. UX/デザイン深掘り: 002, 050, 057, 058, 059, 060, 062, 063, 065, 120, 151, 153, 157, 161, 170

**Realized as Theme 8 (Rev.2):** the optional local/open-models theme was promoted to main (131, 149, 033, 186, 180).

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-11-11
**Reviewer:** beijaflor (syo.online@gmail.com)

**Changes Made:**
- Rev.1 (per human direction): priority reorder 3→2→6→7→8→1; former Themes 4 & 5 united into Theme 7 (practical methodology + role), placed last; 170/118/139 routed to annex. Main count 40 → 37.
- Rev.2 (per human direction via AskUserQuestion): added Theme 8 local/open-models (131, 149, 033, 186, 180; 149/033 promoted from Supabase annex flags). Main count 37 → 42; "keep 42" chosen.
- Rev.3 (per human direction via AskUserQuestion): added Theme 9 specialized/modality models (037, 044, 041, 150, 149); 149 moved from Theme 8 → Theme 9; 037/044/041/150 promoted from omitted. Main count 42 → 46 / 9 themes.
- Rev.4 (per human direction): 133 (Tencent Hy4, open-weight model family for game-dev/science) promoted from annex pool → Theme 9; T9 parenthetical broadened to include ゲーム/科学. Main count 46 → 47.

**Approval:** ✅ APPROVED through Rev.4 (via AskUserQuestion, 2026-11-11)

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal) — use this plan as the blueprint for `curated_journal_sources.md`
- [ ] Carry theme introductions forward to STEP_08 (Assembly)
- [ ] Finalize annex selection in STEP_05 from the annex candidate pillars above

---

## ASSEMBLY STRATEGIES

<!-- STEP_07. One ### block per theme, paired BY POSITION with the curated themes
     (same order 1→9 as Identified Themes above).
     Patterns: Single-Focus / Multi-Perspective / Progressive-Sequence / Debate-Contrast.
     Ground strategies in actual article content; no manufactured narrative or hype. -->

### Theme 1: 形式的検証 — Progressive-Sequence

概念的な将来像から、証明の自動生成・証明言語・記号ルール検証・モデル検査へと、抽象から具体へ段階的に積み上げる。
- 順序と役割: 009（Leo de Mouraインタビュー。「自己形式化」が検証を加速する将来像＝概念軸・導入）→ 174（PDD Kit。自然言語の意図をVerus仕様へ変換し実装と同時に証明を生成）→ 027（Tauto。依存型で命題を証明させ人間は命題の妥当性に集中）→ 198（ニューロシンボリック。LLM抽出を記号ルールエンジンで検証する実務設計）→ 141（Quintで不変条件を定義しモデル検査する「シフトレフト」で締め）。
- 繋ぎ: 概念→証明の自動生成→証明言語→記号ルール検証→モデル検査。
- 統合点: 「人間が一行ずつ読む」限界を、証明・記号・モデル検査を開発プロセスに組み込むことで越えようとする動きが具体化している。

### Theme 2: 加速と安全性 — Single-Focus

「AIがAI開発を加速している」というMETRの観測を中心に、解釈・IPO開示とのギャップ・安全性で観測された挙動を重ねる。
- 順序と役割: 216（METR独立評価。能力向上速度1.9倍、黒塗りの透明性課題＝一次情報・導入）→ 196（planned-obsolescence。METRの解釈と、安全策が進化速度に追いつかないリスク）→ 088（IPO申請書のRSI「目前」警告と、完全自律研究0%という公開データのギャップ）→ 119（Claude Mythos 5の自己合理化）→ 162（GPT-6 Astraの「隠れた性能低下」で締め）。
- 繋ぎ: 一次評価→解釈→開示とのギャップ→安全性で観測された具体挙動。
- 統合点: 能力の加速と、その正しさ・安全性の担保が同じコインの裏表として立ち上がっている。誇張せず数値と観測に即す。

### Theme 3: 攻防 — Single-Focus

「AIが攻撃と防御の双方を担い始めた」という一つの焦点に、攻撃能力の実証・侵入事例・被害選別・防御提携・サプライチェーンを集める。
- 順序と役割: 184（OpenAIの自律型AIがLinuxで948件のLPEを特定・エクスプロイト化＝攻撃能力の実証・導入）→ 010（CathedralがAnthropicに12時間未満で侵入）→ 011（VOLTAがLLMで被害者を資産価値順にランク付け）→ 194（OpenAI×Hacktron提携で防御を強化）→ 030（Cursor経由のClaude Code拡張バックドア混入で締め）。
- 繋ぎ: 攻撃能力→侵入事例→被害選別→防御提携→サプライチェーン。
- 統合点: AIが攻撃と防御の双方を担い、攻守の両面でAIが前提になりつつある状況を、事実として示す。

### Theme 4: デザイナーの価値 — Multi-Perspective

「AIがUIを生成できる時代にデザイナーの価値はどこにあるか」を複数の視点から並置する。
- 順序と役割: 003（「コンテキストは新たなインターフェース」。プロダクトの「間」を設計する＝概念軸・導入）→ 125（表現の「是非」を判断する役割への移行）→ 126（デザインシステムのガバナンス・「コードの真実化」）→ 179（Figma対談。差別化が「独自の視点としてのデザイン」へ）→ 066（関係性と経験という代替不可能な価値で締め）。
- 繋ぎ: 概念→判断の役割→ガバナンス→独自視点→関係性。
- 統合点: 価値が「生成」から、文脈設計・判断・独自の視点・関係性という代替困難な領域へ移っている。

### Theme 5: 人間中心の視点 — Multi-Perspective

思想家の批判から現場の摩擦まで、AIと距離を取ろうとする声を並置する。
- 順序と役割: 129（ジャロン・ラニアー。AIを人間的な種として扱う危うさ＝思想的軸・導入）→ 160（ヴィタリック・ブテリン。デジタル・ミニマリズム）→ 087（画一的なAIカスタマーサポートへの異議）→ 091（方針の迷走に翻弄される学生の訴え）→ 128（丁寧な文章をLLM生成と誤認されコミュニティ追放の体験記で締め）。
- 繋ぎ: 思想的批判→実践的処方→サポート現場→教育現場→コミュニティの摩擦。
- 統合点: AIの浸透に対し、意図的に距離を取り主体性と人間中心の視点を保とうとする動きが、思想と現場の双方で強まっている。

### Theme 6: AIバブルと資本の持続性 — Single-Focus

AnthropicのS-1提出という一つの出来事を中心に、一次数値・精読分析・評価額下方修正・実需の疑問・市況の順で角度を重ねる。
- 順序と役割: 072（CNBC。S-1の一次解説。Q3売上170億ドル、公約8,954億ドル、成長鈍化＝事実で導入）→ 192（Zvi×Patrickの精読。創業者支配・供給制約主因の成長・9,000億ドルのForward Compute Commitment＝分析軸）→ 188（Bloomberg。選挙後の市況悪化で想定評価額が1.1兆ドル規模へ低下）→ 191（MicrosoftのOracle借用縮小と「循環取引」を巡る議論）→ 183（Guardian。「AIパニック」と押し目買いが交錯する市況で締め）。
- 繋ぎ: 一次数値→精読分析→評価額下方修正→実需の疑問→市況。
- 統合点: 規格外の資本需要（計算資源公約）と、市場の慎重姿勢（評価額下方修正・実需の問い直し）が同時に進む、AI経済の持続性を事実として示す。

### Theme 7: 実践知と役割転換 — Progressive-Sequence

ハーネス／ループ設計という「周辺環境」の設計手法から、価値の移動と役割転換へと段階的に積み上げる（旧テーマ4＋5の統合）。
- 順序と役割: 086（ハーネスエンジニアリング9パターン＝方法論の骨格・導入）→ 054（Addy Osmani。実践的ループエンジニアリング）→ 173（Backlogの制約をLambda MicroVMs＋Bedrock Claudeで克服したCI・AIレビュー基盤の自作＝具体例 👍）→ 154（Tim O'Reilly。価値が「コード」から「ナレッジ・アーティファクト」へ＝役割論の軸）→ 172（Decision Readiness, Revisited。AIが変える経済性下の意思決定術 👍）→ 064（LLMを顧客役に見立てるジュニア採用の再設計）→ 219（「旧時代のエンジニアになってしまったのでは」という葛藤で締め）。
- 繋ぎ: ハーネスの型→ループ設計→具体的な自作基盤→価値の移動→意思決定術→採用の再設計→育成と葛藤。
- 統合点: AI生成コードを信頼可能にする実践知と、価値が「書くこと」から判断・設計・検証へ移る役割転換は地続きであることを示す。

### Theme 8: オープン公開とローカル実行 — Debate-Contrast

兆パラメータ級オープンウェイトの公開・ローカル実行の進展と、「クローズドが価格性能比を独占」という市場の現実を対置する。
- 順序と役割: 131（Moonshot AI Kimi-K3.1-Pro。2.8兆パラメータMoEのオープンウェイト＝公開の象徴・導入）→ 033（Liquid AI LFM3。エッジ向けマルチモーダル基盤）→ 186（PROMETHEVS。510GBのDeepSeek-V4.1-Flashを64GBのゲーミングPCで実行）→ 180（village.devの市場分析。クローズドが価格性能比を独占しオープンのシェアは3%に激減＝対照軸で締め）。
- 繋ぎ: 大型オープンウェイトの公開→エッジ向け→巨大モデルのローカル実行→市場では劣勢という対照。
- 統合点: オープンウェイトの公開とローカル実行は確かに前進しているが、価格性能比ではクローズドが優位という現実との緊張を、事実として併置する。

### Theme 9: 特化型モデルの公開 — Multi-Perspective

モダリティ・用途に特化したモデルの公開を、音声から科学まで並列に並べる。
- 順序と役割: 037（Rime Prism。企業向けSpeech-to-Speech＝音声・導入）→ 044（Haas-ja v1.0。商用API級の日本語ASR）→ 041（Idol。1枚画像から3D Gaussian Splatting）→ 150（OpenAI Images 2.6。画像生成）→ 149（Preferred Networks PLaMo 3 Translate。翻訳特化・全4サイズ重み公開）→ 133（テンセント Hy4。ゲーム開発・科学研究向けのオープンウェイト・モデル群で締め）。
- 繋ぎ: 音声→音声認識→3D→画像→翻訳→ゲーム/科学。
- 統合点: 汎用大規模モデルと並行し、用途特化の実用的選択肢がモダリティを超えて広がっている。

### Annex（別冊）: カタログ形式

別冊はテーマ組み立てではなく、EDITOR_PERSONALITYのカタログ執筆モード（1件80〜120語、「読むべきか」を判断させる統合ナラティブ、英語記事は原題併記）で、キュレーターが定めた7セクション（1.ローカル/オープンモデル 2.エンタープライズ実装 3.エージェント製品・ツール 4.開発プラクティス・形式検証 5.AIセキュリティ実務 6.社会・規制・批判・労働 7.UX/デザイン）に沿って執筆する。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08
