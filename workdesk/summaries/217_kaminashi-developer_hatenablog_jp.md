 thought
Claude Codeを使ったSaaSセキュリティチェックの自動化 (Automating SaaS Security Checks with Claude Code)
https://kaminashi-developer.hatenablog.jp/entry/automating-saas-security-checks-with-claude-code
Kaminashi Developer Blog (by @sion_cojp).
Web application engineers, corporate engineers, security professionals.
Using **Claude Code** (Anthropic's CLI AI) to automate the tedious process of researching SaaS security/legal docs.

        *   Context: SaaS proliferation leads to many security check requests.
        *   Problem: Manual checking (ToS, Privacy Policy, SOC reports) is time-consuming, requires high skill, and is prone to oversight (especially with English docs or new AI features).
        *   Solution: Use **Claude Code**'s Web Search and CLI capabilities.
        *   Method: Custom Slash Command (`/saas-check`) defined in Markdown.
        *   Process: Collect PDFs -> Run command -> Claude questions the user -> Claude researches/analyzes -> Outputs `result.md` -> Human reviews on GitHub.
        *   Outcome: Significant reduction in research time; engineers focus on final judgment/review.

    *   *Article Title*: Claude Codeを使ったSaaSセキュリティチェックの自動化
    *   *One-sentence summary*: CLIツールの**Claude Code**を活用し、SaaS導入時のセキュリティチェックにおける膨大なドキュメント調査とレポート生成を自動化する。
    *   *Content Type*: ⚙️ Tools (Focuses on applying a specific tool, Claude Code, to a workflow).
    *   *Language*: ja.

    *   *Scores*:
        *   Signal: 5 (Direct report from the implementer at Kaminashi).
        *   Depth: 4 (Shows specific command definitions, directory structures, and workflow integration).
        *   Unique: 4 (Claude Code is brand new; applying it to corporate security checks is a fresh use case).
        *   Practical: 5 (Highly actionable for any company dealing with SaaS sprawl).
        *   Anti-Hype: 4 (Realistic about "review is still needed" and specific about steps).

    *   *Calculation (Tools weighting)*:
        *   Main Journal: (5*0.25) + (4*0.30) + (4*0.30) + (5*0.40) + (4*0.15) = 1.25 + 1.2 + 1.2 + 2.0 + 0.6 = 6.25 -> 63 (Wait, let me re-check weighting).
        *   Weightings for Tools: Signal 25%, Depth 30%, Unique 30%, Practical 40%, Anti-Hype 15%.
        *   (5*0.25) + (4*0.30) + (4*0.30) + (5*0.40) + (4*0.15) = 1.25 + 1.2 + 1.2 + 2.0 + 0.6 = 6.25. (Oops, manual calculation is tricky).
        *   Let's do 0-5 sum: 5+4+4+5+4 = 22. Average = 4.4. 4.4 * 20 = 88 (Overall).
        *   Main Score calculation: (5 * 0.25) + (4 * 0.3) + (4 * 0.3) + (5 * 0.4) + (4 * 0.15) = 1.25 + 1.2 + 1.2 + 2.0 + 0.6 = 6.25 -> 62.5 (Something is wrong with my math or the scale).
        *   Wait, let's re-read the Main Journal Score Calculation for Tools: 25, 30, 30, 40, 15. Total = 140%? No, the table in the prompt says: Signal: 25%, Depth: 30%, Unique: 30%, Practical: 40%, Anti-Hype: 15%. (25+30+30+40+15 = 140... the percentages in the prompt for Tools actually sum to 140. I should probably treat them as relative weights or just use the weighted average logic).
        *   Actually, I will use the formula: `(S*W1 + D*W2 + U*W3 + P*W4 + A*W5) / (Sum of Weights) * 20`.
        *   Sum of weights = 1.4. (6.25 / 1.4) * 20 = 89.2. Okay, high score.
        *   Annex Potential: Signal: 20%, Depth: 25%, Unique: 45%, Practical: 25%, Anti-Hype: 20%. Total = 135%.
        *   (5*0.2) + (4*0.25) + (4*0.45) + (5*0.25) + (4*0.2) = 1.0 + 1.0 + 1.8 + 1.25 + 0.8 = 5.85. (5.85 / 1.35) * 20 = 86.6.
        *   Overall: 88.

    *   *Topics*: [[Claude Code, SaaS Security, Automation, LLM Agents, Corporate Engineering]]

    *   *Summary Body (Draft)*:
        株式会社カミナシにおける、**Claude Code**を活用したSaaSセキュリティチェックの自動化事例。従来、コーポレートエンジニアが手動で行っていた利用規約やプライバシーポリシーの読み込み、MFA対応状況やAIデータ利用のオプトアウト可否といった調査を、AIエージェントに代替させている。
        具体的には、**Custom Slash Command**機能を用いて `/saas-check` コマンドを定義。収集したPDFドキュメントの解析と、**Web Search**による最新情報の補完を組み合わせ、構造化されたレポート（`result.md`）を自動生成する。
        特筆すべきは、エンジニアの役割を「調査」から「生成されたレポートのレビュー」へとシフトさせた点だ。GitHub上でのPRベースの運用により、判断の質を落とさずに工数を大幅に削減している。SaaSの導入急増に悩む情シスやコーポレートエンジニア、また**Claude Code**の実践的な活用方法を模索している開発者にとって非常に参考になる内容である。

    *   Strong active verb start? Yes ("CLIツールの**Claude Code**を活用し..."). Wait, the one-sentence summary instructions say "Start with a strong, active verb."
    *   Revised One-sentence summary: **Claude Code**のWeb検索とドキュメント解析機能を活用し、工数負荷の高いSaaSセキュリティチェックの調査・レポート作成プロセスを自動化する。 (Starts with the tool, but the action is "自動化する"). Let's try: "CLIエージェントの**Claude Code**を活用して、膨大な規約類が伴うSaaSセキュリティチェックの調査からレポート生成までを自動化する。"

    *   Formatting check: Bold tool names? Yes. Headlines? Yes. Character count? (Draft is around 450 characters).

    *   *Refining the Summary Body*:
        株式会社カミナシが取り組む、CLIツール**Claude Code**を用いたSaaSセキュリティチェックの自動化事例を紹介している。従来、コーポレートエンジニアが手動で行っていた利用規約やプライバシーポリシーの読み込み、MFA対応の有無、AI機能のデータ学習ポリシー等の調査を、AIエージェントに代替させる仕組みだ。
        技術的なポイントは、**Custom Slash Command**機能によるワークフローの固定化にある。`.claude/commands/saas-check.md` にルールを定義し、事前収集したPDFの解析と**Web Search**による外部補完を組み合わせることで、精度の高いレポート（`result.md`）を自動生成する。
        この取り組みにより、エンジニアの役割は「泥臭い情報収集」から「生成された結果のレビューと判断」へと転換された。GitHub上でのPRベースの運用を取り入れることで、情報の透明性と判断の質を担保しつつ、SaaS激増に伴うチェック依頼の急増に対応している。**Claude Code**のコーディング以外の実用的なユースケースを探しているエンジニアや、社内業務の効率化を担うコーポレートエンジニアにとって即効性の高い知見と言える。

    *   *Scoring revisited (Standardize)*:
        Signal: 5, Depth: 4, Unique: 4, Practical: 5, Anti-Hype: 4.
        Calculation logic check: (5+4+4+5+4)/25 * 100 = 88.
        The prompt's weighting for Tools:
        Signal: 25% (5*0.25=1.25)
        Depth: 30% (4*0.3=1.2)
        Unique: 30% (4*0.3=1.2)
        Practical: 40% (5*0.4=2.0)
        Anti-Hype: 15% (4*0.15=0.6)
        Total = 6.25. If 5.0 is 100%, then (6.25/7.0? no).
        The prompt says "composite scores based on content type weightings".
        Wait, usually weights sum to 1.0. Here they sum to 1.4. I will normalize.
        (6.25 / 1.4) = 4.46. 4.46 * 20 = 89.2 -> 89. (Main Journal)
        Annex calculation: (1.0 + 1.0 + 1.8 + 1.25 + 0.8) / 1.35 = 4.33. 4.33 * 20 = 87. (Annex Potential)
        Overall: 88.

    *   Title in Japanese.
    *   URL.
    *   One-sentence summary.
    *   Content Type.
    *   Language.
    *   Scores.
    *   Topics.
    *   Summary Body.

    Check: "Summary length should vary by content type". Tools category = "Standard articles: 450-650 characters (DEFAULT)".
    The drafted body is approx. 480 characters. Perfect.

    Final check on bolding: **Claude Code**, **Custom Slash Command**, **Web Search**.

    *Self-Correction on Content Type*: It's a "Tools" category because it evaluates/introduces a tool (Claude Code) in a specific workflow. Correct.
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