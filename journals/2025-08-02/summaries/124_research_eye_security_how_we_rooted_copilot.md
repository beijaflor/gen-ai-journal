## How we Rooted Copilot

https://research.eye.security/how-we-rooted-copilot/

セキュリティ研究者がMicrosoft Copilot EnterpriseのPythonサンドボックスにおける権限昇格の脆弱性を突き止め、rootアクセスを達成した。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 94/100 | **Annex Potential**: 96/100 | **Overall**: 96/100

**Topics**: [[AIセキュリティ, サンドボックスエスケープ, 権限昇格, GitHub Copilot Enterprise, Jupyter Notebookセキュリティ]]

マイクロソフトのGitHub Copilot Enterpriseに搭載されたライブPythonサンドボックス（Jupyter Notebook）に、深刻な権限昇格の脆弱性が発見されました。Eye Securityの研究チームは、このサンドボックス環境がシステム上でLinuxコマンドを実行できることを突き止め、特に興味深いことに、root権限で実行される`entrypoint.sh`スクリプトが、フルパスを指定せずに`pgrep`コマンドを呼び出している点に着目しました。

この脆弱性の核心は、`$PATH`環境変数にありました。`ubuntu`ユーザーが書き込み可能な`/app/miniconda/bin`ディレクトリが、システムにインストールされている正規の`/usr/bin`よりも優先して`$PATH`に設定されていたため、攻撃者は自身の悪意ある`pgrep`スクリプトを`/app/miniconda/bin`に配置することが可能でした。これにより、`entrypoint.sh`が`pgrep`を呼び出すたびに、攻撃者のスクリプトがroot権限で実行され、サンドボックス内でrootアクセスを奪取することに成功しました。

ウェブアプリケーションエンジニアにとって、この事例は、日常的に利用するAI開発ツールのセキュリティに深く関連します。AIが生成するコードやAIが動く環境の信頼性は、開発プロセス全体のセキュリティに直結します。今回の脆弱性は、たとえ主要ベンダーのツールであっても、基盤となるインフラストラクチャに古典的なセキュリティホールが存在し得ることを示しています。特に、開発環境におけるサンドボックスの分離と、実行されるプロセスの権限管理の重要性を再認識させるものです。この種の発見は、我々がAIツールを導入・利用する際に、単なる機能性だけでなく、そのセキュリティ実装に対しても厳格な目を向けるべきだという強いメッセージとなります。