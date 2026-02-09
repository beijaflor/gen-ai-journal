## パッシブ・セーフなAPIの設計：障害に強く整合性を保つ実装パターン

https://www.danealbaugh.com/articles/passively-safe-apis

**Original Title**: Designing a Passively Safe API

外部APIの失敗やネットワークの不安定さを前提に、システム整合性を損なうことなく再試行を可能にする「パッシブ・セーフ」なAPIの設計指針を提示する。

**Content Type**: Technical Reference（技術リファレンス）
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 94/100 | **Overall**: 96/100

**Topics**: [[API Design, Idempotency, Transactional Outbox, Distributed Systems, Error Handling]]

マイクロサービス移行期における実務的な教訓に基づき、障害発生時でもデータ整合性を維持し、副作用なしに再試行を可能にする「パッシブ・セーフ（受動的に安全）」な設計を解説している。単一のトランザクションでは完結しない外部API連携や非同期処理において、**Transactional Outbox**パターンを用いたメッセージ配信の保証や、**Message Inbox**によるコンシューマ側の重複排除の重要性を詳述。特に、POSTやPATCHリクエストを安全にするための**Idempotency-Key（冪等性キー）**の導入と、リクエスト処理を複数の**Atomic Phase**に分割して**Recovery Point**をデータベースに記録する実装モデルは、コードレベルの具体性があり非常に有用だ。

また、**Exponential Backoff**と**Jitter**を用いた再試行戦略や、一時的なエラーを識別してキャッシュ可否を判断する**is_transient**フラグの活用、期限切れキーのクリーンアップ（リーパー処理）など、運用上の詳細な注意点も網羅されている。分散システムにおける「不完全な成功」や「部分的な失敗」によるデータ不整合に悩むウェブアプリケーションエンジニアにとって、堅牢なAPIを構築するための実践的なバイブルとなる内容だ。