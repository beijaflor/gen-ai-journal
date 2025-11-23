## Chrome DevTools MCP vs Playwright MCP - どちらを選ぶべき？実測で比較

https://zenn.dev/nexta_/articles/google-chrome-mcp-server

Claude Codeを使ったブラウザテストにおけるChrome DevTools MCPとPlaywright MCPの選択基準を、Blazorアプリを用いた具体的な検証と機能比較に基づき、デバッグ、テストコード生成、パフォーマンス分析といった各MCPの利点を明確に提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[Chrome DevTools MCP, Playwright MCP, Claude Code, ブラウザテスト, パフォーマンス分析]]

この記事は、Claude Code環境でブラウザテストを行う際、Chrome DevTools MCPとPlaywright MCPのどちらを選択すべきか、Blazorアプリでの実測に基づき詳細に比較検証しています。まず、記事公開後にPlaywright MCPコントリビューターからの指摘を受け、初期の誤った認識（「Playwright MCPはAIがセレクターを自動生成する」）を訂正し、両MCPの要素識別方法に本質的な違いはなく、スナップショットに含まれる識別子（ref/uid）を使用していることを明確にしています。主な違いは、Chrome DevTools MCPがCDP（Chrome DevTools Protocol）で直接操作するのに対し、Playwright MCPはPlaywrightライブラリで操作を実行し、その後に同等のPlaywrightコード例をレスポンスに含める点にあると説明しています。

検証では、Blazorのフォーム操作を両MCPで実行し、それぞれの挙動とレスポンスを比較。Playwright MCPは操作後にそのままテストコードとして使えるPlaywrightコードを生成するため、テストコード作成の効率化やPlaywrightのベストプラクティス学習に有効であると評価されています。一方で、Chrome DevTools MCPはUID指定による確実な操作が可能で、デバッグに適していますが、ドロップダウン操作に複数ステップを要し、コード例は含まれません。

6つの観点から比較した結果、Chrome DevTools MCPは細かい制御やデバッグ、そしてPlaywright MCPにはないCore Web Vitalsなどの詳細なパフォーマンス分析機能（自動改善提案含む）が強みです。一方、Playwright MCPは操作手順がシンプルで、Playwrightコード形式のレスポンスがテスト自動化の参考になる点が優位とされています。

著者は、デバッグや要素特定、パフォーマンス分析にはChrome DevTools MCPを、標準的なフォーム操作や探索的テスト、テストコード生成にはPlaywright MCPを推奨しています。また、CI/CDでの自動テストには従来のPlaywright/Seleniumが依然として適していると結論付けています。Webアプリケーションエンジニアにとって、この比較はClaude Codeを用いた開発ワークフローにおいて、目的（デバッグ、テスト自動化、パフォーマンス改善）に応じた適切なMCPの選択指針を提供し、開発効率とアプリケーション品質の向上に直結する重要な情報です。