## Lossy encyclopedia

https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/

Simon Willisonは、LLM（大規模言語モデル）を「欠損のある百科事典」と定義し、その本質的な情報圧縮による限界を理解し、特定のタスクでは具体的な情報提供が必須であると提唱します。

**Content Type**: Opinion & Commentary

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 87/100 | **Overall**: 84/100

**Topics**: [[LLM Limitations, Prompt Engineering, Generative AI, Knowledge Representation, Practical AI Usage]]

Simon Willisonは、LLM（大規模言語モデル）を「欠損のある百科事典（lossy encyclopedia）」と捉えるべきだと提唱します。これは、LLMが膨大な事実を圧縮して記憶しているものの、その圧縮過程で詳細が失われる「非可逆的」な性質を持つためです。この視点は、ウェブアプリケーションエンジニアがLLMの能力と限界を理解する上で極めて重要です。

なぜこれが重要かというと、LLMを「すべてを知っている完璧なデータベース」として扱うと、特に専門的で具体的なタスクにおいて期待を裏切られる可能性が高いからです。例えば、Hacker Newsのコメントで言及されたZephyrプロジェクトの特定のハードウェア（Pi Pico with st7789 spi display drivers）向けボイラープレートコードのような、極めて精密な情報を「知っている」ことを期待するのは、LLMの本質に反します。LLMは、このような「可逆的な百科事典」でしか答えられないような詳細な事実の正確な再現には向いていません。

この洞察が示唆するのは、LLMを「与えられた事実に従って動作するツール」として活用することです。もし特定の、正確な情報が必要な場合は、LLMにそれを「知っている」ことを期待するのではなく、正しい具体例や参照情報そのものをプロンプトに含めて与えるべきです。これにより、LLMは提供された高品質な情報を基に、より関連性の高い、正確なアウトプットを生成する能力を発揮します。このアプローチは、コード生成、特定のライブラリの利用、複雑な技術問題の解決など、日々の開発作業でLLMをより効果的に活用するための鍵となります。LLMの「非可逆性」を理解し、それを考慮したプロンプト設計を行うことで、開発者はAIを強力なアシスタントとして最大限に活用できるようになります。