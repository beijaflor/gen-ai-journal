## ClaudeがPackagist上の353件のゼロデイ脆弱性を発見

https://sansec.io/research/claude-finds-353-zero-days-packagist

**Original Title**: Claude finds 353 zero-days on Packagist

AIエージェントを活用した自動監査パイプラインにより、Packagist上のMagento拡張機能から353件のゼロデイ脆弱性を特定・実証した調査結果を公開している。

**Content Type**: 🔬 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 94/100 | **Overall**: 92/100

**Topics**: [[ゼロデイ脆弱性, Claude 4.5 Opus, セキュリティ監査, AIエージェント, サプライチェーン攻撃]]

Sansecの調査チームは、**Claude 4.5 Opus**を中核に据えた4段階のAIセキュリティパイプラインを構築し、**Packagist**上の上位5,000件の**Magento**拡張機能を対象とした大規模なセキュリティ監査を実施した。構築されたシステムは、1. パッケージを収集するAggregator、2. 静的解析を行うSecurity Auditor、3. **Docker**コンテナ上で脆弱性を検証するVulnerability Reproducer、4. 防御ルールを生成する**WAF** Suggestorの4ステージで構成される。特筆すべきは、単なる脆弱性指摘に留まらず、動的にコンテナを起動して`curl`による**PoC（概念実証）**を実行し、攻撃の有効性を自動検証している点だ。

この監査の結果、**RCE**（リモートコード実行）15件、**SQLi**（SQLインジェクション）50件、**IDOR**（認可不備）265件を含む、合計353件のゼロデイ脆弱性が実証された。調査費用はパッケージ1件あたり約2ドル（総額1万ドル）に抑えられており、数ヶ月を要する人的な調査が、わずかな計算リソースとAIの推論能力によって代替可能であることを証明した。筆者は、脆弱性発見のボトルネックが「熟練した研究者のスキル」から「計算予算とトークンスループット」へと移行していると分析している。

サードパーティ製の拡張機能やライブラリを多用するWebアプリケーション開発者や、LLMエージェントによる自動セキュリティ監査のワークフロー構築を目指すエンジニアにとって、極めて高い示唆を与える内容となっている。