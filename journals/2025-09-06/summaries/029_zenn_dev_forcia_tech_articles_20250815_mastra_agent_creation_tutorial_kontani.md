## Mastra × MCPでドキュメント作成を自動化してみる

https://zenn.dev/forcia_tech/articles/20250815_mastra_agent_creation_tutorial_kontani

TypeScriptのAIエージェントフレームワークMastraを用いて、Slackスレッドや関連URLから情報を収集し、構造化された技術文書を自動生成する具体的なワークフローと実装手法を解説する。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Mastra, AIエージェントフレームワーク, Model Context Protocol (MCP), ドキュメント自動生成, Slack連携]]

Webアプリケーションエンジニアが直面する、SlackやJira、GitHubなど多岐にわたる情報源から散逸した情報を集め、ドキュメントを作成する労力は大きいという課題に対し、本記事はTypeScript製のAIエージェントフレームワーク「Mastra」を活用した自動化手法を詳述しています。Mastraは単なるLLMラッパーではなく、RAGや複雑なAIエージェントを構築するための多様な機能を提供します。

具体的な実装では、まずシンプルなAgent定義から始め、Zodスキーマを用いた出力の型制御を提示。次に、LLMの能力を拡張する「Model Context Protocol（MCP）」の概念を説明し、GitHub公式MCPサーバーや社内製esa MCPサーバーをAgentに組み込む方法を紹介します。特に重要な点として、アーカイブされたSlack公式MCPサーバーの代替として、カスタム関数`getSlackThreadMessage()`を`createTool()`でラップし、Slackスレッドの内容を直接取得する手法を解説。これにより、特定の外部連携要件にも柔軟に対応できることが示されています。

さらに、これらのAgentとツールを組み合わせ、`createWorkflow()`メソッドを使って複数のステップを連結する複雑なワークフローを構築します。このワークフローは、Slack URLからメッセージを取得し、メッセージ内のURLから関連情報を抽出し、ユーザーの要望に応じたドキュメントテンプレートを生成し、最終的にSlackメッセージ、抽出されたコンテキスト情報、テンプレートを統合して詳細なMarkdown形式の技術文書を出力するプロセスを自動化します。特に、`then()`による逐次処理と`parallel()`による並列処理を組み合わせることで、効率的な情報収集と文書生成を実現しています。このアプローチは、断片的な情報から正確かつ構造化されたドキュメントを迅速に生成し、開発チームの生産性を大幅に向上させる可能性を秘めています。
