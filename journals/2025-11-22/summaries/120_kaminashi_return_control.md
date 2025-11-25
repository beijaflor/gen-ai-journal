## AIエージェントの制御を柔軟に。Strands Agents と Amazon Bedrock AgentCore で「Return of Control」を実装してみた

https://kaminashi-developer.hatenablog.jp/entry/try-return-of-control

Strands AgentsとAmazon Bedrock AgentCoreを活用し、AIエージェントの柔軟な制御を可能にする「Return of Control」機能の実装方法を詳細に解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 92/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AIエージェント, Amazon Bedrock, Strands Agents, Return of Control, 開発ワークフロー]]

カミナシのエンジニアが、AIエージェントの柔軟な制御を可能にする「Return of Control」（RoC）機能の、Amazon Bedrock Agentsと似た実装をStrands AgentsおよびAmazon Bedrock AgentCoreを用いて実現した過程と学びを共有しています。RoCは、エージェントが特定のアクション（外部API呼び出し、データベースアクセス、人による承認など）の実行をアプリケーション側に委ね、制御を一時的に中断し、結果を受け取って処理を再開する機能です。

著者は、この機能がウェブアプリケーションエンジニアにとって重要である理由として、以下の点を挙げます。第一に、認証情報をエージェント側に持たせることなく、アプリケーション側で一元管理できるため、セキュリティと管理が向上します。例えば、ユーザーごとに異なるAPIキーをセッション情報から取得して利用できます。第二に、既存のバックエンドロジックやデータ取得・加工処理をそのまま活用できるため、開発コストを削減し、効率を高めます。第三に、アプリケーションと同じ環境で実行されるため、デバッグやログ確認が容易になり、開発体験が向上します。

実装にあたっては、当初エージェントの`state`に情報を記録しLLMに中断を「祈る」という方法を試みたものの、確実性に欠けるという課題に直面しました。しかし、Strands Agentsに最近追加された`interrupts`機能（`tool_context.interrupt()`）を活用することで、真の意味でエージェントの実行を中断し、呼び出し元に制御を返すことが可能になりました。会話履歴や状態の維持には、Strands AgentsのSession Management機能とAmazon Bedrock AgentCore Memoryを組み合わせて使用し、`memory.id`と`session_id`を用いてセッションを管理します。中断時には`stop_reason`に`interrupt`が格納され、`interrupt_id`と共にアクション情報をアプリケーションに返却。アプリケーション側でアクションを実行後、`interrupt_results`として結果をエージェントに渡すことで、途中から推論を再開できる詳細な実装方法がコードと共に示されています。

この取り組みは、Strands Agentsが将来的にRoCを公式サポートするロードマップにあることを踏まえつつ、現時点での柔軟なエージェント制御の実装パターンを提供し、AIエージェントを既存システムに組み込む際の具体的な課題解決策を示しています。