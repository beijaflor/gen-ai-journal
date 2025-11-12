## Claude Codeに計画的なコーディングを強制する「Superpowers MCP」

https://www.trevorlasn.com/blog/superpowers-claude-code-skills

**Original Title**: How I force Claude Code to plan before coding with Superpowers MCP

著者は、「Superpowers MCP」というカスタムツールを導入することで、Claude Codeが計画なしにコード生成を進める問題を解決し、構造化された開発ワークフローを強制することで、大規模な移行やデバッグ作業の効率と品質を劇的に向上させています。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[AIエージェント, コーディング支援ツール, 開発プロセス改善, Next.js移行, 計画駆動開発]]

この記事では、著者がClaude Codeを大規模プロジェクトで使用する際に直面した、AIが計画なしにコード変更を提案し、結果としてファイルの見落としやバグにつながるという課題に対する解決策として、独自ツール「Superpowers MCP（Modular Custom Persona）」を紹介しています。Superpowers MCPは、ClaudeのAgent Skills機能を活用し、開発ワークフロー（テスト、デバッグ、計画）を体系的に強制することで、コードの品質と開発効率を大幅に向上させることを目的としています。

このシステムは、Claude Codeがタスクに合わせて自動的にロードする「スキル」として機能します。各スキルは、指示、スクリプト、リソースを含むフォルダとして定義され、適用条件や従うべきプロセスを規定します。これにより、Claudeは作業を小さなチャンクに分割し、進行状況を`PLAN.md`、`progress.md`、`verification.md`といったマークダウンファイルに記録するため、トークン効率が向上し、セッション間でコンテキストが失われることがありません。

著者は特に重要な3つのスラッシュコマンドを挙げています。アイデアを洗練する`/superpowers:brainstorm`、詳細な実装計画を作成する`/superpowers:write-plan`、そして計画をバッチ処理で実行・レビューする`/superpowers:execute-plan`です。具体的な例として、Next.js 16の`cacheComponents`機能有効化という大規模な移行作業で`/superpowers:write-plan`を使用した際、23のAPIルートファイル、`new Date()`を使用するコンポーネント、Suspense境界が必要なコンテキストプロバイダーなど、500行に及ぶ詳細なロードマップが生成されたと述べています。この計画には、各フェーズの検証コマンド、成功基準（Lighthouseスコア95以上など）、そしてロールバック計画までが含まれており、コードに触れる前に全体像を把握できたことが、バグの回避と開発時間の短縮に大きく貢献したと強調しています。

Superpowers MCPは、テスト駆動開発（TDD）、体系的なデバッグ、完了前の検証といったスキルを通じて、開発者がステップを飛ばすことを文字通り「阻止」します。例えば、デバッグ時には推測による修正ではなく、根本原因の調査を強制し、TDDではテストが失敗するのを確認してからコードを書くように促します。これにより、確実な検証に基づくプロアクティブな開発が可能になり、単に「多分動く」という曖昧な状態での作業を排除できます。

Superpowers MCPはClaude CodeのCLIツールを介してプラグインとして簡単に導入でき、AIエージェントを活用する開発プロセスに計画性と堅牢性をもたらす、極めて実用的なソリューションです。著者は、このツールがなければ、数日間の反応的なデバッグを要したであろう作業が、詳細な計画によってプロアクティブに進められ、信頼性の高い成果に結びついた点を最大の利点としています。