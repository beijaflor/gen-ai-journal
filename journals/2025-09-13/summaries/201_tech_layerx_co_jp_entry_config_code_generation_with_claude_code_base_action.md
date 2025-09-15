## claude-code-base-action で設定ファイル自動生成のための Agentic Workflow を作る

https://tech.layerx.co.jp/entry/config-code-generation-with-claude-code-base-action

LayerXは、Claude CodeのSubagent機能を活用し、社内ツールの設定ファイルを自動生成するAgentic Workflowを構築し、手動運用の課題を解決しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AIエージェント, 自動コード生成, Configuration as Code, GitHub Actions, Claude Code / Subagents]]

LayerXのエンジニアリングブログは、社内ツール「ABAC Generator」におけるグループ管理設定ファイルの複雑な自動生成課題に対し、Claude CodeのAgentic Workflowを構築した事例を共有しています。SmartHR属性に基づくMicrosoft Entra IDグループの自動更新を担うこのツールは、手動でのTypeScript設定ファイル記述が非プログラマーにとって高い認知負荷となり、組織図の正確な理解が必要でした。

この課題解決のため、同社はGitHub Actions上で`claude-code-base-action`を活用。初期の直線的なWorkflow案から、より洗練されたSubagentベースのアプローチへと進化させました。特に重要なのは、設定生成Subagentの精度不足に直面した際、これを「`memberConditions`のみを生成するSubagent」と「主要なグループ設定を生成し、`memberConditions`の生成を委譲するSubagent」の二つに分割することで、安定した正確な出力を実現した点です。

このアプローチは、webアプリケーションエンジニアにとって、なぜ重要なのでしょうか。第一に、Infrastructure as CodeやConfiguration as Codeの価値がAI時代に大きく高まる中、内部ツールのようなニッチでドキュメントが少ない領域でも、AIエージェントが複雑な設定をコード化し、手動運用負荷を劇的に軽減できる可能性を示しています。第二に、LLMベースのエージェントの精度を向上させるための具体的な設計パターン、すなわち「複雑なタスクを独立した再利用可能なSubagentに分解する」というUNIX哲学的な手法の有効性を示唆しています。これは単なるプロンプトエンジニアリングを超え、より堅牢でスケーラブルなAIエージェントシステムを構築するための重要な知見となります。さらに、`CLAUDE_WORKING_DIR`を用いたモノレポでの安全な運用など、実践的なTipsも提供されており、日々の開発ワークフローにAIエージェントを組み込む際の具体的なヒントが得られるでしょう。複雑な業務設定から開発者を解放し、より本質的な課題解決に注力できる環境を整備する上で、この取り組みは極めて実践的かつ価値ある事例と言えます。