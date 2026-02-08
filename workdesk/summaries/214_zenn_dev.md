## Claude Codeに乗り遅れたあなたへ。Open CodeとGithub CopilotとVSCode（期間限定kimi k2.5）

https://zenn.dev/kiva/articles/7be372e4783248

**GitHub Copilot**をバックエンドとして利用可能なCLI型AIエージェント**Open Code**の導入方法と、開発現場での実用性を検証する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:3/5
**Main Journal**: 73/100 | **Annex Potential**: 73/100 | **Overall**: 72/100

**Topics**: [[Open Code, GitHub Copilot, Claude Code, AIエージェント, CLIツール]]

本記事は、**Claude Code**の対抗馬として注目されるオープンソースのCLIツール**Open Code**を、株式会社KivaのCTOが実際に試用した記録です。**GitHub Copilot**をバックエンドとして連携させる手順や、リポジトリの仕様書となる**AGENTS.md**の自動生成、**Planモード**による実装方針の検討、コードレビュー機能など、ターミナル完結型のエージェント開発サイクルを具体的に紹介しています。また、期間限定で利用可能な**Kimi K2.5**の統合についても言及されています。

筆者は、CLIベースの開発がエディタを介さないため動作が非常に軽量である点や、新規機能の初期開発における高い生産性を評価しています。一方で、CLI上ではコードの差分確認（Diff）が困難であることや、既存の複雑なチーム開発においては依然として**VS Code**上のGUI操作に分があるといった、現場視点での冷静な比較分析も提示されています。

**GitHub Copilot**のライセンスを活かしつつ、**Claude Code**のようなCLIエージェントの操作感を体験したいエンジニアや、軽量なAI開発環境を模索している開発者に最適なガイドです。