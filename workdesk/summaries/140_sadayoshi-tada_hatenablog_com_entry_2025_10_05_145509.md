## AWS Knowledge MCP Server が GA されたので試しに設定してみたメモ✍

https://sadayoshi-tada.hatenablog.com/entry/2025/10/05/145509

AWS Knowledge MCP Serverの正式リリースとClaude環境での具体的な活用方法を解説し、開発者が最新のAWS情報を効率的に取得できるメリットを提示します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[AWS Knowledge MCP Server, Claude Desktop, Claude Code, AIエージェント, クラウド情報取得]]

AWS Knowledge MCP Serverが正式リリース（GA）され、その設定方法と実用的な活用が解説されています。このMCPサーバーは、AWSドキュメント、ブログ記事、新機能の発表、Well-Architectedのベストプラクティスといった膨大な最新情報に、開発者がClaude DesktopやClaude CodeなどのMCP互換クライアントから直接アクセスできるように設計されています。無料で認証なしで利用でき（レート制限あり）、AWSアカウントも不要なため、手軽に利用開始できる点が魅力です。

利用可能な主なツールには、AWS全体のドキュメント検索を行う`search_documentation`、ドキュメントをMarkdown形式で読み込む`read_documentation`、関連コンテンツを推奨する`recommend`、そして実験的ながらリージョンごとのサービス利用可否を確認する`get_regional_availability`などがあります。

著者はClaude DesktopおよびClaude Codeにおける具体的な設定方法を提示し、実際の動作を検証しました。特に、同時期にリリースされたAWS API MCP Server v1.0.0について質問したところ、パフォーマンス向上、セキュリティ強化、可観測性の向上、通信オプションの拡張、人間参加型ワークフローの改善といった詳細なリリース概要が正確に参照記事とともに提示されました。

この結果から、著者はAWS Knowledge MCP Serverが、日常の開発において最新のAWS情報を効率的に入手し、整理・要約する上で非常に有用なツールであると評価しています。re:Inventなどのイベント前後における情報収集の効率化にも貢献すると期待されています。