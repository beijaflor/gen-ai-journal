## Anthropic、Claude Codeサブスクリプションのサードパーティ製ツール利用を制限

https://news.ycombinator.com/item?id=46549823

**Original Title**: Anthropic blocks third-party use of Claude Code subscriptions

Anthropicが、月額200ドルの定額プランを自社製CLI「Claude Code」以外で利用できないよう制限を強化した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:4/5 | Depth:2/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 82/100 | **Overall**: 68/100

**Topics**: [[Anthropic, Claude Code, OpenCode, API Pricing, Vendor Lock-in]]

Anthropicが、月額200ドルの定額制プラン（**Claude Max**等）を、**OpenCode**などのサードパーティ製CLIツールから利用することを制限し始めた。背景には、定額プランが従来の従量制APIと比較して極めて安価（場合によっては5倍以上の価格差）であり、サードパーティツールが「格安の使い放題プラン」の抜け穴として利用されていた実態がある。これに対しAnthropicは、自社製の**Claude Code** CLIのみに利用を限定するよう認証仕様を変更した。

コミュニティでは、OpenCode側が**OAuth**トークンの偽装やプラグインによる回避策で対抗する「いたちごっこ」が続いている。エンジニア視点では、単なるコスト問題に留まらず、ベンダーによるツールの囲い込み（ロックイン）や、トレーニングデータ収集を目的とした強引な手法に批判が集まっている。高いトークン消費を伴う大規模開発において、APIコストを抑えつつ好みのツールを使い続けたいエンジニアにとって、技術選定上の重要なリスク要因となる。