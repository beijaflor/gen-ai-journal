## そのAIレビュー、レビューしてますか？ / Are you reviewing those AI reviews?

https://speakerdeck.com/rkaga/are-you-reviewing-those-ai-reviews

AIによるコードレビューを単なる自動化プロセスではなく「継続的に育成すべき評価システム」と定義し、LLM as a Judgeの知見を応用した改善手法を提示する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Code Review, LLM as a Judge, CodeRabbit, Prompt Engineering, Evaluation Rubrics]]

著者のr-kagaya氏は、AIによるコードレビューの本質を「人間の代わりにコードを判断させている状態」と定義し、**LLM as a Judge**（AIによるAIの評価）の知見をレビュープロセスの最適化に適用する手法を解説しています。AIレビューを単なる導入で終わらせず、フィードバックを通じて「育成」していくべき対象として捉えているのが特徴です。

技術的な洞察として、LLM特有の**自己バイアス**や**位置バイアス**、**冗長性バイアス**がレビュー品質に与える影響を指摘。これらへの対策として、**生成と評価の分離**（一つのモデルに書かせ、別のモデルに評価させる）や、明確な採点基準である**ルーブリック**の明文化を推奨しています。

具体的な実践例として、**CodeRabbit**の**path_instructions**を用いたディレクトリ単位の基準定義や、人間との対話から知見を蓄積する**Learnings機能**を活用した**ダブルループ学習**のプロセスを紹介。AIの指摘に対して「なぜその判断をしたのか」という理由（説明可能性）を語らせ、人間がそれをメタ評価することで、チーム固有の最適なレビュー基準を構築していく道筋を示しています。

AIレビューの精度向上やノイズ除去に課題を感じているエンジニアや、AIエージェントをワークフローに組み込み、開発プロセスを再構築しようとしているテックリードにとって非常に有益なガイドです。