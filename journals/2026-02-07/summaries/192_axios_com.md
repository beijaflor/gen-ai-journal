## AnthropicのClaude Opus 4.6がOSSの未知の脆弱性500件を発見

https://www.axios.com/2026/02/05/anthropic-claude-opus-46-software-hunting

**Original Title**: Anthropic's Claude Opus 4.6 uncovers 500 zero-day flaws in open-source code

Anthropicの最新モデル**Claude Opus 4.6**が、500件以上の未知の脆弱性を自律的に特定し、セキュリティ対策におけるAIの実用性を証明した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:3/5
**Main Journal**: 81/100 | **Annex Potential**: 78/100 | **Overall**: 80/100

**Topics**: [[Claude Opus 4.6, 脆弱性診断, ゼロデイ攻撃, オープンソースセキュリティ, 自律型エージェント]]

Anthropicは、最新のフラッグシップモデル「**Claude Opus 4.6**」が、オープンソースライブラリから500件を超える未発見の重大なセキュリティ脆弱性（ゼロデイ）を特定したと発表しました。この検証はサンドボックス環境で行われ、モデルには**Python**や**デバッガー**、**ファジングツール**へのアクセス権のみが与えられました。特筆すべきは、モデルが特別な指示なしに自律的に探索を行い、外部の研究者によって全ての脆弱性が有効であると確認された点です。

従来のツールでは検出困難だった**GhostScript**や**OpenSC**のバグに対し、Gitのコミット履歴を分析したり、独自の**Proof-of-Concept (PoC)**を記述して脆弱性を実証したりといった高度な推論能力を発揮しています。Anthropicは、この能力がOSSの安全性向上に寄与すると確信しており、防御側へのツール提供を優先する方針です。同時に、悪用を防ぐためのリアルタイム検出機能などの安全策も導入されています。

自社製品のセキュリティレビューやOSSの依存関係管理に携わるエンジニアにとって、LLMが「人間の補助」を超えて「自律的な診断者」として機能し始めたことを示す重要なニュースです。