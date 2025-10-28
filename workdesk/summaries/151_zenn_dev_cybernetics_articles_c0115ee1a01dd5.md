## 実行時に成長を続けるAgentic Context Engineering

https://zenn.dev/cybernetics/articles/c0115ee1a01dd5

記事は、GEPAを凌駕する新たなLLM振る舞い適応手法「ACE (Agentic Context Engineering)」の仕組みと、その主要な3つのコンポーネント（外部メモリ、コンテキスト再構成、自己フィードバック）を詳述し、エージェントの継続的な成長を実現すると解説する。

**Content Type**: Research & Analysis
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Agentic Context Engineering, LLM Behavior Adaptation, Prompt Optimization, External Memory for LLMs, Agent Frameworks]]

この記事は、既存のプロンプト最適化手法GEPAを性能で一貫して上回る新しいLLM振る舞い適応手法「ACE (Agentic Context Engineering)」を紹介している。著者はまず、LLMの振る舞いを操作する手段として「Fine-Tuning」「PEFT」「Context Adaptation」の3つを整理し、ACEが重みを一切変更しない「Context Adaptation」の枠組みに属することを明確にする。特に、PEFTとContext Adaptationの双方に存在する「Prompt Optimization」の言葉の混乱についても筆者なりの整理を行っている。

ACEは、プロンプト単体の最適化に留まらず、外部メモリ、In-Context Learning (ICL) の例、履歴、思考方針など「コンテキスト全体」を動的に適応させる点がGEPAと異なる。推論時にオンラインで処理を行い、連続的なタスクやエージェント利用を想定しているため、一度最適化して終わりではなく、継続的にコンテキストを成長させることが可能となる。これは人間の「試行 → 反省 → 記録 → 再利用」のサイクルをLLM向けに持ち込んだフレームワークと言える。

ACEの核となるのは以下の3つの役割に分かれた分業スタイルである。
1.  **外部メモリ (External Memory)**：戦略、失敗例、ドメイン知識などを箇条書きで構造化し蓄積する「進化するプレイブック」として機能する。
2.  **コンテキスト再構成 (インクリメンタル更新)**：Reflectorが抽出した「学習すべき内容」を小さな差分（デルタ）として既存メモリに統合し、コンテキスト全体の書き換えを避け、計算コストとレイテンシを抑えながら必要な部分を順次更新する。
3.  **Reflection (自己フィードバック)**：ReflectorがLLMの出力や推論過程から教訓や失敗パターンを自然言語で抽出し、Curatorがそれをデルタエントリとして外部メモリに組み込む。これによりプロンプト崩壊を防ぎ、記憶の破棄ではなく成長が起きる。

著者は、ACEの構造がプロンプト単体ではなく「コンテキスト全体」を進化させることで、ICLやGEPAの限界を超える土台を持つと評価している。一方で、Reflectorの性能に大きく依存する点が課題として挙げられており、ここに高コストのLLMを使用した場合の推論コストへの影響を懸念している。しかし、DSPyのようなプロンプトエンジニアリングを自動化するフレームワークへの実装や、既存のコード検索・メモリ引き継ぎツールと比較しても、ACEの高度なメモリ管理は開発者の体験を大幅に向上させる可能性を秘めていると期待を示している。