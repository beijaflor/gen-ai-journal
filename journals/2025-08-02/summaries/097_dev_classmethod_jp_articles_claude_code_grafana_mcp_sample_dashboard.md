## Claude CodeからGrafanaのMCPサーバーを使ってダッシュボードを作ってみた

https://dev.classmethod.jp/articles/claude-code-grafana-mcp-sample-dashboard/

Claude CodeがGrafana MCPサーバーを活用し、ダッシュボードの作成とデバッグを自動化する実践手法を具体的に示す。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, Grafana, AIコーディングアシスタント, ダッシュボード自動化, LLMオーケストレーション]]

この記事は、AnthropicのAIコーディングアシスタント「Claude Code」がGrafanaのManagement Plane (MCP) サーバーを活用し、ダッシュボードの作成からデバッグまでを自動化する実践的な手法を詳細に解説しています。Webアプリケーションエンジニアにとって、視覚化ツールの設定や管理は手間がかかる作業ですが、本記事はAIによる効率化の可能性を示唆します。

具体的な手順として、Claude CodeにGrafana MCPサーバーを連携させるための設定（`~/.claude/settings.json`でのパーミッションと環境変数の設定）から始め、AIにGrafanaのデータソース一覧を取得させます。その後、AWS Cost Table (Athenaデータソース) を用いたサンプルダッシュボードの作成を指示。重要なのは、Claude Codeが初期段階でデータソース指定ミスやAthenaクエリの型不一致（数値比較と文字列型の年・月）といったエラーを発生させた点です。

しかし、筆者はClaude Codeに「`No data`が表示される」「データソースが間違っている」「クエリでエラーが出ている」といった具体的なフィードバックを与え、さらには「AWS CLIでAthenaクエリを先にテストしてから反映させる」という指示を追加することで、AIが自律的に問題を特定し、クエリを修正して機能するダッシュボードを完成させるプロセスを示しています。これは、AIが単にコードを生成するだけでなく、具体的なエラーとユーザーからの詳細な指示を基に、複雑な技術的課題を反復的に解決する能力を持つことを明確に示しており、実務におけるAIとの協調開発の新たな可能性を開きます。

開発者はこのアプローチにより、Grafanaダッシュボードのプロビジョニングや更新作業を大幅に効率化し、手動でのJSON編集やUI操作の負担を軽減できるため、より価値の高い業務に集中できるようになるでしょう。AIがエラーから学習し、改善する具体的なワークフローは、今後のAI活用における重要な示唆を与えます。