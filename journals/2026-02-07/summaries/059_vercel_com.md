## Vercel Sandboxが一般公開：AIエージェント向けのセキュアなコード実行環境を提供

https://vercel.com/blog/vercel-sandbox-is-now-generally-available

**Original Title**: Run untrusted code with Vercel Sandbox, now generally available

提供を開始する：AIエージェントが信頼できないコードを安全かつ高速に実行できる、LinuxマイクロVM基盤の一般公開により、エージェント開発のインフラ課題を解決する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 88/100 | **Overall**: 84/100

**Topics**: [[Vercel Sandbox, AI Agents, MicroVM, Firecracker, Security]]

Vercelは、AIエージェントがコードの実行やテストを安全に行うための専用環境「**Vercel Sandbox**」の一般公開（GA）を発表しました。本製品は、Vercelのデプロイ基盤を支える**Firecracker**ベースのマイクロVM技術を活用しており、1秒未満の高速起動と完全な分離環境を実現しています。

主な機能として、**sudo権限**付きのLinux環境、エフェメラル（一時的）な動作、そして複雑な環境状態を即座に復元できる**スナップショット機能**を備えています。これにより、エージェントはリポジトリのクローンや依存関係のインストールといった準備時間を省き、即座にタスクを再開できます。開発者はオープンソースの**CLI**や**SDK**を通じて、自身のアプリケーションにこの実行レイヤーを容易に組み込むことが可能です。

AIエージェントやコーディング支援ツールを開発しており、ユーザーから提供された信頼できないコードをセキュアかつスケーラブルな環境で実行したいエンジニアに最適です。