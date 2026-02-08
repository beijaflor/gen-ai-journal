## 自己改善型コーディング・エージェント：眠っている間に開発を進めるループの構築

https://addyosmani.com/blog/self-improving-agents/

**Original Title**: Self-Improving Coding Agents

自律的なAIエージェントをループ実行し、コードの改善、テスト、コミットを全自動で完結させる具体的な構築フレームワークを提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Agents, LLM Orchestration, Autonomous Coding, Ralph Wiggum Technique, Developer Productivity]]

Google のエンジニア Addy Osmani 氏が、**Claude Code** や **Amp** などの AI エージェントを連続ループで実行し、自律的に開発を加速させる実用的なフレームワークを公開した。中心となるのは「Ralph Wiggum」と呼ばれる手法で、開発をアトミックなタスクに分解し、1回ごとに実行コンテキストをリセットすることで、長大なプロンプトに伴うハルシネーションや文脈の忘却を回避する。

技術的な核心は、エージェントが発見した知見を **AGENTS.md**（または **MEMORY.md**）というファイルに永続化する「自己改善」の仕組みだ。これにより、反復を重ねるごとにプロジェクト固有の規約やバグの修正パターンが蓄積され、後続のエージェントがより賢く振る舞えるようになる。また、**Unit Test** や **Type Check**、**Lint** を検証ゲートとしてループ内に組み込み、テストに合格したコードのみを **Git Commit** するフローを構築することで、品質の自動担保を実現している。

さらに記事では、プランナーとワーカーを分離した階層型オーケストレーションによるスケーリングや、サンドボックス環境での実行、**Feature Branch** の活用によるリスク管理、トークンコストの最適化など、実戦投入に不可欠な知見を網羅している。AI エージェントを単なる補助ツールから、信頼できる「自律的なチームメンバー」へと進化させ、開発効率を劇的に高めたいエンジニアにとって必読のガイドである。