## Build Slack agents with @vercel/slack-bolt

https://vercel.com/changelog/build-slack-agents-with-vercel-slack-bolt

Vercelが、Vercel AI Cloud上で堅牢なSlackエージェントを構築・デプロイするためのライブラリ`@vercel/slack-bolt`を公開しました。

**Content Type**: News & Announcements

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:2/5
**Main Journal**: 94/100 | **Annex Potential**: 89/100 | **Overall**: 68/100

**Topics**: [[Vercel, Slack Bots, AI Agents, AI SDK, Serverless Functions]]

Vercelは、堅牢なSlackエージェントをVercel AI Cloudにデプロイするための新しいライブラリ`@vercel/slack-bolt`を発表しました。このライブラリは、Node.js Requestオブジェクトを扱うあらゆるフレームワークや関数とシームレスに連携するため、Next.jsを含む既存のVercelプロジェクトへの統合が非常に容易です。特に注目すべきは、Vercel AI SDKとの密接な連携で、これにより開発者はOpenAI GPT-5などの大規模言語モデル（LLM）を活用した対話型AI機能をSlackボットに迅速に組み込むことができます。提供されているコード例では、Slackチャンネルのメッセージをリッスンし、AIによって生成されたテキストで応答するプロセスが、わずか数行で実現されています。

ウェブアプリケーションエンジニアにとって、この発表は大きな意味を持ちます。VercelのFluid compute、AI SDK、AI GatewayといったAI Cloudの強力なプリミティブをフル活用しながら、使い慣れたVercel環境でSlackボットを開発・運用できるためです。これにより、開発者はインフラの複雑さに煩わされることなく、生成AIを用いた高機能なSlackエージェントの構築に集中できます。既存のVercelベースのアプリケーションにAI駆動のワークフローや自動応答システムを導入したい場合、`@vercel/slack-bolt`は、その障壁を劇的に下げ、迅速なプロトタイピングから本番デプロイまでを支援する実践的なツールとなるでしょう。