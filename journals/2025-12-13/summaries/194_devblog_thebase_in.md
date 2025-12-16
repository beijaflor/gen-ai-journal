## GitHub Copilot の独自観点レビューで速さと品質を両立する

https://devblog.thebase.in/entry/2025/12/12/110000

BASEのエンジニアがGitHub CopilotとCustom Instructionsを活用し、コードレビューの品質と速度を向上させる具体的な手法を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, コードレビュー, VSCode, Custom Instructions, 開発効率化]]

BASEのカートチームのバックエンドエンジニアが実践する、GitHub CopilotとVSCode Custom Instructionsを組み合わせた独自のコードレビュー手法が紹介されました。このアプローチは、コードレビューの品質を維持しつつ、その速度を大幅に向上させることを目指しています。

著者は、自身のコードレビュープロセスにおいて、GitHub Copilot Code Reviewに加えて、VSCode上でCopilotにカスタムのレビュー観点を与えることで、「複眼チェック」を単独で行い、レビュー品質の下限を担保しながら速度向上を実現していると説明します。具体的な導入手順は以下の通りです。まず、VSCodeにGitHub MCP Serverをインストールし、Personal Access Token (PAT) またはApp tokenを設定します。次に、プロジェクトの`.github/instructions`ディレクトリ配下に`codereview.instructions.md`というカスタム命令ファイルを配置します。このファイルには、「変更ファイル一覧の確認」「変更差分の解説」「コードレビューガイドラインによる○△×評価」「テストケースの列挙と不足指摘」「既存実装との比較と差異指摘」「改善案の提案」といった、6つの詳細なコードレビュー手順が記述されています。

実際のレビュー実行時には、VSCodeのCopilot Chatを開き、「コンテキストの追加」から作成した`codereview`のカスタム命令を選択します。その後、チャット入力欄にレビュー対象のPull RequestのURLを貼り付け、「レビューしてください」と依頼するだけで、CopilotがGitHub MCP Serverを介してコード差分をチェックし、カスタム命令に沿った多角的なレビュー結果を生成します。

生成されるレビュー結果は、PRの概要と変更内容の解説、コードレビューガイドラインに基づく具体的な○△×評価、実装されているテストケースの列挙とその不足点の指摘、同じネームスペース内の既存実装との比較、気になった箇所と改善案の提案、そしてPR作成者への質問と総評から構成されます。これにより、エンジニアはレビューの着眼点や品質が標準化され、より効率的かつ網羅的なレビューが可能になると筆者は述べています。この手法は、WebアプリケーションエンジニアがGitHub Copilotを単なるコード補完ツールとしてだけでなく、レビュープロセスにおける強力な協調AIとして活用し、開発ワークフロー全体の効率と品質を高めるための実践的な具体例として非常に価値があります。