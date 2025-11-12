## Claude Code に「RBS を生成するコード」を書かせたら便利だった #Ruby

https://qiita.com/tomoasleep/items/6b185799f203564161ed

Claude Codeを活用することで、Rubyのメモ化代入に関するRBS定義の生成が自動化され、`prism`や`rbs` gemを用いることで開発者の型定義記述の負担を大幅に軽減できる。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Ruby, RBS, AI Code Generation, Static Analysis, Development Workflow Automation]]

著者は、Ruby開発においてrbs-inlineとSteepを利用しているが、メモ化代入のような頻繁に使うRubyの慣用句に対してRBS（Ruby Type Signature）を手動で記述する手間が課題であると述べています。特に、インスタンス変数の型定義が必要となるケースでは、この冗長な作業を自動化したいと考えました。

この課題に対し、著者はClaude Codeを活用してRBS定義を生成するスクリプトを書かせたところ、非常に効果的であったと報告しています。成功の鍵は、AIへの指示において解析に使うgemを具体的に指定することです。特に、Rubyコードの解析には`prism` gem、Rubyの型やクラス構造の解析には`rbs` gemの使用を推奨しています。これにより、正規表現ベースの保守性の低いコードが生成されるのを防ぎ、より堅牢なスクリプトを得られると強調しています。

記事では、`prism`がRubyコードのパーサーとしてメソッド名の一覧生成に役立つこと、`rbs` gemがクラスの継承関係などの型情報を効率的に解析できることを具体的なコード例を挙げて説明しています。また、`rbs` gemがRubyコードを直接解析できないため、`rbs-inline`で一度RubyコードからRBSファイルを生成してから`rbs` gemに解析させるワークフローが有効であると解説。さらに、スクリプト自身が生成したRBSファイルを次回の解析に含めないよう除外することの重要性を指摘し、実行結果の冪等性確保を促しています。

実運用においては、これらのRBS生成スクリプトをRakeタスクとしてまとめ、`sig/generated-by-scripts`のような特定のディレクトリに出力することで、管理と実行が容易になることを提案しています。これにより、開発者は煩雑な型定義の手間から解放され、より効率的にRubyアプリケーション開発を進めることが可能となります。