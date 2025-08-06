## Mastraを参考にドキュメントMCPサーバーを作ってみた

https://zenn.dev/himara2/articles/c2835dd77bd743

LLMが最新かつ正確なドキュメントを参照する際の課題に対し、特定のサービス（microCMS）の公式ドキュメントを直接LLMに提供する「Document MCPサーバー」の実装方法と効果を詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 88/100

**Topics**: [[MCP Server, LLM精度向上, ドキュメント参照, AIエージェント, microCMS]]

記事は、LLMが最新かつ正確なドキュメントを参照する際の課題を解決するため、「Document MCPサーバー」という具体的なソリューションを提示します。これは、既存のWeb検索ベースのAIエージェントでは古い情報や誤解釈のリスクがあるという背景から、特定のサービス（microCMS）の公式ドキュメントを直接LLMに提供する仕組みとして開発されました。Mastraの成功事例に触発され、著者自身がmicroCMS向けに実装したこのサーバーは、CursorやClaude CodeのようなAIコーディングツールで、質問に対するLLMの回答精度を劇的に向上させ、さらに参照元のドキュメントURLを提示することでユーザーが情報の信頼性を確認できるようになります。

技術的実装として、ドキュメントコンテンツをマークダウン形式でローカルに保持し、これらをLLMが利用するための三つのツールを定義しています。「list_documents」でファイル一覧を返し、「search_document」でファイル内容を取得、そして「fetch_general」で共通情報を読み込ませることで、LLMは精度の高い回答を導き出します。特に、APIのリクエスト方法や管理画面URLの構築方法といった共通知識を常に参照させる工夫が凝らされています。さらに、ドキュメントが更新された際には、microCMSからのWebhookをPipedreamで受け取り、自動でGitHubのPull Requestを作成する仕組みで、情報の鮮度を保つ運用まで考慮されています。

このアプローチは、一般的なRAG（Retrieval Augmented Generation）を超え、ドメイン固有の知識をLLMに効率的かつ正確に提供する、より洗練された手法を示しています。特定のSaaSやライブラリが自社のドキュメントMCPサーバーを提供するトレンドは、開発者のAIアシスタント活用体験を次のレベルへと引き上げる可能性を秘めており、今後のAIを活用した開発ワークフローにおける重要な要素となるでしょう。
