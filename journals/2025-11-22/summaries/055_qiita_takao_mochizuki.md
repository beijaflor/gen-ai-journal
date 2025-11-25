## 【完全版】Gemini 3 を CLI で使う方法まとめ（インストール → 認証 → モデル選択まで網羅）

https://qiita.com/Takao-Mochizuki/items/089124b23a2053d9b822

この記事は、Google Gemini 3をCLIで活用するための、インストールから認証、モデル選択までの全手順を網羅し、開発フローを高速化する方法を詳述する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Gemini CLI, Google Gemini 3, 開発ツール連携, LLM活用, CLI認証]]

本記事は、Google Gemini 3をコマンドラインインターフェース（CLI）から利用するための包括的なガイドを提供しています。著者は、初期セットアップからモデル選択まで体系的に解説することで、開発者がGemini CLIを迅速に導入し、その強力な機能を活用して開発フローを高速化することを目指しています。

まず、Gemini CLIの利用にはNode.js v20以上、npm v10以上、およびGoogleアカウントが前提条件となります。インストールは`npm install -g @google/gemini-cli`コマンドで簡単に行え、`npx`を使った一時的な試用も可能です。

初期設定では、CLI起動後にGoogleアカウント連携による認証が推奨されています。ブラウザでのログインと権限許可を経て、ターミナルからの利用が可能となります。

最も重要なステップは、Gemini 3を利用可能にするための「Preview Features」の有効化です。CLI内で`/settings`コマンドを実行し、「Preview Features」を`true`に切り替えることで、Gemini 3モデルへのアクセスが開かれます。この設定後、`/model`コマンドでモデル選択画面を開くと「Gemini 3 is now enabled.」と表示され、Gemini 3系のモデルが利用可能な状態になります。著者は「Autoモード」を推奨しており、これによりGemini 3系が自動的に優先利用されると説明しています。

著者は、Gemini 3の推論能力が大幅に向上している点を強調し、CLIと組み合わせることで開発体験が飛躍的に向上すると述べています。特に「Preview FeaturesのON」と「モデル選択画面でのGemini 3有効化の確認」の2点が、Gemini 3を最大限に活用するための鍵であるとまとめました。記事の最後に、著者はこのガイドが実際のCLI操作ログと動作確認に基づいていることを付記しています。