## spec-workflow-mcpを使ってみたら気に入ったので、紹介する - yasuhisa's blog

https://www.yasuhisay.info/entry/2025/09/05/110633

`spec-workflow-mcp`は、LLM Agentと連携する仕様書駆動開発を、堅牢な状態管理と直感的なWebダッシュボードを通じて効率化し、開発者のワークフローを強化します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 80/100

**Topics**: [[LLM Agent, 仕様書駆動開発, 開発ワークフロー, Claude Code, 開発ツール]]

LLM Agentの進化によりコード生成は容易になったものの、完全なバイブコーディングでは仕様不適合や保守性の問題が生じがちです。特にClaude CodeのようなAgentはAuto Compact後にコンテキストを失いやすく、指示の精度が低下する課題がありました。本記事は、こうしたAgentとの協調開発における仕様書駆動開発の重要性を指摘し、その実践を強力に支援するツール`spec-workflow-mcp`を紹介しています。

`spec-workflow-mcp`は、特定のIDEに縛られず、汎用的なMCP（Multi-Capability Platform）として導入が容易な点が特徴です。`claude mcp add spec-workflow`コマンド一つで手軽にセットアップでき、既存のiTerm2/tmux環境で開発を進めたいエンジニアにとって大きなメリットとなります。

本ツールの最大の魅力は、その堅牢な設計と優れたUI/UXにあります。仕様の状態管理にはMarkdownではなくJSONとTypeScriptが用いられ、状態が壊れるリスクを低減し、信頼性の高い開発プロセスを実現します。さらに、`--dashboard`オプションで起動するWebサーバー型ダッシュボードは、作成した仕様書の一覧、レビュー状況、タスクの進捗を視覚的に提供します。これにより、LLM Agentが生成したコードのレビューが捗り、従来のdiffベースのレビューよりも効率的かつ正確なフィードバックが可能になります。

また、仕様書とタスク定義が永続化されるため、LLM Agentが途中でコンテキストを忘れても、明確な参照点があることで混乱を避け、作業をスムーズに再開できます。これは、LLM Agentの信頼性と生産性を向上させ、「次に何をすべきか」を人間が思考する負担を軽減する点で、開発ワークフローに革命をもたらします。特定のベンダーに依存せず、仕様書駆動開発を効率的に実践できる環境が整うことで、LLM Agentとのより堅牢で予測可能な協調開発が実現します。