## Web APIをMCP化してAgent-readyにした話

https://developers.cyberagent.co.jp/blog/archives/60687/

CyberAgentのAI事業本部がFastMCPを活用し、既存の複数のWeb APIをAIエージェントから容易に利用可能なMCP Gatewayとして統合した方法を解説します。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Web API, AIエージェント, FastMCP, OpenAPI, MCP Gateway]]

この記事は、CyberAgentのAI事業本部がレスポンシブ検索広告の品質向上を目指し、既存のWeb API群をAIエージェントから容易に利用可能にする「Agent-ready」な状態にした取り組みを紹介しています。従来、AIエージェントから個別のAPIを呼び出す場合、エージェントごとにロジックの実装が必要で、API仕様変更時の修正コストも大きいという課題がありました。

この課題を解決するため、同社はModel Context Protocol (MCP) サーバーの導入を決定し、複数のAPIサーバーのGatewayとなるMCPサーバー（MCP Gateway）を構築するアプローチを採用しました。これにより、個別のAPI呼び出しロジックが不要となり、API仕様変更時の修正もMCPサーバー側だけで完結できるメリットを享受します。通信オーバーヘッドの増加はあるものの、開発・運用コスト削減を優先したと著者は述べています。

MCP Gatewayの構築には、Python向けフレームワークであるFastMCPが用いられました。FastMCPの主要な機能は二つです。一つは「OpenAPI統合機能」で、OpenAPI仕様に準拠した既存のAPIサーバーから自動的にMCPサーバーを構築します。これにより、手動でのMCPツール・リソース構築が不要になります。もう一つは「Server Composition機能」で、複数のMCPサーバーを一つにまとめることを可能にします。特に`mount`機能を利用することで、メインサーバーがリクエストをサブサーバーに委譲するGateway形式を実現し、複数の既存APIを一元的にエージェントから扱えるようにしました。

このMCP GatewayをAIエージェントに登録することで、広告文の生成と品質判定のプロセスをイテレーティブに繰り返し、より高品質な広告文の生成が期待できると著者は述べています。Amazon Bedrock AgentCore Gatewayの着想を得つつ、自社で開発した経緯も触れています。ただし、OpenAPI Specからツール・リソースがエンドポイント単位で自動生成されるため、エンドポイント数が多いとLLMのコンテキストを圧迫する可能性があり、将来的な課題としてAnthropicのtool searchのようなツールの活用を提唱しています。