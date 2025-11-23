## Repeated Samplingを使ったLLM推論時スケーリングで麻雀点数計算問題生成タスクを解くぞ！

https://tech.layerx.co.jp/entry/mahjong-repeated-sampling

LayerXのエンジニアは、LLMの推論時スケーリング手法であるRepeated Samplingを麻雀点数計算問題生成タスクに適用し、高精度な問題生成を実現する手法と実装の要点を解説します。

**Content Type**: Research & Analysis
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 74/100 | **Overall**: 76/100

**Topics**: [[LLM推論最適化, Repeated Sampling, AI Agent, 構造化出力, BAML]]

LayerXのエンジニアは、LLMの推論時スケーリング手法「Repeated Sampling」を麻雀点数計算問題生成タスクに応用した経験を解説しています。Repeated Samplingは、LLMに複数の回答候補を生成させ、Verifierが最適な解を選ぶことでモデル性能を引き出す技術です。その有効性は、正解が含まれる「Coverage」と、正解を識別する「Precision」に依存すると著者は指摘します。

特に、VerifierのPrecisionの高さが重要であり、麻雀問題生成タスクでは、VerifierがLLM出力の自然言語問題文から情報を抽出し、ユーザー指示との適合性を判定します。自然言語の解釈という非決定論的な側面を持つため、高精度なVerifierの実装が鍵となります。記事ではBAMLによる構造化出力を採用。麻雀の複雑なルール制約を型定義で強制し、LLMが生成した問題文から正確なデータを抽出し、LLM-as-a-Judgeとして検証するアーキテクチャを構築しました。

実験では、GPT-5で生成した候補をGPT-4oとBAMLで構成したVerifierで検証。20個の複雑な指示に対しサンプリング数5で実行し、95.0%という高いタスク成功率を達成しました。これはRepeated SamplingなしのGPT-5単体での76.5%から大幅な改善です。しかし、候補生成にGPT-4を使うと成功率は5.0%に急落し、モデル性能とコストのバランスの重要性が示されました。

今後の課題として、成功タスク発見時の推論キャンセルによるコスト削減、AB-MCTSなど高度なスケーリング手法の導入、そしてReward ModelやMajority Voteを用いた複雑な条件（例：「難しい問題」）への対応が挙げられています。著者は、論文で提示される手法も実際のドメイン問題適用には多くの工夫と学びがあることを強調し、その難しさと楽しさを伝えています。