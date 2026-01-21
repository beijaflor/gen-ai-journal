## Vercel Web Interface GuidelinesがAIエージェントのコマンドとして利用可能に

https://vercel.com/changelog/web-interface-guidelines-now-available-as-an-agent-command

**Original Title**: Web Interface Guidelines now available as an agent command

VercelのWebインターフェース・ガイドラインをAIエージェントの拡張コマンドとして提供し、UI実装の品質検証を自動化する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 83/100 | **Overall**: 80/100

**Topics**: [[Vercel, AI Agents, UI/UX Guidelines, Accessibility, Code Review]]

Vercelは、自社の「Web Interface Guidelines」をAIエージェント用のスキル（コマンド）として提供開始した。エンジニアは指定の `curl` コマンドを実行するだけでこの機能をインストールでき、AIエージェントに対して `/web-interface-guidelines` というコマンドを実行することで、UIコードの包括的なレビューを依頼できるようになる。

このコマンドによって、アクセシビリティ、キーボード操作のサポート、フォームの振る舞い、アニメーションの適切さ、パフォーマンスなど、モダンなWebアプリケーションに求められる重要な品質基準をAIが自動でチェックする。サポートされているエージェントには、Claude Code、Cursor、OpenCode、Windsurf、Gemini CLIが含まれており、その他のエージェントについてもプロジェクトに `AGENTS.md` を追加することで対応が可能だ。

著者がこのアップデートを重要視している理由は、AIによるコード生成が主流になる中で、人間が作成した高品質なデザイン・実装のガイドラインをAIに直接「教え込む」ことが、プロダクトの品質維持において極めて有効だからだ。これまでドキュメントとして参照されるだけだったガイドラインを、開発者が日常的に使用するエージェントの「コマンド」へと昇華させることで、エンジニアはアクセシビリティやベストプラクティスの詳細を記憶していなくても、AIの力を借りて高いUI品質を常に担保できるようになる。AIとの協調開発における「品質の自動検証」を具体的かつ実践的なワークフローへと統合した点が、本機能の大きな意義である。