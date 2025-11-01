## ZedでCodexが稼働開始

https://zed.dev/blog/codex-is-live-in-zed

**Original Title**: Codex is Live in Zed

Zedは、Agent Client Protocol (ACP) を介してOpenAIのCodexのサポートを開始し、ユーザーからの強い要望に応えつつ、異なるAIエージェントの統合における技術的な学びを共有しました。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[Zed IDE, OpenAI Codex, Agent Client Protocol, AIコード補完, IDE統合]]

Zedは、ユーザーからの強い要望に応え、Agent Client Protocol (ACP) を通じてOpenAIのCodexのサポートを正式に開始しました。これにより、Claude CodeやGemini CLIといった既存のエージェントと同様に、ZedユーザーはIDE内で直接Codexを利用できるようになります。

この統合の主な利点は、開発者がコードを書く際にIDEを離れることなく、AIエージェントの強力な機能にアクセスできる点です。これにより、コンテキストスイッチングが減少し、開発フローの維持に貢献します。Zedは、Codexの利用に関する課金や法的取り決めはユーザーとOpenAIの間で直接行われ、プロンプトやコードがZedのサーバーを経由することはないと明確に述べており、プライバシーとセキュリティへの配慮を強調しています。また、Codex-ACPアダプターはオープンソース化され、Zed以外での利用も可能にしています。

今回の統合を通じて、Zedの開発チームは異なるエージェントの動作特性から重要な教訓を得ました。特に、Codexがターミナルコマンドを独自プロセスで実行し、その出力バイトをクライアントにストリームするという点が挙げられます。これは、他のエージェントがクライアントにコマンド実行を要求する従来の方式とは異なります。

この違いは、ターミナルの動作モード、特に擬似ターミナル（PTY）モードの採用に関する考察につながりました。PTYモードはインタラクティブな操作や色付きの出力を可能にする一方で、エージェントが `git rebase --continue` のようなインタラクティブなコマンドでデッドロックに陥るリスクがあります。非PTYモードはインタラクティブ性は劣るものの、エージェントが停止するケースを減らせるという利点があり、どちらのモードにも一長一短があることが示されました。これらの学びは、将来のACP統合における推奨事項に役立つと筆者は説明しています。

ACP自体はZedに限定されず、Neovim、Emacs、そしてJetBrainsのIDE群といった他のエディタでも採用が広まっています。Zedは今後、ACPアダプターの開発から、プロトコルの未来に関するコミュニティとの協力に焦点を移していく意向を示しており、Agent-based Codingエコシステムのさらなる発展が期待されます。