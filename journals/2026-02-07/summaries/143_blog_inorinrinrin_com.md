## Selenium作者によるAIと人間のためのブラウザ操作自動化ツール Vibium を使ってみる

https://blog.inorinrinrin.com/entry/2026/02/02/185352

解説する、Selenium作者によるAIエージェント対応のブラウザ操作自動化ツール「Vibium」の概要とJSを用いた具体的な実装手順を。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Vibium, Selenium, MCP, ブラウザ自動化, Claude Code]]

**Selenium**の作者Jason Huggins氏が新たに開発した、AIエージェント向けのブラウザ操作自動化ツール**Vibium**の概要と実践的な使用法を解説。単一のバイナリにブラウザのライフサイクル管理、**WebDriver BiDi**プロトコル対応、さらに**MCP (Model Context Protocol)**サーバー機能を統合しており、**Claude Code**などのMCPクライアントから設定不要でブラウザを操作できる点が最大の特徴となっている。

記事ではJS/TS（**vibium**パッケージ）を用いた具体的な自動化シナリオを例示。**vibe.launch()**による起動から、**vibe.find()**を用いた要素特定、**vibe.screenshot()**による検証、さらには**vibe.evaluate()**による動的なDOM操作まで、直感的なAPI群によるワークフローを紹介している。セレクトボックスの操作など一部泥臭い実装が必要な箇所もあるが、人間とAIがツールを共用するという設計思想は、今後の自動化ツールの標準となる可能性を秘めている。

既存の**Selenium**や**Playwright**に代わる、AIエージェント連携を前提とした軽量な自動化基盤を求めている開発者や、**MCP**を利用したブラウザ操作を試したいエンジニアは必読だ。