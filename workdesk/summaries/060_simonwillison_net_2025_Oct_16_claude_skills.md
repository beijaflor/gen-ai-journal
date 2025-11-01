## Claude Skillsは素晴らしい、MCPより大きな変革の可能性

https://simonwillison.net/2025/Oct/16/claude-skills/

**Original Title**: Claude Skills are awesome, maybe a bigger deal than MCP

Anthropicが発表したClaude Skillsは、Markdownとスクリプトでモデルの能力を拡張するシンプルかつ強力な新機能であり、Claude Codeを汎用エージェントへと変貌させ、従来のModel Context Protocol (MCP)を超える影響力を持つと著者は主張します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Claude Skills, LLM Agents, Model Context Protocol (MCP), コーディング環境, 開発ワークフロー自動化]]

Anthropicが発表したClaude Skillsは、LLMの能力を拡張する革新的なパターンであり、従来のModel Context Protocol (MCP)よりも大きな影響力を持つ可能性を秘めていると著者は強調します。

Claude Skillsは、指示、スクリプト、リソースを含むMarkdownファイルベースのフォルダで構成され、必要な時にのみモデルによって読み込まれます。これにより、ClaudeはExcel操作や企業のブランドガイドライン遵守など、特定のタスクで性能を向上させます。このシステムはトークン効率に優れており、モデルは各スキルの簡潔な説明（MarkdownのフロントマターYAML）のみを初期に認識し、関連タスクが要求された場合にのみ詳細情報を読み込みます。例えば、Slack用GIF作成スキルでは、PythonスクリプトでGIFを生成し、Slackの2MB制限をチェックし、サイズオーバーの場合は再試行する能力が示されています。

このSkillsメカニズムは、ファイルシステムアクセスとコマンド実行が可能なコーディング環境に大きく依存します。著者は、この依存関係がClaude Codeを単なるコーディングツールではなく、コンピューター上のあらゆる自動化を可能にする「汎用エージェント」へと昇華させると指摘。データジャーナリズムの例を挙げ、複雑なデータ処理ワークフローがMarkdownと簡単なPythonスクリプトで実現できる可能性を示唆しています。

従来のMCPが膨大なトークンを消費し、複雑なプロトコル定義を必要としたのに対し、SkillsはCLIツールのようにLLMが内部的にヘルプを参照し、使い方を自己学習するため、トークン効率が大幅に向上します。新しいCLIツールを実装せずとも、Markdownファイルでタスクを記述できるシンプルさが最大の利点であり、著者はこのシンプルさこそがSkillsの核心だと主張します。Skillsは他のLLMでも容易に利用可能であり、これにより「Skillsの爆発的な増加」が起こり、MCPブームを過去のものにするだろうと予測。LLMのツール実行能力を最大限に引き出す、複雑な部分を環境に委ねるこの設計は非常に賢明であると結論付けています。