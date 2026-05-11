## LLMエンジニアのためのワークロード別最適化ガイド：Offline、Online、Semi-onlineの分類と戦略

https://modal.com/llm-almanac/workloads

**Original Title**: LLM Engineer's Almanac - Workloads | Modal Advisor

LLMワークロードを「オフライン」「オンライン」「セミオンライン」の3種に分類し、それぞれの特性に応じた推論エンジン（vLLM/SGLang）やハードウェア最適化手法を詳説する。

**Content Type**: Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 94/100 | **Overall**: 96/100

**Topics**: [[LLM推論, vLLM, SGLang, 投機的デコード, インフラ最適化]]

Proprietary API（OpenAI等）から**DeepSeek**や**Qwen**といったオープンモデルへの移行が進む中、LLMの推論ワークロードを適切に設計するための技術指針を解説している。著者はワークロードを「**Offline**（バッチ）」「**Online**（対話型）」「**Semi-online**（バースト型）」の3つに分類し、それぞれのエンジニアリング上の課題と解決策を提示する。

**Offline**ではスループットが最優先され、**vLLM**による**Chunked Prefill**や非同期RPCの活用を推奨している。低遅延が求められる**Online**では、ホストオーバーヘッドの少ない**SGLang**を基盤に、**EAGLE-3**を用いた**Speculative Decoding（投機的デコード）**や、**FP8**によるメモリ帯域の節約、**Prefix-aware routing**による**KV Cache**の最適化が不可欠となる。また、急激な負荷変動が起こる**Semi-online**においては、**GPU Memory Snapshotting**を用いて**Torch JIT**のコンパイル時間を短縮し、コールドスタートを分単位から秒単位へ改善する手法が有効である。

LLMアプリケーションのコスト効率とパフォーマンスを最大化し、推論スタックの自社運用を検討しているインフラエンジニアやバックエンドエンジニアにとって必読の内容である。