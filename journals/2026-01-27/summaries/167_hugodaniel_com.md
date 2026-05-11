## CLAUDE.mdの自動生成でBANされた開発者が問う「ブラックボックス化したAIモデレーション」

https://hugodaniel.com/posts/claude-code-banned-me/

**Original Title**: I was banned from Claude for scaffolding a CLAUDE.md file

月額220ユーロの「Max 20x」ユーザーがプロジェクトひな型ツールにCLAUDE.mdを組み込む作業中、警告なしに組織アカウントを無効化された顛末から、不透明なAIモデレーションと事業者の無対応姿勢に警鐘を鳴らす。

**Content Type**: 💭 Opinion & Commentary
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 72/100 | **Annex Potential**: 78/100 | **Overall**: 75/100

**Topics**: [[Claude Code, AIモデレーション, アカウントBAN, プロンプトインジェクション, CLAUDE.md]]

ブログ筆者の**Hugo Daniel**氏は、自作JSフレームワーク「**boreDOM**」用のスキャフォールディングツールに**CLAUDE.md**を組み込む作業中、突然 `"This organization has been disabled."` というAPIエラーで利用不能となった。手順は単純で、Claude A にひな型ツールを更新させ、新規プロジェクトで Claude B を立ち上げ、Claude B のエラーを Claude A にフィードバックして CLAUDE.md を改善する、というループを「human-in-the-loop」として回していただけだ。途中から Claude A が CLAUDE.md 内で Claude B への指示を**ALL CAPS**で書き始めたあたりで、システムプロンプト風の文面がプロンプトインジェクション検知ヒューリスティクスに引っかかった、というのが筆者の仮説である。

問題視されているのはBAN自体ではなく、その後の対応だ。Google Formsで提出した異議申立てには返信なし、サポート窓口にも返信なし、唯一届いたのは**Anthropicからの返金通知メール一通**のみ。筆者はこれを「対話ではなく、口止め料」と評し、AIモデレーションが「精度よりも安全側に極端に倒された**ブラックボックス**」になっていると指摘する。`CLAUDE.md` の自動生成のように**システム指示風のテキストを生成・反復するワークフローは地雷原**であり、有料の重課金ユーザーであっても予告なく排除されうる、というのが教訓だ。AIエージェントを使った自動化ツール開発に関わる読者にとっては、自前のスキャフォールド処理がどこでモデレーションに踏み込みうるかを再考する材料となる一方、ベンダーロックインのリスクと「人間に対する説明責任を欠いたプラットフォーム」への依存度を見直す契機としても読める。
