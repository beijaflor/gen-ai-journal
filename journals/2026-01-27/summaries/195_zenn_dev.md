## Spec-Driven Development (仕様駆動開発) をきっかけに、仕様と設計を整理する

https://zenn.dev/optimisuke/articles/090949f0487326

ISO規格に基づき「仕様」と「設計」を厳密に定義し直すことで、AIエージェントとの円滑な協調開発を可能にする思考法を提示する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Spec-Driven Development (SDD), AI Coding Agents, EARS, ISO/IEC/IEEE 29148, Requirements Engineering]]

本記事は、**AWS Kiro**などのAIコーディングエージェントの活用において重要視される「仕様駆動開発（**Spec-Driven Development**）」の本質を、国際規格である**ISO/IEC/IEEE 29148 (JIS X 0166)**の定義に立ち返って整理した解説記事です。アジャイル開発での「察する」コミュニケーションが通用しないAI相手には、満たすべき条件を体系化した成果物である**Specification（仕様）**と、それをどう実現するかという**Design（設計）**を厳密に分離し、明文化する必要があることを指摘しています。

具体的な手法として、**EARS (Easy Approach to Requirements Syntax)**を用いた要求事項の記述方法や、仕様を「守るべき前提」として固定することでAIによる設計・実装の自動探索を可能にするワークフローを紹介しています。単なるツールの紹介に留まらず、従来の要求工学の知見をAI時代の開発プロセスに再適用する視点を提供している点が特徴です。AIエージェントへの指示が曖昧になりがちな開発者や、エージェントとの協調精度を高めたいエンジニアにとって、思考を整理するための強力なガイドとなります。