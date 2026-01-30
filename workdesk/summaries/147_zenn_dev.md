## Spec DrivenではなくImplementation Drivenを選ぶ理由

https://zenn.dev/akring/articles/ef2d8d1e95ff86

AIによる試行錯誤のコスト低下を背景に、仕様を起点とするのではなく実装を通じた探索の成果として仕様を定義する「実装駆動開発（IDD）」の有効性を提唱する。

**Content Type**: 💭 Opinion & Commentary
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 81/100 | **Annex Potential**: 83/100 | **Overall**: 80/100

**Topics**: [[AIコーディング, 開発プロセス, Implementation-Driven Development, 仕様駆動開発, YAGNI]]

近年のAIコーディングの普及に伴い、AIの出力を制御する手段として**仕様駆動開発（Spec-Driven Development）**が再注目されています。しかし著者は、探索が不十分な段階で仕様を開発の起点に据えることに違和感を唱えています。本記事では、実装を思考の起点とする**Implementation-Driven Development (IDD)**というスタンスを提示し、その背景にある歴史的経緯やAI時代の開発環境における合理性を解説しています。

主な洞察として、著者は**Winston W. Royce**の論文を引用し、本来のウォーターフォールモデルも試作や反復を通じた知見の整理を前提としていたことを指摘。AIの登場によりコード生成や検証のコストが劇的に下がった現代では、先に仕様を固めるよりも、まず動くものを作りながら前提を更新するアプローチの方が、結果として**YAGNI**（不要なものは作らない）の原則を実践しやすくなると主張しています。仕様は「守るべき前提」ではなく、理解が進んだ後の「探索の成果物」として位置づけるべきだという考え方です。

仕様と実装を「仮説とその正当化」ではなく「試行錯誤による合意形成」と捉え直す視点は、AIツールを実務に組み込むエンジニアにとって重要な指針となります。**GitHub Copilot**や**Cursor**などのツールを使いこなしつつ、開発プロセスの設計や大規模なコード生成の制御に課題を感じているエンジニアに推奨します。