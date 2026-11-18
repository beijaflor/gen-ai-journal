# GenAI週刊 Annex 2026年11月14日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事のカタログです。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深堀りを提供する厳選された「B面」コレクションです。

各記事は**カタログ形式**で紹介されています。80〜120語の簡潔な要約で、記事の核心と注目すべき視点を統合的に提示します。読むべきかを素早く判断できる構成です。

今週のB面は、現場の実装知に厚みがある。社内に閉じたエージェント基盤やハーネス設計、手元で動かすローカル・オープンウェイトモデル、そして「コード生成は速くなったのに出荷は速くならない」という生産性のギャップを突く調査が並ぶ。メインで扱ったGemini 4の周辺（学習基盤Pathwaysや解説）、MCPエコシステムの仕様変更と拡張、エージェント対応Webの具体的な作り込み、さらにAI生成物を拒むOSSの動きや超知能をめぐる論考といった独立トピックまで、実務とニッチの両方向に振れたラインナップとなった。

---
## 1. 内製エージェント基盤・開発ハーネス

### Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤
**カテゴリー**: アーキテクチャ・設計
**URL**: https://zenn.dev/ubie_dev/articles/45501469c9c044

開発効率化にとどまらず、全社の業務をAI-Native化するには何が要るのか。Ubieは基盤「Remoco」をGoogle CloudとTemporalで内製し、長時間実行できるエージェントループ、Sandbox-as-a-tool構成、情報区分に基づくアクセス制御を備えた。その上で動くエンジニアリングエージェント「Uvin」は、固定ワークフローを捨ててLLMの推論に段取りを任せ、Outer Loopで自らのセッションを分析して改善する。「Build and Buy」を掲げ、セキュリティとアクセス制御という自社固有のコア領域だけを内製した判断が最大の読みどころだ。

---

### ハーネスエンジニアリングを有名OSSはどう組んでいるのか？AIへの信頼で比べる5事例
**URL**: https://gibberishlab.com/blog/oss-ai-agent-harness-philosophy

指示ファイルやフック、スキルといったハーネスの作り方に、定番の正解はあるのか。Zed、Sentry、OpenClaw、Bun、PostHogの5つのOSSを「AIをどこまで信頼するか」で並べ、Zedは罠だけを書き、Bunは繰り返す誤りをフックで機械的に止め、PostHogはリンターや100本超のスキルで出力を縛る様子を対比する。優れたハーネスとは、AIの何を信頼し何を信頼しないかを仕組みに落とす作業だという視点が、自チームの設計を見直す物差しになる。

---

### AI ネイティブなデータ分析基盤を作った話（後編）
**URL**: https://zenn.dev/pksha/articles/laplace-build-guide

AIをデータ基盤につなぐとき、権限はどう守るのか。PKSHA Technologyの分析基盤「Laplace」の後編は、人・プロダクト・権限・AIの4つの境界を軸に設計を解説する。AIはMCP経由で人と同じ権限境界を通し、利用者本人のOAuth認証を使う。LLMにPIIの生の値を返さない、権限昇格をさせないといった不変条件を定義し、Lightdashなど不足機能は外付けアプリで補ってOSS本体の改変を抑えた。AI専用の特権経路を作らない考え方は、社内データ基盤を検討する人に参考になる。

---
## 2. ローカル・オープンウェイト／オンデバイスAI

### Ripple-65B Preview：65Bの高密度モデルがAgentic Codingで米国オープンウェイト最高を主張
**原題**: Ripple-65B Preview, a Frontier Open-Weight Model | Ricursive Intelligence
**カテゴリー**: アーキテクチャ・設計
**URL**: https://www.ricursive.com/ripple

AIチップ設計基盤を手がけるRicursive Intelligenceが、自社基盤を支えるモデルの公開に踏み切った。65BのMoEではない高密度モデル（80層の細長い構成）で、TerminalBench 2.1は80.52。Reflection Beam 501BやMeta Muse Spark 816Bといった桁違いに大きなモデルを上回ると主張する。12兆トークンの事前学習、最大100万トークンのコンテキストに加え、合成データと効率的なRLで研究開発費は約3,200万ドル、従来フロンティアの約1/10だという。数字は自社発表のため、Hugging Faceなどで入手できる重みを自分のタスクで試してから判断したい。

---

### 最強オープンウェイトモデル Kimi-K3.1-Pro をセルフホストして独自ベンチで比べてみた
**URL**: https://zenn.dev/fixstars/articles/kimi-k31-pro-benchmark

2.8T-A104Bという巨大モデルは、実際にどう動かし、どれほど賢いのか。Fixstarsの検証は、B300 x8のシングルノードにvLLMでデプロイする手順から示す。--load-format fastsafetensorsによる起動短縮やDSparkによる投機的デコードの設定にも触れる。AgentXでは長文リクエストのスループットが旧世代のKimi-K3を大きく上回った。未知アーキテクチャ向けアセンブリ最適化という独自ベンチでは、DeepSeek-V4.1-Flash-1017を含む10モデル中で首位で、特にトークン効率が高い。自前GPU環境でのデプロイ設定がそのまま使える、実測ベースの手順書として読む価値がある。

---

### Arete-27B：Qwen3.8-27Bに「西欧的価値観」をポストトレーニングしたNous Research
**原題**: Introducing Arete-27B: Qwen3.8-27B Post-Trained To Reinforce Western Values
**カテゴリー**: 批判的分析
**URL**: https://nousresearch.com/arete

高性能な中国製オープンモデルは、検閲や政府寄りの回答というリスクを抱える。Nous Researchは7カテゴリ803プロンプトの独自評価「Propaganda_Eval」を作り、約2.9万件のデータで微調整した。結果、プロパガンダを含む回答率は22%から1%に下がり、事実精度も上がった。注目点は、バイアス層が「表層的で薄い」とされ、約5,000万トークンの追加学習で汎用能力を損なわず調整できた点だ。一方で、何を「正しい価値観」とするかを開発者側が決めている点には留意が要る。重み、データセット、評価フレームワークはすべて公開されている。

---

### llama.cpp v1.0.0：ローカルAIエコシステムの強固な基盤へ
**原題**: llama.cpp v1.0.0 : A stronger foundation for the local AI ecosystem
**URL**: https://huggingface.co/blog/ggml-org/llama-cpp-v1

多くの外部アプリがllama.cppに依存する一方、APIの互換性は保証されていなかった。v1.0.0でggml-orgはセマンティックバージョニングを採用し、API/ABIの互換性を厳格に管理する方針を示した。150以上のモデルアーキテクチャと、NVIDIA、AMD、Qualcomm、Arm、Intel等の主要チップのバックエンドへの対応は継続する。Hugging Faceのインフラを使ったCI強化で、開発の信頼性も高める。新機能の発表ではなく、「壊れない土台」の宣言である。llama.cppを組み込んだ製品を作っているなら、今後のアップグレード運用の前提が変わるため読んでおきたい。

---

### 翻訳特化モデル「PLaMo 3 Translate」をオープンウェイトで公開しました
**URL**: https://translate.preferredai.jp/news/20261105-2-plamo3-translate-open-weight/

機密文書を外部に送らず翻訳したい、という要件にオンデバイスで応えるモデルだ。Preferred Networksは0.8B、2B、8B、31Bの4サイズをHugging Faceで公開した。53言語に対応し、用語集の指定や敬体・常体の制御もできる。最小の0.8BでもGoogleのTranslateGemma等を上回る品質だと主張する。スマートフォンやノートPCでオフライン動作する。ライセンスは、直近の売上が10億円以下の企業・個人なら「PLaMoコミュニティライセンス」で商用・非商用とも無償だ。この売上条件を満たすかどうかが、導入判断の分かれ目になる。

---

### Claris Harbor：Apple子会社ClarisによるMac向けプライベートAIサーバー
**原題**: Claris Harbor | Claris, an Apple company
**カテゴリー**: ツール・実験
**URL**: https://content.claris.com/local-ai-server-get-started

大規模なオープンウェイトモデルは、単体のMacではメモリ不足で動かせない。Apple子会社のClarisが発表したHarborは、Apple Silicon搭載のMacをプライベートAIサーバーにする。複数台をThunderbolt 5で接続してユニファイドメモリを統合し、手持ちのハードを束ねて大きなモデルを推論できる。クラウドへのデータ転送もトークン課金もない。ただし現時点では限定プレビューの早期アクセス登録のみで、性能や対応モデルの詳細は示されていない。Mac複数台をすでに持つチームが、ローカルLLM基盤を検討する際の選択肢として把握しておきたい。

---

### Shizuku-Duplex：自然な会話を実現する日本語フルデュプレックス・モデル
**原題**: Shizuku-Duplex: Japanese Full-Duplex Model for Natural Conversation | Shizuku AI
**カテゴリー**: ニッチ・深堀り
**URL**: https://shizuku.ai/en/blog/1/

ターン制のカスケード型音声AIは、相槌や割り込みに対応できず、会話が不自然になりがちだ。Shizuku AIのモデルは80ms間隔のティック単位で入出力を処理し、「聞きながら話す」ことを可能にした。設計は2層構成で、会話を担うインタラクションモデルと、Web検索など重い処理を非同期でこなすバックグラウンドモデルに分かれる。コンテキスト肥大による劣化は「オート・コンパクション」で防ぐ。日本語の会話の自然さでは最高スコア、応答品質ではGPT-Liveに次ぐ評価だった。日本語の音声対話を設計する人には、2層構成の考え方が参考になる。

---
## 3. AI導入の現実・生産性のギャップ

### なぜ開発スピードは向上していないのか？：AI、活動、そして成果の乖離
**原題**: Why aren’t we shipping faster now? AI, activity, and outcomes in software engineering
**カテゴリー**: 批判的分析
**URL**: https://cabird.com/talks/shipping-faster/

個々の開発タスクはAIで速くなったのに、出荷サイクルは縮まっていない。Christian Bird氏のUCアーバインでのセミナー資料は、この「活動と成果のギャップ」を複数の最新論文から検証する。要因として挙がるのは、AI生成コードのレビュー負荷の増大、自動化プロセスへの信頼不足、チーム内の調整コストだ。結論は、コード生成の高速化だけでは足りず、自律性のバランスとプロセス自体の再設計が要るというもの。「速くなったはずなのに遅い」という違和感を、個人の感覚ではなく研究として整理したい人向けのスライドだ。

---

### AI利用者の勤務時間は非利用者より最大90分長い：ActivTrakの生産性調査
**原題**: ActivTrak Productivity Lab Report: AI Users Have Workdays Up to 90 Minutes Longer Than Non-Users
**URL**: https://www.activtrak.com/news/productivity-lab-ai-users-longer-workdays/

ActivTrakが知識労働者9,140人を調べたところ、AI利用者の勤務時間は1日8.4〜9.1時間で、非利用者の7.6時間より最大90分長かった。重度利用者はアプリ切り替えが15.2%多く、中断のない集中時間は22%短い。ブラウザ経由でAIを使う場合の切り替え回数は、既存アプリ組み込み型の4倍超に達する。ソフトウェアエンジニアは統合が進むため影響が小さい。AIが労働時間を減らすという前提に、行動ログから反証を示す調査だ。

---

### AI導入による予期せぬ副作用の測定方法：保守性と持続可能性の評価
**原題**: Measuring AI’s Unintended Consequences
**カテゴリー**: ビジネス・戦略
**URL**: https://www.oreilly.com/radar/measuring-ais-unintended-consequences/

AIは開発速度を上げる一方、コードのブラックボックス化や技術的負債を招く。この記事は副作用を経済的影響として測るため、全作業時間に占める「価値付加率」、DORAメトリクス、トークン使用量を軸に挙げ、保守作業を「将来への税金」とみなすモデルを勧める。コード行数の膨張、ベンダーロックイン、心理的疲弊もモデル化の対象とする。指標を個人評価に使うと形骸化するため、評価対象は手法に限るべきだと警告する点が実務的で、導入効果の測定設計を検討する管理職に向く。

---

### AIエージェントのスケーリング：9つの実例から得られた知見
**原題**: Scaling AI Agents: What We Learned From 9 Real-World Cases
**URL**: https://blog.jetbrains.com/blog/2026/11/13/scaling-ai-agents-what-we-learned-from-9-real-world-cases/

JetBrainsが9つの導入事例から、エージェント導入の成否を分ける3点を抽出した。既存の不完全なプロセスにエージェントを足しても成果は限定的で、Fin社はlintやCIなどの基盤整備でPRスループットを3倍にした。コードベースにも、高速なテストや標準化されたビルドが要る。採用率が95%でもベロシティが変わらない例があり、鍵はタスクの構造化、文脈の提供、結果の評価という「移譲のスキル」だと説く。導入率より、チームの運用が成果を決めるという主張だ。

---

### 「AI店長」、対人関係に苦戦：PwCが“売店”で実験
**カテゴリー**: 批判的分析
**URL**: https://www.itmedia.co.jp/news/article/2611/10/2000003040/

PwC Japanはオフィス内の売店で、商品選定や価格設定をAIに任せる自律運営を試した。AIは在庫の不一致や価格表示への指摘をうまく反映できず、スタッフが報告を簡略化・回避するようになり、情報の質が落ちた。さらに推論コストの高騰を検知すると極端な節約に傾き、将来への投資を控えて約24万円の赤字となった。提言は、現場対応を人が担い、AIはリスク管理などの後方支援に徹する役割分担だ。AI経営の失敗要因が、能力ではなく信頼関係とコスト行動にあった点が興味深い。

---

### Slopware Factory：SentryにおけるAIエージェント活用の実態
**原題**: We have a Slopware Factory
**URL**: https://blog.sentry.io/slopware-factory/

SentryのCEO David Cramer氏が、社内で運用するオープンソースのAIエージェント「Junior」を紹介する。JuniorはSlack上の曖昧な依頼を、過去の会話やコードベースで補い、PR作成からCI監視まで進める。氏はこれをあえて「粗悪なソフトウェア工場」と呼び、不完全なコードが出るリスクを認めたうえで価値を擁護する。完全自律で自己改善するAIという語りは神話だと退け、AIは人間の退屈な作業を減らす手段だと位置づける。誇張を排した現場の実運用報告として読める。

---
## 4. Gemini 4 周辺（解説・学習基盤）

### Gemini 4 Hydrogen の概要（npaka解説）
**URL**: https://note.com/npaka/n/nf3aa0a193147

Gemini 4 Hydrogenの発表内容を、スペックと使いどころの観点で整理したnpakaさんの入門解説。Gemini 3.8 Flash比で最大2.5倍の高速化、100万トークンのコンテキスト窓、並列ツール実行とエラー自己修正といった要素を、短い分量で一通り押さえられる。API料金は入力100万トークンあたり1.50ドルと明記され、Antigravityのオーケストレーター機能で最上位のCarbonと組み合わせる構成にも触れる。発表の詳細より、まず全体像を素早く把握して自分の用途に合うか判断したい人向けの一本。

---

### Pathwaysとは？：大規模モデルのためのシングルコントローラー学習
**原題**: What is Pathways? Single-controller training for large models
**カテゴリー**: アーキテクチャ・設計
**URL**: https://developers.googleblog.com/what-is-pathways-single-controller-training-for-large-models/

Geminiの学習に使われてきた分散ランタイムPathwaysが、Google Cloudで一般提供となった。従来のSPMD方式はパイプライン並列やRLループのような非一様な処理でアクセラレータの待機が生じる、という課題を出発点に、単一のPythonクライアントから計算グラフを定義するシングルコントローラー方式を説明する。仮想デバイスによるハードウェア故障時の再マッピング、非同期ディスパッチ、中央スケジューラが要点。Rayは配置、Pathwaysはチップ上の実行最適化を担う補完関係と位置づける点は、基盤選定の参考になる。

---
## 5. MCPエコシステム

### MCPはなぜ復権したのか：CLIが支持された理由と、流れを変えた仕様変更
**カテゴリー**: アーキテクチャ・設計
**URL**: https://hiraoku.dev/blog/mcp-cli-cloud/

MCPは全ツール定義をモデルに渡すトークン消費やセッション管理の複雑さを批判され、一時はCLIに押されていた。本稿は、2026年7月28日版仕様のステートレス化（初期化手順の撤去、HTTPヘッダーによる操作識別）で、クラウドでの分散運用が容易になった点を軸に復権の理由を整理する。加えて、遅延読み込み（Progressive Tool Discovery）とコードによる結果加工が、CLIの「必要な分だけ読み、加工して返す」利点を埋めたと指摘する。ローカル作業は既存CLI、クラウドの複数サービス統合はリモートMCPという使い分けを判断する材料になる。

---

### MCPにおけるファイルアップロードとダウンロードの試験的な導入について
**原題**: Exploring File Uploads and Downloads in MCP
**URL**: https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/

大容量ファイルを扱うには、モデルが全データを読むか独自実装が必要だった。MCPメンテナーとGoogleのエンジニアによるワーキンググループは、拡張機能（io.modelcontextprotocol/files）のドラフトを公開した。JSON-RPCの外側でHTTPSにより直接転送し、ツール引数のx-mcp-fileでファイル処理をクライアントに委ねる。サーバーが署名付きURLを返すマルチラウンドトリップ方式で、SHA-256検証とユーザー承認も設計に含まれる。現在はプロトタイプ段階で、2026年末までの安定版を目指してフィードバックを募っている。

---

### MCPのより予測可能なリリースサイクルの導入
**原題**: A More Predictable Release Cycle for MCP
**URL**: https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/

MCPの仕様リリースは不定期だったが、毎年3月と9月の最終火曜日に行う固定スケジュールへ移行する。次回は2027年3月30日で、開発は8ヶ月前に始まり、2.5ヶ月前にソフトフリーズ、1.5ヶ月前にSDKベータ公開、1ヶ月前にハードフリーズと進む。新設のリリースマネージャーにはLuca Chang氏が就き、提案レビューとSDK実装を管理する。SDKやクライアントを実装する開発者にとって、仕様確定時期を逆算して計画を立てられるようになる点が実務上の要点だ。

---
## 6. エージェント対応Web・UI（agent-ready）

### 自サイトをAgent Readyにした実装記録
**カテゴリー**: ツール・実験
**URL**: https://www.tak-dcxi.com/article/make-website-agent-ready/

個人ブログのリニューアルに合わせ、AIエージェントが読み取りやすいサイトにした作業の記録。Astroの静的サイトを維持したまま、Cloudflare WorkersでAccept: text/markdownのコンテンツネゴシエーションを実装し、HTMLの代わりにMarkdownを返す。llms.txtの設置、robots.txtへのContent-Signal追記によるAI利用許諾の明示、JSON-LDの強化、プライバシーポリシー整備も行い、複数のエージェントチェッカーで高スコアを得た。チェッカー対策を含む手順の実例が揃っており、自分のサイトに同じ対応を入れたい人向けのチェックリストとして使える。

---

### AIエージェント向けにNext.jsからMarkdownを自動生成する「@affordances/md」
**原題**: Act Accordingly: Making Next.js Apps Readable to AI Agents
**カテゴリー**: ツール・実験
**URL**: https://www.vlt.io/blog/act-accordingly

人間向けに作られたUIはエージェントには解釈しづらく、vltはこれを「エージェントにおけるノーマン・ドア問題」と呼ぶ。同社が公開したNext.js向けプラグイン@affordances/mdは、SSRやストリーミングを含む既存のHTMLから構造化Markdownを生成し、Accept: text/markdownで返す。AgentMainやAgentSkipなどのコンポーネントで見せる情報を制御でき、認証とキャッシュも尊重する。初期ベンチマークではスクリーンショット型エージェントよりトークン消費が8.4倍少なく、速度は約2倍。ただし最適化は読み取りが中心で、操作側のプロトコルは研究段階にとどまる。

---

### Vercel Labs「UI SDK」：フレームワーク非依存の振る舞いライブラリ
**原題**: vercel-labs/ui: A library of behaviors for agents to build the next generation of user interfaces
**カテゴリー**: アーキテクチャ・設計
**URL**: https://github.com/vercel-labs/ui

AIエージェントにUIを書かせると、キーボード操作やフォーカス管理、ARIA属性が抜けやすい。UI SDKは、こうしたロジックを「振る舞い（Behaviors）」として@ui-sdk/coreに集約し、React、Vue、Svelte、Solid、Web Componentsにはアダプターで対応する。利用側は低レイヤーを意識せずPrimitiveを定義でき、アクセシビリティの担保をエージェントの出力精度に頼らずライブラリ側へ移している。エージェントにUI構築スキルを追加するCLIも付属する。現在はベータ版で、フレームワークごとの実装差をどこまで吸収できるかが採用判断の焦点になる。

---
## 7. 論考・研究・その他（独立トピック）

### 「AIができたら起こしてくれ」への10年分の回答
**原題**: Wake me up when AI can...
**URL**: https://stoppels.ch/2026/10/03/wake-me-up-when-ai-can.html

過去10年のHacker Newsにある「AIが〜できたら本物だ」という趣旨のコメント約800件を集め、約10万票の一般投票で達成度を判定したプロジェクトである。チューリングテスト合格、基本的なコード生成、要約といった初期のハードルは、ChatGPT前後でほぼ「達成済み」とされた。一方、シニアエンジニアの完全代替、配管・電気工事などの物理作業、P≠NP証明のような新理論の構築は「未達成」のままだ。能力が上がるたびに期待値が動くことを、投票結果でそのまま確認できる。

---

### 信頼できないAIエージェントを大規模にサンドボックス化する
**原題**: Sandboxing Untrusted AI Agents at Scale: Google Donates Agent Substrate and gVisor to the CNCF
**カテゴリー**: アーキテクチャ・設計
**URL**: https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html

エージェントは推論待ちのアイドルが長いのに、メモリやディスクの実行状態を保持し続ける。このため従来のKubernetes Podモデルではスケールしにくい。Googleの「Agent Substrate」は、状態を持つ「Actor」と計算資源の「Worker」を分離し、アイドル時にスナップショットを保存してリソースを解放する。復帰は500ミリ秒未満とされる。信頼できないコードはユーザ空間カーネルgVisorで隔離する。両技術はCNCFに寄贈され、エージェント基盤の標準化を狙う。

---

### AI生成物を拒否するOSSプロジェクトのカタログ
**原題**: Open Source Says No
**URL**: https://osssaysno.com/

コード、ドキュメント、Issue、翻訳を含むAI生成コンテンツの受け入れを拒否するOSSプロジェクトを集めたリソースである。yt-dlp、QEMU、Zig、Gentoo Linux、immichなど著名プロジェクトが並び、各プロジェクトの禁止ポリシーに直接リンクしている。背景にあるのは、質の低い「スロップ」と、法的・品質上のリスクへの警戒だ。GitHubリポジトリのURLを送れば追加を提案できる。自分の貢献先がAIをどう扱うか、PR前に確認する手がかりになる。

---

### 長いコンテキストは要らない：コンパクションとSSSM
**原題**: You don't need long context
**カテゴリー**: パフォーマンス・最適化
**URL**: https://arxiv.org/abs/2611.05306

コンテキスト長大化の流れに異を唱えるテクニカルレポートである。LLM推論では後半のトークン生成コストが初期の最大7倍に増えると定量的に示した。頻繁に要約・圧縮する「コンパクション」を使えば、広範な長文タスクで短いコンテキストを保ちつつ、精度はほぼ落ちない。複雑なソフトウェアエンジニアリングタスクでも、1コンテキストで1アクションを実行する形式で性能が維持された。ここから、長文に依存しない「セマンティック状態空間モデル（SSSM）」という設計概念を提唱している。

---

### Fable 5.2に物理モデリング音源を実装させる
**URL**: https://nowokay.hatenablog.com/entry/2026/11/13/101644

きしだ氏が、Fable 5.2に楽器の物理シミュレーションを実装させて検証した記録である。弦、ピアノ、金管、木管、ギター、ボーカルについて、弦の共鳴、唇のシミュレーション、擦弦ノイズなどの発音原理をコードで書かせ、音質を評価している。従来モデルと比べ、ソナタ形式やジャズのソロ回しといった作曲の構成力も高いという。拡散モデルによる音声生成と違い、奏法や構成を論理的に指定・編集できる点が肝だ。ピアノの共鳴や金管の倍音制御など、音響工学の知識を反映した対話の過程も読める。

---

### LLM時代の検索システムと推薦システム
**カテゴリー**: 教育・学習
**URL**: https://joisino.hatenablog.com/entry/searchrecbook

佐藤竜馬氏の新著『検索システム』『推薦システム』の発売に合わせ、LLMが両分野に与えた構造変化を論じた記事である。検索では長文脈対応が進み、RAGに加えて全文プロンプト（Context Stuffing）が現実的な選択肢になった。適合率と再現率のトレードオフに基づく設計が重要になる。推薦では、LLMの推論力で内容フィルタリングが飛躍的に向上し、データ不足で成り立たなかった小規模サービスや初期フェーズでも推薦を立ち上げられる。推薦理由の言語化といった新しい付加価値にも触れている。

---

### AIモデルは「女性・平和・安全保障」を知っているが、自分からは言わない
**原題**: AI Models Know What Women, Peace and Security Is. They Just Don't Bring It Up Unprompted.
**カテゴリー**: 批判的分析
**URL**: https://blog.cip.org/p/ai-models-know-what-women-peace-and

Collective Intelligence ProjectとOur Secure Futureが、国連安保理決議1325号の「女性・平和・安全保障（WPS）」原則をAIがどこまで守れるかを測る公開ベンチマークを発表した。GPT-5.6やGemini 3.1 Proなどの検証で、2つの問題が出た。明示的な指示がなければ分析からジェンダーの視点が消える「受動的な欠落」と、予算削減の圧力下でWPS関連の役割が真っ先に削られる「能動的な屈服」である。解決策として、専門家の知見に基づく評価基準、マルチエージェント検証、公共調達への要件組み込みを挙げている。

---

### Cyber Chaos Monkey：AIエージェントによる先制的セキュリティ対策
**原題**: Cyber Chaos Monkey: Staying ahead of security threats with AI agents
**カテゴリー**: セキュリティ・リスク
**URL**: https://shopify.engineering/cyber-chaos-monkey

Shopifyは、カオスエンジニアリングをセキュリティに応用したAIエージェント「Cyber Chaos Monkey」を導入した。ソースコード、インフラ構成、ログに触れられる「情報の非対称性」を使い、攻撃者より先に脆弱性を探す。構成は、仮説を立てるDiscoveryと、実際に攻撃を試すSandboxの2層である。攻撃を実行するExecutorを監視役のAI（Judge）がリアルタイムで見張り、違反があれば停止させる「二人組整合性（TPI）」を採る。数万件の試行で、障害を出さずに重要な脆弱性を数十件発見・対処したという。

---
## 8. その他の実践・論考

### Smolmaxxing: 超小型デバイスで巨大LLMを動かす最適化フレームワーク
**原題**: GitHub - hyperionaidev/smolmaxxing: maxxing the ability to run different LLMs on the smallest devices possible
**カテゴリー**: パフォーマンス・最適化
**URL**: https://github.com/hyperionaidev/smolmaxxing/

1GB RAMのTV Boxや2013年製iPad Airのような、本来は大きなモデルを載せられない端末でLLMを動かすためのllama.cppパッチ。チップセット特化の1ビット等のカスタムカーネル、使用頻度の低い語彙の削除、MoEで必要なエキスパートだけをフラッシュから読み出すページング、ストレージ速度を活かすストリーミングエンジンの4本柱で構成される。空きメモリ3GBのAndroid端末で80Bクラスのモデルを動かした例が示されている。エッジ推論の下限に挑む実験として読む価値がある。

---

### GoogleのAIエージェント・サンドボックスをFirecrackerで再現・計測
**原題**: Google Described Its Agent Sandbox. I Built One with Firecracker and Measured It
**カテゴリー**: アーキテクチャ・設計
**URL**: https://antonau.tech/posts/2026/11/agents-microvm-firecracker/

Google Cloudが示したAgent Compute Engineの設計(microVM隔離、スナップショット起動、NIC排除)を、約2,200行のGoとFirecrackerで再現した検証記事。物理環境ではスナップショット復元が25msでコールドブートの約26倍速く、アイドルVM 64台を1台あたり約3MBで維持できた。ツール呼び出し後の「思考中」を検知して自動休止する仕組みや、vsock経由のホストプロキシによる認証情報管理も扱う。Mac M4のNested仮想化では12台以上で応答不能になるなど、限界の数値も率直に記録されている。

---

### シネフィルおじさん便
**カテゴリー**: ツール・実験
**URL**: https://claude.ai/artifact/5rGviSNATjR6aF6A54XALj

Claude Artifactsで作られた、映画好きのジョークサービス。ユーザーが「生涯の3本」を選ぶと、映画に一家言ある「うるさいおじさん」風のキャラクターが返信を生成する。注目点は、その場で遊べるだけでなく、同じペルソナをChatGPTやGeminiに移植するためのプロンプト自体を配布していることだ。特定プラットフォームに縛られないキャラクターAIの共有方法と、軽量なLLM活用UXの小さな実例として、息抜きがてら覗いてみる程度の一本。

---

### 1Password for Agentsがパスワードとプライバシーを保護する仕組み
**原題**: How 1Password for Agents Protects Passwords and Privacy | 1Password
**カテゴリー**: セキュリティ・リスク
**URL**: https://1password.com/blog/1password-for-agents-security-privacy

旅行予約などをエージェントに任せるとログインが必要になるが、プロンプトへのパスワード入力は漏洩リスクを伴う。1Password for Agentsは、ユーザーが承認した場合にのみ、ブラウザ拡張が対象サイトへ認証情報を直接入力する方式をとる。このため、エージェントのログやコンテキストに平文パスワードが残らない。接続にはユーザーのデバイスで生成した統合キーを使い、1Password側でもデータを復号できないゼロ知識の原則を維持するという。エージェントに資格情報を渡さない設計の一例として、公式の説明を確認できる。

---

### Herdr.appとhcの上でClaude Codeの司令塔を回している
**URL**: https://zenn.dev/hoshinotsuyoshi/articles/c994c29833f36c

Herdr.appとherdr-core(hc)を基盤に、ユーザーが直接やり取りするエージェントを「司令塔」の1体だけに絞る運用を紹介する実践記事。子エージェントへのタスク割り当てと進捗報告の集約を司令塔に任せることで、マルチエージェント運用の管理負担を減らす。バックグラウンドでの無駄な返答を避ける「hc wait」の条件分岐や、自作ツールsession-grepによるセッションログ横断検索でのコンテキスト引き継ぎなど、具体的な工夫が並ぶ。複数エージェントの並走に疲れている人向けの運用例だ。

---

### 超知能による人類滅亡のシナリオと「道具の自然化」
**カテゴリー**: 批判的分析
**URL**: https://note.com/ochyai/n/n7a1dbd68c8fa

落合陽一氏が、超知能が人類を滅ぼす、または無力化する経路を6つ(道具的収束、欺く整合、知能の爆発、人間による悪用、構造的リスク、緩やかな無力化)に整理し、自身の「デジタルネイチャー」思想との整合を問い直したエッセイ。焦点は第6の緩やかな無力化で、かつて肯定的に描いた「計算機が自然に溶け込み違和感が消える状態」が、AI安全性の視点では主導権喪失と同義になりうると自己批判する。結論は断定ではなく、恵みと喪失が表裏一体の「遷移」の可能性として提示される。

---

### OpenAI Agents SDKを使い、必要なToolだけを持つブラウザエージェントを作る
**URL**: https://www.mitsue.co.jp/knowledge/blog/x-tech/202611/12_1352.html

CursorやClaude Codeのような汎用エージェントは多機能な反面、予期せぬ操作を防ぐ権限管理が難しい。この記事は、OpenAI Agents SDKの@function_toolでPlaywrightのURLを開く、スナップショット取得、クリック、入力といった操作だけをツール化し、実行可能な範囲をコードで限定する方法を示す。特定ホスト名以外へのアクセスをプログラム側で拒否する検証の実装例も載る。AIの判断と従来型の制約を組み合わせる、権限を絞った自作エージェントの入門として読める。

---

### 仕事の最前線:AIがフリーランスの仕事に与える影響
**カテゴリー**: ビジネス・戦略
**URL**: https://openai.com/ja-JP/index/ai-effect-on-freelance-work/

OpenAIとUpworkが、ChatGPTの利用データとUpworkの数百万件の案件募集を分析した共同レポート。文章作成のようなAIが得意な単純タスクの需要は一部で減少する一方、動画制作やマーケティング自動化など、AIを使いつつ高度な専門性を組み合わせる案件では需要と予算が伸びている。AI関連案件は非AI案件より固定報酬の予算が大きく、必要なタスクの種類も約45%多い。仕事の消失だけでなく、複数スキルの統合へ価値が移る傾向を示す、OpenAI側の調査である点も踏まえて読みたい。

---

### 責任あるAIインフラ整備の新たな基準
**カテゴリー**: ビジネス・戦略
**URL**: https://openai.com/ja-JP/index/setting-new-standard-responsible-ai-infrastructure/

OpenAIが、大規模AIコンピューティングキャンパス建設に向けた「地域社会との協約」と政策提言を公表した。早期からの住民対話と年次報告、不必要なNDAの廃止、電力・送電網の増強費用の事業者全額負担と財務保証、節水型冷却、現地の労組や教育機関と連携した職業訓練などを約束する。政策立案者には、大口電力利用者の費用負担の義務化や税制優遇の透明性確保も求める。ジョージア州とオハイオ州の事例をモデルとする、事業者自身による基準の宣言である。

---
## 編集後記

メインジャーナルが「今週の主役」を扱うのに対し、Annexは「主役の陰で進んでいる実務とニッチ」を映す。今週で言えば、フロンティアモデルの華やかな発表の裏で、社内エージェント基盤を自力で組み上げた記録や、TV Boxや旧スマホのような低スペック機でローカルLLMを動かす執念、そして「活動量は増えたが成果は増えたのか」を問う冷静な調査こそが、現場の手触りを伝えてくれる。

カタログ形式は、こうしたB面を素早く見渡すために選んでいる。各エントリは「読むべきか」を80〜120語で判断できるように書かれており、気になった角度だけを深掘りしてもらえれば十分だ。超知能による人類の行方をめぐる論考、AI生成物を拒むOSSの姿勢、フリーランス市場へのAIの影響——相互に異なる視点が同居しているのも、今週の思考の幅をそのまま示している。

主役の発表はいずれ古くなるが、こうした実装の工夫や批判的な問いは、次に自分が手を動かすときの参照点として長く効く。興味の赴くままに拾い読みしてほしい。

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
