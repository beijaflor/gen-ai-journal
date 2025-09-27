## AI エージェントのための Agent Payments Protocol (AP2) を試してみた

https://azukiazusa.dev/blog/trying-agent-payments-protocol-ap2/

Googleが提案するAgent Payments Protocol (AP2) を活用し、AIエージェントがユーザーに代わって安全な決済を実行するためのデジタル契約「Mandates」の仕組みと、そのサンプル実装を試す手順を詳細に解説します。

**Content Type**: 📖 Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 96/100 | **Overall**: 76/100

**Topics**: [[Agent Payments Protocol (AP2), AI エージェント, 自律決済, デジタル契約, エージェント間通信]]

現状の決済システムは人間の直接操作を前提としており、自律型AIエージェントがユーザーに代わって安全に決済を行うことは想定されていませんでした。Googleが提案するAgent Payments Protocol (AP2) はこの課題を解決し、エージェント主導の決済を安全に開始・処理するための新しいプロトコルです。AP2はModel Context Protocol (MCP) やA2AといったAIエージェント間通信プロトコルを拡張し、改ざん防止機能を備えた暗号化署名付きデジタル契約「Mandates」によって信頼を構築します。

Mandatesには、ユーザーが立ち会うリアルタイム購入と、事前に詳細な条件に署名してエージェントにタスクを委任する「委任タスク」の2つの方法があります。これにより、AIエージェントはユーザーの意図に基づき、不正請求や詐欺のリスクを軽減しながら決済を実行できるようになります。

この記事では、現在提案段階にあるAP2のGitHubサンプルコードを実際に試し、人間が立ち会う場合の決済フローを具体的に解説しています。Shopping Agentがユーザーの購入リクエストを受け取り、Merchant Agent、Credentials Provider、Card Processor Agentといった複数のエージェントと連携しながら、Intent Mandate、Cart Mandate、Payment Mandateを順に生成・署名していくプロセスが詳細に示されています。

Webアプリケーションエンジニアにとって、このAP2はAIエージェントの可能性を大きく広げる重要な技術です。これまでは情報収集や提案に留まっていたエージェントが、決済という商取引の核心部分に安全に介入できるようになることで、より高度で自律的なサービスやビジネスロジックを設計・実装する道が開かれます。特に、エージェントがユーザーの代理として複雑なオンライン取引を完結させる未来を構築する上で、信頼と責任の基盤を提供するAP2の動向は注視すべきです。