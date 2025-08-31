## Cloudflareが最も効率的なAI推論エンジンを構築した方法

https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/

Cloudflareが、Rust製のLLM推論エンジン「Infire」を開発し、vLLMを上回る効率と低CPU使用率でエッジネットワーク上の分散型AI推論を劇的に高速化しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[LLM Inference Optimization, Distributed AI Edge Computing, Rust Programming for AI, GPU Utilization Techniques, Continuous Batching & Paged KV Cache]]

Cloudflareは、分散型エッジネットワークにおける大規模言語モデル（LLM）推論の非効率性に対処するため、Rust製推論エンジン「Infire」を開発しました。既存のオープンソースソリューションvLLMは、集中型データセンター向けに最適化されており、Cloudflareの広範なエッジネットワークや、特にセキュリティサンドボックス（gvisor）使用時の高いCPUオーバーヘッド、起動時間の問題に適合しませんでした。

Infireは、Rustによる低レベル制御を活用し、GPU、メモリ、ネットワークI/Oの利用率を最大化します。そのアーキテクチャは、OpenAI互換のHTTPサーバー、バッチャー、Infireエンジンで構成され、起動時のモデルウェイトロード（非同期コピーやJITコンパイルの並列化）から最適化されています。特に重要なのは、複数のプロンプトを並列処理し、残りのバッチスロットをプリフィルトークンで埋める「連続バッチ処理とチャンク型プリフィル」です。これにより、行列積演算の効率が劇的に向上し、GPUのTensor Coreを最大限に活用します。また、「ページ型KVキャッシュ」を採用し、KVキャッシュを動的に割り当てることでメモリ効率を高め、並列処理可能なプロンプト数を大幅に増加させます。さらに、Nvidia Hopper GPU向けに特化した低レベルCUDAカーネルの最適化や、CUDAグラフの活用により、カーネル起動コストを削減しています。

この結果、InfireはvLLM 0.10.0と比較して最大7%高速な推論を実現し、特に実際の負荷がかかる環境では顕著な性能向上を示します。最も重要なのは、CPU使用率を大幅に削減し、GPU利用率を80%以上に引き上げた点です。これにより、Cloudflareはより少ないリソースでより多くのリクエストを処理できるようになり、Workers AIを利用する開発者は、高速かつ効率的なAI機能を提供できるようになります。この技術的詳細は、分散AIシステムの性能ボトルネックを理解し、自身のアプリケーションでAI活用を進める上での貴重な指針となるでしょう。