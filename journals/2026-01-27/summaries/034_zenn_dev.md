## Claude CodeでGitHub Issue駆動開発を自動化する

https://zenn.dev/driller/articles/claude-code-issue-workflow

独自ツールキット「**Issue Workflow**」を用いて、Claude CodeによるGitHub Issueベースの開発プロセスを一気通貫で自動化する手法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Claude Code, GitHub Issue, TDD, git worktree, 開発ワークフロー]]

本記事は、**Claude Code**を活用してGitHub Issueの確認からブランチ作成、テスト駆動開発（**TDD**）、PR作成、マージまでを自動化するツール「**Issue Workflow**」の導入と活用法を詳説している。

このツールキットは、**Red-Green-Refactor**サイクルの強制や、**lint**・**format**・**typecheck**（Python環境では**ruff**や**mypy**）といった品質ゲートの自動実行機能を備えている。特筆すべきは、**git worktree**を活用した`/add-worktree`コマンドの実装であり、複数のIssueを独立した作業ディレクトリで並行して進める環境を容易に構築できる。単なるAIによるコード生成を超え、開発プロセスの「型」をAIに遵守させることで、一貫した品質を保ちながら開発速度を最大化する設計思想が示されている。

**Claude Code**を単なるチャットツールとしてではなく、Issue駆動開発の自律的な実行エンジンとして実プロジェクトに組み込みたいWebアプリケーションエンジニアにとって、即戦力となるガイドである。