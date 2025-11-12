## OpenAI AgentKitでサクッとAIエージェント作ってみた #ノーコード

https://qiita.com/morimune/items/3d07e4e0062598093b3e

OpenAI AgentKitを利用し、ノーコードでAIエージェントを迅速に構築する手順を具体的な星座占いエージェントの作成例と共に解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 82/100 | **Overall**: 80/100

**Topics**: [[OpenAI AgentKit, AIエージェント構築, ノーコード開発, ワークフロー自動化, Generative AI]]

Webアプリケーションエンジニアは、OpenAIが2025年10月6日に発表した統合ツールセット「AgentKit」を活用し、いかにノーコードでAIエージェントを迅速に構築できるか理解できるでしょう。本記事は、KIYOラーニングの森下氏が、AgentKitに含まれる「Agent Builder」を使って星座占いAIエージェントを実際に作成する手順を詳細に解説しています。

著者はまず、AgentKitが開発者や企業がAIエージェントの構築、展開、最適化をサポートする包括的なツールであることを説明。次に、Agent Builderの基本機能であるCore Agent（エージェントの振る舞いを定義）、End（フローの終点）、そしてTools（File search, Guardrails, MCP）やLogic（If/else, While, User approval, Data Transform, Set state）といった各種ノードの役割を紹介します。

具体的な星座占いエージェントの作成手順では、以下のステップが詳細に示されます。
1.  **ワークフロー作成**: Agent Builderにアクセスし、新規ワークフローを「Create a workflow」から開始します。
2.  **Guardrailsの追加**: Startノードの直後にGuardrailsを追加し、入力・出力の安全性とポリシー順守を設定（今回はデフォルト）。
3.  **Set stateで生年月日を保存**: ユーザーが入力したテキストから生年月日（YYYY-MM-DD形式）を抽出し、`birthdate`という状態変数に保持するロジックを設定します。
4.  **If / elseで分岐**: `birthdate`の形式が正しいか否かで処理を分岐させ、適切なエージェントフローへと誘導します。
5.  **Agentノードの配置と設定**:
    *   生年月日が未入力または形式不正な場合（Else側）には、ユーザーに生年月日を尋ねるAgentを設定します。このAgentには簡潔に質問を行うための`Instructions`を設定します。
    *   生年月日が有効な場合（If側）には、`birthdate`を用いて今日の運勢を生成するAgentを設定します。このAgentには、太陽星座の判定ロジック、Web検索の活用方法、そして総合運・恋愛運・仕事運などを定型フォーマットで出力するための詳細な`Instructions`が与えられ、質問や確認を一切行わない厳格なルールが指定されます。
6.  **動作確認**: 右上のPreview機能を用いて、生年月日未入力時と入力時のエージェントの応答フローを実際に確認します。この際、キャンバス上で処理パスが視覚的に表示されるため、デバッグが容易である点が強調されています。

著者は、Agent Builderが「まず作って動かす」という目的に非常に適しており、画面操作が直感的で、ノードを置いてつなぐだけで基本フローが作成できる点、そしてPreview機能で即座に動作確認し、現在の処理場所を把握できる点を高く評価しています。ウェブアプリケーションエンジニアにとって、この新しいノーコードツールは、AIエージェントのプロトタイプ開発や機能検証を迅速に進めるための強力な手段となるでしょう。