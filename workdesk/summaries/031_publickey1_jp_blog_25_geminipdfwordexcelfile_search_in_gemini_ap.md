## GeminiにPDFやWord、Excel、テキストファイルなどの検索機能を組み込める「File Search in Gemini API」提供開始、フルマネージドなRAGシステムを提供

https://www.publickey1.jp/blog/25/geminipdfwordexcelfile_search_in_gemini_apirag.html

Google Cloudは、GeminiにPDFやWord、Excelなどのファイルをセマンティック検索可能なフルマネージドRAGシステム「File Search in Gemini API」の提供を開始しました。

**Content Type**: News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Gemini API, RAG, Google Cloud, ファイル検索, 生成AI]]

Google Cloudは、生成AI「Gemini」にPDFやWord、Excel、テキストファイルといった多様なドキュメント形式を読み込ませ、セマンティック検索を可能にするフルマネージドなRAG（Retrieval-Augmented Generation）システム「File Search in Gemini API」の提供開始を発表しました。

このAPIの登場は、企業がGeminiを社内ドキュメント活用に用いる際の大きな課題を解消するものです。記事によれば、従来、Geminiに社内固有の質問へ回答させるためにはRAGシステムの構築が必要でしたが、そのためには専用サービスやベクトルデータベースの準備、前処理、プログラミングなど、複雑な作業が伴いました。

「File Search in Gemini API」は、これらの外部サービスを組み合わせる手間なく、APIを操作するだけでRAGシステムを構築できる点が最大の特長です。ユーザーは、検索対象ファイルを保存する「ファイル検索ストア」を作成し、そこにファイルをアップロードするだけで、RAGシステムの基盤を構築できます。アップロードされたファイルは自動的にチャンク化され、ファイル検索エンベディングに変換されてインデックスが作成されるため、Geminiは指定されたファイル検索ストア内で高度なセマンティック検索を実行し、関連情報を迅速に見つけ出せるようになります。

さらに、検索結果には回答生成に使用されたドキュメントの引用情報が含まれるため、ファクトチェックが容易になり、企業での信頼性の高いAI活用が促進されます。現在、「gemini-2.5-pro」と「gemini-2.5-flash」モデルをサポートし、PDFやWord、Excel、JavaScript、JSON、HTML、Markdownなど多岐にわたるファイル形式に対応しています。これにより、Webアプリケーションエンジニアは、複雑なRAGインフラ構築から解放され、より迅速かつ効率的にGeminiを活用した高精度な情報検索・応答システムを開発できるようになるでしょう。