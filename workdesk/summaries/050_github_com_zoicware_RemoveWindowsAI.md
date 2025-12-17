## Windows 11からCopilot、RecallなどのAI機能を強制的に削除

https://github.com/zoicware/RemoveWindowsAI

**Original Title**: Force Remove Copilot, Recall and More in Windows 11

Windows 11に搭載されたCopilotやRecallなどのAI機能を包括的に削除し、プライバシーとパフォーマンスを向上させるPowerShellスクリプトが公開されました。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[Windows 11, Copilot, プライバシー, システムツール, 脱AI]]

Windows 11の最新および将来のビルドでAI機能が増加することに対応し、ユーザーエクスペリエンス、プライバシー、セキュリティを向上させることを目的としたPowerShellスクリプト「RemoveWindowsAI」が公開されました。著者は、これらのAI機能がユーザーにとって不要であり、プライバシーやセキュリティ上の懸念を引き起こすため、システムから徹底的に削除する必要があると主張しています。

このスクリプトは、Windows 11に統合された様々なAIコンポーネントを削除または無効化するための包括的な機能を提供します。主な機能は以下の通りです。
*   **CopilotおよびRecallの無効化と削除**: レジストリキー、関連ポリシー、Appxパッケージ、およびスケジュールされたタスクを強制的に削除します。
*   **入力インサイトとタイピングデータ収集の停止**: ユーザーのプライバシーを保護するため、これらのデータ収集機能を無効にします。
*   **EdgeのCopilot、PaintのImage Creator/AI機能、メモ帳のRewrite AI機能の削除**。
*   **AI Fabricサービス、AIアクション、AI音声エフェクト、設定検索のAI機能の無効化**。
*   **AIパッケージの再インストール防止**: カスタムのWindows Updateパッケージをインストールし、AIパッケージがCBS (Component-Based Servicing) ストアに再インストールされるのを防ぎます。
*   **隠されたAIパッケージとファイルの削除**: システムに隠されたAI関連のAppxパッケージ（非削除可能なものを含む）、CBSパッケージ、およびその他のインストールファイルやレジストリキーを一掃します。

スクリプトはWindows PowerShell (5.1) を管理者権限で実行することで利用でき、UI付きの実行モードや、特定のオプションを選択できる非対話型モードも提供されています。システムへの広範な変更を伴うため、一部のサードパーティ製アンチウイルスソフトウェアが誤って悪意のあるものとして検出する可能性があると警告されており、テスト環境での使用が推奨されています。著者は、MicrosoftがAI機能を追加し続ける限り、スクリプトも最新の安定版Windows 11ビルドに対応できるよう更新を続けると述べており、ユーザーが未検出のAI機能を見つけた際には情報提供を呼びかけています。このツールは、AI機能の強制的な統合に不満を持つ開発者やエンドユーザーに対し、システムに対するより深い制御とプライバシー保護の手段を提供します。