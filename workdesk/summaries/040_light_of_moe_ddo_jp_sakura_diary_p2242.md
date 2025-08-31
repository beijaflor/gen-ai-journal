## ローカルLLMをEVO X2でホストする方法まとめ

https://light-of-moe.ddo.jp/~sakura/diary/?p=2242

AMD Ryzen AI Max+ 395を搭載したEVO X2上でローカルLLMを安定稼働させるには、`llama.cpp`をVulkan対応でビルドし、`llama-server`として活用するのが最も効果的であることを示す。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 89/100 | **Annex Potential**: 88/100 | **Overall**: 88/100

**Topics**: [[Local LLM Hosting, AMD GPU, Vulkan API, llama.cpp, systemd]]

この記事は、AMD製GPUであるRyzen AI Max+ 395を搭載したEVO X2環境でローカルLLMを安定して動作させるための具体的な手法を詳細に解説しています。現状、Ryzen AI Max+ 395はAMD独自のGPGPUライブラリであるrocmに完全には対応しておらず、ollamaなどの一般的なツールをrocm経由で利用すると、システムの不安定化やVRAM認識の不具合が発生する課題を指摘しています。

著者は、ollama (rocm版) では安定性に難があり、LM StudioはVulkan互換で安定動作するものの、GUIが必須のためヘッドレスなサーバー用途には不便であると評価。最終的に、`llama.cpp`をVulkan APIサポートを有効にしてビルドし、その`llama-server`機能を利用することが最も安定し、外部からのアクセスにも適していると結論付けています。

webアプリケーションエンジニアにとって重要なのは、この手順がAMD環境におけるローカルLLM運用の具体的なボトルネックを解消する、実践的な解決策を提示している点です。詳細なビルド手順、`cmake`オプション (`-DGGML_VULKAN=ON`)、`llama-server`の実行オプション (`--ctx-size`, `--n-gpu-layers 999`など)、そして`systemd`を用いた常時起動設定までが具体的に示されており、すぐにでも自社環境や開発ワークフローにプライベートなLLM推論環境を組み込みたい場合に極めて有用です。これにより、NVIDIA製GPUが主流のLLM環境において、特定のAMDハードウェアで直面する非互換性や不安定性の問題を克服し、オープンソースLLMの可能性を最大限に引き出す道筋が示されます。rocmの将来的な改善を待ちつつも、現行環境で安定したローカルLLMサーバーを構築する上で、この情報は不可欠な知見となります。