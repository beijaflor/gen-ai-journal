## Fly.ioにおける「Sprites」の設計と実装：高速な使い捨てコンピュータの裏側

https://simonwillison.net/2026/Jan/15/the-design-implementation-of-sprites/

**Original Title**: The Design & Implementation of Sprites

Fly.ioの新機能「Sprites」の背後にある、S3バックエンドとSQLiteメタデータを利用した超高速なサンドボックス環境のアーキテクチャを詳細に解説する。

**Content Type**: Technical Reference 🛠️ Technical
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Fly.io, Sprites, Cloud Architecture, SQLite, Litestream]]

Simon Willison氏が、Fly.ioのThomas Ptacek氏による新機能「Sprites」の内部実装に関する技術解説を紹介しています。Spritesは「ボールペンのように使い捨て可能なコンピュータ（ball-point disposable computers）」と定義されており、開発者向けサンドボックスやAPI実行環境として、必要な時に1〜2秒で即座に提供されることを目指したサービスです。

従来のFly Machinesはプロビジョニングに最大1分程度かかるという課題がありましたが、Spritesは「ウォームプール」方式でこれを解決しています。全ての物理ワーカーが次に起動すべき標準コンテナを事前に把握しており、各リージョンで未使用の「空のマシン」を待機させておくことで、新規作成時の重い処理を完全に排除しています。

特筆すべきは、そのストレージスタックの設計です。著者は、信頼性の低いローカルストレージを避け、S3互換のオブジェクトストレージをバックエンドの主役に据えることで「血圧が下がるほど」の安心感を得ていると述べています。実装にはJuiceFSのモデルを参考に、ストレージをデータ（チャンク）とメタデータ（マップ）に分離する手法を採用しています。

1. **データチャンク**: 信頼性の高いS3互換オブジェクトストレージに保存。NVMeは単なるリードスルーキャッシュとして機能。
2. **メタデータ**: 高速なローカルストレージ上のSQLiteで管理。
3. **耐久性の確保**: Litestreamを使用して、このSQLiteメタデータをオブジェクトストレージにリアルタイムで複製。

この構成により、ローカルディスクの状態に依存しない「ステートレスなインフラ」でありながら、300msという驚異的な速さでのチェックポイント作成とリストアが可能になっています。Webアプリケーションエンジニアにとって、このアーキテクチャは「高い信頼性」と「使い捨て可能な俊敏性」を両立させるための、モダンなクラウドネイティブ設計の極めて具体的なリファレンスと言えるでしょう。著者は、何にも依存しないローカルストレージの設計こそが、Spritesの高速性と信頼性の鍵であると強調しています。