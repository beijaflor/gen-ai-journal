## ClaudeCodeでSerenaMCP導入時にTerraformファイルがあるとエラーになる事がある

https://qiita.com/sodafloatlab/items/79958a7a492ba4e05188

AIコーディングツールSerenaMCPとClaudeCodeの連携時に発生するTerraform関連エラーに対し、設定ファイル編集による具体的な解決手順を詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIコーディングツール, SerenaMCP, ClaudeCode, Terraform, 開発環境設定]]

AIコーディング環境の導入において、既存のプロジェクト構成が予期せぬエラーを引き起こすケースがあります。本記事は、AIアシスタントSerenaMCPをClaudeCodeに導入する際、Terraformファイルが存在することで「Terraform executable not found」というエラーが発生する問題とその具体的な解決策を詳述しています。

問題の根源は、執筆時点（2025年8月5日）でSerenaMCPがTerraformを直接サポートしていない点にあります。SerenaMCPの言語検出機能がプロジェクトルートにある`infrastructure/`配下のTerraformファイルを優先的に認識し、サポート対象外の`terraform`を`~/.serena/project.yml`の`language`として自動設定してしまうことが原因でした。この誤認識により、AIアシスタントがプロジェクトの正しいコンテキストを理解できず、トークン削減などのSerenaMCPの利点を享受できなくなります。

この問題の解決策は、`~/.serena/project.yml`を手動で編集することです。具体的には、`language`設定をプロジェクトの主要言語（例: `python`）に変更し、同時に`ignored_paths`に`infrastructure/*`などのTerraform管理パスを追加します。これにより、SerenaMCPが不要なTerraformファイルをスキャンしないようになり、正しいプロジェクトコンテキストで動作するようになります。

この事例は、AI開発ツールがまだ既存の多様なプロジェクト構造（特にIaCとアプリケーションコードが混在するモノレポなど）に完全に適応しているわけではない現状を示しています。エンジニアは、AIアシスタントを最大限に活用するために、そのコンテキスト理解の限界を認識し、適切な設定調整を行う必要があることを強調しています。将来的に、AIツールがより賢くプロジェクト構造を解釈し、TerraformなどのIaCもネイティブにサポートするようになることを期待させる内容でもあります。同様の課題に直面している開発者にとって、具体的な解決策として非常に実用的な知見を提供するものです。