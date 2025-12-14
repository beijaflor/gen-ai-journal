## コーディングエージェントがChrome DevTools MCPでブラウザセッションをデバッグ可能に

https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session

**Original Title**: Let your Coding Agent debug your browser session with Chrome DevTools MCP

Chrome DevTools MCPが強化され、コーディングエージェントがアクティブなブラウザセッションに直接接続し、デバッグを支援する機能が導入されました。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Chrome DevTools, コーディングエージェント, デバッグ, ブラウザ自動化, AI開発支援]]

Chrome DevTools Message Communication Protocol (MCP) が大幅に強化され、コーディングエージェントがアクティブなブラウザセッションに直接接続し、デバッグ作業を支援できるようになりました。この新機能は、開発者が手動デバッグとAIによるデバッグ支援との間をシームレスに移行することを可能にします。

具体的なメリットとして、エージェントはログイン済みの既存ブラウザセッションを再利用できるため、追加の認証が不要になります。これにより、ログインが必要な複雑なシナリオにおけるデバッグが容易になります。また、開発者はChrome DevToolsの「Elements」パネルで選択した要素や、「Network」パネルで検出された失敗したネットワークリクエストに対し、直接コーディングエージェントに調査を依頼できるようになりました。開発者が手動で問題箇所を特定した後、そのタスクをエージェントに引き継ぐことで、デバッグの効率が劇的に向上します。

この機能は、Chrome M145（Canary版）で導入されたもので、既存のリモートデバッグ機能の上に構築されています。利用するには、まず`chrome://inspect/#remote-debugging`でリモートデバッグを明示的に有効にする必要があります。その後、Chrome DevTools MCPサーバーを`--autoConnect`オプション付きで設定することで、実行中のChromeインスタンスに自動的に接続し、リモートデバッグセッションを要求します。悪意のある使用を防ぐため、リモートデバッグセッションの要求時には常にユーザーの許可ダイアログが表示され、セッション中は「Chrome is being controlled by automated test software」というバナーが表示され、ユーザーに制御状況を明示します。

著者らは、これが第一歩に過ぎず、今後はDevToolsのより多くのパネルデータをコーディングエージェントに公開していく計画であると述べており、AIを活用した開発ワークフローのさらなる進化を示唆しています。この統合は、ウェブアプリケーションエンジニアにとってデバッグプロセスを革新し、生産性を向上させる重要な一歩となるでしょう。