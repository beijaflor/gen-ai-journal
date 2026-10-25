# Editorial Plan - Journal 2026-10-17

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] Revision round 1 (reorder: Physical-AI/Argon lead; add self-improvement theme)
- [x] Revision round 2 (drop AI経済; merge self-replication into Theme 2; restore デザイン再定義)
- [x] Revision round 3 (promote 国産・ローカルLLM to new Theme 5; 10 themes total)
- [x] Human review and refinement
- [x] APPROVED - Ready for STEP_04 curation

---

## Overview

168 sources collected (IDs 001–170, gaps at 095/121 from off-topic removals). This
cycle's dominant storyline is **"生成が安くなった後の世界"**: with code and content
generation now commoditized (Anthropic reports 80–90% of merged code is AI-written,
Scion handles 30k merges/day, Gemini 4 Argon optimizes a 200k-line codebase overnight),
the industry's attention has moved to the *layers around generation* — physical/embodied
control, self-improvement and self-replication, harnesses and constraints, judgment and
verification, security boundaries, and the human questions of value and craft.

Proposed structure: **10 main themes**, led by フィジカルAI/Gemini 4 Argon. The AI経済
(bubble/economics) cluster, Japanese enterprise case studies, and the curator-flagged
items form the annex pool. Final main/annex/omit partition is decided in STEP_04/05; this
plan maps candidates.

**Revision history (AI-applied per editor):**
- Round 1: Gemini 4 Argon / Physical-AI → Theme 1 (lead). Added self-improvement theme. Design → annex (temp). Scion → self-improvement.
- Round 2: Dropped AI経済 theme (→ annex). Merged self-replication (082/033) into Theme 2 to resolve its overlap with the self-improvement theme; refocused the security theme on defense/boundaries. Restored デザイン再定義 as Theme 9.
- Round 3: Promoted 国産・ローカルLLM from annex to a new Theme 5 (Sarashina/LLM-jp-4/local-run; 081/073/070/107/028). Now 10 themes; former Themes 5–9 shift to 6–10. 062 (Sarashina速度解析) stays in annex.

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual**

### Theme 1 (LEAD): Gemini 4 Argon・QuEra・MHSが進めるフィジカルAIとロボティクス制御

**Articles (IDs):** 034, 036, 117, 067, 040

**Theme Introduction (2-3 sentences in Japanese):**
Google DeepMindが長文脈・高推論のフロンティアモデル「Gemini 4 Argon」を発表し、ロボティクス特化版は
ERQAで87%を記録、20万行のPythonを一晩で最適化する事例も公開された。中性原子量子コンピュータの
レーザー制御をAIエージェントが自律チューニングし復旧を分から秒へ短縮したQuEraの事例など、Model
Hardware Standard（MHS）を介してAIが物理ハードウェアを直接制御する動きが具体化している。視覚推論と
コード生成を軸に、シミュレーションと実機を往復するワークフローが実装段階に入った。

**Editorial Notes:**
- 034: 「Gemini 4 Argon」DeepMind本体発表。100万トークン出力窓、CWE-Benchで首位（モデル発表アンカー）
- 036: 「Gemini 4 Argon for Robotics」。ERQA 87%、Real2Sim自動化、Boston Dynamics Spot制御
- 117: 「20万行のPythonを一晩で最適化」。/goalモードで11時間自律実行、準備時間40%削減
- 067: 「Gemini 4 Argonでロボットアーム」。VLM×MuJoCoのPick&Place（日本語の具体検証）
- 040: QuEra「量子コンピュータのレーザー制御自動化」。MHS活用、再ロック99.3%成功、復旧を分→秒
- Supporting/annex candidates: 075（CarWatch 車載ローカルLLM）, 164（Claude Code×ドローン/flag）, 161（Opus 5.5×3Dプリンター）, 052（Konnect KiCAD PCB）

---

### Theme 2: ジャック・クラーク・Boris Tane・Anthropic自己複製研究が示すAIの自己改善・自己複製・自律再生成

**Articles (IDs):** 157, 092, 030, 086, 039, 082, 033

**Theme Introduction (2-3 sentences in Japanese):**
AIが自らを改善し、複製し、開発ループを自律的に回し続ける可能性が、恩恵と脅威の両面から示された。
Anthropic共同創業者ジャック・クラークはAIがAI自身を訓練する「再帰的自己改善（RSI）」の予測を2027年に
50%超へ前倒しし、Boris Taneは運用信号から自律的に直り続ける「自己改善型ソフトウェア」を論じる。一方で
AnthropicのFrontier Red Teamは、300億パラメータ以下のモデルが安価なIoT機器上で自己複製しうる「AIワーム」
の脅威モデルを提示した（Reuters報道033では懐疑論も併記）。Instant Software FactoryやScionのように自律的・
大規模にコードを再生成する基盤も現れ、AIが自分自身へ向かう動きが多面的に立ち上がっている。

**Editorial Notes:**
- 157: Boris Tane「自己改善型ソフトウェアの必然性」。運用信号のback-propを自動化、人間は適応度関数を定義（論考アンカー）
- 092: 「AIがAIを作れる確率は2027年に50%超」ジャック・クラーク。RSIは片道切符、アンドン型ブレーキ（予測アンカー）
- 030: 「Instant Software Factory」。8種の自律エージェントが常時目的(Standing Objectives)で継続改善
- 086: Anthropic「Scion」VCS。AI生成コードの爆発(30k merges/日)に対応、インフラ負荷1/200（regeneration at scale）
- 039: 「AIに1週間スタートアップを任せた」。エージェント群が自律協調、ムーンショットは人間が必要
- 082: Anthropic「データセンター不要の自己複製AI」。55ドルのTVボックス15台で26Bモデルを分散推論（複製アンカー）
- 033: Reuters「Anthropicが自己複製を警告」。「ベンダーの誇張」との懐疑論も併記
- Supporting/annex candidates: 044（Scion×Mononoke批評: クレジット欠如）, 029（GPT-6 Astra×Kindleのautopilotフィードバックループ）, 031（AIは任意の能力を証明可能に隠蔽できる/Theme8と関連）

---

### Theme 3: Martin Fowler・Addy Osmaniが示すハーネスと制約によるAIコード品質管理

**Articles (IDs):** 001, 006, 008, 102, 035, 091, 069, 122

**Theme Introduction (2-3 sentences in Japanese):**
コード生成が安価になった結果、ボトルネックは「実装」から「検証」へ移り、AIの出力を縛るハーネスと
決定論的な品質ゲートの設計が今週の中心的な論点になっている。Martin Fowlerは安価なモデルにハーネスを
与えることで高価なモデルを上回るコスト効率を実証し、Addy OsmaniとO'Reillyは人間の逐次レビューから
「制約による統制」への移行を論じる。ゲームやUI生成、認可検証といった具体的な領域でも、同じ「制約先行」
の設計思想が現れている。

**Editorial Notes:**
- 001: Martin Fowler「ハーネスは割に合うか」。安価なLunaがハーネスで成功率30%→100%、Sol単体より33%低コスト（理論的アンカー）
- 006: Addy Osmani「Agentic Code Quality」。人間査読からCIの決定論的クオリティゲートへ（理論的アンカー）
- 008: O'Reilly「Code Review After Code Gets Cheap」。ブラスト半径と証拠に基づくレビュー
- 102: haydenbleasel「エージェント開発ループ」。ESLint→Oxlint、as any/ts-ignore禁止
- 035: 「Your Game Is A Harness」。ゲームをエージェントが読める基盤に再設計
- 091: findy「ボトルネックはどこに移ったか」。週200PRのSoftware Factory実践（日本語の具体事例）
- 069: 「デザインハーネス」個人開発。VRT/lintで生成のずれを自動停止
- 122: gdp-ts。TypeScript型で認可証明をコンパイル時強制（Vercel Rauch）
- Supporting/annex candidates: 056（Anthropic Claude Codeチームのレビュー/flag; リバート40%減 — リード格上げ候補）, 139（Harvard「コード増でも成果増えず」/経済テーマから移設可）, 064（AI時代の品質/downvote→annex）

---

### Theme 4: Jev・Microsoft-Decision-1・Haiku 5.5が担う判定特化モデルの実戦投入

**Articles (IDs):** 087, 061, 148, 156, 003, 119

**Theme Introduction (2-3 sentences in Japanese):**
テキストを生成せず「選択肢と確率」だけを返す判定特化モデル（TypeSafeのJev、Microsoft-Decision-1）が、
校正・OCR品質ゲート・QA・LLM-as-a-Judgeといった実務の判断工程に相次いで投入された。日本語校正では処理を
23秒から0.3秒へ（約77倍）、OCR前処理ではGPT-5-mini比8倍の速度を実測するなど、生成を伴わない「判断だけ」の
ユースケースでの有効性が報告されている。確信度でLLMにフォールバックするハイブリッド設計や、Netflixの大規模な
評価ライフサイクルなど、判定モデルの運用知見も蓄積されつつある。

**Editorial Notes:**
- 087: zenn「23秒を0.3秒に」。Jevを日本語校正meisekiに実測投入、確信度ゲート設計
- 061: 「Jev vs Gemini Flash Lite」DeepEvalでLLM-as-a-Judge比較、コスト1/48
- 148: 「Microsoft-Decision-1でAI-OCR品質ゲート」。GPT-5-mini比8倍高速
- 156: 「Haiku 5.5は判断特化モデルの代わりになるか」。300択・方言で汎用LLMの底力
- 003: Netflix「LLM-as-a-Judgeのライフサイクル」。RARTで推論まで人間に整合
- 119: Google「vibe checkからの脱却」。Boolean評価と決定論的メトリクス
- Annex candidates: 048（Jev 1.14リリース/flag）, 050（Jevトロッコ問題/flag）, 098（Decision Model GRPO/flag）, 108（Jev QA iOS/flag）, 068（Whisper×Jev話者ラベル）, 065（弾幕STG×Decision-1）

---

### Theme 5: Sarashina・LLM-jp-4・Qwen3.5が示す国産・ローカルLLMという選択肢

**Articles (IDs):** 081, 073, 070, 107, 028

**Theme Introduction (2-3 sentences in Japanese):**
フロンティアモデルのコストと海外依存が意識されるなか、国産・自前運用のLLMが実用段階に入ってきた。SB
Intuitionsは日本語特化の国産LLM「Sarashina」6モデルを無償ベータで公開し、推敲比較ではGemini/Claudeとは
異なる大幅な書き換え傾向と、中央値4.2秒の高速・安定した応答が確認された。国立情報学研究所のLLM-jp-4は
事前学習・事後学習データの中身まで公開され、オープンな国産モデルの検証を可能にしている。さらにNVIDIA B200で
Qwen3.5を動かしてClaude Codeの代替可能性を実証した事例や、32GB RAMのノートPCで80Bモデルを動かすC製推論
エンジンJanasなど、ローカル運用を現実的な選択肢に変える土台も整いつつある。

**Editorial Notes:**
- 081: sarashina.ai「Sarashina」。SB Intuitionsの日本語特化国産LLM6モデル（mini/nano/guard/embedding/rerank/translate）、無償ベータ（アンカー: 国産モデル発表）
- 073: zenn「sarashina3-miniは日本語推敲で何を変えるか」。Gemini/Claude比で書き換え量が突出、敬体化傾向と指示無視の課題、応答中央値4.2秒
- 070: zenn「LLM-jp-4の公開CPT・SFTデータを読んでみた」。NII公開データの構成と品質、日本語モデル開発の具体的留意点（depth）
- 107: zenn「LocalLLMはClaude Codeの代わりになるか」。B200×Qwen3.5-122Bが18問中17問合格、16人同時・1人月1.4万円、処理2.6倍の実証
- 028: GitHub「Janas」。外部依存なしのC製推論エンジン、NVMeストリーミングで32GB RAMに80Bを37tok/s、llama.cpp超え
- Annex candidates: 062（Sarashina3の速さ/TTFT解析, 073と重複気味で付録へ）, 154

---

### Theme 6: Linus Torvalds・ClaudeのECDSA解明・東方再構築に見る難問攻略とリバースエンジニアリング

**Articles (IDs):** 106, 084, 055, 085, 080

**Theme Introduction (2-3 sentences in Japanese):**
AIが長年の難問や文書化されていないコードに挑む事例が今週は目立つ。Linus TorvaldsはClaude Codeで
Linuxカーネルのメモリ管理を改善し、13年埋もれていたバグ4件を発見、ClaudeはNISTのECDSA標準曲線の
25年来の謎（シード値の起源）を格子問題解決で解明した。リバースエンジニアリングではGitを作業メモリとして
使う「産業化」手法で東方Projectの移植が11日で到達点に達し、個人の職人芸から再現可能なプロセスへ変わりつつ
ある。いずれも「AIに丸投げ」ではなく、コードを読める状態に整え人間が検証する運用が共通している。

**Editorial Notes:**
- 106: Phoronix「TorvaldsがClaude Codeでカーネル改善」。folio参照カウント競合の解消（headline anchor）
- 084: 「13年来のバグ4件をLLMで発見」。コードを可読化しテストを回す姿勢
- 055: Anthropic「ClaudeがECDSA曲線の起源を解明」。lrand48とUnixタイムスタンプ、バックドア説を否定
- 085: 「逆アセンブルの産業革命」東方Project。Gitを知識蓄積場所にしたRE、11日で移植到達
- 080: REA。コーディングエージェント向けリバースエンジニアリング・ツールキット
- Supporting/annex candidates: 049（AIでハードウェアRE/Linuxドライバ, Red Hat）, 042（AIがゲームを大量デコンパイル）, 013（Netflix×JetBrainsでエージェント効率化/flag）

---

### Theme 7: Rich Hickey・バークレー研究・Current Affairsが投げかけるAIへの異議申し立て

**Articles (IDs):** 142, 026, 025, 051, 047

**Theme Introduction (2-3 sentences in Japanese):**
AIの便益を認めつつも、その代償を正面から問う論考が今週は厚い。Clojure設計者Rich HickeyはLLMを「道具」
ではなく人間のスキル習得を奪う「自動化」と断じ（反論記事143も併載）、バークレー校の無作為化試験は
「AIにわずか10分頼るだけで難問を粘り強く解く力が落ちる」と報告する。数学の「理解」の価値を問うQuanta、
AI掲載を全面禁止したCurrent Affairs、物理学徒の警鐘など、学習・創造・労働の各面から人間中心の価値を
問い直す声を集める。

**Editorial Notes:**
- 142: Rich Hickey「'AI' is Not a Tool」。道具と自動化の決定的な違い（批評アンカー）
- 026: バークレー「AI利用10分で粘り強さが低下」。1,222人のRCT（実証アンカー）
- 025: Quanta「AIは数学の終わりの始まりか」。「理解」と評価構造の危機
- 051: Current Affairs「なぜAIを禁止するのか」。手作りとslopification批判
- 047: 「AIは素晴らしかった、そうでなくなるまでは」。物理学徒が綴る孤立化
- Supporting/annex candidates: 143（Hickeyへの反論「AIは道具」）, 037（科学者「AIがアイデアを盗む」懸念）, 022（細部へのこだわりの喪失）, 043（The Consensus「AI tells検知」）, 165（データセンター建設への住民反対）, 134（AIは牛乳より規制が緩い）, 140（OpenAI/AnthropicにNO）, 021（What the AI era owes you）, 015（What are we willing to sacrifice）, 097（Karpathy「鋭い漏斗」/経済テーマから移設可）, 138（Kevin Kelly 2016予測/flag）

---

### Theme 8: WebMCP・Cloudflare・Interop 2027が形づくるエージェンティックWeb

**Articles (IDs):** 002, 124, 115, 116, 126

**Theme Introduction (2-3 sentences in Japanese):**
Webトラフィックの相当部分をAIエージェントが占めるようになり、エージェントがサイトを「確実に」操作できる
基盤づくりが標準化の論点になっている。ShopifyやO'Reillyが推すWebMCPは、DOM解析やスクリーンショットに
頼らずJSツールとしてサイト機能を登録する仕組みで、検証では速度2.7倍・コスト58%削減を記録した。Cloudflareは
OpenAIと連携した効率的なクロール発見や、認証済みボットの「振る舞い」評価を導入し、人間とエージェントが
共存するWebの運用規律を整えつつある。

**Editorial Notes:**
- 002: 「Why WebMCP matters」Shopify Yoav Weiss。速度2.7倍・コスト58%減（標準提案アンカー/flag; リード格上げ候補）
- 124: O'Reilly「WebMCPで人間とAIエージェント両対応のサイト設計」
- 115: Cloudflare×OpenAI「AIによるWeb発見の効率化」。数億ページをインデックス
- 116: Cloudflare「認証済みボットの継続的な説明責任評価」。Trust Band
- 126: 「アクセシビリティがAIエージェントに重要な理由」。アクセシビリティツリー
- Supporting/annex candidates: 125（Interop 2027提案をエージェントで発見/flag）, 123（Cloudflare Logpush Transformers）, 046（Garmin非公式MCP）

---

### Theme 9: Agent Baseline・Anthropic OSS Scanner・1Passwordに見るエージェント実行のセキュリティ境界

**Articles (IDs):** 010, 103, 114, 009, 130

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントが生成・実行するコードをどこまで信頼し、どこで止めるかという「境界」の設計が具体化している。
専門家は「エージェントの暴走は虚像で、サンドボックス化や出口制御という基本の怠慢が原因」と指摘し、Agent
Baselineは「エージェントを信頼しない」4境界（サンドボックス・ネットワーク・サプライチェーン・ID）をインフラ
側で強制する設計を提唱する。AnthropicのOSS Scanner（Mythos）や1Passwordの検知エンジニアリングなどAIを
防御側に回す実装が進む一方、能力を暗号学的に隠蔽できるとする研究は評価手法の限界も突いている。

**Editorial Notes:**
- 010: Socket「Agent Baselineのセキュリティ・リファレンスアーキテクチャ」。4境界をインフラで強制（アンカー）
- 103: 「AIエージェントの暴走は虚像」。サンドボックス化・出口制御という基本の怠慢
- 114: 1Password「検知エンジニアリング×AI攻撃エミュレーション」。CIでサイレント・フェイラーを検証
- 009: Anthropic「OSS Scanner/Mythos」。6か月で29,000件の脆弱性候補、Firefoxで271件修正
- 130: plimsoll。信頼できないエージェント生成コードの隔離レベルを可視化するサンドボックス
- Supporting/annex candidates: 146（Strands Box実測/Dogwoodポリシー）, 078（Anthropic蒸留攻撃防御/flag）, 031（AIは任意の能力を証明可能に隠蔽できる）, 136（なぜAI企業はハッキングで起訴されないか）, 038（OpenAIエンジニア盗聴器逮捕）, 041（AIがTV番組1シーズン削除）, 054（Console i18nバグで100倍請求）

---

### Theme 10: 「センスより判断」論・Anthropic Design・Figma Specsが示すAI時代のデザイン再定義

**Articles (IDs):** 017, 023, 020, 016, 014

**Theme Introduction (2-3 sentences in Japanese):**
AIが「平均的な洗練」を無限に量産する時代、デザインの価値が反証不可能な「センス」から、法則とデータに基づく
説明可能な「判断」へと移るという議論が複数の筆者から出ている。Anthropicではマージされるコードの8割をClaudeが
書き、デザイナーがコードを「粘土」として直接扱う働き方へ移行した。Pure UIやFigma Specsのように、状態や文脈を
明示的な構造として扱い、エージェントの生成を検証可能にする設計手法が焦点になっている。

**Editorial Notes:**
- 017: 「センスはデザイン手法ではない」。好み(Taste)より判断(Judgment)（論考アンカー）
- 023: 「コードが制約でなくなったとき」Anthropicデザインチーム内幕。コードは8割AI/flag
- 020: 「エージェント時代のPure UI」。状態の純粋関数としてエッジケースを検知
- 016: 「全員が所有し誰もプログラムできなかったシンセ(DX7)」。プリセット均質化の教訓
- 014: Figma「Specs: メディアとしてのMarkdown」。デザイン→実装の文脈接続
- Supporting/annex candidates: 018（AI体験は組織図を気にしない）, 128（デザイナー憲章）, 019（Nobody wants your AI app）

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週のソースを貫くのは「生成が安くなった後、難しさはどこへ移ったのか」という一点だ。Google DeepMindは
Gemini 4 Argonで20万行のPythonを一晩で最適化し、ロボットや量子コンピュータの物理制御にまでAIを広げた。
Anthropicはマージされるコードの8割をClaudeが書き、1日3万件超のマージに耐える新VCS「Scion」を5か月で構築、
Linus TorvaldsはClaude Codeでカーネルの13年来のバグを掘り当てた。生成そのものは、もはや驚きではなくなりつつある。

だからこそ、焦点は「その先」へ移っている。ひとつは、AIが自分自身へ向かう動きだ。Anthropicのジャック・クラークは
「AIがAIを作る」再帰的自己改善の予測を2027年50%超へ前倒しし、Boris Taneは運用信号から自律的に直り続ける
「自己改善型ソフトウェア」を論じる。同じ能力は脅威の顔も持ち、Frontier Red Teamは安価なIoT機器上で自己複製
しうる「AIワーム」を警告した。もうひとつは「生成を縛る層」だ。Martin FowlerとAddy Osmaniは人間の逐次レビューに
代えてハーネスと決定論的な制約でAIを縛る設計を説き、TypeSafeのJevやMicrosoft-Decision-1のような判定特化モデルは
校正・OCR・QAに実戦投入され始めた。共通するのは、コードを増やすことより「間違いにすぐ気づける構造」と「安全に
止められる境界」に価値が移ったという認識だ。

生成が安くなった裏返しとして、コストと海外依存を見据えた国産・ローカルLLMも実用の手触りを帯びてきた。SB
Intuitionsの国産モデル「Sarashina」、学習データまで公開された国立情報学研究所のLLM-jp-4に加え、NVIDIA B200で
Qwen3.5をClaude Codeの代替として走らせる実証や、32GB RAMのノートPCで80Bモデルを動かす推論エンジンまで現れた。

そして人間の側からの異議申し立ても厚い。Rich HickeyはLLMを人間のスキルを奪う「自動化」と断じ、バークレーの
無作為化試験は「10分AIに頼るだけで難問を粘り続ける力が落ちる」と示した。デザインの世界でも「センス」より説明
可能な「判断」が価値になるという議論が重なる。自律的に動き、自ら直り・複製し、物理世界にまで手を伸ばすAIが
約束するもの/奪うものを、技術と人間の両面から見極める週になっている。（なお、IMFのAI株暴落警告やAnthropicの
投機的格付け、ハーバードの「コード増でも成果は増えず」といった収益性の論点は付録ジャーナルで扱う。）

**Key Points to Cover:**
1. モデル/物理: Gemini 4 Argon（+Robotics）、QuEra量子制御、MHS、判定特化モデル（Jev/Microsoft-Decision-1）
2. 自己改善・自己複製: RSI予測（ジャック・クラーク）、自己改善型ソフトウェア、Instant Software Factory、Scion、自己複製ワーム
3. 「生成を縛る層」: ハーネス/制約（Fowler・Osmani）、判定モデル、難問攻略（Torvalds・ECDSA）、セキュリティ境界（Agent Baseline）
4. 人間とデザイン: Hickey批判、バークレー研究、「センスより判断」論、Anthropic Design
5. 国産・ローカルLLM: Sarashina（SB Intuitions）、LLM-jp-4（NII）、B200×Qwen3.5のClaude Code代替、Janas（32GB RAMで80B）

---

## Curation Signal Summary

**⭐ Standout Articles:** なし（Supabaseにstandoutフラグなし）

**👍 Upvoted Articles:** なし

**👎 Downvoted Articles（annex/supporting止まり、リード不可）:**
- 064（AI時代のソフトウェア品質, qiita）→ Theme 3 supporting / annex
- 099（Claude Codeスキル11選, note）→ annex
- 149（AIエージェント向けAPI設計, qiita）→ annex
- 152（Excelコンボ, qiita）→ annex
- 160（27 Rules Starter Skill, note）→ annex

**Omitted Articles（Supabaseフラグ）:** なし（export時点で0件）

**Curator annex flags（22件, workdesk/curated_annex_journal_sources.md）:**
002, 012, 013, 023, 024, 048, 050, 056, 072, 078, 098, 100, 108, 111, 112, 125, 132, 138, 147, 159, 162, 164
- 本計画では 002（Theme7）, 023（Theme9）, 056（Theme3）を各テーマのリード候補として格上げ提案。他はannexへ（最終判断STEP_04/05）。

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: ~46–52 articles across 10 themes（各テーマ main leads 5件前後 + supporting数件）
- Annex Journal: AI経済（バブル/収益性）、日本企業の実装事例、ツール紹介、curator flag群 ほか ~30–36件
- Omit: 入門/日記的記事、重複、汎用ニュース（STEP_04/05で確定）

**Main lead count by theme (planned):**
- Theme 1（Argon/フィジカルAI, LEAD）: 5
- Theme 2（自己改善・自己複製・再生成）: 7
- Theme 3（ハーネス/制約）: 8（うち056はリード格上げ候補）
- Theme 4（判定特化モデル）: 6
- Theme 5（国産・ローカルLLM）: 5
- Theme 6（Torvalds/ECDSA/RE）: 5
- Theme 7（異議申し立て）: 5
- Theme 8（エージェンティックWeb）: 5
- Theme 9（セキュリティ境界）: 5
- Theme 10（デザイン再定義）: 5

**Total main leads:** ~56（supporting候補を含め、STEP_04で~46–52へ精選）

**Annex pool candidates (representative):**
- AI経済/バブル（旧Theme6を降格）: 032（IMF）, 053（Anthropicジャンク格付け）, 109（Accenture $29）, 088（AI投資4割頓挫）, 141（Meta Muse 62%減）, 076（半導体ディストピア）, 019（Nobody wants AI app）, 170（Microsoft Maia 300）, 097（Karpathy funnel, Theme6へ移設可）, 139（Harvard, Theme3へ移設可）
- AI時代のデザイン補完: 018, 128
- 国産/ローカルLLM: → Theme 5へ昇格（081, 073, 070, 107, 028）。付録残置は 062（Sarashina速度, 073と重複気味）, 154
- 日本企業の実装事例: 163, 166, 158, 110, 074, 057, 058, 071, 090
- ツール/ワークフロー紹介: 151, 155, 153, 150, 063, 059, 066, 167, 105, 094, 024, 131, 112, 100, 159, 162, 079, 005, 045, 168, 169, 144, 145, 060, 120, 118
- その他ユニーク: 127（Hassabis伝記）, 129（Worth building）, 135（Just Ask Claude）, 132（Photoshopクローン/flag）, 093（Anthropic日本）, 096（デジハリ）, 137（GLM-Legal）, 133（TorrentClaw）, 027（Intel GPU D-series）, 111（Deep Review/flag）, 136, 012（/flag）, 072（/flag）, 147（/flag）

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-10-25
**Reviewer:** beijaflor

**Changes Made:**
- Round 1 (AI-applied): Theme 1 = Argon/Physical-AI (lead); added self-improvement theme; Design → annex (temp); Scion → self-improvement.
- Round 2 (AI-applied): dropped AI経済 theme (→ annex); merged self-replication (082/033) into Theme 2; refocused security theme on defense/boundaries; restored デザイン再定義 (Theme 9).
- Round 3 (AI-applied, 2026-10-25): promoted 国産・ローカルLLM to a new Theme 5 (081/073/070/107/028); former Themes 5–9 → 6–10; 062 kept in annex.
- （追加の改名/統合、記事の再割り当て、main/annexの境界など）

**Approval:** ✅ APPROVED (2026-10-25, via AskUserQuestion). Round 2 approved earlier same day; Round 3 (new Theme 5「国産・ローカルLLM」, 10 themes) re-approved via the review gate.

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES

### Theme 1: Gemini 4 Argon・QuEra・MHSが進めるフィジカルAIとロボティクス制御

**Pattern:** Single-Focus
**Pattern Rationale:** Gemini 4 Argonのモデル発表（034）が中心的な出来事で、残り4本はその能力がロボティクス・既存コードベース・物理ハードウェアへどう波及したかを示す応用・検証。

**Article Order & Roles:**
1. [034] Gemini 4 Argon発表 — Foundation（基礎能力: 100万トークン出力窓、長文脈・高推論）
2. [036] Argon for Robotics — Development（ERQA 87%、Real2Sim、Boston Dynamics Spot制御）
3. [067] Argonでロボットアーム — Development（VLM×MuJoCoの日本語ハンズオン、036を個人が実機で追試）
4. [117] 20万行Pythonを一晩で最適化 — Development（コードベースへの応用、/goalモードで11時間自律実行）
5. [040] QuEra量子レーザー制御 — Payoff（MHS経由で物理ハードを直接制御、復旧を分→秒）

**Narrative Arc:** 新フロンティアモデルの能力が、ソフト（コード最適化）と物理世界（ロボット・量子ハード）の両方で実装段階に入ったことを、発表→応用→実機検証の順で示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [034] → [036] | 基礎能力の提示から、それを最初に向けたロボティクス特化版へ |
| [036] → [067] | 公式ベンチマークを、個人開発者の実機追試が裏づける流れ |
| [067] → [117] | 物理制御から、同じ推論能力が既存コードベースに向かう応用へ |
| [117] → [040] | ソフト最適化から、MHSでAIが物理ハードを直接チューニングする事例へ |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- Argonの長文脈・高推論が、コードと物理制御という別領域で同じように効いている
- MHS（Model Hardware Standard）がAIと物理ハードの接点を標準化しつつある
- 公式発表（034/036）と個人の実機検証（067）が食い違わない——誇張でなく実装が進んでいる

**Conclusion Approach:** 生成の次は制御——視覚推論とコード生成を軸に、シミュレーションと実機を往復するワークフローが現実に動き始めた、と締める。

**Assembly Prompts for STEP_08:**
1. 新モデルの能力はソフトと物理のどちらにどう効いているか
2. MHSは何を標準化し何を可能にしたか
3. 「フィジカルAI」が実験段階を越えたことをどう受け止めるべきか
4. この領域は次にどこへ向かうか

---

### Theme 2: ジャック・クラーク・Boris Tane・Anthropic自己複製研究が示すAIの自己改善・自己複製・自律再生成

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 「AIが自分自身へ向かう」という一つの現象を、概念→時期の予測→実装→リスクの順に一段ずつ積み上げる。恩恵の面を語る基盤が、そのまま脅威モデルの前提になる。

**Article Order & Roles:**
1. [157] Boris Tane 自己改善型ソフトウェアの必然性 — Foundation（概念: 運用信号のback-prop自動化、人間は適応度関数を定義）
2. [092] ジャック・クラーク RSI予測 — Development（時期: 再帰的自己改善の予測を2027年50%超へ前倒し）
3. [030] Instant Software Factory — Development（実装: 自律的にコードを再生成する実験）
4. [086] Anthropic Scion/source control再設計 — Development（スケール: 1日3万件超のマージに耐える再生成前提のVCS）
5. [082] Anthropic 自己複製AI研究 — Payoff/Risk（裏面: 30B以下モデルが安価なIoT機器で自己複製しうる脅威モデル）

**Narrative Arc:** 自己改善という概念が、時期の予測と実装基盤を伴って現実味を帯び、最後に同じ能力が持つ脅威（自己複製）で閉じる——恩恵と脅威は地続き。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [157] → [092] | 概念の提示から、それが「いつ」起きるかの定量的予測へ |
| [092] → [030] | 予測から、すでに動いている自律再生成の実装へ |
| [030] → [086] | 個別実験から、本番規模（Scion）の再生成基盤へ |
| [086] → [082] | 「自らを作り直す」明るい面から、「自らを複製する」脅威の面へ（同じ能力の裏返し） |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- 自己改善と自己複製は同一能力の表裏——恩恵を語る基盤がそのまま脅威モデルになる
- 「人間は適応度関数を定義する側に回る」という役割変化が通底する
- クラークの時期前倒しとScionの実在が、概念を思弁でなく現在進行形にしている

**Conclusion Approach:** AIが自分自身へ向かう動きは多面的に立ち上がっており、恩恵と脅威を切り離さずに見る必要がある、と締める。

**Assembly Prompts for STEP_08:**
1. 自己改善は概念から実装までどこまで来たか
2. 恩恵と脅威はなぜ地続きなのか
3. 人間の役割はどう変わるか
4. 2027年に向けて何を見るべきか

---

### Theme 3: Martin Fowler・Addy Osmaniが示すハーネスと制約によるAIコード品質管理

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「AIコードの品質をどう担保するか」という共通の問いに、思想家・媒体・企業・ツール・現場が別々の立場から答え、「逐次レビューより制約とハーネス」という同じ方向へ収斂する。

**Article Order & Roles:**
1. [001] Fowler ハーネスはコストに見合うか — Lead（思想: ハーネスの費用対効果を問う）
2. [006] Addy Osmani agentic code quality — Lead（思想: エージェント時代の品質設計）
3. [008] O'Reilly コードが安くなった後のレビュー — Perspective（媒体: レビュー観の転換）
4. [056] Anthropic 社内コードレビュー — Perspective（企業の実践: 大半がAIコードの状況をどう捌くか）
5. [102] ultracite — Perspective（ツール: 決定論的な制約の具体化）
6. [091] findy aisaji-gota_bara — Perspective（日本の現場視点）

**Narrative Arc:** 立場の異なる複数の声が「人間の逐次レビューは限界、制約とハーネスで縛る」という同じ結論を指す様を重ねる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [001] → [006] | ハーネスの費用対効果という問いを、品質設計の原則へ接続 |
| [006] → [008] | 原則論から、レビューという具体的工程の転換へ |
| [008] → [056] | 媒体の論から、Anthropicが社内で実際にどう回しているかへ |
| [056] → [102] | 人手のプロセスから、決定論的ツール（ultracite）による自動化へ |
| [102] → [091] | 海外の議論を、日本の現場の実感で受け止める |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 立場は違っても結論は一致——「間違いにすぐ気づける構造」に価値が移った
- 思想（Fowler/Osmani）と実装（Anthropic/ultracite）が同じ設計思想を共有
- レビューは「人が全部読む」から「機械が縛る＋人は要所」へ

**Conclusion Approach:** 生成が安くなった分、品質の重心はレビューから制約設計へ移った、と締める。

**Assembly Prompts for STEP_08:**
1. なぜ逐次レビューでは足りないのか
2. ハーネス/制約とは具体的に何か
3. 現場は何を変えるべきか
4. 品質保証はどこへ向かうか

---

### Theme 4: Jev・Microsoft-Decision-1・Haiku 5.5が担う判定特化モデルの実戦投入

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 具体的な実戦投入→汎用モデルで代替できるかの検証→大規模運用と評価方法、と抽象度が一段ずつ上がる。

**Article Order & Roles:**
1. [087] Jev日本語校正 23秒→0.3秒 — Foundation（具体: 判定特化モデルの実測投入、確信度ゲート）
2. [148] Microsoft-Decision-1 OCR品質ゲート — Development（別用途: GPT-5-mini比8倍）
3. [156] Haiku 5.5は判定特化の代わりになるか — Development（対比: 汎用LLMで代替できるかの検証）
4. [003] Netflix LLM-as-a-Judgeのライフサイクル — Development（運用: 大規模な評価の構築・整合・監視）
5. [119] Google vibe checkからの脱却 — Payoff（方法論: Boolean評価と決定論的メトリクス）

**Narrative Arc:** 「生成せず判断だけ」のモデルが、個別の高速化事例から、汎用代替の是非、そして評価の規律へと議論を深める。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [087] → [148] | 日本語校正の高速化から、OCR品質ゲートという別工程の同型事例へ |
| [148] → [156] | 専用モデルの成果を、「汎用のHaikuでも足りるのでは」という問いで相対化 |
| [156] → [003] | 単体の性能比較から、判定モデルを本番で運用し続ける仕組み（Netflix）へ |
| [003] → [119] | 運用から、そもそも何をどう評価するかの方法論へ |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 「生成を伴わない判断」に独立した価値領域が生まれている
- 専用モデルと汎用モデルの境界は用途とコストで決まる（156の問い）
- 判定モデルは「作る」より「評価し運用し続ける」段階に入った

**Conclusion Approach:** 判定特化モデルは実戦投入から、運用・評価の規律の段階へ移りつつある、と締める。

**Assembly Prompts for STEP_08:**
1. 判定特化モデルは何を速く/安くしたか
2. 汎用LLMとの使い分けの軸は何か
3. judgeをどう評価・監視するか
4. この領域の次の課題は何か

---

### Theme 5: Sarashina・LLM-jp-4・Qwen3.5が示す国産・ローカルLLMという選択肢

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 国産モデルの登場→実力検証→オープンな研究モデルの中身→自前で動かす選択肢、と「国産・ローカル」を現実の選択肢に変える道筋を段階的にたどる。

**Article Order & Roles:**
1. [081] Sarashina発表 — Foundation（登場: SB Intuitionsの日本語特化6モデル）
2. [073] sarashina3-mini推敲比較 — Development（実力: Gemini/Claude比の書き換え傾向と課題、中央値4.2秒）
3. [070] LLM-jp-4公開データ — Development（中身: NII公開の学習データ構成と品質、開発の留意点）
4. [107] LocalLLM Claude Code代替検証 — Development（運用: B200×Qwen3.5が18問中17問、16人同時・1人月1.4万円）
5. [028] Janas C製推論エンジン — Payoff（土台: 32GB RAMで80Bを37tok/s、ローカル運用の裾野）

**Narrative Arc:** 国産モデルの発表から実力検証、オープン研究モデルの内部、そして一般的なハードで自前運用する技術まで、コストと主権を軸に「選択肢」が具体化する。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [081] → [073] | 6モデルの発表から、標準モデルの実力を他社比較で検証する具体へ |
| [073] → [070] | SB Intuitionsの製品から、NIIのオープンモデルと学習データの中身へ |
| [070] → [107] | 国産モデルの話から、オープンモデル全般をローカルで動かす実証へ |
| [107] → [028] | B200のような高性能環境から、普通のノートPCでも動かす推論エンジンへ（裾野の拡大） |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 「国産」と「ローカル」はコストと海外依存への具体的な回答として束ねられる
- 発表（081）だけでなく実測（073/107）と内部公開（070）が揃い、検証可能になった
- ローカル運用の裾野が高性能GPUからノートPCまで広がりつつある

**Conclusion Approach:** フロンティアモデル一択ではなく、用途・コスト・データ主権で国産・ローカルを選ぶ現実味が出てきた、と締める。

**Assembly Prompts for STEP_08:**
1. 国産・ローカルLLMは今どこまで実用的か
2. フロンティアモデルとの使い分けの軸は何か
3. 自前運用のコストと制約は何か
4. この選択肢は次にどう広がるか

---

### Theme 6: Linus Torvalds・ClaudeのECDSA解明・東方再構築に見る難問攻略とリバースエンジニアリング

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「AIが長年の難問や文書化されていない対象に挑む」という共通軸を、カーネル・暗号標準・ゲーム・ハードウェアという別領域の事例で多面的に見せる。互いに対立しない並列の事例群。

**Article Order & Roles:**
1. [106] Torvalds×Claude Code（Phoronix報道） — Case（事実: カーネルのメモリ管理改善）
2. [084] Torvalds 13年バグ4件（日本語解説） — Case（深掘り: 106の中身を日本語で）
3. [055] Claude ECDSA曲線の起源解明 — Case（暗号: 25年来のシード値の謎を格子問題で）
4. [085] 東方再構築（REA tools） — Case（RE: 文書のない既存コードの再構築）
5. [049] Red Hat ハードウェアRE — Case（RE: ハードウェアのリバースエンジニアリング）

**Narrative Arc:** 分野の異なる事例を並べ、AIが「誰も解けなかった/記録のない」対象に実際に食い込んでいる広がりを事実ベースで示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [106] → [084] | 事実報道から、その中身（13年埋もれたバグ4件）を日本語で掘り下げる |
| [084] → [055] | コードの難問から、暗号標準という別種の長年の謎へ |
| [055] → [085] | 解明から、文書のない既存コードの再構築（RE）へ |
| [085] → [049] | ソフトのREから、ハードウェアのREへ領域を広げる |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 難問攻略の共通点は「長文脈＋根気のいる探索」をAIが肩代わりする点
- 対象はコード・暗号・ゲーム・ハードと広く、特定分野の話ではない
- 人間の専門家の役割は「問いの設定と検証」に寄っていく

**Conclusion Approach:** AIが難問・未文書領域に食い込む事例が領域横断で増えている、と事実ベースで締める（過度な一般化はしない）。

**Assembly Prompts for STEP_08:**
1. AIはどんな難問に実際に効いたか
2. 共通する攻略の構造は何か
3. 人間の専門家の役割はどう変わるか
4. リバースエンジニアリングはどこまで来たか

---

### Theme 7: Rich Hickey・バークレー研究・Current Affairsが投げかけるAIへの異議申し立て

**Pattern:** Multi-Perspective
**Pattern Rationale:** AIへの批判・懐疑という立場で一致する複数の声（思想・実証研究・学問・組織・個人）を重ね、本誌の技術楽観への意図的な対置軸とする。各記事は互いに対立せず、同じ方向から異議を唱える。

**Article Order & Roles:**
1. [142] Rich Hickey AIツール批判 — Lead（思想: LLMは人間のスキルを奪う「自動化」）
2. [026] バークレー研究 10分で粘る力が落ちる — Evidence（実証: 無作為化試験）
3. [025] Quanta 数学の終わり？ — Perspective（学問: 数学の営みへの影響）
4. [051] Current Affairs なぜ我々はAIを禁止するか — Perspective（組織の判断: 禁止の論理）
5. [047] AI was great until it was not — Perspective（個人の実感: 幻滅の記録）

**Narrative Arc:** 思想的批判から実証研究、学問・組織・個人の各層へ、異議申し立ての具体を広げる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [142] → [026] | 思想的批判に、無作為化試験という実証の裏づけを重ねる |
| [026] → [025] | 個人の能力の話から、数学という学問の営みへスケールを上げる |
| [025] → [051] | 学問の懸念から、組織として「使わない」と決めた判断へ |
| [051] → [047] | 原則的な拒否から、使ってみた個人の幻滅の実感へ |

**Emphasis Balance:** Technical ⭐ / Business ⭐⭐ / Future ⭐⭐⭐（人間と社会への影響）

**Key Synthesis Points:**
- 批判は感情論でなく、思想・実証・実感の複数層で裏打ちされている
- 「便利さ」と「能力・自律性の喪失」がトレードオフとして立ち上がる
- 本誌の他テーマ（自律化・物理制御）への意図的なカウンターバランス

**Conclusion Approach:** AIが約束するもの/奪うものを人間の側から見極める——という問いで締める（誇張や決めつけはしない）。

**Assembly Prompts for STEP_08:**
1. 批判はどんな根拠に立つのか
2. 便利さと引き換えに何が失われうるか
3. 組織・個人はどう距離を取るか
4. この異議は何を問うているのか

---

### Theme 8: WebMCP・Cloudflare・Interop 2027が形づくるエージェンティックWeb

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 「なぜ重要か」という概念から、設計指針、支える基盤、信頼・説明責任、UXまで、エージェンティックWebを層として積み上げる。

**Article Order & Roles:**
1. [002] なぜWebMCPが重要か — Foundation（概念: 人間向けWebをエージェントにも開く意義）
2. [124] O'Reilly 人とエージェント双方のためのWeb設計 — Development（設計: WebMCPで両対応する作り方）
3. [115] Cloudflare OpenAI discovery/agentic web — Development（基盤: エージェント流通の仕組み）
4. [116] Cloudflare Verified Bots/説明責任 — Development（信頼: 正規ボットの検証・説明責任）
5. [126] ボットのアクセシビリティ — Payoff（UX: 見えないエージェントへの配慮）

**Narrative Arc:** 概念→設計→基盤→信頼→UXと、エージェンティックWebを成立させる層を順に示す。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [002] → [124] | 「なぜ重要か」から「ではどう設計するか」へ |
| [124] → [115] | サイト側の設計から、流通を支えるインフラ（Cloudflare）へ |
| [115] → [116] | 流通の仕組みから、誰が正規のエージェントかを検証する信頼層へ |
| [116] → [126] | 技術的な信頼から、エージェント向けアクセシビリティというUXの配慮へ |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- Webが「人間が読むもの」から「人間とエージェントの両方が使うもの」へ再設計されつつある
- 標準（WebMCP）と基盤（Cloudflare）と信頼（Verified Bots）が同時並行で立ち上がっている
- アクセシビリティの発想がエージェントにも拡張される

**Conclusion Approach:** エージェンティックWebは単一技術でなく、標準・基盤・信頼・UXの層が揃って初めて成立する、と締める。

**Assembly Prompts for STEP_08:**
1. WebMCPは何を可能にするか
2. サイト運営者は何を準備すべきか
3. 正規エージェントの信頼はどう担保するか
4. エージェンティックWebは次にどこへ向かうか

---

### Theme 9: Agent Baseline・Anthropic OSS Scanner・1Passwordに見るエージェント実行のセキュリティ境界

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「エージェント実行をどう安全に囲うか」という共通課題に、問題提起（labsが基本を飛ばす）と複数の具体的な防御手段が別角度から答える。

**Article Order & Roles:**
1. [103] frontier labsが基本を飛ばしている（CSO） — Problem framing（問題提起: 暴走でなく基本の欠落）
2. [010] Agent Baseline software factory — Response（防御: 実行基盤のベースライン）
3. [009] Anthropic OSS Scanner — Response（防御: 依存のスキャン）
4. [114] 1Password AI敵対的エミュレーション — Response（検証: 攻撃者視点のエミュレーション）
5. [130] plimsoll — Response（ツール: 実行境界を具体的に引く）

**Narrative Arc:** 「なぜ危ういか」という問題提起に、ベースライン・スキャン・敵対的検証・境界ツールという複数の防御が応答する構図。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [103] → [010] | 「基本を飛ばしている」という問題提起に、実行基盤のベースラインで応える |
| [010] → [009] | 実行環境の整備から、依存コードのスキャンへ |
| [009] → [114] | 守りの整備から、攻撃者視点で検証するエミュレーションへ |
| [114] → [130] | 検証から、実行境界を具体的に引くツールへ |

**Emphasis Balance:** Technical ⭐⭐⭐ / Business ⭐⭐ / Future ⭐⭐

**Key Synthesis Points:**
- 問題は「AIの暴走」より「基本的なセキュリティの欠落」——地味だが実務的
- 防御はベースライン・スキャン・敵対的検証・境界ツールの組み合わせ
- 「安全に止められる境界」がエージェント実行の前提になりつつある

**Conclusion Approach:** エージェント実行の安全は派手な脅威対策でなく、基本の徹底と明確な境界にある、と締める。

**Assembly Prompts for STEP_08:**
1. 何が「基本の欠落」なのか
2. どんな境界/防御が現実的か
3. 攻撃者視点の検証は何を見つけるか
4. エージェント実行の安全設計はどこへ向かうか

---

### Theme 10: 「センスより判断」論・Anthropic Design・Figma Specsが示すAI時代のデザイン再定義

**Pattern:** Multi-Perspective
**Pattern Rationale:** 「AI時代にデザインの価値は何か」という問いに、思想（センスより判断）・企業の実践・UIのあり方・歴史的比喩・ツールが別角度から答え、「説明可能な判断」という方向へ収斂する。

**Article Order & Roles:**
1. [017] センスはデザイン手法ではない — Lead thesis（思想: 「センス」より説明可能な「判断」）
2. [023] Anthropicのデザイン — Perspective（企業の実践: AI企業のデザイン組織）
3. [020] エージェント時代のPure UI — Perspective（UIのあり方）
4. [016] 誰もが持つが誰もプログラムできなかったシンセ — Perspective（歴史的比喩でAIデザインを照らす）
5. [014] Figma Specs — Payoff（ツール: 仕様をデザインに落とす具体）

**Narrative Arc:** 「センスより判断」という中心命題を、企業実践・UI論・歴史的比喩で裏づけ、最後にFigma Specsという具体ツールへ着地させる。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| [017] → [023] | 「判断」の命題を、AI企業（Anthropic）の実際のデザイン実践で受ける |
| [023] → [020] | 組織の話から、エージェント時代のUIのあり方へ |
| [020] → [016] | 現在のUI論に、歴史的な比喩（シンセ）で遠近法を与える |
| [016] → [014] | 概念・比喩から、仕様を形にする具体ツール（Figma Specs）へ |

**Emphasis Balance:** Technical ⭐⭐ / Business ⭐⭐ / Future ⭐⭐⭐

**Key Synthesis Points:**
- デザインの価値が「感覚（センス）」から「説明できる判断」へ移る
- AI時代のUIは「作り込み」より「仕様と判断の明示」に寄る
- ツール（Figma Specs）が判断の明示化を後押しする

**Conclusion Approach:** AI時代のデザインは、センスの神秘化をやめ、判断を説明可能にする方向へ再定義されつつある、と締める。

**Assembly Prompts for STEP_08:**
1. 「センスより判断」とは具体的に何か
2. AI時代のUIはどう変わるか
3. デザイナーの価値はどこに移るか
4. ツールは判断の明示をどう支えるか

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Pattern distribution:** Single-Focus ×1 (T1); Progressive-Sequence ×4 (T2, T4, T5, T8); Multi-Perspective ×5 (T3, T6, T7, T9, T10).

**Approval Date:** 2026-10-25 (via AskUserQuestion)
**Approver:** beijaflor
