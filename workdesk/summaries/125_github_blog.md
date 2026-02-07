## GitHub Copilot CLIのスラッシュコマンド活用チートシート

https://github.blog/ai-and-ml/github-copilot/a-cheat-sheet-to-slash-commands-in-github-copilot-cli/

**Original Title**: A cheat sheet to slash commands in GitHub Copilot CLI

ターミナル上でのGitHub Copilot CLI操作を効率化するスラッシュコマンド群の機能と、ワークフローへの統合メリットを体系的に提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 76/100 | **Overall**: 80/100

**Topics**: [[GitHub Copilot CLI, スラッシュコマンド, ターミナル, コンテキスト管理, 開発効率]]

**GitHub Copilot CLI**における**スラッシュコマンド**（`/`で始まる命令）の活用ガイド。ターミナル内での操作を迅速かつ予測可能にするための各種コマンドが網羅されている。具体的には、セッション履歴をリセットする**`/clear`**、使用するAIモデルを動的に切り替える**`/model`**、アクセス可能なディレクトリを制限してセキュリティを高める**`/add-dir`**や**`/list-dirs`**などが紹介されている。

自然言語によるプロンプトとは異なり、スラッシュコマンドは常に一定の動作を保証するため、ワークフローの定型化に適している。また、**MCP（Model Context Protocol）**サーバーの設定管理や、CLIから直接**Pull Request**を作成する**`/delegate`**、セッション内容をGist等で共有する**`/share`**など、高度なエージェント機能やコラボレーション機能との連携方法も詳述されている。

ターミナル環境を主戦場とし、コンテキストの肥大化を防ぎながら正確なコード生成やシステム操作を行いたい開発者に最適なリファレンスである。CLIを単なるAIチャット窓口ではなく、コマンドラインの強力な拡張ユーティリティとして使いこなしたいエンジニアは一読すべき内容となっている。