## GitHub MCP Tools で必要ないツールを減らす工夫 #cursor

https://qiita.com/kokamoto01/items/1f1fc39af9cd72a365b0

CursorのGitHub MCP Toolsの40個の制限を克服するため、プルリクエストの作成と更新に特化した最適なツール構成と効率的なワークフローを解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Cursor, GitHub MCP Tools, プルリクエスト, AIコーディング, ツール最適化]]

Qiitaの記事では、AIコーディング支援ツールCursorのGitHub MCP Toolsが持つ40個というツール上限に対し、プルリクエスト（PR）の新規作成と更新作業を効率的に行うための具体的な最適化戦略が解説されています。この課題を解決するため、著者はClaude 4 Sonnetを活用し、PR作業に必須のツール構成を導き出しました。

提案される最適なツール構成は合計8個で、以下の内訳です。新規PR作成には`create_branch`、`push_files`、`create_pull_request`、`get_file_contents`の4つ。既存PRの更新には`get_pull_request`、`get_pull_request_files`、`update_pull_request_branch`、`create_pull_request_review`の4つが推奨されています。これらのツールはPR作業に特化しており、`push_files`や`get_file_contents`は新規・更新の両フローで共通して使用されます。

この構成により、開発者はCursorのツール上限に抵触することなく、PR作成からレビューコメント追加までのワークフローをスムーズに実行できます。具体的には、新規作成フローは「ブランチ作成 → ファイルプッシュ → PR作成」、更新フローは「既存PR確認 → 変更ファイル確認 → 更新ファイルプッシュ → ブランチ更新 → レビューコメント追加」というステップで進行します。イシュー作成、リポジトリ作成、フォーク、マージ、一覧・検索系ツールなど、PR作業に直接関係しないツールは無効化することで、ツールの煩雑さを減らし、本質的な開発タスクに集中できる点が重要です。

このアプローチは、AIツールを導入する際に直面する「機能過多」や「パフォーマンス制約」といった現実的な課題に対し、最小限の構成で最大限の効率を引き出す実践的な知見を提供します。Webアプリケーションエンジニアにとって、日々の開発作業の中心となるPR管理において、AIの力を最大限に引き出しつつ、ツールの制限をスマートに回避する有効な手段となるでしょう。