## 生成AI搭載型ペンプロッター「GPenT」：ハードウェアとLLMを融合させた垂直描画システム

https://theodore.net/projects/Polargraph/

**Original Title**: Generative Pen-trained Transformer

壁掛け式の垂直描画マシン「Polargraph」にLLMを統合し、自然言語から物理的なアートを生成するエンドツーエンドのシステムを構築する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[ペンプロッター, Gemini API, G-code, Stable Diffusion, IoT]]

Teddy Warner氏が開発した、壁掛け式の垂直描画マシン「**GPenT**（Generative Pen-trained Transformer）」の構築プロセスを詳述した記事です。ハードウェアは**Arduino Mega**と**RAMPS 1.4**、**NEMA 17**ステッパーモーターを組み合わせた**Polargraph**構成を採用し、制御系は**Raspberry Pi 5**上で動作するFlaskベースのWeb UI「**plotter.local**」で統合されています。

プロジェクトの核心はAIとの融合にあります。**Gemini API**を利用して、ユーザーの抽象的な入力をJSON形式の描画パラメータ（生成器の選択、色、座標変換）へ変換し、物理的なペン操作に落とし込むワークフローを確立しています。また、**Stable Diffusion**の潜在空間から直接**G-code**をデコードしようとする実験的な拡散モデル「**dcode**」についても触れており、VAEがピクセル再構成に最適化されているためにパスプランニングが困難であるといった、技術的な限界と教訓が率直に共有されています。

ハードウェアとLLMを連携させた独自のクリエイティブ・ツールを構築したいエンジニアや、物理デバイスを操作するエージェントの実装に関心がある開発者に最適なリファレンスです。詳細な**BOM**（部品表）や**Marlin**ベースのファームウェア、Web UIのソースコードも公開されており、再現性の高いプロジェクトとなっています。