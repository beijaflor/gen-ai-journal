## Neovim 0.12（開発版）でcopilot-language-serverを設定してみたぞ（脱copilot.lua）

https://zenn.dev/vim_jp/articles/a6839f7204a611

Neovim開発版のLSPインライン補完サポートを活用し、GitHub Copilotを専用プラグインから`copilot-language-server`経由へと移行する具体的な設定手順と、実践上の重要な注意点を解説する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Neovim, GitHub Copilot, Language Server Protocol, Inline Completion, Editor Configuration]]

Neovim開発版のLSPが`textDocument/inlineCompletion`をサポートしたことにより、GitHub Copilotの統合方法に大きな変化が訪れています。これまでの専用プラグイン（`copilot.lua`など）から、`copilot-language-server`を介したLSPベースの補完へと移行する具体的な設定が、ウェブアプリケーションエンジニアにとって今、極めて重要です。なぜなら、このLSP経由のアプローチは、より安定した一貫性のあるAI補完体験を提供し、将来的には他のLLMベースの補完ツールへの切り替えも容易にする標準的な手法となるからです。

記事では、`nvim-lspconfig`を用いた効率的なセットアップ手順を詳細に解説しています。特に重要なのは、特定のファイル（例：`env`、`conf`）やGit管理外のディレクトリでCopilotを起動しないよう`root_dir`を設定する方法です。また、`lspconfig`が提供する認証コマンドを上書きしないよう、キーマップやインライン補完の有効化は`on_init`内の`LspAttach`オートコマンドで定義するという実践的なノウハウが提供されています。これにより、既存のCopilotユーザーはより洗練された統合を実現でき、Neovimをメインエディタとして使う開発者にとって、AIコーディングアシスタントの可能性を最大限に引き出すための具体的な指針となります。