 thoughtful
Claude Code Sub-agents Hands-on (Claude Codeサブエージェントハンズオン).
https://tech.iimon.co.jp/entry/2025/12/22
Japanese.
Claude Code's sub-agents feature.
Overview of sub-agents, step-by-step creation process, practical test (TODO app with complex architecture), results (cost/time/structure), and key takeaways (orchestration via `CLAUDE.md`).

        *   Content Type: Tools (specifically about a feature of a developer tool).
        *   Signal: 4 (Direct experience, though secondary analysis of an official tool).
        *   Depth: 3 (Shows workflow and setup, result analysis).
        *   Unique: 3 (Practical implementation of sub-agents is a trending topic).
        *   Practical: 4 (Shows how to actually use and orchestrate them).
        *   Anti-Hype: 4 (Mentions cost and time/slowness).

    *   *Title*: Claude Codeサブエージェントハンズオン
    *   *URL*: https://tech.iimon.co.jp/entry/2025/12/22
    *   *One-sentence summary*: Claude Codeのサブエージェント機能を活用し、オーケストレーターを通じた高度なTODOアプリ開発プロセスの実践結果を報告する。 (Report the practical results of developing a sophisticated TODO app by leveraging Claude Code's sub-agent feature through an orchestrator.)

    *   *Summary Body (Drafting in Japanese)*:
        Claude Codeの「サブエージェント」機能を実際に試し、その設定方法から実用性までを検証したハンズオン記事。サブエージェントは、特定の専門分野（DDD、TDD、React等）を持つ独立したAI人格であり、メインの会話とは別のコンテキストウィンドウで動作する。
        筆者はまず、DDDやクリーンアーキテクチャ、コードレビューなど8種類の専門エージェントを作成。当初、単一のプロンプトではサブエージェントが自動起動しなかったが、`CLAUDE.md`を「オーケストレーター」として定義し、指示をサブエージェントへ委任・レビューさせるフローを明示したところ、意図した通りの協調動作が確認された。
        結果として、DDDやクリーンアーキテクチャに基づいた高度なディレクトリ構成を持つTODOアプリが40分ほどで完成。コストは約19ドルと安くないが、複雑な設計を伴う開発を自律的に進める能力が示された。筆者は、単にエージェントを用意するだけでなく、`CLAUDE.md`等で明示的に役割とフローを定義することが、サブエージェントを効果的に活用する鍵であると指摘している。

    *   *Validation against requirements*:
        *   Target: Web application engineers.
        *   Focus: What happened/Why it matters.
        *   Tone: Direct, active voice.
        *   Character count: Medium article (around 800-1200 chars). *Wait, the drafting above is a bit short. Let's expand to hit the 800-1200 range while maintaining substance.*

    *   *Expansion Strategy*:
        *   Detailed step of creation.
        *   The specific role of `CLAUDE.md`.
        *   Breakdown of the output structure (Atomic Design + DDD).
        *   Cost vs. Time trade-off analysis from the author's perspective.

    *   *Refined Summary Body*:
        本記事は、Anthropicが提供するCLIツール「Claude Code」の強力な機能である「サブエージェント」を実際に導入し、高度な設計パターンに基づいたアプリケーション開発を完遂させるまでのプロセスを詳解している。サブエージェントとは、特定の専門分野とツール、システムプロンプトを持つ独立したAI人格であり、メインエージェントからタスクを委譲されることで、個別のコンテキストで動作する。

        検証において筆者は、DDD、TDD、React、TypeScript、クリーンアーキテクチャなどの専門家、およびコーディング・設計・テストのレビュー担当という計8つのサブエージェントを構築した。特筆すべきは、サブエージェントを単に作成するだけでは「適切な判断」による自動起動が十分に行われなかった点である。これに対し、筆者はプロジェクトのガイドラインとなる`CLAUDE.md`に、メインエージェントを「オーケストレーター（指揮者）」として振る舞わせる定義を追記。サブエージェントへの委任、レビューの実施、結果の統合というワークフローを明示することで、高度な協調動作を実現させた。

        この構成でTODOアプリの開発を試みた結果、DDDのエンティティやユースケース、Atomic Designに基づくコンポーネント、DIコンテナを含む、実戦レベルの堅牢なディレクトリ構成（計41ファイル）が生成された。完成までに約40分、コストは約19.33ドルを要したが、人間がゼロからこのアーキテクチャを実装する労力と比較すれば、驚異的なスピードであると筆者は評価している。

        結論として、サブエージェントの真価を引き出すには、個別の専門性を定義するだけでなく、`CLAUDE.md`等を通じて「どのタイミングでどのエージェントを使い、どう品質を担保するか」というメタな指示出し（オーケストレーションの設計）が不可欠であることが示唆されている。これは、AIエージェントを単なる補完ツールではなく、開発プロセス全体を自律的に回す「チーム」として機能させるための重要な知見である。

    *   Title: Claude Codeサブエージェントハンズオン
    *   URL: https://tech.iimon.co.jp/entry/2025/12/22
    *   One-sentence summary: Claude Codeのサブエージェント機能を活用し、オーケストレーターを通じた高度なTODOアプリ開発プロセスの実践結果を報告する。
    *   Content Type: ⚙️ Tools
    *   Scores: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
        *   Main Journal: 0.25*4 + 0.3*3 + 0.3*3 + 0.4*4 + 0.15*4 = 1.0 + 0.9 + 0.9 + 1.6 + 0.6 = 5.0 -> 100 scale: 5.0*20 = 100? No, standard average * 20 is easier. Let's use the weightings.
        *   Signal (4*0.25=1.0) + Depth (3*0.3=0.9) + Unique (3*0.3=0.9) + Practical (4*0.4=1.6) + Anti-Hype (4*0.15=0.6) = 5.0 (out of 5.0) -> 100. *Wait, let's re-calculate.*
        *   Main Journal (Tools weighting): (4*0.25 + 3*0.30 + 3*0.30 + 4*0.40 + 4*0.15) / 5.0 * 100 = (1.0 + 0.9 + 0.9 + 1.6 + 0.6) / 5 * 100 = 5.0 / 5 * 100 = 100. *Is this too high?* Let's check the score descriptions. Signal 4, Depth 3, Unique 3, Practical 4, Anti-Hype 4. Total raw points = 18. Average = 3.6. 3.6*20 = 72.
        *   Main: (1.0+0.9+0.9+1.6+0.6) * 20 = 100. Something is wrong with my math or the scale. The framework says "sum of (score * weight)". Max possible is 5. So yes, 5.0 * 20 = 100.
        *   Actually, let's look at the weights again. 0.25+0.3+0.3+0.4+0.15 = 1.4. Ah, the weights don't sum to 1.0. 25%+30%+30%+40%+15% = 140%. I should divide by 1.4 or just use the weighted average.
        *   Calculation: (4*0.25 + 3*0.3 + 3*0.3 + 4*0.4 + 4*0.15) / 1.4 * 20 = 5.0 / 1.4 * 20 ≈ 71.4.
        *   Annex Potential: (4*0.20 + 3*0.25 + 3*0.45 + 4*0.25 + 4*0.20) / 1.35 * 20 = (0.8 + 0.75 + 1.35 + 1.0 + 0.8) / 1.35 * 20 = 4.7 / 1.35 * 20 ≈ 69.6.
        *   Overall: (4+3+3+4+4)/5 * 20 = 72.

    *   *Note*: The score calculation logic in the prompt is a bit ambiguous regarding the sum of weights. I will assume the intended method is `(Sum of (Score * Weight)) / (Sum of Weights) * 20`.

    *   Weights for Tools:
        *   Main: Signal 0.25, Depth 0.30, Unique 0.30, Practical 0.40, Anti-Hype 0.15 (Sum = 1.4)
        *   Annex: Signal 0.20, Depth 0.25, Unique 0.45, Practical 0.25, Anti-Hype 0.20 (Sum = 1.35)
    *   Scores: S:4, D:3, U:3, P:4, A:4
    *   Main Calculation: (1.0 + 0.9 + 0.9 + 1.6 + 0.6) = 5.0. 5.0 / 1.4 * 20 = 71.4 -> 71
    *   Annex Calculation: (0.8 + 0.75 + 1.35 + 1.0 + 0.8) = 4.7. 4.7 / 1.35 * 20 = 69.6 -> 70
    *   Overall: 3.6 * 20 = 72.

    Let's check the summary body length. 800-1200 characters requested.
    My draft is around 650 characters. I need to add more detail about the specific sub-agents and the tree structure/result analysis.

    *Expanded Summary Body*:
    本記事は、Anthropicが提供するCLIツール「Claude Code」の強力な機能である「サブエージェント」を導入し、高度な設計パターンに基づいたアプリケーション開発を完遂させるまでの実証プロセスを詳解している。サブエージェントとは、特定の専門分野、ツール権限、独自のシステムプロンプトを持つAI人格であり、メインエージェント（Claude Codeのセッション）から特定のタスクを切り出して委譲されることで、メインのコンテキストを消費せずに並列的あるいは独立した推論を行う仕組みである。

    筆者は検証にあたり、DDD（ドメイン駆動設計）、TDD（テスト駆動開発）、React、TypeScript、クリーンアーキテクチャの各専門家、およびコード・設計・テストのレビュー担当という計8つの専用サブエージェントを構築した。設定プロセスでは、各エージェントに対してOpusやSonnetといったモデルの選択、使用ツールの許可、役割に応じたシステムプロンプト（mdファイル）の生成手順を具体的に示している。

    実証における最大の知見は、サブエージェントを単に作成するだけでは期待通りに自律動作しないという点だ。筆者は、プロジェクトの行動規範を定義する`CLAUDE.md`を更新し、メインエージェントを「オーケストレーター（指揮者）」として振る舞わせる指示を明記した。具体的には、「ユーザーの指示を適切なサブエージェントに委任する」「回答をレビュー専用エージェントに検証させる」といったワークフローを定義することで、エージェント間の協調動作を誘発することに成功した。

    このオーケストレーションにより生成されたTODOアプリは、ドメイン層、アプリケーション層、インフラ層が明確に分離され、Atomic Designを採用したプレゼンテーション層や、DI（依存性の注入）コンテナまでをも備えた計41ファイルに及ぶ極めて堅牢な構成となった。完了までに約40分、コストは約19.33ドルを要したが、人間が同様の品質でゼロからアーキテクチャを設計・実装する時間を考えれば、AIによる「自律的なチーム開発」の有用性を強く裏付ける結果となっている。

    筆者はまとめとして、サブエージェントの活用は単なるタスク分担に留まらず、`CLAUDE.md`等を通じた「メタな指示出し（意思決定フローの設計）」こそが、AIを単なる補完ツールから自律的な開発パートナーへと昇華させる鍵であると結論付けている。開発者にとっては、いかにしてAIに「役割」と「プロセス」を正しく与えるかという、エージェント・オーケストレーションの重要性を再認識させる内容である。

    (Character count check: ~1050 characters. Perfect.)

    *   Title/URL formatting.
    *   One-sentence summary starts with active verb.
    *   Content Type & Scores.
    *   Topics (5 specific tags).
    *   Japanese body with correct length and objectivity.

    Topics: Claude Code, サブエージェント, クリーンアーキテクチャ, エージェント・オーケストレーション, CLAUDE.md

    Wait, the one-sentence summary should start with an active verb.
    "Claude Codeのサブエージェント機能を活用し..." -> "検証する" at the end? Or "活用して...構築するプロセスを報告する".
    Better: "報告する" at the end, but the instructions say "Start with a strong, active verb." In Japanese, verbs are usually at the end. I will use a nominalized verb or a strong active phrasing like "実証する、..." or "検証・報告する、...".
    Let's use: "実証する：Claude Codeのサブエージェント機能を活用し、オーケストレーターを通じた高度なTODOアプリ開発プロセスの実践結果を。" (Demonstrate: results of...) or "検証する、Claude Codeの...".
    The English equivalent "Demonstrate/Report/Explore..." translates naturally with the verb at the end in Japanese. Let's start with the object and end with a strong verb.
    "報告する：Claude Codeのサブエージェント機能を活用し、オーケストレーターを通じた高度なTODOアプリ開発プロセスの実践結果を。" -> This matches.

    Final check on scores:
    Signal: 4 (Direct experience)
    Depth: 3 (Solid flow, result provided)
    Unique: 3 (Implementation detail)
    Practical: 4 (Config and CLAUDE.md tip)
    Anti-Hype: 4 (Real cost/time mentioned)
    Main: 71, Annex: 70, Overall: 72. Correct.

    Topics: [[Claude Code, サブエージェント, エージェント・オーケストレーション, クリーンアーキテクチャ, CLAUDE.md]]

    Ready.
## Claude Codeサブエージェントハンズオン

https://tech.iimon.co.jp/entry/2025/12/22

報告する：Claude Codeのサブエージェント機能を活用し、オーケストレーターを通じた高度なTODOアプリ開発プロセスの実践結果を。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[Claude Code, サブエージェント, エージェント・オーケストレーション, クリーンアーキテクチャ, CLAUDE.md]]

本記事は、Anthropicが提供するCLIツール「Claude Code」の強力な機能である「サブエージェント」を導入し、高度な設計パターンに基づいたアプリケーション開発を完遂させるまでの実証プロセスを詳解している。サブエージェントとは、特定の専門分野、ツール権限、独自のシステムプロンプトを持つAI人格であり、メインエージェント（Claude Codeのセッション）から特定のタスクを切り出して委譲されることで、メインのコンテキストを消費せずに並列的あるいは独立した推論を行う仕組みである。

筆者は検証にあたり、DDD（ドメイン駆動設計）、TDD（テスト駆動開発）、React、TypeScript、クリーンアーキテクチャの各専門家、およびコード・設計・テストのレビュー担当という計8つの専用サブエージェントを構築した。設定プロセスでは、各エージェントに対してOpusやSonnetといったモデルの選択、使用ツールの許可、役割に応じたシステムプロンプト（mdファイル）の生成手順を具体的に示している。

実証における最大の知見は、サブエージェントを単に作成するだけでは期待通りに自律動作しないという点だ。筆者は、プロジェクトの行動規範を定義する`CLAUDE.md`を更新し、メインエージェントを「オーケストレーター（指揮者）」として振る舞わせる指示を明記した。具体的には、「ユーザーの指示を適切なサブエージェントに委任する」「回答をレビュー専用エージェントに検証させる」といったワークフローを定義することで、エージェント間の協調動作を誘発することに成功した。

このオーケストレーションにより生成されたTODOアプリは、ドメイン層、アプリケーション層、インフラ層が明確に分離され、Atomic Designを採用したプレゼンテーション層や、DI（依存性の注入）コンテナまでをも備えた計41ファイルに及ぶ極めて堅牢な構成となった。完了までに約40分、コストは約19.33ドルを要したが、人間が同様の品質でゼロからアーキテクチャを設計・実装する時間を考えれば、AIによる「自律的なチーム開発」の有用性を強く裏付ける結果となっている。

筆者はまとめとして、サブエージェントの活用は単なるタスク分担に留まらず、`CLAUDE.md`等を通じた「メタな指示出し（意思決定フローの設計）」こそが、AIを単なる補完ツールから自律的な開発パートナーへと昇華させる鍵であると結論付けている。開発者にとっては、いかにしてAIに「役割」と「プロセス」を正しく与えるかという、エージェント・オーケストレーションの重要性を再認識させる内容である。