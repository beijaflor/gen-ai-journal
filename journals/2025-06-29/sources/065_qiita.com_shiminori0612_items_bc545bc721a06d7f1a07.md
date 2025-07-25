## [Claude Code で ESLint fix しちゃおう](https://qiita.com/shiminori0612/items/bc545bc721a06d7f1a07)

**AIでコード修正を自動化！Claude Code活用術**

この記事では、AIコーディングアシスタント「Claude Code」を使い、ESLintの自動修正機能（`--fix`）では対応できないコード修正を効率的に行う方法を紹介しています。筆者は、特に関数の返り値の型を明示する`@typescript-eslint/explicit-function-return-type`というルールを既存のコードベースに適用する際にClaude Codeを活用しました。

手作業では数百ファイルにも及ぶ修正が必要だったところ、Claude Codeに具体的な指示を与えることで、わずか数時間で513ファイルもの修正を完了させることができたと報告しています。

ただし、AIによる修正は完璧ではな��、手動での微調整や、修正後に新たな型エラーが発生することもあったため、AIの生成したコードは必ず自身で確認することの重要性を強調しています。この記事は、AIを単なるツールとして使うだけでなく、その特性を理解し、うまく付き合いながら開発効率を向上させるための一つの実践例を示しています。