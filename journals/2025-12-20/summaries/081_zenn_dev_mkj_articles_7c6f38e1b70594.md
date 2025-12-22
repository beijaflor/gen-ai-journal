## AIフレンドリーなNotebook環境「marimo」で、AIコーディングの課題を解決

https://zenn.dev/mkj/articles/7c6f38e1b70594

松尾研究所のテックブログが、AIコーディングツールとの相性が悪いJupyter Notebookの問題を解決する、.pyベースのリアクティブNotebook環境「marimo」を紹介し、その機能とAI開発における重要性を解説しています。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[marimo, Jupyter Notebook, AIコーディングツール, リアクティブプログラミング, VS Code]]

Jupyter Notebook (.ipynbファイル) は内部的にJSON形式で保存されるため、CursorやClaude CodeなどのAIコーディングツールで編集しようとすると、構造が壊れたり、大量の差分が発生したりと相性が悪いという問題が指摘されています。本記事は、この課題を解決する次世代のNotebook環境として、marimoとVS CodeのPython Interactive Windowを紹介しています。

著者は、.ipynbファイルがAIツールと相性が悪い主な理由として、JSON構造による差分の複雑さ、コードと実行結果が混在することによるノイズ、そして行単位編集の困難さを挙げています。AIがコードの一部を修正するだけでも、JSON全体を正確に操作する必要があり、エラーにつながりやすいと解説しています。

この問題への解決策として紹介されているのが「marimo」です。marimoはJupyter Notebookと同様のインタラクティブな開発体験を提供しながら、内部的には純粋なPythonファイルとして保存されます。これにより、通常のPythonコードと同様にAIツールでの編集が可能になり、JSON操作なしでセル追加や関数修正が指示できるようになります。marimoの主な特徴は以下の通りです。
1.  **AIツールで編集しやすい**: セルが`@app.cell`デコレータで定義された関数として表現されるため、通常の.pyファイルと同じ感覚でAIによるコード補完や修正提案が受けられます。
2.  **リアクティブ実行**: セルの変更に依存するセルが自動的に再実行されるため、「上から順に実行し直す」手間が不要で、意図しない変数の残留や上書きを防げます。
3.  **Gitフレンドリー**: 純粋な.pyファイルであるため、Gitでの差分比較やマージが容易になり、チーム開発での利便性が向上します。
4.  **複数の実行形態**: Notebookとしての対話的開発に加え、スクリプト実行やWebアプリとしてのデプロイも可能です。スライダーなどのインタラクティブなUI要素も標準搭載されています。

既存の.ipynbファイルを`marimo convert`コマンドで簡単に変換できるほか、VS Code拡張機能を利用することで、VS Code上でmarimoノートブックとしてインタラクティブに開発できる点も強調されています。また、VS Codeユーザー向けに、.pyファイルに`# %%`を追加するだけでNotebookのように実行できるPython Interactive Windowも代替案として紹介されています。

著者は、.ipynbファイルもAIコーディングツールでの編集が徐々に可能になりつつあるものの、まだ動作が不安定な面があるとし、marimoやPython Interactive WindowのようなAIフレンドリーなツールが、Notebookでの試行錯誤とAI活用の両立を最大限に促進すると期待を述べています。