## AIエージェントがインタラクティブなUIを返すことを可能にする MCP UI

https://azukiazusa.dev/blog/mcp-ui/

MCP UIは、AIエージェントがチャット応答としてインタラクティブなUIコンポーネントを返すことを可能にし、ユーザー体験を革新します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Agent, User Interface, Model Context Protocol, Interactive Components, Developer Tools]]

MCP UIは、AIエージェントのテキストベースの対話の限界を超え、グラフ、画像ギャラリー、購入フォームなどのインタラクティブなUIコンポーネントを直接チャット応答として返すことを可能にする革新的な技術です。Webアプリケーションエンジニアにとって、これはAIエージェントを活用したユーザー体験を劇的に向上させる上で極めて重要です。

このプロトコルはModel Context Protocol (MCP) を拡張し、`@mcp-ui/server` および `@mcp-ui/client` TypeScript SDKを通じて実装されます。サーバー側では、`createUIResource`関数を用いて`ui://`スキーマを持つUIリソースを定義し、これをエージェントのツール応答に含めます。リソースの内容は、直接HTML文字列 (`rawHtml`)、外部URLを埋め込む(`externalUrl`)、またはReact/Webコンポーネントとしてスクリプトを実行する(`remoteDom`)形式で指定可能です。

クライアント側では、提供される`UIResourceRenderer`コンポーネントがこれらのUIリソースを受け取り、セキュリティが確保されたサンドボックス化されたiframe内でレンダリングします。これにより、従来のテキスト応答では不可能だったリッチな視覚表現や操作性を実現できます。

さらに、`window.parent.postMessage`を用いた双方向のメッセージングにより、UIコンポーネントからのユーザーアクション（例：ボタンクリック）をエージェントに通知し、エージェント側で処理することが可能です。`messageId`を使用することで非同期な通信もサポートされ、より複雑なインタラクションが構築できます。

この技術は、AIエージェントを単なる情報提供者から、具体的なアクションを実行できる強力なツールへと進化させます。Webアプリケーションにエージェント機能を組み込む際、ユーザーエンゲージメントと機能性を飛躍的に高める新たなワークフローの可能性を切り拓く、実用性の高いアプローチと言えるでしょう。