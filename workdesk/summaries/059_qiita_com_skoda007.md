## VSCodeからBacklogのMCPに接続するまでのステップまとめ #githubcopilot

https://qiita.com/skoda007/items/47b90d91d3172695cf41

本記事は、GitHub Copilot ChatとBacklog MCPサーバーを連携させ、VSCodeからBacklog情報を効率的に検索して開発ワークフローを改善する手順を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 79/100 | **Annex Potential**: 76/100 | **Overall**: 80/100

**Topics**: [[GitHub Copilot Chat, Backlog MCP Server, VSCode Extension, Developer Workflow Automation, API Integration]]

この記事は、VSCodeのGitHub Copilot ChatとBacklog MCPサーバーを連携させ、Backlogの情報を効率的に検索・参照する具体的な手順を解説しています。開発中に「あの仕様はどこに？」「Wikiのこの情報は何だった？」といった疑問が生じた際、毎回手動でBacklog内を検索する手間を削減するのが狙いです。

具体的な連携手順は以下の通りです。まず、VSCodeでMCP（Microsoft Copilot Protocol）が利用できるよう設定し、Backlogの個人設定からAPIキーを発行します。次に、Backlog MCPサーバーをDockerコンテナとしてVSCodeに登録する設定を記述します。ここでは、`BACKLOG_DOMAIN`と`BACKLOG_API_KEY`を環境変数として指定し、`ghcr.io/nulab/backlog-mcp-server`イメージを実行します。この設定により、Copilot ChatはBacklog APIを介してプロジェクト情報にアクセス可能になります。

設定後、GitHub Copilot Chatのモードを「Agent」に切り替え、「Backlogでコーディング規約が記載されているWikiのページってどこにある？」といった質問を投げかけると、MCPサーバーがBacklogを検索し、関連するWikiページへのリンクを提示します。これにより、必要な情報を素早く取得でき、開発者はコンテキストスイッチを最小限に抑えながら業務に集中できます。

なぜこれが重要かというと、Webアプリケーション開発において、プロジェクト管理ツール内に散在するドキュメントやチケット情報への迅速なアクセスは、生産性に直結するからです。AIアシスタントにその検索を委ねることで、定型的な情報探索にかかる時間を大幅に削減し、より本質的な開発業務に注力できるようになります。開発者にとって、日々の情報検索の手間を省き、ワークフローを改善するための具体的なソリューションとして非常に価値のあるアプローチです。