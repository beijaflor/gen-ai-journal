## GitHub Copilot Chat の Plan "モード" をコードレベルで理解する

https://zenn.dev/openjny/articles/43e010c65faa9a

解明する。GitHub Copilot Chatの「Plan」モードが、従来の基本モードとは異なり、実は拡張機能が注入する「カスタムエージェント」として実装されていることをソースコードレベルで紐解きます。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, VS Code, AI Agents, Prompt Engineering, Software Architecture]]

GitHub Copilot Chatの「Plan」モードが、Ask、Edit、Agentといった他の基本モードとは根本的に異なるアーキテクチャで構築されていることを、VS Codeの実装レベルから深掘りした記事である。著者はVS CodeおよびCopilot Chat拡張機能のソースコードを調査し、Planモードが従来のインテントベース（プログラム的な制御）ではなく、実は拡張機能が注入する「カスタムエージェント」のラッパーに過ぎないことを明らかにした。

技術的な核心は、なぜPlanエージェントがUI上で「モード」として扱われるのかという点にある。著者の分析によれば、VS Codeには特定の条件（Copilot Chat拡張機能から登録されていること）を満たすカスタムエージェントを、UIコンポーネントが例外的に「組み込みモード」として表示する特別な処理が仕込まれている。これには、VS Codeが持つ「Contribution Points」や「Prompt Storage」というプロンプト管理の抽象化レイヤーが深く関わっており、技術的にはユーザーが作成するカスタムエージェント（.agent.md）と同等の仕組みが、プラットフォーム側の特権的な処理によって公式機能として統合されている。

また、実際のエージェント定義ファイル（Plan.agent.md）の解析も非常に示唆に富んでいる。このプロンプトではXMLタグ（`<workflow>`, `<stopping_rules>`, `<plan_style_guide>`など）を用いた高度な構造化が行われており、LLMに対して「実装は絶対に行わず、計画立案にのみ集中せよ」という制約を多層的に課している。特に興味深いのは、Planモード自身が複雑な検索を行うのではなく、`#tool:runSubagent`を通じて他のエージェント（Agentモード）に調査を委譲する設計である。これにより、計画立案の品質を保ちつつ、自律的な情報収集を可能にしている。

エンジニアにとっての重要性は、Planモードの挙動がブラックボックスではなく、私たちが作成するカスタムエージェントと同じ仕組みで動いていると知ることにある。著者は、Planモードの定義ファイルを参考にすれば、特定のプロジェクトや社内ドキュメント、独自のチケット管理システムに特化した「自分たち専用のPlanモード」を構築することも可能だと主張している。ツールを単に消費するだけでなく、その設計思想を学び、自分たちの開発ワークフローに最適化されたエージェントを自作するための具体的な指針を提示している点が、本記事の大きな価値である。