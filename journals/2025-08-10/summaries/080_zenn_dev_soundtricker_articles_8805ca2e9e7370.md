## Agent Development Kit 1.9.0 で追加された 新たなPluginのCallback

https://zenn.dev/soundtricker/articles/8805ca2e9e7370

ADK 1.9.0は、Agent Development Kitに新たなエラーハンドリング用コールバックを追加し、エージェントやツールの例外処理を大幅に簡素化します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Agent Development Kit, Agent Frameworks, Error Handling, LLM Agents, Developer Tools]]

Agent Development Kit (ADK) 1.9.0がリリースされ、特に「on_tool_error_callback」と「on_model_error_callback」という新しいPluginのCallback機能が注目されます。これは、ADKを用いたAIエージェント開発におけるエラーハンドリングの課題を根本的に解決します。

これまで、ADKのエージェントやツール内で例外が発生すると、そのエラーはRunnerの外部にスローされ、開発者はRunnerの呼び出し元で複雑なtry-exceptブロックやwhileループを用いて再試行ロジックを実装する必要がありました。これによりコードは煩雑になり、状態管理も困難でした。

今回のアップデートで追加された新しいコールバックは、ツールやLLMの実行中にエラーが発生した際に、その場で処理を差し込むことを可能にします。例えば、ツールが一時的に失敗した場合、on_tool_error_callback内で自動的にリトライ回数を管理し、適切なエラーメッセージをLLMに返すことで、エージェント自身に処理を継続させることができます。これにより、外部にエラーが伝播するのを防ぎ、呼び出し元のコードを大幅に簡素化できます。

Webアプリケーションエンジニアにとって、この機能はAIエージェントの堅牢性と信頼性を向上させる上で極めて重要です。APIレート制限やネットワークエラーなど、外部要因によるツールの失敗は日常的に発生します。これらのエラーをエージェント内部でスマートに処理し、自動回復させる仕組みは、より安定したユーザー体験を提供し、運用コストを削減します。クリーンで保守性の高いエージェントコードは、開発効率を大きく高めるでしょう。