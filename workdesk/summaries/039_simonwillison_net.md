## Chrome 版 Claude を活用し Cloudflare ダッシュボードの迷宮から設定を特定

https://simonwillison.net/2025/Dec/22/claude-chrome-cloudflare/

**Original Title**: Using Claude in Chrome to navigate out the Cloudflare dashboard

ブラウザエージェント「Claude in Chrome」を利用して、複雑な Cloudflare ダッシュボード内から特定の CORS 設定箇所を 2 分弱で正確に突き止める。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Claude in Chrome, Browser Agents, Cloudflare, CORS, Developer Productivity]]

著名な開発者 Simon Willison 氏が、ブラウザエージェント「Claude in Chrome」拡張機能を実務のトラブルシューティングに活用した成功体験を報告している。氏は、自身の S3 バケット経由で配信している特定のディレクトリに CORS（Access-Control-Allow-Origin: *）設定が適用されている理由を思い出せず、複雑な Cloudflare ダッシュボード内を自力で探索することに限界を感じていた。当初は S3 側の設定を疑ったが、プレフィックス単位の CORS 設定が S3 では不可能なことから Cloudflare 側に原因があると推測したものの、膨大なメニューの中から目的の設定画面に辿り着けずにいた。

この課題に対し、氏は Chrome 内で動作する Claude エージェントを起動し、「なぜこのディレクトリに CORS ポリシーが適用されているのか、Cloudflare の設定箇所を探してほしい」とプロンプトを入力した。エージェントは自律的にダッシュボード内を探索し、わずか 1 分 45 秒で正確な設定箇所（Transform Rules 内の Response Header Transform Rule）を特定することに成功した。著者はこのやり取りを公開するため、公式の共有機能がない代わりに「Claude Code」を駆使して操作ログを HTML 形式のトランスクリプトへ変換し、そのプロセスの透明性を確保している。

著者は、この経験の重要性を「複雑な SaaS の管理画面を人間が手動で探索する苦痛を、AI エージェントが劇的に軽減できる可能性」にあると説明している。特に Cloudflare のように階層が深く多機能なツールの UI において、ドキュメントを読み漁ることなく自然言語での問い合わせから直接設定箇所に到達できるメリットは計り知れない。設定の「場所」を忘れてしまうことはエンジニアにとって頻繁に起こる問題であり、UI の迷宮をショートカットする手段としてのエージェントの有効性を示している。

一方で、著者はブラウザエージェントというカテゴリ全体に対して、依然として深い懐疑心を抱いていることも強調している。最大の懸念点は、信頼できないウェブサイトからの指示がエージェントを乗っ取る「プロンプトインジェクション」のリスクである。氏は今回、エージェントがブラウザ上で動作する様子を「鷹のような鋭い目で見守っていた」と述べており、利便性は認めつつも、高度な権限を持つエージェントを自由奔放に動作させることへの危険性に警鐘を鳴らしている。この事例は、単なるテキスト生成を超えた「ブラウザ操作を伴う AI」が、開発者の日常的な運用タスクや設定管理のワークフローをどのように変革し得るかを示す、具体的かつ示唆に富むユースケースとなっている。