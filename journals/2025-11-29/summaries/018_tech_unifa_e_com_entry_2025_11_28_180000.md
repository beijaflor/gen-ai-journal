## 進め！“Vibe Testing”計画！ 〜AI開発推進部 QAの”初”挑戦〜

https://tech.unifa-e.com/entry/2025/11/28/180000

ユニファのQAエンジニアが、経験知（暗黙知）をAIと共に形式知化し、構造的な品質保証モデル「Vibe Testing」を構築するプロジェクトについて解説します。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Vibe Testing, AI-driven QA, 形式知化, WYSIWID, テスト自動化ツールチェーン]]

ユニファのAI開発推進部でQAエンジニアを務める高田氏が、自身の「Vibe Testing」計画について、その着想から構想、挫折、そして現在の立ち位置までを詳細に公開しました。本プロジェクトは、QAエンジニアの長年の経験知である「暗黙知」を、AIとの協創を通じて「形式知」へと変換し構造化することで、根本的な品質保証のエンジニアリングを目指すものです。

高田氏は、QA歴の中で直面してきた「書式や粒度がバラバラ」「仕様書がない」「意図が伝わらない」という3つの「亡霊」のような課題に苦しんできました。自身の「品質保証のゴールデントライアングル」（Where/What/How）という思考の型はあったものの、その属人性が課題でした。転機となったのは、ソフトウェアの可読性を高める構造パターンを提唱する論文「What You See Is What It Does (WYSIWID)」との出会いです。この論文のConcepts/Syncs/Actionsが自身の経験知と見事にマッピングできることを発見し、さらに「Who（AIも読者である）」と「Why（目的・因果関係）」を設計の中核に埋め込むことの重要性を認識しました。

このインサイトに基づき、「Vibe Testing」では以下の具体的な解決策を導入しています。
1.  **【Format問題】**: テスト設計書に「Concepts Definition」と「Viewpoint Matrix（Syncs）」を新設し、テストの「期待値」を「Then Property（満たすべき性質）」に再定義することで、AIが検証すべき「正解」の精度を高め、Whyを明示化。
2.  **【Spec問題】**: ユーザーストーリーをConceptsとSyncsに分解するプロセス自体を「テスト仕様書」と位置付け、Property-Based Approachを導入。Concepts側に「状態の整合性（Integrity）」を持たせることで、Syncsの肥大化を抑制し、AIへの指示を「目的と性質の検証」へと進化させます。
3.  **【Communication問題】**: テストピラミッドをベースに各テストレベルを再定義し、Small（Unit Test）ではConceptsのProperty検証、Medium/Large（Integration/System/E2E Test）ではSyncsの相互作用と因果関係（Why）を検証する共通言語を確立。AIエージェントを新たな「Who（テスター）」とし、人間とAIが同じドキュメントを見て協働する環境を整備します。

実装には、Cursor AI、spec-kit、Playwright、Vitest、Atlassian MCP Serverなどを活用したツールチェーンを構想。AIエージェントがMarkdown形式のSpecから実装計画やタスクを生成し、自動・手動テストを通じて品質を担保します。

高田氏は「『Why』の言語化コスト」「抽象度のコントロール」といった課題を認識しつつも、「Easy（安易さ）ではなくSimple（単純さ）を追求する」「構造なきテストは手作業の再発明に過ぎない」「失敗を徒労ではなく資産に変える」という強い信念を持って本プロジェクトを推進しています。これからのQAエンジニアは、単なる確認者ではなく「品質のモデラー」へと進化し、品質の「Why」を問い続けるストーリーテラーになるべきだと力説しています。