## I regret building this $3000 Pi AI cluster

https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster

筆者は、3000ドルを投じて構築したRaspberry Pi Compute Module 5クラスターがAI/HPCワークロードに対して期待外れの性能しか出せず、大半の用途において投資価値がないと結論付けている。

**Content Type**: 🔬 Research & Analysis

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 83/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Raspberry Pi Clusters, LLM推論, 分散コンピューティング, HPCベンチマーク, AIハードウェアの費用対効果]]

この記事は、10台のRaspberry Pi Compute Module 5（CM5）を搭載した総額3000ドルのクラスターが、AIおよびHPC（ハイパフォーマンスコンピューティング）用途において実用的な価値を提供しないという筆者の「後悔」を詳細に検証している。HPCベンチマークでは、シングルCM5の10倍の性能（325 Gflops）を達成したものの、より高価なFramework Desktopクラスターと比較すると4分の1の速度にとどまり、ギガフロップあたりの価格効率でも劣る結果となった。

AI推論のテストでは、より深刻な課題が浮き彫りになった。CM5のiGPUがllama.cppのVulkanをサポートしないためCPUのみの推論となり、小規模モデル（Llama 3.2:3B）でさえ1秒あたり約6トークンと遅い。大規模モデル（Llama 3.3:70B）を複数のPiに分散させた場合、llama.cpp RPCでは1秒あたり0.28トークン、distributed-llamaでも1秒あたり0.85トークンと、Frameworkクラスターに比べて著しく低い性能に終始した。

この結果は、ウェブアプリケーションエンジニアにとって重要な示唆を与える。安価なシングルボードコンピュータを多数集めた分散環境は魅力的だが、AI/MLワークロードに必要な専用のハードウェアアクセラレーション（GPUサポート）や、効率的な分散フレームワークがなければ、期待通りの性能は得られない。AIプロジェクトにおいてコスト効率の良いコンピューティングを求める際には、単にノード数を増やすだけでなく、各ノードの処理能力、特にGPUを活用できるかどうかが決定的に重要となる。本記事は、ほとんどのAI/HPC用途でPiクラスターは非推奨であると断言しており、特定のエッジコンピューティングやCIジョブといったニッチな用途を除いては、投資対効果が低いことを明確に示している。