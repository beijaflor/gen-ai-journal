## 90万人以上のユーザーからChatGPTやDeepSeekの対話データを盗む2つのChrome拡張機能が発覚

https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html

**Original Title**: Two Chrome Extensions Caught Stealing ChatGPT and DeepSeek Chats from 900,000 Users

悪質なChrome拡張機能が90万人以上のユーザーからLLMとの対話データを窃取し、AI利用における「プロンプト密猟」という新たなセキュリティ脅威の実態を露呈させている。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 94/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Chrome拡張機能, ChatGPT, セキュリティ, 機密情報漏洩, Prompt Poaching]]

サイバーセキュリティ研究者の調査により、Chromeウェブストアで配布されていた2つのAI関連拡張機能が、ChatGPTおよびDeepSeekにおけるユーザーの対話内容や閲覧中のURLを窃取し、外部サーバーへ送信していたことが判明した。対象となったのは「Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI」および「AI Sidebar with Deepseek, ChatGPT, Claude, and more.」で、これらは合計90万人以上のユーザーにインストールされていた。

これらの拡張機能は、インストール時に「匿名のアナリティクスデータ」の収集に対する同意を装いながら、実際にはブラウザのDOM（Document Object Model）を操作してLLMとの対話メッセージを直接抽出し、30分ごとに攻撃者の制御下にあるサーバーへ送信する仕組みを持っていた。OX Securityの研究者によれば、これらの拡張機能は「Chat with all AI models」という100万人規模の人気拡張機能を巧妙に偽装しており、インフラの隠蔽のために「Lovable」というAI搭載の開発プラットフォームを悪用してプライバシーポリシーをホストするなど、発覚を免れるための巧妙な工作も確認されている。

著者は、このようにブラウザ拡張機能を通じてAIのプロンプトを隠密に収集する手法を「Prompt Poaching（プロンプト密猟）」と定義し、これが企業スパイや知的財産窃盗の新たな強力な武器になると強く警告している。特にエンジニアや従業員が開発コードや社外秘のビジネス情報をLLMに投入する際、ブラウザ拡張機能がその全内容を傍受できる点は、組織にとって極めて深刻なセキュリティホールとなる。

また、この問題は悪意のあるマルウェアだけに留まらない。SimilarwebやStayfocusdといった数百万人のユーザーを抱える正規の拡張機能も、AIツールへの入力をトラフィック分析目的で収集し始めていることが報告されている。Similarwebの最新のプライバシーポリシーでは、AIに入力されたプロンプトやアップロードされたファイルが収集対象であることが明記されており、収益化を狙う企業による「データの合法的な搾取」が一般化しつつある。

筆者によれば、これはプロンプト密猟というトレンドの始まりに過ぎず、今後より多くの企業が同様の手法を採用することが予想される。ウェブアプリケーションエンジニアは、個人および組織のレベルで拡張機能の利用を厳格に管理し、たとえ「おすすめ（Featured）」バッジが付いているものであっても、ブラウザに不要な権限を与えないよう細心の注意を払うべきである。