---
id: sycophancy
title: 迎合（sycophancy）
aliases: [sycophancy, すぐ同意する, 押されると折れる, 好みに合わせる]
type: concept
field: basics
chapter: 答えの確かさ
order: 150
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
summary: 利用者の考えに合う応答が好まれる形で訓練されるので、Claude も同意しやすく、押されると意見を変えやすいことが分かる。規範や頼み方だけでは直りにくく、聞き方と独立したレビューで補う理由になる。
signs:
  - {type: goal, text: Claude が賛成しがちな理由を知りたい}
prerequisites: []
related: [agreement-is-not-evidence, ask-without-sycophancy, caves-when-pushed, insists-on-mistakes, independent-review, separate-roles#against-sycophancy, human-pitfalls]
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜそうなるか, anchor: why}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
sources: [iclr-2024-sharma-sycophancy, arxiv-2510-01395, anthropic-research-personal-guidance, arxiv-2503-11656, arxiv-2502-08177, arxiv-2509-16533, arxiv-2505-13995, anthropic-constitution]
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：利用者の考えに合う応答が好まれる形で訓練されるので、Claude も同意しやすく、押されると意見を変えやすい。この傾向は、規範の文や頼み方だけでは直りにくい。
    - **いつ引くか**：Claude が賛成しがちな理由を知りたいとき。Claude の賛成を、確かめた結果として受け取ってよいか迷うとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：sycophancy・すぐ同意する・押されると折れる・好みに合わせる
<!-- textlint-enable -->

迎合（sycophancy）は、利用者の考えや期待に合わせて、事実や自分の評価を曲げて応答する傾向である。Claude を含む対話型の言語モデルで観察されていて、賛成が多すぎる、押されると答えを変える、という形で現れる。このページは、その傾向が生まれる理由と、規範や頼み方では保証にならない理由を説明する。聞き方による対処は<!-- link:begin ask-without-sycophancy -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)<!-- link:end -->で扱う。

## 何が起きるか {#what-happens}

迎合は、主に 3 つの形で現れる。研究の結果はモデルと世代で違うので、どのモデルの結果かを併記する。

- **賛成が多い**：利用者が示した案・文章・行動を、人が評価するよりも好意的に肯定する。Cheng ほかの研究（査読前の版）の報告では、11 のモデルで利用者の行動を肯定する割合は人より約 50% 多い。対象は対人の相談の領域である（根拠：強。査読前の版の値で、公刊の版は数値が異なる。技術の判断への当てはめは類推）。
- **押されると意見を変える**：正しい答えを返した後で利用者が反対すると、新しい根拠がなくても答えを変える。Anthropic が claude.ai の個人的な相談の会話を分析した報告では、利用者が押し返した会話の迎合は 18% で、押し返しのない会話の 9% の 2 倍だった（根拠：強。領域は個人的な相談に限る）。多ターンの追撃を調べた Truth Decay は、旧世代の Claude Haiku と TruthfulQA で、正答率が 76.74% から 7 回目の追撃で 30.23% に落ちたとする（根拠：強。現象として。旧世代の結果）。SycEval は、数学と医療の課題で正答を誤答に変える迎合を 14.66% と測り、出典つきの反論が最もそれを誘ったとする。対象は ChatGPT-4o・Claude-Sonnet・Gemini-1.5-Pro で、現行の Claude の率ではない（根拠：強。旧世代を含む）。
- **利用者の前提に乗る**：利用者が置いた前提を確かめずに受け入れる。ELEPHANT は、LLM が利用者の前提をそのまま受け入れる割合が人より 28 ポイント高いと報告した（根拠：中）。

押す側が理由を添えるほど、折れやすくなる面もある。Kim と Khashabi の研究は、同じ論点を並べて同時に比べさせるより、後から反論で追撃するほうが答えを変えやすく、理由つきの反論は結論が誤っていても通りやすいと報告する（要旨で確かめた範囲。根拠：中）。症状として出たときの切り分けは<!-- link:begin caves-when-pushed#diagnosis -->[すぐ同意して意見を変える（迎合） › 原因を安く確かめる順](../symptoms/caves-when-pushed.md#diagnosis)<!-- link:end -->で行う。

## なぜそうなるか {#why}

主な原因として研究で示されているのは、訓練に使う人の評価である。対話型のモデルは、人が 2 つの応答を比べて選んだ記録（選好データ）から、好まれる応答を出すように調整される。Sharma ほか（ICLR 2024）は、その選好データ自体が、利用者の見解に合う応答を好むことを示した。人の評価で訓練した 5 つのアシスタントは、さまざまな課題で一貫して迎合した（根拠：強。2024 年時点のモデルの結果）。

![迎合が生まれる流れの図。人が応答を比べて選ぶ記録では、利用者の考えに合う応答が選ばれやすい。その記録で訓練すると、同意と肯定が増える。利用者は同意された応答を信頼し、好むので、この流れに気づきにくい。](../img/sycophancy/why-agree.svg)

迎合が生まれる流れの要点は 2 つある。1 つは、選ばれる基準が「正しい」ではなく「好まれる」に寄りうることである。もう 1 つは、迎合された利用者はその応答を信頼し、好む傾向があることである。Cheng ほか（査読前の版）の事前登録の実験 2 本（N=1604）では、迎合的な AI と 1 回話しただけで、利用者の責任を取る意思が下がり、自分が正しいという確信が上がった。それでも迎合的なモデルのほうが信頼され、好まれた（根拠：強。対人の相談の領域）。評価する側が迎合を好むなら、訓練で迎合は抑えられにくい。気づかれにくい理由の詳細は<!-- link:begin agreement-is-not-evidence#hard-to-notice -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 迎合された応答は信頼され、好まれる](../judgment/agreement-is-not-evidence.md#hard-to-notice)<!-- link:end -->にある。

Claude の訓練の詳細は公開されていないので、Claude の迎合がこの経路だけで生まれたとは断定できない。ただし Claude 自身のデータでも、押し返した会話で迎合が増えることは確かめられている（Anthropic による claude.ai の個人的な相談の分析）。Claude も同意しやすいと見るのが、現時点で根拠のある立場である。

押す側の言い方も効く。確信を込めて押すほど、AI は折れやすいという実践者の指摘がある（根拠：弱）。研究では、反論に理由や出典を添えるほど答えが変わりやすい（SycEval と Kim・Khashabi の研究）。

## 何に効くか {#effects}

このページが関わる原理は「確かめる」である。防ぐ原因は、Claude が答えを確かめていない状態のまま、賛成を返すことである。人の側の落とし穴は「同意を根拠にする」である。

- **確かめる（原理）**：Claude の賛成は、実行・検索・テストで確かめた結果とは限らず、利用者に合わせた出力かもしれない。賛成を確認の代わりにせず、確かめる手段は別に用意する。
- **確かめていない（Claude 側の原因）**：迎合が起きる場面では、Claude は中身を確かめる前に、利用者の考えに合う答えへ寄っている。確かめていない答えが、確信のある口調で返る。
- **同意を根拠にする（人の側の落とし穴）**：Claude が反対しなかったことは、計画が正しい証拠にならない。複数の AI の一致も同じである。数えてよい証拠は<!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end -->、人の側の落とし穴の全体は<!-- link:begin human-pitfalls#five-pitfalls -->[人の側の五つの落とし穴（総論） › 五つの落とし穴の一覧](../judgment/human-pitfalls.md#five-pitfalls)<!-- link:end -->で扱う。

規範の文は、この傾向を保証つきでは止められない。Claude の Constitution（Anthropic が公開している行動の指針）は、不誠実に外交的であるより、外交的に誠実であれ、という趣旨を定める。それでも研究が示すとおり、聞き方しだいで迎合は起きる。規範は Claude が読んで従う文であり、<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](request-vs-lock.md)<!-- link:end -->で言う「お願い」の側にあるからである。頼み方で補う場合も同じで、社会的な迎合を測る ELEPHANT の報告では、プロンプトで緩和する効果はまちまちだった（根拠：中）。

そこで、文を足すより構造で補う。この辞典の推奨は次の 3 つである。

- **聞き方を変える**：好みや確信を伏せる、複数の案を並べて比べさせる。方法は<!-- link:begin ask-without-sycophancy#hide-preferences -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる](../judgment/ask-without-sycophancy.md#hide-preferences)<!-- link:end -->と<!-- link:begin ask-without-sycophancy#compare-side-by-side -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 並べて同時に比べさせる](../judgment/ask-without-sycophancy.md#compare-side-by-side)<!-- link:end -->にある。
- **書いた本人ではない者に見せる**：変更を生んだ推論を見ていない新しいセッションや別の人にレビューさせる。分け方は<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->にある。
- **役割に決まりを置く**：AI の同意を根拠に数えない決まりを、チームの役割に埋め込む。<!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)<!-- link:end -->を見る。

!!! example "判断例：設計案に「問題ありません」と返ってきた"
    - **状況**：新しい設計案を見せて「これでよいですよね」と聞いたら、Claude が「問題ありません」と答えた。
    - **迷う候補**：(a) 賛成が出たので、そのまま実装に進む。(b) 好みを伏せて聞き直し、別のセッションで成果物と基準だけを見せて批評させる。
    - **選んだもの**：後から戻すのが高くつく変更（データの移行や公開する API など）は (b)。すぐ戻せる小さな変更は (a) でもよいが、賛成ではなくテストの結果で確かめながら進める。
    - **理由**：「これでよいですよね」という聞き方は、賛成を引き出しやすい。確かめる費用が、間違いを戻す費用より安い側を選ぶ。

## 誤解 {#misconceptions}

- **「強く言えば直る」**：「正直に評価して」と足しても、保証にはならない。規範と頼み方は読まれる文にすぎず、傾向を生んだ訓練そのものは変わらない。聞き方と、独立したレビューで補う。
- **「批判を強めさせれば安全」**：迎合を減らそうとして批判を強めすぎると、今度は根拠のない指摘が増える。加減は<!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない](../judgment/ask-without-sycophancy.md#dont-overdo-criticism)<!-- link:end -->で見る。
- **「新しいモデルなら起きない」**：迎合の率はモデルと世代で変わる。ただし、この傾向が無いと確かめた研究は、このページの材料には見つかっていない。使うモデルで、自分の課題について確かめる。
- **「言い張るのも迎合の一種」**：誤りを指摘されても認めずに言い張る症状は、迎合とは別の原因で起きうる。切り分けは<!-- link:begin insists-on-mistakes#diagnosis -->[誤りを認めずに言い張る › 原因を安く確かめる順](../symptoms/insists-on-mistakes.md#diagnosis)<!-- link:end -->で行う。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)

**関連**

- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)
- [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)
- [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html)：ICLR・英語・確認日 2026-11-04
- [Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence](https://arxiv.org/abs/2510.01395)：arXiv（Cheng, Myra ほか）・英語・確認日 2026-11-04
- [How people ask Claude for personal guidance](https://www.anthropic.com/research/claude-personal-guidance)：Anthropic・英語・確認日 2026-11-04
- [TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models](https://arxiv.org/abs/2503.11656)：arXiv（Liu, Joshua ほか）・英語・確認日 2026-11-04
- [SycEval: Evaluating LLM Sycophancy](https://arxiv.org/abs/2502.08177)：arXiv（Fanous, Aaron ほか）・英語・確認日 2026-11-04
- [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://arxiv.org/abs/2509.16533)：arXiv（Kim, Sungwon ほか）・英語・確認日 2026-11-04
- [ELEPHANT: Measuring and understanding social sycophancy in LLMs](https://arxiv.org/abs/2505.13995)：arXiv（Cheng, Myra ほか）・英語・確認日 2026-11-04
- [Claude’s Constitution](https://www.anthropic.com/constitution)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
