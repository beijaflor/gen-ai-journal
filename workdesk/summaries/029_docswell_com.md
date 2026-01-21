## GitHub Copilotにも追加されたAgent Skillsとは

https://www.docswell.com/s/yuma/5RE1Q3-2025-12-20-dotnetlab

開発エージェントに特定のタスク実行手順やリソースを体系的に理解させるためのオープン規格「Agent Skills」の仕組みと、GitHub Copilotにおける具体的な実装方法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GitHub Copilot, Agent Skills, Anthropic, AI Agent, VS Code]]

本記事は、Anthropicが開発し2025年12月にオープンスタンダード化された「Agent Skills」の概要と、GitHub Copilotでの活用方法を解説したテクニカルスライドである。Agent Skillsとは、AIエージェントが特定のタスクを遂行する際に参照すべき「標準手順書」を、指示（Instructions）・スクリプト（Scripts）・リソース（Resources）の3要素でパッケージ化する仕組みを指す。

著者は、この機能がGitHub Copilot（VS Code Insiders版やCLI）に導入されたことの重要性を強調している。設定はプロジェクト内の `.github/skills/[skill-name]/` ディレクトリに `SKILL.md` を配置することで行い、YAMLフロントマターで名前や説明（description）を定義する。Copilotはユーザーのリクエストを解析し、この説明文と合致した際にのみ動的にSkillを読み込む。この3段階のフェーズ（発見・指示の読み込み・リソースアクセス）を経ることで、AIが過剰なコンテキストを保持して精度が低下することを防ぎつつ、必要な時にだけ高度に専門化された手順を適用できる点が技術的な肝である。

また、著者は「Custom Instructions」との使い分けについても具体的な指針を示している。常に守らせたいルールはCustom Instructionsに記述すべきだが、テスト、デバッグ、デプロイといった「手順通りに動いてほしいプロジェクト固有のワークフロー」や、MCP（Model Context Protocol）ツール等の具体的な使用法を定義する場合にはAgent Skillsが最適であると主張している。

Webアプリケーションエンジニアにとって、この規格の採用は、開発チーム内の暗黙知をAIが解釈可能な形式でコードベースに同梱できることを意味する。特定のライブラリの更新手順や社内のデプロイフローなどをSkillとして定義しておくことで、AIエージェントの自律性を高め、属人性を排除したAI駆動開発を加速させるための基盤となる。単一のベンダーに依存しないオープン規格であるため、ツールを跨いで開発手順を共有・再利用できる将来性も高く評価されている。