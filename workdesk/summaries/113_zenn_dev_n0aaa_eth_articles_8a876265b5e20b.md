## 🤖 AI UX｜AIチャットを“スルスル”動かすSmooth Text Streaming

https://zenn.dev/n0aaa_eth/articles/8a876265b5e20b

Vercel AI SDK v5を活用し、AIチャットの応答テキストを滑らかに表示するSmooth Text Streamingを実装することで、ユーザー体験が大幅に向上します。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[AIチャットUX, Smooth Text Streaming, Vercel AI SDK, Next.js, LLM開発]]

最近のAIチャットサービスでは、応答テキストが滑らかに表示される「Smooth Text Streaming」がユーザー体験向上に不可欠です。本記事は、テキストが途切れ途切れに表示されることによるユーザーのストレスを解消し、自然な読書体験を提供するこの機能を、Vercel AI SDK v5を用いて効率的に実装する方法を具体的に解説しています。

実装の核となるのは、サーバー側で`streamText()`を利用し、その`experimental_transform`プロパティに`smoothStream()`を組み込む点です。`smoothStream()`はAIモデルから受け取ったテキストを適切な粒度（chunking）に分割し、`delayInMs`で指定されたテンポで整流して表示します。特に日本語の場合、単語区切りが難しいため、正規表現`/[\u3040-\u309F\u30A0-\u30FF]|\S+\s+/`による`chunking`設定が推奨されており、これによりAIの返答がユーザーにとって極めて自然なリズムで読めるようになります。ツール実行イベントなどの非テキスト要素は遅延なく即時送出されるため、機能性とUXの両立が図られています。

フロントエンドでは`useChat`フックと`DefaultChatTransport`が`toUIMessageStreamStreamResponse()`で返されるUI Message Stream（SSE）を解釈し、滑らかな表示を実現します。この実装は、単にAIの応答内容だけでなく、「どのように表示されるか」がUXを大きく左右するというAI時代のUI設計の重要性を浮き彫りにします。AIと人間のインタラクションにおいて、技術的な微調整がユーザーの知覚や満足度に与える影響は大きく、WebアプリケーションエンジニアがAIサービス開発において見落とせないポイントとなるでしょう。