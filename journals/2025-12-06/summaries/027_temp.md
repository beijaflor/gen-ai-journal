## MCPサーバーになってみた #TypeScript

https://qiita.com/jugyo/items/12633900df47cecbf5c5

AIエージェントが外部ツールと連携するためのプロトコルであるMCP（Model Context Protocol）を深く理解するため、筆者は人間がターミナルを介してAIからの質問に直接回答する「人間MCPサーバー」をTypeScriptとExpressで実装しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 81/100 | **Annex Potential**: 86/100 | **Overall**: 84/100

**Topics**: [[MCP (Model Context Protocol), AIエージェント, TypeScript, Express.js, 人間参加型AI]]

この記事は、AIエージェントがデータベースアクセスやファイル操作といった外部ツールと連携するためのプロトコルであるMCP（Model Context Protocol）について、その仕組みを「自分がMCPサーバーになる」というユニークなアプローチで解説しています。

著者は、AIエージェントであるClaude CodeからのHTTPリクエストを受け取り、ターミナルに質問を表示し、人間（著者自身）が回答を入力してClaude Codeに返すという「人間MCPサーバー」を、TypeScriptとExpress.jsを用いて実装しました。このシステムは、`@modelcontextprotocol/sdk/server/mcp.js`と`express`を基盤とし、Node.jsの`readline`モジュールを使ってターミナルからの人間による入力を処理します。

具体的な実装では、Expressアプリケーション内にMCPサーバーをセットアップし、「ask_human」というツールを登録します。このツールは、AIからの質問を受け取ると`askHuman`関数を通じて人間に入力を促し、その回答をAIに返します。また、MCPにおけるセッション管理の重要性にも触れ、HTTPヘッダー経由でセッションIDをやり取りする仕組みを実装し、AIとサーバー間の一連の会話の状態維持を実現しています。

筆者は、実際にAIからの質問に回答する体験を通じて、プロトコルの流れを体感し、AIに呼び出される側の人間としての独特の緊張感や、自身の回答がAIの思考に組み込まれる不思議な感覚を述べています。さらに、将来的に人間がAIに「呼び出されるだけの存在」になる可能性や、AIに選ばれる存在として価値を保つための努力の必要性、限られたAIのコンテキストウィンドウにおける人間の居場所の少なさといった、哲学的な考察も展開しています。この実践的なアプローチは、MCPの技術的理解を深めるだけでなく、人間とAIの関係性について深く考えるきっかけとなることを示唆しており、読者にも同様の体験を勧めています。