## OCIのノーコード・エージェントビルダー『Agent Factory』がリリース！触ってみた

https://qiita.com/yushibats/items/cb29c3208ac188dad5f1

Oracleが新たにリリースした、エンタープライズ向けノーコードAIエージェント構築プラットフォーム「Agent Factory」の概要と、OCI上での具体的なセットアップ・RAG実装手順を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 75/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Oracle Cloud Infrastructure, AIエージェント, RAG, ノーコード, Oracle Database]]

Oracleが提供を開始した「Oracle AI Database Private Agent Factory（通称：Agent Factory）」は、エンタープライズ品質のAIエージェントをノーコード・ローコードで構築・運用できるプラットフォームだ。著者は、LangGraphやcrewAIといったオープンソースの柔軟性を認めつつも、商用サポートやセキュリティ、基幹システム連携といった企業導入特有の課題を解決する手段として、本ツールの重要性を強調している。

本ツールの最大の特徴は、Oracle Databaseとの深い連携にある。Oracle AI Vector Searchをはじめとするデータベース機能をワークフロー内で直接活用でき、最新のDB機能もリリースと同時に利用可能だ。また、SSOやロール管理、ガードレール設定などのエンタープライズ向けガバナンス機能を備えつつ、OCI GenAI、OpenAI、Llamaといった多様なLLMを選択できる柔軟性も併せ持っている。

記事では、OCI Marketplaceを利用したセットアッププロセスを詳細に解説している。Autonomous Database (ADB) との接続、OCI Generative AIサービスの設定など、GUIベースのウィザードに従うだけで環境構築が完結する様子が示されている。さらに、実践的な例として「Knowledge Agent」を用いたRAGエージェントの作成手順を紹介しており、Webサイトをデータソースとして登録し、クローリングから回答生成までを迅速に実現できることを実証している。著者は、直感的なGUIによりRAGの立ち上げが極めて手軽であることを高く評価しており、企業内データに基づいた信頼性の高いエージェント開発を加速させる強力なツールであると結論付けている。