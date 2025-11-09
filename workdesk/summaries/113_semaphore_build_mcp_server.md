## MCPサーバーを構築しよう

https://semaphore.io/blog/build-mcp-server

**Original Title**: Let’s Build an MCP Server

この記事は、わずかなPythonコードでCI/CDシステムとAIアシスタントを連携させるModel Context Protocol（MCP）サーバーの構築方法を詳細に説明している。

**Content Type**: Tutorial & Guide
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 91/100 | **Annex Potential**: 88/100 | **Overall**: 88/100

**Topics**: [[MCP (Model Context Protocol), CI/CD, AI Agents, Conversational DevOps, Python Development, API Integration]]

この記事は、わずかなPythonコードでModel Context Protocol (MCP) サーバーを構築し、CI/CDシステム（Semaphore API）とAIクライアント（Codex）を統合する方法を解説しています。ウェブアプリケーションエンジニアにとって、このアプローチはCI/CDワークフローをAIを通じて会話形式で管理し、自動化する新たな道を開きます。

著者は、MCPサーバーがAIクライアントと外部API間の橋渡し役となり、開発者が自然言語でビルドデータやプロジェクト情報を照会・操作できる「会話型DevOps」時代が到来すると主張しています。記事では、SemaphoreのパブリックAPIを例にとり、Pythonの`FastMCP`ライブラリと`httpx`を使用してプロジェクトリストを取得するMCPツールを実装する具体的な手順が示されています。

実装は、`uv`を使ったプロジェクト初期化と仮想環境構築から始まります。次に、`main.py`ファイル内で`FastMCP`インスタンスを生成し、`@mcp.tool()`デコレータを用いて`list_projects`関数を定義します。この関数は環境変数からSemaphore APIトークンと組織情報を取得し、認証されたHTTPリクエストでプロジェクト情報を取得、AIが解釈しやすい構造化された辞書リストとして返します。`FastMCP`は、Pythonの型ヒントから自動的に出力スキーマを生成するため、手動でのJSONスキーマ定義が不要となり、開発の労力を大幅に削減できます。

構築後、`MCP Inspector`というインタラクティブなデバッガーを使用してサーバーの動作を確認し、ツールが正しく定義され、APIからデータが取得できることを検証します。最終ステップでは、`codex mcp add`コマンドを使って構築したMCPサーバーをCodex AIに登録し、「List all my Semaphore projects」といった自然言語での問いかけを通じて、AIが実際にMCPツールを呼び出し、プロジェクトリストを返す様子を実演します。

この技術は、AIエージェントが「前回のビルドが失敗した理由を教えて」「パイプラインにテストステップを追加して再実行して」といった複雑なコマンドを理解し、実行する未来を示唆しています。Semaphoreは、公式のMCPサーバーを現在開発中であり、まもなく一般提供される予定であると述べられており、この動きがDevOpsにおけるAI統合の重要性をさらに裏付けています。これにより、CI/CDプロセスがより直感的でアクセスしやすくなり、エンジニアの生産性向上が期待されます。