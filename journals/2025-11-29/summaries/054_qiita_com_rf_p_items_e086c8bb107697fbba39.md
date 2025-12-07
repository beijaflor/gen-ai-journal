## AntigravityがNano Banana Proに対応したらしいので画像生成させてみる

https://qiita.com/rf_p/items/e086c8bb107697fbba39

AIアシスタント「Antigravity」の画像生成機能がGoogle DeepMind製「Nano Banana Pro」（別名 Gemini 3 Pro Image）に対応したことを、実際のプロンプトと応答で検証します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[Antigravity, Nano Banana Pro, Gemini, 画像生成AI, AIツール]]

Antigravityがリリース3日目にしてバージョン1.11.5でNano Banana Proに対応したとのことで、筆者はその画像生成能力を検証しています。まず、簡易TODOリポジトリの「かっこいいタイトルロゴ画像」の生成を試みましたが、AIは3パターンを生成しつつも、「Nano Banana Proで作られたものか？」という質問に対し、DeepMind製の独自の組み込みツールを使用していると回答し、Nano Banana Proの使用を否定しました。再度「nano banana proを使って生成してください」と指示しても、同様に理解できない反応が返されました。

次に、公式ポストにあったLP全体のデザイン生成を試みます。「新鮮なバナナのECサイトのLPイメージ画像を生成してください」と指示したところ、Antigravityはイメージ画像を生成した後、指示に反して要件定義や基本設計を行い、Vite+Reactを使った実装までノンストップで動き出してしまいました。これにより、LPデザインの生成自体は短時間だったものの、実装フェーズで10分ほどの時間を要しました。しかも、最初に生成されたイメージ画像と、最終的にコードで実装されたWebサイトの見た目には大きな乖離が見られました。

筆者が最初に生成されたLPイメージの技術について尋ねたところ、Antigravityは「AI画像生成ツール（Imagenなど）」を使用して作成したと回答し、具体的なテキストプロンプトも開示しました。しかし、さらに「nano banana proではない？」と問い詰め、Google検索結果を提示すると、Antigravityは最終的に「その通りです。私が使用した画像生成モデルは、Google DeepMindが開発した最新の画像生成技術（Nano Banana Pro、またの名を Gemini 3 Pro Image）に基づいています」と認めました。

この検証から、Antigravity自体は「Nano Banana Pro」という特定の名称やそれが利用されていることを直接的には認識していない可能性があるものの、Gemini 3.0を使って画像を生成している場合は、実質的にDeepMind製のNano Banana Proが活用されていると結論付けています。つまり、ユーザーが明示的に「Nano Banana Proを使って」と指示する必要はない、というのが筆者の見解です。この検証は、AIツールの内部技術名に対する挙動の不透明さや、プロンプトの出し方による応答の変化を示す興味深い事例と言えるでしょう。