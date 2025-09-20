## Claude CodeからCodexをMCPで呼び出せるようになった話｜Claude Code性能低下問題もこれで解決！ #ClaudeCode - Qiita

https://qiita.com/tomada/items/6ed639a7dae70264ab5d

Claude CodeからMCPを介してCodex CLIを直接呼び出せるようになり、性能が低下しているClaude Codeの課題を解決しつつ、両者の強みを活かした二段構えのAI駆動開発ワークフローが実現しました。

**Content Type**: Tools
**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, Codex CLI, LLM連携, AI駆動開発, ワークフロー最適化]]

Claude Codeの性能低下に悩む開発者にとって朗報です。この度、OpenAIのCodex CLIがMCP（Model Context Protocol）に対応し、常用しているClaude Codeから直接、高精度なCodex CLIを呼び出せるようになりました。これにより、AI駆動開発のワークフローに新たな最適解が提示されています。

設定は非常にシンプルで、Claude Codeのプロジェクト内に`.mcp.json`ファイルを作成するか、`claude mcp add`コマンド一つで完了します。この設定により、Claude Code内から`/mcp`コマンドでCodex CLIが「connected」状態として認識されるようになります。

この連携の最大の特長は、二段構えのプロンプト処理です。ユーザーがClaude Codeに質問を投げかけると、Claude Codeはそれを解釈し、コード品質、アーキテクチャ、パフォーマンス、セキュリティなど多角的な観点から具体的な詳細プロンプトを生成します。さらに、`CLAUDE.md`ファイルの内容を基にプロジェクトの文脈も加味した上で、この洗練されたプロンプトをCodex CLIに送ります。Codex CLIは、この詳細なインプットを元に、深い分析と複雑な推論を実行し、精度の高い結果を返します。

このアプローチにより、開発者はそれぞれのツールの強みを最大限に活かせます。日常的なサクッとした実装タスクや汎用的な開発にはClaude Codeを、時間をかけた深い分析や複雑な問題解決、アーキテクチャ設計といった重要なタスクにはCodex CLIを利用するという明確な使い分けが可能です。特に、最近話題になるClaude Codeの性能低下問題への有効な対策となり、開発品質の維持に貢献します。さらに、Claude CodeのMaxプランとCodex CLI（ChatGPT Plus経由）を組み合わせることで、トークンコストを最適化しながら最高のパフォーマンスを引き出せる点も、スタートアップのエンジニアにとって大きなメリットです。

これはAI駆動開発におけるツール選択と連携の新たなベストプラクティスを示しており、適材適所でAIツールを使いこなすスキルがこれからのエンジニアに求められるでしょう。