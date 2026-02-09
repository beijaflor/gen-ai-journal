## Vercel Workflow 4.1 Beta公開：イベントソーシングへの移行で自己修復機能を実現

https://vercel.com/changelog/workflow-event-sourcing

**Original Title**: Workflow 4.1 Beta: Event-sourced architecture

ワークフローの状態管理にイベントソーシングを採用し、分散システムの信頼性とスループットを大幅に向上させる。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Vercel Workflow, Event Sourcing, NestJS, AI Agent, TypeScript]]

Vercelは、長期実行型の分散ワークフローを構築する**Vercel Workflow**の最新アップデート「4.1 Beta」を公開しました。最大の変化は、状態管理アーキテクチャに**イベントソーシング（Event-sourced architecture）**を採用した点です。内部状態を直接更新するのではなく、すべての変更を追記型のイベントログとして保存し、必要に応じて再生（リプレイ）して状態を再構築します。これにより、キューのメッセージ紛失や競合状態からの**自己修復（Self-healing）**が可能になり、完全な監査ログによるデバッグの容易性と高いデータ整合性を実現しました。

また、システム全体のスループットが強化され、毎秒数千ステップの並列処理が可能になったほか、**Google Search**などのプロバイダー実行ツールのサポート、`@workflow/nest`パッケージによる**NestJS**との統合、TC39の**Explicit Resource Management**（`using` 宣言）のサポートなど、実用的な機能が多数追加されています。信頼性の高いAIエージェントのオーケストレーションや、複雑なビジネスロジックの非同期実行をTypeScriptで実装したい開発者にとって、導入の大きな障壁が解消されたアップデートです。