## Claude Code の ENABLE_TOOL_SEARCH=1 の挙動を理解する

https://zenn.dev/him0/articles/8b6c82e592e30b

Claude Codeの実験的フラグ `ENABLE_TOOL_SEARCH=1` を検証し、MCPツールの動的な検索・ロードによってコンテキストウィンドウの消費を最適化する仕組みを明らかにする。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 74/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[Claude Code, MCP (Model Context Protocol), Context Window Optimization, Reverse Engineering, Anthropic API]]

Claude Codeにおいて、MCP（Model Context Protocol）ツールはエージェントの機能を拡張する強力な手段だが、ツールの説明（Description）が増えるほどコンテキストウィンドウを圧迫するという課題があった。著者は、実験的な環境変数 `ENABLE_TOOL_SEARCH=1` を有効にすることで、この問題に対するAnthropicの最新アプローチである「ツールの動的検索と遅延ロード」がClaude Code内でどのように機能するかを、リバースエンジニアリングを通じた技術検証によって詳細に分析している。

従来、MCPツールは起動時にすべての定義がコンテキストに投入されていた。しかし、このフラグを有効にすると、`MCPSearch` という仲介ツールが導入される。著者の調査によると、各ツール定義に `defer_loading: true` フラグが付与され、AIは必要に応じて `MCPSearch` を介してツールを検索・選択した後に初めてその詳細をロードするようになる。これにより、利用しないツールの定義がトークンを無駄に消費するのを防ぎ、コンテキストの「節約」が可能になる仕組みだ。

分析の過程で、著者はClaude Codeの組み込みツール（Skillなど）にはこの遅延ロードが適用されず、常にコンテキストに含まれる挙動を確認している。これについて著者は、頻繁に使用されるツールは即時性を優先し、サードパーティ製などの膨大になりがちなMCPツールは効率性を優先するという、利便性とコストのバランスを取った設計判断であると推察している。

Webアプリケーションエンジニアにとって、この挙動の理解は極めて重要である。自作のMCPサーバーを運用する場合、ツールの説明文を詳細に記述してもコンテキストを過度に圧迫しなくなるため、AIによるツール選択の精度を向上させつつ、長期間の対話や複雑なタスクにおけるパフォーマンス維持が期待できる。Anthropicが提唱する「Advanced Tool Use」の仕組みが、実用的なCLIツールであるClaude Codeにどのように統合されつつあるかを具体的に示す、先行事例としての価値が高い記事である。