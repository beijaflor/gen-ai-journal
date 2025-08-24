## 技術書知識を即戦力化！Sub Agent化から設計支援・レビューまでの最短フロー

https://zenn.dev/furedea/articles/53b5117b389454

技術書の知識をClaude CodeのSubagentへ変換する実践的なワークフローを構築し、設計支援やコードレビューの効率化を実現します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Claude Code, AIエージェント, 知識管理, コードレビュー, ソフトウェア設計]]

本記事は、技術書から得た知識が忘れ去られ、実務で活かされないという課題に対し、Claude CodeのSubagentを活用した画期的な解決策を提案します。Subagentは特定のコンテキストに特化した小型エージェントであり、人間の外付け記憶として技術知識を保持し、コード設計支援やレビューを自動化できる点が重要です。

著者は、このSubagentを効率的に作成・活用する一連のワークフローを詳述しています。まず、技術書のハイライトやWeb記事をObsidianのMarkdown形式で集約。豊富なプラグインにより、KindleのハイライトやWebコンテンツを容易にObsidianに取り込める点が強調されています。次に、これらMarkdownファイルからSubagentを自動生成するカスタムSlash Command「book2agent」を導入。ObsidianとClaude Code間の連携にはMCP Toolsを利用し、Local Rest API経由でドキュメント参照を可能にします。

実践例として、Clean Codeの原則を基にしたSubagentを作成し、FastAPIのコードレビューを行う様子が紹介されており、与えられた知識ベースのみに基づき、具体的かつ実践的な改善提案を行う能力を示します。

ワークフロー構築の中で得られたClaude Codeの知見として、ユーザーの確認なしにファイル書き込みが行われる挙動（特に検証フェーズを細かく設定した場合）や、Slash Commandの機能の柔軟性が言及されています。これにより、知識の定着と活用という開発者の長年の課題が、AIエージェントによる自動化と専門知識の外部化によって克服できる可能性を示し、抽象的な知識を具体的な開発プロセスに組み込む実践的な手段を提供します。