## Conductor: Gemini CLIのためのコンテキスト駆動型開発を導入

https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/

**Original Title**: Conductor: Introducing context-driven development for Gemini CLI

Googleは、Gemini CLI向けの新しい拡張機能「Conductor」を発表し、チャットベースのAI開発で失われがちなプロジェクトのコンテキストを、永続的なMarkdownファイルとしてコードベースと共に管理するコンテキスト駆動型開発を導入します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Gemini CLI, Context-Driven Development, AI Agent Workflows, Persistent Context, Brownfield Projects]]

Googleは、Gemini CLI向けの新拡張機能「Conductor」を発表し、AI開発における「コンテキスト駆動型開発」を導入しました。これは、チャットベースのAIツールでは維持が難しいプロジェクトのコンテキストを、永続的なMarkdownファイルとしてコードベースと共に管理する画期的なアプローチです。Conductorは、人間が開発の主導権を保持しつつ、AIエージェントにプロジェクトの深い認識を与え、一貫性と高品質を伴うコード生成を可能にします。

Conductorの核心は、プロジェクトの製品目標、技術スタック、ワークフローの好みといったコンテキストをリポジトリ内で「唯一の信頼できる情報源」として形式化することです。これにより、AIは定義されたガイドラインに常に従い、既存コードベースとの整合性を保った開発が実現します。特に、既存の複雑なコードベース（ブラウンフィールドプロジェクト）に対しては、Conductorが対話を通じてアーキテクチャやガイドラインのドキュメント作成を支援し、プロジェクトの成長と共にAIの知識も更新されます。

チーム開発においては、Conductorはプロジェクトレベルの設定を共有し、例えばテスト戦略などを自動適用させることで、どの開発者がAIを使用してもコードの一貫性を保証します。これは新規メンバーのオンボーディングを加速し、チーム全体の生産性と品質を向上させます。

Conductorのワークフローは、複雑なタスクに適した構造化されたエージェント開発を促進します。
1.  **コンテキスト確立**: `/conductor:setup`で製品、技術スタック、ワークフローのコア情報を定義。
2.  **仕様と計画策定**: `/conductor:newTrack`で作業単位を初期化し、詳細な要件（Specs）と実行可能なToDoリスト（Plan）をMarkdownファイルで作成。
3.  **実装**: 計画承認後、`/conductor:implement`を実行。エージェントが`plan.md`に沿って作業し、進捗はファイルに保存され、中断や変更も容易です。

著者は、このコンテキスト駆動型開発が複雑なプロジェクトに高品質な成果をもたらし、Geminiをエンジニアリングチームの強力な拡張機能とすると述べています。