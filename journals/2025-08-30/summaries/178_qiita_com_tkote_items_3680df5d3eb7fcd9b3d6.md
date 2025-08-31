## MCP の Elicitation を GitHub Copilot Chat で試す #oci

https://qiita.com/tkote/items/3680df5d3eb7fcd9b3d6

GitHub Copilot ChatとMCPのElicitation機能を活用し、OCI Computeインスタンスの安全な操作を可能にするユーザー確認フローの実装方法を詳細に解説します。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 96/100 | **Overall**: 76/100

**Topics**: [[MCP, GitHub Copilot Chat, OCI Compute, LLM Agent, Elicitation]]

本記事は、Webアプリケーションエンジニアにとって極めて重要な課題である、GitHub Copilot Chatを通じて自然言語でOCI Computeインスタンスを安全に制御するMCPサーバーの構築手法を詳述しています。中心的な焦点は、LLMのハルシネーションや悪意あるプロンプトが意図しない、あるいは壊滅的なクラウド操作を引き起こす潜在的なリスクへの対策です。

このリスクを軽減するため、著者はMCPの「Elicitation」機能、すなわちサーバーがクライアント経由でユーザーに追加情報や確認を求める標準化されたメカニズムを効果的に活用。具体的には、Computeインスタンスの起動や停止といった変更を伴う操作を実行する前に、ユーザーに対して明確な「yes/no」の確認プロンプト（例：「インスタンス [name] を起動しますか? [y/N]」）が表示され、ユーザーが明示的にアクションを承認することを必須としています。

技術的な実装として、FastMCPライブラリを用いて`list()`と`action()`ツールを定義。`action()`ツール内では`ctx.elicit()`により確認メッセージを送信し、Pydantic BaseModelを継承した`UserInput`オブジェクトによるクライアントからの入力を待機します。GitHub Copilot Chatとの統合は、`.vscode/mcp.json`にMCPサーバーを「Command (stdio)」タイプとして設定することで実現され、Copilot Chatからこれらのツールを呼び出すことが可能になります。環境変数による柔軟な動作制御も考慮されています。

Webアプリケーションエンジニアにとってこの取り組みが重要である理由：AIエージェントがインフラやデプロイメントの自動化に深く関わるにつれ、安全性確保と意図しない結果の防止は不可欠です。本記事は、Elicitationという具体的なパターンを通じて、人間が意思決定プロセスに関与する、堅牢なAI駆動型ワークフローを構築する方法を提示。Copilot Chatのような日常的な開発者ツールに直接安全策を組み込むことで、OCIのような基幹クラウドインフラにおけるLLM主導の操作の信頼性を格段に高める実践的な解決策を提供しています。