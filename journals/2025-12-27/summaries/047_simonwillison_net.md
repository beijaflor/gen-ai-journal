## Claude in Chromeを使用してCloudflareの複雑なダッシュボード設定を特定する

https://simonwillison.net/2025/Dec/22/claude-chrome-cloudflare/

**Original Title**: Using Claude in Chrome to navigate out the Cloudflare dashboard

ブラウザエージェント「Claude in Chrome」を活用し、複雑なCloudflareダッシュボード内から特定のCORS設定を短時間で発見した実体験を報告する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 79/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Claude in Chrome, Browser Agents, Cloudflare, CORS, Developer Experience]]

エンジニアであり著名な技術ブロガーであるSimon Willison氏が、ブラウザエージェント「Claude in Chrome」拡張機能を使用して、複雑なCloudflareダッシュボードの中から迷子になっていた設定箇所を特定した成功事例を報告している。

背景として、筆者は自身のS3バケット上の特定ディレクトリに対して、以前設定したはずのオープンなCORSポリシー（Access-Control-Allow-Origin: *）のソースを探していた。S3のバケットレベルの設定ではなく、Cloudflare側で設定した可能性を疑ったものの、機能が膨大でナビゲーションが困難なCloudflareの管理画面から該当箇所を自力で見つけ出すのは時間がかかる作業だった。そこで筆者は、Chrome上で動作するAIエージェントであるClaudeに対し、設定場所を特定するようプロンプトで依頼した。

Claudeのエージェント機能は、筆者のログイン済みのダッシュボードを自律的に探索し、わずか1分45秒で正解に辿り着いた。結論として、その設定はCloudflareの「Transform Rules（変換ルール）」内の「Response Header Transform Rule」として定義されていた。筆者はこれまで、プロンプトインジェクションのリスクなどのセキュリティ上の懸念から、ブラウザエージェントというカテゴリーに対して強い懐疑心を持っていたが、今回の経験を通じてその実用性を高く評価している。

著者が強調しているのは、開発者にとっての「UIの複雑さ」という摩擦をAIが解消する可能性だ。どれほど熟練したエンジニアであっても、稀にしか触らないSaaSのダッシュボードの奥深くにある設定を見つけ出すのは時間の浪費になりがちである。Claudeのようなエージェントが、ユーザーの権限で安全にブラウザを操作し、必要な情報に直接アクセスできることは、ワークフローの劇的な効率化に繋がる。一方で著者は、エージェントの動作を注意深く監視し、リスクを認識した上で利用すべきであるという慎重な姿勢も示している。この事例は、単なる情報の要約やコード生成に留まらない、AIによる「複雑なツール操作の代行」という新たなフェーズの有用性を具体的に示している。