## bash-tool経由でAI SDKエージェントにおける「スキル」の利用が可能に

https://vercel.com/changelog/use-skills-in-your-ai-sdk-agents-via-bash-tool

**Original Title**: Use skills in your AI SDK agents via bash-tool

AI SDKエージェントによる、サンドボックス環境でのBash実行とファイルシステム操作を統合した「スキル」機能の利用を可能にします。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 85/100 | **Overall**: 82/100

**Topics**: [[AI SDK, bash-tool, AI Agents, Sandbox Runtime, Vercel]]

Vercelは、**AI SDK**のエージェントが**bash-tool**を通じて「スキル（Skills）」を扱える機能を導入しました。これにより、エージェントはファイルシステムのコンテキスト、**Bash**実行権限、およびサンドボックス化されたランタイムアクセスを組み合わせた高度な操作が可能になります。開発者は、**experimental_createSkillTool**を用いて特定のディレクトリからスキルを検出し、**createBashTool**と組み合わせることで、エージェントに一貫したコンテキスト提供と安全な実行環境を付与できます。

本アップデートの特筆すべき点は、公開されている既存のスキルを活用できるだけでなく、独自のプロプライエタリなスキルをプライベートに定義・利用できる柔軟性にあります。分離された実行モデルをベースにしているため、機密性を保ちながら複雑なタスクを自動化できます。

**AI SDK**を用いてコード操作やサンドボックス内での実行を伴うエージェントを構築しているエンジニアにとって、スキルの再利用性と安全性を高めるための実用的なアップデートです。