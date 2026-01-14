## Claude CodeのAgent Skillでgit commitを自動化する

https://zenn.dev/saka1/articles/647a177cc5f7b8

Claude Codeの「Agent Skill」機能を活用し、ステージング済みの変更内容からConventional Commits準拠のメッセージを自動生成してコミットまで完結させるワークフローを構築する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Claude Code, Agent Skill, Git automation, Conventional Commits, Prompt Engineering]]

Claude Codeの「Agent Skill」機能を活用し、Gitのコミット作業を効率化する具体的な手法が紹介されています。筆者は、`git diff`の内容を解析して適切なコミットメッセージを生成し、そのまま実行まで行うスキル「git-cm」を開発しました。

このスキルの核心は、`SKILL.md`に定義された自然言語によるワークフローにあります。具体的には、まずステージング済みの変更を確認（`git diff --cached`）し、差分を分析。その後、Conventional Commits形式に従ってメッセージを生成し、`git commit`を直接実行するという手順が自動化されています。

筆者は設計において、AIと人間の役割分担を明確にすることを重視しています。「コミットに何を含めるか（`git add`）」は依然として人間の責務とし、AIは「メッセージの考案とコマンド実行」のみを担当させることで、開発フローの制御権を人間が保持しつつ省力化を実現しています。もしAIが不適切なメッセージを作成しても、後から`commit --amend`で修正可能という運用の容易さも考慮されています。

また、プロンプトの工夫により「日本語で」「詳細を」といった柔軟な指示にも対応可能です。情報の詳細度や言語を状況に応じて使い分けられるため、ドキュメントの更新からコードの修正まで幅広く対応できます。さらに、スラッシュコマンド（`/git-cm`）による明示的な呼び出しに限定することで、予期せぬタイミングでの自動コミットを防ぐ安全策も講じられています。

Claude Codeを単なるチャットUIとしてではなく、特定の開発タスクに最適化されたエージェントとしてカスタマイズするこの手法は、AIとの協働における実用的な指針となります。定型的なコミット作業の負担を減らしつつ、Conventional Commitsのような標準的な形式を維持したいエンジニアにとって、非常に有益なツール拡張例と言えるでしょう。