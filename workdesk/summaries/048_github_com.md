## lnai：AIツールの設定管理を一本化するCLIツール

https://github.com/KrystianJonca/lnai

**Original Title**: Unified AI configuration management CLI

複数のAIコーディングツールの設定を単一のソースで管理し、各ツールのネイティブ形式へ自動同期するCLIツール。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[AIコーディングツール, CLI, 設定管理, MCP, 開発生産性]]

`lnai`は、**Claude Code**、**Cursor**、**GitHub Copilot**、**Windsurf**といった複数のAIコーディングツール間で散逸しがちな設定ファイルを一元管理するためのオープンソースCLIツールです。プロジェクト固有の開発ルール、**MCP（Model Context Protocol）**サーバーの設定、各種パーミッションなどを`.ai/`ディレクトリ内の単一のソース（One Source of Truth）で定義し、`lnai sync`コマンドを実行することで各ツールが読み取れる固有のネイティブ形式へ即座に同期できます。

技術的な特徴として、各ツールの設定ファイル構造への自動変換に加え、設定の**バリデーション**機能や、元ファイルが削除された際の不要な生成ファイルの自動クリーンアップ機能を備えています。これにより、**Cursor**用の`.cursorrules`や**GitHub Copilot**用の`copilot-instructions.md`、**Gemini CLI**の設定などを個別に手動更新する手間を排除します。

複数のAIアシスタントをプロジェクトの状況に応じて使い分けている開発者や、チームで共通のAI指示書を効率的に配布・管理したいプラットフォームエンジニアに最適です。AIツールの乱立による設定の断片化を解決し、開発ワークフローのポータビリティを向上させます。