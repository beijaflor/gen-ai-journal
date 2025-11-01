## Playwright Agents によるテストの自動生成を試してみた

https://azukiazusa.dev/blog/playwright-agents/

Playwright AgentsがClaude Codeと連携し、テストの計画、生成、および失敗したテストの修正を自動化する具体的な方法を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Playwright, AI Test Generation, Claude Code, Agent-based Development, Automated Testing]]

Playwright v1.56で導入されたPlaywright Agentsは、Planner、Generator、Healerの3つのエージェントから構成され、アプリケーションコードを解析してテストケースの計画、テストコードの生成、失敗したテストの修正を自動化します。本記事は、Claude CodeからPlaywright Agentsを呼び出し、Next.jsで構築されたシンプルなカンバンアプリのテストコードを自動生成する具体的な手順を解説しています。

まず、`npx playwright init-agents --loop=claude`コマンドでPlaywright Agentsの定義とClaude Code用の設定ファイルを生成します。これにより、Planner、Generator、HealerエージェントがClaude CodeのSubAgentsとして利用可能になります。

次に、Plannerエージェントを`@agent-playwright-test-planner`として呼び出し、ユーザーが定義したストーリーに基づいてテストシナリオの計画をMarkdown形式（`TEST_PLAN.md`）で生成します。著者は、このプロセスがプロンプトで明示的に指定されなかった特殊文字の入力ハンドリングやタスクの優先度設定など、アプリケーションコードからより詳細なテストケースを導き出す点に注目しています。これにより、手動での計画段階の負担が大幅に軽減され、より包括的なテストケースが作成されると述べています。

続いて、`@agent-playwright-test-generator`でGeneratorエージェントを呼び出し、`TEST_PLAN.md`を参照して実際のPlaywrightテストコードを生成します。これにより、開発者は手作業でのテストコード記述にかかる時間を大幅に削減できると筆者は強調します。

最後に、実行して失敗したテストがある場合、`@agent-playwright-test-healer`でHealerエージェントを起動します。Healerはテストを実行し、エラー内容を分析して、問題の解決策を導き出しコードを修正します。具体的には、`<div>`を`<h3>`に変更してセマンティクスとアクセシビリティを改善したり、Next.js App Routerのキャッシュ問題を解決するために`page.reload()`を追加したりする修正が例として挙げられています。これにより、テストのデバッグと保守の手間が自動化され、テストスイートの健全性維持に寄与すると説明されています。

著者は、Playwright Agentsがテストのライフサイクル全体（計画、生成、修正）を自動化することで、開発者の生産性を飛躍的に向上させると結論付けています。特に、AIエージェントと連携することで、より実践的で効率的なテスト自動化が実現できる点が、ウェブアプリケーションエンジニアにとって重要な意味を持つと述べています。