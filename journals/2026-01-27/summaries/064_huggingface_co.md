## 30Bクラス最強のMoEモデル「GLM-4.7-Flash」

https://huggingface.co/zai-org/GLM-4.7-Flash

**Original Title**: zai-org/GLM-4.7-Flash

軽量ながら30Bクラス最高峰の性能を誇るMoEモデル「GLM-4.7-Flash」が、高いコーディング・エージェント能力を武器にリリースされた。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GLM-4.7-Flash, MoE, SWE-bench, vLLM, コーディングエージェント]]

Z.ai (Zhipu AI) が公開した最新の軽量LLM **GLM-4.7-Flash** の概要と実装プラクティスが公開されました。本モデルは30Bクラスの **MoE (Mixture of Experts)** アーキテクチャを採用しており、計算リソースを抑えつつ、大規模モデルに匹敵する高度な推論能力を提供します。

特筆すべきは、ソフトウェアエンジニアリングの実務能力を測定する **SWE-bench Verified** において 59.2 という極めて高いスコアを記録している点です。これは競合する同クラスのモデルを大きく上回る数値であり、実際の開発ワークフローにおける自律的なバグ修正やコード生成に高い適性を示しています。また、数学（**AIME**）や科学的推論（**GPQA**）のベンチマークでも非常に優れた成績を収めています。

運用面では、 **vLLM** や **SGLang** 、 **Transformers** といった主要な推論フレームワークをサポートしており、ローカル環境や独自の推論サーバーへのデプロイが容易です。さらに、マルチターンな推論タスクにおいて一貫性を維持するための **Preserved Thinking** モードも搭載されています。

低コストかつ高レスポンスな独自のコーディングエージェントを構築したい開発者や、高精度なAIツールをセルフホストしたいエンジニアにとって、現在最も有力な選択肢の一つと言えるでしょう。