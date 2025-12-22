## OpenMemory: LLMアプリケーション向けローカル永続メモリストア

https://github.com/CaviraOSS/OpenMemory

**Original Title**: GitHub - CaviraOSS/OpenMemory: Local persistent memory store for LLM applications including claude desktop, github copilot, codex, antigravity, etc.

OpenMemoryは、従来のベクトルデータベースとは異なり、ローカルで永続的な多分野認知構造を持つLLM向けメモリエンジンを提供し、AIエージェントの長期的な記憶能力と推論精度を大幅に向上させます。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 97/100 | **Overall**: 96/100

**Topics**: [[LLMメモリ管理, 認知アーキテクチャ, ローカルAI開発, ベクトルデータベース代替, AIエージェントツール]]

CaviraOSSが発表した「OpenMemory」は、Claude DesktopやGitHub CopilotなどのLLMアプリケーション向けに設計された、ローカルで永続的なメモリストアです。従来のLLMがメッセージ間で情報を「忘れる」問題や、ベクトルデータベースがフラットなデータチャンクを保存し、メモリの種類、重要度、時間、関係性を理解しないという課題を解決するために開発されました。

OpenMemoryは、単なるベクトルデータベースではなく、多分野認知構造、自然な減衰、グラフベースのリコール、時間認識型ファクトトラッキング、そして説明可能なウェイポイントトレースといった機能を備えた「完全な認知メモリエンジン」として機能します。これにより、AIシステムに永続的な記憶、データ所有権、そしてベンダーロックインからの解放を提供します。

特に、同プロジェクトは、PineconeとLangChainを組み合わせた従来のメモリ実装が12行以上を要するのに対し、OpenMemoryではわずか3行で設定が完了すると強調しています。この手軽さの鍵となるのが「Standalone Mode」であり、バックエンドサーバーなしでNode.jsまたはPythonアプリケーション内で直接実行でき、ローカルSQLiteファイルにデータを保存するため、ゼロコンフィグ、オフライン動作、および高いプライバシーを実現します。

OpenMemoryのアーキテクチャは「階層的メモリ分解」を採用しており、入力された情報をエピソード記憶、意味記憶、手続き記憶、感情記憶、内省記憶といった複数のセクターに分類・処理します。各セクターで埋め込みが生成され、ベクトル検索、ウェイポイントグラフ拡張、類似性・顕著性・新近性・重みに基づく複合スコアリングが行われます。さらに、時間の側面を重視した「Temporal Knowledge Graph」を搭載し、事実の有効期間を管理し、エージェントが過去の事実と現在の事実を混同しないようにすることで、長期的な推論能力を向上させます。

開発者向けには、Node.jsおよびPython用のローカルファーストSDK、バックエンドサーバーモード、そしてVS Code拡張機能を提供しています。特にVS Code拡張機能は、コーディング履歴やプロジェクトの進化を追跡し、AIアシスタントに高信号メモリサマリーを供給します。また、MCP (Model Context Protocol) とのネイティブ統合により、Claude DesktopやCursorなどのMCPクライアントで直接OpenMemoryを利用可能です。

性能ベンチマークでは、10万ノードに対する平均リコール時間115ms、スループット338QPSといった高い数値を報告しており、既存の類似システム（Zep、Supermemory、Mem0）と比較しても、応答時間、スループット、Recall@5の精度、減衰安定性において優位性を示しています。著者は、OpenMemoryがAIエージェント、コパイロット、アプリケーションにとっての「メモリOS」となり、開発者のワークフローに高い実用性と効率性をもたらすと主張しています。