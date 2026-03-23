{
  "metadata": {
    "version": "1.0",
    "generatedAt": "2026-03-23T04:50:34.237057+00:00",
    "generatedBy": "gemini-3-flash-preview"
  },
  "content": {
    "title": "LLMを活用したソフトウェア開発術：設計・開発・レビューを分離するエージェント・ワークフロー",
    "url": "https://www.stavros.io/posts/how-i-write-software-with-llms/",
    "language": "en",
    "contentType": "💡 Tutorial & How-to (チュートリアル)",
    "oneSentenceSummary": "開発の主眼をコーディングからアーキテクチャ設計へとシフトし、設計者・開発者・レビュアーの役割を異なるLLMエージェントに分担させることで高品質なコードを生成する実践的ワークフローの解説。",
    "summaryBody": "本記事では、LLM（大規模言語モデル）を駆使して数万行規模のソフトウェアを高い信頼性で構築するための実践的なワークフローが紹介されています。筆者は、プログラミングそのものよりも「ものづくり」を重視し、LLMの台頭によってエンジニアの役割が「コードの正確性」から「システムのアーキテクチャ設計」へと変化したと説きます。\\n\\n具体的なプロセスとして、以下の3つの役割を異なるモデルに割り当てるマルチエージェント方式を採用しています：\\n1. **設計者 (Architect):** 最も強力なモデル（Claude Opus等）を使用。人間と対話して詳細な設計図とタスクを作成。\\n2. **開発者 (Developer):** トークン効率の良いモデル（Sonnet等）を使用。設計図に従ってコードを実装。\\n3. **レビュアー (Reviewers):** 複数の異なるモデル（Codex, Gemini等）を使用。多角的な視点からコードを検証。\\n\\n記事の後半では、自作のパーソナルアシスタント「Stavrobot」にメール機能を追加する際の実録プロンプトが掲載されており、曖昧な要求から詳細な仕様を詰め、エッジケース（ワイルドカードによるメールアドレス検証など）に対処していく過程が非常に具体的に示されています。",
    "topics": [
      "LLM",
      "AIエージェント",
      "ソフトウェア開発",
      "プログラミング",
      "ワークフロー"
    ],
    "scores": {
      "signal": 5,
      "depth": 5,
      "uniqueness": 4,
      "practical": 5,
      "antiHype": 4,
      "mainJournal": 95,
      "annexPotential": 75,
      "overall": 92
    },
    "originalTitle": "How I write software with LLMs"
  }
}