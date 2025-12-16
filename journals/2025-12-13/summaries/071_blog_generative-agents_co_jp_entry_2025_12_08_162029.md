## 「AIエージェントキャッチアップ #60 - Microsoft Agent Framework」を開催しました

https://blog.generative-agents.co.jp/entry/2025/12/08/162029

Generative Agentsは、Microsoftが公開したAIエージェント構築フレームワーク「Microsoft Agent Framework」の主要機能と開発アプローチを詳解しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[AIエージェント, Microsoft Agent Framework, ワークフロー, Semantic Kernel, AutoGen]]

ジェネラティブエージェンツ社は、勉強会「AIエージェントキャッチアップ #60」にて、Microsoft Agent Frameworkの概要とその実用的な利用法について解説しました。このフレームワークは、AIエージェントの構築、オーケストレーション、デプロイを効率化するために設計されており、既存のSemantic KernelとAutoGenのアイデアを統合・拡張した後継プロジェクトとして、Microsoftからパブリックプレビューで提供されています。

Webアプリケーションエンジニアにとって重要な点は、PythonとC#/.NETの両方をサポートしているため、既存の技術スタックに組み込みやすいことです。記事では、`OpenAIChatClient`を用いたエージェントの基本的な実装方法から、ツールやミドルウェアを設定する応用例が示されました。さらに、`Executor`クラスや`@executor`デコレーターを使用して各ステップを定義し、`WorkflowBuilder`で並列処理や条件分岐を含む複雑なワークフローを構築できる機能も詳解されています。

特に、主要なワークフローフレームワークであるLangGraphとの違いに言及している点は、開発者が適切なツールを選択する上で重要です。LangGraphが共有「ステート」を介して値を渡すのに対し、Microsoft Agent Frameworkは`ctx.send_message`を通じて次のステップへ直接値を渡す設計を採用しており、このアプローチの違いはワークフローの設計思想に影響を与えます。また、`ctx.request_info`を使用したHuman-in-the-Loop機能もサポートされており、人間の介入を必要とするシナリオにも対応可能です。

このフレームワークは、AIエージェント開発の複雑さを軽減し、より堅牢で実用的なシステムの迅速な開発を可能にする強力な選択肢として、今後のAI駆動型開発において注目すべきツールです。