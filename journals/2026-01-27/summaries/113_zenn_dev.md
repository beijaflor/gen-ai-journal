## Claude Codeにお遣いさせて見えてきた、買い物エージェントの一つの解

https://zenn.dev/wmoto_ai/articles/ai-shopping-human-in-the-loop

購買履歴に基づいたルールベースの予測と、**Claude Code Hooks**による厳格な権限制御を組み合わせた、実用的な買い物エージェントの構築手法を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Claude Code, AIエージェント, Human-in-the-Loop, セキュリティガードレール, GitHub Actions]]

ネットスーパーの買い物自動化における、AIエージェントの設計原則と実装を解説する記事です。**Claude Code**をメインエンジンに採用し、過去4年分の購買履歴を活用した統計的な「先読み」と、人間が**GitHub Issues**上で最終確認を行う**Human-in-the-Loop (HITL)**を組み合わせています。

技術的な核心は、**Claude Code Hooks**（`PreToolUse`と`Stop`）を用いた多重のガードレール構築にあります。AIに直接ブラウザを操作させず、ホワイトリスト化された専用CLIのみを実行可能に制限。さらに、実行前後の検証スクリプトによって、検索結果にない商品の勝手な購入や不正なシェルコマンドの実行をコードレベルでブロックしています。

著者は、曖昧な要求への対応はAIが得意とする一方で、定期的な購入パターンの予測はルールベースの方が適していると指摘しており、両者の使い分けが実用性を高める鍵であると主張しています。**Claude Code**を活用したセキュアなエージェント実装や、安全性と利便性を両立させた自動化ワークフローを構築したいエンジニアにとって、具体的かつ示唆に富むガイドです。