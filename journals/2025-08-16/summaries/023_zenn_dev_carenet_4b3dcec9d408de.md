## [2025年8月8日] ついにGPT-5！！！……うーん？ (週刊AI)

https://zenn.dev/carenet/articles/4b3dcec9d408de

GPT-5の発表があったものの、オープンソースのローカルLLMであるgpt-ossがより実践的なゲームチェンジャーとして浮上し、Claude Codeの改善策やGoogleの新機能などAI開発ツールの進展が続いた一週間を振り返ります。

**Content Type**: Tools
**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GPT-5, gpt-oss, Claude Code, LLM, AI開発ツール]]

今週はGPT-5の発表がありましたが、筆者は予想の範囲内で「AGIらしさは感じられなかった」と評価しています。むしろ、真のゲームチェンジャーとして浮上したのはOpenAIが提供するオープンソースのローカルLLM「gpt-oss」です。これはo4-mini/o3-mini相当の性能を持ち、API料金を気にせずローカルで自由に改造・利用できるため、スタートアップや資金力のない企業にとって非常に大きな意味を持ちます。これにより、独自モデルとの密結合に頼っていたサービスは厳しい競争に直面し、今後はAIモデルそのものよりもドメイン知識やニッチな特徴を加えた付加価値サービスへのシフトが加速するでしょう。

また、AnthropicからはClaude Opus 4.1の発表に加え、エンジニア待望のClaude Code向けセキュリティレビュー機能が追加され、開発ワークフローにおける実用性が大きく向上しました。GoogleもGemini CLI GitHub ActionsやJulesの正式リリース、Geminiへの学習支援モード追加、さらにワールド生成プラットフォーム「Genie 3」など、全方位で圧倒的なリリーススピードを見せつけています。

さらに注目すべきは、一部で話題になっていたClaude Codeの性能低下問題に対するコミュニティの動きです。特に「Serena」という無料ツールがその解決策として大きく注目されました。Serenaは、Claude Codeにドキュメントを直接読み込ませるのではなく、効率的なMulti-Context Prompting (MCP) を介することで、トークン効率を劇的に改善し、Claude Codeの推論能力を大幅に向上させます。これにより、性能低下を感じていたエンジニアはバージョンダウンの必要なく、Claude Codeをより賢く活用できるようになります。

GPT-5が期待ほどのAGIを見せなかったとはいえ、gpt-ossによるローカルLLMの普及、既存AI開発ツールの機能強化と課題解決は、Webアプリケーションエンジニアの生産性や開発アプローチに直接的な影響を与える「Big Week」であったと言えるでしょう。