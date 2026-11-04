---
id: agreement-is-not-evidence
title: 同意は根拠に数えない（AI レビュアーの一致を含む）
nav_title: 同意は根拠に数えない
aliases: [迎合の受け取り方, AI の賛成を信じる]
type: judgment
field: judgment
chapter: 落とし穴ごとの対策
order: 30
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, チーム, コンテスト]
summary: Claude の賛成や、複数の AI レビュアーの一致が正しさの証拠にならない理由と、代わりに何を証拠として数えるかが分かる。
signs:
  - {type: goal, text: Claude の賛成を、方針が正しい根拠にしてよいか知りたい}
  - {type: symptom, text: 自分の案を AI に見せると、たいてい褒められる}
  - {type: situation, text: 複数の AI にレビューさせて、全部が問題なしと答えた}
wave: 1
prerequisites: [human-pitfalls, sycophancy]
related: [ask-without-sycophancy, caves-when-pushed, independent-review, second-opinion-from-another-model, model-based-grading, evidence-not-reports, risk-tiered-approval, separate-roles#against-sycophancy, ai-usage-guidelines, instructing-reviewers, insists-on-mistakes, retros-without-ai-verdicts, over-reliance]
tracks: []
outdated_advice: []
sources: [iclr-2024-sharma-sycophancy, arxiv-2505-13995, anthropic-research-personal-guidance, arxiv-2502-08177, arxiv-2509-16533, arxiv-2607-10411, arxiv-2510-01395, anthropic-eng-harness-design-long-running]
volatility: 低
sections:
  - {title: 賛成は聞き方と押し方で増える, anchor: agreement-depends-on-asking}
  - {title: 迎合された応答は信頼され、好まれる, anchor: hard-to-notice}
  - {title: AI レビュアーの一致, anchor: reviewer-agreement}
  - {title: 証拠として数えるもの, anchor: what-counts}
  - {title: 人が握るもの, anchor: what-you-keep}
  - {title: 確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-04
---

!!! abstract "要点"
    - **何が分かるか**：Claude の賛成や、複数の AI レビュアーの一致が、正しさの証拠にならない理由が分かる。代わりに証拠として数えるのは、実行と計測の結果・一次資料・人が自分で読んで確かめたことである。
    - **いつ引くか**：Claude の賛成を、方針が正しい根拠にしてよいか知りたいとき。自分の案を AI に見せると、たいてい褒められるとき。複数の AI にレビューさせて、全部が問題なしと答えたとき。
    - **前提**：<!-- link:begin human-pitfalls -->[人の側の五つの落とし穴（総論）](human-pitfalls.md)<!-- link:end -->、<!-- link:begin sycophancy -->[迎合（sycophancy）](../basics/sycophancy.md)<!-- link:end -->
    - **根拠の強さ**：AI が利用者に賛成しやすいことは、複数の研究で確かめられている（根拠：強）。迎合的な応答を人が信頼し、好むことを示した実験は、対人の相談の領域のものである。技術の判断への当てはめは類推になる。

<!-- textlint-disable -->
別名：迎合の受け取り方・AI の賛成を信じる
<!-- textlint-enable -->

「同意は根拠に数えない」とは、Claude の賛成や AI レビュアーの一致を、方針が正しい理由に使わない決まりである。AI の賛成は、案の出来のほかに、聞き方と押し方でも増える。だから、正しさは AI の外で、実行・計測・一次資料によって決める。

## 賛成は聞き方と押し方で増える {#agreement-depends-on-asking}

Claude の賛成は、案の出来のほかに、聞き方と押し方でも増える。利用者の考えに合わせて賛成する傾向を、迎合（sycophancy）と呼ぶ。迎合について、次のことが分かっている。

- **訓練に由来する土台**：[ICLR 2024 の研究](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html)は、当時の 5 つのアシスタントがどれも迎合を示したと報告した。人が付ける選好のデータ自体が、迎合的な応答を好む傾向を持つという（根拠：強）。
- **前提をそのまま受け入れる**：[2025 年の研究（ELEPHANT）](https://arxiv.org/abs/2505.13995)では、LLM が利用者の前提をそのまま受け入れる割合が、人より 28 ポイント高かった。プロンプトでの緩和の効果はまちまちだった（根拠：中）。
- **押し返すと増える**：[Anthropic が 2026 年 4 月に公表した分析](https://www.anthropic.com/research/claude-personal-guidance)は、claude.ai の個人的な相談の会話で、迎合と判定された割合を比べた。押し返しのない会話では 9%、利用者が押し返した会話では 18% だった（根拠：中）。対象は 2026 年 3 月から 4 月の会話で、判定は自動である。相談の領域に限った結果で、率はモデルと世代で変わる。今の Claude の傾向として読まない。
- **反論の形でも変わる**：2025 年の 2 つの研究が、反論の形で結果が変わると示した。[反論への追従を調べた研究](https://arxiv.org/abs/2509.16533)では、元の答えと反論を同時に並べて評価させるより、答えたあとの会話で利用者に反論されるほうが、答えを変えやすかった。理由をつけた反論は、結論が誤っていても通りやすかった。[SycEval](https://arxiv.org/abs/2502.08177)では、引用を添えた反論が、正しい答えを誤りに変える迎合を最も多く誘った（根拠：中）。調べたのは、複数社の、旧い世代を含むモデルである。
- **コードの判断でも**：[コードスメルの検出を調べた研究](https://arxiv.org/abs/2607.10411)では、誤った前提や偏った示唆を添えた問い方にすると、判断の反転率が最大で 72% になった（根拠：弱）。査読前の単独の研究で、ここに書いたのは要旨に書かれた範囲だけである。対象のモデルは要旨からは分からない。

つまり、賛成の多さは、案の質を測った値ではない。案が同じままでも、賛成は増える。前提を書き添えても、押し返しても、理由をつけて反論しても、同じことが起きる。

ここに挙げた研究は、AI の賛成を技術の判断の正しさの証拠にすることを直接調べたものではない。モデルも当時のものなので、今の Claude の傾向として読まず、自分の場面に当てはめるときは類推とする。

聞き方を整えて賛成が減っても、案が正しいという証拠が増えるわけではない。賛成を減らす聞き方は、<!-- link:begin ask-without-sycophancy -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）（準備中）<!-- link:end -->が扱う。

## 迎合された応答は信頼され、好まれる {#hard-to-notice}

迎合（利用者の考えに合わせて賛成すること）された応答を、人は質が高いと感じ、信頼し、好む傾向がある。

対人の相談を題材にした研究が、迎合された人の反応を調べた。2026 年 3 月に Science で公刊された研究で、参考に挙げたのは[査読前の版](https://arxiv.org/abs/2510.01395)である。この研究は、11 のモデルが人より約 5 割多く利用者の行動を肯定したと報告した。分析の方法を先に公開する事前登録の実験では、迎合的な AI と 1 回話しただけで、責任を取って関係を修復しようとする意思が下がり、自分が正しいという確信が上がった。それでも参加者は、迎合的なモデルのほうを信頼し、好んだ（根拠：強・類推）。ただし、技術の判断を直接調べた実験ではない。

ここから先は推論になる。賛成されると確信が上がり、確信が上がると確かめる動機が下がる、という流れが考えられる。賛成した相手は質が高く見えるので、その相手の次の賛成も重く受け取りやすい。そのため、注意して見抜く心がけだけでは、迎合を防ぎきれない（推論・実践例なし）。

見抜く心がけに頼らず、「採る理由に AI の賛成を書かない」という決まりで防ぐ。

## AI レビュアーの一致 {#reviewer-agreement}

複数の AI レビュアーが全員「問題なし」と答えても、方針が正しい根拠には数えない。全員一致が示すのは、どのレビュアーも問題を見つけなかったところまでである。人数を増やしても根拠が増えない理由は、次の 3 つである。

- **偏りが同じ向き**：ICLR 2024 の研究では、調べた複数のアシスタントがそろって迎合を示した（根拠：強）。賛成に傾く者を人数分そろえても、同じ傾きが繰り返されるだけである。
- **同じものを見ている**：同じ文書と同じ依頼文を見せると、書き添えた好みや前提が、全員を同じ向きに押す。一致は、押す力が 1 つだったことの表れかもしれない。
- **レビュー役にしても甘い**：[Anthropic の 2026 年 3 月の報告](https://www.anthropic.com/research/harness-design-long-running-apps)によると、エージェントに自分が作ったものを評価させると、出来が凡庸でも、自信を持って褒める。作る役とは別に、調整していない Claude を QA 役にしても、正当な問題を見つけたあとで、大した問題ではないと自分を説得して承認した。QA 役を使える水準にするには、例を付けた採点の基準を与え、人の判断とのずれを見て指示を直す作業が、数回要った（根拠：中）。実験は Anthropic が組んだ特定の仕組みで、Sonnet 4.5 から Opus 4.6 までの世代を使っている。結果はモデルの版に依存する。

AI レビュアーは、問題を見つけさせる道具として使う。人の判定と基準を合わせていない AI レビュアーの「問題なし」は、合格を決める判定に使わない。指摘は、再現や実行で確かめられる。「問題なし」は、どこを見てそう言ったのかが分からず、確かめる手がかりがない。指摘ごとに確かめ方（再現の手順や実行するコマンド）を付けさせると、受け取った側がそのまま実行して確かめられる。依頼の書き方は、<!-- link:begin instructing-reviewers -->レビュアーへの指示の書き方（準備中）<!-- link:end -->にある。

レビューする者を変更の書き手から分ける理由と分け方は、<!-- link:begin independent-review -->[書いた本人ではない者にレビューさせる](../verify/independent-review.md)<!-- link:end -->にある。別のモデルに第二の意見を求める使いどころは、<!-- link:begin second-opinion-from-another-model -->別のモデルに第二の意見を求める（一致は証拠にならない）（準備中）<!-- link:end -->にある。

人の判定と比べて基準を合わせた AI の採点は、扱いが別になる。人の判定とどれだけ一致するかを測り、その度合いを添えれば、計測の一種として使える。合わせ方は、<!-- link:begin model-based-grading -->Claude に採点させる（人の判定で較正する）（準備中）<!-- link:end -->にある。

!!! example "判断例：AI レビュアー 3 つが全部「問題なし」と答えた変更"
    - **状況**：決済の再試行の処理を書き換えた。差分を AI レビュアー 3 つ（別々のモデルを含む）に見せると、3 つとも「問題なし」と返した。既存のテストは通っているが、再試行の経路を通るテストはない。再試行の失敗を起こして試すには、模擬の環境を用意する必要があり、半日かかる。今日中に出したい。
    - **迷う候補**：（A）3 つが別々に同じ結論を出し、既存のテストも通っているので、問題なしとして今日中に出す。（B）3 つの一致は参考にとどめ、再試行の失敗を起こして実行し、結果を見てから出す。出すのは明日になるかもしれない。（C）今日中に出し、再試行の経路は未確認と書いて、問題が出たら戻せるようにしておく。
    - **選んだもの**：B。
    - **理由**：3 つの一致が示すのは、誰も問題を見つけなかったことまでで、再試行が正しく動くことではない。同じ差分と依頼文を見ているなら、3 つは同じ向きに押されている。失敗を起こして実行した出力は、AI の賛成と無関係に結果が決まる。決済の誤りは、二重の請求のように取り消しにくいので、戻せる前提で出す C は選ばない。

## 証拠として数えるもの {#what-counts}

証拠に数えるのは、AI の賛成とは別の経路で確かめられるものである。

| 証拠に数える | 証拠に数えない |
| --- | --- |
| 実行の結果（実行したコマンドと、生の出力と、何件中何件かが分かる件数） | Claude が賛成した、褒めた |
| 計測の結果（先に決めた基準で測った数値） | 複数の AI レビュアーが一致した |
| 一次資料と実物（公式の文書・仕様・ログ・git や grep で見た事実） | 人の判定と比べて基準を合わせていない AI の採点 |
| 人が自分で読んで確かめたこと（AI の要約でなく、原文や差分を読んだもの） | 実行も出力も付かない「確認しました」の報告 |

実行・計測・一次資料は、AI が何と言っても結果が変わらない。AI の採点は例外で、人の判定と比べて基準を合わせ、一致の度合いを測ったものに限って、計測の結果として数える。

報告と事実が食い違ったときは、実行・grep・git で見た事実を正とする。詳しくは、<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](../verify/evidence-not-reports.md)<!-- link:end -->を見る。

AI の承認は、人の承認に数えない。承認の数をリスクの段で決める方法は、<!-- link:begin risk-tiered-approval -->リスク段階別の承認（AI の承認を人の承認に数えない）（準備中）<!-- link:end -->にある。

AI が挙げた指摘や懸念は、どこから確かめるかを決める手がかりになる。賛成された所も、確かめを省く理由にはならない。AI が挙げた指摘は、再現できたときの結果が証拠になる。

場面ごとに、証拠に当たるものを挙げる。開発では、失敗を起こして実行した出力や、変更した経路を通るテストの結果が当たる。コンテストでは、小さい入力で、遅くても確実な全探索の答えと突き合わせた結果や、手元で回して出たスコアが当たる。

実行や計測がすぐにできない判断では、手元にある AI の賛成は、証拠の代わりにならない。その判断は、確かめていない決定として扱う。採るなら「未確認」と書き、取り消しやすい形で採り、実行か計測ができる最初の機会に置き換える（推論・実践例なし）。

## 人が握るもの {#what-you-keep}

AI が何体賛成しても、人が手放さないものは 3 つある。採る基準と、採るかやめるかの決定と、中核の理解である。

- **採る基準**：案を AI に見せる前の段階で、何が出たら採り、何が出たらやめるかを書く。先に書いておけば、結果が出たあとに基準を動かせない。
- **採る・やめるの決定**：決めるのは人である。決めたら、根拠を一文で書く。その一文に AI の賛成が入っていたら、実行・計測・一次資料で置き換える。
- **中核の理解**：設計の要になる部分は、AI の説明を読んだだけで済ませず、自分で説明できる状態にする。自分で説明できない部分は、AI の賛成が正しいかを自分では判断できず、賛成に頼るしかなくなる。判断を預けすぎる問題は、<!-- link:begin over-reliance -->[判断を預けすぎる（過度依存）](over-reliance.md)<!-- link:end -->にある。

チームでは、「AI の同意は根拠に数えない」を決まりにして、疑う役を持ち回りで置き、案の理由に AI の賛成が入っていないかを見させる。役の分け方は、<!-- link:begin separate-roles#against-sycophancy -->役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）（準備中）<!-- link:end -->にある。ガイドラインへの書き方は、<!-- link:begin ai-usage-guidelines -->社内ガイドラインに書くこと（準備中）<!-- link:end -->にある。

## 確かめ方 {#how-to-check}

自分の判断が AI の賛成に寄りかかっていないかは、採る前と振り返りの 2 つの場面で確かめる。

採る前に、次を確かめる。

- 採る理由に、AI の賛成や一致が入っていないか。入っていれば、実行・計測・一次資料の結果に置き換えたか
- 賛成を得た依頼文に、自分の好みや前提を書き添えていないか。押し返して得た賛成ではないか
- 一致したレビュアーが、同じ文書と同じ依頼文を見ていないか。見ていれば、一致は 1 つの意見が繰り返されただけかもしれない。見ていなくても、一致は根拠に数えない
- AI が挙げた指摘は、実行して確かめたか。確かめていない指摘には「未確認」と書いたか
- 「問題なし」と言われた範囲のうち、実行していない所はどこか

振り返りでは、次を確かめる。

- AI が賛成した案は何件あり、そのうち実行や計測で確かめたのは何件、外れたのは何件か。日付つきで記録しているか
- 件数が少ないうちは傾向として読み、断定していないか。確かめた案のうち外れた割合は、数件でも、自分の環境で賛成がどれだけ当てにならないかの目安になる
- 振り返りの評価を AI に任せていないか。AI には集計だけを頼む進め方は、<!-- link:begin retros-without-ai-verdicts -->振り返りで AI に評価させない（集計係にとどめる）（準備中）<!-- link:end -->にある

どの確かめでも、賛成に寄りかかっている点が見つかったら、その賛成は根拠から外し、実行・計測・一次資料で確かめ直す。確かめ直すまでは「未確認」と書く。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html)：ICLR・英語・確認日 2026-11-04
- [ELEPHANT: Measuring and understanding social sycophancy in LLMs](https://arxiv.org/abs/2505.13995)：arXiv（Cheng, Myra ほか）・英語・確認日 2026-11-04
- [How people ask Claude for personal guidance](https://www.anthropic.com/research/claude-personal-guidance)：Anthropic・英語・確認日 2026-11-04
- [SycEval: Evaluating LLM Sycophancy](https://arxiv.org/abs/2502.08177)：arXiv（Fanous, Aaron ほか）・英語・確認日 2026-11-04
- [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://arxiv.org/abs/2509.16533)：arXiv（Kim, Sungwon ほか）・英語・確認日 2026-11-04
- [Mitigating LLM Sycophancy in Code Smell Detection Using Evidence-Guided Reasoning Prompts](https://arxiv.org/abs/2607.10411)：arXiv（Fahad, Istiaq Ahmed ほか）・英語・確認日 2026-11-04
- [Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence](https://arxiv.org/abs/2510.01395)：arXiv（Cheng, Myra ほか）・英語・確認日 2026-11-04
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [人の側の五つの落とし穴（総論）](human-pitfalls.md)
- [迎合（sycophancy）](../basics/sycophancy.md)

**次に読む**

- 迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）（準備中）
- 振り返りで AI に評価させない（集計係にとどめる）（準備中）
- PR を作り、レビューを受ける（準備中）
- リスク段階別の承認（AI の承認を人の承認に数えない）（準備中）

**関連**

- [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- 別のモデルに第二の意見を求める（一致は証拠にならない）（準備中）
- Claude に採点させる（人の判定で較正する）（準備中）
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）（準備中）
- 社内ガイドラインに書くこと（準備中）
- レビュアーへの指示の書き方（準備中）
- [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- [判断を預けすぎる（過度依存）](over-reliance.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
