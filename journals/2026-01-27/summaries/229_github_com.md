## [ChartGPU：WebGPUベースの高パフォーマンスなオープンソース・チャートライブラリ]

https://github.com/ChartGPU/ChartGPU

**Original Title**: ChartGPU: Beautiful, open source, WebGPU-based charting library

WebGPUを駆使して数百万件規模のデータポイントを100 FPS以上で描画し、高度なインタラクションを実現する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[WebGPU, データ視覚化, TypeScript, フロントエンド, オープンソース]]

**ChartGPU**は、次世代のWebグラフィックス規格である**WebGPU**をフル活用し、数百万件のデータポイントを高速に描画するTypeScript製のオープンソースライブラリです。従来のCanvasやSVGベースのライブラリでは描画負荷がボトルネックとなっていた大規模なデータセットに対し、100 FPSを超える滑らかなインタラクションを提供します。**折れ線グラフ**、**棒グラフ**、**キャンドルスティック**、**散布図**といった主要なグラフ形式を幅広くサポートしています。

技術的な特徴として、100万点以上のポイントクラウドの構造を可視化する**Scatter Density（ヒートマップ）モード**や、GPUバッファへの効率的なデータ転送を行うアーキテクチャが挙げられます。**WGSLシェーダー**による高速描画と、注釈（Annotation）などの**DOMオーバーレイ**を組み合わせることで、パフォーマンスと柔軟なUIを両立させています。また、**React bindings (chartgpu-react)** も用意されており、既存のReactプロジェクトへの導入もスムーズです。

金融データのリアルタイム監視や大規模なログ分析など、膨大なデータをWebブラウザ上で快適に可視化したいWebアプリケーションエンジニアに最適なツールです。Chrome 113+やSafari 18+など、WebGPUに対応したモダンブラウザでの利用が前提となります。