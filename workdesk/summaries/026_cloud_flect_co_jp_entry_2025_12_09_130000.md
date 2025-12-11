## Prompt Injection の観点についてまとめてみる

https://cloud.flect.co.jp/entry/2025/12/09/130000

LLMを利用したサービス開発において、開発者はPrompt Injectionという固有のセキュリティリスクに対し、その攻撃経路と手法を理解し適切な防御策を講じる責任を負います。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Prompt Injection, LLMセキュリティ, セキュリティ対策, RAG, Jailbreaking]]

LLMを利用したサービスの開発では、従来のWebセキュリティと同様に、Prompt Injectionといった固有のセキュリティリスクへの対応が不可欠です。本記事は、Prompt Injectionへの耐性を検討する際の観点を体系的にまとめ、その重要性をウェブアプリケーションエンジニアに示します。

まず、システムへの攻撃経路を特定するため、Prompt Injectionを「直接的攻撃」と「間接的攻撃」の二種類に分類します。直接的攻撃はユーザーがLLMに悪意ある指示を直接入力する一般的な手法であり、間接的攻撃はLLMがRAGなどで参照するデータに悪意ある指示を埋め込む、よりテクニカルな手法です。開発中のシステムがユーザーからの直接入力とLLMが参照する外部データにどのように関与するかを特定することで、思考の足がかりを築くことを著者は推奨しています。例えば、公開チャットアプリが社内資料のみをRAGで参照する場合、直接的攻撃に焦点を絞って防御を検討できます。

次に、AmazonやPalo Alto Networksがまとめた一般的なPrompt Injectionの手法について詳細に解説します。主な手法には、LLMの役割を変更させる「Prompted Persona Switches」、悪意ある実行コードを生成させる「Code Injection」、指示を複数に分割して検出を回避する「Payload Splitting」、画像や音声などテキスト以外の媒体を利用する「Multimodal Injection」、他言語や絵文字、Base64などで指示を隠蔽する「Multilingual / Obfuscated」などが挙げられます。特に、現代の推論モデルがギャル文字などを正確に解釈できることから、巧妙な暗号化による攻撃の可能性も指摘されており、高度な推論機能が逆にセキュリティリスクを高める側面も強調されています。その他、「Model Data Extraction」「Template Manipulation」「Fake Completion」「Reformatting」「Exploiting LLM Friendliness and Trust」といった多岐にわたる攻撃手法も紹介されています。

Salesforceによる攻撃の「目的」に焦点を当てた分類も提示されており、こちらはTrust Layerの設計やLLMベースの意図理解による防御戦略に有用とされています。

LLMの柔軟性がセキュリティリスクの複雑性を増す中で、開発者はこれらの攻撃経路と具体的な手法を理解し、サービスへの信頼を破壊しないよう、適切な防御策を講じる知識を常に蓄えるべきだと著者は結論付けています。