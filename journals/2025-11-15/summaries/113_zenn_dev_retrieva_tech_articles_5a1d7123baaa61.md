## LangChain DeepAgents × Local LLM で使い放題のAIエージェント開発

https://zenn.dev/retrieva_tech/articles/5a1d7123baaa61

DeepAgentsとローカルLLMを組み合わせ、コストとセキュリティの懸念を解消するAIエージェント開発環境を構築します。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, ローカルLLM, LangChain, DeepAgents, Ollama]]

本記事は、高コストとセキュリティの課題を抱えるAIエージェント開発において、ローカルLLMとDeepAgentsを組み合わせた「使い放題」の環境構築方法を詳述しています。ChatGPTやDevinのようなAIエージェントが注目される一方で、LLMのヘビーな利用によるコスト増大や、外部API経由での情報漏洩リスクが懸念されています。これに対し、筆者は高性能化したローカルLLMと専用フレームワークを用いるアプローチを提案します。

具体的には、OllamaでOpenAIが公開した高ToolUse性能を持つオープンウェイトモデル「gpt-oss:20b」をローカル環境にデプロイし、LangChain/LangGraph v1.0に対応したAI Agent構築ライブラリ「DeepAgents」と連携させます。さらに、DeepAgents向けのUIを導入することで、ブラウザ経由でエージェントとのチャットが可能になります。記事では、Ollamaによるgpt-oss:20bのセットアップ、DuckDuckGo検索ツールを組み込んだDeepAgentsエージェントのPythonコード、そしてDeepAgents UIの立ち上げ手順を詳細に解説しています。特に、UIでファイルプレビューを可能にするため、カスタムの`LangGraphFilesystemBackend`を導入する工夫が紹介されています。

実際に「最新のVLM情報をまとめて」という指示を与えた結果、Web検索とファイル書き込みを通じてレポートが自動生成される様子が示されており、ローカル環境で高度なエージェントが動作する実証がなされています。ただし、TODO管理ツールの未更新やURLの表示形式といった、プロンプトや実装の調整が必要な点も正直に指摘されており、今後の改善の余地も提示されています。このソリューションにより、開発者は電気代以外のランニングコストを気にすることなく、内部ナレッジ連携やサブエージェント拡張を通じて、社内特化型のエージェントを完全ローカルで構築できる可能性が示唆されています。