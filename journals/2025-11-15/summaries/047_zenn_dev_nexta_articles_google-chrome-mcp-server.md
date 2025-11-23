## Chrome DevTools MCP vs Playwright MCP - どちらを選ぶべき？実測で比較

https://zenn.dev/nexta_/articles/google-chrome-mcp-server

Claude Codeを用いたブラウザテスト自動化において、Chrome DevTools MCPとPlaywright MCPの機能と用途を実践的に比較し、適切な選択基準を提示します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[ブラウザテスト, Model Context Protocol, Claude Code, Playwright, Chrome DevTools]]

この記事は、Claude Codeでブラウザテストを行う際に利用できる「Chrome DevTools MCP」と「Playwright MCP」について、Blazorアプリケーションを用いた実測比較を通して、それぞれの特徴と適切な使い分けを解説しています。

まず重要な訂正として、Playwright MCPはAIがセレクターを自動生成するのではなく、Chrome DevTools MCPと同様にスナップショットに含まれる識別子（ref）を使用して要素を特定し、Playwrightライブラリで操作を実行することを明確にしています。LLMはセレクターを生成していません。

両MCPの本質的な違いは、操作の実行方法とレスポンス形式にあります。
Chrome DevTools MCPは、アクセシビリティツリーにUID（一意識別子）を付与し、Chrome DevTools Protocol (CDP) で直接操作を実行します。これにより、要素の確実な指定やデバッグ、そしてCore Web Vitals測定などの詳細なパフォーマンス分析が可能です。パフォーマンス分析機能はChrome DevTools MCP特有の大きな強みであり、LCPやCLS、TTFBといった指標の測定や、レンダリングブロックリソース削減などの改善提案を自動生成します。

一方、Playwright MCPはアクセシビリティツリーから要素のref（識別子）を取得し、内部でPlaywrightライブラリを使って操作を実行します。そして、レスポンスに実際のPlaywrightコード例を含めるのが最大の特徴です。このコード例は、そのままテストコードとして利用でき、Playwrightのベストプラクティス（`getByRole()`など）を学習しながら効率的にテスト開発を進めるのに役立ちます。

具体的なフォーム入力やドロップダウン操作の検証では、Chrome DevTools MCPがUIDを明示的に確認し、複数ステップで確実な操作を行うのに対し、Playwright MCPはより少ないステップでシンプルに操作でき、テストコードの生成が容易であることを示しています。

筆者は、デバッグや要素の確実な特定、パフォーマンス分析にはChrome DevTools MCPが適しており、標準的なフォーム操作や探索的テスト、Playwrightコードの学習や自動テストコード生成にはPlaywright MCPが有効であると結論付けています。CI/CD自動テストにはどちらも不向きで、従来のPlaywright/Seleniumを推奨しています。両MCPは内部的にアクセシビリティツリーを使用し、基本的なブラウザ操作（ドラッグ＆ドロップ、キーボード操作など）は同等に実行可能です。