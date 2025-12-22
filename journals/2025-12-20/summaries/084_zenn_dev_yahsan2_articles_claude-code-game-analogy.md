## ドラゴンを倒して覚える Claude Code - Commands, Skills, Subagents, Rules の違いと使い分け

https://zenn.dev/yahsan2/articles/claude-code-game-analogy

RPGゲームの比喩を通して、Claude Codeの主要な機能であるCommands、Skills、Subagents、Rules、そしてCLAUDE.mdの役割と使い分けを解説します。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 76/100 | **Annex Potential**: 75/100 | **Overall**: 88/100

**Topics**: [[Claude Code, LLM Agent Frameworks, Developer Workflows, Prompt Engineering, Context Management]]

本記事は、Claude Codeのカスタマイズで手が止まりがちなエンジニア向けに、Commands、Skills、Subagents、Rules、CLAUDE.mdといった各機能の概念と適切な使い分けをRPGゲームの冒喩で分かりやすく解説しています。

まず、**Commands**は、頻繁に行う指示や確認をスキップし、メインエージェント（主人公）に特定のタスクを効率的に実行させるための「何をやるか」を定義するものです。例えば、`/attack [敵の名前]`のように引数を渡し、定型作業を自動化します。次に**Skills**は、複雑な手順や専門知識をまとめて定義し、メインエージェントが「どうやるか」を詳細に教えなくても、スキル名だけで実行できるようにするものです。これにより、特定の能力を発動する際のコンテキスト（情報量）を節約できます。

さらに、**Subagents**は、特定の役割を持つ専門家として機能し、メインエージェントとは独立したコンテキストで動く「仲間」です。複数のスキルを組み合わせ、振る舞いを定義することで適切な判断をさせることができ、特に複数のタスクを並列で処理する際にその真価を発揮します。これにより、メインエージェントのコンテキスト汚染を防ぎ、効率的な役割分担が可能になります。

そして、**Rules**は特定のファイルパス（エリア）に適用されるルールを定義する「道の看板」のようなものです。そのエリアに入ったときに自動で読み込まれ、エージェントがその場で必要な前提条件や注意点を守るように促します。最後に**CLAUDE.md**は、プロジェクト全体の「世界観」や常に適用される前提条件を定義する場所であり、特定の機能に縛られない広範な指針を記述します。

著者は、これらの概念を明確に区別し、適切に組み合わせることで、AIエージェントの挙動をより効率的かつ柔軟に制御できると主張しています。これにより、煩雑な指示出しが不要になり、より複雑な開発タスクへの応用が可能になるため、Claude Codeを活用するWebアプリケーションエンジニアにとって実践的な指針となるでしょう。