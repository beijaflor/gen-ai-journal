## The second wave of MCP: Building for LLMs, not developers

https://vercel.com/blog/the-second-wave-of-mcp-building-for-llms-not-developers

Vercelは、LLMの特性を活かすため、単一のAPI操作をラップするのではなく、ユーザーの完全な意図を処理するワークフロー指向のツール構築を推奨し、Multi-Cloud Platform (MCP) の進化における新たなアプローチを提唱します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[LLMツール設計, API設計パターン, ワークフローオートメーション, Multi-Cloud Platform, 状態管理]]

Vercelは、LLM向けツールの設計における「MCP（Multi-Cloud Platform）の第二の波」として、単なる既存APIのラッパーではなく、ユーザーの完全な意図を処理するワークフロー指向のツール構築を提唱しています。従来のAPIラッパー方式では、LLMは開発者のように状態やコンテキストを保持しないため、会話のたびに低レベルなAPI呼び出しの複雑なシーケンスを再構築する必要がありました。これは非効率的で、一貫性の欠如やエラーの原因となります。

記事が指摘するのは、開発者が一度記述すれば再利用できる状態管理やエラー処理、API連携のロジックを、LLMは毎回ゼロから組み立てなければならないという点です。例えば、プロジェクトの作成、環境変数の追加、デプロイ、ドメイン設定といった一連のプロセスを、LLMが個々のAPIエンドポイントを通じて手動でオーケストレーションするのは非常に困難です。

この問題を解決するため、Vercelは`create_project`、`add_env`、`deploy`といった個別のツールではなく、`deploy_project(repo_url, domain, environment_variables)`のようにユーザーの「意図」を完了する単一のツールを設計することを推奨します。このツールは内部で複数のAPI呼び出し、状態管理、エラー回復といった確定的な処理をコードで実行し、LLMには技術的なステータスコードではなく「プロジェクトが正常にデプロイされました」といった会話的な応答を返します。

このアプローチにより、オーケストレーションの負担はLLMからツール側に移り、LLMは推論と自然言語理解に集中できます。これにより、LLMを活用した機能の信頼性と効率が大幅に向上し、ウェブアプリケーションエンジニアはより堅牢なAI駆動型アプリケーションを構築できるようになります。特に、反復的で退屈な手動ワークフローをMCPツールとして抽象化することで、AIエージェントがより自律的かつ正確にタスクを実行できるようになる点が重要です。