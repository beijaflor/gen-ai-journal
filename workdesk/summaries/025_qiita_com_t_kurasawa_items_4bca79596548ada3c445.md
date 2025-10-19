## Chrome DevTools MCP を使ってAIにブラウザ操作とエラーデバッグをさせてみる（Gemini CLI 環境構築手順付）

https://qiita.com/t-kurasawa/items/4bca79596548ada3c445

GoogleのChrome DevTools MCPとGemini CLIを組み合わせることで、AIがブラウザを直接操作し、フロントエンドのエラーデバッグまで自律的に行う新しい開発ワークフローが実現します。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[Chrome DevTools MCP, Gemini CLI, AIブラウザ自動化, フロントエンドデバッグ, AIエージェント]]

この記事は、Googleがプレビュー公開したChrome DevTools MCPをGemini CLIと組み合わせることで、生成AIがブラウザを直接操作し、エラーデバッグまで自律的に行えるようになる新しい開発ワークフローを紹介しています。これにより、ターミナルでの指示、ブラウザでの表示確認、エラーコードのAIへの伝達といった開発中の反復作業が大幅に削減され、フロントエンド開発に不可欠なツールになる可能性を提示しています。

著者は、Claude Code CLIやCodeX CLIに似たAIエージェントであるGemini CLIの環境構築から始め、Chrome DevTools MCPの設定手順を詳細に解説しています。プロジェクトローカルおよびグローバルな設定方法、WSL環境でのChromeインストール手順も網羅されており、Webアプリケーションエンジニアがすぐに試せるように配慮されています。

デモンストレーションでは、まずGemini CLIがYahoo!ファイナンスを開き主要ニュースを要約するブラウザ操作能力を示します。さらに重要なのはエラーデバッグの例です。ToDoリストアプリのJavaScriptコードに意図的にタイプミス（`toggle`を`toggleTypo`に）を仕込み、AIに動作確認をさせます。AIはタスク追加後にチェックボックスをクリックするとコンソールにエラーが発生したことを検知し、「`toggleTypo is not a function`」というエラーメッセージから`script.js`内のタイプミスを特定、修正を提案し、再テストでエラーが解消されたことを確認します。ブラウザのコンソールエラーやHTML DOM構造を読み解くこの能力は、従来のブラウザ自動化ツールにはない画期的な点です。

結論として、著者はChrome DevTools MCPがブラウザの内部機能（コンソールログやパフォーマンスなど）にアクセスできるため、クロスブラウザE2Eテスト向けのPlaywright MCPとは異なり、フロントエンド開発中の動作確認やデバッグ、パフォーマンス分析に適していると述べています。AIが開発プロセスに深く統合され、より賢く、能動的なペアプログラマとして機能することで、開発者の生産性とワークフローが大幅に向上するでしょう。