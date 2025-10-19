## MCP のツールアノテーションでユーザーにヒントを提供する

https://azukiazusa.dev/blog/mcp-tool-annotations/

Model Context Protocol (MCP) は、LLMが外部ツールを呼び出す際にユーザーにツールの動作に関するヒントを提供するアノテーション機能を導入し、TypeScript SDKによる設定方法とClaude Codeでの表示を実演する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Model Context Protocol (MCP), Tool Annotations, LLM Agent Development, User Experience (UX) for AI Tools, TypeScript SDK]]

Model Context Protocol (MCP) は、LLMが外部ツールと対話するための標準的な枠組みを提供します。LLMがユーザーの許可なしにツールを実行し、予期せぬ動作を引き起こす可能性を考慮し、MCPはツールの動作に関するヒントをユーザーに提供する「ツールアノテーション」の仕組みを導入しました。これにより、ユーザーはツールの機能を事前に理解し、呼び出しの是非を判断できるようになります。

主なアノテーションには、ツールの人間が読める名前を示す`title`、データ変更がないことを示す`readOnlyHint`、破壊的な変更の可能性を示す`destructiveHint`、冪等性を示す`idempotentHint`、そして外部エンティティとの相互作用を示す`openWorldHint`があります。特に`readOnlyHint`は、ユーザーに安全性を伝える上で重要です。ただし、これらのアノテーションはあくまで「ヒント」であり、ツールが動作を保証するものではないため、セキュリティ判断に用いるべきではありません。

記事では、TypeScript SDKを使用して簡単なTODOリスト管理MCPサーバーを構築し、`add_todo`ツールと`list_todos`ツールにそれぞれアノテーションを設定する具体的なコード例を示しています。例えば、`list_todos`ツールには`readOnlyHint: true`を設定しています。このサーバーをClaude Codeクライアントに登録すると、ツール一覧画面でアノテーションで設定した`title`が表示され、`readOnlyHint: true`のツールには「(read-only)」と明示されることが確認できます。

この機能は、LLMエージェントがユーザーに透明性を提供し、より信頼性の高いインタラクションを実現する上で極めて重要です。開発者は、これらのアノテーションを適切に設定することで、ユーザーがツールの意図を正確に把握し、安心してAIと協調作業できるような、質の高いAIアプリケーションを構築するための重要な手がかりを得られます。