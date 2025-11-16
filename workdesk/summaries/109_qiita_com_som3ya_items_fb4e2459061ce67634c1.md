## RAMEN-SHIO-235B - 事後学習の軌跡 #LLM

https://qiita.com/som3ya/items/fb4e2459061ce67634c1

松尾研LLM開発コンペ2025において、チームRAMENはQwen3-235Bベースの「RAMEN-SHIO-235B」を開発し、SFTからDPOへの戦略転換と詳細なハイパーパラメータ調整を通じてHumanity's Last Examでトップ性能を達成した軌跡を解説する。

**Content Type**: Research & Analysis
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 93/100 | **Annex Potential**: 92/100 | **Overall**: 92/100

**Topics**: [[LLM事後学習, 強化学習 (DPO/GRPO), MoEモデル, 大規模言語モデル (LLM), ハイパーパラメータ調整]]

東京大学松尾・岩澤研究室主催のLLM開発コンペ2025において、チームRAMENはQwen3-235B-A22B-Thinking-2507をベースに「RAMEN-SHIO-235B」を開発し、Humanity's Last Exam (HLE) でオープンソースモデル最高レベルの性能を達成、優勝しました。本記事は、この3週間という限られた期間での事後学習の軌跡を詳細に解説します。

当初、SFT（Supervised Fine-Tuning）とGRPO（Group Relative Policy Optimization）の二軸で学習戦略を検討しましたが、強力なベースモデルが追加学習で性能劣化する課題や、マルチノードGRPO実装の困難さ、そして実験に要する時間の長さがボトルネックとなりました。SFTは`ms-swift (Megatron)`への移行で高速化できたものの、HLEスコアがベースモデルを下回る傾向に。GRPOもメモリ不足や環境構築の複雑さ、実行時間の問題から断念せざるを得ませんでした。

プロジェクト中盤で、チームは実装がシンプルで高速なオフライン強化学習であるDPO（Direct Preference Optimization）へと戦略を転換。DPOでは、モデル自身に問題を解かせ、正解を出力（chosen）し不正解を出力（rejected）としてペアを作成した学習データを活用。これにより、ベースモデルの出力分布と乖離しすぎず、望ましい振る舞いを強化することを目指しました。

まず30BモデルでSFT、DFT、DPOを比較検証した結果、SFTやDFTが性能を低下させる傾向にある中、DPOはベースモデルと同程度の性能を維持し、改善余地があることを確認。この知見に基づき、235BモデルでのDPOに集中することになりました。

235BモデルでのDPOでは、LoRAの設定、学習率、$\beta$、学習対象層、データ構成といったハイパーパラメータの綿密な探索を実施。MoEルーターの学習を含めるとHLEスコアが低下すること、高すぎるLoRA rank/alphaは学習を不安定にすること、そして特定の学習率（2e-5）と$\beta$（0.075）の組み合わせが安定した性能向上（HLEスコア17.77から19.12へ）をもたらすことを突き止めました。

本記事は、大規模LLMを競争環境下で最適化する際の現実的な課題と、SFTの限界、DPOの有効性、そしてハイパーパラメータチューニングの重要性を浮き彫りにします。ウェブアプリケーションエンジニアにとって、高性能LLMを特定の目的に合わせて微調整する際の戦略立案、技術選定、およびMoEモデル特有の考慮事項に関する実践的な示唆に富んでいます。