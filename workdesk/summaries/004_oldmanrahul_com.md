## GitHubのPR URLに「.diff」を付与してAIコードレビューを10秒で開始するテクニック

https://oldmanrahul.com/2025/12/19/ai-code-review-trick/

**Original Title**: Get an AI code review in 10 seconds

GitHubのPR URL末尾に「.diff」を追加して取得した生の差分データをLLMに投入することで、専用ツールを使わずに即座にコードレビューのフィードバックを得るワークフローを推奨する。

**Content Type**: 📖 Tutorial & Guide (チュートリアル & ガイド)
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 53/100 | **Annex Potential**: 52/100 | **Overall**: 80/100

**Topics**: [[GitHub, コードレビュー, LLM, 開発ワークフロー, 生産性向上]]

GitHub Copilot Enterpriseや特定のブラウザ拡張機能などのツールを導入することなく、GitHubのプルリクエスト（PR）から即座にAIによるフィードバックを得るためのシンプルな「トリック」が紹介されています。手法は極めて単純で、任意のPRのURLの末尾に`.diff`を追加するだけです。これにより、ブラウザ上にコードの生の差分（raw diff）が表示されるため、そのテキストをコピーしてChatGPTやClaudeなどのLLMに貼り付け、レビューを依頼することが可能になります。

筆者は、この手法が人間の同僚によるコードレビューを完全に置き換えるものではないと強調しつつも、人間が介在する前の「第1パス（初期確認）」として非常に有効であると主張しています。明らかなバグの検出や、自分では見落としがちなエッジケースの指摘をAIから事前に受けることで、人間による本番のレビューに回す前にコードをよりクリーンな状態に仕上げることができます。これにより、開発サイクル全体の短縮につながるだけでなく、レビュワーの負担を減らす「同僚への礼儀」としても機能すると、筆者はその意義を説明しています。