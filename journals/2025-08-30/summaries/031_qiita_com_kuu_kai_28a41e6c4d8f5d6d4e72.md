## Windows powershell に Claude Code を入れる。

https://qiita.com/kuu_kai/items/28a41e6c4d8f5d6d4e72

Windows PowerShellでClaude Code CLIが「認識されません」となる問題の根本原因を解明し、Git Bashパス設定とPATH環境変数の追加による確実な解決手順を提示します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Claude Code CLI, PowerShell, 環境変数, Git Bash, ツールインストール]]

本記事は、Windows PowerShell環境でAnthropic社のClaude Code CLIを導入する際に遭遇しやすい「claude: 用語 'claude' は…認識されません」というエラーの具体的な解決策を提示します。Webアプリケーションエンジニアにとって、AIコーディングアシスタントのCLIツールは開発効率を大きく左右しますが、WindowsではGit Bashの依存性や実行ファイルのパス設定が障害となることが少なくありません。

記事が解明する主要な原因は二つです。一つは、Claude CodeのWindowsネイティブ版がGit Bashの`bash.exe`を必要とし、そのパスを`CLAUDE_CODE_GIT_BASH_PATH`環境変数で明示する必要がある点。もう一つは、ネイティブインストーラが配置する`~\.local\bin`ディレクトリがデフォルトで`PATH`環境変数に含まれていないため、`claude.exe`が見つからないという問題です。

この問題の解決策として、記事は以下の手順を推奨します。まずGit for Windowsがインストールされていることを確認し、`bash.exe`のパスを環境変数`CLAUDE_CODE_GIT_BASH_PATH`に設定します。次に、公式ネイティブインストーラを実行して`claude.exe`をインストールし、その配置先である`~\.local\bin`をユーザー`PATH`に追加します。最後にPowerShellを再起動することで、`claude`コマンドが正常に認識され、利用可能になります。

なぜこれが重要かと言えば、これによりWindows環境のエンジニアは、AIコーディングアシスタントをスムーズに導入し、日々の開発ワークフローに統合できるようになるからです。特に、クロスプラットフォームを前提としたAIツールがWindows特有の環境課題に直面するケースは多く、本記事は具体的なシステム設定を通じてツールの実用性を高める上で非常に価値のある情報を提供しています。`npm`ルートでのインストール時のPowerShell `ExecutionPolicy`問題にも触れつつ、ネイティブインストーラが最も確実な「勝ち筋」であると強調しており、開発者の手間を省く実践的な知見が満載です。