## Why Is Japan Still Investing In Custom Floating Point Accelerators?

https://www.nextplatform.com/2025/09/04/why-is-japan-still-investing-in-custom-floating-point-accelerators/

Pezy Computingは、日本の戦略的支援を受け、NVIDIA製GPUの寡占状態に対するヘッジとして、エネルギー効率と特定のHPC/AIワークロードに特化した独自浮動小数点アクセラレータの開発を継続している。

**Content Type**: 🔬 Research & Analysis

**Scores**: Signal:4/5 | Depth:5/5 | Unique:5/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 92/100 | **Overall**: 88/100

**Topics**: [[AI向けカスタムハードウェア, アクセラレータアーキテクチャ, HPCとAIの融合, エネルギー効率の高いコンピューティング, 地政学的リスクと半導体供給]]

現在のAI開発はNVIDIA製GPUに大きく依存していますが、日本が独自に開発を進めるPezy Computingの浮動小数点アクセラレータ「Pezy-SC」シリーズは、そのオルタナティブとして注目に値します。本記事は、このカスタムハードウェアがなぜ日本の戦略的投資を受け、GPUと異なるアプローチでHPCおよびAIワークロードの性能と電力効率を追求しているのかを詳細に分析しています。

Pezy-SCシリーズは、MIMD（多命令多データ）アーキテクチャの一種であるSPMD（単一プログラム多データ）アプローチを採用し、シンプルなPE（プロセッサエレメント）と効率的なキャッシュ階層、多重スレッド処理でレイテンシを隠蔽します。最新の「Pezy-SC4s」はTSMCの5nmプロセスを採用し、2048のPE、96GBのHBM3メモリ、1.5GHzで動作。FP64精度ではNVIDIAのHopper H100 GPUと比較してゲノム解析で2.8倍の性能を発揮する可能性が示唆されており、ワットあたりの性能においてもGPUと互角に渡り合えると評価されています。BF16などAIで重要なデータ型もサポートし、Google Gemma3やMeta Llama3、Stable Diffusion 2といった主要なLLMも既にポーティングされています。

ウェブアプリケーションエンジニアにとって重要なのは、この取り組みが現在のGPU一極集中状態に多様性をもたらす可能性です。AIモデルのトレーニングや推論に使うハードウェアの選択肢が増えれば、コストや電力効率の最適化、特定のワークロード特性に合わせたデプロイが可能になります。また、GPU供給の地政学的リスクが高まる中、自国で高性能計算リソースを開発する日本の戦略は、将来的なAIインフラの安定性確保という観点からも極めて重要です。Pezyのようなカスタムチップの動向を理解することは、AIアプリケーション開発のプラットフォーム選定や、より持続可能なAIシステム設計を考える上で、長期的な視点を提供します。