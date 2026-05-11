## LLM時代の「コードを書かない」開発：APIとCLIを合成する設計手法

https://walters.app/blog/composing-apis-clis

**Original Title**: The best code is no code: composing APIs and CLIs in the era of LLMs

既存の**CLI**と**OpenAPI**仕様を「合成」し、LLMが直接シェルコマンドを実行する設計によって、カスタムコードの削減とトークン効率の向上を実現する手法を提案する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 78/100 | **Overall**: 84/100

**Topics**: [[LLM Agents, CLI Composition, OpenAPI, OAuth2.0, Developer Experience]]

LLMエージェントのためのツール実装において、独自の**MCP**（Model Context Protocol）サーバーやカスタムコードを構築する代わりに、既存の**CLI**と**OpenAPI**仕様をシェル上で「合成」するアプローチを解説している。LLMはテキスト操作に長けているため、個別のAPIコールを定義するよりも、Unixシェルのコマンドパイプラインを利用させる方がトークン効率や再利用性の面で優位であると著者は主張する。

具体的な実装技術として、OpenAPI仕様をプログラムとして解釈し実行する**Restish**や、標準的なOAuth 2.0認証をCLIで完結させる**oauth2c**を紹介。さらに、macOSの**Keychain**でバイオメトリクス保護を有効にする高度なテクニック（`security -T ""`）や、APIが公開されていないサービスを**HAR**ファイルからリバースエンジニアリングしてエージェント用ツール化する手法まで踏み込んでいる。

単なる「AIツールの作り方」に留まらず、保守コストを下げ、人間とマシンの両方が使いやすいインターフェースを維持するための実践的な設計思想を提示している。エージェントの外部ツール連携を検討している開発者や、認証周りの自動化に悩むエンジニアにとって非常に示唆に富む内容だ。