## MCPツール棚卸しによるClaude Codeのコンテキスト最適化

https://zenn.dev/medley/articles/optimizing-claude-code-context-with-mcp-tool-audit

Claude CodeでMCPツールがコンテキストを過剰消費し性能低下を招く問題を改善するため、不要なツールの削除や無効化を通じたコンテキスト最適化戦略を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Claude Code, MCP Tools, Context Optimization, AI Agent Performance, 開発ワークフロー]]

Claude CodeのようなAIコーディングエージェントにおいて、MCP（Model Context Protocol）ツールの安易な追加がコンテキストの過剰消費を引き起こし、エージェントの応答精度を著しく低下させる「コンテキスト腐敗」という深刻な問題に対処する。Anthropic社の指摘にもある通り、コンテキストはモデルの「アテンション・バジェット」であり、有限かつ重要なリソースである。筆者の環境では、全コンテキストの約30%をMCPツールが占有し、対話やファイル読み込みに利用可能な「Free space」が大幅に減少していた。

この記事は、ウェブアプリケーションエンジニアがAIエージェントの性能を最大限に引き出すための実践的な最適化手法を提示する。まず、`claude /context`コマンドを用いて現在のコンテキスト使用状況を可視化し、SentryやCircleCIなど使用頻度の低い MCP ツールが大量のトークンを消費している実態を明らかにする。そして、これらのツールを削除することで、MCPツールのコンテキスト占有率を30.3%から3.2%へと劇的に削減し、使用可能な「Free space」を27%以上増加させることに成功した。

この経験に基づき、MCPツールの効率的な運用として以下の三点が推奨される。第一に、特定のタスクでのみ必要なツールは、タスク開始時に `claude add mcp` で追加し、完了後に `claude remove mcp` で削除する運用。第二に、頻繁に使うが一時的に不要なツールは `/mcp` コマンドから無効化する機能の活用。これにより設定を維持しつつ、コンテキスト消費を抑制できる。第三に、`/context` コマンドを定期的に実行し、コンテキスト使用状況を常に把握する習慣を付けること。これらの具体的な対策を講じることで、AIエージェントが持つ有限なコンテキストリソースを効果的に管理し、その潜在能力を最大限に引き出すことができる。これは、より効率的で応答性の高いAgentic Codingを実現するために不可欠な知見となるだろう。