## How we accelerated Secret Protection engineering with Copilot

https://github.blog/ai-and-ml/github-copilot/how-we-accelerated-secret-protection-engineering-with-copilot/

GitHubのSecret Protectionチームは、GitHub Copilotを活用し、トークンの有効性チェック範囲を劇的に拡大することで、定型的なエンジニアリングワークフローの自動化と加速を実現した。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[GitHub Copilot, Secret Protection, AIエージェント, 開発ワークフロー自動化, DevSecOps]]

GitHubのSecret Protectionチームは、誤ってコミットされた機密情報の有効性を確認する「Validity Checks」機能の強化において、GitHub Copilotを効果的に活用した経験を共有しました。従来のプロセスでは、新しいトークンタイプの検証ロジックを追加する作業がフレームワーク化されていても遅く、網羅率向上が課題でした。

この課題に対し、チームはCopilotを「コーディング」と「リリース設定」という、特に反復性の高いステップに組み込みました。具体的には、人間がAPIエンドポイントの調査を行い、その結果を詳細なGitHub IssueとしてCopilotに指示（プロンプト）として与えます。Copilotはこの指示に基づき、バリデーターのコードを含むプルリクエストを自動生成します。生成されたコードは、人間のレビューと自動テストを経て、既存のプロセスと同様にデプロイされます。特に「ダークシップ」（本番環境で挙動を観察しつつ、結果をデータベースに書き込まない）という安全な検証フェーズを経て、最終的なリリース設定変更もCopilotが担当します。

この取り組みにより、チームは数週間で約90種類のトークンタイプに対応し、以前は数ヶ月かかっていた32タイプから大幅に加速しました。これは、Copilotが人間のエンジニアにとって「増幅装置」として機能し、繰り返しの多いタスクを並行処理可能にしたためです。

Webアプリケーションエンジニアにとっての重要な教訓は、AIコーディングエージェントが、定型的でフレームワークに沿ったタスクを劇的に加速できる点です。ただし、Copilotは人間のエンジニアリング判断の代替ではなく、質の高いプロンプト作成、人間による厳格なコードレビュー、テストが不可欠であると強調されています。この事例は、既存のワークフローにAIを賢く組み込むことで、開発者はより複雑で創造的な課題に集中できるようになることを示唆しています。