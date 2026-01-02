## AI・MCP・Unityの関係性 - なぜAIはUnityを直接操作できないのか

https://zenn.dev/dsgarage/articles/ai-mcp-unity-relationship

Unityエディタが持つGUI特有の制約をMCP（Model Context Protocol）で解消し、AIによる直感的なエディタ操作と自動開発を実現するアーキテクチャを詳解する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[MCP, Unity, AIエージェント, Claude Code, UniMCP4CC]]

生成AIが高度なコードを生成できる現在においても、Unityエディタの操作（オブジェクト配置やインスペクタの設定など）をAIが直接実行することは困難である。本記事は、この「AIには手も目もない」という物理的・構造的な断絶を、Anthropicが提唱するMCP（Model Context Protocol）を用いてどのように克服するか、その具体的なアーキテクチャと実装（UniMCP4CC）を解説している。

著者は、Unityが人間によるGUI操作を前提とした設計であることを強調する。従来の「バッチモード」はCI/CDなどの非対話的な処理には適しているが、開発中の「試行錯誤のサイクル」には対応できない。この課題に対し、AIの出力をAPI呼び出しに変換する「MCP Bridge（Node.js）」と、Unityエディタ内でリクエストを待ち受ける「Unity MCP Server」を介在させることで、AIによる間接的なエディタ操作を可能にしている。

技術的な核心として、350以上のUnity Editor APIをAIが認識・利用するための「tools/list」の仕組みと、異種システム間の共通言語としてのJSONの重要性が語られている。AIは自然言語の指示を解析し、適切なAPIとその引数をJSON形式で生成する。これを受け取ったUnity側のサーバーが、エディタと同じプロセス内でC#コードを実行することで、ヒエラルキーへのオブジェクト生成やコンポーネントの付与をリアルタイムで行う。

Webアプリケーションエンジニアにとって、このアプローチは「LLMの推論能力を既存のGUIツールや閉鎖的なエコシステムにどう接続するか」という汎用的な設計パターンを示している。単なるコード生成を超え、AIエージェントが開発環境そのものを「操作」するための具体的なブリッジの実装例として、AIネイティブな開発フローを構築する上で極めて示唆に富む内容となっている。筆者は、この仕組みによって「物理演算を使いたい」といった抽象的な意図をAIが具体的なRigidbodyの追加へと翻訳し、実行まで完結できるメリットを強調している。