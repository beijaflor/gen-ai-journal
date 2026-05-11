## バイブコーディング 第2回：AIを活用したクラウドオーケストレーションツールの構築

https://matklad.github.io/2026/01/20/vibecoding-2.html

**Original Title**: Vibecoding #2

クラウドAPIの複雑な操作を自動化する独自ツールを、人間が構造を定義しAIが詳細を実装する『協業』によって構築する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 86/100 | **Overall**: 88/100

**Topics**: [[Vibecoding, Cloud Orchestration, Deno, AWS EC2, AI-assisted Development]]

分散データベース**TigerBeetle**の開発者である著者が、検証用のクラウド環境を制御する独自ツール**box**を**Claude**等のAIを用いて構築した過程を報告している。著者は「AIによるワンショットのコード生成」が保守性や品質に欠ける点を指摘し、人間が**TypeScript**でインターフェースや型定義のスケルトン（構造）を自ら記述し、AIにAPI呼び出し等の具体的な「肉付け」を任せるインクリメンタルな開発手法の有効性を説いている。

具体的には、**Deno**とシェルスクリプトライブラリ**dax**を組み合わせ、**AWS EC2**のスポットインスタンス確保や同期、コマンド実行をSIMD的に行うワークフローを構築。複雑な**AWS CLI**のフラグ管理や、初心者が陥りがちな「OS起動とSSH起動の待機時間の差」といったトラブルの解決において、AIが極めて高い補助能力を発揮することを示した。また、指示を自然言語で記述するよりも、コードの型や空の関数を提示する「Show, Don't Tell」のアプローチがAIの精度を高めるという知見も共有されている。

クラウドインフラの操作を自動化したいエンジニアや、AIを単なる生成器ではなく設計の補助ツールとしてワークフローに組み込みたい開発者にとって、実践的なガイドとなる内容である。