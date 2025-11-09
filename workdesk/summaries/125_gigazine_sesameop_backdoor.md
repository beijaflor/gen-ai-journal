## OpenAIのAPIがハッカーのバックドアに悪用されているとMicrosoftの研究チームが報告

https://gigazine.net/news/20251106-sesameop-backdoor-openai-assistants-api/

Microsoftは、ハッカーがOpenAIのAssistants APIをバックドア型マルウェア「SesameOp」のコマンド＆コントロールチャネルとして悪用し、長期的なスパイ活動を行っていると報告しました。

**Content Type**: News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[マルウェア, バックドア, OpenAI API, Assistants API, サイバーセキュリティ]]

Microsoftのサイバー脅威対応チームDARTが、OpenAIのAssistants APIを悪用する新たなバックドア型マルウェア「SesameOp」を発見しました。このマルウェアは、侵害した環境内で長期的なスパイ活動を行うため、OpenAIのAPIをコマンド＆コントロール(C2)チャネルとして利用しています。

SesameOpは、本来エンタープライズクライアントがAIアシスタントを構築するための開発ツールであるAssistants APIを悪用し、圧縮・暗号化されたコマンドを取得し、感染システム上で実行します。収集した情報は、対称・非対称暗号化を組み合わせて暗号化され、同じAPIを介して外部に送信されます。これにより、ハッカーは従来の方法に頼ることなく、AIツールを介して密かに通信し、悪意ある活動を指揮できるのです。

この手口の重要な点は、OpenAIプラットフォームの脆弱性や設定ミスを悪用したものではなく、Assistants APIに組み込まれている正当な機能を悪用している点にあります。この事実から、脅威アクターが新たな技術の意図せぬ使われ方を常に模索していることが浮き彫りになります。

Webアプリケーションエンジニアの視点から見ると、これはAI関連APIの利用における新たなセキュリティリスクを示唆しています。AIを活用したアプリケーションを開発・運用する際には、単にAPIのセキュリティだけでなく、その「利用方法」自体が悪用されないかという視点も不可欠です。現在Assistants APIは2026年8月に廃止され、Responses APIに引き継がれる予定ですが、APIの選定と設計において、通信経路としての側面をより深く考慮する必要があることを警告しています。MicrosoftとOpenAIは連携して、悪用されたアカウントとAPIキーを無効化しています。