## ForgejoインスタンスをAIクローラーから守る方法

https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html

**Original Title**: How I protect my forgejo instance from AI Web Crawlers

サーバー負荷を引き起こすAIクローラーを回避するため、NginxでCookieとJavaScriptを組み合わせた軽量なアクセス制限を実装する手法を解説する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Forgejo, Nginx, AIクローラー, ボット対策, セルフホスト]]

著者は、自身のコードをホストするためにCodebergでも採用されているオープンソースのGitソフトウェア「Forgejo」を運用している。しかし、robots.txtを完全に無視し、Web APIを介して全コミット履歴をクロールしようとするアグレッシブなAIクローラーの猛攻を受け、インスタンスが頻繁にダウンする深刻なリソース不足（CPU/IO負荷）に直面した。

当初は完全なアクセス制限も検討したが、パブリックなフォージとしての公開性を維持するため、より低コストで効果的な対策を模索。重厚なボット対策ツールである「Anubis」などの導入も検討されたが、設定の複雑さやシステムへの負荷を嫌い、著者はNginxの設定のみで完結する「クイックでダーティな修正」を選択し、実行した。

この手法の核心は、HTTPステータスコード「418 I'm a teapot」とJavaScriptを組み合わせた認証フローにある。Nginx側で以下のロジックを実装している：
1. `User-Agent`がGitコマンドラインツール（`git/`や`git-lfs/`）である場合は、Gitクローン等の操作を妨げないよう無条件で許可する。
2. それ以外のブラウザアクセスの場合、特定のカスタムCookieがセットされているかを確認する。
3. Cookieがない場合、418エラーを返すと同時に、ブラウザ側でCookieをセットしてページを自動リロードさせる短いJavaScriptコードをHTMLとして出力する。

現在のAIクローラーの多くはHTTPリクエストを繰り返すだけであり、JavaScriptを実行してCookieを処理する能力を持たない。そのため、この段階でアクセスが遮断される。一方で、一般的なユーザーのブラウザであればJavaScriptが即座に実行されるため、一瞬のリロードを挟むだけで通常通りForgejoを利用できる。著者はこの挙動を「Anubis等の他ソリューションに比べてユーザーへの摩擦が最小限である」と評価している。

著者は、この対策がJavaScriptを解釈する高度なクローラーには通用しないことを認めつつも、現在のクローラー被害の多くは「質より量」を重視した単純なスクレイピングによるものであるため、現状はこの程度の障壁でも十分に効果的であると主張している。完璧な防御よりも、最小限の工数でサーバーの可用性を維持し、AIによる無断スクレイピングからリソースを守る実用的なアプローチとして提示されている。