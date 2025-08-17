## Hacking Diffusion into Qwen3 for the ARC Challenge

https://www.matthewnewton.com/blog/arc-challenge-diffusion

ARCチャレンジにおける生成モデルの性能改善を目指し、自己回帰型LLMを拡散モデルとして再構築する実験的アプローチを検証し、その有望な点と現行の課題を詳細に解説する。

**Content Type**: Research & Analysis

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Generative AI, Large Language Models, Diffusion Models, Abstract Reasoning Challenge, Performance Optimization]]

Abstraction and Reasoning Corpus (ARC)チャレンジにおいて、自己回帰型LLM（例: Qwen3-8B）は、パズルを左上から順に解く「タイプライター型」のアプローチを取るため、簡単な部分と難しい部分に同じ計算リソースを費やし、非効率という課題がありました。

本稿ではこの課題を解決するため、既存の自己回帰型LLMを拡散モデルに変換し、モデルがより確信度の高い（エントロピーの低い）ピクセルから順に埋めていく非逐次的な生成手法を提案・検証しています。これはDiffuGPT/DiffuLLaMAの先行研究に基づいています。

実験の結果、10ステップでの拡散モデルは自己回帰型モデルよりも1.68倍高速で、トークン精度も約3%向上しました。しかし、この精度向上は完全な課題解決には繋がらず、完璧に解けたタスク数はゼロでした（自己回帰型は1件）。さらに、30ステップでは拡散モデルが逆に遅くなることが判明しました。

この性能低下の主な理由は、拡散モデルがKey-Value (KV) キャッシュを利用できないことにあります。ARCチャレンジでは、問題の入力例が非常に長く、モデルが生成ステップごとにその全体を再計算する必要があるため、キャッシュを活用できる自己回帰型モデルの方が効率的になるのです。

本稿は、非逐次的な生成の可能性を示しつつも、LLMを拡散モデルとして応用する際のKVキャッシュのような根本的なアーキテクチャ上の課題が、サンプリング戦略の工夫よりも性能に大きく影響することを明確に示しています。これは、ウェブアプリケーションエンジニアが将来のAIベースのコード生成ツールや開発ワークフローを評価する上で、ツールの基盤となる技術的制約を理解する重要性を浮き彫りにします。