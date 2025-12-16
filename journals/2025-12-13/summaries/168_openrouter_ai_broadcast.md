## OpenRouterのBroadcast機能：LLM利用の可視化

https://openrouter.ai/docs/guides/features/broadcast/overview

**Original Title**: Broadcast | OpenRouter Observability

OpenRouterは、LLMリクエストのトレースデータを外部オブザーバビリティプラットフォームへ自動送信する「Broadcast」機能をリリースし、開発者がアプリケーションコードを変更することなくLLM利用の監視、デバッグ、分析を可能にした。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 87/100 | **Annex Potential**: 83/100 | **Overall**: 88/100

**Topics**: [[LLM Observability, API Monitoring, OpenRouter, Debugging, AI Workflow]]

OpenRouterが、LLMリクエストのオブザーバビリティを強化する新機能「Broadcast」のベータ版をリリースした。この機能により、アプリケーションコードに特別な計測を追加することなく、OpenRouter経由のLLM呼び出しに関する詳細なトレースデータを、外部のオブザーバビリティおよび分析プラットフォームに自動的に送信できるようになる。これは、ウェブアプリケーションエンジニアがLLMの利用状況を効率的に監視、デバッグ、分析するための重要な改善点となる。

Broadcast機能は、OpenRouterのダッシュボード設定から簡単に有効化でき、Braintrust、Datadog、Langfuse、LangSmith、Weave、S3 OTel Collectorなど、複数の主要な宛先をサポートしている。送信されるトレースデータには、リクエストとレスポンスのデータ（マルチモーダルコンテンツは効率のために除去）、トークン使用量、コスト情報、タイミング、モデル情報、ツール利用状況など、包括的な情報が含まれる。

特に重要なのは、オプションで「user ID」や「session ID」をAPIリクエストに含めることで、特定のユーザーや会話、エージェントワークフローに関連付けてトレースを追跡・デバッグできる点だ。さらに、各宛先ごとにAPIキーフィルタリングやサンプリングレートを設定できるため、開発環境と本番環境で異なる監視ポリシーを適用したり、高ボリュームのアプリケーションでデータ量やコストを管理しながらも可視性を維持したりすることが可能となる。サンプリングはセッションIDに基づいて行われるため、セッション全体の一貫したデータが得られる。

セキュリティ面では、宛先認証情報は暗号化されて保存され、トレースの送信はリクエスト完了後に非同期で行われるため、APIレスポンスの遅延は発生しない。また、個人アカウントだけでなく組織アカウントでも設定可能で、組織管理者はチーム全体で一貫したオブザーバビリティを確保できる。この機能は、LLMをプロダクション環境で利用する際の運用効率とデバッグ能力を大幅に向上させるものとして、注目に値する。