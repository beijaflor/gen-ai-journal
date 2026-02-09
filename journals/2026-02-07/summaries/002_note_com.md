## 高機能Local LLM｜GLM-4.7-Flashの特徴とその無検閲・改良版についての話＠TextGeneration WebUI

https://note.com/gentle_murre488/n/n2d04724fac63

ローカルLLM「GLM-4.7-Flash」のアーキテクチャを解剖し、性能を拡張した無検閲・クリエイティブ特化版の技術的特徴と導入手順を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 71/100 | **Overall**: 76/100

**Topics**: [[GLM-4.7-Flash, Local LLM, Mixture-of-Experts, GGUF, TextGeneration WebUI]]

Zhipu AIと清華大学が開発した**GLM-4.5**をベースに、ローカル動作向けに極限まで効率化された**GLM-4.7-Flash**の技術的特徴と、その派生モデルである**Grande-Heretic-UNCENSORED-42B**の実装詳細について解説している。**GLM-4.7-Flash**は、総パラメータ31B（アクティブ3B）という軽量さながら、**Thinking Mode（思考モード）**を継承し、数学ベンチマーク**AIME 25**で91.6%という高い推論性能を示す。本記事が主に紹介する改造版モデルは、**Brainstorm 20x adapter**を用いてレイヤー数を48から67層へと拡張し、表現の自由度を高めるための**Abliterated（検閲除去）**処理が施されているのが特徴だ。技術的な側面では、**GGUF**形式への量子化において**16ビット精度**の出力テンソルを使用し、思考品質の低下を防ぐ工夫がなされている。**TextGeneration WebUI**を用いたローカル環境での動作検証も行われており、VRAM 32GB環境で13万コンテキスト長を実用的な速度で処理可能であることを示している。特定のタスクだけでなく、複数の指示を破綻なくこなすエージェント能力をローカルで求める開発者に適した内容である。高性能なローカル推論環境を自前で構築したいエンジニアや、クリエイティブな文章生成に特化したモデルを探しているユーザーは必読だ。