## 公式の「Chrome DevTools MCP」を VS Code の GitHub Copilot（エージェントモード）で軽く試す（現在、パブリックプレビュー版）

https://qiita.com/youtoy/items/075ddb8c09eaa0e98b4b

VS CodeのGitHub Copilotエージェントモードで、現在パブリックプレビュー中のChrome DevTools MCPを利用し、ウェブページのパフォーマンスチェックを簡単に行う方法を実演する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[GitHub Copilot Agent Mode, Chrome DevTools MCP, VS Code Integration, Web Performance Testing, AI Coding Tools]]

この記事は、現在パブリックプレビュー版として提供されている「Chrome DevTools MCP (Multi-protocol Client Protocol)」をVS CodeのGitHub Copilotエージェントモードと連携させ、ウェブアプリケーションのパフォーマンス測定を行う実用的な手法を紹介しています。これは、ウェブアプリケーション開発者にとって、開発ワークフローを大きく変革する可能性を秘めた重要な進展です。

なぜこれがこれほど重要なのでしょうか？従来のパフォーマンス最適化は、ブラウザの開発者ツールを手動で操作し、その結果を分析するという手間のかかる作業でした。しかし、Chrome DevTools MCPがAIエージェントと結びつくことで、このプロセスが劇的に効率化されます。すなわち、VS Codeのような開発環境内からGitHub Copilotに自然言語で指示を出すだけで、AIエージェントが自動的にChromeブラウザを制御し、指定されたウェブページのパフォーマンスを測定し、その結果を直接開発者へフィードバックしてくれるのです。

記事では、その具体的な導入方法として、VS Codeの設定に`chrome-devtools-mcp`を追加するコマンド（`code --add-mcp '{"name":"chrome-devtools","command":"npx","args":["chrome-devtools-mcp@latest"]}'`）を提示しています。さらに、「`Check the performance of https://developers.chrome.com`」という簡潔なプロンプトを与えるだけで、ブラウザが起動してパフォーマンス測定が実行され、その詳細な結果がVS Code上に表示されるという、一連の流れを明確にデモンストレーションしています。

この統合は、特にフロントエンドエンジニアの日常的な業務において大きな変革をもたらします。手作業による反復的なテストや分析の負荷をAIに委ねることで、開発者は本来注力すべき、より複雑なロジックの実装やユーザー体験の向上といった創造的な活動に集中できるようになります。これは、AIエージェントが単なるコード生成を超え、デバッグ、テスト、QA、デプロイといった開発ライフサイクル全体に深く関与し、自動化された「エージェント駆動開発」の未来が着実に近づいていることを強く示唆しています。今後の展望として、パフォーマンス測定にとどまらず、アクセシビリティチェック、セキュリティ脆弱性診断なども、AIエージェントがIDE内で自動実行する未来が視野に入ります。