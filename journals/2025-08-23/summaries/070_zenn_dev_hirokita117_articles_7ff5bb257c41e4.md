## Second Me をローカル LLM で動かすーmacOS で Docker は使わない方法

https://zenn.dev/hirokita117/articles/7ff5bb257c41e4

macOS上でDockerを使わず、ローカルLLMで動作する個人AI「Second Me」の構築手順と、トレーニング時の具体的なエラー解決策を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Local LLM, Personal AI, macOS Development, Ollama, Troubleshooting]]

この記事は、macOS上でDockerを使用せずにオープンソースの個人AI「Second Me」をローカルLLM（Ollama）で動作させるための具体的な手順と、その過程で著者が直面した技術的な問題の解決策を詳細に解説しています。Webアプリケーションエンジニアにとって重要な点は、まずDockerを介さずに`Node.js`、`Python`、`Homebrew`経由での`cmake`や`poetry`、`uv`といった依存関係をインストールし、プロジェクトをセットアップする実用的な環境構築手法が示されていることです。

さらに、記事の核心的な価値は、ローカルLLMとしてOllamaを利用する際の設定、特に日本語性能に優れた`Llama-3.1-Swallow-8B-Instruct-v0.5`モデルの導入方法と、そのモデルのコンテキスト長を正確に設定する重要性にあります。トレーニングプロセス中に頻発する「トレーニングデータのサイズが大きすぎる（推奨100KB）」、「Augment Content Retentionでの処理停止に対するConcurrency Threadsの調整」、そして最も実践的な「Ollamaの500エラー」に対する具体的なデバッグ方法が詳細に解説されています。特に、Ollamaの`embedding length`と`context length`の値を混同し、`.env`ファイルの`EMBEDDING_MAX_TEXT_LENGTH`設定を誤った場合の対処法は、同様の問題に直面する開発者にとって時間と労力を節約する極めて実践的な知見です。

最終的に著者は、トレーニング完了後も「通常のローカルLLMとの大きな違いを感じられなかった」という率直な感想を述べており、これはAIツールの実用性と期待値のギャップについて現実的な視点を提供します。AIを活用した個人開発や社内ツール構築を検討するエンジニアにとって、本記事は実装の具体的な障壁だけでなく、データ品質やモデル選定が実際の性能に与える影響を再認識させる示唆に富む内容と言えるでしょう。