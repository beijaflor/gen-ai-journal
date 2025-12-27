## Temporal における実行境界を超えるコンテキスト伝搬の仕組み

https://tech.layerx.co.jp/entry/temporal-context-propagation

分散ワークフローエンジンである Temporal において、Client、Workflow、Activity という異なる実行境界をまたいでコンテキスト情報を一貫して伝搬させる実装手法を解説する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Temporal, 分散システム, Go, TypeScript, Observability]]

分散ワークフローエンジンである Temporal において、Client、Workflow、Activity という物理的・論理的に分離された実行境界を越えて、トレース ID やテナント ID といったコンテキスト情報を一貫して伝搬させる手法を解説した技術記事である。Temporal の特性上、各要素は異なるプロセスやネットワークで実行される可能性があり、Durable である（実行が中断・再開される）ため、Go の `context.Context` のような標準的なメモリ内での伝搬仕組みが機能しない。そのため、分散システムにおける観測可能性（Observability）の担保や、リクエストごとのテナント制御を実現するには、Temporal のヘッダー機能を介した明示的な伝搬メカニズムが不可欠となる。

Go SDK に関しては、標準で提供されている `ContextPropagator` インターフェースの活用に焦点を当てている。著者は、`Inject`（Client からヘッダーへ）、`ExtractToWorkflow`（ヘッダーから Workflow へ）、`InjectFromWorkflow`（Workflow からヘッダーへ）、`Extract`（ヘッダーから Activity へ）という 4 つのフェーズでの実装方法を、テナント ID の伝搬を例に具体的なコードで示している。これにより、開発者は Go の `context.Context` や `workflow.Context` を通じて、ネットワーク境界を意識せずにデータへアクセス可能になる。

一方、TypeScript SDK には公式のプロパゲーター機能が未実装であるため、Node.js の `AsyncLocalStorage` と Temporal の `Interceptor` を組み合わせた代替案を提示している。Client、Workflow、Activity の各レイヤーでインターセプターを定義し、ペイロードコンバーターを用いてデータのシリアル化と復元を行う実装は、TypeScript 環境で分散トレーシングを実現するための重要なプラクティスと言える。

筆者は、LayerX の AI エージェント基盤においてこの仕組みを導入しており、実際のプロダクション環境での運用を想定した設計となっている。特に「なぜ通常のコンテキストが使えないのか」という根本的な課題の提示から、各言語 SDK の内部構造に踏み込んだ具体的な回避策までを網羅しており、Temporal を用いた大規模な Web アプリケーション開発におけるシステム設計の重要な指針となる内容である。