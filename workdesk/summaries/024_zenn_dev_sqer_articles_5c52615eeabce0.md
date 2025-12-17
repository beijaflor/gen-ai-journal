## Claude Codeのビルドインツールは無効化してシステムプロンプトを削減できる

https://zenn.dev/sqer/articles/5c52615eeabce0

Claude Codeの組み込みツールを無効化することで、システムプロンプトのトークン消費量を効率的に削減する方法を実証します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Claude Code, トークン削減, システムプロンプト最適化, LLM開発, 開発ツール]]

この記事は、Claude Codeの組み込みツールを無効化することで、システムプロンプトのトークン消費量を大幅に削減できる実用的な最適化手法を紹介しています。著者は、`~/.claude/settings.json`ファイルに`{"permissions": {"deny": ["NotebookEdit"]}}`のように不要なツール名を追加するだけで、そのツールの使い方に関するシステムプロンプトが削減されることを示しています。

具体的な`/context`の使用状況の比較では、無効化後に「System tools」のトークンが16.0kから9.8kに減少し、全体のコンテキスト使用率が11%から6%に改善されることが明確に示されています。

この技術的な背景として、Claude Codeの組み込みツールはほとんどがMCP（Model Context Protocol）サーバーとして実装されており、各ツールには詳細な`InitializerResult Instructions`が含まれていると解説されています。これらの指示はinitialize呼び出し時にシステムプロンプトに渡され、結果として多くのトークンを消費します。不要なツールを無効化することで、これらの説明がシステムプロンプトに含まれなくなり、大幅なトークン削減につながるという筆者の見解が示されています。

応用例として、外部ツール`serena-mcp`を利用する際に、組み込みツールとの役割重複を避けるため、`Edit`、`Glob`、`Grep`、`Read`、`Write`といった全ての組み込みツールを無効化することが提案されています。これは、開発者がプロンプトのコンテキストをより詳細に制御し、カスタムエージェントとの統合を効率化できる点で重要です。