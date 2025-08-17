## Claude CodeにVerylのコードを書かせてみた

https://zenn.dev/dalance/articles/6463b2fcae7130

Claude CodeがModel Context Protocol (MCP) とLanguage Server Protocol (LSP) を活用し、新しいハードウェア記述言語Verylのコード生成からデバッグまでを遂行できることを実証しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 74/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[AIコーディング, ハードウェア記述言語, Language Server Protocol, Model Context Protocol, AIエージェントデバッグ]]

この記事は、Claude Codeが開発中の新しいハードウェア記述言語Verylのコードを生成し、デバッグする実験を報告しています。注目すべきは、AIがModel Context Protocol (MCP) とそのクライアントツールlsmcpを介してVerylのLanguage Server (veryl-ls) と連携し、このタスクを達成した点です。

実験では、まず加算器モジュールのVerylコードをClaude Codeに作成させ、次に1クロック遅延のロジックを追加する際に意図的に構文エラーを発生させました。Claude Codeはlsmcpを通じてveryl-lsからコンパイルエラーの診断情報を受け取り、さらに既存のVerylコード（delay.veryl）を参照することで、正しくエラーを修正し、コードをフォーマットしました。

この実験がウェブアプリケーションエンジニアにとって重要なのは、AIコーディングの適用範囲が一般的なプログラミング言語に限定されない可能性を示唆しているからです。LSPとMCPを組み合わせることで、AIは既存の言語サーバーの機能を活用し、新たな言語やドメイン固有言語（DSL）、あるいは社内独自のフレームワークにすら適応し、コード生成からエラー修正までを一貫して行えるようになります。これは、普段慣れない言語やレガシーコードベース、特殊なドメインにおける開発において、AIが強力なアシスタントとなり得ることを意味します。AIがLSPから得たフィードバックに基づいて自律的に修正する能力は、開発ワークフローの効率を劇的に向上させる潜在力を持っています。