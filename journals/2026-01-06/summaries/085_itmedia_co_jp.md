## NPUだけでOpenAIのLLM「gpt-oss」が動く！　速度や消費電力を計測してみた

https://www.itmedia.co.jp/aiplus/articles/2512/29/news040.html

AMDのNPU「Ryzen AI」と最適化ランタイム「FastFlowLM」を用いて、OpenAIの「gpt-oss 20B」を省電力かつ低発熱でローカル実行した実測結果を報告する。

**Content Type**: 🔬 Research & Analysis
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 78/100 | **Overall**: 76/100

**Topics**: [[Local LLM, NPU, Ryzen AI, gpt-oss, FastFlowLM]]

本記事は、米OpenAIが2025年8月に公開したオープンウェイトモデル「gpt-oss 20B」を、AMDのNPU「Ryzen AI」上で動作させ、その実用性と効率性を詳細に検証したレポートである。これまで「AI PC」に搭載されるNPUは、実用的な規模のLLMをローカルで動かすには力不足と見なされることが多かったが、専用の最適化ランタイム「FastFlowLM」とAMDのデスクトップアプリ「Lemonade」の登場により、NPU単体での実用的な推論が現実味を帯びてきた。

検証には、Ryzen AI 7 PRO 350（50TOPSのNPU性能）を搭載した「ThinkPad T14 Gen 6 AMD」を使用。比較対象として、NPUとGPUのハイブリッド実行、および一般的なローカルLLM実行ツールである「LM Studio」でのパフォーマンスを測定している。筆者が提示したデータによれば、NPU実行の最大の利点は消費電力と熱管理にある。ハイブリッド実行がピーク時に約45Wを消費するのに対し、NPU単体（FastFlowLM利用時）では約16〜24W程度に抑えられており、内部温度もGPU併用時の80℃に対し、70℃程度で安定している。

「gpt-oss 20B」における生成速度については、NPU実行で約11トークン/秒を記録した。これはLM Studioを用いたGPU/CPU実行の約14.5トークン/秒には及ばないものの、ワットパフォーマンス（トークン/秒W）で見ればNPU側が優位（約0.55 vs 0.41）となる。ただし、最初のトークンが出るまでの時間（TTFT）はNPU実行の方が長く、体感的なレスポンスでは従来のGPU環境に軍配が上がる。

筆者は、NPUでのLLM実行が「GPU不要で省電力」という兆しを見せた一方で、依然としてメモリ帯域がボトルネックとなっており、ハードウェアとアルゴリズム双方のさらなる進化が必要であると結論づけている。コーディングエージェントのような高速なフィードバックを必要とする用途では、依然として外部GPUが必須であるものの、エッジ側での常時稼働やバックグラウンド処理においては、NPUによる低消費電力な推論が将来的に重要な役割を果たすことを示唆している。開発者にとっては、ローカルLLMのデプロイ先としてのNPUの成熟度を測る上で、非常に具体的なベンチマークデータとなっている。