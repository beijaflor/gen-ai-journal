## Microsoft、クロスフレームワークのWindowsアプリ開発を一元化するCLI「winapp」をパブリックプレビュー

https://blogs.windows.com/windowsdeveloper/2026/01/22/announcing-winapp-the-windows-app-development-cli/

**Original Title**: Announcing winapp, the Windows App Development CLI

Visual StudioやMSBuildを使わないElectron/CMake/.NET/Rust/Dart開発者向けに、SDKセットアップ、マニフェスト・証明書生成、MSIXパッケージング、デバッグ用Package Identity注入までを単一のCLIに集約したオープンソースツール。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 78/100 | **Overall**: 79/100

**Topics**: [[winapp CLI, Windows App SDK, MSIX packaging, Package Identity, Electron]]

Microsoftが、Windowsアプリ開発の煩雑なツールチェーン管理を統合するオープンソースCLI「**winapp**」のパブリックプレビューを公開した。複数のSDK、`appxmanifest.xml`、証明書、MSIXパッケージングといった従来の「設定との戦い」を一本化する設計で、Visual StudioやMSBuildを介さない**Electron/C++ (CMake)/.NET/Rust/Dart**といったクロスプラットフォーム開発者を主な対象としている。`winapp init` がプロジェクトルートでSDKダウンロード、C++/WinRTプロジェクション生成、マニフェスト・アセット作成、開発用証明書発行までをワンコマンドで完了させ、CI/CD向けにはGitHub ActionsとAzure DevOps向けアクションも提供される。

特に注目すべきは**Package Identity**周りの改善だ。**Windows AI API**、Security、Notifications、そして**MCPホスト**といった近年のAPI群はパッケージ化済みアプリでないと動作しないものが多く、従来は1機能のテストのためにフルパッケージとインストールが必要だった。`winapp create-debug-identity my-app.exe` で実行ファイルに直接Identityを付与でき、内部開発ループを維持したまま検証できる。Electron向けには npm パッケージ化され、`winapp node add-electron-debug-identity` で動作中のElectronプロセスへIdentityを注入、`npm start` のままWindows AI APIをテスト可能にする。さらに `@microsoft/winapp-windows-ai` パッケージ経由でNode.jsから**LanguageModel**などのWindows AI APIを直接呼び出せる実験的projectionも提供され、Phi Silicaのような端末側AI機能をElectronアプリへ取り込みたい開発者の参入障壁を大きく下げる内容となっている。WinGet (`winget install microsoft.winappcli`) または npm から導入可能。
