## Advent Calendarの運営だってClaude Codeに任せたい —— Chrome DevTools MCPとPlaywright MCPでの自動化の記録

https://qiita.com/naopen/items/31c4221906d60247aa87

Claude CodeのMCPを活用し、Qiita Advent Calendarの運営作業を自動化する過程を通じて、その高度なトラブルシューティング能力と実用的な価値を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Claude Code, MCP, Webスクレイピング自動化, Chrome DevTools, LLMトラブルシューティング]]

KDDIアジャイル開発センターのアドベントカレンダー運営者が直面していた、新着記事の確認、情報収集、Slackへの投稿といった一連の定型作業は、毎日5〜10分を要し、コンテキストスイッチのコストやヒューマンエラーが頻発していました。この煩雑な作業をClaude CodeのMCP（Model Context Protocol）機能を用いて自動化したところ、作業時間が大幅に短縮され、その過程でClaude Codeの驚くべきトラブルシューティング能力が明らかになりました。

初期の自動化試行では、標準のFetch機能やPlaywright MCPを使用しましたが、Fetchでは必要な情報を取得できず、Playwrightではページ全体のレンダリングにより約19.2kトークンという巨大なコンテキスト消費が発生し、トークン制限の問題に直面しました。

そこで著者は、Claude CodeにQiita API v2ドキュメントを参照させた上で、よりスマートな情報取得を試みました。Claude CodeはまずAPIドキュメントを確認しましたが、アドベントカレンダーに関する情報がないと判断すると、自律的にデバッグを開始しました。具体的には、Chrome DevTools MCPを使ってブラウザのNetworkタブを調査し、裏側で呼ばれるAPIを探しました。それでも見つからないと見るや、存在しそうなAPIエンドポイントをcurlコマンドで推測して叩くといった、人間が行うような試行錯誤を見せました。

最終的に、APIでの情報取得が不可能と確定した後、Claude CodeはPlaywrightのようにページ全体をコンテキストに含めるのではなく、必要な情報だけを効率的に抽出するためのJavaScriptコードをその場で生成・注入し、DOMから正確なデータを取得することに成功しました。この方法により、巨大なトークン消費を避け、クリーンなJSONデータを取得できるようになりました。

この自動化により、毎朝5分かかっていた作業は30秒に短縮され、リンクの貼り間違いなどのヒューマンエラーも解消されました。著者は、Claude Codeが単にコードを生成するだけでなく、APIがないと判断すればDevToolsで調査し、それでもだめならJSを書いてDOMを解析するという、まるで新人エンジニアとペアプログラミングをしているかのようなトラブルシューティング能力を持っている点に感銘を受けています。この「人間臭い」試行錯誤のログは、LLMの挙動を理解する上で非常に示唆に富むと述べられています。ただし、Qiita API v2の利用に際しては、サーバー負荷をかけないよう節度ある利用を呼びかけています。