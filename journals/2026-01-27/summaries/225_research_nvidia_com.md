## NVIDIA PersonaPlex：任意の役割と声で自然な対話を実現するフルデュプレックスAI

https://research.nvidia.com/labs/adlr/personaplex/

**Original Title**: NVIDIA PersonaPlex: Natural Conversational AI With Any Role and Voice

任意の音声プロンプトとテキストによる役割指定を維持したまま、割り込みや相槌を含む人間のように自然な同時並行対話（フルデュプレックス）を実現する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 54/100 | **Annex Potential**: 54/100 | **Overall**: 80/100

**Topics**: [[PersonaPlex, フルデュプレックスAI, 音声エージェント, NVIDIA, Moshi]]

NVIDIAが、音声による「声」の指定とテキストによる「役割」の指定を両立させたフルデュプレックス対話モデル**PersonaPlex**を発表した。従来の音声AIは、カスタマイズ性は高いが応答が遅く不自然な**ASR→LLM→TTSカスケード型**か、自然な対話は可能だが役割が固定される**フルデュプレックス型**の二択を迫られていたが、本作はそのトレードオフを解消している。技術的には、70億パラメータの**Moshi**アーキテクチャをベースに、**Mimiニューラルオーディオコーデック**を用いた単一モデル構成を採用。Temporal/Depth Transformerにより「聞きながら話す」動作を制御し、低遅延な応答を実現している。

学習プロセスにおいて、実際の会話データ（**Fisher English corpus**）から自然な相槌や割り込みのパターンを、LLM生成の合成データからタスク遂行能力を抽出して統合した点が最大の特徴だ。これにより、銀行の窓口業務から緊急時の宇宙飛行士まで、多様なコンテキストに応じた**バックチャネリング**や感情表現を伴う対話が可能になった。評価指標においても、ターン管理の精度や割り込みへの反応速度で既存の**Gemini Live**等の商用モデルを上回る性能を記録している。

コードとモデルウェイトが公開されており、リアルタイム音声エージェントを自前でホストし、低遅延かつ高度にパーソナライズされたユーザー体験を構築したいエンジニアにとって、極めて強力なリファレンスとなるだろう。既存の音声UIの「機械的な間」に不満を感じているプロダクト開発者は必見の内容だ。