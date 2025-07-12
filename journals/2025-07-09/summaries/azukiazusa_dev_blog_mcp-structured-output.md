## MCP の Structured tool output を試してみる

https://azukiazusa.dev/blog/mcp-structured-output/

MCP の Structured tool output 機能により、ツールからの応答が構造化され、LLM のコンテキストと開発者体験が向上する。

[[MCP, Structured Output, Zod, TypeScript, LLM Context]]

Model Context Protocol (MCP) の 2025-06-18 より導入された「Structured tool output」機能は、ツールからの応答を構造化データとして扱えるようにするものです。これにより、LLM がツールの出力をより正確に理解し、開発者はスキーマ定義を通じて安全にツールを利用できるようになります。具体的には、TypeScript SDK で Zod を使用して `outputSchema` を定義し、ツールの出力に `structuredContent` フィールドを含めることで、構造化されたデータを返します。また、MCP Inspector を使用して、スキーマに準拠しない場合のバリデーションエラーを確認しながらテストを進めることができます。これは、LLM を活用したアプリケーション開発において、ツールの信頼性と開発効率を向上させる上で非常に重要です。

---

**編集者ノート**: MCP の Structured tool output は、LLM エージェント開発における「信頼性」と「開発体験」を劇的に改善する可能性を秘めています。特に、複雑なツール連携やデータ処理が求められるアプリケーションでは、スキーマ定義によるバリデーションがバグの温床となりがちな部分を事前に潰せるため、開発サイクルの短縮と品質向上に直結するでしょう。今後は、このような構造化されたインターフェースが、LLM エージェントと外部ツール間の標準的な連携方法になっていくと予想されます。これにより、より複雑で信頼性の高いAIアプリケーションが容易に構築できるようになるはずです。
