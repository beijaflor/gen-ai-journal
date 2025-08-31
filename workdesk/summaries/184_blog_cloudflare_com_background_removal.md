## Evaluating image segmentation models for background removal for Images

https://blog.cloudflare.com/background-removal/

Cloudflareは、Images APIの背景除去機能を実現するため、複数の画像セグメンテーションモデルを詳細に評価し、BiRefNetを最適な選択肢として採用した。

**Content Type**: Research & Analysis

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[画像セグメンテーション, Workers AI, モデル評価, 背景除去, コンピュータビジョン]]

Cloudflareは、開発者がAI機能を容易に導入できるようWorkers AI上にImages API向け背景除去機能をリリースしました。この機能は、画像内の被写体と背景を分離する二値画像セグメンテーションモデルを利用しており、その開発にあたり、CloudflareはU2-Net、IS-Net、BiRefNet、SAMの4つの主要モデルについて、効率性（推論時間）と精度（IoU、Dice係数、ピクセル精度）を厳密に評価しました。

評価の結果、BiRefNetが複雑な画像や高解像度画像において、高い精度と実用的な推論時間を両立することが判明しました。特に、BiRefNetの双方向の情報伝達アーキテクチャは、きめ細かなエッジの識別と画像全体の構造認識を両立させ、背景が複雑な場合や被写体が細部を持つ場合でも優れた性能を発揮しました。一般的なユースケースにおいて、事前の分類なしに高い精度を提供する汎用モデルが求められたため、BiRefNetが採用されました。

本記事は、単なる機能発表に留まらず、AIモデルの選定プロセスにおける技術的トレードオフ、モデルアーキテクチャ（多尺度アプローチ、中間監視、双方向参照）の違いが性能にどう影響するか、そしてWorkers AIのようなプラットフォームがどのようにAIワークロードの展開を簡素化するかを示しています。Webアプリケーションエンジニアにとって、これはAIを活用した画像処理機能を自社プロダクトに統合する際のモデル選定のヒントとなり、またCloudflare Images APIを利用することで、eコマースの製品画像処理やクリエイティブな画像編集アプリケーションなど、多様なユースケースで高品質な背景除去を簡単に実現できることを意味します。提供されたAPIの利用例やWorkerでの連携コードスニペットは、具体的な実装イメージを提供し、開発体験の向上に貢献します。