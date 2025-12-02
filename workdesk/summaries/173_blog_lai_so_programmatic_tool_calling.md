## AnthropicのProgrammatic Tool Calling（PTC）がAIエージェントのコンテキスト問題を根本的に解決

https://blog.lai.so/programmatic-tool-calling/

AnthropicがClaude APIの新機能「Programmatic Tool Calling（PTC）」を公開し、従来のTool Useが抱えるコンテキストウィンドウ肥大化の問題を抜本的に解決します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Programmatic Tool Calling, Claude API, コンテキスト管理, AIエージェント, Function Calling]]

Anthropicが発表したProgrammatic Tool Calling（PTC）は、ClaudeがTool呼び出しを含むPythonコードを生成し、これをAnthropic提供のサンドボックス内で実行するという画期的な機能です。従来のTool Useでは、Toolを呼び出すたびにClaudeが推論し、その結果がコンテキストウィンドウに追加され続けるため、トークン消費が増大し、モデルの精度低下（コンテキスト腐敗）を招く問題がありました。特に大量のデータ（例: Excelシート数千行）を扱うケースでこの課題が顕著でした。

PTCでは、ClaudeはTool呼び出しを含むPythonコードを一度だけ生成し、中間結果はサンドボックス内の変数に保持されるため、Claudeのコンテキストには`print()`で出力された最終結果のみが戻されます。これにより、著者の検証では約74%ものトークン削減が実現され、実行時間の短縮にも寄与することが示されました。この仕組みは、コンテキスト肥大化とそれに伴う推論精度の問題を根本的に解決するものです。

PTCの導入は、エージェント開発者にとって、コンテキストエンジニアリングにおける重要な問題解決技術として直接的な恩恵をもたらします。一方で、Claude CodeやCursorといったエディタの利用者にとっては、エディタ側がPTCを採用すれば、Toolを多数設定してもタスク失敗が起こりにくくなるという間接的なメリットがあります。

また、著者はCloudflareのCode Modeとの比較を行い、両者が異なる目的（PTCはコンテキスト肥大化回避、Code ModeはLLMのコード生成能力活用）から出発しながらも、「中間結果をLLMに戻さず、コード内に閉じ込める」という共通の設計に収束している点を指摘し、動的に生成したコードをサンドボックスで実行するモデルへの変化がAIエージェントの進化において重要な過渡期にあると結論付けています。