---
id: what-not-to-delegate
title: 任せないもの（評価・採否・撤退・中核の理解）
aliases: [人が握るもの, 任せてはいけないこと]
type: concept
field: delegate
chapter: 任せる前の判断
order: 10
level: 任せる
priority: 必須
surfaces: [app, claude-code]
principle: [握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, やめられない]
scenes: [開発, データ分析, コンテスト]
summary: 評価の定義・採否・撤退・中核の理解など、どの段階でも人が握るものと、任せてよいものの分け方が分かる。分ける軸は、出力を機械的に確かめられるかである。
signs:
  - {type: goal, text: AI にどこまで任せてよいか、線を引きたい}
  - {type: symptom, text: AI の案をそのまま採って、なぜそうしたか説明できない}
  - {type: situation, text: 評価の基準まで AI に作らせている}
prerequisites: [four-principles]
related: [verifier-defines-problem, decide-when-to-quit, how-much-understanding-to-keep, over-reliance, agreement-is-not-evidence, is-the-task-ai-suited, pairing-and-delegating, five-questions-before-delegating, open-ended-loop-trap, separate-roles, risk-tiered-approval, think-before-asking, roadmap]
sources: [sakana-icfp, sakana-ahc058, nvidia-winning-kaggle-competition-generative-ai, zenn-chiman-b233cc80, battlecode-2026-lorem-ipsum-pdf, arxiv-2603-21551, understandingai-openai-model-crushed-top-human, pmc-vaccaro-2024-human-ai-combinations, sleesman-2012-escalation-commitment]
volatility: 低
sections:
  - {title: どの段階でも人が握るもの, anchor: what-humans-hold}
  - {title: 任せてよいもの, anchor: what-to-delegate}
  - {title: 分ける軸：機械的に確かめられるか, anchor: verifiable-axis}
  - {title: 握ることが防ぐもの, anchor: what-it-prevents}
  - {title: 案の出どころより、誰がどの評価で採ったか, anchor: who-adopted}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：評価の定義・採否・撤退・中核の理解など、どの段階でも人が握るものと、任せてよいものの分け方が分かる。
    - **いつ引くか**：AI にどこまで任せてよいか、線を引きたいとき。AI の案をそのまま採って、なぜそうしたか説明できないとき。評価の基準まで AI に作らせているとき。
    - **前提**：<!-- link:begin four-principles -->[四つの原理と比例則（見せる・確かめる・縛る・握る）](../start/four-principles.md)<!-- link:end -->

<!-- textlint-disable -->
別名：人が握るもの・任せてはいけないこと
<!-- textlint-enable -->

任せないものとは、AI に作業を渡しても人の手元に残す判断の一覧である。原理でいえば「握る」にあたり、任せる幅をどれだけ広げても減らない。

## どの段階でも人が握るもの {#what-humans-hold}

人が握るものは、評価の定義、戦略の採否と撤退、中核コードの理解、本番環境の制約の 4 つである。

- **評価の定義**：評価器、CV の切り方、採否の基準を決めること。何を良しとするかがここで決まり、誤ればその後の作業はすべて誤った目標へ向かう。理由は <!-- link:begin verifier-defines-problem#why -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 検証器に映ったものだけが目標になる](../eval/verifier-defines-problem.md#why)<!-- link:end --> で扱う。
- **戦略の採否と撤退**：どの案を採り、いつやめるかを決めること。基準は着手前に書き、判定は作った本人から離す。やり方は <!-- link:begin decide-when-to-quit#write-criteria-first -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 基準を着手前に書く](../judgment/decide-when-to-quit.md#write-criteria-first)<!-- link:end --> にある。
- **中核コードの理解**：中核は説明できるまで確かめ、説明できないものは採らない。線の引き方は <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける（準備中）<!-- link:end --> にある。
- **本番環境の制約**：本番で守る規則や運用上の制限を把握すること。AI の手元には見えていない前提があるので、人が持ち込む。

この一覧は、段階を上がっても短くならない。段階ごとの位置づけは <!-- link:begin roadmap#always-hold -->[ロードマップ（委任の段階別） › どの段階でも人が握るもの](../start/roadmap.md#always-hold)<!-- link:end --> にまとまっている。

## 任せてよいもの {#what-to-delegate}

任せてよいものは、実装量の多い作業、評価環境の周辺作業、集計、可視化、定型の高速化である。いずれも、結果を機械的に確かめられる。

| 任せてよい | 人が握る |
| --- | --- |
| 実装量の多い作業 | 評価の定義（評価器・CV・採否基準） |
| 評価環境の周辺作業 | 戦略の採否と撤退 |
| 集計・可視化 | 中核コードの理解 |
| 定型の高速化 | 本番環境の制約 |

コンテストや競技の事例も、この分け方に沿っている。

- ICFP 2025 で 1 位のチームでは、人が全体戦略、手書きの SAT エンコーディング、テスト基盤を作った。ShinkaEvolve（進化的探索でコードを改良する道具）はその枠の中でソルバを進化させた。「人が枠と評価を作り、AI が量を回す」分業の実例である（根拠：中、一次報告）。
- AtCoder Heuristic Contest の AHC056 で 1 位の参加者が AI に任せたのは、前計算の SIMD 化とビット並列化だけだった（根拠：弱、体験記）。
- Kaggle で 1 位の参加者は、3 つのモデルに 60 万行を超えるコードを生成させた。追うアイデアの選択とワークフローの指揮は自分で行った（根拠：中、企業ブログ）。
- Battlecode 2026 のあるチームは、経路探索の初版や通信のビット符号化を AI に書かせた。戦略判断とデバッグはすべて自分で行った（根拠：弱、参加チーム自身の振り返り。対戦型の競技で、他の領域には類推）。

これらは「勝ち方」の真似ではなく、どこを任せてどこを握ったかの構造を取り出したものである。AI 単独の優勝事例を手順として真似ることは勧めない。

## 分ける軸：機械的に確かめられるか {#verifiable-axis}

任せるか握るかを分ける軸は、出力を機械的・客観的に確かめられるかである。テストが通る、スコアが出る、高速化の前後で出力が一致する。こうした確かめ方があれば、任せて結果で判断できる。良し悪しの基準、採る方針、動く理由は確かめる側の問題なので、人が握る。

この軸が効く理由は、検証器が問題を定義するからである。Claude は渡された検証器が定める問題を解き、置かれたループを何でも速める。検証器が誤っていれば、誤りも同じ速さで増える。詳しくは <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end --> にある。評価を任せないのは、この「確かめる側」を AI に作らせると、確かめる仕組みが消えるからである。

軸には 2 つの使い方の注意がある。

- 確かめられる作業でも、結果を採るかは人が決める。スコアが上がっても、その案を採ってよいとは限らない。
- 任せる幅を広げるほど、確かめる仕組みと封じ込めを強める。比例則は <!-- link:begin four-principles#proportional-rule -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 比例則](../start/four-principles.md#proportional-rule)<!-- link:end --> にある。無人で走らせる前の確認は <!-- link:begin five-questions-before-delegating#five-questions -->[任せ方の段階と、無人で走らせる前の五つの問い › 無人で走らせる前の五つの問い](five-questions-before-delegating.md#five-questions)<!-- link:end --> で行う。

作業そのものが AI に向くかの見積もりは、<!-- link:begin is-the-task-ai-suited#five-axes -->そのタスクは AI に向いているか（五つの軸） › 五つの軸（準備中）<!-- link:end --> で行う。欠ける軸があれば、その部分は人が受け持つ。

!!! example "判断例：高速化を頼むとき、評価スクリプトはどちらが書くか"
    - **状況**：ヒューリスティック系のコンテストで、解法の実行が遅い。AI に高速化を頼みたい。
    - **迷う候補**：評価スクリプトまで AI に書かせてスコアが上がった案を採る方法と、評価スクリプトは自分で書いて前計算の高速化だけを AI に頼む方法。
    - **選んだもの**：評価スクリプトは自分で書く方法。
    - **理由**：前者は手間が少ないが、評価の定義まで AI へ渡してしまう。高速化は出力が元と一致するかで機械的に確かめられるので任せてよい。評価スクリプトは確かめる側そのものなので、人が握る。

## 握ることが防ぐもの {#what-it-prevents}

握る原理は、人が 4 つのものを持ち続けることである。良しとする基準、採る案、やめる時期、中核の理解である。原理の一覧での位置は <!-- link:begin four-principles#hold -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 握る](../start/four-principles.md#hold)<!-- link:end --> にある。握らないと、次のことが起きる。

評価の基準まで AI に作らせ、その基準で出た案を採る。結果は良く見えるが、なぜその案を採ったのか、基準が妥当なのかを自分で説明できない。Claude 側の原因は、確かめていないことである。完了や良し悪しを検証器や人の評価でなく、出力の自己申告やもっともらしさで決めている。AI の賛成や、AI レビュアー同士の一致は、確かめたことに数えない。理由は <!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end --> にある。

人の側の落とし穴は 2 つある。

- **預けすぎる**：判断まで預けると、もっともらしい誤りをそのまま採る。Vaccaro らのメタ分析（Nature Human Behaviour、2024）は、2020 年 1 月〜2023 年 6 月の 74 論文・106 実験を対象にした。人と AI の組み合わせは、人と AI の良いほう単独より平均で劣った（g=−0.23）。判断課題では損が出た（g=−0.27）。知識労働の結果であり、現行の Claude への当てはめは類推である（根拠：強・類推）。手元に残す判断は <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end --> にある。
- **やめられない**：費やした分だけ、方針を捨てにくくなる。Sleesman らのメタ分析（Academy of Management Journal、2012。166 の独立な標本）では、時間の投資と、初期の決定への個人の責任が固執を強めた。組織の意思決定での結果である（根拠：強）。AI の速さが固執を強めるかは、研究と実践例のどちらもない推論である。撤退の基準を先に書く方法は <!-- link:begin decide-when-to-quit#why-escalation -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › なぜやめられなくなるか](../judgment/decide-when-to-quit.md#why-escalation)<!-- link:end --> にある。

## 案の出どころより、誰がどの評価で採ったか {#who-adopted}

「考察は人間にしかできない」という断定は誤りである。逆に「AI に任せれば十分」とも言えない。問うべきは案の出どころでなく、誰がどの評価で採ったかである。

- AtCoder World Tour Finals 2026 の Heuristic 部門では、OpenAI のモデルが人間の上位勢を上回ったと報じられている（根拠：弱、二次の報道）。報道どおりなら、考察の出どころが AI であることは、すでに起こりうる。
- AHC058 の作問者は、貪欲法に必要と想定した実験的な洞察がエージェントのログに見られなかったと述べた。貪欲部分の考察の精度は人が上だとも述べた（根拠：中）。
- CSAW の LLM CTF 部門の 2025 年の結果では、平均解答数が人主導で 2.7、エージェントで 5.5、ハイブリッドで 7.7 だった（根拠：中、小標本。CTF の教育の場の結果で、他の領域には類推）。
- Kaggle で 3,803 チーム中 5 位になった事例では、成功した施策 11 件のうち 8 件が人の発案だった（根拠：弱、自己申告の体験記）。

事例の向きは割れている。そのため、案の出どころを人と AI のどちらかに決め付けず、採るときの手順を決める。案ごとに、出どころ、採った評価、採った人を残す。評価は人が定義した検証器や基準にし、AI の賛成は数えない。判定を実装した人から離す方法は <!-- link:begin separate-roles#against-sycophancy -->役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）（準備中）<!-- link:end --> にある。AI の承認を人の承認に数えない考え方は <!-- link:begin risk-tiered-approval#ai-approval-doesnt-count -->リスク段階別の承認（AI の承認を人の承認に数えない） › AI の承認を数えない（準備中）<!-- link:end --> にある。考察そのものは、先に自分の案を書いてから AI に問いや反論を頼む順にすると、自分の案が AI の案に置き換わるのを避けやすい。順序と使い分けは <!-- link:begin think-before-asking#self-first -->頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI（準備中）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [ShinkaEvolve in Action: How a Human-AI Partnership Conquered a Coding Challenge](https://sakana.ai/icfp-2025/)：Sakana AI・英語・確認日 2026-11-04
- [Sakana AI Agent Wins AtCoder Heuristic Contest (First AI to Place 1st)](https://sakana.ai/ahc058/)：Sakana AI・英語・確認日 2026-11-04
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/)：NVIDIA Developer Blog・英語・確認日 2026-11-04
- [Claude Code / CodexでKaggle金メダルを取った話](https://zenn.dev/chiman/articles/b233cc808d6af3)：Zenn（chiman）・確認日 2026-11-04
- [Battlecode 2026 Postmortem（Lorem Ipsum）](https://battlecode.org/assets/files/postmortem-2026-lorem-ipsum.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [AI In Cybersecurity Education -- Scalable Agentic CTF Design Principles and Educational Outcomes](https://arxiv.org/abs/2603.21551)：arXiv（Xi, Haoran ほか）・英語・確認日 2026-11-04
- [An OpenAI model crushed top human programmers at a world coding competition](https://www.understandingai.org/p/an-openai-model-crushed-top-human)：Understanding AI・英語・確認日 2026-11-04
- [When combinations of humans and AI are useful: A systematic review and meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11659167/)：PubMed Central・英語・確認日 2026-11-04
- [Cleaning Up the Big Muddy: A Meta-Analytic Review of the Determinants of Escalation of Commitment](https://gwern.net/doc/psychology/cognitive-bias/sunk-cost/2012-sleesman.pdf)：gwern.net（論文の写し）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [四つの原理と比例則（見せる・確かめる・縛る・握る）](../start/four-principles.md)

**次に読む**

- [任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)
- 伴走と委託（準備中）

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- どこまで理解を手放してよいか（中核と周辺）（準備中）
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- そのタスクは AI に向いているか（五つの軸）（準備中）
- AI に改善を回させ続ける罠（開いたループ）（準備中）
- 役割を分ける（書く人・承認する人・疑う人）（準備中）
- リスク段階別の承認（AI の承認を人の承認に数えない）（準備中）
- 頼む前に自分で考える（AI には問い・反論・道具を頼む）（準備中）
- [ロードマップ（委任の段階別）](../start/roadmap.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
