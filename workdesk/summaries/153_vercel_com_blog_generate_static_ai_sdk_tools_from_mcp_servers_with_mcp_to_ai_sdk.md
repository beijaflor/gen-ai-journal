## Addressing security and quality issues with MCP tools in AI Agent

https://vercel.com/blog/generate-static-ai-sdk-tools-from-mcp-servers-with-mcp-to-ai-sdk

Vercelは、動的なModel Context Protocol (MCP) ツールが引き起こすAIエージェントのセキュリティ、コスト、品質問題を解決する静的AI SDKツール定義生成CLI「mcp-to-ai-sdk」をリリースしました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Agent Tools, Model Context Protocol (MCP), AI SDK, AI Security, Static Code Generation]]

Vercelは、AIエージェントのツール連携に利用されるModel Context Protocol (MCP) が抱えるプロダクション環境での課題を解決するCLIツール「mcp-to-ai-sdk」を発表しました。MCPはエージェント間のツール呼び出しを連携する標準プロトコルとして普及していますが、動的なツール定義はセキュリティ、コスト、品質面で予期せぬ問題を引き起こす可能性があります。

具体的には、MCPサーバーの変更によってツールの説明が更新され、プロンプトインジェクションを引き起こしたり、リードオンリーだったツールが意図せずデリート機能を追加し、権限昇格につながったりするリスクが挙げられます。また、GitHubのMCPサーバーのようにツール定義だけで膨大なトークンを消費し、不要なコストやレイテンシーを発生させる問題、さらにはツール名の変更や説明の曖昧さによるエージェントの動作不安定化も指摘されていました。

これらの課題に対し、「mcp-to-ai-sdk」は、`shadcn/ui` のアプローチをAIツールに適用します。任意のMCPサーバーからツール定義をダウンロードし、ローカルでカスタマイズ可能なAI SDK互換の静的ツールを生成します。これにより、ツール定義がコードベースに組み込まれ、バージョン管理下で変更がレビューされるようになります。

このアプローチの最大の利点は、以下に集約されます。
1.  **セキュリティ**: ツール定義がコードレビューで管理されるため、プロンプトインジェクションなどのリスクを軽減します。
2.  **パフォーマンス**: 必要なツールのみをエージェントのコンテキストに含めることで、不要なトークン消費とレイテンシーを削減します。
3.  **信頼性**: ツールスキーマと説明が安定し、上流の変更による予期せぬ動作を防ぎます。
4.  **カスタマイズ性**: モデルに最適化された説明の調整や、引数の制限、認証ロジックの追加が可能になります。

「mcp-to-ai-sdk」は、MCPの持つ発見とプロトタイピングの利点を維持しつつ、プロダクションシステムで不可欠なセキュリティと信頼性を両立させる、AIアプリケーション開発の成熟に向けた重要な一歩となります。