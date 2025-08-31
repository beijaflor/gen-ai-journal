## DB設計レビューの負荷を7割削減 ── Slack × Bedrockで実現した自動化の仕組み

https://techblog.zozo.com/entry/db-design-review-bot

ZOZOはSlackとAWS Bedrockを活用し、DB設計レビューを自動化することで、レビュー工数を7割削減し、開発ガイドライン遵守と効率を向上させたと詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[DB設計レビュー自動化, AWS Bedrock, LLM活用事例, 開発ワークフロー改善, コスト最適化]]

ZOZOは長年の課題であったDB設計レビューの負荷軽減のため、SlackとAWS Bedrockを活用した自動レビューBotを導入した事例を詳述しています。これまで手作業で行われていたレビューは、開発者間のガイドライン遵守度合いのばらつきや定型的な確認作業が「トイル化」しており、DBREの大きな負担となっていました。

この解決策として、既存のConfluenceとSlackを活用したレビューフローにBotを組み込む方式を採用。技術選定では、Slackとの連携にSlack Bolt for Pythonを、Confluence Server版とCloud版双方に対応するためAtlassian Python APIを用いたREST API直接利用を選択。LLMには、レビュー精度が高く利用頻度も考慮してAnthropic Claude 3.5 Sonnetを採用しました。

特に注目すべきは、Botの回答精度向上に必要な開発ガイドラインを、Bedrockのナレッジベース機能ではなくプロンプトに直接埋め込むシンプルなアプローチを取った点です。これは、ナレッジベースが高価なベクトルデータベース（Amazon OpenSearch Service）を裏側で使用するため、費用対効果が見合わないと判断したためです。また、将来的なモデル変更に柔軟に対応できるようBedrock Converse APIを利用し、HTML形式の設計情報をLLMでパースしてJSON化するなど、細部にわたる工夫が光ります。

このBot導入により、レビュー時の指摘件数が約7割削減され、ガイドライン遵守の徹底（スペルミス検出など）とDBREの運用負荷大幅軽減を実現。運用コストも月額約7.62ドルと極めて低く抑えられました。本事例は、LLMを既存のワークフローに賢く組み込み、具体的な課題を低コストで解決する実践的なアプローチとして、ウェブアプリケーションエンジニアにとって大きな示唆を与えます。同様の自動化は、コードレビューなど他の開発プロセスにも応用可能であり、今後のLLM活用における運用改善の好例と言えるでしょう。