## Wasm-agents: AI agents running in your browser

https://blog.mozilla.ai/wasm-agents-ai-agents-running-in-your-browser/

Mozilla.aiは、WebAssemblyとPyodideを活用し、ブラウザ内で直接動作するAIエージェント「Wasm-agents」を開発しました。

[[WebAssembly, Pyodide, AIエージェント, ブラウザ内実行, 開発ワークフロー]]

Mozilla.aiが発表した「Wasm-agents」は、AIエージェントをブラウザ内で直接実行可能にする画期的な技術です。これは、WebAssembly (Wasm) とPyodideを利用することで、PythonコードをWebブラウザ上でほぼネイティブの速度で動作させることを実現しています。これにより、AIエージェントの実行に必要な追加のツールやフレームワークのインストールが不要となり、単一のHTMLファイルとしてUIとエージェントのコードを内包できるため、オープンソースエージェントの導入障壁を大幅に低減します。

Wasm-agentsは`openai-agents-python`ライブラリを基盤とし、OpenAI互換APIを通じてOpenAIモデルや自己ホスト型モデル（HuggingFace TGI, vLLM, Ollamaなど）と連携可能です。これにより、開発者はブラウザのサンドボックス環境内で、会話型エージェント、リクエストルーティングを行うマルチエージェントシステム、ツール呼び出し機能を持つエージェントなど、多様なAIアプリケーションを構築できます。

この技術は、AIエージェントの配布と利用を簡素化し、ユーザーが手軽にAI機能を体験できる道を開きます。特に、ローカルでの実行とデータ保護の可能性は、プライバシーを重視するアプリケーション開発において重要な意味を持ちます。CORSの問題や大規模モデルの要件といった課題は残るものの、ブラウザベースのAIエージェントは、今後のWebアプリケーション開発に大きな影響を与えるでしょう。

---

**編集者ノート**: Webアプリケーションエンジニアにとって、このWasm-agentsの登場は、AI機能の提供方法に革命をもたらす可能性を秘めています。これまでサーバーサイドで実行されていたAIモデルやエージェントが、ブラウザ上で直接動作するということは、ユーザー体験の向上、リアルタイム性の確保、そしてサーバーコストの削減に直結します。特に、PyodideによるPythonコードのブラウザ実行は、既存の豊富なPython製AIライブラリをWebフロントエンドに持ち込めることを意味し、開発の自由度を飛躍的に高めます。

将来的には、複雑なAI処理をクライアントサイドで完結させる「エッジAI」の普及が加速し、Webアプリケーションはよりリッチでインタラクティブなものになるでしょう。例えば、オフラインでも動作するAIアシスタントや、ユーザーのデバイスリソースを活用したパーソナライズされたAI機能などが、標準的なWeb技術で実現可能になります。これにより、Webアプリケーション開発のスキルセットに、ブラウザ内AIの最適化やWasmの知識が不可欠となる時代が到来すると予測します。

