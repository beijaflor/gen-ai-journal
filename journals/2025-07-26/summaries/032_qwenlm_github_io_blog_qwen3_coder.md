## Qwen3-Coder: Agentic Coding in the World

https://qwenlm.github.io/blog/qwen3-coder/

Qwenチームは、大規模コンテキスト長と高度な強化学習を活用し、開発ワークフローにエージェントAI能力をシームレスに統合する強力なコーディングモデル「Qwen3-Coder」を発表しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Agentic Coding, Large Language Models, Reinforcement Learning, Developer Tools, Code Generation]]

Qwenチームは、これまでのモデルで最もエージェント性の高いコードモデル「Qwen3-Coder」を発表しました。特に、480BパラメータのMixture-of-Expertsモデル「Qwen3-Coder-480B-A35B-Instruct」は、ネイティブ256K、外挿1Mトークンのコンテキスト長をサポートし、エージェントコーディングタスクでオープンモデルとして最先端の性能を発揮します。これはWebアプリケーションエンジニアにとって、大規模リポジトリや複雑なPull Requestを扱う際に、モデルがより広範なコードベースを理解し、一貫性のある提案を行う上で極めて重要です。

本モデルは7.5兆トークン（うち70%がコード）で事前学習され、コーディング能力を大幅強化。特筆すべきは、後続学習における「Code RL（実行駆動型強化学習）」と「Long-Horizon RL」への注力です。Code RLでは「解決は難しいが検証は容易」なタスクに焦点を当て、コード実行成功率を飛躍的に向上。Long-Horizon RLでは、SWE-Benchのような実世界タスクに対し、計画、ツール使用、フィードバック、意思決定を伴う複数ターンの対話で解決を促します。20,000もの環境を並行実行可能なスケーラブルなシステム構築は、より自律的なエージェント実現への大きな一歩です。

さらに、Gemini CodeをフォークしたCLIツール「Qwen Code」がオープンソース化され、既存のClaude CodeやCline、OpenAI互換APIを通じてQwen3-Coderを容易に利用可能です。これにより、開発者はエージェントAIをワークフローにシームレスに統合し、コード生成だけでなく、デバッグ、リファクタリング、新機能実装といった複雑なエンジニアリング課題に対し、AIがより実践的に貢献する可能性が広がります。
