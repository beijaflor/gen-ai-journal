## `claude-chill`: Claude Codeのターミナル描画ラグを解消するRust製プロキシ

https://github.com/davidbeesley/claude-chill

**Original Title**: claude-chill: A PTY proxy that tames Claude Code's massive terminal updates using VT-based rendering.

Claude Codeが生成する巨大なターミナル更新データを制御し、差分描画によってラグやチラつきを解消する軽量プロキシツールです。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 89/100 | **Overall**: 92/100

**Topics**: [[AI Coding Tools, Claude Code, CLI Tools, Rust, Developer Experience]]

Anthropicが提供するエージェント型CLIツール**Claude Code**は、描画のチラつきを抑えるために出力を同期ブロックでラップしますが、これが数千行に及ぶ全画面の再描画を頻繁に引き起こし、ターミナルの動作を著しく重くする課題があります。**claude-chill**はこの問題を解決するために開発されたRust製の**PTYプロキシ**です。

本ツールはターミナルと**Claude Code**の間に介在し、内部の**VT100エミュレータ**で画面状態を追跡します。巨大な同期ブロックをインターセプトし、実際の画面上の差分のみをレンダリングしてターミナルへ送信することで、描画負荷を劇的に軽減します。また、便利な機能として**Lookback Mode**を備えており、特定のキー（デフォルトは**Ctrl+6**）を押すことで、過去の出力履歴をバッファから一括出力して自由にスクロール確認することが可能です。さらに、**Kitty keyboard protocol**を自動検出し、**Ghostty**や**WezTerm**などのモダンなターミナル環境でも透過的に動作する設計となっています。

低スペックなPC環境や、描画パフォーマンスの低いターミナルエミュレータを使用しながら、快適に**Claude Code**を利用したいエンジニアに最適なツールです。