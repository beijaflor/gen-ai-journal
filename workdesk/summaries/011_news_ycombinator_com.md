## jQuery 4.0正式リリース：現代的な仕様への刷新とレガシーブラウザの整理

https://news.ycombinator.com/item?id=46664755

**Original Title**: jQuery 4 | Hacker News

現代的なWeb標準への刷新とレガシーブラウザの整理を断行し、jQuery 4.0として約10年ぶりのメジャーアップデートを実施した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[jQuery, JavaScript, Web Standards, Browser Compatibility, Legacy Maintenance]]

10年以上の歳月を経てメジャーアップデートされた**jQuery 4.0**のリリースについて。内部コードを**ESモジュール**へ完全移行し、**IE11未満**や古いEdge、iOS、Androidブラウザのサポートを終了した。**Trusted Types**への対応や**Content Security Policy (CSP)**に関連する脆弱性への対策など、現代的なセキュリティ要件が盛り込まれている。

Hacker Newsの議論では、**HTMX**や**Vanilla JS**が普及した現代におけるjQueryの意義が焦点となっている。メソッドチェーンによる高い可読性や、**WordPress**などの巨大エコシステムにおける保守上の利便性が再評価される一方で、コードの整理に伴う一部の非推奨API（`isArray`等）の削除には注意が必要だ。

既存のjQueryベースのプロジェクトを抱える保守エンジニアや、SPAフレームワークを使わずに効率的なDOM操作を求める開発者にとって、移行の是非を判断すべき重要なマイルストーンといえる。