## Vercel Agentによるオンデマンドのコードレビュー機能が提供開始

https://vercel.com/changelog/on-demand-vercel-agent-code-reviews

**Original Title**: On-demand Vercel Agent code reviews

Vercel Agentによるコードレビューを、GitHubのプルリクエスト上からオンデマンドで実行可能にするアップデートを公開した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 74/100 | **Overall**: 72/100

**Topics**: [[Vercel Agent, Code Review, GitHub Integration, Developer Experience, AI Workflow]]

Vercelは、同社のAIエージェント機能「Vercel Agent」によるコードレビューを、GitHubのプルリクエスト（PR）からオンデマンドでトリガーできる機能を発表した。これまでVercel Agentによるレビューは自動実行が主であったが、今回のアップデートにより、開発者はGitHub上のデプロイメントテーブル内に新設された「Review with Vercel Agent」ボタンをクリックすることで、任意のタイミングで明示的にAIによるレビューを依頼できるようになった。

この機能の意義は、開発ワークフローにおけるAIの介入タイミングを開発者自身がコントロールできる点にある。著者の意図によれば、すべてのプッシュに対して自動でレビューを走らせるのではなく、開発者が「今、フィードバックが欲しい」と判断した瞬間にAIを呼び出せるようにすることで、よりノイズの少ない効率的な開発体験を提供するものである。

また、従来通りすべてのPRに対して自動レビューを行う設定も、チーム設定（Team Settings → Agent → Review PRs Automatically）から引き続き選択可能となっている。これにより、チームの文化や開発スピード、コスト管理のポリシーに合わせた柔軟な運用が可能になる。Vercel GitHub Appを導入しているプロジェクトであれば、即座にこの新機能を利用開始できる。