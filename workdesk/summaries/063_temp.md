## AWS re:Invent2025 Keynote現地速報

https://tech.dentsusoken.com/entry/2025/12/03/aws_reinvent_2025_keynote

AWS re:Invent 2025のキーノートでは、その大半がAI関連の新サービス・機能の発表に割かれ、特にマルチモーダル対応のAmazon Nova 2 Omniや、AIエージェントの制御・評価機能、そしてコード生成からセキュリティ、DevOpsまでを自律的に支援するKiro関連ツール群が開発者にとって重要であることが示されました。

**Content Type**: News & Announcements
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 98/100 | **Annex Potential**: 98/100 | **Overall**: 72/100

**Topics**: [[AWS re:Invent, Generative AI, AI Agent Development, Multimodal AI, AI for DevSecOps]]

電通総研の宮原氏がAWS re:Invent 2025キーノートの現地速報として、発表された新サービス・機能の中からエンジニアとして特に注目すべきAI関連のアップデートをまとめています。今回のキーノートは2時間の約9割がAIに関する内容で占められ、AWSがAI開発と発表を最優先事項としていることが明確に示されました。

特に以下のサービスが発表されました。

*   **Amazon Nova 2**: AWSの基盤モデルAmazon Novaの進化版で、コストと精度のバランスを重視。Lite、Pro、Sonicといったモデルに加え、テキスト、画像、動画、音声を入力し、画像・テキストを出力可能な業界初のマルチモーダルモデル「Amazon Nova 2 Omni」が登場し、即時要約などの事例が紹介されました。
*   **Amazon Nova Forge**: 企業独自のカスタムモデル開発を支援するサービスで、RAGとは異なるアプローチでドメイン特化型課題の解決を目指します。
*   **Policy in AgentCore**: Amazon Bedrock AgentCore上のAIエージェントのツール（主にAWS Lambda）実行をコンプライアンス要件に基づいて制御する機能で、Cedar形式でポリシーを記述します。
*   **AgentCore Evaluations**: Amazon Bedrock AgentCoreで動作するAIエージェントの品質評価を、LLM as a judgeを利用して実施する機能です。
*   **Kiro autonomous agent**: 仕様駆動開発を促進し生産性向上を目指すもので、長時間のコード生成や並列実行に特化しています。
*   **AWS Security Agent**: Kiroに関連し、生成されたコードのセキュリティチェックをAIが実行する機能です。
*   **AWS DevOps Agent**: Kiroに関連し、本番環境でのインシデント発生時にCloudWatchなどと連携し、エラーの原因特定と修正を自律的に行い、オンコール対応の負荷軽減が期待されます。

キーノートのわずかな時間で、データベース利用のコミットによりコストメリットが得られる「Database Saving Plan」も発表されました。

筆者は、Bedrock、Bedrock AgentCore、Kiroといった個人的に興味のあるサービスの発表が多く、非常に刺激的なキーノートであったと述べています。そして、フロントエンド、バックエンド、インフラ・SREといったロールに関わらず、我々エンジニアはAIをさらに活用していく必要があると改めて感じた、と締めくくっています。