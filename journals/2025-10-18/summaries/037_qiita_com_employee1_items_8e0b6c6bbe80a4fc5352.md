## AWS MCPサーバー（DocumentationとKnowledge）をVS Codeで使えるようにしてみた

https://qiita.com/employee1/items/8e0b6c6bbe80a4fc5352

本記事は、WSL環境下のVS CodeでAWSのDocumentation MCPサーバーとKnowledge MCPサーバーを有効化し、GitHub Copilotと連携させてAWSナレッジを活用する方法を具体的に解説しています。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[AWS MCP Server, VS Code, GitHub Copilot, AWS Documentation, Developer Tools Integration]]

この記事は、AWSのMCPサーバー（Documentation MCPサーバーとKnowledge MCPサーバー）をVS Codeで利用可能にするための詳細な設定手順を、GitHub Copilotとの連携を含めて紹介しています。これにより、Webアプリケーションエンジニアは、最新のAWSドキュメントや広範なナレッジ（FAQ、ベストプラクティス、トラブルシューティング記事など）を開発環境内で直接参照できるようになり、開発効率の向上が期待されます。

筆者はまず、WSL環境でVS CodeのAgentモードを有効化し、Pythonパッケージ管理ツール`uv`を使用してPython 3.10以上をインストールする前提条件と準備手順を説明しています。主要な設定は、VS Codeのユーザーデータディレクトリにある`mcp.json`ファイルに各MCPサーバーの設定を記述することで行います。Documentation MCPサーバーについては、`uvx`コマンドとサーバーパスを指定し、Knowledge MCPサーバーについては、初期のURL指定に加え、`TypeError: fetch failed`エラーを回避するための`uvx mcp-proxy`コマンドによる代替設定方法も提示されており、具体的なトラブルシューティングのヒントも提供されています。

設定が完了すると、VS Code内で各MCPサーバーを「Running」状態にすることで利用可能になります。筆者は、GitHub Copilot (GPT-4.1) とDocumentation MCPサーバーの連携事例、およびClaude Sonnet 3.5とKnowledge MCPサーバーの連携事例を紹介し、AIアシスタントがMCPサーバーを介して質問に正確に回答する様子を具体的に示しています。特に、`settings.json`に設定を記述するとエラーが発生する問題や、MCPサーバーの稼働状況を確認するコマンド`mcp list server`についても補足されており、読者が実際に導入する際の障壁を低減する配慮が見られます。

筆者は、この連携によって「最新情報のナレッジをもとに自分たちの聞きたい情報を取得できるため、非常にうれしい機能だと感じた」と述べ、開発ワークフローにおけるAWSナレッジ活用の重要性を強調しています。