## Servicenow上でGeminiを使えるようにする方法

https://qiita.com/macha_soda7/items/aa4b2accb378e5c810dc

ServiceNowユーザーがGoogle Geminiを統合し、個人情報や過去の会話履歴を基にカスタマイズされた回答を生成する具体的な実装手順を解説します。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:3/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 77/100 | **Overall**: 76/100

**Topics**: [[ServiceNow, Google Gemini API, API連携, ローコード開発, プロンプトエンジニアリング]]

ServiceNowユーザーがGoogle Geminiを統合し、個人情報や過去の会話履歴を基にカスタマイズされた回答を生成する具体的な実装手順を解説します。この解説は、ServiceNowの基本的な操作を理解していれば誰でも容易に実装可能であり、業務効率のさらなる向上を目指すものです。

記事では、まずGemini APIキーの取得から、ServiceNowへのAPI連携方法までをステップバイステップで説明します。具体的には、ServiceNowのREST Message機能を利用してGemini APIのエンドポイントを設定し、Script Includeで質問を処理する関数を作成、専用のテーブルとUI Actionを定義して、ユーザーが質問を入力しボタンを押すだけでGeminiからの回答を受け取れる仕組みを構築します。

さらに筆者は、ただGeminiを使うだけでなく、「自分専用のAI」を作成するための応用として、重要な2つの拡張機能を提示しています。一つは、個人情報（名前、年齢、好みなど）をJavaScriptオブジェクトとしてScript Include内に定義し、それをJSON形式でプロンプトに含めてGeminiに渡す方法です。これにより、Geminiはユーザーの背景情報を踏まえた回答を生成できるようになります。もう一つは、ServiceNowのテーブルに保存された過去の会話履歴（質問と回答のレコード）をGlideRecordで取得し、プロンプトの一部としてGeminiに渡すことで、AIが文脈を記憶し、より連続性のある対話を行えるようにする手法です。ただし、無料枠のAPI利用制限として、取得できる過去の会話は10件までという実用的な制約も明記しています。

本記事の実装は、ServiceNowのようなエンタープライズプラットフォーム上で、いかに生成AIを具体的かつ実践的に活用するかを示しており、特にローコード環境でのAI統合に興味を持つウェブアプリケーションエンジニアにとって、即座に応用可能な価値を提供します。既存の業務フローにAIの知見を組み込み、個別のニーズに応じたインテリジェントな自動化を実現する上での強力な指針となるでしょう。