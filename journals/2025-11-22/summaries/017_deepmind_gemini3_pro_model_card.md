## Gemini 3 Pro モデルカード: Googleの最先端マルチモーダル推論モデルの技術仕様

https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf

**Original Title**: Gemini 3 Pro Model Card

Google DeepMindがGemini 3 Proの公式モデルカードを公開し、Sparse MoEアーキテクチャ、1Mトークンコンテキスト、64K出力、ベンチマーク結果、安全性評価を詳細に文書化した。

**Content Type**: 📋 Documentation
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 85/100 | **Overall**: 90/100

**Topics**: [[Gemini 3, モデルカード, MoE, マルチモーダル, AI安全性]]

Google DeepMindがGemini 3 Proの公式モデルカードを公開した。Gemini 3 ProはSparse Mixture-of-Experts（MoE）Transformerベースのアーキテクチャを採用し、入力トークンごとにパラメータのサブセットを動的にルーティングすることで、総モデル容量と計算・サービングコストを分離している。テキスト・画像・音声・動画のネイティブマルチモーダル対応で、コンテキストウィンドウ最大1M、出力最大64Kトークンを実現。

訓練データは公開Webドキュメント、テキスト、コード、画像、音声、動画を含み、強化学習による多段階推論・問題解決・定理証明データも活用。AI生成合成データも含まれる。訓練はGoogle TPUとJAX、ML Pathwaysで実施された。

ベンチマーク結果では、Humanity's Last Examで37.5%（Gemini 2.5 Pro: 21.6%、Claude Sonnet 4.5: 13.7%）、ARC-AGI-2で31.1%（Gemini 2.5 Pro: 4.9%）、AIME 2025（コード実行付）で100%を達成。LiveCodeBench Proでは2,439（GPT-5.1: 2,243を上回る）、SWE-Bench Verifiedで76.2%、τ2-bench（エージェント）で85.4%、Vending-Bench 2で$5,478.16（他モデルを大幅に上回る）を記録。MRCR v2（1M pointwise）では26.3%で長コンテキスト性能も示した。

配布チャネルはGemini App、Google Cloud/Vertex AI、Google AI Studio、Gemini API、Google AI Mode、Google Antigravity。安全性評価ではGemini 2.5 Pro比でトーン+7.9%改善、不当な拒否+3.7%改善。Frontier Safety Framework評価ではCBRN、サイバーセキュリティ、有害操作、ML R&D、ミスアライメントすべてでCritical Capability Level未達。既知の制限としてハルシネーション可能性、知識カットオフ2025年1月、ジェイルブレイク脆弱性（改善されたが未解決）がある。
