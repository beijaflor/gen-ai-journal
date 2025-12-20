## AI で再注目された技術やツールたち

https://blog.pokutuna.com/entry/ai-rediscovered-tech-and-tools

AIの台頭により、Server-Sent Events、Pandoc、Markdown、Marp、アクセシビリティツリー、音声入力といった既存の技術やツールが、新たな価値を見出し再注目されていると筆者は指摘する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 87/100 | **Annex Potential**: 86/100 | **Overall**: 80/100

**Topics**: [[Server-Sent Events, Pandoc, Markdown, AIエージェント, アクセシビリティツリー]]

筆者は、AIの急速な進化とコーディングエージェントの普及に伴い、既存の技術やツールが新しい文脈で再評価され、予期せぬ用途で広く使われるようになった現状を解説する。

まず「出世頭」としてServer-Sent Events (SSE)を挙げ、チャットAIのレスポンスのほとんどがSSEで送られていると指摘。逐次的なデータ表示を可能にするSSEは、WebSocketよりもシンプルにリアルタイム通信を実現できるため、AIチャットの応答ストリーミングにおいて重要な役割を担っている。特に、ユーザー入力のPOSTに対してAIがSSEでレスポンスを返す形式が新しい。

次に、多機能なドキュメント変換ツールPandocが再注目されている。2023年頃、AIに論文や資料を読ませるために自前でテキストデータに変換する必要があった際、Pandocがその主要な役割を果たした。Markdown自体も、AIとの構造化テキスト連携における標準的な選択肢となっている。Markdownでスライドを作成するMarpや、MarkdownからGoogleスライドを生成するツールなども、LLMの支援を受けるテキストベースツールの再評価の流れを示している。

PlaywrightのariaSnapshotが用いるアクセシビリティツリーも、AIによるブラウザ操作の文脈で印象的だ。生のHTMLはAIにとってノイズが多いが、アクセシビリティツリーはページ構造をセマンティックに伝え、AIが扱いやすいシリアライズ形式として機能する。

さらに、筆者自身がAIエージェントへの指示出しで文章を書く機会が増えたことから、音声入力の使用が大幅に増加したと述べる。OpenAIのWhisperのような高精度な音声認識モデルの登場により、SuperwhisperやVoiceInkといったデスクトップアプリが普及し、開発者の新しいワークフローに組み込まれている。

その他、ドキュメントツールObsidian、ナレッジグラフを用いたGraphRAG、そしてコーディングエージェント実行のためのサンドボックス技術（非推奨のsandbox-execが活用される例も）もAIの文脈で再注目されていることが述べられている。これらの例は、AI時代において、目新しい技術だけでなく、実績ある既存技術がいかに新しい価値を生み出しているかを示している。