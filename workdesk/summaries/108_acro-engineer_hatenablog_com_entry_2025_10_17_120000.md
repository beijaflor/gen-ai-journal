## Amazon Bedrock AgentCore で Lambda でAIエージェントを開発してみた（MCPで内部連携あり）

https://acro-engineer.hatenablog.com/entry/2025/10/17/120000

Amazon Bedrock AgentCoreの一般公開を受け、この記事はLambda関数と外部APIをMCPツールとして統合し、堅牢かつ多機能なAIエージェントを効率的に開発する実践的な方法を示す。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[Amazon Bedrock AgentCore, AIエージェント開発, Lambda, ツール連携, AWS]]

2025年10月13日に一般公開されたAmazon Bedrock AgentCoreは、AIエージェントの本格運用を支えるAWSの新しいサービス群です。本記事は、このAgentCoreの主要コンポーネントであるRuntime、Gateway、Identityを活用し、既存のLambda関数と外部API（Tavily）をMCP（Multi-Component Protocol）ツールとして統合するAIエージェントの開発手順を詳細に解説しています。

ウェブアプリケーションエンジニアにとって重要なのは、AgentCore Gatewayを利用することで、既存のAPIやLambda関数といった社内資産をAIエージェントの機能として容易に組み込める点です。これにより、エージェントの機能範囲を拡張しつつ、新規開発コストを抑え、さらにGatewayが認証・認可を一元管理するため、ツールごとのセキュリティ対策実装が不要となり、セキュリティリスクを大幅に軽減できるという大きなメリットがあります。

具体的な検証アプリケーションとして、「Tavilyで調べた内容のサマリをS3に保存する問い合わせエージェント」が構築されています。実装プロセスでは、Lambda関数をAgentCore GatewayのターゲットとしてMCPツールスキーマ定義と共にデプロイする方法、Tavily APIキーをAgentCore Identityで安全に管理する方法、そしてこれらを統合するAgentCore Gatewayの作成と、AgentCore Runtimeでのエージェントのデプロイまでがステップバイステップで説明されます。提供されたPythonコードと設定手順は、AgentCoreの認証フローやツール呼び出しの仕組みを具体的に理解するために非常に有用です。

最終的に、エージェントはGateway経由でTavily検索とS3ファイル保存（Lambda）を自律的に使い分け、ユーザーからの問い合わせに対して最新情報を収集し、要約してS3に保存し、共有リンクを生成する一連の処理を正常に実行できることが実証されました。著者は、AgentCoreが統合的な接続・認証・スケール運用を担うことで、実務での多機能AIエージェント開発がより便利になると結論付けており、今後のAIを活用したシステム開発において、既存資産を活かしつつセキュアでスケーラブルなエージェントを構築する上で不可欠な知見を提供しています。