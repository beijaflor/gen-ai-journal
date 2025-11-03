## Chrome DevTools MCPサーバーによるパフォーマンスデバッグ

https://www.debugbear.com/blog/chrome-devtools-mcp-performance-debugging

**Original Title**: Performance Debugging With The Chrome DevTools MCP Server

Chrome DevTools MCPサーバーは、AIモデルがブラウザを操作し、ウェブページのパフォーマンス問題を特定・解決するための新たなインターフェースを提供します。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Chrome DevTools, Webパフォーマンス, AIエージェント, Model Context Protocol, LCP最適化]]

Googleが新たに公開したChrome DevTools MCPサーバーは、AIモデルがChromeブラウザと連携し、ウェブページのパフォーマンスデバッグを自動化する革新的な方法を提供します。MCP（Model Context Protocol）は、AIモデルがブラウザを開き、ウェブページを読み込み、操作し、コンソールメッセージをリスト表示したり、パフォーマンスのトレースを記録したりできる命令セットを通じて、他のアプリケーションと通信することを可能にします。これにより、GeminiのようなAIモデルが、ユーザーの指示に基づいてウェブサイトの動作を解析し、具体的なパフォーマンス改善策を提案できるようになります。

記事では、まずGemini CLIツールとDevTools MCPサーバーのセットアップ方法が詳細に説明されます。その後、GeminiがMCPサーバーを介してbooking.comを操作し、ホテルの検索を行うインタラクションが示され、その結果としてLCP (Largest Contentful Paint) やCLS (Cumulative Layout Shift) といったCore Web Vitalsに基づいたSubstack.comのパフォーマンス分析が実行される様子が紹介されます。AIはこれらのメトリクスを評価し、LCPのロード遅延が高いといった具体的な問題点を指摘します。

特に注目すべきは、AIがLCP最適化に関する具体的な推奨事項を提供できる点です。例えば、LCP画像に対して`fetchpriority="high"`属性を追加したり、`loading="lazy"`属性を削除したり、JavaScriptではなく初期HTMLに`<img>`タグを配置したりするよう指示します。さらに、ローカルウェブサイトのファイル変更をAIに許可することで、レンダリングブロックを引き起こすjQueryスクリプトを`defer`するなどの修正をAIが提案・実行し、その改善効果（LCPが55%改善）を即座に検証するデモンストレーションも行われています。

このDevTools MCPサーバーは、DevToolsやLighthouseに存在するパフォーマンス分析データにチャット形式で簡単にアクセスできるため、特にローカル環境でのウェブサイトのパフォーマンス問題を迅速に特定し、修正を試すための強力なツールとなり得ます。将来的には、より深い統合と機能拡張が期待され、ウェブ開発者のデバッグワークフローを大きく変革する可能性を秘めています。