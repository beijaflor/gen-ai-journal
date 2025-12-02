## Qwen-Image-Edit-2509をdatabricks notebookで動かしてみました。

https://techblog.cccmkhd.co.jp/entry/2025/11/18/145109

CCCMKホールディングスのAIエンジニアが、Alibaba Cloud開発の画像編集AIモデル「Qwen-Image-Edit-2509」をDatabricks Notebook環境で検証し、その高い性能と画像生成パラメータ`true_cfg_scale`の挙動を詳しく解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Qwen-Image-Edit-2509, Databricks Notebook, 画像編集AI, Classifier-Free Diffusion Guidance, true_cfg_scaleパラメータ]]

CCCMKホールディングスのAIエンジニアが、Alibaba Cloudが開発した画像生成モデル「Qwen-Image」をベースに画像編集機能が拡張された最新版「Qwen-Image-Edit-2509」をDatabricks Notebook環境（A100 GPU 1台）で試用し、その高性能に驚きを示しています。特に画像内での自然なテキスト描画能力が高く、英語と中国語に加えて日本語でも一定の性能を発揮すると評価しており、ウェブアプリケーションに組み込む際のテキストを含む画像処理の可能性を示唆しています。

記事では、Databricks Notebook上でQwen-Image-Edit-2509を動かすための具体的な手順が紹介されています。これには、最新版の`diffusers`と`transformers`のインストール、モデルのダウンロード、そして`torch_dtype=torch.bfloat16`を指定したパイプラインの初期化が含まれ、開発者が容易に環境を構築できるよう詳細なコードスニペットが提供されています。

さらに、プロンプトによる画像編集の例として、「け」の文字色を赤に変更する、背景を雪景色に変更するといった操作が実行され、モデルが高い忠実性で指示に従う様子が視覚的に示されています。一方で、`width`や`height`パラメータで画像サイズを変更すると生成画像の品質が低下したり、プロンプトへの追従性が損なわれる場合があるという実用的な注意点も指摘しており、アプリケーション開発時の設計に影響を与える重要な知見です。

特に注目すべきは、画像生成時に指定する`true_cfg_scale`パラメータに関する詳細な解説とその効果検証です。このパラメータは「Classifier-Free Diffusion Guidance (CFG)」に基づき、プロンプトが画像にどれだけ強く影響を与えるかを制御します。筆者は、CFGが生成プロンプトとネガティブプロンプトそれぞれの推論結果からノイズの差分を求め、それに重みをかけて全体のノイズに加算する仕組みであることを説明。このため、`true_cfg_scale`を使用する際には`negative_prompt`の指定が不可欠であると強調しています。異なる`true_cfg_scale`値での画像比較を通じて、値が低いとフォトリアルで全体と調和した画像が、高いとプロンプトの指示に忠実だが品質が低下する傾向があることを示し、用途に応じてこのパラメータを調整する必要があるとの結論を導き出しています。

著者は、Qwen-Image-Edit-2509が非常に高品質でプロンプトに忠実であると総括しつつ、日本語テキストの扱いに課題が残るケースも認めており、今後はLoRAのような技術による解決策を検討していくとしています。これは、高度な画像編集機能をWebアプリケーションに統合しようとするエンジニアにとって、モデルの選定やチューニング、そして多言語対応における現実的な課題と将来の展望を示唆する貴重な情報です。