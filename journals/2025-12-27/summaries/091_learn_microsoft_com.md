## Microsoft Agent Frameworkの概要：.NETとPython向け次世代AIエージェント開発キット

https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview

**Original Title**: Introduction to Microsoft Agent Framework

Semantic KernelとAutoGenの機能を統合し、複雑なマルチエージェント・オーケストレーションを可能にする次世代の開発フレームワークを提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[AI Agent, Microsoft Agent Framework, Multi-agent Orchestration, Semantic Kernel, AutoGen]]

マイクロソフトは、AIエージェント構築のための新たなオープンソース・デベロップメントキット「Microsoft Agent Framework」を公開した。これは、同社がこれまで展開してきた「Semantic Kernel」と「AutoGen」のプロジェクトから得られた知見と機能を統合した、次世代の統一基盤である。.NETおよびPythonをサポートし、エンタープライズ級の信頼性とマルチエージェントの柔軟性を両立させている。

本フレームワークの核心は、「AIエージェント」と「ワークフロー」という2つの主要機能にある。AIエージェントは、LLMを活用して意思決定やツール呼び出しを自律的に行うコンポーネントであり、Azure OpenAIなどの主要モデルや、MCP（Model Context Protocol）サーバーを介したツール統合に対応している。一方、ワークフローはグラフベースの構造を持ち、複数のエージェントや関数を連結して複雑な多段階タスクを実行する。型ベースのルーティングや状態管理（チェックポイント）、ヒューマン・イン・ザ・ループ（人間による介入）の仕組みを備えており、単一エージェントでは困難だった長期実行プロセスの明示的な制御を可能にしている。

筆者は、本フレームワークが必要な理由として、従来ツールの強みを一つに集約する必要性を強調している。具体的には、AutoGenのシンプルな抽象化能力と、Semantic Kernelのエンタープライズ機能（テレメトリ、型安全性、状態管理、フィルタリングなど）を融合させることで、開発者が実行パスを詳細に管理できる仕組みを導入した。これにより、自律的な試行錯誤が必要なシーンには「エージェント」を、構造化された予測可能なタスクには「ワークフロー」を使い分けるといった、より堅牢で実用的なAIアプリケーションの構築が可能になる。

Webアプリケーションエンジニアにとって特に注目すべきは、状態管理と拡張性の高さだ。エージェントスレッドによる状態保持、コンテキストプロバイダーによるメモリ管理、アクションを傍受するミドルウェアなど、実務で不可欠なビルディングブロックが揃っている。また、筆者は「関数で書けるタスクはエージェントを使わずに関数で書くべき」という、ハイプを排した現実的な設計指針も示しており、AIを過度に抽象化せず、コードベースの制御とAIの自律性を適切にバランスさせることを推奨している。現在はパブリックプレビュー段階だが、今後のMicrosoft系AIスタックの中核となることが確実視されており、AIエージェントの実装を検討する開発者にとって最優先でチェックすべきリファレンスと言える。