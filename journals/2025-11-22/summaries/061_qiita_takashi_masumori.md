## Copilot Studio でエージェントフローにファイルを渡す #PowerAutomate

https://qiita.com/Takashi_Masumori/items/dd5698bf0064f42e9db3

著者は、Copilot StudioからAIプロンプトへの直接ファイル連携で情報抽出が期待通りにいかない場合がある問題に対し、エージェントフローを介してOCRでテキストを抽出しプロンプトに渡す具体的な回避策を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:3/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 80/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Copilot Studio, Power Automate, OCR, ファイル連携, エージェントフロー]]

この記事は、Copilot Studioを利用する際、チャットで受け取ったファイルを直接AIプロンプトに渡しても、期待通りに情報が抽出されないケースがあるという課題に対する実践的な解決策を提示しています。著者は、この「クセ」とも言える挙動により、多くのユーザーがつまずく可能性があると指摘しています。

この問題の解決策として紹介されているのは、一度エージェントフロー（Power Automateを介したものと推測される）を挟み、AIモデルのOCR機能を使ってファイルからテキスト情報を抽出し、その結果をAIプロンプトに渡すという手法です。

具体的な手順としては、まずエージェントフロー側でファイルを入力として受け取り、それをOCRに渡し、抽出結果を返します。次に、エージェント側のトピックでは、質問ノードでファイルを受け取る設定をオンにし、受け取ったファイルを`{ contentBytes: Topic.Seikyu.Content, name: Topic.Seikyu.Name }`という特定の形式でエージェントフローに渡します。この方法により、ファイルを直接プロンプトに渡す場合に比べて、より確実に目的の情報を抽出できるようになります。

このアプローチは、Copilot StudioとPower Automateを組み合わせた開発において、ファイルの取り扱いにまつわる一般的な課題を克服し、AIプロンプトの精度と信頼性を向上させるための重要なヒントとなるでしょう。