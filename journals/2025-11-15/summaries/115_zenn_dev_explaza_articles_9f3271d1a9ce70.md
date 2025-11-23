## 書いたコードを“スキル化”して再利用してる話

https://zenn.dev/explaza/articles/9f3271d1a9ce70

Claude CodeのAgent Skillsを活用し、既存のコードから共通パターンを「スキル」として自動生成・再利用することで、開発の効率と品質を向上させる方法を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Agentic Coding, Claude Code, コード生成, Repositoryパターン, 開発ワークフロー]]

著者は、コード記述における定型的な繰り返し作業、特にデータストアへのアクセスで多用されるRepositoryパターンにおいて、手動作成や従来のテンプレート化（go generateなど）では時間と手間がかかり、またLLMに既存コードを参考にさせると古い記述や不要なコードを生成しがちという課題を提示しています。

この課題に対し、著者はClaude CodeのAgent Skills機能が有効な解決策であると主張しています。Agent Skillsは、SKILL.mdを起点にスクリプトやマークダウンをモジュールとしてまとめて配布・参照できるClaude Codeの拡張機能です。特に、Anthropicが提供する公式の「skill creator」というスキルを活用することで、特定のプルリクエストやGitの差分からコード変更を抽出し、そのパターンから自動的にテンプレートを作成してスキルとして再利用できる点が画期的です。

具体的な実践例として、著者は自社の関数型DDDを採用したRepositoryパターンのコード（neverthrowによるエラーハンドリング、AppContextによるマルチテナンシー対応を含む）を用意し、これをskill creatorに与えることで、Repository層のコードを生成・リファクタリングするための汎用的な「repository-generator」スキルを作成しました。このスキルは、エンティティ名やマルチテナンシーの要否などの変数置換をサポートするテンプレート（assets/repository-template.ts）と、Repositoryパターンのアーキテクチャやベストプラクティスを詳述したリファレンスドキュメント（references/repository-pattern.md）を含んでいます。

このスキルを用いることで、例えば「TaskRepositoryを作成してください」といったシンプルなプロンプト一つで、標準化されたRepositoryコードを高精度に生成できることを実演しています。これにより、LLMにコードを「参照」させるのではなく、明確な「テンプレート」としてスキルを与えることで、不要な修正の手間を省き、開発速度とコード品質を同時に向上させることが可能になる、と著者は結論付けています。定期的にGitの差分からスキルを作成・更新することで、常に最新かつ最適なコード生成を実現できると展望しています。