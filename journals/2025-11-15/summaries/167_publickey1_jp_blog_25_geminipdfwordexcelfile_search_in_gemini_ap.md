## GeminiにPDFやWord、Excel、テキストファイルなどの検索機能を組み込める「File Search in Gemini API」提供開始、フルマネージドなRAGシステムを提供

https://www.publickey1.jp/blog/25/geminipdfwordexcelfile_search_in_gemini_apirag.html

Google Cloudは、GeminiにPDFやWord、Excelなどの多様なファイルを読み込ませて検索可能にするフルマネージドなRAGシステム「File Search in Gemini API」の提供開始を発表しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Gemini API, RAG, ドキュメント検索, AI開発ツール, フルマネージドサービス]]

Google Cloudは、同社の生成AIサービスGeminiに、PDF、Word、Excel、プレーンテキストなど様々な形式のファイル検索機能を組み込める「File Search in Gemini API」の提供を開始しました。これは、企業がGeminiを社内ドキュメントに基づいて活用する際に不可欠なRAG（Retrieval-Augmented Generation）システムを、API操作だけで簡単に構築できるフルマネージドサービスとして提供するものです。

従来、RAGシステムを構築するには、ベクトルデータベースの準備、ファイルのチャンク化やエンベディングへの変換、インデックス作成などの前処理、プログラミングによる生成AIとの連携といった複雑な作業が必要でした。本APIはこれらの手間を大幅に削減し、開発者は外部サービスを組み合わせることなく、API経由で「ファイル検索ストア」を作成しファイルをアップロードするだけで、自動的にこれらのRAGプロセスが処理されます。アップロードされたファイルは自動的にチャンク化、エンベディング変換されインデックスが作成された後、48時間で削除されるため、データ管理の負担も軽減されます。

これにより、Geminiが指定されたストア内のドキュメントに対してセマンティック検索を実行し、社内固有の質問に正確に回答することが可能になります。さらに、回答の生成に使用されたドキュメントの引用情報が示されるため、ファクトチェックも容易になります。現時点では「gemini-2.5-pro」と「gemini-2.5-flash」の2つのモデルがサポートされており、Webアプリケーションエンジニアは、企業向けAIアプリケーションの開発において、RAGの導入障壁が大きく下がることで、より迅速かつ効率的に高度な情報検索機能を実装できるようになります。