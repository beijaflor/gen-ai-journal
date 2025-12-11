## Claude Codeを使ってzenn-editorの依存パッケージをすべて最新化しました

https://zenn.dev/team_zenn/articles/zenn-editor-dependencies-update

Claude Codeを活用し、zenn-editorの依存パッケージを全面的に最新化することで、セキュリティとパフォーマンスを大幅に向上させました。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 78/100 | **Overall**: 88/100

**Topics**: [[AIを活用した開発, 依存関係管理, フロントエンドツール, CI/CD, DevContainer]]

Zennチームは、開発リソース不足で滞っていたzenn-editorの依存パッケージ最新化を、Claude Codeの力を借りて全面的に実施しました。当初は検証から始め、ルートおよび`packages/zenn-cli`の`package.json`更新とそれに伴うエラー解決をClaude Codeに任せることで、AIの有効性を確認しました。

本格的な作業では、Claude Codeが効率的に作業できるようDevContainersを整備し、個別のパッケージごとにPRを分割して慎重に進められました。Vitest V4のようなClaudeのカットオフされた知識では対応できない問題には、ドキュメントのURL提供やContext7 MCPを利用して対処しました。

最新化の一次リリース後、ユーザーからのバグ報告に対応し、chokidar v4のglobパターン非サポートによるホットリロードの不具合や、Windows環境での`zenn init`実行エラーを修正。この際、簡易的ながらLinux・Windows環境でのE2Eテスト用GitHub Actions Workflowを構築し、今後の恒久的な品質改善に繋げました。

この取り組みの結果、検出された脆弱性が63件から9件へと大幅に減少し、pnpm auditの安全性が向上しました。また、ビルドシステムをWebpackからRspackへ移行したことで、ビルド時間が12.43秒から2.56秒へと79.4%高速化されました。さらに、Node.js、pnpm、lerna-liteのアップデートに伴いOIDC Trusted Publishingを設定し、npm publishの安全性を高めました。今後の定期的な更新を促すため、Dependabotも導入されています。

著者は、Claude Codeがbreaking changesの調査やコード修正を効率化する上で非常に役立ったと評価しており、AIツールの活用が開発タスクの遅延解消に貢献したことを強調しています。