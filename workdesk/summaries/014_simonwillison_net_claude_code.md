## My review of Claude’s new Code Interpreter, released under a very confusing name

https://simonwillison.net/2025/Sep/9/claude-code-interpreter/

Simon Willisonは、名称の混乱にもかかわらず、Claudeに新たに導入されたサーバーサイドのコード実行環境を詳細にレビューし、その機能、技術仕様、潜在的なリスクを解き明かす。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[Claude Code Interpreter, LLMコード実行環境, プロンプトインジェクション, データ分析, Node.jsサポート]]

Simon Willisonは、Anthropicが混乱を招く名称でリリースしたClaudeの新しいサーバーサイドコード実行環境を詳細に検証しています。これはChatGPTのCode Interpreterに匹敵する強力な機能であり、Webアプリケーションエンジニアにとって見過ごせない進化です。

この新機能は、以前のブラウザ内JavaScript実行とは異なり、専用のサーバーサイドコンテナ環境でPython 3.12.3とNode.js 18.19.1（Ubuntu 24.04、RAM 9GB、ディスク約5GB）を実行します。特筆すべきは、PyPIからの追加Pythonパッケージの`pip install`が可能な点です。これは、ChatGPT Code Interpreterにはない柔軟性を提供し、特定のライブラリを必要とするデータ分析やスクリプト実行において大きな利点となります。

一方で、インターネットアクセスは厳格な許可リスト（GitHubやPyPIなど）に限定されており、悪意のある命令が混入した場合のプロンプトインジェクションによるデータ流出リスクがあるため、機密データの扱いには注意が必要です。記事では、SQLiteデータベースの分析やExcelデータからのチャート再生成といった具体的なユースケースを通じて、その実用性と機能の堅牢性を示しています。ただし、ファイルサイズの上限が30MBと、ChatGPTの512MBと比較して低い点は留意すべきです。

Anthropicがこの強力な機能を「Upgraded file creation and analysis」という曖昧な名称で発表したことは、その真の価値を隠しており、より直感的な説明が求められています。しかし、この機能はLLMの真価を引き出すものであり、開発者のワークフローに深く統合されることで、データ処理や自動化の可能性を大きく広げると筆者は評価しています。特に、Web開発者にとってはNode.jsの利用が可能な点が魅力的です。