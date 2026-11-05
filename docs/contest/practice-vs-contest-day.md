---
id: practice-vs-contest-day
title: 練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）
nav_title: 練習と本番の使い分け
aliases: [本番で AI を使えない大会の準備, Human Only 部門に向けた練習]
type: concept
field: contest
chapter: 規則と練習
order: 40
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [握る, 確かめる]
prevents: []
pitfalls: [預けすぎる, 体感を信じる]
scenes: [コンテスト, 学習]
summary: 本番で AI を使えない大会に向けて、練習では AI を解説役・採点役・テストの作り手として使い、本番の条件で自力を確かめる使い分けが分かる。
signs:
  - {type: situation, text: AI を禁じる大会に向けて練習している}
  - {type: symptom, text: AI と一緒だと解けるのに、本番では手が止まる}
  - {type: situation, text: AI を使ってよい部門と使えない部門の、どちらに出るか迷っている}
prerequisites: [competition-rules, learning-with-ai]
related: [how-much-understanding-to-keep, felt-vs-measured, when-ai-is-unavailable, competition-day-operations, format-cheatsheet#algorithm, think-before-asking, read-specs-yourself, own-generated-code, differential-testing]
tracks: []
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 本番で使えない線引き, anchor: rules-change-the-line}
  - {title: 練習で AI に頼むこと, anchor: what-to-ask-in-practice}
  - {title: 本番の条件で自力を確かめる, anchor: test-under-contest-conditions}
  - {title: 部門のある大会で、練習の場を選ぶ, anchor: choosing-divisions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：本番で AI を使えない大会に向けては、練習で AI を解説役・採点役・テストの作り手にし、本番の条件で自力を確かめる。
    - **いつ引くか**：AI を禁じる大会に向けて練習している。AI と一緒だと解けるのに、本番では手が止まる。AI を使ってよい部門と使えない部門のどちらに出るか迷っている。
    - **前提**：<!-- link:begin competition-rules -->[大会の規則の早見（禁止・部門分け・許可と開示）](competition-rules.md)<!-- link:end -->、<!-- link:begin learning-with-ai -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)<!-- link:end -->

<!-- textlint-disable -->
別名：本番で AI を使えない大会の準備・Human Only 部門に向けた練習
<!-- textlint-enable -->

練習と本番の使い分けは、AI が使える練習の場と、使えない本番の場とで、AI に頼む内容を分けることである。AI に任せる前提で作った手順は、本番で使えない大会がある。このページは、その食い違いを練習の間に埋める頼み方と確かめ方を扱う。競技の練習法そのもの（解説の読み方、復習の仕方）は、姉妹の教材 kyopro-atlas の practice-method を見る。

## 本番で使えない線引き {#rules-change-the-line}

AI を使う開発の手順の多くは、AI に任せることを前提に線を引く。たとえば CLAUDE.md の冒頭に「丸投げ OK／要確認／禁止」の 3 区分を書き、テストで守られた実装や集計は任せ、戦略や評価方法の変更は確認する、という使い方である（根拠：弱。実務家の紹介）。この線引きは、AI を使える場では役に立つ。しかし AI を禁じる大会の本番では、線を引く相手の AI がいない。

本番で使えないのは、線引きだけではない。次の 3 つも、練習で慣れた分だけ本番で欠ける。

- 方針を思い付く前に AI に聞く癖
- AI が出した解法を読んで、自分の理解に直す流れ
- AI に作らせたテストや補助の道具

大会ごとに、AI の扱いは禁止・部門分け・許可と開示のどれかに分かれる。どの大会がどの類型か、版はいつのものかは、<!-- link:begin competition-rules#rules-by-type -->[大会の規則の早見（禁止・部門分け・許可と開示） › 類型ごとの大会（確認日付き）](competition-rules.md#rules-by-type)<!-- link:end --> で引く。版を確かめていない大会は、出る前に一次資料で今の規則を読む（<!-- link:begin competition-rules#unverified-versions -->[大会の規則の早見（禁止・部門分け・許可と開示） › 大会ごとの規則のページと、出る前に確かめること](competition-rules.md#unverified-versions)<!-- link:end -->）。練習の場と本番の場で、規則の扱いが違うことがある点にも注意する。練習の場で AI を使ってよいかは、その場の規則を読んで決め、本番の規則と同じだと決め付けない。

このページが名指す落とし穴は 2 つある。1 つは、練習の間に AI へ預けすぎて、本番で必要な力が育たないこと。もう 1 つは、AI と一緒に解けた体感を、自力で解ける力だと信じてしまうことである。前者は <!-- link:begin how-much-understanding-to-keep#supervision-paradox -->[どこまで理解を手放してよいか（中核と周辺） › 確かめる力が衰える（監督のパラドックス）](../judgment/how-much-understanding-to-keep.md#supervision-paradox)<!-- link:end --> に、後者は <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end --> に仕組みがある。AI と一緒だと解けるのに本番で手が止まるのは、この 2 つが重なった形である。

## 練習で AI に頼むこと {#what-to-ask-in-practice}

AI を禁じる大会を目指すなら、練習では AI を解説役・採点役・テストの作り手として使い、本番は AI なしで解けるようにする（根拠：弱。実務家の紹介と立場の表明）。人が握るもの（原理でいう「握る」）は、方針を立てることと、解法を自分の言葉で言えることである。AI には、その確かめを手伝わせる。

頼む順番は、先に自分で考え、その後で AI に頼む形にする。理由は、自分の案がないまま AI の案を読むと、評価の物差しが AI の案に引っ張られるからである。順序の考え方は <!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end --> にある。

| 役 | AI に頼むこと | 頼まないこと | 詳しい手順 |
| --- | --- | --- | --- |
| 解説役 | 詰まったときのヒントを 1 段ずつ。解説を読んだ後の見落とし | 解法やコードをそのまま出すこと | <!-- link:begin learning-with-ai#hints-not-answers -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 答えではなくヒントを返させる](../judgment/learning-with-ai.md#hints-not-answers)<!-- link:end --> |
| 採点役 | 自分の解法の誤りがありそうな点の指摘。問題文の読み違いの指摘 | 直したコードを出すこと | <!-- link:begin read-specs-yourself#misreading-detector -->[仕様を自分で読み、AI に誤読を指摘させる › AI に誤読を指摘させる](../recipes/read-specs-yourself.md#misreading-detector)<!-- link:end --> |
| テストの作り手 | 愚直解と入力の端のケース、突き合わせの道具 | 正解の側を本解に合わせて直すこと | <!-- link:begin differential-testing#steps -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 手順](../eval/differential-testing.md#steps)<!-- link:end --> |

どの役でも、AI が出した説明は、自分の言葉で言い直せるまで採らない。言い直せない所が、読み直す箇所になる（<!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end -->）。

次の雛形は、練習の依頼にまとめて入れる例である。解法を書く前の段階で、AI が答えを出さないようにする。指示はお願いなので、効かないことがある。効かなかったときは、依頼を出し直すのでなく、自分の案を先に書いてから頼む順番を守る。

<!-- gen:begin snippet practice-vs-contest-day/practice-coach -->
<!-- textlint-disable -->

??? example "雛形：練習で AI を解説役・採点役にする依頼"

    ```markdown
    あなたは、AI を使えない大会に向けて練習している私の解説役・採点役です。
    次のルールで動いてください。

    - 私が「自分の解法」を書くまで、解法・方針・コードを答えとして出さない
    - 詰まったときは、私が「ヒントを 1 段」と頼んだ分だけ、問いか観察のかたちで返す
    - 私の解法を見せたら、まず誤りがありそうな点を指摘する。直したコードは出さない
    - 解説を読ませるときは、要約でなく「この解説で私が見落としていそうな前提」を挙げる
    - 私が提出しようとしている解法で足りないテストがあれば、入力の端（最小・最大・重複・空）を挙げる

    今回の問題：（問題文または URL を貼る）
    私の持ち時間：（例：本番と同じ長さ）
    いまの状態：（例：方針は立てた／まだ何も思い付かない）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet practice-vs-contest-day/practice-coach -->

!!! example "判断例：解説を読む前に AI に聞くか"
    - **状況**：ある問題で 30 分考えても方針が立たない。公式の解説はまだ読んでいない。
    - **迷う候補**：AI に「最初の観察だけ」を頼む。いったん別の問題に移り、後で戻る。
    - **選んだもの**：別の問題に移り、後で同じ問題に戻ってもなお詰まれば、AI にヒントを 1 段だけ頼む。
    - **理由**：本番では、詰まった問題から離れて別の問題を進める場面が来る。離れる判断も、練習する対象に入る。すぐ AI に観察を頼む選び方も筋は通るので、離れる練習が足りない人ほど、先に離れるほうを選ぶ。

## 本番の条件で自力を確かめる {#test-under-contest-conditions}

本番の条件で自力を確かめるとは（原理でいう「確かめる」）、AI を使わず、本番と同じ長さと形式で解き、記録を残すことである。AI を使った練習の手応えは、体感としてずれやすい（<!-- link:begin felt-vs-measured#evidence -->[体感と実測 › 何が起きるか（研究と根拠の強さ）](../eval/felt-vs-measured.md#evidence)<!-- link:end -->）。同じ物差しで取った記録で判断する。

確かめ方の例は次のとおりである（推論・実践例なし。この辞典の提案）。

1. 本番の形式と制限時間を、<!-- link:begin format-cheatsheet#algorithm -->[コンテストの形式別の早見表（AI の効き方と人が握るところ） › 短時間のアルゴリズム](format-cheatsheet.md#algorithm)<!-- link:end --> などで確かめる。
2. 規則が許す道具の範囲を、<!-- link:begin competition-rules -->[大会の規則の早見（禁止・部門分け・許可と開示）](competition-rules.md)<!-- link:end --> と一次資料で確かめる。そこで許される道具だけで、その時間を解く。
3. 解けた問題の数、各問題にかかった時間、詰まった所を記録する。何を記録するかは <!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end --> にある。
4. 同じ条件の模擬を、AI を使った練習の合間に何度か挟み、記録を並べる。

AI を使わない時間を決めて残すことは、確かめる力の衰えへの備えでもある（<!-- link:begin how-much-understanding-to-keep#ai-free-time -->[どこまで理解を手放してよいか（中核と周辺） › AI を使わない時間を残す](../judgment/how-much-understanding-to-keep.md#ai-free-time)<!-- link:end -->）。頻度や長さは、自分の記録を見て決める。

本番では、AI が使えない前提で運ぶ。AI なしでも最低限を進められる状態は、<!-- link:begin when-ai-is-unavailable#minimum-without-ai -->[AI が使えないときの備え（障害・上限） › AI なしで最低限を進められる状態](../cost/when-ai-is-unavailable.md#minimum-without-ai)<!-- link:end --> に、本番当日の備えは <!-- link:begin competition-day-operations#fallback -->[本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › AI が止まっても続けられる備え](competition-day-operations.md#fallback)<!-- link:end --> にある。AI を禁じる大会では、この備えが前提になる。

模擬で AI を使わずに解けた問題と、AI と一緒にだけ解けた問題を、分けて記録する。後者が多い間は、本番で手が止まりやすい、と読む。これは自分の記録に基づく読み方で、数値の目安は置かない。

## 部門のある大会で、練習の場を選ぶ {#choosing-divisions}

部門のある大会は、AI を使えない部門と使える部門で、別々の練習の場として使える（根拠：弱。紹介された使い方）。AI を使えない部門は自力の練習の場、AI を使える部門は、仕様を決めて AI に実装を任せる練習の場になる。部門の許可の範囲、解説を出す義務の有無は、大会ごと・回ごとに違いうる。条文は要約せず、出る前に一次資料で読む（<!-- link:begin competition-rules#unverified-versions -->[大会の規則の早見（禁止・部門分け・許可と開示） › 大会ごとの規則のページと、出る前に確かめること](competition-rules.md#unverified-versions)<!-- link:end -->）。

どちらの部門に出るかは、目的で決める。

!!! example "判断例：どちらの部門に出るか"
    - **状況**：AI を使えない部門と使える部門のある大会に出る。AI を禁じる別の大会に、数か月後に出る予定もある。
    - **迷う候補**：AI を使えない部門に出て、自力の力を確かめる。AI を使える部門に出て、AI を使った進め方を試す。
    - **選んだもの**：AI を禁じる大会までの期間が短いので、AI を使えない部門に出る。AI を使う練習は、別の場で時間を区切ってする。
    - **理由**：目標が AI を禁じる大会なら、本番に近い条件の記録が一番の根拠になる。逆に、目標が AI との進め方を磨くことなら、AI を使える部門が合う。どちらも筋は通る。

どちらを選んでも、AI を使える側では、任せる範囲と確かめる所を先に決める。評価の物差しと採否は人が握る。任せる幅を広げる側ほど、確かめを先に置く（<!-- link:begin competition-rules#hold-the-boundary -->[大会の規則の早見（禁止・部門分け・許可と開示） › 規則の境界を人が握る](competition-rules.md#hold-the-boundary)<!-- link:end -->）。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [大会の規則の早見（禁止・部門分け・許可と開示）](competition-rules.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)

**関連**

- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [AI が使えないときの備え（障害・上限）](../cost/when-ai-is-unavailable.md)
- [本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）](competition-day-operations.md)
- [コンテストの形式別の早見表（AI の効き方と人が握るところ） › 短時間のアルゴリズム](format-cheatsheet.md#algorithm)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)
- [仕様を自分で読み、AI に誤読を指摘させる](../recipes/read-specs-yourself.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [答えの分かる遅い解と比べる（差分テスト・オラクル）](../eval/differential-testing.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
