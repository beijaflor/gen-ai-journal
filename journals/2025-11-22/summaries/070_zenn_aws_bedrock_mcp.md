## Bedrock AgentCore で Remote MCP サーバーをホストする2つの方法の徹底検証

https://zenn.dev/aws_japan/articles/001-bedrock-agentcore-remote-mcp

AWS Bedrock AgentCoreを活用したRemote MCPサーバーのホスティング手法として、AgentCore RuntimeとAgentCore Gateway + Lambdaの2つを詳細に比較検証し、それぞれの特性と適切なユースケースを明らかにします。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[AWS Bedrock, AgentCore, Remote MCP, Lambda, CDK, Agent Orchestration]]

本記事は、AIエージェントと外部システムを接続するプロトコルであるModel Context Protocol (MCP) を、AWS Bedrock AgentCore上でRemote MCPサーバーとしてホストする2つの主要なアプローチを徹底的に検証しています。対象となるのは、(1) AgentCore Runtimeでホストする方法と、(2) AgentCore GatewayとLambdaを組み合わせてホストする方法です。筆者はAWS CDKを用いて両手法の具体的な実装例を提示し、開発・運用の容易性、実行環境のスペック、運用コスト、レイテンシーという4つの観点から比較を行っています。

検証の結果、以下の特性が明らかになりました。

1.  **開発・運用の容易性**:
    *   **AgentCore Runtime**は、MCPサーバーのロジックをコンテナイメージとしてデプロイするため、新規開発や頻繁な修正が必要な場合に、実装と説明が一体化しており効率的です。ローカルでの動作確認も容易です。
    *   **AgentCore Gateway + Lambda**は、Toolの実装（Lambda）とToolの説明（AgentCore Gateway TargetのInline Schema）が分離しているため、開発中の修正やテストのたびに両方のリソースを管理・デプロイする必要があり、効率が低下します。ただし、既存のLambda関数をToolとして再利用する場合には適しています。

2.  **実行環境の仕様**:
    *   **AgentCore Runtime**は、入出力ペイロードサイズが100MB、メモリ8GB、実行時間がストリーミングで最大60分と、Lambdaよりも柔軟な設定が可能で、画像分析や長時間の調査タスクなど、リソース集約的な処理に適しています。
    *   **Lambda**は、CPUスペックが最大6vCPUと高い一方で、ペイロードサイズが6MB、実行時間15分という制約があり、用途が限定されます。

3.  **運用コスト**: 両手法間で大きな差はなく、コスト削減の観点ではどちらを選んでも問題ないという結論に至っています。

4.  **レイテンシー**:
    *   **AgentCore Gateway + Lambda**は、AgentCore Runtimeと比較して約2倍の低レイテンシー（全体の実行時間で約1700ms対3600ms）を実現しています。これは、GatewayがToolの定義をキャッシュし、Lambdaを直接呼び出すため、MCPサーバー自体の起動や初期化が不要なことによるものです。
    *   **AgentCore Runtime**は、仮想環境上でのMCPサーバー起動や処理性能がボトルネックとなり、レイテンシーが高くなる傾向が見られました。

結論として筆者は、MCPサーバーを新規開発し、柔軟な実行環境が求められる場合は**AgentCore Runtime**を、既存のLambda関数をToolとして活用したい場合や、極限まで低レイテンシーが求められる場合は**AgentCore Gateway + Lambda**を選択すべきだと提言しています。さらに、AgentCore Gatewayが提供する認証の一元化やSemantic Searchなどのメリットも考慮し、両者の使い分けや併用が重要であると強調しています。