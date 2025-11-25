## 僕のClaude Code Plugin紹介 ~skills/create-git-worktree~

https://qiita.com/getty104/items/4716e77cbadd901ea11d

著者はClaude CodeのPlugin機能を用いて`create-git-worktree` Skillを開発し、git worktreeの作成と初期設定を自動化するワークフローを紹介します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 74/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Claude Code, AIエージェント, Git Worktree, 開発ワークフロー自動化, Plugin開発]]

この記事では、著者が自身のClaude Code Plugin環境の一部として開発した`skills/create-git-worktree`というSkillが紹介されています。Claude CodeのPlugin機能は、カスタムコマンドやSkillなどをパッケージとして配布できるものであり、Skillは特定のタスクを実行するために参照される再利用可能な知識と手順をまとめたものです。主にMarkdownファイル（SKILL.md）で定義され、Claude Codeがユーザーのリクエストに応じて適切な指示に従い、スクリプト実行やワークフロー管理をルールベースで自動化できます。

今回紹介された`create-git-worktree` Skillは、git worktreeの作成と管理をClaude Codeに任せることを目的としています。このSkillを利用することで、デフォルトブランチへのチェックアウト、`.git-worktrees/`ディレクトリへのworktree作成、作成したworktreeへの移動、親ブランチからの必要なファイル（`.env`, `.serena`など）のコピー、そしてnpmによるライブラリのインストールといった一連の作業が自動化されます。著者は、このSkillがMCPやサブエージェントでは実現しにくい「よしなにスクリプトやワークフローを実行する」ことを可能にし、開発ワークフローを効率化する実用的な方法であると強調しています。