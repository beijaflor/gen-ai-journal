## ChatGPT, Claude, & Gemini security scanning with Cloudflare CASB

https://blog.cloudflare.com/casb-ai-integrations/

Cloudflareは、企業が生成AIを安全に利用できるよう、ChatGPT、Claude、Geminiに対しAPIベースのCASB統合によるセキュリティスキャン機能の提供を開始しました。

**Content Type**: News & Announcements

**Scores**: Signal:5/5 | Depth:3/5 | Unique:2/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 78/100 | **Annex Potential**: 71/100 | **Overall**: 72/100

**Topics**: [[CASB, Generative AI Security, Data Loss Prevention, AI Governance, Zero Trust Architecture]]

Cloudflareは、企業の生成AI利用を安全に進めるため、Cloudflare One向けにAPIベースのCASB機能がOpenAI ChatGPT、Anthropic Claude、Google Geminiに対応したことを発表しました。これにより、ITおよびセキュリティチームは、これらのAIツールのセキュリティ体制評価、データ損失防止（DLP）検知、データ公開・共有の監視、コンプライアンスリスクの特定などを、ユーザーデバイスにソフトウェアをインストールすることなく実施可能となります。企業での生成AI利用が急増する中、データ漏洩や不正利用、設定ミスといった新たなセキュリティ課題が顕在化しており、本統合はその重要な解決策を提供します。

Cloudflareのソリューションは、APIベースCASBによるAIツール内の静止データ可視化と、Cloudflare Gatewayのインライン制御によるプロンプト制御、シャドウAI特定、DLPポリシー適用を組み合わせることで、GenAI利用に対する統一的な制御プレーンを提供します。ウェブアプリケーション開発者にとって、自社サービスにおけるAI活用推進時、社内データ取り扱いに関するセキュリティポリシーがどう適用され、保護されるかを理解する上で非常に重要な情報です。

具体的な機能として、ChatGPT向けにはActionsやCode Execution機能の有効化状況、GPT Storeなどで公開されたチャットやGPTの外部共有状況、APIキー管理、添付ファイルからの機密データ（資格情報、ソースコードなど）DLP検知が可能です。ClaudeではAPIキー管理とアップロードファイル内の機密データDLP検知を重視。Geminiについては、Google Workspaceアドオンという性質から、多要素認証（MFA）未設定ユーザーの特定やAI Ultraライセンスを持つ停止済みアカウントの検出など、IDとライセンスの衛生管理に特化しています。これらの新機能は、組織が生産的に生成AIを活用しつつ、企業データとネットワークのセキュリティおよびプライバシーを確実に保護するための強固な基盤となります。