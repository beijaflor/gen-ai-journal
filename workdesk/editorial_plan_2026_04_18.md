# Editorial Plan — Journal 2026-04-18

## Planning Status
- [x] AI theme analysis complete
- [x] Human review completed
- [x] ✅ APPROVED — Ready for STEP_04

---

## 今週のハイライト（下書き）

4月第3週は、Anthropicが Claude Opus 4.7・Routines・Desktop 再設計の3連続リリースを行い、Cloudflare が「Agents Week」として10本以上のエージェント向けインフラ記事を一斉公開した。それらの"賑やかさ"の裏側では、まだ一般公開されていないモデル「Claude Mythos Preview」の危険性が英国 AI 安全研究所（AISI）の評価報告として明らかになり、米財務省・FRB が金融機関トップを集めてリスク警告を行うという異例の事態が起きた週でもある。

日本語コミュニティでは「ハーネスエンジニアリング」という概念の定義をめぐる議論が活発に展開された。「モデルの賢さよりも、エージェントを動かす環境設計が勝敗を決める」という主張が複数の独立した記事で展開されており、概念の共通言語が形成されつつあることが観察できる。

一方で、AI コーディングツールの普及による「人的コスト」の告発も目立った。シニアエンジニアの認知過負荷とバーンアウト、AI 生成コードの「理解の負債」、ヴァイブコーディングの医療現場での失敗事例など、生産性向上の裏側にある構造的な問題が具体的なデータとともに報告された。オープンソース側では、AlibabaのQwen3.6-35B-A3B が Simon Willison のベンチマークで Claude Opus 4.7 の SVG 生成精度を上回り、ローカル実行可能な中規模モデルがフロンティアモデルに肉薄し始めたことが示された。

---

## テーマ構成（6テーマ・計22記事案）

---

## テーマ1: Claude Opus 4.7・Routines・Desktop 再設計 — Anthropicの4月大型アップデート

**記事ID一覧:**
- 193. https://www.anthropic.com/news/claude-opus-4-7
- 212. https://claude.com/blog/introducing-routines-in-claude-code
- 161. https://claude.com/blog/claude-code-desktop-redesign
- 042. https://claude.com/blog/subagents-in-claude-code
- 245. https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code

**テーマ紹介（2-3文）:**
Anthropicは今週、フラッグシップモデル Claude Opus 4.7 のリリースに加え、CLI ツール Claude Code に「Routines」機能（定型ワークフローの自動実行）とデスクトップ版の UI 再設計を相次いでリリースした。Routines はスケジュール実行・イベントトリガー・メール/カレンダー連携の3形式をサポートし、人間の承認なしに繰り返しタスクを処理する。同時に、サブエージェントの公式ガイドと Opus 4.7 を Claude Code で使うベストプラクティスも公開され、エコシステム全体が新モデルを中心に刷新された。

**アセンブリパターン案:** Progressive-Sequence（概要 → Routines詳細 → 実装ガイド → ベストプラクティス）

---

## テーマ2: Claude Mythos Preview と AI安全保障 — 40社限定公開に至る経緯と AISI評価

**記事ID一覧:**
- 065. https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
- 064. https://thezvi.substack.com/p/claude-mythos-the-system-card
- 031. https://www.itmedia.co.jp/news/articles/2604/10/news131.html
- 005. https://www.politico.com/news/2026/04/08/d-c-circuit-rejects-anthropic-plea-to-pause-supply-chain-risk-label-00864880
- 169. https://1password.com/blog/beyond-patching-building-a-mythos-ready-security-program

**テーマ紹介（2-3文）:**
Anthropicの未公開モデル「Claude Mythos Preview」について、英国 AI 安全研究所（AISI）が公式評価を公開した。CTF 課題で 73% の成功率を記録し、32 段階の企業ネットワーク攻撃シミュレーション（TLO）をフロンティアモデルとして初めて完遂した（10 回中 3 回）。米財務省・FRBが主要銀行CEOに警告を行うなか、Anthropicは供給チェーンリスク指定に対する控訴も棄却されており、モデルの能力拡大と規制・安全保障の緊張が高まっている。

**アセンブリパターン案:** Single-Focus with supplementary perspectives（AISI評価を主軸に、システムカード分析・金融警告・法的動向を補足）

---

## テーマ3: ハーネスエンジニアリング論争 — 「環境設計」が競争優位になる時代

**記事ID一覧:**
- 204. https://zenn.dev/watany/articles/d8b692bbca65a3
- 202. https://zenn.dev/sasadango28/articles/claude-code-harness-engineering-20260415
- 201. https://zenn.dev/murasaki/articles/d9fea8b4e730ce
- 160. https://note.com/rk611/n/n8424c56f4fa5
- 015. https://zenn.dev/mkj/articles/d700c07675d7b1
- 152. https://zenn.dev/ubie_dev/articles/sec-agent-harness-eng

**テーマ紹介（2-3文）:**
「ハーネスエンジニアリング」の定義をめぐり、日本語コミュニティで複数の独立した記事が展開された週だった。watany 氏がハーネスという用語の混乱を整理し、sasadango28 氏がClaudeソースコード流出を元に5層構造を提示し、murasaki 氏はエージェント開発の成熟度を8レベルで定義した。mkj 氏は「RL 環境の共有」まで含めた「大環境時代」の到来を論じ、Ubie の事例ではセキュリティエージェント向けのハーネス設計が実装レベルで報告されている。

**アセンブリパターン案:** Multi-Perspective（各執筆者が独立して同じ概念を定義・拡張しており、それぞれの視点を並列提示）

---

## テーマ4: エージェント・インフラの拡張 — CloudflareのAgents WeekとGitHubのAPM

**記事ID一覧:**
- 057. https://blog.cloudflare.com/welcome-to-agents-week/
- 056. https://blog.cloudflare.com/durable-object-facets-dynamic-workers/
- 213. https://github.com/microsoft/apm
- 216. https://microsoft.github.io/apm/
- 174. https://vercel.com/blog/a-new-programming-model-for-durable-execution
- 218. https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/

**テーマ紹介（2-3文）:**
Cloudflare が「Agents Week」と銘打ち、エージェント向けメモリ・ブラウザ・Email・AI 検索（AutoRAG）・AI プラットフォーム・Durable Object Facets など10本以上の機能を一斉公開した。同時期に GitHub/Microsoft は「APM（Agent Package Manager）」という、エージェントが使うツールと権限セットを npm のように管理するパッケージシステムを発表し、Vercel はサーバーレスの「Durable Execution」モデルを提案した。これらは「エージェントが実行環境・状態管理・ツール依存関係を持つ独立したソフトウェア単位として扱われる時代」への移行を示す。

**アセンブリパターン案:** Single-Focus（Cloudflareビジョン） + Supplementary（GitHub APM・Vercel）

---

## テーマ5: AIコーディングの人的コスト — バーンアウト・認知負債・「10倍」の実態

**記事ID一覧:**
- 067. https://techtrenches.dev/p/the-human-cost-of-10x-how-ai-is-physically
- 055. https://www.oreilly.com/radar/comprehension-debt-the-hidden-cost-of-ai-generated-code/
- 094. https://www.tobru.ch/an-ai-vibe-coding-horror-story/
- 144. https://heidenstedt.org/posts/2026/ai-assisted-cognition-endangers-human-development/

**テーマ紹介（2-3文）:**
AI コーディングツールの普及が「10 倍の生産性」をもたらす一方で、シニアエンジニアが AI 生成コードのレビュー負荷で物理的な燃え尽きに追い込まれているとの告発記事が話題となった。O'Reilly の Addy Osmani は「理解の負債（Comprehension Debt）」という概念を提示し、コード生成速度が人間の理解速度を超えることで生じるリスクを論じた。ヴァイブコーディングの医療現場での失敗事例や、AI 支援による認知発達への影響など、生産性の裏側にある構造的課題が複数の角度から報告された週だった。

**アセンブリパターン案:** Progressive-Sequence（個人事例 → 構造的分析 → 教育・認知開発への影響）

---

## テーマ6: ローカルLLMとオープンソース競争 — Qwen3.6がClaude Opus 4.7を超えた瞬間

**記事ID一覧:**
- 191. https://qwen.ai/blog?id=qwen3.6-35b-a3b
- 197. https://simonwillison.net/2026/Apr/16/qwen-beats-opus/
- 107. https://ai.meta.com/blog/introducing-muse-spark-msl/
- 061. https://medium.com/google-cloud/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4

**テーマ紹介（2-3文）:**
Alibaba が 4 月 16 日に公開した Qwen3.6-35B-A3B は、35B パラメータ・3B アクティベーション（MoE）設計で SWE-bench Verified 73.4% を達成し、ラップトップで動作する。Simon Willison の SVG 生成ベンチマークでは、Claude Opus 4.7 が自転車フレームの描画に失敗した一方で Qwen3.6 が正確に描写し、特定タスクでの逆転が観測された。一方、Meta は音楽生成モデル「Muse Spark」をオープンソースではなくクローズドな API として公開し、Llama 路線からの転換を示した。

**アセンブリパターン案:** Debate-Contrast（オープン・ローカルモデルの台頭 vs クローズド化の流れ）

---

## 記事選定サマリー

| テーマ | 記事数 | 主なシグナル |
|--------|--------|-------------|
| Anthropic 大型アップデート | 5 | 193⭐(Supabase), 212⭐(Supabase) |
| Claude Mythos 安全保障 | 5 | 065(Supabase upvote) |
| ハーネスエンジニアリング論争 | 6 | 015(Supabase upvote), 160(Supabase upvote), 201(Supabase upvote) |
| エージェント・インフラ | 6 | 213(Supabase upvote), 216(Supabase upvote) |
| AIコーディングの人的コスト | 4 | — |
| ローカルLLM・OSS競争 | 4 | — |
| **合計** | **30** | |

> ⚠️ 注意: curation_flags.md の記事 ID は Supabase 内部 ID であり、sources.md の連番とは **一致しない**。上表の記事 ID は sources.md の連番を使用している。curation_flags.md のシグナルを参照する場合は URL で照合すること。

---

## 選定外・注意点

**Supabase フラグがあるが sources.md に存在しない記事（要確認）:**
- https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/ (Supabase ⭐)
- https://takoratta.hatenablog.com/entry/2026/04/09/085051 (Supabase ⭐)
- https://agentcommunity.org/ (Supabase ⭐)
- https://www.oreilly.com/radar/the-missing-mechanisms-of-the-agentic-economy/ (Supabase ⭐)
- https://addyosmani.com/blog/code-agent-orchestra/ (Supabase ⭐)
- https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/ (Supabase ⭐)
- https://cursor.com/ja/blog/cursor-3 (Supabase ⭐)
- https://cozy-starburst-e4f699.netlify.app/ (Supabase ⭐)

これらはブラウジング中に Supabase 管理画面でフラグを立てたが、workdesk/sources.md に追加されず要約が生成されていない。STEP_04 でこれらを含めることはできない。

**テーマ4 記事数が多すぎる場合の削減候補:**
- 218（gh skill）は単独で価値が低い。APM（213/216）と Cloudflare の主要記事に絞るのが良い。

**テーマ3 記事数が多い場合の削減候補:**
- 152（Ubie セキュリティハーネス）は詳細な実装記事として価値があるが、テーマが重くなる場合は除外可能。

---

## 次ステップ

1. ✏️ **人間レビューゲート**: 各テーマの記事選定・紹介文を確認
2. 承認後: STEP_04（メインジャーナルキュレーション）へ進む
3. 記事IDを themes 別に整理した `workdesk/curated_journal_sources.md` を作成

---

*Generated: 2026-04-26*
