## Claude Code Agent Skills 入門

https://blog.serverworks.co.jp/claude-code-agent-skills-guide

Claude Codeの「Agent Skills」機能を活用し、プロジェクト固有のルールを自動適用させつつコンテキスト消費を劇的に削減する手法を詳説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 91/100 | **Overall**: 72/100

**Topics**: [[Claude Code, Agent Skills, AIエージェント, プロンプトエンジニアリング, コンテキスト最適化]]

本記事は、**Claude Code**の重要な拡張機能である**Agent Skills**の基本概念から具体的な実装方法までを解説しています。**Agent Skills**は、AIエージェントに対してプロジェクト固有のコーディング規約やAPIのレスポンス形式などの「専門的なマニュアル」を動的に提供する仕組みです。従来の`CLAUDE.md`やプロンプトによる指示との最大の違いは、エージェントが必要な時だけ自動的にスキルを読み込む「プログレッシブディスクロージャー」にあります。これにより、コンテキストウィンドウの消費を大幅に抑制し、16,000トークンの消費をわずか500トークン程度まで削減できる実例が示されています。

具体的なユースケースとして、APIレスポンスの形式統一、コードレビューの自動化、`allowed-tools`を用いた読み取り専用の安全なコード調査モードなどが挙げられています。スキルの定義は`SKILL.md`というマークダウン形式で行い、個人用（`~/.claude/skills/`）またはプロジェクト用（`.claude/skills/`）として共有可能です。また、この仕様は**オープンスタンダード**として公開されており、**Cursor**や**VS Code**、**GitHub Copilot**など、多くの主要なAIツール間で再利用できる点もエンジニアにとって大きな魅力です。

**Claude Code**や**Cursor**を日常的に利用し、定型的な指示の自動化やコンテキストの最適化を図りたいエンジニアにとって必読の内容です。