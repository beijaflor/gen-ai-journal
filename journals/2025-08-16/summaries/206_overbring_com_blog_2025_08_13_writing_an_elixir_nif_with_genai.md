## I let LLMs write an Elixir NIF in C; it mostly worked

https://overbring.com/blog/2025-08-13-writing-an-elixir-nif-with-genai/

LLM (Grok 3, Gemini 2.5 Flash, GPT-5)を活用し、ElixirのクロスプラットフォームNIFをC言語で開発した体験を詳述し、その過程で明らかになったLLMの強力な支援と顕著な課題を提示する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 100/100

**Topics**: [[Elixir NIFs, C Language Programming, LLM for Code Generation, Cross-platform Development, GitHub Actions CI/CD]]

本稿は、Elixirのファイルブラウザアプリ開発で発生したディスク空き容量のオンデマンド確認ニーズに応えるため、C言語でElixir NIFを構築した経緯を詳細に記している。従来の`os_mon`では更新頻度やWindowsでの制約があり不十分だったため、OS内部やC言語の経験が乏しい著者は、Grok 3で初期コードとMakefileを生成させ、Gemini 2.5 FlashやGPT-5と連携してクロスプラットフォーム対応とメモリ安全性の改善を繰り返した。

この試みは、LLMが未経験分野のコーディングをゼロから支援する強力なツールとなり得ることを示した一方、その限界も浮き彫りにした。LLMは過去の改善を「忘れ」たり、矛盾する指示を出したり、自信過剰な誤答を返したりと、人間による根気強いデバッグと丁寧なプロンプト（例：新しいチャットで再開、LLMに質問させる）が不可欠であることが強調される。特にOTPバージョン互換性の問題はLLMでは解決できなかった。

結果として、Linux、macOS、Windows、一部のBSDで動作する実用的なElixirパッケージ「DiskSpace」が完成し、GitHub ActionsによるCI/CDも確立された。本記事は、LLMがコーディングにおける「AGIの前兆」」という過剰な宣伝とはかけ離れた「単なるツール」であることを示し、ウェブアプリケーションエンジニアが低レベルなタスクにLLMを適用する際の現実的な期待値と「Human-in-the-loop」の重要性を具体的に示唆する貴重な事例となる。