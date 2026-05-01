## Figmaの苦境：Claude Designの登場とSaaSエコノミクスの地殻変動

https://martinalderson.com/posts/figmas-woes-compound-with-claude-design/

**Original Title**: Figma's woes compound with Claude Design

Anthropicが発表したClaude Designは、Figmaのユーザー基盤である非デザイナー層を直接奪い、SaaS企業が自社のAI推論提供者と競合するという構造的弱点を浮き彫りにしています。

かつてブラウザベースの設計とコラボレーションで市場を席巻したFigmaが、AIの台頭により「SaaSpocalypse（SaaSの黙示録）」の犠牲者になろうとしています。筆者のMartin Alderson氏は、Figmaのユーザーの約3分の2がデザイナー以外の職種（開発者、PM等）であることを指摘。これらの層が必要とする「プロトタイプや報告書などの補助的なデザイン業務」は、最新のLLM（Claude等）で十分に代替可能であり、Figmaのマルチプレイヤー機能やプラグインといった従来の「堀（モート）」を無効化しつつあります。

さらに深刻なのは構造的な問題です。Figmaは自社製品のAI推論にAnthropicのモデルを利用していますが、これは競合相手に資金を供給していることに他なりません。Anthropic側は、API経由で提供する古いモデル（Sonnet 4.5等）よりも優れた最新モデル（Opus 4.7）を自社のClaude Designに直接組み込むことができ、かつ推論コストも自社内なら極めて低く抑えられます。2,000人の従業員を抱えるFigmaに対し、Anthropicはごく少人数で対抗製品を構築できてしまうという、AI時代の新しいSaaSエコノミクスが提示されています。

---

## Claude Designをめぐる考察：デザインの「真実の源」は再びコードへと回帰する

https://samhenri.gold/blog/20260418-claude-design/

**Original Title**: Thoughts and Feelings around Claude Design

複雑化しすぎたFigmaのシステムに対し、AI時代には「コード」こそがデザインの真実の源泉となり、Claude Designのようなツールがその転換を主導するという洞察。

著者のSam Henri Goldは、Claude Designのリリースを受けてデザインツールの未来を考察しています。かつてFigmaはSketchに勝利しましたが、その過程で「変数・モード・プロパティ」といった複雑で独自の非公開システムを構築してしまいました。これらはLLMの学習データに含まれないため、AIエージェント時代においてFigmaは不利な立場にあります。一方でClaude Designは「素材への忠実さ（Truth to materials）」を掲げ、HTML/JSというコードを直接扱うことで、Claude Codeとのシームレスな連携を実現しようとしています。著者は、デザインツールが今後「実装に直結するエージェント型」と「システムに縛られない純粋な創造型」の2つに分かれ、FigmaがかつてSketchを追い抜いたような地殻変動が再び起きると予測しています。

---

## Google Labs、AI向けデザインシステム定義フォーマット「DESIGN.md」をオープンソース化

https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/

**Original Title**: Stitch app’s DESIGN.md format is now open-source for designers

Google Labsが開発した、AIエージェントにデザインの意図や規則を正確に伝えるためのMarkdown形式の仕様「DESIGN.md」がオープンソースとして公開されました。

Google Labsは、デザイン生成ツール「Stitch」で採用されているデザインルール定義フォーマット「DESIGN.md」のドラフト仕様をオープンソース化しました。このフォーマットは、プロジェクト間でデザインルールを共有可能にすることを目的としており、AIエージェントが単にUIを生成するだけでなく、その「意図（推論）」を理解できるように設計されています。これにより、特定のブランドガイドラインに沿ったUI生成や、WCAGアクセシビリティルールに基づいた自動検証が可能になります。Markdownベースであるため、開発者とデザイナーのワークフローに組み込みやすく、特定のプラットフォームに依存せずにAIとの協調を強化できる点が特徴です。現在GitHubで仕様が公開されており、コミュニティからのコントリビューションも受け付けています。

---

## AIエージェント時代のプロダクト作りの基礎知識「Agentic UX」とは？

https://goodpatch.com/blog/2026-04-agentic-ux

AIが自律的にタスクを遂行するAIエージェント時代において、デザインの焦点を操作性からAIとのコミュニケーション設計へと転換させる概念「Agentic UX」を提唱・解説する記事。

昨今のAI技術の進化により、ユーザーの意図を理解して自律的にタスクをこなす「AIエージェント」が普及しつつあります。これに伴い、プロダクト設計のあり方も、従来の「ユーザーが操作するUI」から「AIに依頼し、協働する体験」へと変化しており、その核となる考え方が「Agentic UX」です。Agentic UXでは、以下の4つの設計観点が重要視されます。1.意図(Intent)：曖昧な指示をAIが理解可能なタスクへ翻訳するプロセス。2.環境(Environment)：エージェントが動くためのルールやデータ構造の整備。3.信頼(Trust)：プロセスを可視化し、人間が承認できる仕組み(HITL)による透明性の確保。4.制御(Control)：人間が最終的な主導権を持ち、いつでも介入・修正できる操縦性の提供。AI導入の障壁となる「使い方が不明」「信頼できない」といった課題を、デザイナーが得意とする体験設計の力で解決し、AIと人間の円滑なパートナーシップを実現するための指針が示されています。

---

## Zero-dayの終焉：Mozilla、AI（Claude Mythos）を活用してFirefoxの脆弱性271件を一挙修正

https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/

**Original Title**: The zero-days are numbered

MozillaはAnthropicの次世代AI「Claude Mythos」を活用し、Firefox 150において271件の脆弱性を修正したことを発表し、AIによる自動診断が防御側に決定的な優位をもたらす時代の到来を告げた。

Mozillaは、Anthropic社の最新AIモデル「Claude Mythos Preview」を用いた大規模なソースコードスキャンにより、Firefox 150において271件のセキュリティ脆弱性を特定・修正したと報告しました。これは、従来のエリート研究者が手動で行っていた高度な推論によるバグ発見をAIが同等以上の精度で代替できるようになったことを示しています。

これまで、ソフトウェアの脆弱性をゼロにすることは不可能とされ、攻撃者が有利な「非対称性」が常識でした。しかし、AIによって脆弱性発見のコストが劇的に低下したことで、Mozillaは「防御側が決定的に勝利できる未来」が到来したと主張しています。Rustへの移行やサンドボックス化といった既存の多層防御に加え、AIによる網羅的な解析を組み合わせることで、複雑ではあるが有限であるソフトウェアの欠陥をすべて修正可能なターゲットとして捉え直しています。

---

## Anthropic「Claude Mythos」のセキュリティ能力に関する批判的検証：誇大広告と信頼の崩壊

https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/

**Original Title**: The Boy That Cried Mythos: Verification is Collapsing Trust in Anthropic

Anthropicが主張する「Claude Mythos」の驚異的なサイバー攻撃能力は、恣意的なベンチマークとデータの隠蔽に基づいた誇大広告であり、実際には安価な既存モデルでも再現可能であると批判している。

この記事は、Anthropicの新モデル「Claude Mythos Preview」に伴う244ページのシステムカードを精査し、そのセキュリティ能力の誇張を暴いています。筆者のDavi Ottenheimer氏は、Firefoxの脆弱性悪用成功率（72.4%）がわずか2つのバグに依存しており、それらを除外すると成功率が4.4%まで低下するという同社自身のデータを指摘し、モデルの汎用的な攻撃能力に疑問を呈しました。また、AISLEによる検証で、Anthropicが「危険すぎて非公開」とした脆弱性が安価な小規模オープンモデルでも発見可能であることが示され、筆者は「Project Glasswing」コンソーシアムを、透明性を欠いた「規制の虜」であり、恐怖を煽るマーケティング（FUD）を通じて独占的な地位を築くための手段であると強く非難しています。

---

## ペンタゴンが排除したAnthropicの最強AI「Mythos」、NSAが極秘利用か

https://news.ycombinator.com/item?id=47832222

**Original Title**: NSA is using Anthropic's Mythos despite blacklist | Hacker News

国防総省がAnthropic社を「サプライチェーンのリスク」としてブラックリストに登録した一方で、NSAが同社の高度なサイバーセキュリティAI「Mythos」を密かに利用している実態が判明しました。

Axiosの報道を端緒とした本議論は、米国家安全保障局（NSA）が国防総省（DoD）による禁止命令を無視して、Anthropic社の最新AIモデル「Mythos Preview」を運用している実態を浮き彫りにしています。Mythosはコード生成と自律的エージェント機能に特化した非公開モデルであり、数十年前の0デイ脆弱性を発見するなどの驚異的な能力を持つとされています。DoDは、Anthropicが軍事利用に対して独自の「憲法」や制約（ガードレール）を課そうとしていることを「供給網のリスク」と断定しましたが、NSAは実利を優先して導入を強行した形です。Hacker Newsのユーザー間では、この「リスク」指定が政治的な交渉カードに過ぎないという見方や、AIのモデル重みが核兵器並みの戦略物資として扱われ始めている現状、そして「Mythos」が単なるマーケティング的な誇大広告（ハイプ）なのか真の実力なのかについて、多角的な議論が交わされています。特に、オープンソースプロジェクトへのAI製脆弱性報告の急増など、実社会への影響も具体的に言及されています。

---

## GPT-5.5によるハッキング能力の飛躍的向上：XBOWによる脆弱性診断ベンチマーク評価

https://xbow.com/blog/mythos-like-hacking-open-to-all

**Original Title**: GPT-5.5: Mythos-Like Hacking, Open To All

GPT-5.5は脆弱性検出の見逃し率を大幅に改善し、ソースコードなしのブラックボックス診断でも前世代のホワイトボックス診断を上回る圧倒的な性能を達成した。

セキュリティ企業のXBOW社は、OpenAIの次世代モデル「GPT-5.5」の早期アクセスに基づいた脆弱性診断（ペネトレーションテスト）の評価結果を公開しました。GPT-5.5は、脆弱性の見逃し率を従来のGPT-5の40%からわずか10%まで削減し、Anthropicの「Mythos」に匹敵する性能を示しています。特筆すべきはブラックボックス環境での能力向上で、ソースコードを提供しない状態のGPT-5.5が、ソースコードを提供した状態のGPT-5の精度を上回りました。また、自律型エージェントとしての「粘りと諦め」の判断（Persist or Pivot）が洗練されており、ターゲットへのログイン試行回数の半減や、解決不能な試行の早期断念など、診断ワークフロー全体の効率が劇的に改善されています。このモデルの登場は、自動脆弱性診断における新たな基準（ゴールドスタンダード）を確立するものと評価されています。

---

## OpenAI、GPT-5.5を発表 — Terminal-Bench 2.0で82.7%、エージェントコーディングと長期タスクで実用的飛躍、API版も4月24日提供開始

https://openai.com/index/introducing-gpt-5-5/

**Original Title**: Introducing GPT-5.5

OpenAIは2026年4月23日にGPT-5.5（およびGPT-5.5 Pro）を発表、Terminal-Bench 2.0で82.7%、GDPvalで84.9%、OSWorld-Verifiedで78.7%とエージェントコーディング・コンピュータ操作・科学研究で大幅な性能向上を達成し、GPT-5.4と同等のトークン単価レイテンシを維持しつつ同タスクをより少ないトークンで完遂する「効率的な知能」を打ち出した。

OpenAIが **GPT-5.5** および **GPT-5.5 Pro** を発表しました（2026年4月23日、API版は翌24日提供開始）。「最も賢く、最も直感的に使えるモデル」と位置付け、エージェントコーディング・知識労働・科学研究という3領域での実用的飛躍を訴求しています。

### 主要ベンチマーク（OpenAI公表）

| ベンチマーク | GPT-5.5 | GPT-5.4 | Claude Opus 4.7 | Gemini 3.1 Pro |
|---|---|---|---|---|
| Terminal-Bench 2.0 | **82.7%** | 75.1% | 69.4% | 68.5% |
| Expert-SWE (社内) | **73.1%** | 68.5% | – | – |
| GDPval | **84.9%** | 83.0% | 80.3% | 67.3% |
| OSWorld-Verified | **78.7%** | 75.0% | 78.0% | – |
| Toolathlon | **55.6%** | 54.6% | – | 48.8% |
| BrowseComp | 84.4% | 82.7% | 79.3% | 85.9% |
| FrontierMath Tier 1–3 | 51.7% | 47.6% | 43.8% | 36.9% |
| FrontierMath Tier 4 | **35.4%** | 27.1% | 22.9% | 16.7% |
| CyberGym | **81.8%** | 79.0% | 73.1% | – |

さらにSWE-Bench Pro 58.6%、Tau2-bench Telecom 98.0%（プロンプトチューニングなし）、FinanceAgent 60.0%、社内投資銀行モデリング88.5%、OfficeQA Pro 54.1%。**全評価でGPT-5.4より少ないトークン使用**で同等以上の精度を達成。Artificial AnalysisのCoding Indexでは「競合フロンティアコーディングモデルの半額でSOTA」と主張。

### 性能の質的変化

社内・社外テスターからの定性的フィードバックが象徴的。Every社CEO Dan Shipper氏は「私が使った中で初めて深い概念的明確性を持つコーディングモデル」と評価、Cursor共同創業者Michael Truell氏は「GPT-5.4より顕著に賢く、長時間のタスクで早期停止せず継続する」、NVIDIAのエンジニアは「GPT-5.5へのアクセスを失うのは手足を切断されたような感覚」と述べました。

### 知識労働における実例

OpenAI社内では**85%以上の社員がCodexを毎週利用**。事例：

- **コミュニケーション部門**：6ヶ月分の登壇依頼データを分析、自動Slackエージェントを構築・検証し低リスク案件の自動処理を実現。
- **財務部門**：24,771件のK-1税務フォーム（71,637ページ）をレビュー、前年比で2週間の短縮。
- **GTM部門**：週次レポート生成を自動化し週5-10時間を節約。

### 科学研究での貢献

社内版GPT-5.5がカスタムハーネスと組み合わせて、**組合せ論の中心対象であるラムゼー数のオフ対角漸近事実について新しい証明**を発見し、Leanで形式検証されています。GeneBench（多段階の科学データ分析）、BixBench（バイオインフォマティクス）でリード。免疫学研究者Derya Unutmaz氏は62サンプル・約28,000遺伝子の分析を「チームで数ヶ月かかる仕事」を実現したと評価。

### 配信状況

- **GPT-5.5**：ChatGPTのPlus / Pro / Business / Enterprise + Codex で展開中
- **GPT-5.5 Pro**：ChatGPTのPro / Business / Enterprise
- **API**：4月24日アップデートで提供開始（システムカードに追加セーフガードを追記）
- 顧客採用：NVIDIA、Cisco、Abridge、Databricks、Harvey、Box、Lowe's、Glean、Palo Alto Networks、Ramp、Perplexity 等

### 安全性

OpenAI史上最強のセーフガードを謳い、内部・外部レッドチーム、サイバーセキュリティ・生物学領域のターゲット試験、約200の信頼パートナーからの実利用フィードバックを反映。

---

## OpenAI Codexの新機能「Chronicle」：画面内容から作業コンテキストを自動記憶

https://developers.openai.com/codex/memories/chronicle

**Original Title**: Chronicle – Codex | OpenAI Developers

OpenAIは、macOS版Codexにおいて画面上の情報を自動的に記憶（Memories）として蓄積し、プロンプト入力時の背景説明を省略可能にする新機能「Chronicle」を公開しました。

OpenAIが発表した「Chronicle」は、macOS版Codexアプリ向けのオプトイン方式のリサーチプレビュー機能です。この機能は、画面キャプチャやOCRを利用してユーザーの現在の作業内容（ファイル、Slackのスレッド、Webサイトなど）を解析し、それを「Memories」としてローカルに蓄積します。これにより、ユーザーはAIに対して「今見ているもの」に関する背景を詳しく説明する手間が省け、ツールやワークフローの文脈を維持したまま対話が可能になります。ただし、画面情報の利用に伴うプライバシーのリスクや、悪意のあるサイトからのプロンプト注入（Prompt Injection）リスクが増大するため、機密情報を扱う際の「一時停止」機能や、生成されたメモリ（Markdown形式）のローカル管理・削除方法についても詳しく解説されています。現在はChatGPT Proサブスクライバー向けに提供され、EU、英国、スイスは対象外となっています。

---

## OpenAI、Codex駆動の「Workspace Agents」をChatGPT Business/Enterprise/Edu/Teachers向けに研究プレビュー公開 — GPTsの後継として共有・スケジュール実行・Slack統合・承認ゲートを提供（5月6日まで無料）

https://openai.com/index/introducing-workspace-agents-in-chatgpt/

**Original Title**: Introducing workspace agents in ChatGPT

OpenAIは2026年4月22日、Codexを基盤とする「Workspace Agents」をChatGPT Business/Enterprise/Edu/Teachers向けに研究プレビューとして公開し、GPTsの進化形として組織内共有・クラウド実行・スケジュール起動・Slack連携・人間承認ゲート・コンプライアンスAPIなどエンタープライズ要件を備える（2026年5月6日まで無料、以降クレジット課金）。

OpenAIが **Workspace Agents in ChatGPT** をローンチしました（2026年4月22日、研究プレビュー）。同日のbusiness/workspace-agents/向け概要ページ（本誌#072参照）と並ぶ、より詳細な開発者・運用者向け発表です。本機能は **Codexを基盤とする「GPTsの進化形」** と明確に位置付けられ、共有可能・長時間動作可能・組織統制可能なエージェント基盤を提供します。

### GPTsからの差分

- **クラウド実行**：人がオフラインでもエージェントが継続稼働。
- **スケジュール実行**：定期タスクを無人化（金曜のメトリクスレポート等）。
- **Slack配備**：チャンネル内で能動的に応答するエージェントを展開可能。
- **メモリ・ツール・ファイル**：Codexのワークスペースを活用し、ステップ間の状態を保持。
- **GPTsとの併存**：当面はGPTsも継続提供、近日中にGPTs→Workspace Agentsへの変換機能を提供予定。

### 公式提示の5つのエージェント例

1. **Software Reviewer**：従業員のソフト要求審査・ポリシーチェック・ITチケット起票。
2. **Product Feedback Router**：Slack/サポート/公開チャネルからフィードバックを集約しチケット化、週次サマリ生成。
3. **Weekly Metrics Reporter**：金曜にデータ自動取得→グラフ生成→ナラティブ起草→共有。
4. **Lead Outreach Agent**：受信リードを評価しテーラードフォローアップを起草、CRM更新。
5. **Third-Party Risk Manager**：ベンダー調査（制裁・財務・評判リスク）の構造化レポート。

部門別テンプレート（finance / sales / marketing 等）も提供。

### 統制・セキュリティ機能

- **管理者制御**：ChatGPT Enterprise / Edu でユーザーグループごとに利用可能ツール・アクションを制御。
- **承認ゲート**：機微なアクション（メール送信・スプレッドシート編集・カレンダー追加等）に人間承認を要求可能。
- **プロンプトインジェクション耐性**：誤誘導コンテンツに対して指示への忠実性を保つビルトインセーフガード。
- **Compliance API**：エージェントの設定・更新・実行を監査可能、必要時に管理者がエージェントを停止可能。
- **アナリティクス**：実行回数・利用者数を共有後に確認可能。

### OpenAI社内事例

- **アカウンティング部門**：月次決算（仕訳・残高調整・差異分析）を分単位で完了、内部ポリシー準拠のワークペーパーを生成。
- **セールス部門**：通話メモとアカウント調査をまとめリードを評価、フォローアップを起草。
- **プロダクト部門**：Slackチャネルで従業員質問に応答、ドキュメントリンクを提示し新規問題はチケット化。

### 顧客採用事例

- **Rippling** Sales Consultant が単独で「Sales Opportunity Agent」をエンジニアリング不要で構築・反復。週5-6時間の手作業を自動化。
- 他に SoftBank Corp. / Better Mortgage / BBVA / Hibob が早期テスター。

### 提供条件

- 対象プラン：**ChatGPT Business / Enterprise / Edu / Teachers**
- **2026年5月6日まで無料**、同日からクレジットベース課金開始。
- 今後の予定：自動起動トリガー、改善されたダッシュボード、Codexアプリでのサポート追加。

---

## AmazonとAnthropicが戦略的提携を大幅拡大：1000億ドルのAWS利用コミットと最大250億ドルの追加出資

https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai

**Original Title**: Amazon and Anthropic expand strategic collaboration

AmazonとAnthropicは、今後10年間で1000億ドルのAWS利用と最大250億ドルの追加投資を含む提携拡大を発表し、独自AIチップ「Trainium」を用いた世界最大規模の計算基盤構築を加速させます。

AmazonとAnthropicは、生成AIの進化と普及を加速させるための戦略的提携を劇的に強化しました。Anthropicは今後10年間で1,000億ドル以上をAWSテクノロジーに支出することをコミットし、Amazon独自のAIチップである「Trainium」および「Graviton」を全面的に採用します。これに対しAmazonは、本日実施する50億ドルの投資に加え、将来的に特定の節目に応じて最大200億ドルの追加出資を行う計画です。

本提携の核心は、ハードウェアとインフラの共同開発にあります。Anthropicは、世界最大級のAI計算クラスタ「Project Rainier」を含むインフラ構築においてAmazonのAnnapurna Labsと緊密に連携し、次世代のTrainiumチップ設計に直接フィードバックを提供します。また、最大5ギガワット（GW）の電力を確保し、Trainium2から将来のTrainium4に至るまで、最先端モデルのトレーニングと推論に活用します。顧客向けには、AWS環境から直接AnthropicネイティブのClaudeコンソールを利用可能にするなど、開発体験の統合も進められます。この巨額の投資と技術連携により、両社はAI市場における主導権を盤石にする狙いです。

---

## Amazon Bedrock AgentCoreの新機能発表：インフラ構築を不要にし、数分でエージェントを稼働可能に

https://aws.amazon.com/jp/blogs/machine-learning/get-to-your-first-working-agent-in-minutes-announcing-new-features-in-amazon-bedrock-agentcore/

**Original Title**: Get to your first working agent in minutes: Announcing new features in Amazon Bedrock AgentCore

Amazon Bedrock AgentCoreが、設定のみでエージェントを即座に稼働させるマネージド・ハーネスや一貫した開発体験を提供するCLIなど、開発者がインフラではなくロジックに集中できる新機能を発表しました。

Amazon Bedrock AgentCoreは、AIエージェントの開発における最大の障壁であるインフラ構築とオーケストレーションの手間を解消する新機能を導入しました。主な機能として、わずか3つのAPIコールでエージェントを起動できる「マネージド・エージェント・ハーネス」が追加され、開発者はモデル、ツール、指示を設定するだけで、コンピュート、サンドボックス、認証などのバックエンド配線をAgentCoreに任せることができます。また、プロトタイプから本番環境まで一貫したワークフローを提供する「AgentCore CLI」や、長時間タスクのレジュームを可能にする「永続的ファイルシステム」も発表されました。さらに、Claude CodeやKiroといったコーディングアシスタント向けに、AgentCoreのベストプラクティスに基づいた専用スキルを提供することで、開発体験のさらなる向上を図っています。このプラットフォームは、LangGraphやLlamaIndexなどの既存フレームワークをサポートし、必要に応じて設定ベースからコード定義への移行も可能な柔軟性を備えています。

---

## Claude Cowork in Amazon Bedrock の提供開始：組織全体での AI 活用を AWS 環境内で実現

https://aws.amazon.com/jp/blogs/machine-learning/from-developer-desks-to-the-whole-organization-running-claude-cowork-in-amazon-bedrock/

**Original Title**: From developer desks to the whole organization: Running Claude Cowork in Amazon Bedrock

Amazon Bedrock 上で Claude Cowork が利用可能になり、企業はデータセキュリティとリージョン内のデータレジデンシーを維持しながら、ナレッジワーカー向けに高度な AI デスクトップ機能を展開できるようになりました。

Amazon Bedrock において、Anthropic のデスクトップアプリケーションを AWS 環境で実行できる「Claude Cowork」の提供が開始されました。これにより、開発者向けの Claude Code に加え、組織内のあらゆるナレッジワーカーが AWS のセキュリティ・コンプライアンス基準を満たした状態で Claude を活用できるようになります。

### 主な特徴とメリット
- **エンタープライズレベルのセキュリティ**: プロンプトやファイル、モデルの回答は Amazon Bedrock に保存されず、モデルのトレーニングにも使用されません。IAM による認証、VPC エンドポイントによるネットワーク隔離、CloudTrail による監査など、既存の AWS 管理機能をそのまま利用可能です。
- **デスクトップアプリの利便性**: ドキュメント分析、多段階のリサーチ、データ処理などのタスクを Claude Desktop アプリケーションから実行できます。MCP（Model Context Protocol）サーバーを通じて、ライブドキュメントや Web 検索、社内ツールとの連携も可能です。
- **柔軟な管理と課金**: Jamf や Microsoft Intune などのデバイス管理システムを通じて一括設定が可能。料金は AWS の従量課金制（コンシューマベース）であり、Anthropic 側でのシートライセンス契約は不要です。

なお、データ機密性を維持するため、Anthropic がホストするインフェレンスが必要な機能（Chat タブ、Computer Use、Skills Marketplace など）は含まれず、すべてのモデル推論はユーザーの AWS アカウント内の Amazon Bedrock を通じて行われます。

---

## Anthropicが$20のProプランから「Claude Code」を一時削除、AI課金モデルの限界が露呈か

https://www.wheresyoured.at/news-anthropic-removes-pro-cc/

**Original Title**: [UPDATED] News: Anthropic (Briefly) Removes Claude Code From $20-A-Month "Pro" Subscription Plan For New Users

Anthropicが一部の新規ProプランからAIコーディング機能「Claude Code」を一時的に除外し、高額なMaxプラン専用とするテストを実施していたことが判明しました。

Ed Zitronの調査により、Anthropicが月額20ドルの「Pro」プラン購読者からAIコーディング支援ツール「Claude Code」へのアクセス権を一時的に剥奪し、サポート文書を「Maxプラン専用」に書き換えていたことが明らかになりました。同社の成長責任者は、これが新規ユーザーの2%を対象とした「小規模なテスト」であると釈明し、現在は元の状態に戻されていますが、背景にはAIの推論コスト増大と現行サブスクリプションモデルの維持困難という課題があります。同社幹部は「現在のプランは現在の使用量に合わせて構築されていない」と発言しており、今後すべてのプランで制限が厳格化される可能性が示唆されています。MicrosoftもGitHub Copilotをトークンベースの課金へ移行する準備を進めていると報じられており、AI業界全体で「定額使い放題」の終焉が近づいていることを予感させる動きです。

---

## GitHub Copilot個人向けプランの変更：新規登録の停止と利用制限の強化

https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/

**Original Title**: Changes to GitHub Copilot Individual plans

GitHubは、エージェント機能による計算リソース消費の急増に対応するため、Copilot個人向けプランの新規受付停止や利用制限の厳格化を含む大幅な改定を発表しました。

GitHubは、GitHub Copilotの個人向けプラン（Pro、Pro+、Student）における運用方針の大幅な変更を発表しました。主な変更点は、新規サインアップの一時停止、セッションおよび週単位のトークンベース利用制限の強化、そして一部のハイエンドモデル（Claude 3 Opusなど）の利用可能プランの制限です。

背景には「エージェント的ワークフロー」の普及があります。自律的にタスクをこなすエージェント機能は並列的かつ長時間のリクエストを発生させ、計算コストが個人のサブスクリプション料金を上回るケースが頻発しています。サービス全体の品質維持のため、GitHubは制限の可視化をVS CodeやCLI上で開始しました。既存ユーザーは制限に達した場合、自動モデル選択への切り替えや、より高い制限を持つPro+へのアップグレード、または返金対応を選択することになります。この動きは、生成AIの提供コストとビジネスモデルの持続可能性という業界全体の課題を浮き彫りにしています。

---

## Anthropic、Claude ProプランからClaude Codeを削除するA/Bテストを実施。開発者コミュニティでは不信感と競合への乗り換え議論が加速

https://news.ycombinator.com/item?id=47854477

**Original Title**: Claude Code to be removed from Anthropic's Pro plan? | Hacker News

Anthropicが個人向けProプランからClaude Codeを削除するテストを開始し、不透明な告知と実質的な値上げに憤る開発者の間で他社モデルへの移行が検討されている。

Anthropicが、月額20ドルの「Claude Pro」プランからCLIツール「Claude Code」へのアクセス権を削除するA/Bテストを実施していることが判明し、開発者コミュニティに激震が走っています。

● **変更の背景と現状**: 同社の成長責任者は、計算リソースの制約とエージェント機能の利用激増を理由に、新規登録者の約2%を対象とした「テスト」であると説明しています。既存ユーザーは現時点では維持される見込みですが、ドキュメントが密かに書き換えられたことで不信感が高まっています。
● **コミュニティの反発**: Hacker Newsでは、この動きを「Enshittification（クソ化）」の兆候と捉え、事前の透明性あるコミュニケーションを欠いたAnthropicへの批判が集中しています。また、Opus 4.7のトークナイザー変更による実質的な利用枠減少への不満も重なっています。
● **代替ツールの模索**: 信頼を失ったユーザーの間では、OpenAIのCodex、Google Gemini、またはGLMやKimiといった中国製モデルへの乗り換え、さらにはQwenなどのローカルLLMへの回帰が現実的な選択肢として議論されています。
● **ビジネスの転換点**: 多くのユーザーは、Anthropicが個人の「プロシューマー」を切り捨て、より収益性の高いエンタープライズ（法人）やAPI利用へとリソースを集中させようとしていると見ています。

---

## LLM-as-a-Verifier：スコア粒度・反復検証・基準分解の3軸スケーリングでTerminal-Bench 2およびSWE-Bench VerifiedでSOTA達成（Stanford × UC Berkeley × NVIDIA）

https://llm-as-a-verifier.notion.site/

**Original Title**: LLM-as-a-Verifier: A General-Purpose Verification Framework

Stanford AI Lab・UC Berkeley Sky Computing Lab・NVIDIAらの共同研究によるLLM-as-a-Verifierは、スコア粒度・反復検証・評価基準分解の3軸を同時にスケールさせる汎用検証フレームワークで、Terminal-Bench 2（86.4%）およびSWE-Bench Verified（77.8%）でSOTAを達成し、Claude Opus 4.6・GPT-5.4・Gemini系を上回った。

Stanford AI Lab、UC Berkeley Sky Computing Lab、NVIDIAの研究チーム（筆頭著者Jacky Kwok氏、共著にIon Stoica氏、Azalia Mirhoseini氏らを含む）が、エージェント軌跡（trajectory）を細粒度に評価する汎用検証フレームワーク **LLM-as-a-Verifier** を発表しました。Test-time scalingの報酬モデルとして用いた場合、Terminal-Bench 2で **86.4%**、SWE-Bench Verifiedで **77.8%** のSOTAを達成しています。

### 既存「LLM-as-a-Judge」の限界

標準的なLLM-as-a-Judge手法は、モデルに離散スコアトークン（例：1〜8）を出力させ最高確率のトークンを最終スコアとするため、複雑な軌跡比較で同点が頻発します。Terminal-Benchでは **27%が同点（tie）** となり、優劣の判別に失敗するケースが顕著でした。

### 3軸スケーリングによる検証

本フレームワークは「判定（judge）」ではなく「検証（verifier）」として機能し、3つの軸を同時にスケールします：

1. **スコアトークンの粒度（G）**：1→20まで拡張。`<score_A>` `<score_B>` タグからtoplogprobsを抽出し、各トークンに対する条件付き確率分布を連続的な報酬として近似（量子化誤差を低減）。
2. **反復検証（K）**：1→16回。個別評価のバイアス・ノイズを平均化。
3. **評価基準の分解（C）**：軌跡全体の品質を直接推定するのではなく、「Specification（タスク要件への適合）」「Output（出力フォーマットの一致）」「Errors（失敗シグナルの欠如）」という相補的因子に分解。

報酬は \(R(t,\tau) = \frac{1}{CK}\sum_{c,k,g} p_\theta(v_g \mid t,c,\tau) \phi(v_g)\) として算出され、N候補からは総当たりトーナメントで最良軌跡を選定します。

### 実験結果

Terminal-Benchでの2方向検証精度はk=1で **74.7%**（LLM-as-a-Judgeは57.0%）、k=16で **77.4%**（同70.2%）。**Tie率はLLM-as-a-Verifierが全条件で0%**、Judge側はk=16でも5.4%残存します。エージェントハーネスを問わずプラグアンドプレイで適用可能で、ForgeCodeで86.4%、Terminus-Kiraで79.4%、Terminus 2で71.2%まで成功率を引き上げました。実験では検証側にGemini 2.5 Flashを採用し、Claude Opus 4.6のサンプル軌跡を主に評価対象としています。

### 意義

本研究は、Test-time scalingの中核要素である報酬モデルを、追加学習なしのフレームワーク設計だけでフロンティアモデルを上回る精度に押し上げた点で重要です。GitHub（`llm-as-a-verifier.github.io`）で再現コードが公開されており、PRM/ORMやRL訓練パイプラインへの統合が今後の方向性として示されています。

---

## Qwen3.6-27B：27Bデンスモデルがフラッグシップ級コーディング性能を達成、15倍規模のQwen3.5-397B-A17Bを全主要ベンチで凌駕

https://qwen.ai/blog?id=qwen3.6-27b

**Original Title**: Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

Alibaba CloudのQwenチームは2026年4月にQwen3.6-27B（27Bデンス・マルチモーダル）をオープンウェイトで公開し、SWE-bench Verified 77.2、Terminal-Bench 2.0 59.3など全主要コーディングベンチで15倍規模のQwen3.5-397B-A17B（MoE 397B/17B active）を上回り、Claude 4.5 Opusと並ぶ性能を27Bデンスという実用的スケールで実現した。

Alibaba CloudのQwenチームが、**Qwen3.6-27B** をオープンウェイトモデルとして公開しました（2026年4月）。Qwen3.6-Plus、Qwen3.6-35B-A3B（MoE）に続く同ファミリーの新ラインで、コミュニティで最も需要の高い27Bスケールの**デンス（非MoE）マルチモーダル**モデルです。Qwen Studioで対話可能、Hugging FaceとModelScopeで重みを配布、Alibaba Cloud Model Studio API経由でも利用可能。

### 主張：15倍規模のMoE Flagshipを上回る

本リリースの中核的主張は「**27Bデンスが、前世代フラッグシップQwen3.5-397B-A17B（総パラメータ397B / アクティブ17BのMoE）を全主要コーディングベンチマークで凌駕する**」ことです。コーディングベンチ抜粋（同レポート公開値）：

| ベンチマーク | Qwen3.6-27B | Qwen3.5-397B-A17B | Claude 4.5 Opus | Gemma4-31B |
|---|---|---|---|---|
| SWE-bench Verified | **77.2** | 76.2 | 80.9 | 52.0 |
| SWE-bench Pro | **53.5** | 50.9 | 57.1 | 35.7 |
| SWE-bench Multilingual | **71.3** | 69.3 | 77.5 | 51.7 |
| Terminal-Bench 2.0 | **59.3** | 52.5 | 59.3 | 42.9 |
| SkillsBench Avg5 | **48.2** | 30.0 | 45.3 | 23.6 |
| Claw-Eval Pass^3 | **60.6** | 48.1 | 59.6 | 25.0 |
| QwenWebBench | **1487** | 1186 | 1536 | 1197 |

Claude 4.5 OpusとTerminal-Bench 2.0で同点（59.3）、SkillsBenchとClaw-Eval Pass^3でClaude 4.5 Opusを上回ります。推論面でもGPQA Diamond 87.8、AIME26 94.1と強力。

### マルチモーダル能力

Qwen3.6-35B-A3Bと同様、**思考・非思考両モードを単一チェックポイントで統合**したネイティブマルチモーダル設計。画像・動画・テキストを処理し、文書理解・視覚QAをサポート。VideoMME (w sub.) 87.7、VlmsAreBlind 97.0、AndroidWorld 70.3など視覚エージェントタスクでも高性能。

### デプロイの実用性

MoEルーティングの複雑さを排した**デンスアーキテクチャ**により、トップティアのコーディング能力を実用的・広範に展開可能なスケールで提供する設計。コンテキスト窓は131,072トークン（推論時の最大トークン16,384）。SWE-Bench系評価では200K、Terminal-Bench評価では256Kコンテキストで実施。

### 統合エコシステム

Claude Code・OpenClaw（旧Moltbot/Clawdbot）・Qwen Codeの主要サードパーティコーディングエージェントと連携可能。Alibaba Cloud Model StudioはOpenAI互換API（chat completions / responses）に加え**Anthropic互換API**もサポートしており、`ANTHROPIC_BASE_URL=https://dashscope-intl.aliyuncs.com/apps/anthropic` を設定するだけでClaude CodeからQwen3.6-27Bを呼び出せます。`preserve_thinking` 機能でエージェントタスク向けに前ターンの思考内容を保持可能。

### 評価条件の補足

SWE-Bench Pro評価では公開セットの一部問題を補正し、全比較対象を補正版で評価。Terminal-Bench 2.0はHarbor/Terminus-2ハーネス、3時間タイムアウト、5回平均。SkillsBenchはOpenCode経由で78タスク（API依存タスクを除外した自己完結サブセット）。NL2RepoはClaude Codeで `temp=1.0, top_p=0.95, max_turns=900`。

---

## Kimi K2.6発表：コーディングと長時間自律実行を強化したオープンソースAIモデル

https://www.kimi.com/blog/kimi-k2-6

**Original Title**: Kimi K2.6 Tech Blog: Advancing Open-Source Coding

Moonshot AIが発表したKimi K2.6は、高度なコーディング能力と最大300のエージェントを同時並行で動かす「Agent Swarm」機能を備えた最新のオープンソースモデルです。

Moonshot AIは、コーディング、長時間実行（Long-horizon execution）、およびエージェント群（Agent Swarm）の能力を大幅に強化した最新モデル「Kimi K2.6」をリリースしました。このモデルは、SWE-Bench ProやTerminal-Bench 2.0といった難易度の高いベンチマークで、既存のクローズドモデルに匹敵、あるいは凌駕する性能を示しています。

主な特徴は以下の通りです：
- **長時間コーディングの自動化**: RustやGoなどの多言語対応に加え、10時間を超える連続実行や数千行のコード修正を自律的に行う能力。実証実験では金融マッチングエンジンの性能を劇的に向上させることに成功しています。
- **Agent Swarm（エージェント・スウォーム）**: タスクを最大300のサブエージェントに分解し、4,000ステップを並行して実行する水平スケーリング。ドキュメント、ウェブサイト、スライドなどを一度の実行で生成可能です。
- **Coding-Driven Design**: 単純なプロンプトからUIデザイン、アニメーション、データベース連携を含むフルスタックなウェブアプリを構築可能。
- **Claw Groups**: 複数のエージェントと人間が共同作業を行うための研究プレビューで、異なるデバイスやモデルのエージェントを統括するコーディネーターとしてK2.6が機能します。

Kimi.com、API、および専用のKimi Codeツールを通じて提供が開始されています。

---

## CLAUDE.md の肥大化を 3 層構造で 83% 軽くした — 実測と試行錯誤の記録

https://zenn.dev/pepabo/articles/claude-code-rules-skills-split

Claude Codeの肥大化する設定ファイルCLAUDE.mdを、ルールと遅延ロードされるスキルの3層構造に整理することで、起動時のトークン消費を83%削減した実体験に基づく技術解説。

Claude Codeを使い続ける中で肥大化しがちな`CLAUDE.md`（設定ファイル）の最適化手法を解説する記事です。筆者は2000行近くまで育った設定ファイルを「エントリーポイント（CLAUDE.md）」、「恒常的な制約（rules/）」、「オンデマンドのワークフロー（skills/）」の3層に再構成しました。特に、呼び出されるまでロードされない`skills/`へ機能を切り出すことで、起動時のトークン消費を11万超から約1.9万まで削減することに成功しています。また、Claudeが既知の一般原則（SOLID等）の削除や、chezmoiを用いたホスト別の設定出し分けなど、実用的なTipsも豊富に盛り込まれています。

---

## Android CLIと「Skills」の導入：AIエージェントによる開発を3倍高速化

https://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html

**Original Title**: Android CLI and skills: Build Android apps 3x faster using any agent

Googleは、AIエージェントを用いたAndroid開発を最適化するため、新しいAndroid CLI、タスク指示セット「Skills」、最新ドキュメントを提供する「Knowledge Base」を発表しました。

Googleは、開発者がGeminiやClaude CodeなどのAIエージェントを活用してAndroidアプリをより迅速かつ正確に構築できるようにする新しいツール群を公開しました。中心となる**Android CLI**は、プロジェクト作成やデバイス管理をプログラムから制御しやすく設計されており、従来のツールセットと比較してLLMのトークン使用量を70%削減し、タスク実行速度を3倍に向上させます。また、**Android Skills**はMarkdown形式(SKILL.md)の指示セットで、AIが最新のベストプラクティスに基づいたコーディング（Navigation 3への移行やEdge-to-Edge対応など）を行えるよう導きます。さらに、**Android Knowledge Base**により、AIは常に最新の公式ドキュメントを参照可能になります。これらのツールはCLIでの迅速なプロトタイピングから、Android Studioでの高度な最適化まで、シームレスな開発ワークフローを提供することを目指しています。

---

## ハーネスエンジニアリング時代の「環境構築」を一撃で終わらせるAPM

https://qiita.com/TKfumi/items/0751732005097816296c

AIエージェントの設定やスキルをnpmのように一括管理・共有できるMicrosoft製のパッケージマネージャー「APM」の活用法を紹介する記事。

AIエージェント（Claude Code、Cursor、GitHub Copilot等）がプロジェクトのコンテキストを理解するためには、適切な指示やスキルを与える「ハーネスエンジニアリング」が必要ですが、設定の共有や管理が煩雑になる課題があります。本記事では、この課題を解決するMicrosoft製OSS『APM (Agent Package Manager)』を解説しています。APMは、apm.ymlを用いてプロジェクトに必要な指示（Instructions）、スキル（Skills）、プロンプトテンプレート等を定義し、`apm install`コマンド一つで複数のエージェントツールに環境を展開できます。また、プロンプトインジェクションを防ぐためのセキュリティスキャン機能も備えており、チーム開発におけるAIエージェント利用の標準化を強力にサポートします。記事内ではObsidianスキルを導入する具体例やインストール手順も紹介されています。

---

## Claude向け経験的プロンプトチューニングのスキル定義 (mizchi/chezmoi-dotfiles)

https://github.com/mizchi/chezmoi-dotfiles/blob/main/dot_claude/skills/empirical-prompt-tuning/SKILL.md

著名な開発者mizchi氏による、Claudeの出力を改善するための「経験的プロンプトチューニング」手法を体系化したスキル定義ファイル。

本リソースは、開発者のmizchi氏が公開しているClaudeのCustom Instructions（Skills）の一部であり、LLMのプロンプトエンジニアリングにおける「経験的な調整（Empirical Tuning）」の手法を定義したものです。具体的には、単なる推測ではなく、プロンプトの微細な変更が結果に与える影響を観察・分析し、フィードバックループを回すための方法論をLLM自身に理解させるためのプロンプトセットとなっています。chezmoiを用いてドットファイルと共に管理されており、AIエージェントの振る舞いをより確実かつ技術的なアプローチで最適化しようとする試みの一つです。※対象のファイルパスがGitHub上で見つからない（404）場合がありますが、リポジトリの構成から、Claude Desktop等の拡張機能としての利用が想定されています。