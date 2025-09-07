## AI コーディングエージェントの管理を行う Vibe Kanban を試してみた

https://azukiazusa.dev/blog/coding-agent-management-vibe-kanban/

Vibe Kanbanは、AIコーディングエージェントのタスク管理をカンバン方式で効率化し、人間による進捗監督を支援するツールを詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Vibe Kanban, AI Coding Agents, Kanban Task Management, Git Worktree, MCP Server Integration]]

「AI コーディングエージェントの管理を行う Vibe Kanban を試してみた」の記事は、AIエージェントを活用した開発ワークフローにおける新たな管理ツール「Vibe Kanban」を紹介しています。開発者の仕事がコード生成からAIエージェントのレビュー、設計、管理へとシフトする中で、Vibe Kanbanはカンバン方式のUIでタスクを効率的に管理し、人間がAIエージェントの進捗を監督することを可能にします。

なぜこれが重要かというと、AIエージェントは高速にコードを生成する一方で、その品質、セキュリティ、プロジェクトガイドラインへの準拠を人間が確認する必要があるためです。Vibe Kanbanは、Codex, Claude Code, Gemini CLIなどの主要AIエージェントをサポートし、複数のタスク並列実行、Web UIでのステータス確認、MCPサーバーの一元管理といった特徴を持ちます。

具体的なワークフローとして、npmでの簡単なインストール後、既存プロジェクトまたは新規プロジェクトを選択し、タスクを作成します。AIエージェントはGit Worktreeを使用して分離されたブランチで作業を進め、タスクの進行状況は「TO DO」「In Progress」「Review」「Done」のレーンで視覚的に追跡できます。特に重要なのは「Review」レーンで、AI生成コードの差分を確認し、必要に応じてチャット形式で修正指示を出すことが可能です。GitHub連携によりプルリクエストの作成やマージもスムーズに行え、完了したタスクを容易に本流に統合できます。

さらに、Vibe Kanban自体をMCPサーバーとして利用することで、Claude Desktopのような他のAIエージェントからプロジェクトやタスクを管理できる点も注目に値します。これにより、AIエージェント間の連携を強化し、より高度な自動化と管理が期待されます。開発者は、AIエージェントを効果的に制御し、生成されるコードの品質を維持するための実用的な手段として、Vibe Kanbanを検討する価値があるでしょう。ただし、セキュリティ上のリスクを考慮し、隔離された環境での運用が推奨されています。