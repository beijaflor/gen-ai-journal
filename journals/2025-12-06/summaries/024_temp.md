## VSCode拡張「Continue」× Amazon Bedrock × MCPで開発支援を試してみた

https://qiita.com/saiashi/items/6e970afad01cad979b69

VSCode拡張「Continue」とAWS Bedrock、さらにMCPを連携させることで、低コストかつプライベートリポジトリへの対応を含むGitHub開発フロー全体を自動化するAI開発支援環境を構築できることを実証しています。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AI開発支援, VSCode拡張, Amazon Bedrock, MCP, GitHub自動化]]

記事は、Claude CodeやGitHub Copilotといった有料ツールを試すハードルを感じている開発者向けに、VSCode拡張「Continue」とAWS Bedrock、さらにModel Context Protocol（MCP）を組み合わせた低コストで柔軟な生成AI開発支援環境の構築方法と活用事例を紹介しています。

著者はまず、これらの技術要素の概要を説明します。「Continue」はオープンソースのVSCode拡張でチャットやコード生成が可能、「Amazon Bedrock」は複数のLLMモデル（Claude Haiku 4.5など）を従量課金で利用できるAWSのAI基盤、「MCP」はLLMを外部ツールやデータソースに接続し、AIエージェントの能力を拡張するプロトコルです。

環境構築として、Bedrock用のIAMユーザー作成（AmazonBedrockLimitedAccessポリシー）とアクセスキーの発行、VSCodeへのContinueインストール、そして`config.yaml`でのBedrockモデル（例: Claude Haiku 4.5）とAWSプロファイルの設定手順を詳細に解説しています。セキュリティリスクとして、アクセスキー漏洩による高額料金発生の可能性も指摘し、特定IPアドレスからの利用制限などの対策を推奨しています。

デモンストレーションでは、まず簡単な問い合わせやTerraformコードの自動生成（AWSプロバイダーの最新バージョンにも対応）を「Continue」単体で実行。次に、プライベートGitHubリポジトリへのアクセスができないという課題に対し、GitHub-MCP-Server（DockerとGitHub PATを使用）を導入することで解決できることを示しています。特に注目すべきは、MCPを有効にした状態で、GitHubのIssue解析から作業ブランチの作成、コード修正、コミット・プッシュ、さらにはプルリクエストの作成までの一連の複雑な開発フローをAIがわずか数秒で自動化する応用例です。

著者はこの統合環境のメリットとして、「まるで優秀なペアエンジニアが横で作業してくれているような体験」が得られる点を強調しています。これにより、人間は「作業」ではなく「指示」や「判断」に集中できるようになり、「AIと人間のペアプロ」が実用段階に入りつつあると述べています。

ただし、利用上の注意点も明確に示しています。AIのハルシネーション（誤回答）により、生成されたコードや提案は必ず人間がレビューすることの重要性、GitHub PATには必要最小限の権限のみ付与し、機密情報をAIに入力しないといったセキュリティ対策、そしてBedrockが従量課金であるため、特にMCP利用時にはトークン使用量が増加しコストが跳ねやすい点を挙げ、CloudWatchでのコスト監視を推奨しています。今回の試行錯誤でかかった費用が0.52USDであったことも参考として示し、コストを意識した利用を促しています。