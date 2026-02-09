## Qwen3-Coder-Next：エージェント型コーディングに特化した効率的な大規模言語モデル

https://qwen.ai/blog?id=qwen3-coder-next

**Original Title**: Qwen3-Coder-Next Technical Report

Qwenチームが、コーディングエージェントとローカル開発に特化したオープンウェイトLM「Qwen3-Coder-Next」を発表し、3Bアクティブパラメータで70%超のSWE-Bench Verified精度を達成した。

**Content Type**: Product Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 75/100 | **Overall**: 87/100

**Topics**: [[コーディングエージェント, MoE, 強化学習, SWE-Bench, 推論効率化]]

**Qwen3-Next-80B-A3B-Base**をベースに構築された本モデルは、ハイブリッドアテンションとMoEアーキテクチャを採用し、**大規模な実行可能タスク合成、環境相互作用、強化学習によるエージェント型トレーニング**でスケーリングを実現している。パラメータ数ではなく**エージェント型トレーニングシグナルのスケーリング**に注力し、継続的事前学習、高品質エージェント軌跡による教師あり学習、ドメイン特化エキスパート学習（ソフトウェアエンジニアリング、QA、Web/UX）、エキスパート蒸留を組み合わせた訓練レシピを採用する。

3Bアクティブパラメータながら、**SWE-Bench Verified で70%超、SWE-Bench Pro、TerminalBench 2.0、Aiderで競争力のある性能**を達成し、10～20倍のアクティブパラメータを持つモデルと同等の精度を実現している。長期推論、ツール使用、実行失敗からの回復に重点を置き、マルチターンエージェントタスクにおける長期推論能力を実証している。OpenClaw、Qwen Code、Claude Code、Webデブ、Browser Use、Clineなど複数のダウンストリームアプリケーションへの統合デモも公開されており、**コスト効率の高いエージェント展開**のためのパレートフロンティアを示している。エージェント型コーディングツールの開発者やローカル環境での高効率AI活用を検討する開発者に重要なリファレンス実装となる。
