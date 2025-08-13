## Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives

https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/

Cloudflareが、AI検索エンジンPerplexityがウェブサイトのクローリング拒否指令を回避するためにステルスかつ未申告のクローラーを使用していることを発見し、その詳細を公表しました。

**Content Type**: Research & Analysis

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 94/100 | **Annex Potential**: 95/100 | **Overall**: 96/100

**Topics**: [[Web Crawling Ethics, Bot Management, AI Search Engines, Content Protection, Robots.txt]]

Cloudflareは、AI検索エンジンPerplexityがウェブサイトのクローリング拒否指令やブロックを意図的に回避している実態を詳細に分析し、そのステルス行動を暴露しました。Perplexityは通常のエージェント「PerplexityBot」や「Perplexity-User」がブロックされると、Google Chromeを装った未申告のユーザーエージェントに切り替え、IPアドレスやASN（自律システム番号）を頻繁に変更して検出を逃れていました。同社はrobots.txtファイルを無視したり、フェッチすらしないことが確認されており、これはウェブクローリングの長年の規範（RFC 9309）に反します。

この問題がウェブアプリケーションエンジニアにとって重要なのは、AI企業による不透明なデータ収集がウェブの信頼基盤を揺るがし、コンテンツ制作者のコントロールを著しく侵害するからです。自社コンテンツをAI学習から保護したい、または特定のボットからのアクセスを制限したいと考えるエンジニアにとって、従来のrobots.txtやWAFルールだけでは不十分であり、より高度なボット管理戦略が求められることを示唆しています。Cloudflareは機械学習とネットワークシグナルを組み合わせたフィンガープリント技術でこのステルスクローラーを特定し、顧客保護のための管理ルールを導入しました。この事例は、AI時代のコンテンツの所有権と倫理的なデータ利用に関する議論を深めるものであり、エンジニアは自サイトの防御策を再考する必要があるでしょう。OpenAIのような善意のボット運用者との比較も示されており、AI業界における行動規範の確立が急務であることが浮き彫りになっています。