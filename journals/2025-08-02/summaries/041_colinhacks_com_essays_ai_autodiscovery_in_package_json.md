## Making AI resources auto-discoverable via package.json

https://colinhacks.com/essays/ai-autodiscovery-in-package-json

提案された`package.json`の規約は、AIエージェントによるJavaScriptライブラリのリソース自動発見を可能にし、開発効率を革新します。

**Content Type**: Technical Reference

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[AI Agent Discovery, Package.json convention, Library documentation, RAG, Developer tools integration]]

この記事は、JavaScriptライブラリがそのAI関連リソースをAIエージェントから自動的に発見可能にするための新しい`package.json`の規約を提案しています。提案されるのは、AIフレンドリーなドキュメントのサイトマップである`llms.txt`へのURLを指す`llms`フィールド、ライブラリの全ドキュメントを含む`llms-full.txt`ファイルへのURLを提供する`llmsFull`フィールド、そしてQ&A機能を提供するMCP（Model Communication Protocol）サーバーへのURLを指す`mcpServer`フィールドの3つです。

この規約は、AIエージェントがライブラリのAPIを効率的に理解し、活用できるようにすることで、開発における「鶏と卵」問題を解決しようとしています。既存の`AGENTS.md`がコードベース内部の操作方法を指示するのに対し、この提案はライブラリの公開APIと機能をエージェントに「広告」することを目的としています。ウェブアプリケーションエンジニアにとって、この規約の普及は計り知れない価値があります。AIによるコード補完、質問応答、デバッグ支援が、ライブラリ固有の知識をより正確かつ効率的に活用できるようになり、開発ワークフローが劇的に改善される可能性を秘めています。これは、AIを活用した開発環境において、ライブラリの利用効率を高めるための重要な一歩となるでしょう。