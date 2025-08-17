## 新Codex CLIの使い方

https://blog.lai.so/codex-rs-intro/

OpenAIがChatGPT Plus/Proユーザー向けに無料で提供を開始したRust版Codex CLIの導入と活用法を詳述し、開発者がその機能を最大限に引き出すための具体的なヒントを提供します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Codex CLI, AIコーディングエージェント, Rust, CLIツール, ChatGPT連携]]

OpenAIのCodex CLIが、GPT-5の公開と同時にChatGPT Plus/Proサブスクリプションで追加料金なしに利用可能となり、API課金なしでAIコーディングエージェントを試せる大きな機会が生まれました。これは特に、費用対効果の高い開発ツールを探すWebアプリケーションエンジニアにとって重要な意味を持ちます。

Codex CLIは、TypeScriptからRustへ書き換えられ、より堅牢なツールとして進化しました。macOSやWindows（WSL2なしでも動作）に対応し、npmやHomeBrewで簡単に導入できます。ログインはChatGPT認証でスムーズに行えますが、`python3`コマンドのパス問題や、環境変数`OPENAI_API_KEY`より`~/.codex/auth.json`が優先される認証フローなど、注意すべき点がいくつかあります。これらを理解することは、意図しない課金や動作不良を避ける上で不可欠です。

さらに、記事は`Claude Code`ユーザー向けにコマンド対応表を提供し、`MCP`（Modular Capabilities Protocol）サーバー設定による外部ツール連携（Brave SearchやSerena）、モデル切り替えの注意点（ChatGPTトークンでは`gpt-5`固定、APIキーで他のモデルを指定可能）、エージェントの思考プロセス表示の制御（`thinking`表示のオンオフ）など、高度な活用術を解説しています。特に`thinking`を"high"に設定することで、コード生成の精度向上に繋がるという点は、より実践的な利用を目指すエンジニアにとって役立つ情報です。

このツールは、エージェント開発のリサーチプレビューへの参加や、公開されているソースコードを自身のプロジェクトの参考にする上で価値があります。現在の制限事項（使用量リセット、サンドボックスなど）を理解しつつ、積極的に活用することで、将来のAIを活用した開発ワークフローの可能性を探ることができます。