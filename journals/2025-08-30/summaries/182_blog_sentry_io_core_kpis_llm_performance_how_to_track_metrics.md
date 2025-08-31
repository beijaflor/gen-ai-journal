## The core KPIs of LLM performance (and how to track them)

https://blog.sentry.io/core-kpis-llm-performance-how-to-track-metrics/

Sentryは、LLMアプリケーションの信頼性、コスト効率、ユーザー体験を最適化するための主要KPI10選とその追跡方法を詳説しています。

**Content Type**: 🛠️ Technical Reference

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 78/100 | **Overall**: 80/100

**Topics**: [[LLM Observability, Performance Metrics, Cost Management, User Experience, Agent Orchestration]]

LLMアプリケーションの健全性を測るには、単なるプロンプトとレスポンスの監視だけでは不十分であり、信頼性、コスト効率、ユーザー体験の3つの側面からKPIを体系的に監視することが不可欠である、とSentryは指摘しています。本記事は、Webアプリケーション開発者が直面しがちな「巨大なJSONペイロードによるコンテキストウィンドウの枯渇」「無限ループによるトークン消費の急増」「ツール呼び出しのタイムアウト」といった現実の問題を防ぐため、具体的な監視指標とその重要性を提示します。

主要なKPIとして、エージェントトラフィック、LLM生成数（モデル別）、ツール呼び出しの回数と期間、トークン使用量、LLMコスト、エンドツーエンドレイテンシ（特にファーストトークン）、クリティカルステップ期間、エラー数とエラー率、エージェント呼び出しとネストの深さ、ハンドオフの10項目が挙げられています。これらの指標は、モデルの変更による出力品質の低下や、Vector DBの不安定さによる応答遅延といった、LLMアプリ特有の運用リスクに直結します。

記事では、SentryのAI Observabilityを例に挙げ、これらのKPIを追跡するためのダッシュボードやアラートの設定方法、そしてデプロイや機能フラグを重ね合わせることで根本原因分析を迅速化する実践的なヒントを提供します。特に、運用テレメトリーに焦点を当て、プロンプトや出力のプライバシーを保護しつつ、開発者がLLMアプリケーションの健全性を維持し、安定したサービス提供を行う上で極めて実用的な指針となります。