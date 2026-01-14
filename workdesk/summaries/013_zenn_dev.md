## Playwright MCPでCSSの修正が楽になった

https://zenn.dev/silverbirder/articles/5bba8251cea74a

Playwright MCPを活用し、AIエージェントが実際のブラウザ描画結果を検証することで、静的解析では困難なCSSのレイアウト崩れの原因を迅速に特定する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 79/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Playwright MCP, Model Context Protocol, CSS Debugging, AI Agent, Next.js]]

本記事は、筆者がブログのリニューアル作業において、AIエージェントと「Playwright MCP」を組み合わせて複雑なCSSのレイアウト問題を解決した体験談である。具体的には、Markdownから変換されたHTML要素（テーブルやコードブロックなど）の直後で、背景の横罫線と文字の位置が微妙にずれてしまうという、目視やコード確認だけでは原因特定が難しい事象を扱っている。

筆者はこれまで、CSSのコードやJSXの構造をAIに渡して分析を依頼していたが、今回はPlaywright MCPを導入。これにより、AIエージェントが自律的にローカル環境のブラウザを立ち上げ、該当ページにアクセスしてDOM要素や実際の描画状態（スナップショット）を確認しながら調査を進めることが可能になった。調査の結果、原因はコードブロックで使用していたMonoフォントと本文フォントの字面の差によるもので、同じ `line-height` を指定していても実際の表示高さが僅かに異なり、その差分が累積していたことが判明した。

筆者は、このアプローチの重要性について、AIが「記述されたコード」という静的な情報だけでなく、「実際の描画結果」という動的な状態を起点に調査できる点にあると述べている。Next.jsやStorybook、Chakra UIなど、主要なフロントエンドツールが次々とMCP（Model Context Protocol）への対応を進めている現状に触れ、実際の画面を確認しながらAIと協調してデバッグを行う体験は、開発者の安心感と生産性を大きく向上させると結論付けている。フロントエンドエンジニアにとって、視覚的な不具合のデバッグ工数を劇的に削減する実践的なプラクティスとして示されている。