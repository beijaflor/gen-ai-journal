## OllamaがOCR対応。v0.15.5で手書き認識やコーディング特化モデル追加

https://pc.watch.impress.co.jp/docs/news/2083704.html

追加した、ローカルLLM実行環境のOllamaが最新のプレリリースにおいて、手書き文字対応のOCRモデルとMoEアーキテクチャ採用のコーディング特化モデルのサポートを。

**Content Type**: 📰 News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[Ollama, OCR, Qwen3-Coder-Next, GLM-OCR, ローカルLLM]]

ローカルLLM実行環境 **Ollama** のプレリリース版 **v0.15.5** が公開され、新たに2つの強力なAIモデルが統合された。注目は、0.9Bという軽量さながら手書き文字や数式、複雑な表、公印までも高精度に認識する画像認識モデル **GLM-OCR** のサポートだ。これにより、プライバシーを確保した状態での高度なドキュメント解析がローカル環境で容易になる。

加えて、AlibabaのQwenチームが開発した **Qwen3-Coder-Next** も追加された。これは80Bのパラメータを持ちつつ、推論時には **Sparse Mixture of Experts (SMoE)** 技術によって3Bのみをアクティブにするため、VRAM負荷を抑えた高速なコーディング支援が可能。その他、VRAM量に応じたコンテキスト長の自動最適化や、サブエージェントを起動する **ollama launch** コマンドの強化、ブラウザ経由の **ollama signin** など、開発ワークフローを効率化する実用的なアップデートが含まれている。

ローカルでのコーディングエージェント構築や、機密性の高い手書き文書のデータ化を自動化したいエンジニアにとって、即戦力となるアップデートである。