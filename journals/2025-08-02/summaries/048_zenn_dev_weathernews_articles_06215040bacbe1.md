## FastMCPとOpen API Specification を使った天気予報Remote MCP Serverの実装

https://zenn.dev/weathernews/articles/06215040bacbe1

ウェザーニューズは、FastMCPとOpenAPI Specificationを活用し、既存の気象APIをLLM/AIエージェント向けのRemote MCP Serverとして**公開しました**。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 79/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Model Context Protocol, FastMCP, OpenAPI Specification, LLM/AI Agent Integration, API開発]]

ウェザーニューズは、LLMやAIエージェントが自社の気象データに標準化された方法でアクセスできる環境を構築するため、既存の気象APIを「Remote MCP (Model Context Protocol) Server」として実装しました。このプロジェクトでは、OpenAPI Specificationで定義された既存のAPI仕様とFastMCPを組み合わせることで、MCP Serverを短期間かつ低コストで開発できた点が重要です。

特に注目すべきは、OpenAPI SpecificationをFastMCPのインスタンス定義に直接利用することで、tool定義の手間を省き、既存資産を最大限に活用している点です。認証面では、API GatewayによるMCP Server自体の認証に加え、内部で呼び出すREST APIへの認証情報を透過的に引き渡すため、`httpx.AsyncClient`を継承したカスタムクライアントとミドルウェアを実装している点が技術的な深みを示しています。これにより、エージェントが利用するAPIキーをMCP Server内部のAPI呼び出しにも適用し、セキュアなデータ連携を実現しています。

インフラはAWS Lambda, API Gateway, CloudFrontを活用し、高可用性とスケーラビリティを確保しています。提供される「Tools」は緯度経度に基づく天気予報を、そして「Resources」は天気表現コードとその意味を定義し、エージェントが天気データを正確に解釈できるようにしています。

本実装は、Claude Desktop、VSCodeのGitHub Copilot Agent Mode、LangChain/LangGraphなどの多様なMCPクライアントからの利用例を通して、実用的な価値を明確に示しています。「海浜幕張の天気は？」といった自然言語での問いかけに対し、エージェントがMCP Server経由で気象データを取得し、適切な回答やグラフ生成、データ解析まで行うことが可能になります。これは、企業が持つ専門データをAIエージェントに活用させるための現実的かつ効率的なアプローチであり、開発者は複雑なAPIの詳細を意識することなく、AIアプリケーション開発に注力できるようになります。既存のAPI資産をAIエージェントエコシステムに組み込む際のベストプラクティスを示唆しています。