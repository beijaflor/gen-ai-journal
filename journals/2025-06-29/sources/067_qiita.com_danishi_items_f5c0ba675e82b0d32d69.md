## [Claude CodeをGoogle Cloud Shellから使ってみる](https://qiita.com/danishi/items/f5c0ba675e82b0d32d69)

**Google Cloud ShellでClaude Codeを動かし、インフラ操作を自動化！**

この記事では、AnthropicのAIコーディングアシスタント「Claude Code」をGoogle Cloud Shell上でセットアップし、実際にGoogle Cloudリソースを操作する手順を解説します。Node.jsが動作するUnix互換OSであればCLIとして実行できるClaude Codeの特性を活かし、Cloud Shellという手軽な環境で試す方法を紹介。Vertex AIをモデルプロバイダーとして設定し、`gcloud`コマンドを通じてCloud Storageバケットの作成やファイルのアップロードといった操作を自然言語で指示し、自動実行させる様子がデモされています。Cloud Shellエディタと連携したコーディング支援にも利用可能で、オペレーション自動化の可能性を感じさせる内容です。破壊的なコマンドが実行されるリスクもあるため、IAMの権限管理の重要性も指摘されています。