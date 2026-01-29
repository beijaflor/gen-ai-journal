## Vercel AI GatewayでPerplexity Web Searchを利用可能に

https://vercel.com/blog/use-perplexity-web-search-with-vercel-ai-gateway

**Original Title**: Use Perplexity Web Search with Vercel AI Gateway

プロバイダーに依存せず、一行のコードであらゆるLLMにリアルタイムなWeb検索能力を統合できる機能をVercel AI Gateway経由で提供する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[Vercel AI Gateway, AI SDK, Perplexity, Web Search, Multi-LLM]]

Vercelは、AI Gatewayを通じてPerplexityのWeb検索機能を任意のLLMに統合できる新機能を発表した。従来、大規模言語モデル（LLM）は学習データのカットオフ日により、最新のニュースや価格変動、最新のAPI仕様といった「今日」の情報にアクセスできないという根本的な課題を抱えていた。一部のハイエンドモデルは独自の検索機能を備えているが、提供プロバイダーによってツール呼び出しの仕様や検索結果の精度が異なり、複数のモデルを併用するアプリケーションにおいては実装の複雑化や挙動の不一致を招く要因となっていた。

今回のアップデートにより、開発者はVercel AI Gatewayを介して、プロバイダーに依存しない（provider-agnostic）Web検索機能をシームレスに導入可能になる。具体的には、Vercel AI SDKの`gateway.tools.perplexitySearch()`を利用することで、OpenAI、Anthropic、Googleといった主要プロバイダーのモデルはもちろん、ネイティブな検索機能を持たないMinimaxやZhipu AI (GLM)などのモデルに対しても、リアルタイムな情報取得能力を付与できる。

Webアプリケーションエンジニアにとってこの機能が重要な理由は、開発ワークフローの自動化と運用における柔軟性の向上に直結するからである。例えば、CIアシスタントやコード生成ツールにこの検索機能を組み込めば、最新のパッケージバージョンや修正されたばかりの脆弱性情報、最新のフレームワークドキュメントに基づいた正確なコード提供が可能になり、古い情報によるビルド失敗を防ぐことができる。また、コスト最適化やフェイルオーバーのために複数のモデルを動的に切り替えているプロダクション環境のチャットボットにおいて、検索ロジックをモデルごとに書き換える必要がなくなり、メンテナンス性が劇的に向上する。

著者は、LLMが持つ強力な推論能力を「現在」の情報と結びつけることで、モデルの知識限界という制約を解消できる点に最大の価値を置いている。価格設定は1,000リクエストあたり5ドルとされており、Perplexityの直接利用と同等のコストで提供される。特定のドメインのみを検索対象にするフィルター設定なども可能であり、信頼性の高い情報源に絞ったエージェント構築を容易にする実用的なツールとなっている。