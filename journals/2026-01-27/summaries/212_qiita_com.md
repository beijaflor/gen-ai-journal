## AgentCoreでツールを直書きするのをやめて、Gateway＋Lambdaにした理由

https://qiita.com/Yoshi1001/items/7b5063290ac921cbe3ef

Amazon Bedrock AgentCoreのエージェント開発において、ツール実装をスクリプトから切り離し、AWS LambdaとGatewayを用いたMCP互換形式へ移行することで運用の柔軟性を高める手法を提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 79/100 | **Annex Potential**: 74/100 | **Overall**: 80/100

**Topics**: [[Amazon Bedrock, AgentCore, AWS Lambda, MCP (Model Context Protocol), AIエージェント]]

Amazon Bedrock **AgentCore**（旧Strands）を用いたAIエージェント開発において、ツールの実装をエージェントのスクリプト内に直書きする構成から、**AWS Lambda**と**AgentCore Gateway**を組み合わせた疎結合なアーキテクチャへと移行する実践的な手法を解説している。従来の手法では、ツールの追加や修正のたびにエージェント全体のビルド・デプロイが必要であり、実装のミスがエージェント全体を停止させるリスクがあった。

本書では、各ツールを個別のLambda関数として切り出し、**Amazon Bedrock AgentCore Gateway**を通じて**MCP (Model Context Protocol)** 互換ツールとして登録するワークフローを提案している。これにより、エージェント側は`mcp_client`を通じて動的にツールを読み込むだけで済み、エージェント本体を再デプロイすることなくツールの拡張やメンテナンスが可能になる。また、依存関係の多い**Playwright**を用いたスクレイピング処理を**ECR**ベースのLambdaに分離する手法など、コンテナ化による実行環境の最適化についても触れている。Bedrockを用いたAIエージェントを実運用に乗せたい開発者にとって、メンテナンス性と拡張性を両立させるための有益な設計パターンである。

**Bedrock AgentCore**で実用的なAIエージェントを構築・運用しており、ツールの管理コストや実行環境の依存関係に課題を感じているエンジニアに推奨する。