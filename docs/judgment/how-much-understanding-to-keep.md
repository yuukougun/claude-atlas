---
id: how-much-understanding-to-keep
title: どこまで理解を手放してよいか（中核と周辺）
aliases: [理解の外注, 監督のパラドックス, 説明できないコードを出荷しない, 認知負債]
type: judgment
field: judgment
chapter: 理解を手放さない
order: 90
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [握る]
prevents: []
pitfalls: [預けすぎる]
scenes: [開発, コンテスト, チーム]
summary: コードを中核と周辺に分け、周辺は任せきり、中核は説明できるまで理解を確かめる線引きと、任せるほど確かめる力が衰えうることへの備えが分かる。
signs:
  - {type: symptom, text: AI が書いたコードが増えて、全体を把握できなくなってきた}
  - {type: symptom, text: AI に書かせたコードを、自分では説明できない}
  - {type: goal, text: どこまで AI に任せて、どこは自分で理解しておくか決めたい}
  - {type: situation, text: 障害が起きたら、自分でデバッグしなければならない部分がある}
prerequisites: [learning-with-ai]
related: [what-not-to-delegate, own-generated-code, diffs-humans-must-read, review-bottlenecks, pairing-and-delegating, practice-vs-contest-day, over-reliance, independent-review, create-and-review-prs, human-pitfalls]
tracks: []
outdated_advice: []
sources: [anthropic-research-ai-assistance-coding-skills, arxiv-2601-20245, anthropic-research-ai-transforming-work-anthropic, rustc-dev-guide-llm-guidance-reviewing, speakerdeck-twada-agentic-software-engineering]
volatility: 低
sections:
  - {title: 理解を手放し続けると何が起きるか, anchor: what-happens}
  - {title: 中核と周辺を分ける, anchor: core-and-periphery}
  - {title: 説明できないものは採らない, anchor: explain-or-reject}
  - {title: 確かめる力が衰える（監督のパラドックス）, anchor: supervision-paradox}
  - {title: AI を使わない時間を残す, anchor: ai-free-time}
  - {title: 線引きが守れているかの確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：コードを中核と周辺に分け、周辺は任せきり、中核は説明できるまで採らない線を引ける。
    - **いつ引くか**：AI の書くコードが増えて、全体を把握できないとき。書かせたコードを自分で説明できないとき。障害のとき、自力でデバッグする部分を決めたいとき。
    - **前提**：<!-- link:begin learning-with-ai -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](learning-with-ai.md)<!-- link:end -->

<!-- textlint-disable -->
別名：理解の外注・監督のパラドックス・説明できないコードを出荷しない・認知負債
<!-- textlint-enable -->

AI にコードを書かせる量が増えると、全部を同じ深さで理解し続けることはできなくなる。このページは、理解をどこまで手放してよいかの線引きと、手放し続けた先で起きること、その備えを扱う。結論は、手放す範囲を決めて手放し、手放さない範囲は説明できるまで確かめる、である。

## 理解を手放し続けると何が起きるか {#what-happens}

自分で理解を組み立てないまま AI に任せ続けると、その分の理解の不足があとで返ってくる。これを認知負債という。用語は[用語集](../start/glossary.md#cognitive-debt)にある。

返ってくる場面は、自分でデバッグするときである。Anthropic が 2026 年に公表した研究（論文は arXiv 2601.20245）では、新しいライブラリを学ぶ課題で、AI を使った群と手で書いた群を比べた。理解度クイズで差が最も大きかったのは、デバッグの問題である（根拠：強）。手で書いた群は課題中にエラーへ多く出会っていた（中央値 3 対 1）。著者らは、自力でエラーを解いた経験が、デバッグ能力の形成に寄与した可能性を述べている（根拠：中）。

使い方の型で見ると、理解度が最も低かったのは、デバッグと検証を AI に任せた型だった。ただし各型は n=4 の小さな群で、因果は主張されていない。AI 群のアシスタントは GPT-4o をもとにしたもので、クイズは課題の直後に行われた。Claude に固有の結果でも、長期の結果でもない。研究の詳細は、前提のページが扱う。<!-- link:begin learning-with-ai#faster-but-shallower -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 速さの得は確かめられず、理解は残りにくい](learning-with-ai.md#faster-but-shallower)<!-- link:end -->

実務の側にも同じ警告がある。ある実務家は、理解が追いつかないまま増えるコードを認知負債と呼ぶ。そして、計画の出口で理解を確かめることと、図で説明させることを勧めている（根拠：弱。立場の表明）。Rust コンパイラの開発ガイドは、LLM が生成したコードを含む変更について、レビュアーが作者に、自分の言葉での説明、バグの再現、エッジケースの列挙を求めるよう指示している。

## 中核と周辺を分ける {#core-and-periphery}

コードを、本番で自分がデバッグする必要のある中核と、それ以外の周辺に分ける。周辺は任せきり、中核は理解を確かめながら進める。

| 区分 | 例 | 進め方 |
| --- | --- | --- |
| 周辺 | ログの整形、可視化の道具、集計の補助 | 丸投げしてよい。動かして出力を見れば足りる |
| 中核 | 評価関数、探索、相手のモデル化、通信、提出や配備の流れ | 生成させた後に理解を確かめる型か、概念を質問して自力でデバッグする型で進める |

線を引く目安は 3 つある。

- 壊れたとき、自分が原因を探すことになるか。探すなら中核である。
- 間違いが黙って通るか。出力を見ても誤りに気づけないものは、中核に寄せる。
- 出力を機械的に確かめられるか。確かめられる周辺は任せやすい。この軸は<!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](../delegate/what-not-to-delegate.md#verifiable-axis)<!-- link:end -->が扱う。

周辺を任せきるには、任せた分を確かめる守りが先に要る。周辺でも、差分の中の赤信号は人が読む。読み分けは<!-- link:begin diffs-humans-must-read#core-vs-periphery -->[人間が読むべき差分の箇所 › 要の処理と周辺の読み分け](../verify/diffs-humans-must-read.md#core-vs-periphery)<!-- link:end -->にある。どの段階でも人が握るもの（評価の定義、採否、撤退）は、線引きとは別の話である。扱うのは<!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end -->が扱う。

線はあとで動く。周辺に置いたものが障害の原因になったら、中核に引き上げる。引き上げる条件は、任せる前に決めておく。

## 説明できないものは採らない {#explain-or-reject}

中核の変更は、自分の言葉で説明できるまで採らない。評価の基準は、AI を使ったかどうかではなく、説明できるか、確かめたかである。

説明の確認の例を挙げる。チームメイトに、変更の目的、処理の流れ、入力の端の扱いを、数行で説明する。数行の行数に根拠はなく、あくまで例である。言い直せない所が、読み直す箇所になる。説明させて確かめる手順は、<!-- link:begin own-generated-code#explain -->[生成コードを自分のものにする › 処理の流れと入力の端を説明させる](../verify/own-generated-code.md#explain)<!-- link:end -->と<!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end -->が扱う。

説明できない理由が AI の説明を読んでいないだけなら、読めば済む。読んでも言い直せないなら、そのコードを採らず、小さく作り直させるか、自分で書く。

AI にレビューさせて通っても、説明できたことにはならない。AI の承認は人の承認に数えない。理由は<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end -->を参照する。PR の説明を自分の言葉で書けるまで読む手順は、<!-- link:begin create-and-review-prs#pr-description -->PR を作り、レビューを受ける › PR の説明に書くこと（準備中）<!-- link:end -->にある。

!!! example "判断例：AI が書いた集計と課金計算を、期日までに出す"
    - **状況**：小さな社内サービスで、AI がログ整形、集計バッチ、課金の計算を書いた。期日が近く、全部を読む時間はない。
    - **迷う候補**：全部の差分を同じ深さで読んで、出す日を遅らせる。または、ログ整形と集計は動作確認だけで通し、課金の計算だけ説明できるまで確かめる。
    - **選んだもの**：後者。課金の計算は、入力の端と丸めの扱いを自分の言葉で説明してから採る。
    - **理由**：課金の誤りは黙って通り、障害のときに自分で原因を探すことになる。ログ整形と集計は、出力を見れば誤りに気づける。ただし、集計が課金の入力になっているなら、集計も中核に寄せる。

どちらの候補にも筋は通る。出す日を動かせないときは後者になり、日を動かせるなら前者もありうる。その場合も、全部を同じ深さで読むと、レビューが詰まる。流す量の合わせ方は<!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](../team/review-bottlenecks.md#match-review-capacity)<!-- link:end -->が扱う。

## 確かめる力が衰える（監督のパラドックス） {#supervision-paradox}

AI の出力を確かめるには、確かめる側にコーディングの力が要る。ところが AI を多用すると、その力そのものが衰えうる。これを監督のパラドックスと呼ぶ。任せるほど確かめるという原則が、確かめる力を前提にしているため、この衰えは原則を内側から崩す。

Anthropic の社内調査では、この懸念が挙がっている。Claude でできる作業を、あえて自力でやる技術者もいる（根拠：中。企業の社内調査であり、標本と手法の詳細は確かめていない）。

衰えは気づきにくい。任せている間は、成果物が出続けるからである。確かめる力が落ちたことは、確かめるべき場面で初めて分かる。判断を預けすぎる一般の仕組みは<!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](over-reliance.md#what-to-keep)<!-- link:end -->が、人の側の 5 つの落とし穴の全体は<!-- link:begin human-pitfalls#five-pitfalls -->[人の側の五つの落とし穴（総論） › 五つの落とし穴の一覧](human-pitfalls.md#five-pitfalls)<!-- link:end -->が扱う。

## AI を使わない時間を残す {#ai-free-time}

衰えへの備えとして、定期的に、AI を使わずに実装とデバッグをする時間を残す。課題として課すのではなく、習慣としての推奨にとどめる（根拠：中）。この習慣の効果を直接測った研究は、この辞典の資料には含まれていない。

残す時間には、次のような使い方がある。

- 中核に近い小さな不具合を、AI なしで直す。
- 週次の振り返りで、AI なしの時間を取れたかを確かめる。
- チームなら、批評担当を持ち回りにして、説明できない変更を指摘する役を固定しない。

見ながら一緒に進める伴走と、任せて後で確かめる委託では、理解の残り方が違う。選び方は<!-- link:begin pairing-and-delegating -->伴走と委託（準備中）<!-- link:end -->が扱う。

AI を禁じる大会を目指す場合は、練習で AI を解説役にしつつ、本番の条件で自力を確かめる。<!-- link:begin practice-vs-contest-day#test-under-contest-conditions -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 本番の条件で自力を確かめる](../contest/practice-vs-contest-day.md#test-under-contest-conditions)<!-- link:end -->を参照する。

## 線引きが守れているかの確かめ方 {#how-to-check}

線引きは、決めただけでは守れているか分からない。記録を付けて測り、見直しの条件を先に決める。

1. 週ごとに、AI に任せた変更のうち中核に当たるものを数える。そのうち、自分の言葉で説明できたものの数を並べる。説明できた割合が下がったら、任せる幅を狭める。
2. 中核に近い小さな不具合を、AI なしで直せるかを定期的に試す。直せないなら、AI なしの時間を増やす。
3. 障害の原因が周辺にあったら、その部分を中核に引き上げる。
4. 見直しの条件を、任せ始める前に書いておく。「説明できない変更が続いたら任せる幅を狭める」のように、結果を見る前に、動かしにくい形で決める。

この 4 項目は、この辞典の推奨であり、効果を測った研究はない。測れるのは自分の記録だけである。割合の目標は、記録を付けてから自分で決める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)：Anthropic・英語・確認日 2026-11-04
- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245)：arXiv（Shen, Judy Hanwen ほか）・英語・確認日 2026-11-04
- [How AI is transforming work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)：Anthropic・英語・確認日 2026-11-04
- [Reviewing code with LLMs](https://rustc-dev-guide.rust-lang.org/llm-guidance/reviewing.html)：Rust Project（rustc-dev-guide）・英語・確認日 2026-11-04
- [2026年のソフトウェア開発を考える（2026/07版） / Agentic Software Engineering 2026-07 Findy Edition](https://speakerdeck.com/twada/agentic-software-engineering-2026-07-findy-edition)：Speaker Deck（twada）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](learning-with-ai.md)

**次に読む**

- [生成コードを自分のものにする](../verify/own-generated-code.md)

**関連**

- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- 伴走と委託（準備中）
- [練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）](../contest/practice-vs-contest-day.md)
- [判断を預けすぎる（過度依存）](over-reliance.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- PR を作り、レビューを受ける（準備中）
- [人の側の五つの落とし穴（総論）](human-pitfalls.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
