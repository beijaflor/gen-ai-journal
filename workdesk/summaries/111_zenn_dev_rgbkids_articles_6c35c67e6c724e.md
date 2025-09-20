## やってくる Vibe Design の波。AI時代のプロダクトはエンジニアだけでやっていく

https://zenn.dev/rgbkids/articles/6c35c67e6c724e

「Vibe Design」の台頭により、AIがプロダクト開発におけるデザイン工程をコード生成で担い、エンジニアが単独でプロダクトを完結させる新たな可能性を切り開く。

**Content Type**: ⚙️ Tools
**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 87/100 | **Overall**: 84/100

**Topics**: [[Vibe Design, AIデザイン生成, LLM比較, 画像生成AI, プロダクト開発ワークフロー]]

「Vibe Design」は、AIに指示するだけで、デザインをReactコンポーネントのような直接プログラムに組み込める形で生成させる新たな潮流です。これは、かつてエンジニアが単独でプロダクトを開発し、資金調達していたスタートアップの原点回帰を促し、Webアプリケーションエンジニアがデザインも含むプロダクト開発全体を完遂できる可能性を拓きます。

筆者は、自作のVibe Design System「desys」を用いて、GPT-5、Gemini 2.5 Pro、Claude Opus 4.1、Claude Sonnet 4といった主要LLMのデザイン生成能力を「夏の爽やかなデザイン」や「奇抜なUI」といった曖昧なプロンプトで比較検証しました。その結果、Claude Sonnet 4とGPT-5が比較的高いデザイン生成力を示しましたが、現在のLLM単体でのデザイン表現には限界があることも浮き彫りになりました。

特に注目すべきは、Googleの画像生成AI「Nano Banana (Gemini 2.5 Flash Image)」の活用法です。Nano Bananaは、複雑かつ抽象的な「Vibe」を驚くほど忠実にビジュアル化する高いデザイン解釈力と生成力を持つ一方で、直接コードを生成するのではなく画像を生成します。そのため、生成された画像をVRT（Visual Regression Testing）を使いながらコードに変換・調整するという、一歩踏み込んだワークフローが必要となります。

このVibe Designの進化は、エンジニア主導のプロダクト開発を加速させ、初期段階でのデザイナー依存を軽減する大きなインパクトを持ちます。特にNano Bananaのような画像生成AIとコード変換技術の組み合わせは、Webエンジニアがよりクリエイティブかつ効率的にプロダクトを具現化するための強力な武器となるでしょう。