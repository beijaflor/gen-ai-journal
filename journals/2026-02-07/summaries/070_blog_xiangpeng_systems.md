## 「エージェントのためのシステム」開発を止め、人間が責任を持てる「エージェント・ネイティブ」な基盤を築け

https://blog.xiangpeng.systems/posts/stop-building-agent-systems/

**Original Title**: Stop building systems for agents

提唱する：AIエージェントの普及を阻む真の壁は「人間の責任（アカウンタビリティ）」にあり、徹底的な観測可能性と決定論を備えたシステムこそが「エージェント・ネイティブ」の正体である。

**Content Type**: 💭 Opinion & Commentary
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[AI Agents, Observability, Determinism, Software Architecture, Accountability]]

LLMがコード生成を1000倍に加速させる一方、人間がその動作に責任（アカウンタビリティ）を持つ速度はほとんど変わっていない。著者は、現在のAI開発が「LLMにとって使いやすいインターフェース」の構築に終始していることを「誤った方向」だと批判する。真のボトルネックは、人間がAIの振る舞いを理解・診断・所有できるまでの時間（**Time to Accountability**）にあり、これを短縮しない限り、AIシステムは社会にとって負債になると警告している。

この課題に対し、著者は「人間中心」の**エージェント・ネイティブ・システム**の構築を提唱する。その要諦は、関数の呼び出しからメモリ書き込みまでをガラス張りにする「**徹底的な観測可能性（Radical Observability）**」と、マルチスレッドや分散環境下でも同一入出力と実行順序を保証する「**徹底的な決定論（Radical Determinism）**」の2点だ。現在の「たまたま動いている（happen-to-work）」脆弱な基盤を脱却し、エンジニアが完全に制御・再現可能なシステムを構築することこそが、エージェント時代の真のインフラであると論じている。

AIエージェントのワークフローや基盤インフラを設計しており、AI生成物の信頼性やデバッグの困難さに直面しているエンジニアにとって、設計思想を再考させる必読の提言だ。