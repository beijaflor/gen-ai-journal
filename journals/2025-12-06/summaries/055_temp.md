## FLUX 2.0を32GBユニファイドメモリMacBookで使ってみた

https://techblog.raksul.com/entry/2025/12/01/113455

次世代画像生成モデルFLUX 2.0は、その先進的なアーキテクチャと高い表現力で注目の画像生成モデルであり、32GBユニファイドメモリMacBookでのローカル実行は困難と判明したが、公式APIノードやCloud GPU、今後のモデル進化による代替手段が示された。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[画像生成AI, FLUX 2.0, ComfyUI, ローカル環境, 量子化]]

次世代画像生成モデルFLUX 2.0が注目を集めています。従来のStable Diffusionが採用していたLDM（Latent Diffusion Model）とU-Net構造に対し、FLUX 2.0はStable Diffusion 3.0でも導入されているLatent Flow MatchingとLLMで広く使われるTransformer（Rectified Flow Transformer）という新しいアーキテクチャを採用しています。これにより、より効率的で整合性の高い画像生成を実現し、Mistralベースの強力なVLM（視覚言語モデル）をText Encoderとして搭載することで、複雑なプロンプト理解と高い表現力を持ちます。特に、Stable Diffusionが苦手としていたテキストレンダリング能力の向上や、最大10枚の参照画像から一貫したスタイルで画像を生成できるマルチリファレンス生成が特徴です。

しかし、この強力なモデルには注意すべき点があります。FLUX 2.0 [dev]はOpen Weightモデルとして公開されているものの、「Non-Commercial License」に基づきます。これは、モデル自体の「非商用目的」以外での利用を制限しており、企業が業務の一環としてモデルを利用する場合には商用ライセンス（月額$1999〜）の取得が必要となるため、技術検証の際には特に留意が必要です。

本記事では、320億パラメータを持つ巨大なFLUX 2.0 [dev]を、Apple M4チップ搭載の32GBユニファイドメモリMacBook AirでComfyUIを使ってローカル実行できるか検証しました。FP8量子化やComfyUIのWeight Streaming/Offloadingといった省メモリ技術が適用されているものの、筆者の試みではデフォルト設定（ステップ数20）で約66GBものメモリが必要となり、PCがシャットダウンするという結果に終わりました。開発元やNVIDIAの公式情報ではFP8量子化後のVRAM要件は約38.4GBとされており、ComfyUIが巨大モデルファイルをロードする際に一時的に約2倍のメモリ領域を必要とする挙動が、この失敗の主因と分析されています。

ローカル環境での直接実行が困難であったため、記事では代替策としてBlack Forest Labsが提供するFLUX 2.0 [pro]の公式APIノードをComfyUI上で利用する方法を紹介しています。これは手軽である一方で、LoRAやControlNetといったComfyUIの強みである高度なカスタマイズ性が失われるデメリットも指摘されました。

今後の展望としては、よりメモリ効率の良いFP4量子化モデルの登場を待つか、RunPodのようなCloud GPUサービスを利用して高性能GPU上でComfyUI環境を構築することが現実的な選択肢として挙げられています。これにより、カスタマイズ性を保ちつつFLUX 2.0の真価を引き出すことが可能となります。本記事は、次世代画像生成モデルの強力な可能性を示しつつも、その大規模さゆえのローカル環境での障壁と、それを乗り越えるための具体的なアプローチを提示しています。