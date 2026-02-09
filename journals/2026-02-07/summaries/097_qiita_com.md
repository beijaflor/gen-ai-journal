## AIエージェントと協働するオフィスワーク2026 #ClaudeCode

https://qiita.com/hirokidaichi/items/382920eb22ed3e645257

AIエージェント「Claude Code」と自作CLIツール群を組み合わせ、複数のSaaSを横断してオフィス業務を自律的に処理する高度な自動化アーキテクチャを提案する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, AI Agent, CLI Tools, Workflow Automation, n8n]]

エンジニアの広木大地氏が、**Claude Code**を中心としたAIエージェントによる次世代のオフィスワーク自動化アーキテクチャを詳説しています。AIが判断を行い、実行は自作の**CLIツール**に委譲する「3レイヤー構造（データ、ワークフロー、対話）」を提唱。特筆すべきは、現在の主流である**MCP (Model Context Protocol)**が抱える「コンテキスト消費の増大」という課題に対し、Unix思想に基づいた軽量なCLI連携を選択することで、トークン節約と柔軟なパイプライン構築を両立させている点です。

具体的な実装例として、**Notion**（noti）、**Slack**（slakky）、**Google Workspace**（gog）などのAPIを抽象化した自作CLI群を紹介。これらを**Claude Code**の「Skill」として定義することで、「メール返信案の作成とカレンダー調整の同時実行」や「過去の議事録からの意思決定の抽出」といった、複雑な文脈理解を伴う業務を自律的に処理しています。

また、定型作業は**n8n**で「結晶化」させ、判断が必要な領域のみを対話レイヤーに残すという運用設計、および**SKILL.md**による判断基準の言語化手法など、開発者が実務で**Agentic Workflow**を構築するための極めて具体的かつ高度な知見が提示されています。AIを単なるチャットツールとしてではなく、エンジニアリングによって「業務を実行する主体」へと昇華させたい開発者にとって、最良のリファレンスとなる記事です。