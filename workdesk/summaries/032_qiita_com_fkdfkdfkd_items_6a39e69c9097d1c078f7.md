## Claude MCPのエラーをClaude自身に相談して解決しよう

https://qiita.com/fkdfkdfkd/items/6a39e69c9097d1c078f7

Claude for DesktopのMCP `filesystem`設定で発生するエラーを、Claude自身に公式ドキュメントを学習させて解決した具体的な手順と画期的なデバッグ手法を詳述します。

**Content Type**: 📖 Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 88/100

**Topics**: [[Claude MCP, 環境変数設定, NVM, AIを用いたデバッグ, プロンプトエンジニアリング]]

多くのウェブアプリケーションエンジニアが経験する環境構築の壁に、AIツールであるClaude MCPの`filesystem`設定で著者が直面しました。公式ドキュメント通りに設定しても`command not found`や`Server disconnected`エラーが発生し、通常の検索では解決策が見つからない状況でした。

本記事の最も重要なポイントは、この問題を解決するために「Claude自身にClaudeに関する知識体系（`llms-full.txt`）を学習させ、対話を通じてデバッグを行う」という画期的な手法を採用した点です。これにより、ClaudeはmacOSのGUIアプリケーションにおける`PATH`環境変数の違い、特に`nvm`を使用している場合の`npx`の絶対パス指定の必要性、そして`npx`が内部で子プロセスを呼び出す際にシステムコマンドの`PATH`が不足することで`spawn sh ENOENT`エラーが発生する可能性といった、深層的な原因を正確に診断しました。

結果として、`claude_desktop_config.json`内で`npx`の絶対パスを指定し、`env`セクションに`Node.js`とシステムコマンドの両方を含む`PATH`環境変数を明示的に設定することで問題は解決しました。この経験は、AIが単なるコード生成にとどまらず、複雑なローカル環境に起因する設定トラブルシューティングにおいて、従来の検索手法を凌駕する強力なデバッグパートナーとなり得ることを示唆しています。開発者にとって、AIへの適切な知識投入とプロンプトエンジニアリングによって、AI自身の導入障壁すらもAI自身で解決できるという、新たな可能性と効率的なアプローチを提示しています。