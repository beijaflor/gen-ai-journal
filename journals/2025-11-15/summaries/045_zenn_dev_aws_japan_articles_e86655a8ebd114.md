## CognitoとAgentCore GatewayでMCPサーバーにOAuth認証をつけよう

https://zenn.dev/aws_japan/articles/e86655a8ebd114

AWSのAI/ML Specialist SAであるKondo氏が、Model Context Protocol (MCP) サーバーにOAuth認証を付与する方法を、Dynamic Client Registration (DCR) なしでAWS CognitoとAgentCore Gatewayを用いて実装し、その詳細な手順と認証フローを解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, Model Context Protocol (MCP), OAuth認証, AWS Cognito, AWS AgentCore Gateway]]

本記事では、リモートMCPサーバーの普及に伴い推奨されるOAuthベースの認証を、AWSのマネージドサービスを活用して実装する方法を解説しています。従来のstdio方式に比べ短命なトークンを扱うOAuthは、安全性が高いと著者は指摘します。特にウェブ上で情報が少ないDCR（Dynamic Client Registration）なしのケースに焦点を当て、その実装課題と解決策を示しています。

MCPの認可仕様（2025-06-18版）に基づき、MCPサーバーと認可サーバーがそれぞれ持つべき役割を詳細に整理。クライアントとMCPサーバー間での認可サーバー検出、クライアントと認可サーバー間でのメタデータ検出、そしてOAuth 2.1のAuthorization Code Grantフロー（Resource Indicator対応）といった各ステップの挙動を明確にしています。

具体的な実装では、認可サーバーとしてAmazon Cognito、MCPサーバーとしてAWS AgentCore Gatewayを利用。Cognitoではユーザープール、アプリクライアント、マネージドログイン（RFC8707対応）を設定し、AgentCore Gatewayの認証設定でCognitoユーザープールを指定します。また、RFC8707に対応するため、CognitoのリソースサーバーにGatewayのエンドポイントを追加する手順も詳述されています。

著者は、自作のPythonクライアントコードでの接続成功例を示し、さらに既存のエージェント製品（Claude Code、Claude Desktop、VSCode、ChatGPTなど）をクライアントとして試した結果、DCR非対応が原因で多くが接続に失敗したことを報告。唯一、Amazon Quick Suiteが正常に接続できた事例として挙げられています。この検証結果は、DCRなしでのMCP OAuth認証を試みる開発者にとって重要な知見となります。

本記事は、リモートMCPサーバーのセキュリティ強化に関心のある開発者向けに、具体的な実装パスと考慮すべき点、特にDCRの有無による既存ツールとの互換性問題について、実践的なガイダンスを提供することを目的としています。