## Cloudy Summarizations of Email Detections: Beta Announcement

https://blog.cloudflare.com/cloudy-driven-email-security-summaries/

Cloudflareは、AIエージェント「Cloudy」を活用し、複雑なメールセキュリティ検出ロジックを簡潔に要約するベータ機能を発表、セキュリティチームの脅威分析効率を飛躍的に高めます。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[AIセキュリティ, メールセキュリティ, Large Language Models, RAG, SOCワークフロー]]

Cloudflareは、同社のAIエージェント「Cloudy」に、複雑なメールセキュリティ検出結果を要約する新機能をベータ版として導入しました。この機能は、巧妙化するフィッシングやビジネスメール詐欺（BEC）から顧客を保護するため、Cloudflareが日々展開する多数のAI/MLモデルによる検出ルールの詳細を、セキュリティ運用センター（SOC）チームが迅速に理解できるように設計されています。

従来のシステムでは、「BEC.SentimentCM_BEC.SpoofedSender」のような専門的なルール名だけが表示され、SOCアナリストは検出ロジックやトリガーとなった具体的な要因（感情分析モデルの出力、ヘッダーの異常、送信者評価データなど）を把握するのが困難でした。これにより、調査に時間がかかったり、誤って悪意のあるメールを解放するリスクが生じていました。

この課題に対し、Cloudyは自然言語処理を用いて検出ロジックを明確な説明に変換します。しかし、初期段階ではLLMの幻覚（ハルシネーション）問題が発生し、悪意のあるメッセージを「クリーン」と誤認する危険性がありました。Cloudflareはこの問題を解決するため、RAG（Retrieval-Augmented Generation）システムを導入し、Cloudyが社の検出データコーパスからのみ情報を取得するように制限しました。さらに、「Churchmouse」のような社内モデル名に適切な文脈情報を提供することで、LLMが誤った解釈をするのを防ぎました。

この取り組みは、AIが生成する情報の信頼性を確保するための具体的な技術的アプローチ（RAGとコンテキスト付与）を示しており、WebアプリケーションエンジニアがAIを活用したシステムを構築する際に直面する「ハルシネーション対策」の重要性を再認識させます。複雑なセキュリティインシデントの迅速なトリアージを可能にし、開発者がより安全なシステム設計と運用に集中できる環境を間接的にサポートする点で、その意義は大きいでしょう。