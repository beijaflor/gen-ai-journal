## Mackerel MCPサーバーを活用してAIでISUCONを解いてみよう——問題発見から改善まで全部AIで！

https://mackerel.io/ja/blog/entry/tech/ai-isucon

検証する：Mackerel MCPサーバーとClaude Codeを組み合わせ、計測データに基づいたAIによる自律的なWebアプリケーションのボトルネック分析とパフォーマンス改善を実証する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[MCP (Model Context Protocol), Mackerel, ISUCON, パフォーマンスチューニング, Claude Code]]

**Mackerel**のエンジニアが、自社の**Mackerel MCPサーバー**と**Claude Code**を連携させ、ISUCON 9 予選の課題解決をAIに完全自動化させた検証結果を公開しました。システムの「目」となる監視データ（メトリクス・トレース）を**MCP (Model Context Protocol)**経由でAIに提供することで、AIが自律的にボトルネックを特定し、コード修正とベンチマーク検証のサイクルを回す手法を解説しています。

技術的なポイントとして、**OpenTelemetry**を基盤としたAPM機能の活用に加え、コード変更なしで計装可能な**OBI (OpenTelemetry eBPF Instrumentation)**による計測手法を紹介しています。検証では、AIが「データベースのトランザクション内で重い外部APIを呼び出している」というボトルネックを正確に特定。これをトランザクション外に移動させる修正を自ら適用した結果、初期スコアの約27倍となる50,280点まで改善することに成功しました。

「推測するな、計測せよ」という原則をAIエージェントに実行させるための具体的なプロンプト構造や、計測インフラの構成が具体的に示されています。AIによる自律的なデバッグや、パフォーマンスチューニングの自動化を検討しているエンジニアにとって、実用的なリファレンスとなる内容です。