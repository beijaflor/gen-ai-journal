## 実はマルチモーダルだった。ブラウザの組み込みAI🧠でWebの未来を感じてみよう #jsfes #gemini

https://speakerdeck.com/n0bisuke2/burauzanozu-miip-miai-dewebnowei-lai-wogan-zitemiyou-number-jsfes

ブラウザ組み込みAIであるGemini NanoをWeb API経由で活用することで、Webアプリケーションの新たな可能性が拓かれることを解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[ブラウザAI, Gemini Nano, Web API, クライアントサイドAI, マルチモーダル]]

このプレゼンテーションは、JavaScript祭2025での発表を基に、ブラウザに組み込まれたAI（特にGemini Nano）をWeb APIを通じて活用し、Webの未来をどのように形作るかを探ります。著者は、Chromeに組み込まれたAIを活用することで、これまでサーバーサイドでしか実現できなかった多様なAI機能がクライアントサイドで直接利用可能になる点を強調しています。

主なポイントは以下の通りです。

*   **ブラウザ組み込みAIの登場**: ChromeにはGemini NanoなどのLLMが組み込まれつつあり、Web APIを通じてJavaScriptからアクセスできるようになります。これにより、ユーザーのデバイス上でAI処理が完結するため、プライバシー保護、低コスト、高速な応答が可能になります。
*   **多種多様なAI API**: `Prompt API`が核となり、テキスト生成、書き換え、校正、翻訳、言語検出、要約といった特化型API（`Writer API`、`Rewriter API`など）が提供されます。特に`Prompt API`は、テキストだけでなく画像などのマルチモーダル入力に対応しており、その汎用性が大きな魅力です。
*   **実践的な活用例と制限**: `Prompt API`はJSON出力にも対応しており、構造化されたデータ生成にも利用できます。しかし、Gemini Nanoにはトークン数に実質的な制限があるため、大規模な処理には不向きであり、部分的な要約やシンプルなテキスト処理に適しています。また、モデルの初期ダウンロードが必要で、デバイスのスペックによってパフォーマンスが異なる点も考慮が必要です。
*   **Project FuguとWebの拡張**: ブラウザがOSやハードウェアの機能にアクセスする「Project Fugu」の流れの中で、AI機能もブラウザの持つ強力な能力の一つとして位置づけられます。これにより、Webアプリケーションがカメラやセンサー、生体認証といったデバイス固有の機能とAIを連携させ、よりリッチでインタラクティブな体験を提供できるようになります。

著者は、これらのブラウザ組み込みAIとWeb APIの進化が、Web開発者が「AIネイティブ」なアプリケーションをブラウザ上で直接構築できる新たな時代を切り開くと主張しており、クライアントサイドAIの可能性に大きな期待を寄せています。