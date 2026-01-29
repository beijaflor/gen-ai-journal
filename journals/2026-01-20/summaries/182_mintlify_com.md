## install.md：AIエージェントによる自動実行を標準化するインストール手順の新規格

https://www.mintlify.com/blog/install-md-standard-for-llm-executable-installation

**Original Title**: install.md: A Standard for LLM-Executable Installation

AIエージェントがソフトウェアのインストールを自律的に実行できるようにするための、構造化されたMarkdown規格「install.md」を提案する。

**Content Type**: Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 93/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[AI Coding, LLM Agents, Documentation, DevTools, Standardization]]

Mintlifyは、AIエージェントがソフトウェアのインストールを自律的に実行できるようにするための新しいMarkdown標準規格「install.md」を提案した。現在、多くの開発者ドキュメントは人間が読むことを前提に書かれており、エージェントにとっては「行間を読み取る」ことが難しく、環境構築のような定型的なタスクの自動化において摩擦が生じている。この規格は、その摩擦を解消し、エージェントが確実に行動できる形式を定義するものである。

筆者は、従来の「curl | bash」によるインストール方法には透明性の欠如という問題があると指摘している。これに対し、install.mdは人間が読めるMarkdown形式であるため、実行前に内容を容易にレビューできる。また、LLMは環境（OSやパッケージマネージャーの種類など）を自動検出し、指示された「目的（OBJECTIVE）」を達成するために手順を動的に適応させることができる。これにより、開発者は複雑な条件分岐を持つインストールスクリプトを記述・メンテナンスする手間から解放され、LLMの推論能力に「環境ごとの微細な調整」を委ねることが可能になる。

install.mdの構造には、エージェントをガイドするための特定のキーワードが含まれる。H1での製品名、ブロック引用による製品説明、そして「自律的に実行せよ」という直接的なアクションプロンプトに続き、成功条件（DONE WHEN）や具体的なTODOリストが定義される。これにより、エージェントは自らの進捗を把握し、正しくインストールが完了したかを検証できる仕組みとなっている。

本規格は、先行して普及しつつある「llms.txt」を補完するものである。llms.txtがライブラリの知識をLLMに提供するものであるのに対し、install.mdは具体的なアクション（セットアップ）に特化している。Mintlifyを利用しているプロジェクトでは既にこのファイルが自動生成される機能がロールアウトされており、SDKやCLIの導入をエージェントに丸投げできる環境が整いつつある。筆者は、これが将来的にエージェントによる開発フローの標準的な入り口になると主張している。エージェントが「yak-shaving（本題に入る前の雑用）」を肩代わりするための、極めて実効性の高い提案と言える。