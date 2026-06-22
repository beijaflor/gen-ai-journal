# Editorial Plan - Journal 2026-06-20

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement (round 1: Theme 8 removed, articles moved to annex)
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Corpus Overview

- **総ソース数**: 283（うち280件がunified_summaries.mdに集約済み。NYT/WSJ/FTの3件はペイウォール経由でHNスレッドの要約に置換されているため集約から外れているが、サマリーファイル自体は存在し、ID 173/179/258で参照可能）
- **キュレーションフラグ**（Supabase export 2026-06-22）:
  - ⭐ Standout: 196（Anthropic Claude Code Expertise 40万セッション解析）、214（Vercel eve docs）
  - 👍 Upvote: 034（Fable 5でcs-edu site「言語の庭」生成）、053（docswell SDD-in-loop-engineering）、124（Cloud Native ナデラ学習ループ）、170（Artificial Analysis GLM-5-2リーディング）、174（Browser-use Firecracker browser infra）
  - 👎 Downvote: 036（codeheal-scan AI生成コード診断）、209（Ollama×RAG長期記憶ボット）、282（Tailscale SSH Home Mac CC）
- **今週の中核ニュース**:
  - Anthropic「Claude Fable 5/Mythos 5」が米輸出管理指令で6/12にアクセス停止 → SKテレコム経由の中国懸念が真因と判明（WIRED報道）→ Stamosら40名超のサイバー専門家が解除要求公開書簡
  - Vercel Ship 2026で「eve」「Agent Stack」「Vercel Connect」フルセット発表
  - GLM-5.2がオープンウェイトモデルのArtificial Analysis Intelligence Indexで首位
  - Anthropicが40万Claude Codeセッション解析で「ドメイン専門性 > プログラミングスキル」を実証
  - OpenAIの2025年純損失385億ドル財務文書リーク／SpaceXがCursorを600億ドルで買収

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual**
- ✅ 名指しのアンカー × 単一動詞 × 実体ある対象フレーズ
- ❌ 抽象的なカテゴリ名・em-dash・物語的接続詞は避ける

---

### Theme 1: Claude Fable 5/Mythos 5輸出規制発動・SKテレコム経由の中国懸念・Stamos公開書簡が示すAIモデルの地政学化

**Articles (IDs):** 242, 066, 104, 131

**Theme Introduction (2-3 sentences in Japanese):**
2026年6月12日、Anthropicの最新モデル「Claude Fable 5」と「Mythos 5」が米商務省の輸出管理指令を受けて全世界でアクセス停止となった。当初発表された「ジェイルブレイク脆弱性」という公式理由とは別に、WIREDの追加報道では韓国SKテレコムを介した中国側アクセス遮断が真因であった可能性が示され、David Sacks氏の独自報告やKatie Moussouris氏の防御側からの批判、Alex Stamosら40名超のサイバー専門家による解除要求公開書簡といった反応が同時並行で並んだ。

**Editorial Notes:**
- 242: WIRED報道、米ホワイトハウスがSKテレコムへのアクセス遮断を命令、AmazonリサーチャーのMythos脆弱性発見も背景
- 066: David Sacks氏が「FableがMythosにガードレールをかけたモデル、第三者がジェイルブレイク発見、Anthropicが修正拒否」という内幕を報告
- 104: TechCrunch分析、Katie Moussouris氏の指摘により「ジェイルブレイク」が技術的に脆弱な根拠と判明、政治的報復・恣意的介入の側面
- 131: Luta Security CEOによる正面からの批判、輸出規制は防御側のツールを奪い米国のサイバー防衛を損なう

---

### Theme 2: Vercel "eve"・Agent Stack・Vercel Connectが揃えるエージェント時代のフルスタック基盤

**Articles (IDs):** 214, 160, 161, 266

**Theme Introduction (2-3 sentences in Japanese):**
Vercel Ship 2026にて、AIエージェントを「Next.js相当」の標準フレームワークとして構築・運用するための新スタックが一挙に発表された。Markdownでスキル、TypeScriptでツールを記述するファイル構造の「eve」、モデル接続・耐久ワークフロー・サンドボックスを束ねる「Agent Stack」、短寿命OIDCクレデンシャルで外部サービス接続を担う「Vercel Connect」が同週に並び、Vercelがフロントエンドホスティングから「エージェント時代のフルスタックプラットフォーム」へ自社プロダクトを再定義した形となっている。

**Editorial Notes:**
- 214: Vercel eveの公式ドキュメント、耐久セッション・サブエージェント・サンドボックスを標準装備、Vercel内部100エージェント稼働実績（⭐ standout）
- 160: Vercel Ship 2026 リキャップ、Agent Stack・eve・Vercel Connect・Vercel Services・Vercel Agent・BYOC on AWSをまとめて提示
- 161: Agent Stack詳細、AI Gateway・Workflow SDK・Sandbox・Chat SDKの3層構造でエージェント本番運用の足回りを抽象化
- 266: 日本語実践レポート、Eveのディレクトリベース設計を執筆エージェント構築で検証

---

### Theme 3: GLM-5.2フルオープン・Kimi K2.7 Code・Mac StudioでローカルLLMが商用ラインに到達

**Articles (IDs):** 170, 092, 101

**Theme Introduction (2-3 sentences in Japanese):**
Z.ai（Zhipu AI）のGLM-5.2がArtificial Analysis Intelligence Indexでスコア51を獲得し、オープンウェイトモデルの首位に立った（クローズドモデルのGPT-5.5に匹敵するGDPval-AA v2スコア1524）。同週にMoonshot AIはエージェント特化型「Kimi K2.7 Code」（1兆MoE、推論トークン30%削減）を公開、Vicki Boykis氏はM2 Mac 64GBでGemma 4／GPT-OSSをDockerサンドボックス内で運用する実践レポートを公開し、オープンウェイト＋ローカル実行が「実験」フェーズから「商用ライン」フェーズへ移行した週となった。

**Editorial Notes:**
- 170: Artificial Analysis公式評価、GLM-5.2がオープンウェイト首位、GPT-5.5に匹敵するエージェント能力を実証（👍 upvoted）
- 092: Moonshot AI Kimi K2.7 Codeリリース、1Tパラメータ・MoE 32B active、Kimi Code Bench v2で21.8%スコア向上、256Kコンテキスト
- 101: Vicki Boykis氏「Running local models is good now」、M2 Mac 64GB＋LM Studio＋Pi＋Dockerで日常開発を回す実践検証

---

### Theme 4: Anthropic「Claude Code Expertise」40万セッション解析・Addy Osmani新SDLC・Charity Majors『規律強化』論が示すAIコーディング規律の再定義

**Articles (IDs):** 196, 248, 172

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが2025年10月〜2026年4月の約40万件のClaude Codeセッションを解析し、「人間が計画の70%を、Claudeが実行の80%を担う」という分業構造と、プログラミングスキルよりドメイン専門性が成果を決めるという実証データを公開した。同時にAddy Osmani氏は「エージェントの能力はモデル10%・ハーネス90%」とする新SDLC論を、Charity Majors氏は「AIによりコード生成は無料化されたが、エンジニアリング規律はむしろ強化されるべき」とする論考を発表し、AIコーディングの規律と職能像が一斉に再定義された週となった。

**Editorial Notes:**
- 196: Anthropic Research、40万Claude Codeセッション分析、人間が計画70%/Claudeが実行80%、ドメイン専門性が成果を決定（⭐ standout）
- 248: Addy Osmani「The New Software Lifecycle」、エージェントの能力はモデル10%・ハーネス90%、Vibe Codingからエージェント工学への移行
- 172: Charity Majors「AI demands more engineering discipline. Not less」、コードを「キャッシュ」と再定義、短いフィードバックループ＋オブザーバビリティの徹底

---

### Theme 5: Bayer Reliable Agentic RAG・LayerX prompt-log driven・5万スターClaude Code Tipsが体系化するハーネス工学の実践

**Articles (IDs):** 147, 053, 244

**Theme Introduction (2-3 sentences in Japanese):**
Bayer AGとThoughtworksが構築した製薬データプラットフォーム「PRINCE」のマルチエージェントRAG事例（LangGraphベース、Process-reflectとData-reflectの分離、RAGAS／Langfuseによる継続監視）と、LayerX社のプロンプト履歴を意味的にグルーピングしSkill化を自動提案する「prompt-log driven AI workflow」、そしてdocswellで公開された「SDD in loop engineering」（仕様駆動開発をループの中核資産として再定義）が並び、ハーネス工学が個別ハックから組織運用の標準パターンへ昇格しつつある現在地が見えてきた。

**Editorial Notes:**
- 147: Bayer × Thoughtworksの本番品質Agentic AI、LangGraphによるエージェント分業、Process-reflect/Data-reflect、コンテキスト管理＋リトライ＋永続化のハーネス設計
- 053: 仕様駆動開発（SDD）をループエンジニアリングの中核資産として再定義、コンテキストエンジニアリングと実行履歴からの選別（👍 upvoted）
- 244: LayerX、全プロンプトをローカルJSONLに記録、LLM分析で3回以上の反復パターンを自動検出しSkill化通知、PR/CI修正の7割を仕組み化

---

### Theme 6: SoftBank "Patching as a Service" 1万500件発見・JetBrainsプラグイン窃取・Cloudflare脆弱性ハーネスが形作るAIサイバー攻防

**Articles (IDs):** 192, 229, 143

**Theme Introduction (2-3 sentences in Japanese):**
ソフトバンクとOpenAIの合弁SB OAI JapanがGPT-5.5 Cyberを用いた「Patching as a Service」を発表し、自社診断で1万500件の未知脆弱性を発見したと公表。Cloudflareは脆弱性発見ハーネス（VDH）と検証システム（VVS）のアーキテクチャを公開し、2万件以上の候補から7,000件以上の有効修正案を導出した実績を共有した。一方Aikido Securityは、JetBrains Marketplaceで7万回インストールされた15個以上のAI関連プラグインが、ユーザーのOpenAI/DeepSeek APIキーを攻撃者サーバーへ送信していることを報告しており、AI時代のセキュリティが防御側のハーネス整備と攻撃側のサプライチェーン狙いの両面で具体化している。

**Editorial Notes:**
- 192: 孫正義氏「黒船来航以来の危機」、SoftBank×OpenAI合弁、GPT-5.5 Cyberで自社1万500件発見、日本重要インフラ向け優先提供
- 229: Cloudflare「Build your own vulnerability harness」、VDH+VVSの2系統構成、エージェントを入れ替え可能コンポーネントとして扱い相互検証で誤検知削減
- 143: Aikido Security調査、JetBrains Marketplaceで15+プラグイン70,000インストール、APIキー窃取＋盗難キーを別ユーザーへ「再販」する収益化構造

---

### Theme 7: OpenAI 385億ドル純損失リーク・SpaceX 600億ドルでCursor買収・DOJのxAI擁護が映すAI事業の資本市場現実

**Articles (IDs):** 180, 103, 169

**Theme Introduction (2-3 sentences in Japanese):**
OpenAIの2025年監査済み財務文書がリークされ、売上130.7億ドルに対し純損失385.3億ドル（うち実質営業損失約80億ドル）、Microsoft支払い172億ドルというコスト構造が明らかになった。同週SpaceXはIPO直後にAIコーディングのCursor（旧Anysphere）を600億ドルの株式交換で買収する合意を発表、米司法省（DOJ）はxAIメンフィスのデータセンターで稼働する57基の無許可ガスタービンが「国家・経済・エネルギー安全保障」上不可欠であるとして環境訴訟に反論しており、AI事業の収益性疑義と国家インフラ化が同時に資本市場の文脈で表面化した週である。

**Editorial Notes:**
- 180: OpenAI財務リーク（Ars Technica版）、売上130.7億ドル／R&D 191.8億ドル／Microsoftへ105.9億ドル、Soraプロジェクト縮小と中核業務集中、2030年黒字化目標
- 103: SpaceXがCursorを600億ドル株式交換で買収、xAI統合とAIインフラ・エンタープライズで28兆ドルTAM主張、IPOで時価総額1兆ドル増加
- 169: DOJ準備書面、xAI 57基無許可ガスタービンがGrok運用＋Project Maven軍事支援に不可欠と主張、NAACPの公衆衛生提訴に対抗

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週のAI業界は「Claude Fable 5/Mythos 5の急停止」という地政学的事件を中心に動いた。6月12日に米商務省の輸出管理指令でAnthropicの最新モデルが全世界でアクセス停止となり、当初は「Amazonリサーチャーが見つけたジェイルブレイク」が理由とされていたが、WIREDの追加報道では韓国SKテレコムを介した中国側アクセス遮断が真因であったことが明らかになった。David Sacks氏は「FableはMythosにガードレールをかけたモデルで、Anthropicが第三者発見の脆弱性修正を拒否した」と詳述し、Luta SecurityのKatie Moussouris氏は「指摘されたバイパスは『コードのレビュー』と『コードの修正』の差異に過ぎず、輸出規制を適用すべきものではない」と批判、Alex Stamos氏ら40名超のサイバー専門家が解除要求公開書簡を提出した。AIモデルが「ソフトウェア」から「兵器に準ずる輸出管理対象」へ変質する歴史的転換点が示された。

設計と運用の側面では、Vercel Ship 2026で「eve」（Markdown＋TypeScriptのエージェントフレームワーク）、Agent Stack、Vercel Connect（短寿命OIDCクレデンシャル）がフルセットで発表された。Vercelはフロントエンドホスティング会社からエージェント時代のフルスタックプラットフォームへ自社を再定義しており、Vercel内部だけで100以上のエージェントがeve上で稼働している実績も併せて公開された。同時にAnthropicは約40万件のClaude Codeセッションを解析し「人間が計画の70%、Claudeが実行の80%を担い、ドメイン専門性が成果を決定する」という実証データを公開、Addy Osmani氏は「エージェント能力はモデル10%・ハーネス90%」とする新SDLC論を、Charity Majors氏は「AIによってコード生成が無料化された今こそエンジニアリング規律は強化されるべき」とする論考を発表した。BayerのProduction品質Agentic RAGとLayerXのprompt-log driven自動化、5万スターのClaude Code Tipsまで含めると、ハーネス工学が個別ハックから組織標準へ昇格する転換点が今週同時並行で表面化している。

オープンウェイトモデル側では、Z.ai（Zhipu AI）のGLM-5.2がArtificial Analysis Intelligence Indexで首位を獲得（GPT-5.5に匹敵するGDPval-AA v2スコア1524）、Moonshot AIはエージェント特化型Kimi K2.7 Code（1T MoE、256Kコンテキスト、推論トークン30%削減）を公開した。Vicki Boykis氏はM2 Mac 64GBでGemma 4／GPT-OSSをDockerサンドボックス内で日常開発に投入できると報告しており、ローカルLLMが「実験」から「商用ライン」フェーズへ移行している。Anthropicの輸出規制と並列で、欧米の特定モデルへの依存リスクが地政学的に顕在化したことで、オープンウェイトとローカル実行への「保険」需要が一気に表面化した週でもある。

資本市場とセキュリティの側面でも具体的な数字が動いた。OpenAIの2025年財務文書リークは売上130.7億ドル・純損失385.3億ドル（実質営業損失約80億ドル）・Microsoft支払い172億ドルというコスト構造を露わにし、SpaceXはIPO直後にCursorを600億ドル株式交換で買収。米司法省はxAIメンフィスの無許可ガスタービン57基を「国家・経済・エネルギー安全保障」案件として擁護し、AI事業の収益性疑義と国家インフラ化が資本市場の文脈で同時表面化した。ソフトバンク×OpenAIの「Patching as a Service」は孫正義氏が「黒船来航以来の危機」と表現する規模（自社1万500件発見）、CloudflareのVulnerability Harness、JetBrainsプラグインの APIキー窃取と、AIサイバー攻防が防御側のハーネス整備と攻撃側のサプライチェーン狙いの両面で具体化している。

**Key Points to Cover:**
1. Claude Fable 5/Mythos 5の輸出規制発動・SKテレコム経由の中国懸念・Stamos公開書簡（AIモデルの地政学化）
2. Vercel "eve"・Agent Stack・Connectが揃えるエージェント時代のフルスタック基盤
3. GLM-5.2フルオープン・Kimi K2.7 Code・Mac StudioでローカルLLM商用ライン到達
4. Anthropic 40万セッション解析・Addy Osmani新SDLC・Charity Majors規律論によるAIコーディング規律の再定義
5. Bayer Agentic RAG・LayerX prompt-log・5万スターCC Tipsが体系化するハーネス工学
6. SoftBank PaaS 1万500件・JetBrainsプラグイン窃取・Cloudflare脆弱性ハーネスが形作るAIサイバー攻防
7. OpenAI 385億ドル損失リーク・SpaceX 600億ドルCursor買収・DOJのxAI擁護が映す資本市場現実

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 196 → Theme 4（Anthropic Claude Code Expertise 40万セッション解析、Leadとして配置）
- 214 → Theme 2（Vercel eve docs/site、Leadとして配置）

**👍 Upvoted Articles Used:**
- 053 → Theme 5（docswell SDD-in-loop-engineering、ハーネス工学の中核資産論）
- 170 → Theme 3（Artificial Analysis GLM-5.2リーディング評価、Leadとして配置）

**👍 Upvoted Articles Held for Annex:**
- 034（Fable 5でcs-edu site「言語の庭」生成）→ annex候補（Fable 5実用デモとして annex Group A の主力候補）
- 124（Cloud Native ナデラ学習ループ）→ annex候補（学習ループ／SaaSガバナンス論として annex で扱う、T4「規律」とは焦点が異なる）
- 174（Browser-use Firecracker browser infra）→ annex候補（具体技術解説として annex Group B のインフラ深掘り候補）

**Societal Reception Articles (formerly Theme 8, moved to Annex per round 1 review):**
- 176（Pew Research AI肯定派16%）→ annex候補（AI受容の社会的壁を示す authoritative data）
- 255（Nature脱技能化研究）→ annex候補（医師アデノーマ発見率28.4%→22.4%／Anthropic RCT、デスキリング論考の主軸）
- 253（Matthew Hughes「Herbalife」アナロジー）→ annex候補（Replit/Cursor略奪的マーケティング批判）

**👎 Downvoted Articles:**
- 036（codeheal-scan AI生成コード診断）→ annex候補（T6 セキュリティ補助記事として検討、ただし👎により主力には据えない）
- 209（Ollama×RAG長期記憶ボット）→ annex候補（T3 ローカルLLM補助として検討、ただし👎により主力には据えない）
- 282（Tailscale SSH Home Mac CC）→ annex候補（個人開発Tips、👎により主力からは除外）

**Omitted Articles:** Supabase上のomitフラグはゼロ（export_curation_flags.pyの「No summaries flagged for omission」報告に従う）

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 23 articles across 7 themes
- Annex Journal: 残り257記事（283 - 23 - 3パイウォール代替）から、Fable 5実用検証・ローカルLLM実機事例・社会受容の論考（旧T8）・国内コミュニティ記事・MCP/A2Aプロトコル深掘り・批評論考を中心にcurate

**Article Count by Theme (Planned):**
- Theme 1（Fable 5/Mythos 5輸出規制・地政学化）: 4 articles
- Theme 2（Vercel eve/Agent Stack/Connect）: 4 articles
- Theme 3（GLM-5.2・Kimi K2.7・ローカルLLM商用ライン）: 3 articles
- Theme 4（Anthropic 40万解析・Addy・Charity Majorsの規律再定義）: 3 articles
- Theme 5（Bayer・LayerX・5万スターCCのハーネス体系化）: 3 articles
- Theme 6（SoftBank PaaS・JetBrains・CloudflareのAIサイバー攻防）: 3 articles
- Theme 7（OpenAI財務・SpaceX買収・DOJ xAI擁護の資本市場現実）: 3 articles

*Note: 全テーマが3記事以上を確保。Theme 1とTheme 2は今週の中核ニュースであるため4記事構成。単一記事テーマは設定していない。*

**Total Planned for Main:** 23 articles
**Remaining for Annex:** 約257 articles（うち主要annex候補は👍 034/124/174、👎 036/209/282、および旧T8の176/255/253を含むカテゴリー別）

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-06-22 (round 1)
**Reviewer:** beijaflor

**Round 1 Changes:**
- 削除：旧Theme 8「Pew 16%肯定・Nature脱技能化・Herbalifeアナロジー」
  - 理由：AI受容と社会的負荷の論考は今週の中核ニュース性より evergreen 寄りで、annex 側でカタログ形式の方が読者の判断に資する
  - 影響：176（Pew Research）、255（Nature脱技能化）、253（Herbalife）の3記事を annex 候補へ移動
  - メイン記事数：26 → 23、テーマ数：8 → 7

**Approval:** ✅ APPROVED / ❌ NEEDS REVISION

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal) — 23 articles selected, theme-organized
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [x] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES (STEP_07)

**Pattern distribution across 7 themes:** Multi-Perspective×4 (T3, T4, T6, T7) / Single-Focus×2 (T1, T2) / Progressive-Sequence×1 (T5) / Debate-Contrast×0

---

### Theme 1: Claude Fable 5/Mythos 5輸出規制発動・SKテレコム経由の中国懸念・Stamos公開書簡が示すAIモデルの地政学化

**Pattern:** Single-Focus

**Pattern Rationale:** 4本の記事はすべて「2026年6月12日の米輸出管理指令によるFable 5/Mythos 5アクセス停止」という同一の事件をめぐる別アングルの解析・報告。242（Wired SKT報道）が真因（韓国SKテレコム経由の中国懸念）を初めて明らかにした投資的記事で、他の3本はそれぞれ政治分析・内幕報告・防御側批判を提供する。Multi-Perspectiveと迷ったが、すべての記事が同じ事件への反応であり、242が記事間で明確に上位（一次調査）に立つためSingle-Focusが適合する。

**Article Order & Roles:**
1. **[242]** Wired「SKテレコム経由の中国懸念」報道 — *Lead*：真因を明かす一次調査記事
2. **[104]** TechCrunch「ジェイルブレイクが本質ではなかった」 — *Supporting/政治分析*：政府介入の恣意性と先例的危険性
3. **[066]** David Sacks氏の内幕報告（X投稿） — *Supporting/内幕*：Anthropicが脆弱性修正を拒否した経緯
4. **[131]** Luta Security Katie Moussouris氏の防御側批判 — *Supporting/専門家批判*：規制が米サイバー防衛を損なう

**Narrative Arc:**
真因の暴露（Wired）→ 政府介入の不透明性分析（TechCrunch）→ Anthropic内部の意思決定（Sacks）→ 防御コミュニティからの批判（Moussouris）と、外側（地政学的真因）から内側（業界専門家の声）へ螺旋状に降りていく配列。読者は「なぜ起きたか」を起点に、「どう運用されたか」「業界はどう反応したか」まで一連の構造を立体的に把握できる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [242] → [104] | 「SKテレコム経由の懸念が真因であった一方、Amazonの脆弱性研究という公式理由には別の側面も浮上している」 |
| [104] → [066] | 「政治分析の文脈に加え、内部の意思決定プロセスについても投資家から具体的な報告がある」 |
| [066] → [131] | 「Anthropicの判断とは別に、サイバー防衛コミュニティからは規制そのものへの異論が提起されている」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐ (中 — ジェイルブレイク技術の議論は限定的)
- Business Impact: ⭐⭐⭐ (高 — Anthropic商用展開・米国製AI信頼性への波及)
- Future Outlook: ⭐⭐⭐ (高 — AIモデルの輸出管理対象化という先例)

**Key Synthesis Points:**
- 公式理由（ジェイルブレイク）と真因（SKテレコム経由の中国懸念）の乖離が、AI輸出規制が技術的判断よりも地政学的判断で動くことを示す
- Anthropic自身が「AI安全性」を旗印に掲げてきた歴史と、その同じロジックが自社モデル規制に転用された皮肉
- 民間・政府・第三者専門家がそれぞれ独立した立場から発言する構図は、AIモデルが「兵器に準ずる輸出管理対象」へ変質する歴史的転換点

**Conclusion Approach:**
4本の記事を並べた事実そのものが「AIモデルの地政学化」を示すことを淡々と提示する。Anthropic批判にも政府批判にも片寄せず、現状の不透明性と先例的危険性をフェアに表現する。

**Assembly Prompts for STEP_08:**
1. SKテレコム真因の暴露は、公式発表（ジェイルブレイク）との乖離をどう描くか？
2. Anthropicが自ら提唱してきた「AI安全性」規制と、自社が受けた規制の関係をどう整理するか？
3. 防御側専門家（Moussouris/Stamos）の批判は、なぜ「ジェイルブレイク」の技術的議論を超えて政治的問題として扱われるか？
4. 読者（日本のAI実務者）が今週から取り入れるべき認識は？

---

### Theme 2: Vercel "eve"・Agent Stack・Vercel Connectが揃えるエージェント時代のフルスタック基盤

**Pattern:** Single-Focus

**Pattern Rationale:** 4本のうち3本（214・160・161）はVercel公式の同時発表で、Vercel Ship 2026という単一イベントに連動している。214（eve docs）がエディタ⭐標識されたcenterpieceで、160（Ship recap）と161（Agent Stack）はその周辺コンテキスト、266は外部の実践レポート。これは典型的な「単一発表＋反応」構造でSingle-Focusが自然な選択。

**Article Order & Roles:**
1. **[214]** Vercel "eve" 公式ドキュメント（⭐ standout） — *Lead*：今週の中心となる新フレームワーク発表
2. **[160]** Vercel Ship 2026 リキャップ — *Supporting/イベント文脈*：eveを含む包括的な発表群の全体像
3. **[161]** Agent Stack 解説 — *Supporting/技術深掘り*：eveが乗るAI Gateway・Workflow・Sandbox等の3層構造
4. **[266]** sc30gsw 日本人実践者のEve hands-on — *Supporting/外部視点*：執筆エージェント構築での実機検証

**Narrative Arc:**
公式centerpiece（eve）→ イベント全体の文脈（Ship recap）→ より広い技術スタック（Agent Stack）→ 外部開発者の実践検証（266）と、Vercel自身の主張から外部の検証へ降りていく構成。読者は「何が発表されたか」を中心から押さえ、徐々に「どこまで使えるか」まで把握できる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [214] → [160] | 「eveはVercel Ship 2026の中心ピースとして発表されたが、同イベントでは関連する基盤群も併せて披露された」 |
| [160] → [161] | 「これらの発表の中核を成すのが、eveが乗る『Agent Stack』という上位アーキテクチャである」 |
| [161] → [266] | 「公式発表だけでは見えにくい『実機での使い心地』は、日本の開発者による実践レポートが補完している」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (高 — Markdown+TypeScriptのファイルベース設計、サンドボックス、Durable Sessions等の技術詳細)
- Business Impact: ⭐⭐ (中 — Vercelの自己再定義がフロントエンドホスティング業界に与える影響)
- Future Outlook: ⭐⭐⭐ (高 — エージェント時代のNext.js相当を狙う戦略的位置取り)

**Key Synthesis Points:**
- VercelはNext.js（Web開発）からeve（エージェント開発）へ自社の主戦場を再定義しつつあり、本Ship 2026がその転換点
- ファイルシステムベースのディレクトリ規約は、Next.jsで成功した「Convention over Configuration」をエージェント開発に持ち込む戦略
- Vercel内部で既に100以上のエージェントがeve上で稼働している実績は、ドッグフーディング戦略の典型例

**Conclusion Approach:**
Vercelの自己再定義（フロントエンド→エージェント時代のフルスタック）が一週間で具体化された事実を提示し、Next.jsを成功させた「規約による開発体験向上」モデルがエージェント開発に再適用される構図を整理する。eveが業界標準になるかは未確定だが、戦略的意図は明確である。

**Assembly Prompts for STEP_08:**
1. なぜVercelは「フロントエンドホスティング」から「エージェント時代のフルスタック」へ自社を再定義するのか？
2. eveの「ファイルシステム規約」設計が、Next.jsの成功パターンをどこまで再現できるか？
3. Vercel Connect（短寿命OIDCクレデンシャル）がもたらすセキュリティモデルの革新性は？
4. 読者（フロントエンド開発者・エージェント実装者）が現時点でeveを採用する判断基準は？

---

### Theme 3: GLM-5.2フルオープン・Kimi K2.7 Code・Mac StudioでローカルLLMが商用ラインに到達

**Pattern:** Multi-Perspective

**Pattern Rationale:** 3本の記事はそれぞれ独立した主体（Z.ai、Moonshot AI、個人実践者）の同週の動きで、互いに直接の因果はない。GLM-5.2の首位獲得（170）、Kimi K2.7 Codeの新モデル発表（092）、Vicki Boykis氏のM2 Mac実機検証（101）という3つの異なるスケールの主体を並列に提示することで、「ローカルLLMの商用ライン到達」という現在地が立体化する。Progressive-Sequenceとも迷ったが、これら3本は独立した動きであり、相互の依存関係（A→B→C）はないためMulti-Perspectiveが適合。

**Article Order & Roles:**
1. **[170]** Artificial Analysis「GLM-5.2がオープンウェイト首位」（👍 upvoted） — *客観的評価の視点*：独立評価指標による定量的確認
2. **[092]** Moonshot AI Kimi K2.7 Code 公式リリース — *新モデルの視点*：エージェント特化型1T MoEの登場
3. **[101]** Vicki Boykis「Running local models is good now」 — *実践者の視点*：M2 Mac 64GBでの日常開発投入

**Narrative Arc:**
客観評価（AAI Intelligence Indexで51点首位）→ 新モデル登場（Kimi K2.7 Codeで256Kコンテキスト・エージェント特化）→ 実践適用（M2 Mac+LM Studio+Docker環境）と、評価指標から新モデルへ、新モデルから日常実践へとスコープを進める。読者は「客観的根拠」「新たな選択肢」「実際の使い心地」を一通り把握できる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [170] → [092] | 「ベンチマーク上の首位と並行して、エージェント特化型の新モデルも同週に登場している」 |
| [092] → [101] | 「これらのモデルが実機でどこまで戦えるかは、実践者の日常使用レポートが教えてくれる」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (高 — モデルアーキテクチャ・量子化・実機環境の技術詳細)
- Business Impact: ⭐⭐ (中 — クラウドAPI依存からの脱却、コスト構造変化)
- Future Outlook: ⭐⭐⭐ (高 — オープンウェイトとローカル実行の併存が標準化される展開)

**Key Synthesis Points:**
- GLM-5.2がGDPval-AA v2でGPT-5.5に匹敵する（1524点）水準に到達した事実は、オープンウェイトとクローズドモデルの性能差が「実用上は無視できる」レンジに入ったことを示す
- Kimi K2.7 Codeのエージェント特化（256K context・推論トークン30%削減）は、汎用LLMと特化LLMの市場分化が加速していることを示す
- Vicki Boykis氏のM2 Mac実践は、「ローカルLLMは実験段階」というかつての評価が「日常開発に投入可能」へ書き換えられたことを実感ベースで提示

**Conclusion Approach:**
3つの独立した動き（ベンチマーク・新モデル・実践）が同週に並んだ事実を、「ローカルLLMの商用ライン到達」という現在地として整理する。Fable 5の輸出規制と並列で読むと、欧米クローズドモデルへの依存リスクが地政学的に顕在化した直後にこのオープン側の進展が並んだ構図にも触れる。

**Assembly Prompts for STEP_08:**
1. GLM-5.2のAAI首位は、オープンウェイトとクローズドモデルの実用性能差をどう書き換えたか？
2. Kimi K2.7 Codeのエージェント特化型MoE設計は、汎用LLM市場とどう棲み分けるか？
3. M2 Mac 64GB環境でのDockerサンドボックス実行は、個人開発者・小規模チームに何をもたらすか？
4. Fable 5輸出規制（T1）と並列で見たとき、ローカルLLM/オープンウェイトへの「保険」需要はどう変化するか？

---

### Theme 4: Anthropic「Claude Code Expertise」40万セッション解析・Addy Osmani新SDLC・Charity Majors『規律強化』論が示すAIコーディング規律の再定義

**Pattern:** Multi-Perspective

**Pattern Rationale:** 3本の記事はそれぞれ独立した主体（Anthropic Research、Google Addy Osmani、Honeycomb Charity Majors）が、互いに直接呼応せずに同週に「AIコーディング時代の規律再定義」へ収束する論を提示している。データ（196）・フレームワーク（248）・原則（172）という抽象度の異なる3層から同じ結論に到達する構図はMulti-Perspectiveが適合。Progressive-Sequenceとも迷ったが、依存関係（A→B→C）はなく並列の3視点として読むのが自然。

**Article Order & Roles:**
1. **[196]** Anthropic「Claude Code Expertise」40万セッション解析（⭐ standout） — *データの視点*：実証的根拠の最強アンカー
2. **[248]** Addy Osmani「The New Software Lifecycle」 — *フレームワークの視点*：「モデル10%・ハーネス90%」のSDLC再定義
3. **[172]** Charity Majors「AI demands more engineering discipline」 — *原則の視点*：コードを「キャッシュ」と再定義する哲学

**Narrative Arc:**
データ（人間70%計画/Claude 80%実行・ドメイン専門性が成果決定）→ フレームワーク（モデルではなくハーネス、Vibe Codingからエージェント工学へ）→ 原則（コードは資産ではなくキャッシュ、規律はより強く必要）と、抽象度を下げず3層を並列に提示。読者は「事実」「設計」「哲学」を一通り受け取り、自分のレイヤーで判断できる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [196] → [248] | 「Anthropicの実証データが示す『計画は人間、実行はAI』の構図に対し、Addy Osmani氏は具体的なSDLC再設計を提案している」 |
| [248] → [172] | 「SDLC設計と並んで、より深い原則レベルでもAIコーディング時代の規律論が再構築されている」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (高 — ハーネス設計・コンテキストエンジニアリング・検証スイートの技術論)
- Business Impact: ⭐⭐ (中 — エンジニア職能の評価軸変化、組織設計への影響)
- Future Outlook: ⭐⭐⭐ (高 — 「Vibe Coding」から「エージェント工学」への産業転換)

**Key Synthesis Points:**
- 40万セッション解析の「人間70%計画/Claude 80%実行」という分業比率は、「AIが書く」時代における人間の役割を実証データで定量化した最初の本格的研究
- Addy Osmaniの「モデル10%・ハーネス90%」論は、過去2年の「より強力なモデルが正義」というパラダイムを構造的に否定する
- Charity Majors の「コードはキャッシュ」論は、AIによってコード生成が無料化された現実を踏まえ、エンジニアリング規律が緩むのではなくむしろ強化されるべきだという主張

**Conclusion Approach:**
3者が独立に同じ方向（規律の再定義・強化）へ収束する事実を提示する。Vibe Codingに対する直接の批判ではなく、AIコーディング時代の実証データと構造分析と原則論が「より深い規律」を求めていることを淡々と整理する。

**Assembly Prompts for STEP_08:**
1. Anthropic 40万セッション解析の「ドメイン専門性が成果を決定する」結果は、エンジニア教育・採用にどう波及するか？
2. Addy Osmaniの「モデル10%・ハーネス90%」論は、過去2年の「より強力なモデル競争」のパラダイムをどう塗り替えるか？
3. Charity Majorsの「コードはキャッシュ」論は、Vibe Codingに対する直接批判というより、Vibe Codingの上位概念として位置づけられるべきか？
4. 読者（エンジニア・組織設計者）が今週から自社のSDLCに取り入れるべき具体的な変化は？

---

### Theme 5: Bayer Reliable Agentic RAG・LayerX prompt-log driven・5万スターClaude Code Tipsが体系化するハーネス工学の実践

**Pattern:** Progressive-Sequence

**Pattern Rationale:** 3本の記事は「抽象的なループ概念→大企業の本番事例→個別チームの自動化実装」という、概念から具体への明確な抽象度の階段を構成する。Multi-Perspectiveと迷ったが、053（概念）が147（実装事例）と244（実践DIY）の前提となり、読者は053の抽象論を読んだ上で147/244の具体例を理解する構造が自然なためProgressive-Sequenceが適合。

**Article Order & Roles:**
1. **[053]** docswell「SDD in loop engineering」（👍 upvoted） — *概念基盤（Foundation）*：仕様書駆動開発をループの中核資産として再定義
2. **[147]** Bayer × Thoughtworks 「Reliable Agentic AI Systems」（Martin Fowler） — *エンタープライズ実装（Development）*：プロダクション品質のマルチエージェントRAG事例
3. **[244]** LayerX「prompt-log driven AI workflow」 — *組織的習慣化（Payoff）*：プロンプト履歴の自動分析からSkill化まで全プロセスを仕組み化

**Narrative Arc:**
抽象（仕様書を「ループに渡すコンテキスト」として再定義）→ エンタープライズ事例（LangGraph・Process/Data-reflect分離・RAGAS継続監視）→ 組織習慣化（全プロンプトをJSONLログ化し意味的グルーピングで自動Skill化）と、概念から実装、実装から組織習慣へ徐々にスケールを下げる。読者は理論→大企業→自分のチームという順で具体性が増す。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [053] → [147] | 「概念レベルでのループエンジニアリングが、エンタープライズではどう実装されているかをBayerの事例が示す」 |
| [147] → [244] | 「大企業の本番事例に対し、より身近な規模ではLayerXの『プロンプト棚卸し』が示すように、組織的習慣化のフレームが構築可能である」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (高 — LangGraphマルチエージェント・コンテキストエンジニアリング・JSONL分析の技術詳細)
- Business Impact: ⭐⭐ (中 — エンジニアリング組織の運用効率改善)
- Future Outlook: ⭐⭐⭐ (高 — ハーネス工学が個別ハックから組織標準パターンへ昇格する転換点)

**Key Synthesis Points:**
- 「仕様書を一度きりの設計図ではなく実行履歴と連動する継続的資産」という再定義（053）は、過去のSDDが抱えていた「書いて終わり」の問題を構造的に解決
- BayerのProcess-reflectとData-reflectの分離（147）は、エージェントの「思考プロセスの反省」と「処理データの反省」を独立したループとして扱う本番品質のパターン
- LayerXの「プロンプト履歴をLLMで意味的に分析しSkill化を自動提案する」仕組み（244）は、エージェント開発の改善サイクルそのものを自動化する、いわば「メタ・ハーネス」の実装

**Conclusion Approach:**
ハーネス工学がT4で扱った「規律の再定義」と並行して、概念・大企業・組織習慣の3層で同時並行に体系化されつつあることを示す。エージェント開発が「ツール選定」段階から「組織運用標準」段階へ移行しつつある現在地を整理する。

**Assembly Prompts for STEP_08:**
1. SDDをループの中核資産として再定義することは、過去のドキュメント駆動開発と比べて何が変わるのか？
2. BayerのProcess-reflect/Data-reflect分離は、汎用エージェントフレームワーク（LangGraph等）の運用パターンとして標準化されるか？
3. LayerXのプロンプト棚卸しは「メタ・ハーネス」と言えるか？それは個別チームレベルで再現可能か？
4. T4「規律の再定義」と本テーマ「ハーネス工学の実践」は、それぞれ何を補完するか？

---

### Theme 6: SoftBank "Patching as a Service" 1万500件発見・JetBrainsプラグイン窃取・Cloudflare脆弱性ハーネスが形作るAIサイバー攻防

**Pattern:** Multi-Perspective

**Pattern Rationale:** 3本の記事はそれぞれ独立した主体（SoftBank+OpenAI合弁、Cloudflare、Aikido Security調査）の異なる角度（商用サービス展開・防御エンジニアリング・攻撃側の動向）を提示している。3者は互いに呼応せず並列に存在し、読者は3つの視点を並べて初めて「AI時代のサイバー攻防」の輪郭を掴める。Single-Focus（同一事件への反応）でもProgressive-Sequence（依存関係）でもなく、Multi-Perspectiveが構造的に適合。

**Article Order & Roles:**
1. **[192]** ソフトバンク×OpenAI「Patching as a Service」1万500件発見 — *商用化の視点*：孫正義氏「黒船来航以来の危機」、防御側の商用化が動いた
2. **[229]** Cloudflare「Build your own vulnerability harness」 — *エンジニアリングの視点*：VDH+VVS構成・モデル相互検証で誤検知削減
3. **[143]** Aikido Security「JetBrainsプラグインが APIキーを窃取」 — *攻撃側の視点*：15+プラグイン7万インストール・盗難キーの「再販」エコシステム

**Narrative Arc:**
商用サービス化（防御側がパッケージ製品として登場）→ エンジニアリングパターン（防御側がオープンに技法を公開）→ 攻撃側の事例（同時に攻撃者もエコシステム化）と、防御側の進展を2層、最後に攻撃側の対応を提示することで、AIセキュリティが攻防両面で professionalizing している構図を描く。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [192] → [229] | 「商用パッケージとしての防御に加え、防御エンジニアリングの技法そのものもオープンに体系化されている」 |
| [229] → [143] | 「防御側がこれだけ発展している一方、攻撃側もサプライチェーン狙いという形でエコシステム化が進んでいる」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐ (高 — VDH/VVS構成・MCP連携・サンドボックス内バイナリ実行)
- Business Impact: ⭐⭐⭐ (高 — 日本の重要インフラ企業向けに優先提供される規模の市場形成)
- Future Outlook: ⭐⭐ (中 — 攻防の professionalizing が標準フェーズへ移行)

**Key Synthesis Points:**
- 孫正義氏の「自社で1万500件の未知脆弱性発見」という発言は、AIによる脆弱性発見能力が実用ラインを越え、商用サービスとしてパッケージ化される段階に入ったことを示す
- Cloudflareの「エージェント入れ替え可能設計」と「モデル相互検証で誤検知削減」は、防御側がベンダーロックインを避けつつ精度を確保するアーキテクチャ
- JetBrainsプラグインの「盗難キーを別ユーザーへ再販する」収益化構造は、攻撃者がAIエコシステム特有のサプライチェーン弱点を体系的に exploit しているシグナル

**Conclusion Approach:**
AIサイバー攻防が同週内に商用化・エンジニアリング体系化・攻撃エコシステム化の3面で同時進行している事実を提示する。「攻撃か防御か」の二項対立を超えて、攻防両面の professionalizing として描く。

**Assembly Prompts for STEP_08:**
1. 孫正義氏「黒船来航以来の危機」という強い表現は、自社1万500件発見の事実とどこまで整合するか？
2. Cloudflareの「エージェント入れ替え可能設計」は、ベンダーロックイン回避としてのアーキテクチャパターンとして定着するか？
3. JetBrainsプラグインの「盗難キー再販」エコシステムは、開発者がプラグイン採用時に持つべき認識をどう変えるか？
4. AIサイバー攻防の professionalizing は、日本の重要インフラ企業がどう備えるべきか？

---

### Theme 7: OpenAI 385億ドル損失リーク・SpaceX 600億ドルCursor買収・DOJのxAI擁護が映すAI事業の資本市場現実

**Pattern:** Multi-Perspective

**Pattern Rationale:** 3本の記事はそれぞれ独立した出来事（OpenAIの財務文書リーク、SpaceXのCursor買収合意、DOJのxAI擁護）であり、互いに直接の因果はない。それぞれが「コスト構造」「M&A consolidation」「国家インフラ化」という別アングルからAI事業の資本市場現実を照らしている。3つを並列に提示することで「資本市場におけるAI事業の現在地」を立体化するためMulti-Perspectiveが適合。

**Article Order & Roles:**
1. **[180]** OpenAI 財務文書リーク（Ars Technica） — *コスト構造の視点*：売上130.7億ドル／純損失385.3億ドル／MS支払い172億ドル
2. **[103]** SpaceX 600億ドルでCursor買収（TechCrunch） — *M&A consolidationの視点*：xAI統合とAIインフラ・エンタープライズで28兆ドルTAM主張
3. **[169]** DOJのxAI擁護（TechCrunch） — *国家インフラ化の視点*：57基無許可ガスタービンを「国家・経済・エネルギー安全保障」案件として擁護

**Narrative Arc:**
コスト構造（収益130億／損失385億という実態）→ M&A consolidation（SpaceX/xAIによる600億ドル買収）→ 国家インフラ化（DOJ準備書面でGrokがProject Mavenに不可欠と主張）と、財務実態から市場再編、国家関与へ三段階で資本市場のAI事業現実を可視化する。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [180] → [103] | 「OpenAIの財務実態が示すコスト圧力と並行して、業界全体ではM&Aによる consolidation が進んでいる」 |
| [103] → [169] | 「企業レベルの M&A だけでなく、xAIが国家インフラ案件として政府に擁護されるという、AI事業と国家の癒着も顕在化している」 |

**Emphasis Balance:**
- Technical Depth: ⭐ (低 — 技術論ではなく財務・M&A・国家関与の議論)
- Business Impact: ⭐⭐⭐ (高 — 全記事がビジネス・資本市場側)
- Future Outlook: ⭐⭐⭐ (高 — AI事業の収益性疑義と国家インフラ化の長期軌道)

**Key Synthesis Points:**
- OpenAIの2025年純損失385.3億ドル（実質営業損失約80億ドル）は、収益急増（前年比3.5倍）にもかかわらずコスト構造が極めて重いことを示す
- SpaceXのCursor 600億ドル買収は、xAI/Grokの再構築を加速させるためのコーディング能力獲得であり、AIラボ単独でなくインフラ＋ロボット＋衛星＋AIの統合戦略の一部
- DOJのxAI擁護（57基無許可ガスタービンを「国家安全保障」案件と主張）は、Grokが米軍Project Mavenで実戦投入されている事実を踏まえると、AI事業と国家の癒着が制度的に正当化される転換点

**Conclusion Approach:**
3つの独立した動きが同週に並んだ事実そのものを、「AI事業の資本市場現実」として整理する。バブル論にも反バブル論にも片寄せず、収益性疑義・市場再編・国家インフラ化の3層構造を淡々と提示する。Fable 5輸出規制（T1）と並列で読むと、AI事業が「国家安全保障」と接続する2026年6月の構図がより鮮明になることに触れる。

**Assembly Prompts for STEP_08:**
1. OpenAIの385.3億ドル純損失（実質80億ドル営業損失）は、AI事業の収益性疑義の決定的データになるか？
2. SpaceXのCursor 600億ドル買収は、xAI再構築という戦略文脈のなかでどう位置づけられるか？
3. DOJのxAI擁護は、AI事業と国家インフラの癒着を制度的に正当化する先例となるか？
4. Fable 5輸出規制（T1）とxAI国家インフラ化（本テーマ）が同週に並んだ意味は？

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed (single-focus, multi-perspective, progressive-sequence, debate-contrast)
- [x] Phase 2: Patterns selected and customized for all 7 themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

> The agent leaves `ASSEMBLY PLAN APPROVED` **unchecked** when generating the document. The human flips it to `[x]` inside the `human-review-gate` vim popup; the agent must not check it.

**Approval Date:** 2026-06-22
**Approver:** beijaflor
