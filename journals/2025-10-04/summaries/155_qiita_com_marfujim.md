## Select AI Feedbackを試してみた

https://qiita.com/marfujim/items/81edc9da186c7683e170

Oracle Select AIは、新機能「Select AI Feedback」を導入し、ユーザーフィードバックを通じてNL2SQLの精度を継続的に向上させ、より正確なSQLクエリ生成を可能にした。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[NL2SQL, AI Feedback Loop, Vector Database, Oracle Autonomous Database, Generative AI in Database]]

Oracle Select AIが、自然言語からSQLを生成するNL2SQL機能の精度を飛躍的に高める新機能「Select AI Feedback」をリリースしました。この機能は、Select AIが生成したSQLクエリや結果セットに対して、ユーザーが直接フィードバック（肯定的、否定的、または正しいSQLクエリの提示）を提供できるようにするものです。

具体的には、期待通りのSQLが生成されなかった場合、ユーザーは自然言語で修正指示をしたり、手動で作成した正しいSQLを提示したりできます。このフィードバックはベクトルデータベースに保存され、以降のクエリ生成時にLLMが類似の過去のフィードバックを参照し、生成ロジックを改良します。これにより、単なる問い合わせ対応だけでなく、ビジネスロジックや特定の要件をLLMが学習し、よりパーソナライズされ、コンテキストに応じた正確なSQLクエリを継続的に生成できるようになります。

Webアプリケーションエンジニアにとって、この機能は単なるデータベースの改善以上の意義を持ちます。生成AIを組み込んだアプリケーションを開発する際、AIの出力精度向上は大きな課題です。Select AI Feedbackが示す「ユーザーフィードバックを活用したLLMの継続的学習メカニズム」は、AIエージェントやNL2SQLインターフェースを構築する上での強力なパターンとなります。特に、記事が「適切なユーザー・インターフェースを作成することで、エンドユーザーがフィードバックを提供することもできる」と指摘している点は重要です。開発者は、このフィードバックループをアプリケーションに組み込むことで、エンドユーザー自身がAIアシスタントの精度を向上させ、長期的に運用可能な高品質なAI駆動型アプリケーションを実現できるでしょう。Oracle Autonomous Database 23aiが必要となりますが、LLMとベクトルデータベースを組み合わせた改善アプローチは、幅広いAI開発に応用可能な技術的示唆を与えます。