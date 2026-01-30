## クロード憲法：Claudeのキャラクターと価値観に関するビジョン

https://www.anthropic.com/constitution

**Original Title**: Claude’s Constitution: Our vision for Claude’s character

AIモデルClaudeが意思決定を行う際の根本的な指針となる「憲法」の全文を公開し、その倫理観と行動原理を定義する。

**Content Type**: Technical Reference（技術リファレンス）
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 95/100 | **Annex Potential**: 96/100 | **Overall**: 96/100

**Topics**: [[Anthropic, Claude, AI安全性, モデルアライメント, 自律型エージェント]]

Anthropicが、Claudeのトレーニングと行動の最終的な権威となる「憲法」を全文公開しました。本資料は、モデルが複雑な指示や倫理的ジレンマに直面した際の判断基準を体系化したもので、**憲法（Constitution）**、**プリンシパル・階層（Principal Hierarchy）**、**ハード・コンストレイント（Hard Constraints）**などの概念を通じて、Claudeのキャラクターの核心を定義しています。

Webアプリケーション開発者にとって特に重要なのは、**オペレーター（開発者）**、**ユーザー**、**Anthropic**という3種類の主要なステークホルダー間の優先順位が明文化された点です。APIを通じてClaudeを組み込む際、システムプロンプト（オペレーター指示）がユーザーの要求に対してどのように優先されるか、またその指示がモデルの根本的な安全規則（**Broad Safety**）と衝突した場合にどのような挙動を示すかのロジックが詳述されています。

さらに、**Claude Code**のような自律型エージェント環境における行動指針も含まれており、リソースの過剰取得の回避や、人間による監視・制御の維持（**Corrigibility**）に対するモデルの姿勢が明らかにされています。APIを利用した高度なエージェント機能やRAGシステムを構築する際、モデルの拒絶反応や推論の背景を理解するための決定的なリファレンスとなります。

**Claude API**を活用した独自アプリケーションやエージェントを設計し、モデルの挙動を深く制御・予測したい開発者に必読の内容です。