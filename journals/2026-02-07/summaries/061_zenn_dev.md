## Claude CodeのHooksをハックして自律駆動するマルチエージェントを作った

https://zenn.dev/zaico/articles/d6b882c78fe4b3

**Claude Code**の**Hooks**機能を拡張し、タスク分解から依存関係管理、自己修復までを自律的に行うマルチエージェントシステム「**ChainCrew**」の構築事例を詳解する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 92/100

**Topics**: [[Claude Code, AIエージェント, マルチエージェント, 自律駆動型開発, ChainCrew]]

**Claude Code**が提供する**Hooks**機能を活用し、複数のAIエージェントを協調させる自律駆動システム「**ChainCrew**」の実装記録です。**SessionStart**、**UserPromptSubmit**、**PostToolUse**、**Stop**という4つのフックポイントを使い、タスクの自動分解、セッションを跨いだ状態保持（**task_stack.json**によるスタック管理）、およびコーディングルールの自動適用を実現しています。特筆すべきは、実行中のエラーを**ISSUE**として自己検出し、依存関係を考慮しながらプログラムを修正する自己修復メカニズムです。

記事後半では、OpenH264のYUV444対応という具体的な開発事例を通じ、エージェントが誤った判断をした際の軌道修正プロセスや、65日間で約44億トークンを消費した際の詳細なコスト分析（API換算230万円に対し、**Claude Max**定額プランで大幅に抑制）を公開しています。標準のサブエージェント機能と比較して、**可観測性**と**制御性**に優れる点が大きなメリットとして示されています。

**Claude Code**のポテンシャルを最大限に引き出したいエンジニアや、実用的なAIエージェントの設計パターンと運用コストを学びたい開発者に強く推奨されます。