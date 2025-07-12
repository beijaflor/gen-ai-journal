## Gemini CLI を Google Workspace アカウントで使う

https://qiita.com/revsystem/items/34e65c59f05f97357d71

この記事は、Gemini CLIをGoogle Workspaceアカウントで利用する方法について解説しています。

[[Gemini CLI, Google Workspace, 認証, 環境変数, API有効化]]

2025年6月26日にリリースされたGemini CLIは、GoogleアカウントでのログインまたはAPIキーの指定で利用可能です。Google Workspaceアカウントでは直接サポートされていない旨のメッセージが表示されることがありますが、「その他の方法でログイン」からGoogle Workspaceアカウントで認証できます。

手順は以下の通りです。
*   **Gemini CLIのインストール**: `npx`または`npm`を使用。
*   **Google Workspaceアカウントでの認証**: `gemini`コマンド実行後、ChromeブラウザでGoogleアカウントにログイン。Google Workspaceアカウントで認証後も「Google Workspaceアカウントではありません」と表示される場合があるが、「その他...」メニューから「Google Workspaceでログイン」を選択。
*   **`GOOGLE_CLOUD_PROJECT`環境変数の設定**: 「GOOGLE_CLOUD_PROJECT環境変数が見つかりません」というメッセージが表示された場合、`.env`ファイルまたは`export`コマンドでこの変数を設定する必要がある。プロジェクトIDはGoogle Cloudコンソールで確認可能。
*   **Gemini for Google Cloud APIの有効化**: 環境変数を設定し再認証後、Gemini CLIを使用しようとしてAPIエラーが発生した場合（例：「Hello」と入力）、プロジェクトでGemini for Google Cloud APIが無効になっていることを意味する。エラーメッセージに表示されるURLにアクセスし、APIを有効にする必要がある。

記事では、`~/.gemini/settings.json`でのMCPサーバー（例：AWS Documentation MCPサーバー）の設定についても簡単に触れており、Gemini CLIによる利用統計情報の収集と、`settings.json`で`usageStatisticsEnabled`を`false`に設定することでオプトアウトできることも説明していま���。

---

**編集者ノート**: Gemini CLIがGoogle Workspaceアカウントでも利用可能であるという情報は、企業や組織でのAIエージェント導入を検討している開発者にとって非常に重要です。特に、環境変数の設定やAPIの有効化といった具体的な手順が示されている点は、導入障壁を下げる上で役立ちます。利用統計のオプトアウト機能も、プライバシーを重視するユーザーにとっては安心材料となるでしょう。今後、Gemini CLIのようなツールが、より多様な環境でシームレスに利用できるようになることで、AIを活用した開発の普及がさらに加速すると考えられます。