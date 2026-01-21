## VercelのWebインターフェースガイドラインがAIエージェントのコマンドとして利用可能に

https://vercel.com/changelog/web-interface-guidelines-now-available-as-an-agent-command

**Original Title**: Web Interface Guidelines now available as an agent command

VercelのWebインターフェースガイドラインをAIエージェントのカスタムコマンドとして導入し、アクセシビリティやパフォーマンスの自動レビューを可能にする。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 83/100 | **Overall**: 80/100

**Topics**: [[Vercel, AI Agent, Web Interface Guidelines, Accessibility, Developer Tools]]

Vercelは、同社の「Web Interface Guidelines」をAIエージェント向けのスキルおよびコマンドとして提供開始した。利用者は簡単な`curl`コマンドを実行してインストールすることで、`Claude Code`、`Cursor`、`Windsurf`、`OpenCode`、`Gemini CLI`といった主要なAIコーディングエージェント上で、`/web-interface-guidelines`という専用コマンドを呼び出せるようになる。

このコマンドを実行すると、エージェントがプロジェクトのUIコードをスキャンし、アクセシビリティ（A11y）、キーボード操作のサポート、フォームの挙動、アニメーション、パフォーマンスといった多角的な観点から自動的にレビューを実施する。

筆者によれば、この機能の重要性は、Vercelが培ってきた高品質なデザインとエンジニアリングのベストプラクティスを、開発ワークフローの中に直接「スキル」として組み込める点にある。従来はエンジニアが膨大なドキュメントを参照しながら手動で確認していたチェック項目を、AIエージェントがコンテキストを理解した上で瞬時に検証・指摘することで、品質のボトムアップと開発速度の向上を同時に実現することが著者の狙いである。特にアクセシビリティやキーボードナビゲーションといった、実装時に見落とされがちな要素をエージェントが自動でガードレールとして機能させる点は、現代のWebアプリケーション開発において極めて実用的な支援となる。