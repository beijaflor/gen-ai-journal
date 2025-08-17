## 【メモ】JaveScriptでコンテンツの内容が変わるページと各LLMの読み込み状況

https://www.baka-ke.com/2025/08/11/javascript-and-llm/

主要なLLMがウェブページをクロールする際、JavaScriptによって動的に生成されたコンテンツではなく、初期HTMLのみを読み込むという実験結果を示します。

**Content Type**: Research & Analysis

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 77/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[LLM挙動, Webクローリング, JavaScriptレンダリング, コンテンツ理解, SEO]]

この記事は、ウェブページを読み込む際の各LLMの挙動を検証した興味深い実験結果を報告しています。JavaScriptによって動的に内容が変化するテストページを用意し、ChatGPT、Perplexity、Claude、NotebookLM、Geminiといった主要なLLMがどのようにコンテンツを認識するかを調査しました。

結果は明確でした。対象となった全てのLLMは、JavaScript実行後の動的なコンテンツではなく、ページの初期HTMLのみを読み込んでいることが判明しました。これは、LLMがウェブコンテンツを理解する上で、従来のGoogle検索クローラー（Search ConsoleライブテストではJavaScriptを読み込むことが確認された）とは異なる、重大な制約があることを示唆しています。

この知見は、ウェブアプリケーションエンジニアにとって極めて重要です。現代のウェブサイトの多くはJavaScriptに依存してコンテンツを動的に生成しており、LLMがウェブ情報を基にしたRAG（Retrieval-Augmented Generation）や、ウェブを操作するエージェントとして機能する場合、重要な情報を見落とすリスクがあることを意味します。例えば、ユーザーがログイン後に表示されるコンテンツや、クライアントサイドでデータをフェッチしてレンダリングされるSPA（Single Page Application）のコンテンツは、LLMには認識されない可能性が高いのです。

したがって、LLMが動的コンテンツを正確に理解するためには、サーバーサイドレンダリング（SSR）や静的サイトジェネレーション（SSG）の導入、あるいはLLM向けの専用APIや構造化データフィードの提供といった、別のアプローチを検討する必要があります。この実験は、LLMを活用したシステム開発において、データの取得源と認識能力の限界を深く理解することの重要性を浮き彫りにしています。