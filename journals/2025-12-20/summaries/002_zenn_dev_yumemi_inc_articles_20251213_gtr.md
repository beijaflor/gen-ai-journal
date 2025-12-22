## AIエージェント並列実行に便利なgtr（git-worktree-runner）が.gtrconfig対応でチーム利用しやすくなった

https://zenn.dev/yumemi_inc/articles/20251213_gtr

AIエージェントを並列実行する際のgit worktree管理を簡素化するCLIツール「git-worktree-runner (gtr)」は、`.gtrconfig`ファイルの導入により、設定の宣言的管理とチーム内共有を可能にし、開発ワークフローを効率化します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 99/100 | **Overall**: 76/100

**Topics**: [[AI Agent, git worktree, CLI Tools, Developer Workflow, Team Collaboration]]

この記事では、Claude CodeやCodex CLIなどのAIエージェントを並列実行する際に、煩雑なgit worktree（以下worktree）の管理を補助するCLIツール「git-worktree-runner (gtr)」と、最近導入された`.gtrconfig`ファイルについて解説しています。

著者は、worktreeコマンドが複雑であるという課題に対し、CodeRabbitが開発した`gtr`がその解決策となると紹介します。`gtr`は、`new`コマンドでブランチとworktreeを同時に作成し、`editor`や`ai`コマンドで設定したエディタやAIツールでworktreeを直接開くといった、日常的なworktree操作を簡略化します。また、`list`コマンドでworktreeの一覧を確認し、`rm`コマンドで簡単に削除できるため、多数のworktreeを効率的に管理できます。

これまでの`gtr`は、worktree作成時に`.gitignore`対象ファイルをコピーしたり、依存解決コマンドを実行したりする設定を、`git gtr config add`コマンドで毎回手動で実行する必要があり、設定の共有やチームでの利用が難しいという課題がありました。

しかし、今回のアップデートで導入された`.gtrconfig`ファイルにより、これらの設定をリポジトリ内に宣言的に記述し、gitで管理できるようになりました。これにより、チームメンバーはリポジトリをクローンするだけで、共通の`gtr`設定を適用でき、セットアップの手間を大幅に削減できます。例えば、`copy`セクションで`.env.example`や特定の`.md`ファイルをコピー対象に指定したり、`hooks`セクションで`npm install`や`.env`ファイルのコピーといった`postCreate`フックを定義したりすることが可能です。

著者は、この`.gtrconfig`の導入が、チーム全体でAIエージェントを活用した並列開発ワークフローをより効率的に運用するための重要な改善点であると強調しています。特に、AIツールで`.gtrconfig`を作成する際のヒントとして、ビルド済みとビルド前のworktreeを比較してコピー対象を特定する方法も紹介されており、実用的な側面が強く意識されています。この機能改善により、開発チームはAIエージェントの活用をスムーズに進められるでしょう。