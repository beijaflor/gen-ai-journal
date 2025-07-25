## AIエージェントが読むドキュメントと人が読むドキュメントを分ける

https://zenn.dev/hacobu/articles/9d34268f3dfc62

AI開発ツール導入によるドキュメントの散在と重複を解決するため、プロジェクトのドキュメントを一元化し、AI設定ファイルから参照する手法を提案。これにより、人間とAI双方にとっての一貫性と保守性が向上し、大幅なコード削減を実現した。

[[AI開発ツール, ドキュメント管理, 開発ワークフロー改善, コード削減, 情報一元化, AIエージェント, プロジェクト管理]]

AI開発ツール（Cursor, Claude Codeなど）の導入は、開発効率を高める一方で、プロジェクトのドキュメントがNotion、`.cursor/rules/`、`CLAUDE.md`といった複数の場所に散在し、情報が重複するという課題を生じさせていた。これは人間だけでなく、AIにとっても情報の整合性を保つ上で非効率的である。

この記事では、この問題に対する解決策として、プロジェクトの核となるドキュメントを`docs/`ディレクトリに集約し、各AIツールの設定ファイルからはそのドキュメントを参照する方式を提案している。具体的には、AIに与える指示やコンテキストを直接設定ファイルに記述するのではなく、`docs/`内の関連ドキュメントへの参照を記述する。

このアプローチにより、以下のようなメリットが確認された。
- 人間とAIが参照する情報源の一元化。
- ドキュメント更新時の手間と情報の不整合の削減。
- 新規メンバーのオンボーディングの簡素化。
- 設定ファイルの大幅なコード削減（例: 240行のファイルが37行に減少）。
- 将来的な新しいAIツールへの適応性の向上。

トークン使用量自体は参照先のファイルを読み込むため大きく変わらないが、AIが必要なコンテキストにアクセスしやすくなるという点で効果的であ��。ただし、AI専用の指示は引き続き各AI設定ファイル内に記述することが推奨されている。

---

**編集者ノート**: AIを活用した開発において、ドキュメントの管理は重要な課題。本記事は、AIと人間の両方が効率的に情報を利用できるような、実践的かつ具体的なドキュメント管理戦略を提示しており、特に大規模なプロジェクトや複数のAIツールを導入している環境で注目すべきアプローチである。
