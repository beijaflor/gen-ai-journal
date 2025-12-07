## 僕のClaude Code Plugin紹介 ~skills/web-search~

https://qiita.com/getty104/items/7df76975a8c1c23396e3

Claude CodeのPlugin機能を用いて、Gemini CLIを活用した高品質なWeb検索Skill「skills/web-search」を実装し、その詳細と効果的な利用法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 94/100 | **Overall**: 72/100

**Topics**: [[Claude Code, AIエージェント, Plugin, Skills, Gemini CLI, Web検索]]

筆者は、Claude CodeのPlugin機能を利用して、カスタムコマンド、サブエージェント、Skillsなどをひとつのパッケージとして配布する自身の環境をGitHubで公開しており、その一部である「skills/web-search」を紹介している。

Skillsとは、Claude Codeが特定のタスクを実行する際に参照できる、再利用可能な知識や手順をまとめたもので、主にMarkdownファイル（SKILL.md）として定義される。筆者によれば、SkillsはClaude Code自身が参照する知識ベースとして機能し、関連スクリプトを含むことで、複雑なワークフローや定型作業を一貫性のある方法で自動化できる点が重要である。これにより、Claude Codeは「どのような時に何をすべきか」をルールベースで定義し、実行することが可能となる。

今回紹介される「skills/web-search」は、Claude CodeのデフォルトWeb検索ツールよりも「大規模で高品質な検索」を提供することを目的に開発された。その処理の核となるのは、Gemini CLIを用いたWeb検索であり、Google検索を介して広範かつ質の高い情報収集を可能にする。このSkillの活用により、Next.js 15の新機能やReact QueryのAPIドキュメントといった最新技術情報の取得、TypeScriptの型エラー解決方法の調査（Stack OverflowやGitHub Issuesからの情報含む）、業界ニュースや製品アップデートの収集、ベストプラクティスや実装方法の調査、ViteとWebpackの違いといった複数の技術比較分析が可能になる点が著者の提示する重要なメリットだ。

効果的な利用のためには、Claude CodeのCLAUDE.mdファイル内で明示的に「skills/web-search」を呼び出すよう指示することを著者は推奨している。例えば、「Next.js 15の新機能について公式ドキュメントや技術記事から詳しく調べてください」といった具体的なリクエストに対し、自動的にこのSkillが起動し、Gemini CLIを用いたWeb検索が実行される仕組みとなっている。ただし、利用にはGemini CLIの事前セットアップが必要となる。

スクリプトの実装自体はシンプルで、Geminiコマンドに検索クエリを渡す形を採用している。筆者は、Skillsを用いることで、MCP（Multi-Agent Communication Protocol）やサブエージェントでは実現が難しい「よしなにスクリプトを実行する」「よしなにワークフローを実行する」といった柔軟な自動化が可能になることを強調し、その有用性を訴えている。