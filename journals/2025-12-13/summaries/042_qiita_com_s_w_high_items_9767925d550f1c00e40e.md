## 自律型ソフトウェア開発 AI エージェントを Azure で構築する

https://qiita.com/s_w_high/items/9767925d550f1c00e40e

NRIのエンジニアが、AWS上の自律型ソフトウェア開発AIエージェント「remote-swe-agents」をAzureへ移行した奮闘記を公開し、アーキテクチャの比較、Bicepによる基盤構築、SDKの置き換えといった技術的課題と解決策を詳細に解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[AIエージェント, クラウド移行, Azure, Bicep, GitHub連携]]

この記事は、AWSで公開されている完全自律型ソフトウェア開発AIエージェント「remote-swe-agents」を、Azure上で再構築する詳細な過程を報告しています。著者は、チャットでの指示（例：「このバグを修正して」）に基づき、AIエージェントがGitHubのコードを読み込み、修正し、プルリクエストまで作成するremote-swe-agentsの機能に感銘を受け、これを自身が慣れ親しんだAzure環境で実現しようと挑戦しました。この取り組みは、AWSからAzureへのクラウド移行における具体的な課題と解決策を提示する点で、Webアプリケーションエンジニアにとって非常に重要です。

移行の主要なポイントは、AWSの各サービスをAzureの同等サービスにマッピングすることにありました。具体的には、フロントエンドとAPIはLambdaからAzure App Service（Dockerコンテナ）、認証はCognitoからMicrosoft Entra ID、データベースはDynamoDBからCosmos DB for NoSQL、ストレージはS3からBlob Storage、LLMはBedrockからAzure OpenAI Service（Microsoft Foundry上）、リアルタイムイベント配信はEventBridgeからAzure Web PubSub、VM管理はEC2からAzure Virtual Machines、VMイメージ管理はEC2 AMIからCompute Gallery、VMイメージビルドはEC2 Image BuilderからAzure Image Builderへと置き換えられました。

基盤構築にはBicepが全面的に採用され、VNet統合によるセキュリティ強化、Key Vaultからのシークレット注入、App Serviceへのコンテナデプロイ方法などが詳細に解説されています。特に、AIエージェントが動作するWorker環境については、Azure Image BuilderでカスタムVMイメージを作成し、起動時にBlob StorageからWorkerのソースコードをダウンロード・実行する仕組みが構築されました。これにより、VMイメージの柔軟な管理とWorkerコードの容易な更新を実現しています。また、WebAppとWorker間のリアルタイム通信にはAzure Web PubSubが活用され、特定のWorkerにメッセージを配信するグループ機能が実装されています。

アプリケーション実装においては、AWS SDKからAzure SDKへの置き換えが主要な作業となりました。Cosmos DBクライアントの実装では、マネージドID認証の利用やDynamoDB互換関数の実装により、コード変更を最小限に抑えつつAzureのサービスに適合させています。認証セッション情報のCosmos DBへの保存は、トークンが大きすぎてCookieに入らないという実用的な課題を解決するために採用されました。最終的に、テストリポジトリのIssueを指示通りに修正し、Pull Requestが自動で作成される様子が公開され、その確かな動作が確認されています。

著者は、一見似た機能を持つサービスであっても、使い勝手やSDKの違いから多くの部分を一から作り直す必要があり、予想以上の困難があったと述べています。しかし、この奮闘を通じて、Azure環境で同様の自律型AI開発エージェントを構築する具体的な方法と、そのプロセスで直面する技術的課題への解決策が提示されており、Webアプリケーションエンジニアにとって、クラウドを跨いだAIエージェント開発の参考に、非常に価値のある記事となっています。