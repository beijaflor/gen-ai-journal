## Microsoft Agent Framework (C#) を見てみよう その1「雑感」とハローワールド

https://zenn.dev/microsoft/articles/agent-framework-001

Microsoftは、Semantic Kernelの課題を解消し、エージェント開発に特化した新フレームワーク「Agent Framework (C#)」を発表、LLM連携からマルチエージェントワークフローまで具体的なC#コードでその実践的活用法を詳解します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Microsoft Agent Framework, Semantic Kernel, .NET AI開発, マルチエージェントシステム, LLMツール連携]]

MicrosoftがSemantic Kernelの複雑さを解消し、エージェント開発に特化した新たなフレームワーク「Agent Framework (C#)」を発表しました。これまでSemantic KernelがLLMの急速な進化と互換性維持の間で多くの抽象化レイヤーを抱え込み、「無理なリフォームを重ねた建物」のようになっていた現状を打開するため、エージェント機能に特化して再設計されたものです。このフレームワークは、LLMの基本的なチャットやツール呼び出し機能を担う`Microsoft.Extensions.AI`を前提とし、その上にエージェントとしての機能を集約しています。

Webアプリケーションエンジニアにとって重要なのは、Semantic Kernelの進化の経緯と、なぜこの新フレームワークが必要とされたかを理解できる点です。記事では、`Microsoft.Extensions.AI`を用いてLLMを呼び出し、`AIFunctionFactory`でツール（関数）を自動で利用させる具体的なC#コードから始め、基本的なLLM連携の仕組みを解説しています。

さらに、Agent Frameworkの中核である`ChatClientAgent`を用いた単一エージェントの構築方法を詳解。指示とツールを与えられた猫型アシスタントが会話履歴を考慮して応答する例をC#コードで示し、AIとの状態維持会話の実現方法を示唆しています。

特筆すべきはマルチエージェント機能です。複数のエージェントを順番に実行するシーケンシャルワークフローを`AgentWorkflowBuilder`で簡単に構築できる点が強調されています。小説のタイトルを考えるエージェント、最初の一文を考えるエージェント、それらを結合するエージェントという三段階の連携をC#コードで示し、ストリーミングによる実行状況の可視化も解説。これにより、複雑なタスクを分担して実行する高度なAIアプリケーションを効率的に開発する具体的な道筋が示されます。Semantic Kernelからの移行コストはゼロではないものの、この再整理されたアーキテクチャは、将来の.NETでのAI開発においてよりクリーンで拡張性の高い基盤を提供します。