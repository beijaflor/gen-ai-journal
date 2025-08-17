## AWS LambdaでRemote MCPをほぼ無料でホスティングする

https://zenn.dev/zhizhiarv/articles/host-remote-mcp-on-lambda

開発者は、AWS LambdaとDynamoDBの無料枠を最大限に活用し、Claudeのパーソナルな記憶機能（MCP）をデバイス間で一貫して利用可能なリモートサービスとして構築できます。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 78/100 | **Annex Potential**: 76/100 | **Overall**: 80/100

**Topics**: [[AWS Lambda, Serverless, Claude, Memory Context Protocol, DynamoDB]]

Claudeの応答にパーソナルな記憶機能を持たせるMemory Context Protocol (MCP) を、AWS Lambdaでリモート化する手法を解説する記事です。筆者は、当初ローカルで運用していたMCPを、Claude MobileがリモートMCPに対応したことを受け、サーバーレスアーキテクチャであるLambdaに移行しました。この選択の最大の利点は、LambdaとDynamoDBの永続的な無料枠を活用することで、個人の利用範囲であればほぼコストをかけずにMCPを運用できる点にあります。

技術的な核心は、AWS公式の`mcp_lambda_handler`ライブラリの利用です。この記事では、ローカルMCPで用いたFastMCPとのアーキテクチャ上の違いを詳細に解説しています。FastMCPが常駐HTTPサーバーを前提とするのに対し、`mcp_lambda_handler`はLambda特有のイベント形式に最適化されており、Lambda Function URLと連携することで、軽量かつイベント駆動でのMCP通信を可能にします。これにより、余計なレイヤーを追加することなく、必要な時だけ実行される効率的なリモートMCPを構築できます。

この手法は、ウェブアプリケーションエンジニアにとって重要な示唆を与えます。第一に、AIアシスタントのパーソナライゼーションを、コスト効率良く実現できる具体的な方法を提示しています。ユーザー固有の記憶をAIに持たせることで、より自然で個別化された対話体験を提供できるようになります。第二に、サーバーレス技術と無料枠を組み合わせることで、高度なAI機能を個人や小規模チームでも容易に試せる環境が手に入ります。これにより、運用コストや手間を最小限に抑えながら、デスクトップ、ウェブ、モバイルといった複数デバイス間で一貫したAI体験を提供できる点が大きなメリットです。