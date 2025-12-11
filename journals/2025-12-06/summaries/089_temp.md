## Qwen3-VL、2時間の動画をスキャンしほぼ全ての詳細を特定可能に

https://the-decoder.com/qwen3-vl-can-scan-two-hour-videos-and-pinpoint-nearly-every-detail/

**Original Title**: Qwen3-VL can scan two-hour videos and pinpoint nearly every detail

AlibabaがオープンマルチモーダルモデルQwen3-VLの詳細な技術レポートを公開し、2時間の動画や数百ページのドキュメントを正確に分析する並外れた能力を実証しました。

**Content Type**: Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[マルチモーダルAI, 動画解析, 大規模言語モデル, オープンソースAI, AIベンチマーク]]

Alibabaは、Qwen3-VLに関する詳細な技術レポートを発表し、このオープンマルチモーダルモデルが2時間にも及ぶ動画をスキャンし、ほぼ全ての詳細を特定できる能力を持つことを明らかにしました。このモデルは、最大256,000トークンのコンテキストウィンドウ内で、2時間の動画または数百ページに及ぶドキュメントを処理できるため、長尺コンテンツの深い理解が求められるWebアプリケーション開発者にとって画期的なツールとなる可能性があります。

特に注目すべきは、Qwen3-VL-235B-A22Bモデルが「needle-in-a-haystack」テストにおいて、30分動画で100%、2時間動画（約100万トークン）で99.5%という驚異的な精度で特定のフレームを検出する能力を示した点です。さらに、画像ベースの数学タスクではGemini 2.5 ProやOpenAI GPT-5を上回り、MathVistaで85.8%、MathVisionで74.6%を記録しました。ドキュメント理解タスクのDocVQAでは96.5%、39言語をサポートするOCRBenchでは875ポイントを獲得しています。GUIエージェントタスクでも高い精度を示しており、ScreenSpot Proで61.8%、AndroidWorldで63.7%の成績を収めました。

これらの高性能を支える主要な技術的進歩には、「interleaved MRoPE」による長尺動画の性能向上、「DeepStack」によるビジョンエンコーダの中間結果へのアクセス、そして複雑なT-RoPEに代わる「テキストベースのタイムスタンプシステム」の導入があります。これらの改善により、モデルは視覚情報と時間情報をより効率的かつ詳細に処理できるようになりました。

最大10,000個のGPUを用いて1兆トークン以上のデータで4段階のトレーニングが実施されたQwen3-VLは、Apache 2.0ライセンスの下でオープンウェイトとしてHugging Faceで利用可能です。これにより、Webアプリケーションエンジニアは、独自のアプリケーションやサービスにこの高度なマルチモーダル能力を組み込み、新たなユーザー体験や自動化ソリューションを開発できる可能性が大きく広がります。GoogleのGemini 1.5 Proが既に長尺動画からのフレーム抽出能力を持つ一方で、Qwen3-VLはオープンなパッケージとして競争力のあるパフォーマンスを提供し、オープンソース開発をさらに加速させることでしょう。