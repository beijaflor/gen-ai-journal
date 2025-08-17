## Google Analytics MCP を最短導入する手順（Claude / Gemini 対応）

https://zenn.dev/yamitake/articles/google-analytics-mcp-setup

本記事は、Google Analytics MCPの最短導入を通じて、ClaudeやGeminiといったLLMからGA4データを安全に読み取るための実践的な手順を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Google Analytics 4, LLM Integration, Data Access Security, Command Line Interface, Google Cloud Platform]]

本記事は、Google Analytics Model Context Protocol (MCP) を活用し、LLM（ClaudeやGeminiなど）からGoogle Analytics 4 (GA4) データを安全に読み取るための最短導入手順を解説しています。ウェブアプリケーションエンジニアにとって、プロダクトのユーザー行動を把握するGA4データへLLMを通じて自然言語でアクセスできる能力は、従来のデータ分析ワークフローに革新をもたらします。これにより、GA4の複雑なUIやAPIに直接触れることなく、LLMに「過去30日のアクティブユーザー数を日別に教えて」といった具体的な問いかけを行い、迅速に洞察を得ることが可能になります。

本ガイドの最も注目すべき点は、プロジェクト作成からAPI有効化、認証（Application Default Credentials）までを一貫してCLIベースで行うベストプラクティスを提示している点です。これにより、GUI設定で迷う時間を大幅に削減し、確実なセットアップを実現します。具体的には、`gcloud`コマンドを用いたAnalytics Admin APIとData APIの有効化、`pipx`による`google-analytics-mcp`サーバーのセットアップ、さらにClaude DesktopやGeminiといったLLMクライアントへの具体的な設定ファイル追記方法が、コード例と共に詳細に説明されています。

このMCPは読み取り専用であるため、LLMを通じてGA4データにアクセスする際のセキュリティリスクを最小限に抑えつつ、AIによるデータ分析やレポート作成の可能性を大きく広げます。さらに、IAMのGoogleグループによる管理、開発・本番環境の分離、二段階認証の推奨、最小権限の付与といった運用上のセキュリティベストプラクティスも示されており、本番環境での安全かつ堅牢なシステム構築に役立ちます。この実践的な手順は、エンジニアがAIを活用したデータ分析基盤を迅速に構築し、開発ワークフローを効率化するための具体的な道筋を示しています。