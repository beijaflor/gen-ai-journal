## This MCP Server Could Have Been a JSON File

https://materializedview.io/p/mcp-server-could-have-been-json-file

Critically examining the Model Context Protocol (MCP), the author argues that existing standards like OpenAPI and CLIs are sufficient for LLM-software interaction, rendering MCP largely redundant.

**Content Type**: 💭 Opinion & Commentary

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 92/100 | **Overall**: 88/100

**Topics**: [[LLM-ソフトウェア連携, Model Context Protocol (MCP), API設計, OpenAPI, CLIツール]]

MCP (Model Context Protocol)はLLMとソフトウェアを連携させる新しいプロトコルとして注目されていますが、この記事はMCPの存在意義に疑問を投げかけています。MCPはLLMに利用可能なソフトウェアとその使用方法を教え、LLMが外部ツールを呼び出す経路を提供することを目的としています。しかし、筆者はMCPの「Resources」「Tools」「Prompts」といった概念が曖昧であり、特にToolsはAPIのRPC定義と酷似していると指摘。既存のOpenAPI、gRPC、CLIといった標準的なインターフェース定義で十分であると論じます。

実際に、ChatGPTはMCPのツール定義をOpenAPI定義に問題なく変換できることを示し、OpenAPIがLLMに理解可能であることを強調しています。LLMのコンテキストウィンドウの制約や、多くのサービスが適切に文書化されていないといったMCPの存在意義とされる理由についても、筆者は懐疑的です。モデルの進化によりコンテキストウィンドウは拡大しており、不十分なAPI仕様の改善は、既存の標準に沿って行うべきだとしています。また、ツールの発見性についても、`AGENTS.md`や`openapi.json`など既存のメカニズムで対応可能であると主張します。

ウェブアプリケーションエンジニアにとって重要なのは、LLM連携のために新しいプロトコルに飛びつくのではなく、既存の堅牢で広く採用されている標準（OpenAPI、CLIなど）を活用することです。これにより、不必要な学習コストや技術的負債を避け、より持続可能で互換性の高いシステム構築に集中できます。結局のところ、プロトコルは単なる「配管」であり、重要なのはエージェントがタスクを効率的に完了できるかどうかに貢献する「優れたツール」を構築することであると結論付けています。