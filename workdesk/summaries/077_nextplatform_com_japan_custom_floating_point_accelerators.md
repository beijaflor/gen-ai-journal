## Why Is Japan Still Investing In Custom Floating Point Accelerators?

https://www.nextplatform.com/2025/09/04/why-is-japan-still-investing-in-custom-floating-point-accelerators/

日本はPezy Computingのカスタム浮動小数点アクセラレータへの投資を継続しており、その技術進化、GPUに対する性能、および国家戦略上の重要性を深く掘り下げて解説する。

**Content Type**: Research & Analysis

**Scores**: Signal:4/5 | Depth:5/5 | Unique:5/5 | Practical:2/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 84/100

**Topics**: [[HPC, カスタムアクセラレータ, AI向けハードウェア, 半導体アーキテクチャ, 技術的自立性]]

本記事は、日本のPezy Computingが開発するカスタム浮動小数点アクセラレータ「SCシリーズ」の進化と、日本がこの技術に投資を続ける戦略的意義を深く掘り下げている。AIサーバーが世界のシステム支出の半分を占める中、NVIDIA GPUが主流である現状に対し、Pezyは異なるアーキテクチャ（SPMD、きめ細かいマルチスレッディング）でエネルギー効率を極限まで高めることを目指している。

Pezy-SCシリーズは、2012年の初代Pezy-1から最新のPezy-SC4s（2025年出荷予定）まで、TSMCの微細化プロセス（40nmから5nmへ）とHBMメモリの採用、プロセッサエレメント（PE）数の増加、キャッシュ階層の最適化を経て性能を向上させてきた。特に、高精度計算（FP64）における「flops per watt」ではNVIDIAのHopper H100/H200 GPUに匹敵し、特定のゲノム解析ワークロード（GATK）ではSC3チップ単体でH100の2.25倍の性能を発揮すると報告されている。SC4sではさらに25%の性能向上が見込まれる。

ウェブアプリケーションエンジニアにとって、この動向は現在のAIインフラのGPU依存からの脱却と、将来的な計算リソースの多様化という点で重要だ。日本政府によるPezyへの投資は、需要過多や輸出規制によるGPU調達リスクへのヘッジとして、国家的な技術的自立性を確保する戦略的意図がある。これは、AIを活用したサービスを構築する際、将来的に多様なハードウェア選択肢が生まれ、コストや可用性に影響を与える可能性を示唆する。また、PezyプラットフォームがPyTorchや主要なLLM（Gemma3, Llama3, Qwen2など）をサポートしていることは、AIモデルのポータビリティと、特定のハードウェアベンダーに縛られないAI開発の方向性を示唆しており、多様なAIサービスをデプロイする上での基盤技術の理解に繋がるだろう。エネルギー効率の向上は、持続可能なAI運用の観点からも注目に値する。