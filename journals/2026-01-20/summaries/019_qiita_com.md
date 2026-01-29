## Copilot Studio Lite (Agent Builder) から Copilot Studio へのコピー機能を試してみた

https://qiita.com/Takashi_Masumori/items/70d75533c71352f018cc

Copilot Studio Lite（Agent Builder）で作成した簡易エージェントを、より高度なカスタマイズが可能な Copilot Studio へ移行する新機能を検証し、その活用場面と制約を明示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 94/100 | **Overall**: 72/100

**Topics**: [[Copilot Studio, Agent Builder, Microsoft 365 Copilot, AIエージェント, ガバナンス]]

Microsoft 365 Copilot 環境で簡易的にエージェントを作成できる「Copilot Studio Lite（旧称・現称 Agent Builder）」から、スタンドアロン版の「Copilot Studio」へエージェントをコピーする新機能が追加された。著者はこの機能を実際に検証し、エンジニアや管理者が知っておくべき実務上のメリットと、移行時に発生する技術的な制限を整理している。

本機能の重要性は、単なる「データ移行」ではなく、組織におけるAI活用のフェーズ移行（個人利用から全社共有へ）を円滑にすることにある。著者が指摘する最大の活用メリットは、ライセンスコストの最適化だ。Agent Builderで作成したエージェントの共有には利用者側にも M365 Copilot ライセンスが必要だが、Copilot Studio に移行してテナントクレジットや従量課金ライセンスを割り当てることで、ライセンスを持たない広範囲のユーザーに対しても、低コストでエージェントを公開することが可能になる。また、移行後はCopilot Studioが持つ豊富なコネクタやツールを用いた高度な拡張が可能になる。

ただし、技術的な制約として「ナレッジの欠落」には注意が必要だ。Agent Builderでは個人のTeamsチャットやメールをナレッジとして利用できるが、これらはコピー時に破棄される。著者はこの理由を、Copilot Studio が広範な共有を前提としているため、個人のプライベートな情報を過剰共有（オーバーシェアリング）させないための意図的な仕様であると分析している。ナレッジを維持するには、SharePointなどの適切な情報共有基盤にデータを配置し直す必要がある。

ガバナンスの観点では、環境選択メニューによって既定以外の環境へコピーできる柔軟性がある一方、管理者が意図しない環境へエージェントが展開されるリスクも孕んでいる。著者は、Power PlatformのDLP（データ損失防止）ポリシーやセキュリティロールによる制御を組み合わせた運用の重要性を強調している。個人の「思いつき」で作成されたエージェントを、管理された組織的なAIアセットへと昇華させるための重要なブリッジ機能と言えるだろう。