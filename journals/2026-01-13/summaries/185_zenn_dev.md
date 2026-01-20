## Attention再入門 is all you need

https://zenn.dev/mkj/articles/re-entry-attention_20251209

Attention機構が「Attention is all you need」から現在に至るまで、どのような技術的課題を乗り越え、いかに進化したかを3つの技術的側面から体系的に解説する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 80/100 | **Overall**: 88/100

**Topics**: [[Attention, Transformer, LLM, FlashAttention, KVキャッシュ]]

Transformerの根幹であるAttention機構は、その登場以来、計算量とメモリ消費という「功罪」と戦い続けてきた。著者は、現在のLLMの進化を「計算量の削減」「KVキャッシュの処理」「長文脈（Long Context）対応」という3つの対象と、構造的・実装的アプローチの掛け合わせで整理できると主張している。

第一の柱である計算量の削減では、単純な演算回数だけでなく、GPUメモリのI/Oボトルネックが焦点となる。FlashAttentionはSRAMを活用したタイリング技術でI/Oを最適化し、精度の劣化なく高速化を実現した。一方で、Sparse AttentionやLinear Attentionは、数学的な工夫によって$O(n^2)$の計算オーダーそのものを線形（$O(n)$）に近づける試みとして紹介されている。

第二の柱は、推論時の最大の壁であるKVキャッシュの最適化だ。70Bクラスのモデルではキャッシュだけで数十GBのメモリを占有するため、データ量削減とメモリ管理が不可欠となる。具体的には、複数のQueryでKey/Valueを共有するGQA（Grouped Query Attention）や、DeepSeekで採用された低ランク圧縮を用いるMLA（Multi-head Latent Attention）が、精度を維持しつつメモリ負荷を劇的に下げる手法として挙げられている。また、OSの仮想メモリから着想を得たPagedAttention（vLLM）による動的メモリ割当が、断片化を防ぎスループットを向上させる鍵となっている。

第三の柱である長文脈対応では、Ring AttentionのようなマルチGPUによる並列計算手法と、学習時を超える長さを扱うための位置埋め込み（RoPE, YaRNなど）の拡張技術が詳説されている。

筆者は、これらの進化を知ることは単なる知識の蓄積にとどまらず、ライブラリのバージョン競合（flash-attn周りのトラブルなど）への対応や、ハードウェア性能を引き出すためのエンジニアリングに直結すると強調する。数理的な美しさと、GPUメモリ階層を意識した「泥臭い」最適化の交差点に、現在のLLM開発の最前線があることを示す一端となっている。