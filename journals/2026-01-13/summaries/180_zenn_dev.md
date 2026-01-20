## opencodeを使ってみよう（Anthropic と OpenAIのサブスク対応）

https://zenn.dev/livetoon/articles/get-start-opencode

多様なLLMプロバイダーや既存のサブスクリプションを統合利用できるOSSコーディングエージェント「opencode」の導入方法と、その実用的な利点を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[opencode, コーディングエージェント, Claude Code, LSP, MCP]]

株式会社Livetoonの開発マネージャーである著者は、OSSとして開発されているコーディングエージェント「opencode」の有用性を紹介している。本作はClaude CodeやOpenAIのCodexと同様の機能を持ちながら、特定のモデルに縛られない柔軟性が最大の特徴である。著者は、AnthropicのBedrockやVertex AI、さらにはOllamaやLM StudioといったローカルLLMまで幅広く接続できる点に加え、開発者自身が運営する「opencode Zen」を通じて複数の最新モデルを横断的に利用できる拡張性を高く評価している。

記事の中心となるのは、Webエンジニアにとって切実な「APIコスト」と「既存資産の活用」に関する具体的なソリューションである。著者は、通常はブラウザや公式アプリでしか利用できない「Claude Pro」や「ChatGPT Plus」のサブスクリプション枠を、CLIエージェントから利用するためのセットアップ手順を詳説している。特にOpenAIに関しては、公式がAPIキー認証のみをサポートしている現状に対し、外部プラグインを用いてOAuth経由でChatGPT Plusを接続するという実践的な回避策を提示しており、コスト効率を重視するエンジニアにとって極めて即効性の高い情報となっている。

機能面において著者が特筆しているのは、競合ツールに対する技術的優位性だ。標準的なファイル操作やWeb Fetch機能、MCP（Model Context Protocol）のサポートに加え、opencodeはLSP（Language Server Protocol）サーバー機能を内蔵している。これにより、エージェントがコードのセマンティクスをより深く理解した上での修正提案が可能になると述べている。また、JavaScriptやTypeScriptを用いたカスタムツールの定義や、Agent Client Protocol（ACP）のサポートによるIDE（JetBrains等）との連携、SDKを介した独自フロントエンド開発の可能性など、単なるチャットUIを超えた「開発プラットフォーム」としての側面を強調している。

著者は、数日間の試用を経て、opencodeがソフトウェアとしての品質と実用性を十分に備えていると結論付けている。公式ツール以外の「第3の選択肢」として、特に複数のLLMを使い分けたい、あるいはローカルLLMをワークフローに組み込みたいエンジニアにとって、opencodeは強力なツールになると主張している。