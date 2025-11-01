## ChatGPT 内でアプリを直接操作する Apps SDK に自作のアプリを接続する

https://azukiazusa.dev/blog/chatgpt-apps-sdk/

ChatGPT内で外部アプリを直接操作するApps SDKを用いて、MCPサーバーとReactコンポーネントでインタラクティブなUIを構築する具体的な手順を、開発者向けに詳細に解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 89/100 | **Annex Potential**: 88/100 | **Overall**: 88/100

**Topics**: [[ChatGPT Apps SDK, MCP, UIコンポーネント開発, LLM連携, フロントエンド開発]]

この記事では、OpenAIが提供する「Apps in ChatGPT」の機能と、その基盤となるApps SDKを使用して、ChatGPT内で動作する外部アプリケーションを開発する具体的な手順を解説している。著者は、この機能がLLMがユーザーの意図を理解して適切なアプリを呼び出し、ユーザーがアプリのUIを通じて操作できるという、新しいフロントエンド開発パラダイムを提示すると強調している。

Apps in ChatGPTはMCP（Model Context Protocol）を基盤としたApps SDKを利用して構築される。開発者はMCPサーバーを通じてアプリケーションロジックとUIコンポーネントを設計する。具体的な開発手順は以下の通りだ。

1.  **MCPサーバーの構築**:
    *   Node.jsプロジェクトを初期化し、TypeScript SDK（`@modelcontextprotocol/sdk`）とHTTPサーバーとしてHonoをインストールする。
    *   UIコンポーネントはMCPサーバーの「Resource」として定義され、`text/html+skybridge`のMime Typeと`ui://xxx`形式のURIを持つ。`server.registerResource`メソッドでHTMLコンテンツを登録する。
    *   UIコンポーネントを呼び出す「Tool」を定義し、`_meta["openai/outputTemplate"]`プロパティでUIコンポーネントのURIを指定することで、ツールとリソースを紐付ける。
    *   Honoフレームワークを利用してMCPサーバーをHTTPサーバーとして起動し、ローカル開発時にはngrokなどを使ってHTTPSでインターネットに公開する。

2.  **ChatGPTへのアプリ接続**:
    *   ChatGPTの開発者モードを有効にし、MCPサーバーのURLを指定してアプリを登録する。
    *   これにより、「My Todo App, TODO の一覧を表示して」のようなプロンプトで、ChatGPTがMCPサーバーのツールを呼び出し、定義されたUIコンポーネントがチャット内に表示されるようになる。

3.  **インタラクティブなUIコンポーネントの実装**:
    *   より複雑なUIには、`window.openai`オブジェクトを使用する。これはChatGPTのiframe内で利用可能なグローバルオブジェクトで、テーマ設定（`theme`）、表示モード（`displayMode`）、ツール呼び出し（`callTool`）、状態永続化（`setWidgetState`）などのプロパティやメソッド、イベントリスナーを提供する。
    *   著者は、Reactを用いてUIコンポーネントを実装する方法も紹介。MCPサーバーのロジックとUIコンポーネントのコードを分離し、`web/`ディレクトリでReactプロジェクトを構築する。
    *   `useOpenAiGlobal`カスタムフックを用いて`window.openai`オブジェクトの変更を購読し、TODOリスト表示や追加フォームの実装を通じて`window.openai.callTool`でMCPサーバーのツールを呼び出して状態を更新する具体的な例を示す。
    *   ビルドしたReactコンポーネント（JS/CSS）をMCPサーバーのResourceとして読み込み、HTMLテンプレートに埋め込んで提供するようにMCPサーバーの実装を更新する。

この一連の手順により、開発者はChatGPTのチャット内でインタラクティブに動作する外部アプリを構築・テストでき、LLMの理解力とカスタムUIの操作性を組み合わせたリッチなユーザー体験を実現できると著者は結論付けている。