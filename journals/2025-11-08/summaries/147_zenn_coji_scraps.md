## コーディングエージェントが useEffect を多用するのがつらい

https://zenn.dev/coji/scraps/c890994e6d42b4

コーディングエージェントによるReactの`useEffect`不適切多用問題に対し、外部システムとの同期に限定した利用ポリシーとアンチパターンを明確化し、堅牢なコード生成を促す指針を提示します。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Coding Agents, React Hooks, Best Practices, Front-end Development, Code Quality]]

Zennの記事「コーディングエージェントが useEffect を多用するのがつらい」は、AIコーディングエージェントがReactの`useEffect`フックを不適切に多用しがちな現状に警鐘を鳴らし、その解決策として明確な`useEffect`利用ポリシーを提示しています。著者は、`useEffect`はAPIコール、WebSocket接続、ブラウザAPIなど「外部世界との同期」のみに限定すべきだと主張。プロップや派生値のローカルステートへのコピー、フラグ変更に応じたロジック実行、イベントハンドラではなくエフェクト内でのユーザーアクション処理、空の依存配列での一度きりの初期化（`useMemo`を推奨）といったアンチパターンを具体的に挙げています。

このポリシーは、堅牢で保守しやすいコードを生成するため、レンダリング中の計算、イベントハンドラでのユーザーアクション処理、真の副作用のみにエフェクトを限定し、各`useEffect`には同期対象の外部リソースを短いコメントで明記することを原則としています。これにより、AIが生成するコードの品質向上とReactのベストプラクティス遵守が期待され、Webアプリケーションエンジニアがエージェントの出力コードをレビューする際の具体的な指針となります。