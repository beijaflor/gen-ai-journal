## MCP-UI: A Technical Overview of Interactive Agent Interfaces

https://workos.com/blog/mcp-ui-a-technical-deep-dive-into-interactive-agent-interfaces

Model Context Protocolを拡張するMCP-UIは、エージェントの会話フローにインタラクティブなWebコンポーネントを直接組み込むことで、人間とAIのインターフェースに変革をもたらす。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIエージェントインターフェース, Model Context Protocol, インタラクティブUI, Remote DOM, Webコンポーネント]]

記事は、AIエージェントと実世界ツールを繋ぐModel Context Protocol (MCP) のテキストベースのインタラクションの限界を打破する「MCP-UI」について技術詳細を解説しています。これは、エージェントの会話フロー内にインタラクティブなWebコンポーネントを直接埋め込む実験的な拡張プロトコルです。特にEコマースやデータ可視化、フォーム駆動型ワークフローといった複雑なドメインにおいて、ユーザーがエージェントの応答を手動でUI要素に変換する手間を省き、リッチな体験を実現します。

MCP-UIは、既存のMCPリソース仕様をUIResourceインターフェースで拡張し、`ui://`スキーマでリソースを識別します。レンダリングには、インラインHTML、外部URL、そしてShopifyのRemote DOMライブラリを活用し、ホストアプリのデザインに合わせたJavaScript駆動型UIを可能にするRemote DOM統合の3つのアプローチがあります。Remote DOMは複雑なインタラクションと視覚的一貫性を両立させる重要な要素です。

実装は`@mcp-ui/server` SDKがリソース作成を抽象化し、クライアント側では`@mcp-ui/client`パッケージがReact/Web Componentsを提供。セキュリティはサンドボックス化されたiframeとイベントシステムによって確保され、コンポーネントはエージェントが解釈・実行する構造化されたイベント（ツール呼び出し、インテント、プロンプトなど）を発行することで、エージェントの自律性を維持します。

この技術は、AIエージェントが単なる情報提供者を超え、直接的なアクションと複雑なUI操作を伴うワークフローの中心となる可能性を秘めています。Webアプリケーション開発者にとって、エージェントベースのアプリケーションにおいて、より直感的で高機能なユーザーインターフェースを構築するための具体的な道筋を示しており、生成AIを活用した開発における「テキストの壁」を打ち破るブレイクスルーとなるでしょう。性能やフレームワーク依存性などの技術的課題は残るものの、宣言的UIやクロスプラットフォーム展開といった今後の展望は、その進化が止まらないことを示唆しています。