## 組織で使うためのClaude Code Action via Amazon Bedrock（認証・ログ分析・クラウド破産防止）

https://zenn.dev/cybozu_ept/articles/org-use-claude-code-action

サイボウズは、Claude Code Actionを組織で安全かつ効率的に利用するための独自基盤を構築し、認証・ログ管理・コスト制御といったエンタープライズ特有の課題を解決する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[Claude Code Action, エンタープライズAI導入, AWS Bedrock, GitHub Actions, コスト管理]]

サイボウズの生産性向上チームは、AnthropicのClaude Code Actionを全社で活用すべく、エンタープライズ利用に特化した独自基盤を迅速に構築しました。本家Claude Code Actionをそのまま導入する際の課題として、利用者ごとのAPI契約やGitHub App作成の手間、セキュリティポリシーの強制・ログの一元管理の難しさ、そしてクラウド破産のリスクが挙げられます。これらの課題に対し、同チームは以下の具体的な解決策を講じました。

まず「認証の一元化」として、Anthropic APIへのアクセスはAmazon Bedrock経由で一元管理し、AWS認証にはGitHub ActionsのOIDCと`aws-actions/configure-aws-credentials`を組み合わせ、特にOIDCの`subject claim`に`job_workflow_ref`を追加する工夫でセキュリティを強化しています。GitHub認証には、組織で共有するGitHub Appを利用し、秘密鍵はAWS Secrets Managerで安全に管理することで、利用者の手間を大幅に削減しました。

次に「実行ログの一元保存・分析」では、Bedrockのモデル呼び出しログ機能を活用しS3に保存、AWS GlueとAthenaで分析可能なスキーマ定義を行うことで、法的要件や内部統制に対応可能なログ基盤を構築。

さらに「クラウド破産防止」のため、リポジトリごとに推論プロファイル（Bedrock Inference Profile）を用意し、Athenaクエリで過去1時間のトークン使用量をリアルタイムでチェックし、クォータ超過を防ぐ仕組みを実装。これにより、使われないAPIに対する無駄な定額課金を避け、費用対効果の高い運用を実現しています。

本基盤により、kintoneアプリでの申請と半自動化されたインフラ構築フローを通じて、利用開始までの期間を数日から半日〜1日に短縮。週次・月次レポートの自動生成機能も追加し、組織全体の利用状況を可視化しています。一方で、Claude Code Actionの更新頻度の高さ、セキュリティと利便性のトレードオフ、PublicリポジトリやGHESへの対応などの課題も認識しており、ベータ運用を通じてフィードバックを収集し、改善を続けています。これは、AI開発ツールを組織に導入する際の具体的な課題と、それを技術的に解決する貴重な実践例として、Webアプリケーションエンジニアにとって大いに参考になるでしょう。