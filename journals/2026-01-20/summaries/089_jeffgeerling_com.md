## ラズベリーパイ AI HAT+ 2：8GB RAM搭載もLLM実行には疑問が残る性能

https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/

**Original Title**: Raspberry Pi's new AI HAT adds 8GB of RAM for local LLMs

Raspberry PiがHailo 10H搭載の新AI HATを投入したが、実機検証ではPi 5のCPU性能に及ばず、ローカルLLM用途での優位性に乏しいことを明らかにした。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 80/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [Raspberry Pi, Hailo 10H, Edge AI, NPU, LLM Inference]

Raspberry Pi社が新たに発表した130ドルのハードウェア「AI HAT+ 2」について、著名な技術レビュアーであるJeff Geerling氏がその実力と限界を検証している。この製品は、Hailo 10H NPUと専用の8GB LPDDR4X RAMを搭載し、Raspberry Pi本体のCPUやシステムメモリを消費せずにローカルLLM（大規模言語モデル）を実行できるという触れ込みだ。

しかし、著者の厳格なベンチマーク結果によれば、そのパフォーマンスは期待を下回っている。Qwen2.5 Coderなどのモデルを用いた比較において、Pi 5の標準CPUによる推論速度がHailo 10Hを凌駕した。著者はこの原因が「電力制限」にあると指摘している。Pi 5のSoCは最大10Wまで引き出せるのに対し、Hailo 10Hは3Wに制限されているため、スペック上の40 TOPS（INT8）という数値が実推論速度に直結していない。

また、最大の売りである「8GBの追加RAM」についても、著者は懐疑的だ。現行のPi 5には16GBモデルが存在しており、本体メモリを増設する方が汎用性が高く、llama.cppなどの最適化ツールを活用すればPi 5のCPUだけでも30Bクラスの量子化モデルを実用的な精度で動作させることが可能だからだ。

一方で、コンピュータビジョン（画像認識）タスクにおいてはCPUの10倍の速度を発揮するという強みも確認された。しかし著者は、これだけの目的であれば、より安価な既存の「AI Camera（70ドル）」や「AI Kit（70ドル）」で十分であり、あえて130ドルの新製品を選ぶ理由は乏しいと結論づけている。

エンジニアへの示唆として、本製品は現時点では「解決策を探している課題」のような状態にあり、特定の産業用エッジコンピューティング開発（万引き検知などの特定用途）を除けば、一般的な開発者のAIワークフローを劇的に改善するものではない。ローカルLLM実行環境を構築したいのであれば、専用HATに投資するよりも、16GBモデルのRaspberry Pi 5を選択する方が、より多くのモデルを柔軟かつ高速に動かせるというのが著者の主張である。ソフトウェア側のエコシステムも発展途上であり、ビジョンと推論の同時実行（ミックスモード）でクラッシュが発生するなど、実用レベルに達するには時間がかかる見込みだ。