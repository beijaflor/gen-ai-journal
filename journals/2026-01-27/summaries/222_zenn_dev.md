## 【Google Antigravity】新機能「Skills」について

https://zenn.dev/emp_tech_blog/articles/google-antigravity-skills

**Google Antigravity** の新機能「**Skills**」を活用し、論理的なスクリプトとLLMの柔軟性を組み合わせた高度な再利用可能エージェントの構築手法を詳述する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Google Antigravity, AIエージェント, コードレビュー, 開発自動化, プロンプトエンジニアリング]]

AIエージェント環境 **Google Antigravity** の新機能「**Skills**」の実装と活用方法を解説する。Skillsは、指示書（**SKILL.md**）、実行スクリプト（**scripts/**）、知識ベース（**resources/**）、出力例（**examples/**）を1つのパッケージとして管理する機能だ。従来のカスタム指示（Customizations）とは異なり、タスク実行時のみ動的にロードされるため、コンテキスト（トークン）の節約と回答精度の向上が両立できる点が大きな特徴である。

記事では実例として、Pythonによる機械的なチェックとLLMによる意図理解を組み合わせた「**自動コードレビュー**」の構築手順を詳説。スクリプトによる論理的な検証とLLMによる柔軟なフィードバックを分業させることで、TODOの消し忘れからセキュリティ、パフォーマンス観点まで幅広くカバーする手法を提示している。また、ディレクトリ構造そのものがエージェントへの入力となり、**Git** でのバージョン管理やチーム共有が容易な点も運用上の大きな利点だ。**Antigravity** を既に導入している、あるいはプロジェクト固有のレビュー基準や定型タスクをAIに自律実行させたい開発者にとって、ワークフローを高度化する実用的なリファレンスとなっている。