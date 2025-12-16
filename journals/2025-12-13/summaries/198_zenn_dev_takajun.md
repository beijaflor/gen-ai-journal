## Mini PC + 外付けGPUでローカルLLM環境を作った話

https://zenn.dev/takajun/articles/0a3f487decab01

筆者は、Mini PCとOCuLink接続の外付けGPUを用いてローカルLLM環境を構築し、その費用、具体的な構築手順、およびWindowsとUbuntuでのベンチマーク結果を詳細に検証しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[ローカルLLM, 外付けGPU, Ollama, LibreChat, ハードウェアベンチマーク]]

この記事では、自宅でローカルLLM環境を構築する具体的な方法と、そのパフォーマンス検証結果が詳細に報告されています。筆者は、手軽さと省スペース性を重視し、GMKtec Mini PC NucBox M7と、MINISFORUM DEG1（OCuLink対応の外付けGPUドッキングステーション）、NVIDIA GeForce RTX 5060 Ti（VRAM 16GB）を組み合わせてハードウェアを構築しました。

外付けGPUの接続には、PCIe直結よりも速度ロスがあるOCuLink (PCIe 4.0 x4) を採用していますが、これは「気軽に導入できる」「中国製ミニPCを活用できる」「デスクトップPCを組み立てるより省スペース」というメリットを優先したためと説明されています。特にLLMにおいてはVRAM容量が重要であり、MistralやGPT-OSSなどのモデルを動かすには16GBが最低限必要という判断基準が示されています。

構築した環境でOllamaを使ってMistralモデルの推論ベンチマークを実施した結果、GPUなしの状態と比較して、総実行時間が約8.5倍、トークン生成速度が約9.1倍に高速化され、実用レベルの性能向上が確認されました。また、WindowsとUbuntuのデュアルブート環境での比較検証では、GPU使用時・CPU使用時ともにUbuntuの方が若干高速であることが示されており、Windows環境でのWSLなどを介した仮想化レイヤーのオーバーヘッドがパフォーマンス劣化の一因である可能性が指摘されています。

ソフトウェア面では、NvidiaドライバーのインストールからOllama、そしてOllamaと連携するウェブUI「LibreChat」の導入手順まで具体的に解説されています。LibreChatでウェブ検索機能（RAG）を有効にする設定も紹介されており、現代のLLM活用を見据えた実践的な内容となっています。

総額約18万円のコストはChatGPT Plusの年間費用と比較すると決して安くはないものの、筆者は「GPT-OSS-20BやDeepSeekなどが動く実環境」「OCuLink接続の実践知識」「作る経験」という得られた価値は大きく、業務にも活かせるはずだと、この投資を正当化しています。ウェブアプリケーションエンジニアにとって、実際のハードウェア構成やパフォーマンスのボトルネック、OS間の違いといった実践的な知見は、AI関連の開発を行う上で貴重な参考情報となるでしょう。