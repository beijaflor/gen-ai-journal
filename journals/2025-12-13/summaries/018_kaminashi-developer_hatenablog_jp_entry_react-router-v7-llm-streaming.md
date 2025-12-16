## React Router v7でLLMのストリーミングレスポンスを実装する

https://kaminashi-developer.hatenablog.jp/entry/react-router-v7-llm-streaming

ウェブアプリケーションエンジニア向けに、React Router v7でLLMのストリーミングレスポンスを実装する具体的な方法を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[React Router, LLMストリーミング, ReadableStream API, Resource Routes, フロントエンド開発]]

LLMは応答生成に時間がかかるため、ユーザー体験向上のためにはストリーミングによる逐次表示が不可欠です。本記事は、React Router v7が提供する標準のストリーミング機能が、LLMのような逐次データ表示には対応していないという課題を指摘し、ReadableStream APIを直接活用した実装パターンを提示しています。

React Router v7の標準ストリーミングはPromiseの遅延読み込みを目的としており、`useActionData`フックはデータをJSONとしてパースしてしまうため、ReadableStreamをそのまま扱うことができません。そこで筆者は、UIコンポーネントを持たない`Resource Routes`をAPIエンドポイントとして利用するアプローチを提案。バックエンド側でBedrockモデルなどのLLM API（AsyncIterable形式でレスポンスを返すことが多い）を呼び出し、その応答を`ReadableStream`に変換して`Response`として返します。

クライアント側では`fetch` APIで`Resource Routes`を直接呼び出し、`response.body.getReader()`から取得したリーダーを使ってチャンクを逐次的に読み込み、デコードしたテキストをUIに順次追加していきます。これにより、LLMの生成内容が少しずつ表示されるストリーミング体験を実現します。

さらに、JSON形式のチャンクをクライアントで処理したいケース向けに、サーバー側で各チャンクに改行コードを追加してJSON Lines形式で返し、クライアント側でバッファリングと改行区切りでのJSONパースを行う実装も紹介。この手法はReact Router v7の標準的な使い方からは一部逸脱するものの、`Resource Routes`を活用することで既存アーキテクチャから大きく外れることなくストリーミング処理を統合できる点が強調されており、LLMだけでなく大容量ファイルのダウンロード進捗表示など多様なユースケースに応用できる実用的な知見が提供されています。