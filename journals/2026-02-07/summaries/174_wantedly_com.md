## ウォンテッドリーのLLM アプリケーション自動テスト戦略

https://www.wantedly.com/companies/wantedly/post_articles/1041873

提示する。LLMアプリケーションの非決定性とAPI依存という難題に対する、RSpecとLLM as a Judgeを組み合わせた自動テスト戦略を。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[LLM Testing, RSpec, LLM as a Judge, Amazon Bedrock, Software Engineering]]

ウォンテッドリーにおける、**Amazon Bedrock**を活用したLLM機能の自動テスト手法を解説している。LLMアプリケーションでは、プロンプトという「ビジネスロジック」が外部APIという「モックすべき対象」と表裏一体であるため、従来のテストピラミッドが通用しない。この記事では、この課題を解決するために採用された2段階の戦略が詳しく述べられている。

第1段階では、**RSpec**を基盤に実際のLLM出力を`.snap`ファイルに記録する**スナップショットテスト**を導入し、プロンプト変更によるデグレを可視化した。第2段階では、判定役に**Claude Haiku 4.5**を用いる**LLM as a Judge**を導入。自然言語で期待値を定義できるカスタムマッチャー`satisfy_natural_expectation`の実装により、LLM特有の表記の揺れを吸収した自動検証を可能にしている。実行コスト抑制のため、タグを用いたCIからの分離運用や、スナップショットによる人間・AIエージェント向けの可視化を組み合わせるなど、実運用に即したアーキテクチャが示されている。

LLMを組み込んだプロダクトの開発において、プロンプト調整のデグレ防止とテストの自動化を両立させたいエンジニアにとって、極めて実践的なガイドとなっている。