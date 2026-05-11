## Claude Coworkのオープンソース代替「OpenWork」が登場

https://github.com/different-ai/openwork

**Original Title**: different-ai/openwork

エージェント実行基盤であるopencodeを、非エンジニアでも利用可能な直感的な製品レベルのUIへと変換する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[AI Agents, opencode, Open Source, Tauri, Workflow Automation]]

**OpenWork**は、AIエージェントの基盤となる**opencode**を、開発者向けのCLIから非エンジニアでも扱える製品レベルのUIへと昇華させるオープンソースのデスクトップアプリケーションである。これまでエンジニアに閉じていたエージェント操作を、ワークスペースの選択、進行状況の可視化、実行プランの承認といったガイド付きの直感的なワークフローとして再定義している。

技術的には**Tauri**（**Rust** + **TypeScript**）を採用しており、ローカルで**opencode**を実行するホストモードと、リモートサーバーに接続するクライアントモードの両方をサポートする。**SSE（Server-Sent Events）**によるリアルタイムな進捗ストリーミング、実行プランのタイムライン表示、権限管理機能など、エージェントの挙動を「監査可能」かつ「制御可能」にするための機能が充実している。さらに、**WhatsApp**を介した操作インターフェースなど、既存のチャットツールへの拡張性も備えている。

エージェントを開発者ツールに留めず、チーム内や非技術者向けに安全かつ使いやすい「製品」として提供したいと考えているエンジニア、あるいは**opencode**のエコシステムを活用したワークフロー自動化を検討している開発者に最適である。