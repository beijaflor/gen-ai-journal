## ClaudeCode Workflow Studio - Claude Code用ビジュアルワークフローエディタ

https://github.com/breaking-brake/cc-wf-studio

**Original Title**: ClaudeCode Workflow Studio

複雑なAIエージェントのワークフロー構築を、ドラッグ＆ドロップの視覚的操作と自然言語による指示で簡素化するVS Code拡張機能を提供します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, MCP, VS Code Extension, AI Agents, Workflow Automation]]

Anthropicが提供するエンジニア向けCLIツール「Claude Code」の利用体験を劇的に向上させる、強力なビジュアルエディタが登場しました。この「ClaudeCode Workflow Studio」は、コードを書くことなく複雑なAIエージェントのオーケストレーションや条件分岐を含むワークフローを設計し、そのままClaude Codeで実行可能な形式でエクスポートできるVS Code拡張機能です。

筆者がこのツールを開発した背景には、CLIベースのClaude Codeが持つポテンシャルを最大限に引き出しつつ、エージェント間の連携や条件分岐といった複雑なロジックを直感的に管理したいというニーズがあります。従来、Claude Codeで高度な自動化を実現するには、`.claude`ファイルを手動で記述し、プロンプトやスキルの関係性を管理する必要がありましたが、本ツールはこれをGUI上のキャンバスで視覚化します。

特筆すべきは、単なるドラッグ＆ドロップエディタに留まらず、「Edit with AI」機能を搭載している点です。ユーザーは自然言語で「MCP（Model Context Protocol）を使用してPRレビューを行うワークフローを作って」といった指示を出すだけで、AIがキャンバス上にノードを配置し、ロジックを自動構築します。生成されたフローは、さらに自然言語で「エラーハンドリングを追加して」「出力をSlack形式にして」といった対話形式での微調整が可能です。

技術的な深みとして、Model Context Protocol（MCP）のネイティブサポートが挙げられます。外部APIやデータベース、ブラウザ操作（Playwright等）を行うMCPツールをノードとして組み込めるため、コード生成に留まらない「実務を遂行するエージェント」の構築が容易です。また、条件分岐（IfElse / Switch）やユーザーへの問いかけ（AskUserQuestion）といったノードにより、AIの自律的な判断と人間の介入をシームレスに結合できる設計になっています。

エンジニアにとっての重要性は、開発プロセスにおける「定型的な複雑タスク」の資産化にあります。作成したワークフローは`.claude/agents/`や`.claude/commands/`へワンクリックで書き出され、即座にCLIからスラッシュコマンドとして呼び出せます。さらにSlack共有機能も備えており、チーム全体でのワークフロー共有と再利用を促進します。ローカル完結型の設計（MCPサーバー等の外部通信を除く）であるため、セキュリティ面での懸念も最小限に抑えられています。

Claude Codeという強力なエンジンに「視覚的な設計図」と「AIによる構成支援」を加えることで、AI agentic workflowの構築速度を一段上のフェーズへ引き上げる、極めて実用性の高いツールと言えるでしょう。