## New Relic と LiteLLM Proxy と OpenTelemetry

https://qiita.com/shohei_yamamoto/items/411fb286dfe017fc8960

複数のLLMプロバイダーを一元管理するLiteLLM Proxyを導入し、OpenTelemetryを介してNew Relicで利用状況やコストを可視化する具体的な構築手法を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 75/100 | **Overall**: 76/100

**Topics**: [[New Relic, LiteLLM, OpenTelemetry, LLM Gateway, Amazon Bedrock]]

### 概要
本記事は、KIYOラーニング株式会社のエンジニアが、LLM運用の効率化を目指してLLMゲートウェイである「LiteLLM Proxy」とオブザーバビリティプラットフォーム「New Relic」をOpenTelemetry（OTel）で統合した検証記録である。

著者は、今後プロダクトや社内で利用するLLMが増加することを見据え、複数のプロバイダー（OpenAI、Anthropic、Azure AI、Amazon Bedrock等）へのアクセスを一元化し、セキュリティや運用の効率を向上させる「LLMゲートウェイ」の必要性を強調している。その中でも、ベンダー中立な標準規格であるOpenTelemetryを利用することで、特定の監視ツールに縛られずに詳細なテレメトリデータを収集できる構成を提案している。

具体的な実装では、Docker Composeを用いた環境構築手順が示されている。LiteLLM ProxyからNew Relicへデータを送信するためのOTLP（OpenTelemetry Protocol）設定や、Amazon Bedrockをバックエンドとして利用するためのコンフィグレーションが詳細に解説されている。特に、New Relicが推奨する `http/protobuf` プロトコルの指定や、APIキーによる認証、サービス名の定義など、実戦的な設定項目が網羅されている。

検証の結果、New Relic上の「Distributed tracing」や「Span」データを通じて、リクエストごとの会話ログ（プロンプトとレスポンス）だけでなく、入力・出力トークン数に基づくコスト情報（`gen_ai.cost.*` 属性）まで正確に記録・可視化できることが確認された。著者は、これらのデータをNRQLで集計することで、将来的に独自のダッシュボードを作成し、LLM利用の透明性と運用効率を高めることが可能になると結論付けている。

Webアプリケーションエンジニアにとって、急速に普及するLLM機能を本番環境で運用する際、「誰が、どのモデルを、どれだけのコストで利用しているか」を把握することは喫緊の課題である。標準規格であるOpenTelemetryを軸に据えたこの構成は、既存の監視エコシステムにLLM運用をスムーズに組み込むための現実的かつ強力な解法を提示している。