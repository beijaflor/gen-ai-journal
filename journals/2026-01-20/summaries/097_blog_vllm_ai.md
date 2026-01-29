## vLLMの大規模サービング：Wide-EPによるDeepSeekのH200あたり2.2k tok/sの実現

https://blog.vllm.ai/2025/12/17/large-scale-serving.html

**Original Title**: vLLM Large Scale Serving: DeepSeek @ 2.2k tok/s/H200 with Wide-EP

高度な並列化技術とエンジンアーキテクチャの刷新により、DeepSeekモデルの推論スループットを劇的に向上させた。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[vLLM, DeepSeek-R1, 推論の高速化, Mixture of Experts (MoE), 並列計算]]

vLLMチームは、最新のV1エンジンへの完全移行に伴い、DeepSeek-V3/R1といった大規模なMoE（Mixture of Experts）モデルにおいて、H200 GPU1枚あたり秒間2.2kトークンという圧倒的なスループットを実現したことを発表しました。これは、従来の1.5kトークンから大幅な改善であり、実生産環境における推論効率の新たな基準を示すものです。

この飛躍を支える核心的な技術として「Wide-EP（広域エキスパート並列）」が紹介されています。DeepSeek特有のMLA（Multi-head Latent Attention）アーキテクチャでは、従来のテンソル並列（TP）を用いるとメモリ使用に重複が生じ、KVキャッシュの効率が低下します。Wide-EPは、エキスパート並列とデータ並列を組み合わせ、さらにDeepEPカーネルを統合することで、ノード間通信のオーバーヘッドを抑えつつ、利用可能なKVキャッシュとバッチサイズを最大化します。

また、計算と通信を重ね合わせる「Dual-batch Overlap (DBO)」も重要な役割を果たしています。これはDeepSeekのマイクロバッチ戦略を実装したもので、MoEのディスパッチ待ちによるGPUのアイドル時間を削減します。さらに、推論時のトークンルーティングの偏りを動的に修正する「EPLB（Expert Parallel Load Balancing）」により、特定のエキスパートへの負荷集中を防ぎ、システム全体の稼働率を高い水準で維持します。

著者は、これらの最適化の意義について、単なる速度向上にとどまらず「トークンあたりのコスト（Token-per-dollar）を直接的に削減し、目標とするQPSを達成するために必要なGPUリソースを最小化できること」にあると主張しています。また、プリフィルとデコードを物理的に分離する「Disaggregated Serving」との組み合わせが、計算負荷の高いプリフィルリクエストによるシステム全体の遅延を防ぐために不可欠であると述べています。エンジニア向けには、llm-dやRay Serve LLMといった既存のデプロイスタックを通じて、これらの高度な最適化を即座に利用できる環境が整っていることが示されており、大規模LLM運用のコストパフォーマンスを劇的に改善する道筋が提示されています。