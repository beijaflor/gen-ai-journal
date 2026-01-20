## IQuest-Coder-V1：ソフトウェア進化を学習する新しいCode LLMの訓練パラダイム

https://github.com/IQuestLab/IQuest-Coder-V1/blob/main/papers/IQuest_Coder_Technical_Report.pdf

IQuest Labが発表した技術レポートは、「LLMはソフトウェアの進化からどう学習すべきか」という根本的な問いに答える、新しい**Code-flow訓練パラダイム**を提示する。従来のCode LLMが静的なコードスナップショットから学習するのに対し、IQuest-Coderは動的なソフトウェア進化プロセスそのものを学習データとして活用する。

**Content Type**: 📊 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 95/100 | **Overall**: 95/100

**Topics**: [[Code LLM, 訓練パラダイム, ソフトウェア進化, ベンチマーク性能, オープンソース, LoopCoder]]

**Code-flow訓練パラダイムの3段階**

IQuest-Coderの訓練パイプラインは、ソフトウェアのライフサイクル全体を反映した3つのステージで構成される。

**Stage 1: Pre-training & Annealing**
基礎的なコーディング能力を獲得する段階。2.1兆トークンのCode-flow Pre-training Corpus（CommitEvol、GitFlow、GitHub Codeなど）で事前学習し、その後700億トークンのAnnealingで高品質データに適応させる。

**Stage 2: Mid-training（32k/128k Context）**
長いコンテキストウィンドウでの複雑な推論能力を強化。32kコンテキストで1500億トークン、その後128kコンテキストで300億トークンの訓練を行う。これにより、リポジトリレベルの理解とマルチファイル推論が可能になる。

**Stage 3: Bifurcated Post-training**
2つの経路に分岐する：
- **Thinking Path（強化学習）**: 完全自動化されたRLワークフローで「考える」能力を獲得。SWE-Benchのような複雑なタスクで強力なパフォーマンスを実現
- **Instruct Path（教師あり）**: 一般的なコーディングタスク用の従来型のインストラクションチューニング

**LoopCoder：再帰的Transformerアーキテクチャ**

40B-LoopモデルはユニークなRecurrent Transformerデザインを採用している。従来のTransformerのように1回だけでなく、複数回（最大5ループ）繰り返し推論を行う。これにより、追加パラメータなしで「反復的思考」能力を獲得し、複雑な問題解決とデバッグで優れた性能を発揮する。

**ベンチマーク性能：SOTA達成**

IQuest-Coderは複数の主要ベンチマークで最先端の結果を達成している：

- **SWE-Bench Verified**: 77.2%（全モデル中1位）
- **BigCodeBench**: 49.9%（コード生成と実行で1位）
- **LiveCodeBench**: 87.0%（リアルタイムコーディング課題）
- **Aider Polyglot**: 85.6%（マルチ言語コード編集）
- **HumanEval**: 96.3%（基礎的コーディング能力）

特にSWE-Benchでの77.2%は、実世界のGitHub issueを解決する能力において画期的な結果だ。これは、Code-flow訓練がソフトウェアの進化パターンを効果的に捉えていることを示している。

**完全なWhite-box Release**

IQuest Labは、すべての訓練チェックポイント、データセット、レシピを公開している。これには：
- 7B、14B、40B、40B-Loopモデルの全バージョン
- 2.1兆トークンのCommitEvolデータセット
- 各訓練ステージの詳細な設定とハイパーパラメータ
- 評価ベンチマークと再現手順

このレベルの透明性は、Code LLM研究コミュニティにとって極めて価値が高い。研究者は訓練プロセスを完全に理解し、再現し、改善できる。

**重要な洞察**

IQuest-Coderが提示する最も重要な洞察は、**ソフトウェア進化のダイナミクスを訓練データとして活用することの重要性**だ。従来のCode LLMは、コードの「現在の状態」から学習する。しかしIQuest-Coderは、コミット履歴、変更パターン、リファクタリング、バグ修正といった「進化のプロセス」そのものから学習する。

これは単なる性能向上ではなく、Code LLMの訓練方法に関するパラダイムシフトだ。ソフトウェア開発は静的なアーティファクトの集合ではなく、継続的に進化するプロセスである。IQuest-Coderは、この動的な性質を訓練プロセスに組み込むことで、実世界のソフトウェア開発により近い能力を獲得している。

Bifurcated Post-trainingも興味深い。思考能力（RL経路）と一般的なインストラクション能力（SFT経路）を分離することで、それぞれの目的に最適化された訓練が可能になる。これは、単一の訓練経路で両方をバランスさせる従来の手法よりも効果的だと示されている。

LoopCoderの再帰的アーキテクチャは、さらなる探求に値する。追加パラメータなしで反復的推論を実現し、複雑なデバッグや問題解決で顕著な改善を示している。これは、今後のCode LLMアーキテクチャ設計の重要な方向性を示唆している。