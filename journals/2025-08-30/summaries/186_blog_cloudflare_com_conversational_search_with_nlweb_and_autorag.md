## Make Your Website Conversational for People and Agents with NLWeb and AutoRAG

https://blog.cloudflare.com/conversational-search-with-nlweb-and-autorag/

Cloudflareは、ウェブサイトを人間とAIエージェントの両方にとって会話型にするため、MicrosoftのNLWeb標準とAutoRAGの統合を発表しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:3/5
**Main Journal**: 87/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Conversational AI, RAG, AIエージェント, セマンティック検索, Cloudflare Workers]]

ウェブサイトの検索体験は、ChatGPTのようなAIシステムの登場により根本的に変化しました。従来のキーワード検索は古く、ユーザーは質問をすれば直接回答を得られる「アンサーエンジン」を求めています。さらに、ウェブサイトにはAIエージェントという新たな訪問者が現れており、彼らも構造化された方法で情報にアクセスする必要があります。

Cloudflareは、この課題を解決するため、Microsoftが開発したオープン標準「NLWeb」と、自社のマネージド検索エンジン「AutoRAG」の統合を発表しました。NLWebは、ウェブサイト上で自然言語クエリを可能にし、AIエージェント向けのModel Context Protocol (MCP) サーバーとしても機能します。

AutoRAGは、ウェブサイトを自動的にクロールし、コンテンツをR2に保存後、マネージドなベクターデータベースに埋め込みます。Workers AIを通じてモデル推論と埋め込みを提供し、AI Gatewayで利用状況を監視できます。これにより、ウェブサイト運営者はインフラ管理の負担なく、会話型検索の完全なパイプラインを構築できます。

この統合により、ウェブサイトを「ワンクリック」で会話型に変換できます。AutoRAGがサイトをクロール・インデックス化し、Cloudflare Workerをデプロイします。このWorkerはNLWeb標準を実装し、ユーザー向けの会話型UIを提供する`/ask`エンドポイントと、信頼できるAIエージェント向けの構造化アクセスを提供する`/mcp`エンドポイントを公開します。

Cloudflareは、AutoRAGの機能強化として、大規模な動的ウェブサイトを処理できるよう、JobManagerとFileManagerという二つのDurable Objectを導入し、データ同期の信頼性とスケーラビリティを向上させました。これにより、ウェブサイト自体がRAGの第一級データソースとなり、人間とAIエージェントの両方にとって、より豊かで効率的な情報アクセスが可能になります。ウェブサイトを単なる情報源ではなく、「対話可能な知識ベース」へと進化させることが、本ソリューションの核心です。