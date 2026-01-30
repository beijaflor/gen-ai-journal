## LLMによるコード生成に特化した超小型プログラミング言語「NanoLang」

https://github.com/jordanhubbard/nanolang

**Original Title**: jordanhubbard/nanolang: A tiny experimental language designed to be targeted by coding LLMs

AIが生成しやすく、曖昧さを排除した構文と強制テスト機能を備えたLLMフレンドリーな言語を提供し、生成コードの信頼性向上を目指す。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[NanoLang, LLM-Friendly, Code Generation, Mandatory Testing, C Transpiler]]

Jordan Hubbard氏によって開発された**NanoLang**は、プログラミングLLMがコードを出力することを前提に設計された、実験的な超小型プログラミング言語です。LLMによる生成コードで頻発する「演算子の優先順位によるロジックの曖昧さ」を解決するため、Lispのような**前置記法**（Prefix Notation）を全面的に採用している点が大きな特徴です。また、すべての関数に対して「shadow」ブロック内での**強制テスト**を言語仕様として義務付けており、AIが生成したコードの妥当性をその場で検証できる堅牢なワークフローを構築しています。

技術面では、**静的型付け**、**デフォルトの不変性**、**C言語へのトランスパイル**によるネイティブ性能の維持など、現代的な機能を備えています。さらに、AIモデルが言語を理解するための専用リファレンス（**MEMORY.md**）や、標準ライブラリを含む形式仕様（**spec.json**）が提供されており、LLMのコンテキストに注入して即座に活用できる「AIフレンドリー」な構成が徹底されています。

AIエージェントによる自動プログラミングの精度を高めたい開発者や、AI時代の新しいプログラミング言語の在り方、**Vibe Coding**などの潮流に関心があるエンジニアは必見のプロジェクトです。