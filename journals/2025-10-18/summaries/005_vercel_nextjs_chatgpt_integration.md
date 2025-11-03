## ChatGPT内でNext.jsを実行する：ネイティブアプリ統合への深掘り

https://vercel.com/blog/running-next-js-inside-chatgpt-a-deep-dive-into-native-app-integration

**Original Title**: Running Next.js inside ChatGPT: A deep dive into native app integration

Vercelは、ChatGPTの多層iframe環境下でNext.jsアプリケーションをネイティブに動作させるための包括的な技術的課題を解決し、そのためのSDKとスターターテンプレートを公開しました。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 92/100

**Topics**: [[Next.js, ChatGPT Apps, Iframe Integration, Web Development Patches, Model Context Protocol]]

OpenAIがApps SDKとModel Context Protocol (MCP) のサポートを発表したことで、ChatGPT内にWebアプリケーションを直接組み込む道が開かれました。Vercelはこの機会を捉え、Next.jsアプリケーションをChatGPTの厳格な多層iframeアーキテクチャ内でネイティブに動作させるための深い技術的課題に取り組み、その解決策を公開しました。この取り組みは、Next.jsのクライアントサイドナビゲーション、React Server Components (RSC)、ダイナミックルーティングといったモダンな機能が、iframeのセキュリティモデルによってどのように阻害されるかという問題に焦点を当てています。

著者は、この統合が既存のNext.js開発者にとって、アプリケーションを再構築することなく8億人以上のChatGPTユーザーに配布できる大きな機会であると強調しています。しかし、そのためには、以下に示すNext.jsのコア機能を破壊するような数々の技術的障害を克服する必要がありました。

主な課題とVercelによる解決策は以下の通りです。
1.  **アセットの読み込み問題**: Next.jsが `/ _next` 形式で生成するアセットパスが、iframeのサンドボックスドメインに解決されてしまう。
    *   **解決策**: `next.config.ts` で `assetPrefix` をアプリの実際のURLに設定し、正しいオリジンからアセットを強制的にロード。
2.  **相対URLの解決問題**: 画像、フォント、APIコールなどの相対パスがサンドボックスドメインに解決される。
    *   **解決策**: HTMLの `<base>` 要素を `app/layout.tsx` に挿入し、すべての相対URLの基準をアプリの実際のドメインに設定。
3.  **ブラウザ履歴のURL漏洩**: `history.pushState` や `history.replaceState` が完全なURLを保存し、iframeのセキュリティ境界を破る。
    *   **解決策**: `history` APIの呼び出しをインターセプトし、パス、検索クエリ、ハッシュのみを履歴に保存するようにパッチを適用。
4.  **クライアントサイドナビゲーションの失敗**: Next.jsの `Link` クリック時に、`fetch` リクエストがiframeのドメインに送られる。
    *   **解決策**: `window.fetch` をパッチし、iframeのオリジンをターゲットとするリクエストをアプリの実際のオリジンに書き換え、クロスオリジンリクエスト用に `mode: "cors"` を追加。
5.  **CORSによるRSCのブロック**: iframeからサーバーへのクロスオリジンRSCリクエストがCORSポリシーでブロックされる。
    *   **解決策**: Next.jsのミドルウェアを使用し、OPTIONSプリフライトリクエストに応答し、すべてのレスポンスに適切なCORSヘッダーを追加。
6.  **親フレームによるDOM改変**: ChatGPTの親フレームがルート `<html>` 要素に属性を追加し、Reactのハイドレーション不一致エラーを引き起こす。
    *   **解決策**: `MutationObserver` を使用してルート `<html>` 要素の属性変更を監視し、不正な変更を即座に除去。
7.  **外部リンクのiframe内表示**: 外部リンクがiframe内で開かれてしまい、ユーザー体験を損なう。
    *   **解決策**: `window.openai.openExternal()` APIを使用して外部リンクをユーザーのブラウザで開くようにイベントリスナーで処理。

これらのブラウザAPIパッチに加えて、VercelはMCPサーバーの実装も行いました。MCPサーバーは、リソース（ChatGPTがHTMLをレンダリング）とツール（モデルが呼び出すアクション）を公開し、`openai/outputTemplate` を通じてツールとリソースを連携させます。アプリケーションは `window.openai.toolOutput` プロパティを通じてツール呼び出しからのデータを受け取り、Reactの状態を更新できます。さらに、`useSendMessage`、`useWidgetProps`、`useDisplayMode` といったReactフックが提供され、開発者の体験を向上させています。

このアプローチにより、ネイティブNext.jsナビゲーション、Next.jsの全機能セットの利用、変更されない開発者体験、標準Next.jsアプリに匹敵するパフォーマンス、そして統合されたユーザー体験が実現されます。Vercelはこれらのパッチをすべて組み込んだスターターテンプレートを提供しており、開発者は複雑なブラウザAPIとの格闘ではなく、アプリの機能開発に集中できるようになります。