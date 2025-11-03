## Snowflake Cortex Agents によるお問い合わせ調査 AI Agent の構築

https://tech.layerx.co.jp/entry/2025/10/14/193713

LayerXのエンジニアはSnowflake Cortex Agentsを活用し、構造化・非構造化データを横断してお客様からのお問い合わせを自動調査するAI Agentの構築を試み、その可能性と運用上の課題を明らかにした。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Snowflake Cortex AI, AI Agent, お問い合わせ対応自動化, マルチエージェントシステム, RAG]]

LayerXのエンジニアは、Snowflake Cortex Agentsを用いて、顧客からの問い合わせに対する一次調査を自動化するAI Agentの構築に挑戦しました。債務管理チームは問い合わせ調査の工数削減を目指し、Snowflake Cortex AIの主要機能であるCortex Analyst（構造化データ）、Cortex Search（非構造化データ）、そしてこれらを統合・自律的に操作するCortex Agentsを組み合わせたAI Agentを開発。

実験では、本番DBデータやログ（構造化）、サポートページ（非構造化）を活用。構造化データのみ、非構造化データのみ、そして両者を組み合わせた複雑な問い合わせに対して、AI Agentが適切にデータ分析ツールを呼び出し、原因特定から解決策の提示まで行えるポテンシャルを示しました。特に、Cortex Searchの「ツール説明（Description）」を適切に設定することで、AI Agentの判断精度が向上する重要な知見が得られました。

一方で、実用化に向けた課題も明らかになりました。Cortex AnalystのSemantic Modelは、AIの精度維持のため手動での慎重な構築と継続的なメンテナンスが必要で、新たな運用コストが生じます。また、サポートページなどの非構造化データの鮮度を保つ仕組みも不可欠です。

今後の展望として、記事では、多様な問い合わせに対応するため、AnthropicのRouting Patternを応用したMulti-Agent化（Router AgentがSpecialist Agentを呼び出す形式）による回答精度の向上が提案されています。さらに、ユーザーからのフィードバックを非構造化データとしてAgentに蓄積させ、知識の継続的な自己成長を促すことも目指しています。これらの取り組みにより、エンジニアが顧客へより価値のある機能開発に集中できる環境を構築していく考えです。