## ターミナルでのAI体験を統合する「Toad」のリリース

https://willmcgugan.github.io/toad-released/

**Original Title**: Toad is a unified experience for AI in the terminal

複数のAIエージェントCLIを一つの洗練されたターミナルUI上で統合管理・操作できるフロントエンドツール「Toad」を提供する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Coding Agents, Terminal UI, Developer Tools, ACP Protocol, OpenHands]]

RichやTextualといったPythonのターミナルUIライブラリの作者として知られるWill McGugan氏が、AIエージェントをターミナルで扱うための統合フロントエンド「Toad」をリリースした。Toad（Textual Codeの略）は、OpenHands、Claude Code、Gemini CLIなど12種類以上のAIエージェントを一つのUIでシームレスに操作可能にするツールである。

筆者がこのツールを開発した背景には、自身のスタートアップが資金難で終了した後、自身の持つ「ターミナルをGUIのように見せる技術」をエージェント型コーディングに役立てたいという強い動機がある。

既存のCLIツールと比較したToadの強みは、開発者が日常的に使用するターミナル体験を損なうことなく、モダンなAI機能を統合している点にある。筆者によれば、特に以下の機能が差別化要因となっている。まず「@」による高速なファイル参照機能だ。これはプロジェクトの.gitignoreを考慮したファジーサーチにより、必要なコンテキストを即座にAIに提供できる。次に、シンタックスハイライトに対応した高度なマークダウンレンダリングだ。筆者が培ってきた技術により、大規模なドキュメントでも高速に、かつ表やコードフェンスを美しく表示する。

そして何より特徴的なのが「完全なインタラクティブ・シェルの統合」である。多くのAIツールが標準出力を表示するに留まる中、ToadはTUI（Textual User Interface）アプリケーションの実行や、フルカラー・マウスサポートを維持したまま、AIとの対話とコマンド実行をシームレスに往復できる。筆者はこれを「AIとの会話を伝統的なターミナルワークフローの自然な延長線上にするため」と説明している。

また、Jupyter Notebookのような「過去の会話ブロックを再利用する」コンセプトも導入されており、ターミナルを単なる文字のストリーミング場ではなく、構造化された作業空間として定義し直している。ACP（Agent Control Protocol）を採用することで、今後登場する新たなエージェントCLIも容易に統合できる拡張性を備えている。ターミナル環境に特化したエンジニアにとって、複数のAIエージェントを使い分けながら既存のワークフロー（シェルコマンド、補完、キーボード操作）を維持できるToadは、エージェント時代の新たな標準ツールとしての可能性を秘めている。