## Claude Codeを使ったSaaSセキュリティチェックの自動化

https://kaminashi-developer.hatenablog.jp/entry/automating-saas-security-checks-with-claude-code

CLIエージェントの**Claude Code**を活用して、膨大な規約類が伴うSaaSセキュリティチェックの調査からレポート生成までを自動化する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, SaaS Security, LLM Agents, Automation, Corporate Engineering]]

株式会社カミナシが取り組む、AnthropicのCLIツール**Claude Code**を用いたSaaSセキュリティチェックの自動化事例を紹介している。従来、コーポレートエンジニアが手動で行っていた利用規約やプライバシーポリシーの読み込み、MFA対応の有無、AI機能のデータ学習ポリシー等の調査を、AIエージェントに代替させる仕組みだ。

技術的なポイントは、**Custom Slash Command**機能によるワークフローの固定化にある。`.claude/commands/saas-check.md` にプロンプトとルールを定義し、事前収集したPDFの解析と**Web Search**による外部補完を組み合わせることで、精度の高いレポート（`result.md`）を自動生成する。エージェントがユーザーに不足情報をヒアリングする**AskUserQuestion**ツールも活用されており、対話的な調査プロセスを実現している。

この取り組みにより、エンジニアの役割は「泥臭い情報収集」から「生成された結果のレビューと判断」へと転換された。GitHub上でのPRベースの運用を取り入れることで、判断の質を担保しつつ、SaaS導入依頼の急増に対応している。**Claude Code**のコーディング以外の実用的なユースケースを探しているエンジニアや、社内業務の効率化を担うコーポレートエンジニアにとって、即効性の高い実践ガイドである。
