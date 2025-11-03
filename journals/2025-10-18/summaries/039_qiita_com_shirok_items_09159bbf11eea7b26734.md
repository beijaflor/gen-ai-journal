## Oracle AI Database 26ai がリリースされたので作成してみてみた #oracle

https://qiita.com/shirok/items/09159bbf11eea7b26734

Oracleは、データ管理の中核にAIを統合した次世代データベース「Oracle AI Database 26ai」をリリースし、その主な機能とOCIでのプロビジョニング手順を詳述する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:2/5 | Practical:5/5 | Anti-Hype:2/5
**Main Journal**: 100/100 | **Annex Potential**: 87/100 | **Overall**: 68/100

**Topics**: [[Oracle AI Database, ベクター検索, OCI, エージェント型AI, データベース]]

Oracleは、AIをデータ管理の中核に組み込んだ長期サポートリリース「Oracle AI Database 26ai」をリリースした。本記事は、その概要とOCI上での作成手順について解説している。

この新データベースは、AIベクター検索、データベース管理のためのAI、データ開発のためのAI、アプリケーション開発のためのAI、アナリティクスのためのAIといったオラクルの「AI for Data」ビジョンを推進するもので、顧客は動的なエージェント型AIワークフローを実行し、プライベートデータベースデータと公開情報を組み合わせた高度な回答とアクションを提供できるようになる。

26aiはOracle Database 23aiの後継であり、2025年10月のリリースアップデートを適用するだけで23aiから26aiへシームレスに移行可能だ。特筆すべきは、AIベクトル検索などの高度なAI機能が追加料金なしで利用できる点である。

Oracle AI Database 26aiは、Oracle Cloud、主要なハイパースケールクラウド、プライベートクラウド、オンプレミスなど、データの保存場所を問わず利用でき、Apache Icebergオープンテーブル形式、Model Context Protocol（MCP）、業界をリードするLLM、人気のエージェント型AIフレームワーク、Open Neural Network Exchange（ONNX）埋め込みモデルなど、幅広い選択肢をサポートする。

主要機能には、Oracle Autonomous AI Lakehouse、統合ハイブリッドベクター検索、MCPサーバー・サポート、プライベートAIサービスコンテナ、Select AI Agent、APEX AIアプリケーションジェネレーターなどが含まれる。記事の後半では、OCIコンソールを使用してBase Database Serviceで26aiをプロビジョニングする具体的なステップが詳細に説明されており、データベース・ソフトウェア・イメージの選択から各種設定、DBシステムの作成まで、実運用に向けた手順が網羅されている。

このリリースは、ウェブアプリケーションエンジニアにとって、既存のOracleデータベース環境にAI機能を迅速に統合し、AI駆動型アプリケーションを開発するための具体的な道筋を提供する重要な一歩となるだろう。