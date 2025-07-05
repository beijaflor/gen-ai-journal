## [Gemini CLI を Google Workspace アカウントで使う](https://qiita.com/revsystem/items/34e65c59f05f97357d71?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

**Google Workspaceユーザー必見！Gemini CLIの認証方法を解説**

2025年6月26日にリリースされたGemini CLIは、公式にはGoogle Workspaceアカウントをサポートしていないと表示されますが、実際にはいくつかの設定を行うことで利用可能です。この記事では、その具体的な手順を解説します。

主な手順は、環境変数 `GOOGLE_CLOUD_PROJECT` にGoogle CloudのプロジェクトIDを設定し、そのプロジェクトで「Gemini for Google Cloud API」を有効にすることです。これにより、Google WorkspaceアカウントでもGemini CLIの認証を通過し、プロンプト入力が可能になります。

記事では、`npx`や`npm`を使ったGemini CLIのインストール方法から、認証プロセスで表示されるメッセージ、`.env`ファイルや`export`コマンドでの環境変数の設定方法、Google CloudコンソールでのAPI有効化の手順まで、スクリーンショット付きで詳しく説明されています。

さらに、AWS DocumentationなどのMCP（Multi-purpose Cooperative Processing）サーバーを設定する方法や、使用状況の統計情報収集を無効にするオプトアウト設定についても触れられており、Gemini CLIをより活用するための情報が網羅されています。独自ドメインのメールアドレスでGemini CLIを使いたいと考えていたGoogle Workspaceユーザーにとって、非常に役立つガイドです。