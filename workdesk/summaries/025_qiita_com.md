## Claude Code の language 設定を毎セッション変えて、起動時に自己紹介させる

https://qiita.com/skawaji/items/a87dac2970195a789b1f

活用が進む Claude Code CLI のライフサイクル Hook を利用し、セッションごとに AI の「人格」を自動的に切り替える仕組みを解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[Claude Code, CLI, Automation, Persona, Developer Experience]]

**Claude Code** の設定項目である **language** とライフサイクル **hooks** を組み合わせ、セッションごとに AI の「人格（振る舞い）」を自動でランダムに変更するユニークなカスタマイズ手法が紹介されています。

具体的には、セッション終了時に呼び出される **SessionEnd** で **Bashスクリプト** を実行し、**settings.json** 内の **language** パラメータを次回の候補（関西弁、戦術家、熱血キャラなど）に動的に書き換えます。さらに、起動時の **SessionStart** で自己紹介を促すことで、そのセッションで対話する「相手」を即座に把握できる仕組みを構築しています。著者はさらに、**Gitのブランチ名**（fixやfeatureなど）や **未コミットファイル数** といった開発状況に応じて AI の態度を変化させたり、「語尾・性格・専門家視点」という **3つの軸** を掛け合わせて **1,728通り** ものバリエーションを生成する高度な自動化アイデアを提示しています。

単調になりがちな長時間の CLI 操作に変化を与え、**開発体験（DX）** を向上させたい **Claude Code** ユーザーにとって、ツールの拡張性を引き出し、作業を飽きさせないための実践的なガイドとなっています。