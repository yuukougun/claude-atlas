---
id: suspected-degradation
title: 劣化を疑ったら測って確かめる
aliases: [品質の低下, nerf, 劣化の確かめ方]
type: recipe
field: models
chapter: 替えたとき・劣化を疑うとき
order: 70
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: [体感を信じる]
summary: 劣化を疑ったとき、版と effort を記録して同じ課題を何度か流して比べ、体感でなく結果で確かめられる。製品の側の変更が原因だった例から、公式の報告と変更履歴の確かめ方も分かる。
signs:
  - {type: goal, text: 「劣化した」と感じたのが本当かを、測って確かめたい}
  - {type: goal, text: 更新の前と後で、同じ課題の結果を比べたい}
  - {type: situation, text: 「性能が落とされた」という話を見かけ、自分の環境でも起きているか確かめたい}
prerequisites: [effort-levels, felt-vs-measured]
related: [seems-less-capable, measure-changes, nondeterminism, checking-for-updates, change-timeline-2026, after-switching-models]
tracks: [effort, model-selection]
outdated_advice: []
sources: [anthropic-research-april-23-postmortem, cc-changelog, cc-docs-changelog, cc-docs-settings-reference, hc-release-notes, api-release-notes, status-claude-com]
volatility: 中
sections:
  - {title: 版と effort を記録して、同じ課題で比べる, anchor: measure}
  - {title: 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況）, anchor: official-sources}
  - {title: 製品の側だったときの手当て（更新の通り道・報告）, anchor: if-product-side}
  - {title: 製品の側の変更だった例, anchor: postmortem-example}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：版・モデル・effort を記録して同じ課題を何度か流し、劣化したかを体感でなく結果で確かめられる。
    - **いつ引くか**：「劣化した」と感じて、それが本当か測りたいとき。更新の前後の結果を比べたいときや、「性能が落とされた」という話の真偽を自分の環境で確かめたいときも引く。
    - **前提**：<!-- link:begin effort-levels -->[effort の段階と使い分け](effort-levels.md)<!-- link:end -->、<!-- link:begin felt-vs-measured -->[体感と実測](../eval/felt-vs-measured.md)<!-- link:end -->

<!-- textlint-disable -->
別名：品質の低下・nerf・劣化の確かめ方
<!-- textlint-enable -->

劣化を疑ったら測って確かめるとは、結果が以前より悪くなったと感じたときに、その感じをそのまま信じず、条件を記録して同じ課題で比べる手順である。先に自分の側の条件（版・モデル・effort）の違いを疑い、それで説明がつかないときに、製品の側の変更を公式の報告と変更履歴で確かめる。症状の側から入るときは、<!-- link:begin seems-less-capable -->[急に賢くなくなった気がする](../symptoms/seems-less-capable.md)<!-- link:end --> を先に読む。そこでの安い確かめを済ませても疑いが残るなら、このページの出番である。

## 版と effort を記録して、同じ課題で比べる {#measure}

結果が悪くなったかを確かめるには、比べる 2 組の条件を書き出し、違う項目を 1 つに絞って、同じ課題を何度か流す。体感だけを信じて結論を出すと、課題の難しさの違いや試行ごとのばらつきを、劣化と取り違える。なぜ体感がずれるかは <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end --> にある。

**先に決めておくこと**

- 課題：結果が悪いと感じた作業と、以前うまくいった作業を、入力を固定して用意する。成功の基準の決め方は <!-- link:begin measure-changes#terms -->[変更が効いたかを測る（小さな eval） › 成功の基準を先に決める（task・trial・grader・transcript・outcome）](../eval/measure-changes.md#terms)<!-- link:end --> にある。
- 採点の基準：通る・通らないで判定できる検査を使う。使えないときは、基準を先に文で書く。採点の種類は <!-- link:begin measure-changes#graders -->[変更が効いたかを測る（小さな eval） › 採点の種類（コード・モデル・人）](../eval/measure-changes.md#graders)<!-- link:end --> にある。
- 試行の数：1 回の結果で判断しない。同じ頼み方でも答えが変わる理由は <!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end --> に、試行の数と差の大きさは <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> にある。

**記録するもの**

- 日付と時刻、面
- Claude Code の版、モデル、effort の段
- 契約・アカウントの種類：同じ変更でも、戻される時期がアカウントの種類で違うことがある（例は「製品の側の変更だった例」の節）。
- CLAUDE.md・設定・スキル・プラグイン
- 新しいセッションで始めたか、会話がどれだけ長かったか：会話の量の確かめ方は <!-- link:begin seems-less-capable#diagnosis -->[急に賢くなくなった気がする › 原因を安く確かめる順](../symptoms/seems-less-capable.md#diagnosis)<!-- link:end --> にある。

現在の値の読み取り方は、面によって違う。

=== "アプリ"

    送信ボタンの横のモデルのメニューで、モデルと effort の段を読んで記録する。アプリの画面は更新で変わるので、記録した日付も書く。

=== "Claude Code"

    `claude --version` で版を、`/model` でモデルを、`/effort` で effort の段を確かめて記録する。段の変え方は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](effort-levels.md#how-to-set)<!-- link:end --> にある。

=== "API"

    リクエストに書いた `model` と effort のパラメーターを、そのままログに残す。応答の `model` も記録する。effort を省いたときは「省略」と記録する。省いたときの既定は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](effort-levels.md#defaults-by-surface)<!-- link:end --> で確かめる。

記録の雛形を次に置く。表を埋めると、2 組で違う項目が 1 つだけかを一目で確かめられる。

<!-- gen:begin snippet suspected-degradation/degradation-log -->
<!-- textlint-disable -->

??? example "雛形：版・モデル・effort を並べて残す確かめ記録"

    ```markdown
    # 劣化の確かめ記録

    ## 条件（比べる 2 組で、違う項目は 1 つだけにする）

    | 項目 | A（前・基準） | B（後・疑う側） |
    |---|---|---|
    | 日付と時刻 | | |
    | 面（アプリ・Claude Code・API） | | |
    | Claude Code の版（`claude --version`） | | |
    | モデル | | |
    | effort の段（省略したなら「省略」） | | |
    | 契約・アカウントの種類 | | |
    | CLAUDE.md・設定・スキル・プラグイン | 同じ | 同じ |
    | 課題の入力 | 同じ | 同じ |
    | 新しいセッションで始めたか | | |

    ## 結果（課題ごと、試行ごと）

    | 課題 | 試行 | A の結果 | B の結果 | 採点の基準 |
    |---|---|---|---|---|
    | | 1 | | | |
    | | 2 | | | |
    | | 3 | | | |

    ## 判定

    - 差は、条件の違う 1 項目で説明できるか：
    - 差は、試行ごとのばらつきの範囲を超えているか：
    - 差があり条件が同じなら、公式の報告・変更履歴・稼働状況で確かめた先と日付：
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet suspected-degradation/degradation-log -->

**手順**

1. 課題を固定する。確かめ：別の日に、同じ入力でもう一度流せる。
2. 条件を記録する。確かめ：記録の雛形の項目が全部埋まっている。
3. 変える項目を 1 つに絞る。更新の前後を比べるなら版だけ、effort を疑うなら段だけを変える。確かめ：2 組の記録を並べて、違うのが 1 項目だけである。
4. 新しいセッションで、各組を同じ回数だけ流す。確かめ：各回の経過を保存してある。読み方は <!-- link:begin measure-changes#read-transcripts -->[変更が効いたかを測る（小さな eval） › transcript を読む](../eval/measure-changes.md#read-transcripts)<!-- link:end --> にある。
5. 採点して比べる。確かめ：合計だけでなく課題ごとに見て、差が試行のばらつきの範囲を超えているかを判断した。見方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> にある。

更新の前の記録がないときは、前の版をそのまま再現できるとは限らない。その場合は、effort やモデルなど、今すぐ替えられる 1 項目で比べる。

!!! example "判断例：更新の後から、同じ依頼の結果を悪く感じる"
    - **状況**：Claude Code を更新した後、いつもの修正依頼で、テストを通せないまま終わる回が増えたと感じる。更新の前の記録は残していない。
    - **迷う候補**：更新の前の版を探して入れ直して比べる。または、今の版のまま effort の段を 1 つずつ変えて比べる。
    - **選んだもの**：今の版のまま、effort の段を 1 つずつ変えて、同じ依頼を各段で何度か流す。
    - **理由**：更新の前の版を同じ条件で再現できるとは限らず、記録もないので、比べる相手にならない。effort は既定が変わると結果に出やすく、今すぐ替えて測れる。段で差が出れば既定の変更を疑う手がかりになり、出なければ、体感のずれか別の原因を疑って次の確かめへ進む。

**結果の読み方**

- 差がない：劣化は確認できなかった。体感した場面と課題が違うなら、その場面の課題を足してやり直す。体感と実測がずれる仕組みは <!-- link:begin felt-vs-measured#evidence -->[体感と実測 › 何が起きるか（研究と根拠の強さ）](../eval/felt-vs-measured.md#evidence)<!-- link:end --> にある。
- 差があり、条件も違う：条件の違いが原因の候補である。モデルや既定を替えた後の見直しは <!-- link:begin after-switching-models#checklist -->[新しいモデルに替えたら見直すこと › 見直す順](after-switching-models.md#checklist)<!-- link:end --> にある。
- 差があり、条件が同じ：製品の側の変更を疑い、次の節で確かめる。

## 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況） {#official-sources}

測って差が出て、自分の条件では説明できないときは、製品の側の変更を、公式の報告・変更履歴・稼働状況で確かめる。確かめる先ごとに、分かることと分からないことが違う。

| 確かめる先 | 分かること | 分からないこと |
| --- | --- | --- |
| 公式の報告（Anthropic の研究ブログなど） | 品質の報告への原因の説明と、直した日 | 報告がないことは、変更がないことの証明にならない |
| Claude Code の変更履歴（CHANGELOG と docs の changelog） | 版ごとの変更。既定の変更や戻しの行 | 項目のない版がある。全部の変更が載るとは限らない |
| アプリの Help Center のリリースノート、API の Platform のリリースノート | アプリと API の変更 | 面ごとに別の場所にある。Claude Code の変更は別に引く |
| 稼働状況のページ（status.claude.com） | 障害の有無と経過。メールや RSS で購読できる | 障害として扱われない質の変化は、ここに出るとは限らない |

報道や解説の記事は、公式の報告や変更履歴で確かめてから使う。掲示板の書き込みは、同じ症状の人がいるかの手がかりにとどめる（根拠：弱）。変更履歴の引き方と、自分の版の確かめ方は <!-- link:begin checking-for-updates -->最新を自分で確かめる方法（準備中）<!-- link:end --> に、日付順の一覧は <!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> にある。

## 製品の側だったときの手当て（更新の通り道・報告） {#if-product-side}

測って差があり、条件が同じで、製品の側の変更が疑わしいときに、手元でできる手当ては 3 つある。

1. effort の段を明示して固定する。既定が変わったときの影響を、自分の側で止められる。変え方は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](effort-levels.md#how-to-set)<!-- link:end --> にある。確かめ：同じ課題で測り直して、差が縮んだ。
2. 更新の通り道を見直す。更新の通り道を stable にすると、大きな退行のある版を飛ばして、少し遅れた版を受け取る。代わりに、修正を含む版を受け取るのも遅れる。確かめ：`claude --version` で受け取った版を記録した。設定の書き方は、3 つの手当ての後に置く。
3. 報告する。`/feedback` で報告するときは、条件の記録と、再現できる例を添える。会話の内容が送られうるので、機密のある作業では、送る前に何が送られるかを公式の文書で確かめる。確かめ：修正が出た後の版で、同じ課題を測り直した。

<!-- gen:begin snippet suspected-degradation/update-channel -->
<!-- textlint-disable -->

??? example "雛形：更新の通り道を stable にする設定"

    ```json
    {
      "autoUpdatesChannel": "stable"
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet suspected-degradation/update-channel -->

どの確かめでも説明がつかないときは、文脈の量やモデルを疑う確かめに戻る。順番は <!-- link:begin seems-less-capable#diagnosis -->[急に賢くなくなった気がする › 原因を安く確かめる順](../symptoms/seems-less-capable.md#diagnosis)<!-- link:end --> にある。モデルの退役や既定の変化に気づく方法は <!-- link:begin after-switching-models#retirements-and-default-changes -->[新しいモデルに替えたら見直すこと › 退役と既定の変化に気づく](after-switching-models.md#retirements-and-default-changes)<!-- link:end --> にある。

## 製品の側の変更だった例 {#postmortem-example}

2026 年 3〜4 月に Claude Code の品質への不満が続いたとき、Anthropic は 2026 年 4 月 23 日に事後報告（ポストモーテム）を出した。報告は、原因を製品の側の 3 つの変更と説明した。影響を受けたのは Claude Code や Agent SDK などで、API は含まれないと書かれている。

| 変更 | 期間 | 影響を受けたモデル | 直し方 |
| --- | --- | --- | --- |
| Claude Code の既定の effort を high から medium に下げた | 3 月 4 日から 4 月 7 日 | Sonnet 4.6、Opus 4.6 | 4 月 7 日に戻した（Opus 4.7 は xhigh、ほかは high） |
| 古い思考の履歴を、1 回ではなく毎ターン消すバグ | 3 月 26 日から 4 月 10 日 | Sonnet 4.6、Opus 4.6 | 4 月 10 日に直した |
| 冗長さを抑えるシステムプロンプトの 1 行 | 4 月 16 日から 4 月 20 日 | Sonnet 4.6、Opus 4.6、Opus 4.7 | 4 月 20 日に戻した |

この例から、確かめ方について 4 つのことが分かる。

- 疑う先は、モデルそのものとは限らない。既定の設定、会話の扱い、システムプロンプトのような製品の側の変更が、結果を変えうる。
- 3 つの期間が重なっているので、症状は 1 つの原因に見えにくい。日付で区切って別々に確かめる。
- 戻し方は、アカウントの種類で時期が違った。変更履歴では、API キー・クラウド経由・Team・Enterprise の戻しが先で、Pro と Max の Opus 4.6・Sonnet 4.6 の戻しは後だった。だから、契約の種類も記録する。
- 報道が挙げる教訓も、版と effort をまず確かめること、モデルを替えたら effort を設定し直すことだった（根拠：弱。二次の報道）。モデルを替えた後の見直しは <!-- link:begin after-switching-models -->[新しいモデルに替えたら見直すこと](after-switching-models.md)<!-- link:end --> にある。

nerf という言葉で語られる劣化の一部は、この例のように、製品の側の設定や指示の変更で説明された。ただし、毎回そうとは限らない。別の原因は、この手順で切り分ける。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [An update on recent Claude Code quality reports](https://www.anthropic.com/research/april-23-postmortem)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)：Anthropic・英語・確認日 2026-11-04
- [Claude Status](https://status.claude.com)：Anthropic・英語・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [effort の段階と使い分け](effort-levels.md)
- [体感と実測](../eval/felt-vs-measured.md)

**関連**

- [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- 最新を自分で確かめる方法（準備中）
- 2026 年の主な変更の年表（準備中）
- [新しいモデルに替えたら見直すこと](after-switching-models.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
