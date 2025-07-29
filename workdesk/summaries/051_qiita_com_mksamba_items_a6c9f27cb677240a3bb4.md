## Kiro でアプリ開発してみる（Amazon Lex / Bedrock での旅行プラン作成）

https://qiita.com/mksamba/items/a6c9f27cb677240a3bb4

AWSのAI搭載IDE「Kiro」がAmazon LexとBedrockを連携した旅行プラン作成ボット開発にどう貢献し、どのような課題があったかを実践的に検証する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[Kiro, Amazon Lex, Amazon Bedrock, Vibe Coding, AI-assisted Development]]

このQiita記事では、Amazon LexとBedrockを組み合わせた旅行プラン作成ボット開発において、AWSのAI搭載IDE「Kiro」のVibe Coding機能を実践的に試した経験を共有しています。開発者は、Kiroに要件を入力し、Lambda関数やLex Botのコード生成を試みました。

Kiroは、BedrockのClaude 3 Haikuを呼び出すLambda関数のコードを比較的正確に生成し、旅行プランの提示までがスムーズに確認できました。これは、AIによるコード生成が特定のロジック実装において高い実用性を持つことを示唆しています。特に、LLM連携部分の初期実装を迅速に進められる点は、開発速度向上に直結する大きなメリットです。

しかしながら、Amazon Lex Botの定義生成に関しては大きな課題が露呈しました。Kiroが生成したシェルスクリプトは、Lexのバージョン違い（v1とv2）への対応不足や、インテントやスロット定義の過不足があり、最終的には手動での大幅な修正が必要となりました。これは、AIによるコード生成が、複雑な設定や、サービスごとのバージョンによる仕様変更に完全に追従できていない現状を浮き彫りにしています。

この経験は、AI支援型開発ツールがいかに進化しても、開発者が生成されたコードや設定の**内部を深く理解し、レビューする能力**が依然として不可欠であることを示しています。特に、AWSのような多様なサービス群を持つクラウド環境では、AIが生成するIaC（Infrastructure as Code）や設定ファイルも、そのサービスの特性やバージョンに応じた精査が求められます。AIは初期フェーズの加速には貢献するものの、**品質保証とデバッグ**においては人間の専門知識が不可欠であり、これが現在のAI支援型IDEの現実的な立ち位置と言えるでしょう。
