## Claude Codeのカスタマイズガイド：Rules、Skills、Subagents、MCPの最適配置

https://marioottmann.com/articles/claude-code-customization-guide

**Original Title**: Claude Code Customization: When to Use Rules, Skills, Subagents, and MCPs

Claude Codeを効率的に運用するための5つのカスタマイズ階層を定義し、プロジェクトの文脈や要件に応じた最適な設定手法を体系化する。

**Content Type**: 📖 Tutorial & Guide
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[Claude Code, MCP, AIエージェント, 開発ワークフロー, Anthropic]]

Claude Code（Anthropicが提供するCLI型AIコーディングエージェント）を、単なるチャットツールから高度にカスタマイズされた開発パートナーへと進化させるための具体的なフレームワークを提示している。著者は、カスタマイズを「内部階層（Claudeの思考設定）」と「外部階層（ツール接続）」の2つに大別し、さらに内部を4つのレイヤーに整理するメンタルモデルを推奨している。

内部階層の基盤となるのは、すべての会話で参照される『CLAUDE.md』だ。著者はこれを「従業員ハンドブック」に例え、プロジェクトの標準規約やスキルの目次を記すべきだと述べている。一方、特定のドメイン知識（例：デザインシステムやDBパターン）は『Rules』として.claude/rules/に配置し、ファイルパスによるフィルタリングを活用して、必要な時だけ読み込ませることでコンテキストの純度を保つ。反復的な作業（例：バックエンド構成の決定や法務ページ作成）は、ユーザーがコマンドで呼び出す『Skills』として定義する。Skillsは複数のマークダウンファイルに分割し、決定ロジックやコードテンプレートを分離して管理することが保守性の向上に繋がると説いている。さらに、大規模なリファクタリングやセキュリティ監査のような複雑な自律タスクは、Claudeが自ら判断して起動する『Subagents』に委任させる。

外部との接続には『MCP（Model Context Protocol）』を活用し、GitHubやデータベース、Slackといったツールへの「手」をClaudeに与える。筆者は、これら5つのレイヤーを使い分けることで、「毎回スタックの説明を繰り返す」という非効率を排除し、AIがプロジェクトの文脈を深く理解した状態で動作する環境が構築できると主張する。特に、すべての指示を1つのルールファイルに詰め込むアンチパターンを警告し、適切な階層化こそが、コンテキストの汚染を防ぎつつClaude Codeの真のポテンシャルを引き出す鍵であると結論づけている。