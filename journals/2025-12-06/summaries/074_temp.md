## Air: JetBrainsのエージェント型開発環境

https://air.dev/

**Original Title**: Air: Multitask with agents, stay in control

JetBrainsが開発する新しいAI開発環境「Air」は、Claude Agentを使用して複数のAIエージェントを並列実行し、タスク定義から進捗監視、レビュー/コミットまでの完全なループを開発者の制御下で実現します。

**Content Type**: Products & Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 82/100 | **Overall**: 73/100

**Topics**: [[エージェント型開発, JetBrains, IDE, 並列タスク実行, Claude Agent]]

### 概要
Air（Agentic Development Environment）は、JetBrainsが提供する、複数のAIエージェントと協働してコーディングタスクを並列実行できる開発環境です。現在macOS向けプレビュー版が公開されており、Anthropicのサブスクリプションが必要です。

### 主要な機能

**1. タスク定義と文脈提供**
- ファイル、コミット、シンボル、画像を参照してエージェントに適切なコンテキストを提供
- プロジェクト全体を探索しながらタスクを定義

**2. 並列実行とコンフリクト回避**
- 複数のエージェントを同時に起動し、それぞれの実行場所を決定
- Docker、Git worktree、またはクラウド環境（近日公開予定）で自動セットアップ
- 各タスクを分離して実行し、コンフリクトを防止

**3. タスク間の切り替え**
- 非同期タスクの進捗を追跡
- いつでも介入して追加入力、ステップレビュー、エージェントの動作確認が可能

**4. レビューとコミット**
- IDE的な体験でコード変更を確認
- コードコメントを残し、修正を依頼、またはタスクのフォローアップ
- Airがローカルプロジェクトに変更を戻し、コミット準備完了

### 今後の展開

**複数エージェント対応**
- 現在はClaude Agentに対応
- Codex、Gemini、Junieが近日対応予定

**クラウド実行**
- ラップトップを閉じてもAirがクラウド上で作業を継続

**マルチプラットフォーム**
- WindowsとLinux版を準備中
- 各OSに最適化された体験を提供

**Webクライアント**
- デスクトップアプリまたはブラウザ版でタスクの開始とレビューが可能

### 技術的特徴
- Docker統合による環境分離
- Git worktreeサポート
- 並列タスク管理
- リアルタイム進捗監視
- IDE風コードレビュー機能

### 評価のポイント

**強み:**
- 既存IDE大手JetBrainsによる信頼性の高い実装
- 並列タスク実行による効率化
- 開発者の制御を維持したまま自動化を実現
- 環境分離によるコンフリクト回避

**課題:**
- 現在macOSのみ対応（他OS版は今後）
- Anthropicサブスクリプション必須
- まだプレビュー版段階

### なぜ注目すべきか
JetBrainsという老舗IDEベンダーが、エージェント型開発という新しいパラダイムに本格参入した点が重要です。単なるコード補完ツールではなく、複数のタスクを並列管理し、開発者が制御を保ちながらAIに作業を委譲できる仕組みは、今後の開発環境の方向性を示しています。Docker/Git worktreeを活用した環境分離や、Claude以外のエージェント対応予定など、実用的な設計思想が見られます。

### 参考リンク
- チュートリアル: https://www.jetbrains.com/help/air/
- X (Twitter): https://x.com/getsome_air
- ダウンロード（macOS）: https://download.jetbrains.com/product?code=AIR&latest&distribution=macos_aarch64&type=preview
