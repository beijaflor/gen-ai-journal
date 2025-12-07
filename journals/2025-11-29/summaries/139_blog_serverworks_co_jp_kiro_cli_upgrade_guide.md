## Kiro CLI登場 - Amazon Q Developer CLIからの移行方法と変更点まとめ

https://blog.serverworks.co.jp/kiro-cli-upgrade-guide

Kiro CLIは、Amazon Q Developer CLIからの移行を容易にし、AWS請求との統合、セキュリティ強化、開発者のニーズに合わせた柔軟なサブスクリプションプランを提供することで、エンタープライズでの生成AI活用を促進します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Kiro CLI, Amazon Q Developer CLI, AWS, 生成AI, 開発者ワークフロー]]

サーバーワークスの記事は、Kiro CLIの一般公開に伴い、Amazon Q Developer CLIからの移行方法と主要な変更点を解説しています。2025年11月18日に一般公開されたKiro CLIは、Amazon Q Developer CLIの後継として提供され、既存ユーザーは`q update`コマンドで簡単にアップグレードできます。自動更新が有効な場合、2025年11月24日には自動的にKiro CLIへ更新される予定です。

この移行の最も重要な利点の一つは、Kiro独自のサブスクリプションプランがAWSの請求と統合されたことです。これにより、これまで個別課金が障壁となっていた企業が、AWS利用料金とまとめて支払うことが可能となり、導入と運用のハードルが大幅に下がると著者は指摘しています。Kiroのサブスクリプションは、開発者のニーズに合わせた3つの価格ティアを提供し、Overage（超過使用）にも対応、管理者によるグループ単位または個別ユーザー単位でのアップグレードが柔軟に行えます。

技術的な変更点としては、CLIのエントリーポイントが`kiro-cli`となり、認証方式にGitHubやGmailなどが追加されました。設定ファイルのパスは`.aws/amazonq`から`.kiro`へと変更されますが、既存の`q`や`q chat`コマンド、プロジェクト内の`.amazonq`フォルダ設定は引き続き後方互換性を持って動作します。また、`fs_read`から`read`など、ツール権限の名称も変更されています。

セキュリティ面では、Kiro Pro、Pro+、PowerユーザーにはQ Developer Proユーザーと同様にアウトプット保障が提供され、AWS IAM Identity Center経由での利用時にはコンテンツがモデルトレーニングに使用されないデータ利用ポリシーが適用されます。テレメトリーも同様に収集されません。これらの変更は、開発者が安心して生成AIをエンタープライズ環境で利用するための基盤を強化し、より多くの企業が生成AIの活用へと踏み出すきっかけとなるでしょう。