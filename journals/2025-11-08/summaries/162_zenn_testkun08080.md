## 日本株3700社以上を分析。yfinance x「わが投資術」株式スクリーニングアプリを作った話（バイブコーディング）

https://zenn.dev/testkun08080/articles/python-yfinance-4c4331412bc50f

筆者は、日本株全銘柄の財務データを自動収集し、高速スクリーニングを可能にするWebアプリケーション「yfinance-jp-screener」を開発し、その技術的実装と開発プロセスを詳細に解説します。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:3/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 76/100

**Topics**: [[Python, yfinance, React, GitHub Actions, Docker, 株式スクリーニング]]

筆者は、手動での株価スクリーニングの煩雑さを解消するため、Pythonの`yfinance`とReactを用いた日本株スクリーニングWebアプリ「yfinance-jp-screener」を開発しました。このアプリは、JPX公式データから約3,795銘柄の株式情報を自動取得し、「わが投資術」に準拠したPBR、ROE、時価総額などの財務指標で高速にフィルタリング・可視化します。

システムのアーキテクチャは、Pythonでデータ収集・処理を行い、その結果をCSVファイルとして出力。React製のフロントエンドがCSVを読み込み、ユーザーインターフェースを提供します。データ収集の自動化にはGitHub Actions、デプロイにはDocker Composeを活用しています。

特に注目すべきは、`yfinance`のAPIレート制限を回避するための工夫です。約3,795社ものデータ取得を一度に行うと制限に抵触するため、GitHub Actionsのワークフローを4段階に分割し、それぞれ約1,000社ずつデータを逐次取得・結合する仕組みを構築しました。これにより、安定したデータ自動更新を実現しています。
フロントエンドはReact 19、TypeScript、Vite、Tailwind CSSで構築され、CSVファイルのドラッグ＆ドロップアップロード、PapaParseによる効率的なデータ解析、そして`useMemo`を活用した20項目以上にわたる多機能フィルタリング機能を実装。数値データの単位変換や日本語ロケール対応など、実用的な配慮がされています。
デプロイはDockerとDocker Composeを使用し、PythonバックエンドサービスとReactフロントエンドサービスを容易に連携・起動できるようになっています。初回起動時は全データ収集に約4時間かかるものの、その後の運用を簡素化します。

このプロジェクトは、既存の投資手法を自動化する具体的なソリューションを示しており、Webアプリケーション開発、データ収集の自動化、クラウド環境でのCI/CD構築に関心のあるエンジニアにとって、実践的な学びを提供するでしょう。開発プロセスでは、AIを活用した「バイブコーディング」で大まかな流れをAIとすり合わせ、Claudeでコードを生成・調整したことが明かされています。著者は、今後の展望として`yfinance`の代替としてSakanaAIの`edinet2dataset`の利用も検討しています。