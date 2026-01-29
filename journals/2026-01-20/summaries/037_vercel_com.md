## Vercel Workflow DevKitを活用した「耐久性のある」AIビデオワークフローの構築

https://vercel.com/blog/how-mux-shipped-durable-video-workflows-with-their-mux-ai-sdk

**Original Title**: How Mux shipped durable video workflows with their @mux/ai SDK

VercelのWorkflow DevKitを導入することで、AI処理中のタイムアウトやエラーによる再試行のコストと複雑性を解消する手法を紹介する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Vercel Workflow DevKit, Mux AI SDK, Durable Execution, AI Video Pipeline, Serverless Workflows]]

AIを活用したビデオ処理ワークフロー（コンテンツモデレーション、チャプター生成、要約など）は、複数のステップと外部APIへの依存が多いため、ネットワークタイムアウトやレート制限によって途中で失敗するリスクが常に付きまといます。従来、このような長時間のタスクを安全に実行するには、メッセージキューや状態管理、複雑なリトライロジックを備えたインフラを自前で構築する必要がありました。途中で失敗すれば、それまでに完了した高価なAI処理のコストが無駄になり、開発者はどこから再開するかを管理するコードに追われることになります。

Muxが開発したオープンソースの`@mux/ai` SDKは、この課題を解決するためにVercelの「Workflow DevKit」を採用しています。MuxのDylan Jhaveri氏は、開発者が複雑なインフラの意思決定に縛られることなく、使い慣れたJavaScript/TypeScriptのパターンで耐久性の高い（Durable）ワークフローを構築できる点を重要視しています。

Workflow DevKitの革新的な点は、Reactのディレクティブに近い「"use workflow"」や「"use step"」という注釈を利用するアプローチにあります。これにより、通常のNode.js環境では単なる標準的な関数として動作し（no-op）、Workflow DevKit環境下では自動的に状態の永続化、ステップごとのリトライ、オブザーバビリティ、および分散実行が有効になります。筆者によれば、これにより開発者はYAMLや新しいDSL（ドメイン固有言語）を学ぶ必要がなく、既存のコードに耐久性を「レイヤー」として追加できるようになります。

技術的な実装において、著者は「ステップの分離」を鍵として挙げています。例えば、ビデオの要約生成が成功した後にモデレーションでエラーが発生した場合、ワークフローは中断されますが、再実行時には完了済みの要約ステップの結果を永続化された状態から復元し、失敗した箇所から正確に再開します。これにより、APIの実行コストと時間を最小限に抑えられます。また、ステート保存先を抽象化した「Worlds」という概念により、ローカル（JSON）、Vercel（マネージド）、あるいはセルフホスト（Postgres/Redis）と実行環境を柔軟に切り替えられる可搬性も確保されています。

著者は、この耐久性のある実行モデルが、ビデオ処理に限らず、ドキュメント処理パイプラインやデータ同期、AIエージェントのオーケストレーションなど、外部依存を持つあらゆるマルチステッププロセスに応用可能であると主張しています。Webアプリケーションエンジニアにとって、サーバーレスのタイムアウト制約を超え、信頼性の高いAI機能を最小限のインフラ管理で提供するための極めて実用的なソリューションと言えます。