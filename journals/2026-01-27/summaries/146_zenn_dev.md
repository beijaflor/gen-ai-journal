## Agent SkillsがVercelに乗っ取られそうになっている件について

https://zenn.dev/tkithrta/articles/b7afbf76e7bb31

分析する：VercelがAIエージェントの拡張規格「Agent Skills」のエコシステムを急速に掌握しつつある現状と、それがオープンスタンダードに与える影響。

**Content Type**: 💭 Opinion & Commentary
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 95/100 | **Overall**: 72/100

**Topics**: [[Agent Skills, Vercel, Skills.sh, AIエージェント, オープンスタンダード]]

**Vercel**がAIエージェントの再利用可能な機能拡張規格である**Agent Skills**に向けたマーケットプレイス「**Skills.sh**」および、インストール用ツール「**add-skill**」、管理ツール「**skills**」を立て続けに発表した。**Anthropic**が提唱したこのオープン規格は、**Claude Code**や**Cursor**など多くのエージェントで急速に採用されているが、ツールの乱立によりスキルディレクトリの分散が課題となっていた。著者は、Vercelがこの混乱に乗じて独自に**AgentKey**を定義し、事実上のデファクトスタンダードを握ろうとしている現状を鋭く分析している。

主な論点は、マーケットプレイスによる「**匿名テレメトリ**」に基づいた評価システムの導入や、将来的な「**スキルパッケージレジストリ**」の中央集権化への懸念である。**Next.js**や**Vercel AI SDK**で起きた先行例を挙げ、実装の利便性を武器にオープンな仕様がVercel主導で改変・独占される可能性を指摘している。また、**Claude Code**の制限強化に伴うユーザーの**OpenCode**への移行など、コミュニティの動向についても触れている。

AIエージェントのカスタマイズや開発に携わるエンジニアにとって、規格の主導権争いとツールの選択基準を理解する上で必読の内容である。