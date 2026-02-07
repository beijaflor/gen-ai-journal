## tmux, gwq, fzfでworktreeをサクサク切り替えてAIコーディングを並列する

https://zenn.dev/ymat19/articles/9107170744368f

**Claude Code**などのAIツールを用いた並行開発を加速させるため、**git worktree**と**tmux**を連携させ、ブランチ切り替えからセッション移行までを瞬時に完了するワークフローを提案する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[git worktree, tmux, gwq, fzf, Claude Code]]

**Claude Code**などの自律型AIコーディングツールの台頭により、AIの生成待ち時間を活用した「複数タスクの同時並行開発」の重要性が高まっています。本記事では、この並行開発をCLI上でストレスなく実現するために、**git worktree**、**tmux**、**gwq**、**fzf**を組み合わせた高速なコンテキスト切り替え環境の構築手法を解説しています。

著者は、**git worktree**の課題であるパス指定の煩雑さを解消するツールとして**gwq**を紹介し、さらに**tmux**の**popup window**内で動作する独自の切り替えスクリプトを提示しています。このワークフローにより、**fzf**でブランチを選択するだけで、自動的に適切なディレクトリへworktreeが作成され、**tmux**セッションが作成・スイッチされる仕組みです。各セッションで個別のAIエージェントを稼働させることで、CLIから離れることなく複数の実装を並行して進めることが可能になります。

**Claude Code**や**Aider**といったツールを多用し、タスクの待ち時間を最小化して開発スループットを最大化したいWebアプリケーションエンジニアにとって、非常に実践的なガイドです。