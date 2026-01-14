この記事は、技術ブロガーのきしだ氏（id:nowokay）による、**ComfyUI上でQwen-Image（特にQwen-Image-Edit）を使用して、画像内に正確な日本語を描写させる手法**についての解説です。

主な内容は以下の通りです。

### 1. 背景と解決策
*   **課題:** Qwen-Imageは通常、日本語のテキストを画像内に正しく描くことができません。
*   **解決策:** 「Nano Banana Pro」というモデルの手法を参考に、**あらかじめテキストを画像としてレンダリングし、それをQwen-Image-Editに読み込ませる**ことで、破綻なく日本語を配置させます。

### 2. 公開されたカスタムノード：`comfyui-text-renderer`
きしだ氏は、この手法を簡単に行うためのComfyUI用カスタムノードを作成し、GitHubで公開しています。
*   **リポジトリ:** [https://github.com/kishida/comfyui-text-renderer](https://github.com/kishida/comfyui-text-renderer)
*   **特徴:** テキストを画像化してモデルに渡せます。縦書きにも対応しており、複数のノードを組み合わせることで場所ごとにフォントを使い分けることも可能です。

### 3. インストール方法
記事では2通りの方法が紹介されています。

*   **方法A：Git clone（推奨）**
    `ComfyUI/custom_nodes` ディレクトリで以下を実行。
    ```bash
    git clone https://github.com/kishida/comfyui-text-renderer.git
    ```
*   **方法B：ComfyUI Managerから**
    「Install via Git URL」に上記URLを貼り付けます。ただし、セキュリティエラーが出る場合は、`ComfyUI/user/__manager/config.ini` の `security_level` を `weak` に書き換える必要があります。

※フォント名を正しく取得するために、`pip install fonttools` の実行も推奨されています。

### 4. 使い方とポイント
*   **ワークフロー:** 記事内の画像をComfyUIにドラッグ＆ドロップすることで、設定済みのワークフローを導入できます（Chrome推奨）。
*   **柔軟性:** 「画像結合」ノードを使うことで、黒板には白文字、背中の紙には別のフォントといった、複雑な指定が可能です。
*   **結果:** 白地に黒文字でレンダリングしたテキストを、Qwen-Imageが文脈（黒板など）に合わせて自然に合成してくれます。

### まとめ
Qwen-Image単体では難しい「日本語の画像内描写」を、**自作のテキストレンダリングノードと画像編集モデル（Qwen-Image-Edit）を組み合わせることで解決する**という、実用的なTipsとなっています。