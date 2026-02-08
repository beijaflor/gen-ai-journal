## UIデザインから実装までをAIエージェントに丸投げしてみた（ChatGPT → Google Stitch → Antigravity × Claude Opus 4.5） #MCP

https://qiita.com/kunitomo926/items/205aa17d0acc88a34bf4

AIエージェントとMCPを活用し、要件定義からFlutterアプリの実装までを完全に自動化する開発フローの実証を報告する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:3/5
**Main Journal**: 96/100 | **Annex Potential**: 96/100 | **Overall**: 72/100

**Topics**: [[MCP, Claude 4.5 Opus, Google Stitch, Antigravity, Flutter]]

本記事は、**ChatGPT**、**Google Stitch**、**Antigravity**を組み合わせ、UIデザインから**Flutter**によるアプリ実装までをAIエージェントのみで完結させる検証レポートである。著者は、**ChatGPT**で要件を言語化し、**Google Stitch**でワイヤーフレームを生成。さらに**MCP（Model Context Protocol）**を介して**Antigravity**と連携させ、**Claude 4.5 Opus**に実装を指示する一連のワークフローを実証している。

特筆すべきは、人間によるコーディングを介さず、わずか15分でシミュレーター上で動作する5画面分のプロトタイプが完成した点だ。**Antigravity**の**Agent Manager**が生成する**Implementation Plan**や**Task Walkthrough**の有用性と、**Claude 4.5 Opus**の正確なコード出力能力が、プロトタイピングの工数を大幅に削減できることを示唆している。また、**npx add-skill**を用いた**Google Stitch**の機能拡張（**design-md**, **stitch-loop**など）の手法も具体的に紹介されている。

最新のAIエージェントを活用した爆速でのMVP開発に関心があるエンジニアや、**MCP**を用いた開発環境の高度化を検討している開発者にとって、実践的なリファレンスとなる内容だ。