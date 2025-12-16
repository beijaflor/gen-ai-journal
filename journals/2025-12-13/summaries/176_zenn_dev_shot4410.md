## テセウスのTransformer

https://zenn.dev/shot4410/articles/5354ce65907e15

現在のLLMで採用されているTransformerが、2017年に提案されたオリジナル構造からどのように進化し、その各モジュールの変更が学習挙動や性能にどのような影響を与えているかを詳細に解説します。

**Content Type**: 🔬 Research & Analysis
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 89/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[Transformerアーキテクチャ, 大規模言語モデル, 自己注意機構, 正規化手法, 勾配消失問題]]

この記事は、「テセウスの船」の問いかけになぞらえ、現在のLLMで広く採用されているTransformerモデルが、2017年に発表されたオリジナルの構造とは大きく異なっている点を詳述します。著者は、この進化が学習挙動や予測性能に与える影響について、各モジュールの変更点とその目的を解説しています。

主な変更点として、まずResidual接続とNormalizationの位置が挙げられます。オリジナルがPost-Layer Normalization (Post-LN) であるのに対し、現在のLLMはPre-Layer Normalization (Pre-LN) を採用しています。Post-LNでは層数が増えるにつれて勾配消失問題が発生し学習が困難になることが知られていますが、Pre-LNはこの問題を解決し、大規模モデルの安定した学習を可能にしました。

次に、Normalization手法として、Layer Normalizationから、平均の計算を省略することで高速化を実現したRMSNormへの移行が挙げられます。これはLlamaシリーズで採用され、広く普及しました。Feed-Forward Network (FFN)内の活性化関数も、ReLUからGeLU、そして現在主流のSwiGLUへと進化しており、SwiGLUは予測性能の向上に貢献しています。

Self-Attention機構については、系列長の二乗に比例する計算量を削減するため、計算対象を限定する研究が多く行われてきましたが、LLMではGrouped-Query Attentionのような、演算やパラメータを効率化する手法がLlama 2から導入されています。

位置情報についても大きな変化が見られます。オリジナルの絶対位置情報から、現在はSelf-Attention内に組み込まれる相対位置情報を扱うRoPE（Rotary Positional Embedding）が主流です。RoPEは、学習データに少ない長い文書を扱う際の予測性能と頑健性の向上に寄与することが報告され、PaLMやLlamaでの採用を機に普及しました。

著者は、これら様々なモジュールの変更を経て、原型を留めないほどに進化しながらも「Transformer」と呼ばれ続けるモデルの現状について「テセウスのTransformer」と問いかけ、Attention機構がその本質を定義するのではないかという考察を述べています。多くの研究がなされてきたものの、まだ未知の側面が多く、いまだに研究の余地が十分にあると結んでいます。