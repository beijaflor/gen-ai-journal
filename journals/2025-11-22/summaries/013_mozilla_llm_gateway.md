## any-llm-gatewayでLLMの支出とアクセスを管理

https://blog.mozilla.ai/control-llm-spend-and-access-with-any-llm-gateway/

**Original Title**: Control LLM Spend and Access with any-llm-gateway

Mozilla.aiが、複数のLLMプロバイダーの費用とアクセスを効率的に管理できるオープンソースのプロキシサーバー「any-llm-gateway」をリリースしました。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[LLMコスト管理, APIゲートウェイ, LLMプロキシ, アクセス制御, 利用状況分析]]

Mozilla.aiは、複数のLLMプロバイダーへの一貫したインターフェースを提供するPythonライブラリ「any-llm」の機能拡張として、オープンソースのプロキシサーバー「any-llm-gateway」を公開しました。これは、LLMのコストとアクセス管理におけるWebアプリケーションエンジニアの課題を解決することを目的としています。無制限なアクセスによるコストの増大と、厳しすぎる制限によるイノベーションの停滞というジレンマに対し、このゲートウェイは可視性と制御をもたらします。

any-llm-gatewayは、アプリケーションとLLMプロバイダーの間に位置し、OpenAI互換のCompletions APIを公開することで、OpenAI、Anthropic、Mistral、ローカルモデルなど、any-llmがサポートするあらゆるプロバイダーに統一された方法でアクセスできます。これにより、`provider:model`形式（例: `openai:gpt-4o-mini`）でモデルを指定するだけで、自動トークン追跡を含むストリーミングサポートにも対応します。

主な機能として、自動リセット機能付きの共有予算層を作成できる「スマート予算管理」があり、複数のユーザー間で予算を共有したり、自動強制または追跡のみのモードで運用したりできます。また、マスターキー認証と、有効期限やメタデータを設定可能な「柔軟なAPIキーシステム」を提供し、ユーザーごとの支出追跡を可能にします。さらに、すべてのリクエストとトークン数、コストが記録される「完全な利用状況分析」により、コスト配分とチャージバックに必要な観測性を提供します。本ゲートウェイはDockerやKubernetesによるデプロイにも対応しており、本番環境での利用が容易です。これにより、SaaSアプリケーションの段階的料金設定、研究チームのLLMアクセス管理、組織全体のコスト管理など、幅広いユースケースで自信を持ってLLMアクセスを展開、予算化、監視、制御できるようになると筆者は述べています。