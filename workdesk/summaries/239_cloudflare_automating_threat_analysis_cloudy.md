## Automating threat analysis and response with Cloudy

https://blog.cloudflare.com/automating-threat-analysis-and-response-with-cloudy/

Cloudflareは、AIエージェント「Cloudy」をセキュリティ分析機能とCloudforce One脅威イベントプラットフォームに統合し、会話型インターフェースを通じて脅威分析と対応を自動化・高速化します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 79/100 | **Annex Potential**: 72/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, セキュリティオペレーション, 脅威インテリジェンス, 会話型UI, Workers AI]]

Cloudflareは、AIエージェント「Cloudy」を大幅に強化し、セキュリティ分析機能とCloudforce One脅威イベントプラットフォームに統合、さらに会話型インターフェースを導入しました。これにより、セキュリティ運用のパラドックス（データ増による分析困難）を解決し、脅威分析と対応の自動化を推進します。

Webアプリケーションエンジニアにとって重要な点は、トラフィック異常発生時に、これまでの複雑なダッシュボード操作やログフィルタリングではなく、自然言語で「ログインエンドポイントに絞って」「トップ5のIPアドレスは何か」「悪性IPか」といった質問をするだけで、数分で根本原因分析（RCA）と緩和策の特定が可能になることです。これは、サービスダウンタイムの最小化やセキュリティ侵害リスクの低減に直結します。

さらに、CloudyはCloudflareのグローバルネットワークで観測されるAPT活動、DDoS攻撃、WAFエクスプロイト、サイバー犯罪といった膨大な脅威データセット（Cloudforce One Threat Events）と連携し、特定の業界を狙う攻撃者の動向や最新のIoC（侵害指標）をリアルタイムで提供します。これにより、Webアプリケーションエンジニアは、自身のアプリケーションが直面しうる具体的な脅威に対し、MITRE ATT&CKフレームワークに基づいた高度なインテリジェンスを活用し、先手を打った防御策を講じることが可能になります。

この進化は、CloudflareのWorkers AI上のAgents SDKを活用して実現されており、顧客データを使用しない責任あるAI開発アプローチも示しています。複雑なセキュリティ運用を簡素化し、より迅速かつ効果的なWebアプリケーション保護を実現するCloudyは、開発者にとって強力な味方となるでしょう。将来的にはWAFルールのデバッグ支援なども予定されています。