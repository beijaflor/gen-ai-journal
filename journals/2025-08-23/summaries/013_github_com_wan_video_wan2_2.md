## Wan: Open and Advanced Large-Scale Video Generative Models

https://github.com/Wan-Video/Wan2.2

Wan2.2は、MoEアーキテクチャと効率的な高圧縮VAEを統合し、消費者向けGPUで高解像度動画生成を可能にするオープンソースの基盤動画生成モデルをリリースしました。

**Content Type**: Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 83/100 | **Overall**: 88/100

**Topics**: [[Video Generation, Diffusion Models, Mixture-of-Experts, High-Definition AI, Consumer GPU Inference]]

Wan2.2は、オープンソースの大規模動画生成モデルの主要アップグレード版であり、その技術的革新と実用性が注目されます。特に、動画拡散モデルにMixture-of-Experts（MoE）アーキテクチャを導入し、ノイズ除去プロセスを「高ノイズエキスパート」と「低ノイズエキスパート」に分離することで、計算コストを維持しつつモデル容量を大幅に拡大しました。これにより、複雑な動きやシネマティックな美学を持つ動画を高精度で生成できます。

また、Wan2.2-VAEによる高圧縮設計を採用したTI2V-5Bモデルは、高い圧縮率（4x16x16）で720P@24fpsの動画生成を可能にし、NVIDIA RTX 4090のような消費者向けGPUでも動作します。これは、現行最速クラスの720P@24fpsモデルの一つであり、産業用途と研究の両方でその効率性が際立っています。Text-to-Video、Image-to-Video、Text-Image-to-Videoといった多様な生成タスクに対応し、ComfyUIやDiffusersといった主要なフレームワークへの統合も進んでおり、開発者にとって非常に扱いやすいツールとなっています。

Webアプリケーションエンジニアの視点から見ると、このモデルは高品質な動画生成機能を比較的低いハードルでアプリケーションに組み込む可能性を広げます。特に、MoEによる効率的なスケーラビリティと、消費者向けGPUでの高解像度動画生成能力は、リソースが限られた環境での開発やプロトタイプ作成において大きなメリットとなります。オープンソースであるため、カスタマイズやコミュニティによる機能拡張も期待でき、動画生成AIの活用領域を大きく広げる重要な一歩と言えるでしょう。