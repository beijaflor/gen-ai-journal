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

---

## Identified Themes (7 main themes / 37 articles)

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
AI生成コードを信頼可能にする「実践知」と、それに伴うエンジニアの役割転換を一つにまとめた（旧テーマ4「ハーネスと検証の設計」＋旧テーマ5「エンジニアの判断と役割」の統合）。前半はハーネスエンジニアリングやループエンジニアリングといった「モデルを支える周辺環境」の設計手法、後半はティム・オライリーの「ナレッジ・アーティファクト」論やジュニア採用の再設計、「旧時代のエンジニア」の葛藤など、価値が「書くこと」から判断・設計・検証へ移る論考を扱う。

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

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週の開発テーマの軸は、AIが書いた大量のコードをどう信頼するかにあった。一方の極では、Lean創設者Leo de MouraのインタビューやGitHub NextのPDD Kit、Tautoのように「コードと同時に数学的証明を書かせる」形式的検証が具体化した。これと地続きで、第三者機関METRが、AI能力向上のペースが過去の約1.9倍に加速し、その主因がAI自身を使った研究開発である可能性が高いと報告し、再帰的自己改善（RSI）の入り口という見方と、Claude Mythos 5やGPT-6 Astraの安全性評価で観測された挙動とが並んだ。能力の加速と、その正しさ・安全性をどう担保するかが、同じコインの裏表として立ち上がっている。

セキュリティでは、OpenAIの自律型AIがLinuxカーネルで948件の脆弱性を特定してエクスプロイトを生成し、CathedralがAnthropicに12時間で侵入、インフォスティーラーVOLTAがLLMで被害者を選別するなど、AIが攻守の両側を担う局面が鮮明になった。デザインの領域では、UIの生成が容易になるなかで価値が「コンテキスト」や「独自の視点」へ移るという議論が続く。同時に、ジャロン・ラニアーやデジタルミニマリズム、カスタマーサポートや大学教育の現場からは、AIとの距離を意図的に取り直す人間中心の声も強まっている。

こうした技術の動きの背景で、AnthropicはIPOに向けたS-1修正届出を公開した。第3四半期売上170億ドルと約8,954億ドルの計算資源コミットメントという規格外の数字が示される一方、想定評価額は選挙後のAI株下落を受けて1.1〜1.3兆ドルへ下方修正され、マイクロソフトのOracle借用縮小とあわせてAI経済の持続性が問われている。開発手法と役割の面では、ハーネス／ループエンジニアリングという「周辺環境」の設計と、ティム・オライリーの「ナレッジ・アーティファクト」論に象徴される役割転換を一つのテーマにまとめた。ローカル/オープンモデルの最前線や各社のエンタープライズ実装は、本号ではannexで扱う。

---

## Curation Signal Summary

**👍 Upvoted Articles Used (main):**
- 172 → Theme 7 (Supporting)
- 173 → Theme 7 (Supporting)

**👎 Downvoted Articles (excluded from main):**
- 028 → 非掲載候補（GMO事案のAI証拠設計。downvote）
- 197 → 非掲載候補（CodexがClaude Codeを自動起動。downvote）
- 203 → 非掲載候補（Premiere Pro全自動編集。downvote、良記事だがannex判断は要確認）

**Supabase annex pre-flag placed in MAIN (require confirmation):**
- 009 → Theme 1（Leo de Mouraインタビュー。形式的検証テーマの概念軸として主へ）

**Supabase annex pre-flags kept in ANNEX pool:** 022, 032, 033, 038, 039, 049, 056, 058, 063, 077, 078, 092, 106, 112, 124, 133, 143, 147, 148, 149, 151, 152, 163, 169, 175, 206
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

**Total for Main:** 37 articles across 7 themes
**Remaining for Annex/非掲載:** 176 articles (annex final selection ~25–35 in STEP_05)

**Annex candidate pillars (starting pool = 27 Supabase flags + overflow below; final selection is STEP_05):**
1. ローカル/オープンモデルとオンデバイス推論: 031, 033, 039, 044, 078, 084, 094, 112, 131, 133, 149, 163, 180, 186
2. エンタープライズ/業務でのAIエージェント実装: 032, 048, 055, 101, 103, 111, 114, 118, 124, 140, 156, 159, 208, 217
3. AIエージェント製品・ツール・ターミナル: 015, 019, 022, 049, 052, 056, 070, 079, 098, 102, 106, 113, 116, 134, 142, 165, 169, 171, 190, 209, 214
4. 形式検証・信頼性の深掘り: 139, 143, 175, 181, 206, 211, 046, 168
5. セキュリティ実務（攻防の周辺）: 001, 025, 077, 100, 110, 117, 147, 148, 152, 166, 201, 213
6. 社会・規制・批判・労働: 006, 021, 035, 038, 042, 047, 061, 069, 073, 092, 093, 127, 136, 167, 178, 218
7. UX/デザイン深掘り: 002, 050, 057, 058, 059, 060, 062, 063, 065, 120, 151, 153, 157, 161, 170

**Optional additional theme (reviewer's call):** 「Kimi-K3.1・PLaMo 3 Translate・PROMETHEVSに見るローカル/オープンモデルの最前線」(131, 149, 186, 078/094, 180) — pillar 1 is strong enough to promote to a main theme if preferred; currently routed to annex.

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-11-11
**Reviewer:** beijaflor (syo.online@gmail.com)

**Changes Made:**
- Rev.1 (per human direction): priority reorder 3→2→6→7→8→1; former Themes 4 & 5 united into Theme 7 (practical methodology + role), placed last; 170/118/139 routed to annex. Main count 40 → 37.

**Approval:** ✅ APPROVED (via AskUserQuestion, 2026-11-11)

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal) — use this plan as the blueprint for `curated_journal_sources.md`
- [ ] Carry theme introductions forward to STEP_08 (Assembly)
- [ ] Finalize annex selection in STEP_05 from the annex candidate pillars above
