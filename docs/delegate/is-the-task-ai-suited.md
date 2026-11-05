---
id: is-the-task-ai-suited
title: そのタスクは AI に向いているか（五つの軸）
aliases: [AI 向きの作業, 任せて効く作業]
type: concept
field: delegate
chapter: 任せる前の判断
order: 20
level: 任せる
priority: 推奨
surfaces: [app, claude-code]
principle: [確かめる, 握る]
prevents: [合っていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析, コンテスト]
summary: 検証器の速さ・典型度・テキストで完結するか・環境の制約・期間の五つの軸で、作業を AI に任せて効くかを見積もれる。欠ける軸があれば、その部分は人が受け持つ。
signs:
  - {type: goal, text: この作業を AI に任せて効くか、始める前に見積もりたい}
  - {type: symptom, text: AI に任せたのに、確かめる手間で結局遅くなった}
prerequisites: [verifier-defines-problem]
related: [what-not-to-delegate, five-questions-before-delegating, verifier-three-conditions, pairing-and-delegating, format-cheatsheet#why-formats-differ, build-test-harness, harness-over-model]
sources: [sakana-ahc058, zenn-microsoft-78e01f59, includesecurity-ctfs-ai-era, anthropic-research-cyber-competitions, battlecode-2026-lorem-ipsum-pdf]
volatility: 低
sections:
  - {title: 五つの軸, anchor: five-axes}
  - {title: 人の価値が残る場面, anchor: where-humans-matter}
  - {title: 軸で見積もる, anchor: how-to-score}
  - {title: 見積もりが防ぐもの, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：検証器の速さ・典型度・テキストで完結するか・環境の制約・期間の 5 つの軸で、作業を AI に任せて効くかを見積もれる。欠ける軸があれば、その部分は人が受け持つ。
    - **いつ引くか**：この作業を AI に任せて効くか、始める前に見積もりたいとき。AI に任せたのに、確かめる手間で結局遅くなったとき。
    - **前提**：<!-- link:begin verifier-defines-problem -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI 向きの作業・任せて効く作業
<!-- textlint-enable -->

そのタスクが AI に向いているかとは、作業を渡す前に、AI に任せて効くかを 5 つの軸で見積もる見方である。原理でいえば「確かめる」と「握る」の組で、結果を確かめる手段がある部分は任せ、ない部分は人が持つ。

この軸の整理は、コンテストの事例と実践からの推論であり、軸ごとの効き方を定量的に比べた研究はない（根拠：中、事例からの推論）。点数を出す式ではなく、任せる前に抜けを見つけるための見取り図として使う。

## 五つの軸 {#five-axes}

軸は 5 つある。検証器の速さ・費用・ノイズ、問題の典型度、入出力がテキストで完結するか、環境の制約、期間と時間圧である。AI が最も効くのは、次の 5 つが揃う作業である。機械的で速く安い検証器がある。問題が典型的である。入出力がテキストで完結する。ローカルで回せる。期間が中程度以上ある（根拠：中、事例からの推論）。

| 軸 | 効く側 | 欠けるとき |
| --- | --- | --- |
| 検証器の速さ・費用・ノイズ | 機械的に、速く、安く、ぶれずに確かめられる | 良し悪しを人が一つずつ見るので、確かめる手間が作業の大半になる |
| 問題の典型度 | 既知の型に近い | 新規の部分は、案の当たり外れを AI も人も見分けにくい |
| 入出力がテキストで完結するか | 読むのも出すのもテキストやコード | 画像・実機・人とのやりとりの部分は、AI の手元に情報が届かない |
| 環境の制約 | ローカルで回せ、道具が揃う | 外部サーバや特定の環境が要る部分は、試行が回らない |
| 期間と時間圧 | 試して直す回数を取れる | 短すぎれば確かめる時間がなく、長すぎれば一貫性が崩れる |

**検証器の速さ・費用・ノイズ**は、5 つの中で最初に見る軸である。Claude は渡された検証器が定める問題を解き、置かれたループを何でも速める。そのため、速く安く確かめられる作業ほど、AI の試行の回数がそのまま効く。AtCoder Heuristic Contest の AHC058 では、局所評価による大量の選別が勝因になった（根拠：中、企業の一次の報告）。ISUCON ではベンチマーカーが検証器になり、エージェントが約 1 時間で上位水準に達した（根拠：弱、参加者の記事）。逆に、検証器が誤っていれば誤りも同じ速さで増える。仕組みは <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end --> にある。検証器が信頼できるかの点検は <!-- link:begin verifier-three-conditions#audit -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 三条件を点検する](../eval/verifier-three-conditions.md#audit)<!-- link:end --> で行う。費用も同じ軸に入る。1 回の確認が高ければ、試行の回数は費用の上限に縛られるので、上限は先に決める。

**問題の典型度**は、似た問題が公開の資料に多いかで見る。CTF の残った難問は、OSINT（公開情報の調査）、推測型、文書化の薄い内部実装だった（根拠：中、セキュリティ企業の記事）。新規の部分ほど、AI の案が合っているかを確かめる手段が少なくなる。

**入出力がテキストで完結するか**は、作業に必要な情報と成果物がテキストとコードに収まるかである。画面の見た目、実機の挙動、人への聞き取りが要る部分は、情報が AI に届かない。届かない情報は、人が文字にして渡すか、人が受け持つ。

**環境の制約**は、試行をローカルで回せるかである。外部のサーバとのやりとりが多い、特定の環境が要る、使える道具が限られる場合は、試して直すループが回らない。環境は作れることもある。検証の環境を作らせる手順は <!-- link:begin build-test-harness#what-to-build -->[検証環境・テスト基盤を作らせる › 何を作らせるか](../recipes/build-test-harness.md#what-to-build)<!-- link:end --> にある。

**期間と時間圧**は、中程度以上の期間があるかである。短い期間では確かめる時間が足りない。長い期間では一貫性が課題になる。CTF では AI の優位が序盤に集中した。Airbnb の CTF では、最初の 60 分で 30 問中 13 問を解いて一時 4 位になったが、最終的には 15 問で 39 位だった（根拠：中、Anthropic の報告）。ISUCON では 3〜4 時間で頭打ちになった（根拠：弱、参加者の記事）。

## 人の価値が残る場面 {#where-humans-matter}

人の価値が残るのは、5 つの軸のどれかが欠ける場面と、AI がそもそも使えない場面である。欠けた軸の部分は、人が受け持つ（根拠：中、事例からの推論）。

- **検証器がないか、ノイズが大きい場面**：対戦のメタ、隠れた本番分布、CV（手元の交差検証）と LB（公開順位）のずれが典型である。Battlecode 2026 では、ローカルの勝率が 85% を超えた改良が、オンラインの練習試合では効果が小さかった。AI に書かせた攻撃のコードは、見えている標的しか考慮せず、直接対決で弱かった（根拠：弱、参加チーム自身の振り返り。対戦型の競技で、他の領域には類推）。手元の勝ちが本番の勝ちを意味するかは <!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](../eval/verifier-three-conditions.md#representative)<!-- link:end --> で問う。
- **新規の問題**：型のない問題の考察は、検証器が速くても当たりを引きにくい。考察の出どころが人か AI かより、誰がどの評価で採ったかを残す。分け方は <!-- link:begin what-not-to-delegate#who-adopted -->[任せないもの（評価・採否・撤退・中核の理解） › 案の出どころより、誰がどの評価で採ったか](what-not-to-delegate.md#who-adopted)<!-- link:end --> にある。
- **非テキストや外部環境とのやりとり**：画面、実機、外部のサービス、人との折衝は、人が間に入る。
- **長時間の一貫性**：長い作業では、方針のぶれや前提の取り違えが積もる。節目で人が方針と進み具合を確かめる。
- **AI がそもそも使えない場面**：大会や職場の規則で、AI の利用が禁じられているか、範囲が決まっている。この場合は軸の見積もりより規則が先に来る。形式ごとの違いは <!-- link:begin format-cheatsheet#why-formats-differ -->[コンテストの形式別の早見表（AI の効き方と人が握るところ） › 形式で効き方が違う理由（五つの軸）](../contest/format-cheatsheet.md#why-formats-differ)<!-- link:end --> にある。規則の条文は、その大会の最新の規則で確かめる。

## 軸で見積もる {#how-to-score}

見積もりは、作業を部分に分けて、部分ごとに 5 つの軸を当てる。作業全体に 1 つの答えを出すと、効く部分が欠ける部分に隠れる。欠ける軸のある部分は、人が受け持つか、欠ける軸を補ってから任せる。補う手の代表は、検証器を先に作ることである。

見積もりそのものを Claude に下書きさせてもよい。次の雛形は、作業と今ある確かめる手段を渡し、軸ごとの判定と、任せる部分・人が受け持つ部分の分け方を出させる。返答は下書きで、採るかどうかは人が決める。

<!-- gen:begin snippet is-the-task-ai-suited/score-five-axes -->
<!-- textlint-disable -->

??? example "雛形：作業を 5 つの軸で見積もらせるプロンプト"

    ```markdown
    次の作業を、AI に任せて効くかの 5 つの軸で見積もってほしい。この依頼では作業を始めず、見積もりだけを出す。

    作業：<任せたい作業を 1〜3 文で>
    今ある確かめる手段：<テスト・採点コマンド・ベンチマーク。なければ「目で見る以外にない」>
    使える環境：<ローカルで回せるか。外部サービスや特定の OS が要るか>
    使える期間：<時間または日数>

    軸ごとに、「効く側」「中間」「欠ける」のどれかと、その理由を 1〜2 文で答える。

    1. 検証器の速さ・費用・ノイズ：結果を確かめる手段は、速く、安く、ぶれずに回せるか。
    2. 問題の典型度：既知の型に近いか、新規の部分が大きいか。
    3. 入出力がテキストで完結するか：画像・音・実機・人とのやりとりが要らないか。
    4. 環境の制約：ローカルで回せるか。外部サーバ・特定の環境・使えない道具はないか。
    5. 期間と時間圧：試して直す回数を確保できる期間があるか。

    そのうえで、次を答える。

    - 作業を「任せて効く部分」と「人が受け持つ部分」に分ける。
    - 欠ける軸がある部分は、人が受け持つ理由を 1 行ずつ書く。
    - 欠ける軸を補える手があれば 1 つ挙げる（例：検証器を先に作る）。

    事実として確かめていない判断には、「推測」と付ける。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet is-the-task-ai-suited/score-five-axes -->

!!! example "判断例：ログの集計を任せるか、障害の原因調査を任せるか"
    - **状況**：夜間バッチの失敗が続いている。ログの集計と、失敗の原因調査の両方を AI に頼みたい。
    - **迷う候補**：両方をまとめて任せる方法と、集計だけを任せて原因調査は自分で進める方法。
    - **選んだもの**：集計だけを任せ、原因調査は自分で進める。
    - **理由**：集計は、入出力がテキストで完結し、手元のログで回せ、結果を件数の突き合わせで確かめられる。原因調査は、本番にしかない状態を見る必要があり、環境の制約と検証器の軸が欠ける。調査の手がかりの整理だけは AI に頼めるが、原因だと採るかは自分で確かめる。

見積もりが「向いている」と出たときも、任せる幅は別に決める。対話・計画の承認・停止条件つきの反復・隔離した無人実行の段階と、無人で走らせる前の確認は <!-- link:begin five-questions-before-delegating#five-questions -->[任せ方の段階と、無人で走らせる前の五つの問い › 無人で走らせる前の五つの問い](five-questions-before-delegating.md#five-questions)<!-- link:end --> で行う。見合う確かめ方と封じ込めを先に整えてから、幅を広げる。見ながら一緒に進めるか、任せて後で確かめるかの選び方は <!-- link:begin pairing-and-delegating -->[伴走と委託](pairing-and-delegating.md)<!-- link:end --> にある。

## 見積もりが防ぐもの {#what-it-prevents}

この見積もりが働く原理は「確かめる」と「握る」である。任せる前に、確かめる手段があるかを見て、ない部分を人が握る。

防ぐ原因は 2 つである。

- **合っていない**：典型でない問題や、情報の届かない部分では、AI の出力は目的に合わなくなりやすい。軸を先に当てると、合っているかを人が見る部分が事前に分かる。
- **確かめていない**：検証器がない、遅い、ぶれる作業では、完了や良し悪しが出力の自己申告やもっともらしさで決まりやすい。検証器の軸を先に見ると、確かめる手段のない部分に気づける。

人の側の落とし穴は、**預けすぎる**ことである。「AI に任せたのに、確かめる手間で結局遅くなった」は、検証器の軸が欠けた作業を丸ごと渡した形に当たることが多い。任せたのは作業で、確かめる負担は人に残っていたからである。握り続けるものの一覧は <!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](what-not-to-delegate.md#what-humans-hold)<!-- link:end --> にある。評価の定義まで任せるときに何が消えるかは <!-- link:begin what-not-to-delegate#what-it-prevents -->[任せないもの（評価・採否・撤退・中核の理解） › 握ることが防ぐもの](what-not-to-delegate.md#what-it-prevents)<!-- link:end --> で扱う。

見積もりの結果が悪いとき、原因がモデルでなく、検証の手段や渡す文脈にある場合もある。モデルを替える前の見直しは <!-- link:begin harness-over-model#compare-with-your-eval -->[モデルの差よりハーネスの差 › 比べるときは自分の評価で](../models/harness-over-model.md#compare-with-your-eval)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **「5 つの軸がすべて揃わないなら、任せるべきでない」**：軸は部分ごとに当てる。欠けた部分を人が受け持ち、揃った部分を任せれば足りる。検証器のように補える軸は、先に整えてから任せる。
- **「軸が揃ったから、確認はいらない」**：揃っても、検証器が正しいかは別に点検する。書き換えられないか、本番を代表するかも同じである。点検は <!-- link:begin verifier-three-conditions#why -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 三条件が要る理由](../eval/verifier-three-conditions.md#why)<!-- link:end --> にある。
- **「軸の見積もりは、点数で決まる」**：軸ごとの効き方を比べた定量の研究はない。判定は事例からの推論で、軸が欠けるかを見るために使う。点数の合計では決めない。
- **「コンテスト専用の見方だ」**：軸は大会の事例から整理したが、業務の作業にも同じ形で使える（根拠：中、事例からの推論）。
- **「AI の見積もりは、そのまま採ってよい」**：見積もりを頼んだ返答も、確かめていない判断を含む。採るかどうかは人が決める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Sakana AI Agent Wins AtCoder Heuristic Contest (First AI to Place 1st)](https://sakana.ai/ahc058/)：Sakana AI・英語・確認日 2026-11-04
- [Azure SRE エージェントは ISUCON で戦えるか？パフォーマンスチューニングに挑戦してみた](https://zenn.dev/microsoft/articles/78e01f5932c025)：Zenn（microsoft）・確認日 2026-11-04
- [CTFs in the AI Era](https://blog.includesecurity.com/2026/04/ctfs-in-the-ai-era/)：Include Security・英語・確認日 2026-11-04
- [Claude is competitive with humans in (some) cyber competitions](https://www.anthropic.com/research/cyber-competitions)：Anthropic・英語・確認日 2026-11-04
- [Battlecode 2026 Postmortem（Lorem Ipsum）](https://battlecode.org/assets/files/postmortem-2026-lorem-ipsum.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)

**次に読む**

- [コンテストの形式別の早見表（AI の効き方と人が握るところ）](../contest/format-cheatsheet.md)

**関連**

- [任せないもの（評価・採否・撤退・中核の理解）](what-not-to-delegate.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)
- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [伴走と委託](pairing-and-delegating.md)
- [コンテストの形式別の早見表（AI の効き方と人が握るところ） › 形式で効き方が違う理由（五つの軸）](../contest/format-cheatsheet.md#why-formats-differ)
- [検証環境・テスト基盤を作らせる](../recipes/build-test-harness.md)
- [モデルの差よりハーネスの差](../models/harness-over-model.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
