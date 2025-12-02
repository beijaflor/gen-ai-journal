## TypeScriptでAIエージェントを構築する

https://speakerdeck.com/izumin5210/building-ai-agents-with-typescript

**Original Title**: Building AI Agents with TypeScript #TSKaigiHokuriku

TypeScriptとVercel AI SDKがAIエージェント開発に新たな道を開き、ウェブアプリケーション開発者が効率的に高度なエージェントシステムを構築できると提示します。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 80/100

**Topics**: [[AIエージェント, TypeScript, Vercel AI SDK, マルチエージェントシステム, 耐久性のある実行]]

本講演では、LayerXのizumin5210氏が、TypeScriptを用いてAIエージェントを構築する方法とその利点について解説しています。大規模言語モデル（LLM）の登場により、モデルが汎用的なREST APIとして利用可能になったことで、AI機能開発はPythonだけでなくTypeScriptにも大きく開かれたと著者は主張します。Webフロントエンドとの親和性、高い型安全性、そして既存のWebアプリケーション開発の知識を活かせる点が、WebアプリケーションエンジニアにとってTypeScriptを選択する大きなメリットです。

具体的には、`vercel/ai`ライブラリが、モデルプロバイダーの抽象化、エージェントループの簡易ラッパー、Webフロントエンドとの接続を簡素化する「薄い」ライブラリとして紹介されています。この「薄さ」が、内部の処理を追いやすく、比較的少ない知識でAIエージェントを構築できる理由です。例として、`streamText`を用いたツール呼び出しを含むチャットアプリケーションの実装や、Drizzle ORMによる履歴の永続化、そしてツール呼び出し結果を型安全に扱いUIに表示する手法が示されています。これにより、複雑なAIアプリケーションでも高いユーザー体験を提供できると著者は説明します。

さらに、ユーザーの質問に対して複数のエージェントが協調してリサーチを行う「Deep Research」のようなマルチエージェントシステムの構築方法も紹介されました。LangChainのOpen Deep Researchを参考に、ユーザー要件の明確化、調査指示書の生成、リサーチ監督、並列検索を行うサブエージェント、最終レポート生成といった各ステップがどのように連携するかが示されています。このような複雑なタスクでは、どこをLLMで処理し、どこを決定論的に処理するかという「タスク設計」が非常に重要であると強調されています。コンテキストの肥大化や、決定論的に処理できる部分を確率的なLLMに任せることのリスクを避けるためです。

また、Deep Researchのように処理時間が数分から10分程度かかる可能性のあるタスクでは、通信断やサーバー障害時に結果が失われることが問題となります。このため、TemporalやTrigger.dev、そしてVercelが開発中の`vercel/workflow`といった「Durable Execution（耐久性のある実行）」基盤に乗せる必要性が説かれています。`vercel/workflow`は、ワークフローを可視化し、Human-in-the-Loopや稼働中のワークフローへのメッセージ送信も可能にするため、AI時代のバックグラウンドジョブ基盤として非常に有望であると述べられています。

著者は、AIエージェント開発初心者は複雑に考えすぎず、タスクを分解し、既存のOSS実装を写経・移植することから始めることで、より実践的な学びが得られるとアドバイスしています。