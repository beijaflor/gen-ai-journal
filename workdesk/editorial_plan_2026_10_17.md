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
