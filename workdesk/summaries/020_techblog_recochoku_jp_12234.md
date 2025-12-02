## Claudeで加速するIssue駆動開発：PlayPASS Androidの事例紹介

https://techblog.recochoku.jp/12234

PlayPASS Androidチームは、Claude Code/ActionとIssue駆動開発を組み合わせ、開発ワークフローを自動化・効率化し、開発速度を平均2倍に向上させた具体的な事例を紹介します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Issue駆動開発, Claude Code Action, 開発効率化, Android開発, GitHub Actions]]

PlayPASS Androidチームは、約1.5ヶ月にわたりClaude CodeおよびClaude Code Actionを活用したIssue駆動開発を実践し、開発プロセスの自動化と効率化を実現した事例を紹介しています。従来の開発では、タスクの属人化、並行作業の難しさ、PRレビューのボトルネックといった課題に直面していました。

これらの課題に対し、チームはIssue駆動開発とClaude Code Actionによる自動実装を導入しました。まず、すべてのタスクを「ローカル実装」（Claude Codeによる対話的設計、デバイス依存機能など）と「リモート実装」（Claude Code Actionによるスタンドアロンで完結する軽・中難易度タスク）に分類するワークフローを確立。特にリモート実装向けに、軽微な修正やUseCaseユニットテスト作成といった詳細なIssueテンプレートを複数用意し、Claude Code Actionへの明確な指示書として活用しました。タスクを思いついたらまずIssue化し、AIでの自動化を検討する「Issue駆動の習慣化」が生産性向上の鍵となりました。

GitHub連携では、Androidビルド環境の最適化（ビルド時間を10〜15分から約6分に短縮し、Claude Code Actionのタイムアウトを回避）や、カスタムコマンドによるワークフロー自動化を推進。例えば、`/pr-create`コマンドは、変更内容を自動分析し、PR説明文の自動生成と適切なラベル付けを行い、Draft PRを自動作成することで、PR作成時間を70%削減、レビュー工数を50%削減（pr-reviewコマンドと連携時）する効果を上げています。

この体制により、人間は複雑な設計や新機能開発といったコア業務に集中し、AI（Claude）がユニットテスト作成、リファクタリング、軽微な修正を並行して担当するタスク並列化が実現しました。さらに、GitHub CopilotとClaudeによる並列コードレビューで検出された問題は、Claudeが自動修正することで、レビュー対応の約50%が自動化され、実質的な開発速度が平均2倍に向上したと報告されています。

一方で、約1.5ヶ月の運用で、リモート実装における約3割の再修正が必要となる課題も浮上しました。これは依存関係の見落としやエッジケースの考慮漏れ、プロジェクト固有の規約理解不足が原因であり、対策として`CLAUDE.md`によるルール明文化、カスタムコマンドの活用、CopilotとClaudeによる二重自動レビューが挙げられています。

今後の展望としては、FigmaやNotion、Google AnalyticsとのMCP連携拡大、LSPベースのツール導入によるより複雑なタスクへの適用、チーム標準化の推進が検討されています。本記事は、Issue駆動開発とAIツールを組み合わせることで、開発速度の向上、並行作業の実現、コア業務への集中が可能となることを示しており、Android開発に限らず多くのプロジェクトに応用できる実践的な知見を提供しています。