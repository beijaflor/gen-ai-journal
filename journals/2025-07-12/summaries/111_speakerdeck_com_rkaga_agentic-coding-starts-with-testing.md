## テストから始めるAgentic Coding 〜Claude Codeと共に行うTDD〜

https://speakerdeck.com/rkaga/agentic-coding-starts-with-testing

AIコーディングにおいてテストが果たす役割と、Claude Codeを用いたTDDの実践方法を解説する。

[[Agentic Coding, テスト駆動開発 (TDD), Claude Code, AIとテスト, 開発ワークフロー]]

本プレゼンテーションは、AIを活用したAgentic Codingにおいてテストがいかに重要であるかを強調しています。特に、Claude CodeのようなAIエージェントがコードを生成する際、テストはAIへの指示書として機能し、同時にAIの出力に対するフィードバックループを提供します。これは「Reconciliation Loop」の評価関数として機能し、AIが目標とするコードに収束するための明確な指針となります。

AIエージェントは非常に多才である一方で、その出力は予測不可能な場合があります。テストを包括的に記述することで、AIが生成したコードの品質を保証し、リファクタリングや非慣用的なコードの受け入れに対する信頼性を高めることができます。Kent Beck氏が提唱するように、開発者の役割はコードを書くことから、AIに「良いコードとは何か」を教えることにシフトしており、テストはそのための「カリキュラム」となるのです。

プレゼンテーションでは、Claude Codeを用いたTDDの実践、BDDやRGBCサイクルへの応用、そして「Perfect Commit」の概念が紹介されています。また、高速なテストの重要性や、ユニットテストとE2Eテストを組み合わせた「砂時計型」テスト戦略の提案も含まれており、AIによるテスト生成の可能性にも言及しています。AI時代においてもテストの価値は増大し、開発プロセスにおけるその役割はより一層重要になると結論付けています。

---

**編集者ノート**: AIがコード生成の主役になりつつある今、テストの役割は根本的に再定義されています。単なる品質保証の手段ではなく、AIへの「指示書」であり「教師」となるという視点は、Webアプリケーション開発者にとって非常に重要です。特に、Claude Codeのようなエージェントが複雑なロジックを生成する際、テストがなければその挙動を制御し、意図通りの成果を得ることは困難です。

このプレゼンテーションが示唆するのは、これからの開発者は、コードを書くスキル以上に「テストを書くスキル」、つまり「AIに何をさせたいかを明確に定義するスキル」が求められるということです。テストがAIの学習データとなり、開発サイクルを加速させる「砂時計型」テスト戦略は、CI/CDパイプラインの最適化にも直結します。将来的には、AIがテストコード自体を生成するようになるでしょうが、その「テストのテスト」を行うのは依然として人間の役割です。AI時代の開発ワークフローは、テストを中心に再構築され、より洗練されたテスト戦略を持つチームが競争優位性を確立すると予測します。
```
