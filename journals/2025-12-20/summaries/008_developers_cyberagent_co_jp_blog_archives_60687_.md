## Web APIをMCP化してAgent-readyにした話

https://developers.cyberagent.co.jp/blog/archives/60687/

サイバーエージェントのAI事業本部は、既存のOpenAPI準拠Web API群をAIエージェントから容易に利用可能な「Agent-ready」状態にするため、FastMCPフレームワークを活用してMCP Gatewayを構築しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Web API, AIエージェント, FastMCP, OpenAPI, MCP Gateway]]

サイバーエージェントのAI事業本部は、レスポンシブ検索広告の品質向上を目指し、広告文の品質判定APIなど複数のWeb APIをAIエージェントから連携可能にする「Agent-ready」化に取り組みました。既存のAPIをAIエージェントが直接呼び出す場合、各エージェントでの個別ロジック実装やAPI仕様変更時のメンテナンスコストが課題となるため、MCP（Model Context Protocol）サーバーの導入が決定されました。

チームは、個別のAPIごとにMCPサーバーを開発するのではなく、複数のAPIサーバーの前段にGatewayの役割を持つMCPサーバー（MCP Gateway）を配置するパターンを選択しました。この決定は、MCPサーバーの開発・運用コストを抑えたいという動機と、通信オーバーヘッドがユースケースにおいて許容範囲内であったためです。

MCP Gatewayの構築には、Python向けのフレームワークであるFastMCPが活用されました。具体的には、OpenAPI準拠の既存APIからMCPサーバーを自動生成する「OpenAPI統合機能」と、複数のMCPサーバーを一つにまとめる「Server Composition機能」の`mount`方式を組み合わせることで実現されました。このアプローチにより、手動でのMCPツールやリソース構築の手間が省け、既存のWeb APIを迅速にMCP化し、AIエージェントから一元的に利用できるようになります。

このGatewayをClaude CodeなどのAIエージェントに登録するだけで、複数のWeb APIが利用可能となり、広告文の生成と品質判定のイテレーションを効率的に回し、広告効果の最大化が期待されます。一方で、OpenAPI Specから自動生成されるMCPツール・リソースがエンドポイント単位であるため、エンドポイント数が非常に多い場合にはLLMのコンテキストを圧迫する可能性が注意点として挙げられています。著者は、Anthropic社のtool searchのような新技術が、将来的にこの課題を解決する可能性を示唆しています。