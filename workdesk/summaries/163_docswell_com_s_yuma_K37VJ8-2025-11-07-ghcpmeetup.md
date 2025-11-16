## CI/CDに続く概念？GitHub Universeでも注目のContinuous AIを紹介

https://www.docswell.com/s/yuma/K37VJ8-2025-11-07-ghcpmeetup

GitHub Universeで注目された「Continuous AI」と「Agentic Workflows」が、CI/CDに続く概念として、AIによるソフトウェア開発ワークフローの自動化を推進します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Continuous AI, Agentic Workflows, GitHub Copilot, GitHub Actions, AI駆動開発]]

本記事は、GitHub Universeで注目を集めたGitHub Nextのプロジェクト「Continuous AI」と「Agentic Workflows」について解説するスライド資料です。著者は、GitHub StarでありMicrosoft MVPでもあるMaki Nagase氏。

GitHub Universeでは、GitHub Copilotのサブスクリプションで各社のコーディングエージェントを利用可能にする「Agent HQ」や、コード品質を自動スキャンしCopilotで修正する「Code Quality」、Coding agent版のカスタムチャットモードである「カスタムエージェント」、そしてVS Codeのチャットモード切り替え時にコンテキストを引き継ぐ「Handoffs機能」が特に熱い発表として挙げられました。

本題の「Continuous AI」は、GitHub Nextで進行中の実験的プロジェクトであり、GitHubが提唱する「クソデカ概念」とも評されています。これは、AIを活用してソフトウェア開発やコラボレーションのワークフロー全体を自動化することを目指すものです。既存のCI（継続的インテグレーション）やCD（継続的デプロイメント）に続く概念として、「CAI（Continuous AI）」がソフトウェア開発に新たな価値をもたらすと筆者は主張します。

このContinuous AIを実現する具体的な手段として、「Agentic Workflows」が紹介されています。Agentic Workflowsは、自然言語で自動化したいタスクを表現するだけで、AIエージェントをGitHub Actions上で動かすためのワークフローに自動変換する機能です。GitHub Copilotの契約があれば利用でき、セキュリティ上の理由から明示的な実行権限付与が必要となります。GitHub Copilot CLI、Claude、CodexなどのCLIで実行可能なコーディングエージェントのオプション引数を自動設定し、GitHub Actions上で実行可能な形式に変換してくれます。

例として、週次での業界ニュースレポート作成、リポジトリの健全性可視化、Issueのトリアージ、アクセシビリティレビュー、コード変更に伴うドキュメント更新、CI失敗時の修正案提供、パフォーマンスボトルネックの特定、テストカバレッジ分析と不足箇所のテスト追加といった多岐にわたるタスクの自動化が挙げられ、これらすべてにサンプルが提供されています。これにより、開発者はAIを活用して反復的なタスクから解放され、より創造的な開発に集中できるようになると筆者はその重要性を強調しています。