## GitHubのプルリクエスト上でAIによるコード生成を可視化するブラウザ拡張機能

https://blog.rbby.dev/posts/github-ai-contribution-blame-for-pull-requests/

**Original Title**: Github Browser Plugin for Ai Contribution Blame in Pull Requests

git-aiプロジェクトと連携し、GitHubのプルリクエスト画面上でAIが生成したコード行を「Blame」形式で特定・表示するブラウザ拡張機能を紹介する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[git-ai, GitHub, Code Review, AI Generated Code, Refined GitHub]]

GitHubのプルリクエスト（PR）において、どの行がAI（**Cursor**や**Claude Code**など）によって生成されたかを可視化するブラウザ拡張機能「**refined-github-ai-pr**」についての紹介記事です。このツールは、Rust製のオープンソースプロジェクト「**git-ai**」が**git notes**として保存したメタデータを活用し、PRの差分画面に「AI Blame」を表示します。各行の生成に使用されたモデル名やプロンプトを直接確認できるほか、PR全体におけるAI寄与率の算出も可能です。

開発チームは、AI生成コードの割合を定量的に把握することで、コード品質の「ガットチェック（直感的な確認）」や、将来的なリファクタリング時の判断材料として活用できます。現在は、**Refined GitHub**をベースにしたプロトタイプ段階ですが、AIエージェントによる自動コーディングが普及する中で、コードの出所を明確にするための非常に実用的なアプローチを提示しています。

**git-ai**を既にワークフローに導入している、あるいはチーム開発においてAI生成コードの透明性と責任の所在を明確にしたいエンジニアやマネージャーに推奨されます。