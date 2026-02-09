## エージェント型CIによる「Continuous AI」の実践：開発者が今すぐ自動化できること

https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/

**Original Title**: Continuous AI in practice: What developers can automate today with agentic CI

推論を必要とする判断主導のタスクを、自然言語のルールとエージェントの推論によって自動化する新しいCI/CDパターンを提案する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 88/100

**Topics**: [[Agentic CI, Continuous AI, GitHub Next, gh aw, Developer Workflow]]

**GitHub Next**が提唱する「**Continuous AI (CAI)**」は、従来のCIでは困難だった「推論や判断」を伴う作業を自動化する新しい開発パターンです。ユニットテストや静的解析といった決定論的なルールに基づくCIに対し、**Continuous AI**は自然言語で定義された期待値に基づき、バックグラウンドで動作するエージェントがリポジトリを継続的にスキャンして改善案を提示します。ドキュメントと実装の乖離修正、依存関係の挙動変化の検知、自動テストのカバレッジ向上、パフォーマンス改善など、従来は人間の手作業が必要だった「認知負荷の高い雑用」をAIに委譲する手法が具体的に解説されています。

技術的な実装として、Markdown形式のルールを **GitHub Actions** のワークフローへコンパイルするプロトタイプツール **gh aw** が紹介されています。設計思想の核となる **Safe Outputs** では、エージェントはデフォルトで読み取り専用権限を持ち、成果物は必ずプルリクエスト（PR）やIssueとして生成されるため、開発者が最終的な判断権限（Human-in-the-loop）を維持できる仕組みになっています。YAMLによる厳密なルール定義と、自然言語による意図（Intent）の定義を相補的に組み合わせることで、自動化の領域を大幅に拡張します。

AIを単なるコード補完ツールとしてではなく、自律的にリポジトリを改善する「動的なワークフロー」として統合したいエンジニアや、大規模プロジェクトの保守コストを削減したいチームリーダーにとって必読のリファレンスです。