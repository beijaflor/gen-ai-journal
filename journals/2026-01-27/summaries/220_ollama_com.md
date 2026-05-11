## Ollamaが画像生成を試験的にサポート：CLIから直接画像生成とプレビューが可能に

https://ollama.com/blog/image-generation

**Original Title**: Image generation (experimental)

ローカルLLM実行環境を提供する**Ollama**が、画像生成モデルを試験的にサポートし、ターミナル内でのプレビューを可能にした。

**Content Type**: News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | Annex Potential: 82/100 | Overall: 80/100

**Topics**: [[Ollama, 画像生成, Z-Image Turbo, FLUX.2 Klein, CLI]]

ローカルLLM実行環境のデファクトとなりつつある**Ollama**が、画像生成モデルの試験的サポートを開始しました。現時点ではmacOS版のみの対応ですが、WindowsとLinuxも近日公開予定です。主なサポートモデルは、写実的な表現と中英バイリンガル描画に強い**Z-Image Turbo**（Apache 2.0）と、画像内のテキスト生成精度が高い**FLUX.2 Klein**の2種類です。

特筆すべきは開発体験の向上で、**iTerm2**や**Ghostty**などの画像レンダリング対応ターミナルを使用すれば、CLI上で生成結果を即座にインライン表示できます。サイズ変更（`/set width`）、ステップ数、シード値、ネガティブプロンプトの設定も可能です。既存のLLM同様、コマンド一つで環境構築が完了し、ライセンスのクリーンなモデルをすぐに試用できる点が強みです。

ローカル環境でのAI活用をCLIで完結させたいエンジニアや、プロダクトに組み込む画像生成モデルを選定中の開発者に最適です。