## 自然言語で CI/CD パイプラインを定義する Agentic Workflows

https://azukiazusa.dev/blog/natural-language-ci-cd-with-agentic-workflows/

GitHub Nextが開発するAgentic Workflowsは、自然言語を用いてCI/CDパイプラインを定義し、GitHub CLIを通じてコンパイル・実行することで、ソフトウェア開発における繰り返しタスクの自動化と「継続的AI」を実現します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 76/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Agentic Workflows, CI/CD, GitHub Actions, 自然言語プログラミング, Continuous AI]]

GitHub Nextが開発中のAgentic Workflowsは、CI/CDパイプラインを自然言語で定義し、GitHub CLIの拡張機能（`gh aw`コマンド）を通じてコンパイル・実行可能にする画期的なツールです。これは「継続的AI（Continuous AI）」を実現するための取り組みの一環として位置付けられ、Webアプリケーション開発者が日々直面するIssueトリアージ、継続的QA、ドキュメント生成・更新、アクセシビリティレビュー、テストカバレッジ改善といった反復的タスクの自動化をAIエージェントに委ねることを目指します。

具体的な利用方法として、開発者はMarkdown形式のワークフローファイル（`.md`）にYAML Front Matterでメタデータ（トリガー、権限、使用AIエンジン、ネットワークアクセス、`safe-outputs`設定など）を、本文に自然言語でワークフロー内容を記述します。その後、`gh aw compile`コマンドで、AIエンジン（ClaudeまたはOpenAI）が解釈し実行可能な`.lock.yml`ファイルを生成します。この`.md`ファイルが信頼できる情報源となり、`gh aw run`で実行されます。特に、`safe-outputs`による書き込み権限の厳格な分離は、AIエージェントに自律性を持たせつつもセキュリティを確保する重要な設計思想です。

現在、研究デモンストレーション段階であるものの、本ツールは、AIが開発ワークフローに深く統合される未来像を鮮明に描きます。これにより、Webアプリケーションエンジニアは、定型的なスクリプト作成や手作業の反復作業から解放され、より本質的な問題解決や、創造的なアーキテクチャ設計・新機能開発に注力できる機会を得るでしょう。GitHub Actionsのコンセプトと親和性が高く、既存のGitHubエコシステム内で完結できる点も、導入障壁を低減する上で大きな意味を持ちます。この技術は、開発の生産性と品質をAIの力で飛躍的に向上させる可能性を秘めています。