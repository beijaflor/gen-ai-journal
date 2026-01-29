## AI スクレイパーによるサービス障害への対応

https://blog.metabrainz.org/2025/12/11/we-cant-have-nice-things-because-of-ai-scrapers/

**Original Title**: We can't have nice things… because of AI scrapers

MetaBrainz財団がAI企業による過度なウェブスクレイピングからのサービス保護のため、複数のAPI endpoint へのアクセス制限を実施しました。

**Content Type**: 📢 News & Announcements
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 72/100 | **Annex Potential**: 65/100 | **Overall**: 70/100

**Topics**: [[AI スクレイピング, API セキュリティ, サービス過負荷対策, robots.txt 無視問題, ListenBrainz 保護]]

MetaBrainz 財団は、AI 企業による無分別なウェブスクレイピング攻撃に対抗するため、ListenBrainz の複数 API endpoint に認証要件を追加しました。同財団は「robots.txt を無視」し、1 ページずつ読み込むAIスクレイパーが「何百年かかる」ような非効率な方法でサーバーを過負荷にしていると説明しています。

具体的な対応として、メタデータ検索 API は Authorization トークンの送信を必須化し、Labs API 端点を廃止、LB Radio 機能をログイン必須に変更しました。この急な変更は「サービスを許容可能なレベルで維持する」ために必要だったと述べられています。

このケースは、AI 開発企業の多くが公開データセットを見落とし、自動化された低効率なスクレイピングに頼る傾向を浮き彫りにしています。コミュニティからは「公開データベースのダウンロードを推奨する robots.txt 標準」や「ポイズニング手法」など、防御手段についての提案も寄せられています。
