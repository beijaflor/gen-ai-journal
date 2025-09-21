## たった9行でAIレビュー導入！Claude CodeとGitLab CIで全リポジトリにAIコードレビューを導入した話

https://www.m3tech.blog/entry//claude-code-gitlab-ci-ai-review

エムスリーは、Claude CodeとGitLab CIを統合し、わずか9行のYAMLで全リポジトリにカスタマイズ可能なAIコードレビューシステムを導入しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AIコードレビュー, GitLab CI, Claude Code, Workload Identity Federation, 開発ワークフロー改善]]

エムスリーは、セルフホストのGitLab環境において、Claude CodeとGitLab CIを活用し、わずか9行のCI/CD設定で全リポジトリにAIコードレビューを導入する画期的な仕組みを構築しました。この取り組みは、レビューの深さのばらつき、特定のレビュアーへの負担集中、大規模な変更のレビュー開始時の障壁といった長年の課題を解決します。

システムの中核は、Workload Identity Federation (WIF) によるセキュアな認証を基盤とし、APIキーなしでClaude Codeを利用可能にした点です。共通のGitLab CIテンプレートを通じてClaude Code CLIを呼び出し、マージリクエストの差分を自動でレビューさせます。特に重要なのは、レビュー観点を定義したMarkdownファイルや追加プロンプトを指定することで、プロジェクトやチーム固有の暗黙知をAIに学習させ、レビューをカスタマイズできる点です。AIは、GitLab APIと連携し、具体的なコード箇所にメンション付きのコメントを生成するため、人間はAIの指摘を起点に、より高度なレビューに集中できます。

この導入により、タイポや単純なミスが減少し、プロジェクト特有のルールが形式知化され、コードレビュー自体への関心が高まる効果が得られました。MVPから段階的に機能改善を重ね、現在では週に200件以上のAIレビューが自動で行われています。開発ワークフローの効率化とコード品質向上を実現する、具体的なAIツール活用事例として非常に価値があります。