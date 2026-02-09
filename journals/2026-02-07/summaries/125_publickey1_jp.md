## Claude CodeやGemini CLIなどのコーディングエージェントを安全に使えるMicroVMベースの分離環境「Docker Sandbox」。WindowsとMacに対応

https://www.publickey1.jp/blog/26/dockerclaude_codegemini_climicroivmdocker_snadboxwindowsmac.html

**Docker Sandbox**を使用して、**Claude Code**や**Gemini CLI**などのコーディングエージェントがホスト環境を破壊するリスクを排除した安全な実行環境を構築する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Docker Sandbox, コーディングエージェント, MicroVM, セキュリティ, Claude Code]]

Dockerは、**Claude Code**や**Gemini CLI**、**Copilot CLI**といったコーディングエージェントを安全に実行するための分離環境「**Docker Sandbox**」のWindowsおよびMac版を発表しました。本ツールは、エージェントが生成したコードの実行や環境設定の変更が、ホストマシンのファイルを削除したりシステムを破壊したりするリスクを排除するため、**MicroVM**ベースの強力な隔離環境を提供します。

主な特徴として、エージェントによるパッケージのインストール、テスト実行、さらには環境内でのDockerコマンドの実行を、ホストから完全に分離された状態で完結させることが可能です。また、許可/禁止リストを用いたネットワークアクセス制御機能も備えています。現時点では実験的プレビュー版の位置づけですが、今後は**MCP (Model Context Protocol)** ゲートウェイのサポートやLinux対応、ホスト上のサービスへアクセスするためのポート公開機能などの追加が予定されています。

ローカル環境でのエージェントの自律動作に対して、セキュリティやシステムの安定性の観点から不安を感じている開発者にとって、環境破壊を恐れずにツールの能力を最大限に引き出すための極めて実用的なソリューションとなるでしょう。