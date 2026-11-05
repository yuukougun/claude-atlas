---
id: data-analysis
title: データを分析する
aliases: [データ分析, SQL を書かせる, ログや CSV の集計, 分析の結果を確かめる]
type: recipe
field: recipes
chapter: データと分析
order: 140
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, 同意を根拠にする]
scenes: [データ分析, 開発]
summary: データの集計や分析を、あとで再実行できるクエリやスクリプトの形で Claude に任せる。数字は生データで裏を取り、観察した事実と原因の解釈を分けて出させる。
signs:
  - {type: goal, text: ログや CSV を集計して傾向をつかみたい}
  - {type: symptom, text: 分析の結論はもっともらしいが、数字の出どころが分からない}
  - {type: symptom, text: 自分の仮説に合う分析ばかり返ってくる}
prerequisites: [evidence-not-reports, files-and-code-execution, ask-without-sycophancy]
related: [build-observation-tools, audit-ml-pipelines, entrusted-data, where-your-data-goes, character-encodings, measure-changes#by-stratum, check-the-metric, lockbox-and-holdout, suspect-too-good-results, agreement-is-not-evidence, mcp-or-cli, office-paperwork]
tracks: [code-execution]
sources: []
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 再実行できる形で集計させる, anchor: reproducible-queries}
  - {title: 生データで裏を取る, anchor: check-raw-data}
  - {title: 観察と解釈を分ける, anchor: observation-vs-interpretation}
  - {title: 全体の確かめ方, anchor: how-to-check}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: reviewed
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：集計を再実行できるクエリやスクリプトの形で任せ、数字を生データで裏取りし、観察と解釈を分けて受け取れる。
    - **いつ引くか**：ログや CSV を集計して傾向をつかみたいとき。結論はもっともらしいが数字の出どころが分からないとき。自分の仮説に合う分析ばかり返ってくるとき。
    - **前提**：<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](../verify/evidence-not-reports.md)<!-- link:end -->・<!-- link:begin files-and-code-execution -->[ファイル作成とコード実行](../app/files-and-code-execution.md)<!-- link:end -->・<!-- link:begin ask-without-sycophancy -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)<!-- link:end -->

<!-- textlint-disable -->
別名：データ分析・SQL を書かせる・ログや CSV の集計・分析の結果を確かめる
<!-- textlint-enable -->

データを分析する用途は、集計の手を動かす部分を Claude に任せ、結果を生データで確かめて受け取る進め方である。任せるのは集計の処理までだ。数字を信じてよいかの判断と、原因の解釈は人が握る。

## 先に整える守り {#guards}

データ分析で任せる幅を広げる前に、守りを 4 つ先に整える。数字は一見もっともらしく読めるので、後から気づくのが難しい。

1. **渡してよいデータかを決める**：顧客のデータや規約付きのデータは、契約で扱いが決まった面だけで使う。判断は <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end --> に任せる。送ったデータが学習に使われる条件と残る期間は <!-- link:begin where-your-data-goes -->[送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)<!-- link:end --> で確かめる。
2. **ファイルの文字コードをそろえる**：Shift_JIS の CSV は文字化けや集計の空欄の元になる。渡す前の確かめ方は <!-- link:begin character-encodings#check -->[文字コード（Shift\_JIS の CSV など） › 渡す前に文字コードを確かめる](../japanese/character-encodings.md#check)<!-- link:end --> にある。
3. **証拠の形を先に決める**：集計結果は、実行したコマンドと生の出力と分母で受け取る。「集計しました」という報告だけでは受け取らない。形は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end --> にある。
4. **自分の仮説を伏せる**：「原因は新機能だと思う」と書いて頼むと、その仮説に合う分析が返りやすい。伏せ方は <!-- link:begin ask-without-sycophancy#hide-preferences -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる](../judgment/ask-without-sycophancy.md#hide-preferences)<!-- link:end --> にある。

## 再実行できる形で集計させる {#reproducible-queries}

集計は、答えの数字ではなく、数字を作るクエリやスクリプトとして書かせる。会話の中で数字だけが返ってくると、どの行をどう数えたかが後から追えず、「数字の出どころが分からない」状態になる。スクリプトとして残せば、同じ入力から同じ数字を再実行で出せ、入力が更新されたときも同じ手順で再計算できる。

頼むときに決めておくのは次の 4 点である。

- 入力：読むファイルやテーブル
- 定義：何を数え、どの行を除くか
- 出力先：結果を書き出す場所
- 実行方法：スクリプトを動かすコマンド

依頼の形は次のとおり。偽のデータで先に試すと、定義の書き方を安全に確かめられる。

<!-- gen:begin snippet data-analysis/aggregate-request -->
<!-- textlint-disable -->

??? example "雛形：再実行できるスクリプトで集計させ、分母と元の行を添えさせる依頼の雛形"

    ```text
    <入力ファイル。例：logs/access.csv> を集計して、傾向をつかみたい。
    - 答えの数字だけを返さず、再実行できるスクリプト（<例：analysis/aggregate.py>）として書く。結果の出力先は <例：analysis/out/summary.csv>
    - スクリプトの冒頭に、何を数えるか、どの行を除くか（除く理由つき）を書く
    - 書いたら実行して、実行したコマンドと出力をそのまま見せる。入力の総行数、除いた行数、集計に使った行数も出す
    - 結果の表の上位 3 行と下位 3 行について、元データの該当する行を抜き出して並べる
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet data-analysis/aggregate-request -->

面によって、スクリプトを動かす場所が違う。

=== "アプリ"

    アプリでは、隔離された環境でコードを実行して集計できる。使いどころと頼み方は <!-- link:begin files-and-code-execution#usage -->[ファイル作成とコード実行 › 頼み方](../app/files-and-code-execution.md#usage)<!-- link:end --> にある。作ったスクリプトと結果のファイルは手元へ受け取って残す（<!-- link:begin files-and-code-execution#outputs -->[ファイル作成とコード実行 › 作ったファイルの受け取り方](../app/files-and-code-execution.md#outputs)<!-- link:end -->）。実行環境のネットワークの設定には危険があるので、<!-- link:begin files-and-code-execution#network -->[ファイル作成とコード実行 › 実行環境とネットワークの設定](../app/files-and-code-execution.md#network)<!-- link:end --> を先に読む。

=== "Claude Code"

    Claude Code では、手元のリポジトリの中にスクリプトを置いて、コマンドで実行させる。スクリプトはリポジトリに入れておけば、あとで誰でも同じコマンドで再実行できる。実行した出力は、要約ではなくそのまま見せるよう頼む。

データベースなど外の元データにつなぐ手段（MCP か、CLI か）の選び方は <!-- link:begin mcp-or-cli -->[MCP か CLI か](../extend/mcp-or-cli.md)<!-- link:end --> にある。毎週同じ集計を回すような繰り返しの作業は <!-- link:begin office-paperwork -->[事務作業の半自動化（経費・報告）](office-paperwork.md)<!-- link:end --> の流れに乗せられる。

## 生データで裏を取る {#check-raw-data}

集計の数字は、Claude の説明ではなく生データに照らして確かめる。説明と事実が食い違えば、実行して見た事実を正とする（<!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end -->）。次の順に、段ごとに何で終わったかを見る。

1. **分母を合わせる**：入力の総行数、除いた行数、集計に使った行数を出させる。総行数が、除いた行数と使った行数の合計と合えば、この段は終わりである。合わなければ、読み込みで落ちた行がある。
2. **数行を手で追う**：結果の表の上位と下位から数行を選び、元データの該当行を抜き出して、手計算が合うかを見る。合えば終わりである。手計算の習慣は <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](build-observation-tools.md)<!-- link:end --> でも小さな例で扱う。
3. **欠損と型を見る**：空欄の数、値の型、文字化けを確かめる。文字コードに由来する空欄は、集計の数字を黙って小さくする（<!-- link:begin character-encodings -->[文字コード（Shift\_JIS の CSV など）](../japanese/character-encodings.md)<!-- link:end -->）。欠損の数が説明できれば終わりである。
4. **層に分けて見る**：全体の合計だけで判断せず、期間や種類などの層ごと、いちばん悪い層も見る。見方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> にある。合計と層ごとの数字が矛盾しなければ終わりである。
5. **指標が目的に合うかを確かめる**：数えているものが、本当に知りたいことと合っているかを見る。ずれの見つけ方は <!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](../eval/check-the-metric.md#mismatch)<!-- link:end --> にある。

結果が良すぎるときは、まず集計の側を疑う。急に良くなった数字や満点に近い数字の疑い方は <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end --> にある。機械学習のスコアなら、検証用のデータの漏れも疑う。点検の頼み方は <!-- link:begin audit-ml-pipelines -->機械学習のパイプラインを点検させる（準備中）<!-- link:end --> にある。

「預けすぎる」落とし穴は、この段で起きやすい。裏取りのコマンドを Claude に走らせるのはよいが、「合っています」という報告を読んで終えると、確かめたことにならない。出力そのものを自分の目で読む。

## 観察と解釈を分ける {#observation-vs-interpretation}

観察は、数字から言える事実である。解釈は、その事実を生んだ原因についての仮説である。両者を混ぜて返させると、仮説が事実のように読めてしまう。しかも自分の仮説を伝えていると、それに合う解釈が返りやすい（<!-- link:begin agreement-is-not-evidence#agreement-depends-on-asking -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 賛成は聞き方と押し方で増える](../judgment/agreement-is-not-evidence.md#agreement-depends-on-asking)<!-- link:end -->）。

そこで依頼の中で、観察と提案の出し方を決めておく。改善策は書かせず、観察された事実と追加で取る集計の案だけを出させる。原因の仮説は互いに両立しない形で最大 5 つにし、各仮説に「正しければ観測されるはずのこと」「誤りなら観測されるはずのこと」「最小の確認実験」を付けさせる。どれが有力かの判断はさせない。

<!-- gen:begin snippet data-analysis/observe-and-hypothesize -->
<!-- textlint-disable -->

??? example "雛形：観察と解釈を分け、仮説を反証できる形で出させる依頼の雛形"

    ```text
    次の集計結果について、観察と提案を分けて出してほしい。
    - 対象は <集計結果の場所。例：analysis/out/summary.csv> と、それを作ったスクリプト <例：analysis/aggregate.py>
    - 観察：数字から言える事実だけを書く。値には、元データの行か集計コマンドの出力を添える
    - 改善策は書かない。追加で取るとよい集計の案だけを挙げる
    - 原因の仮説は、互いに両立しない形で最大 5 つ。各仮説に、正しければ観測されるはずのこと、誤りなら観測されるはずのこと、最小の確認実験を書く
    - どの仮説が有力かの判断はしない。判断は私が決める
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet data-analysis/observe-and-hypothesize -->

この依頼で変わるのは、返答が反証できる形になる点である。仮説ごとの確認実験を実際に走らせ、その結果を新しい観察として戻せば、仮説を絞れる。絞る判断は人が握る。賛成の多さや、複数の AI の一致は根拠にならない（<!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end -->）。

!!! example "判断例：遅くなった原因の仮説を持っているとき"
    - **状況**：応答時間のログを集計したところ、先週から遅くなっている。自分は新機能が原因だと考えている。
    - **迷う候補**：新機能が原因だという仮説を伝えて、裏づけを探させる。仮説を伏せて、観察と仮説の一覧だけを出させる。
    - **選んだもの**：仮説を伏せて、観察と仮説の一覧を出させる。
    - **理由**：仮説を伝えると、それに合う切り口の分析ばかり返りやすい。伏せれば、新機能以外の仮説（たとえば特定の時間帯の負荷）も、確認実験つきで並ぶ。自分の仮説は、並んだ中の 1 つとして後から検証すればよい。

切り口を何度も変えて見つけた傾向は、見つけるのに使っていないデータで確かめるまで、偶然の可能性が残る。検証用のデータを分けて持つ運用は <!-- link:begin lockbox-and-holdout -->[ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)<!-- link:end --> にある。

## 全体の確かめ方 {#how-to-check}

結論を受け取る前に、次の 5 つを確かめる。

- スクリプトを新しいセッションで動かして、同じ入力から同じ結果ができる。
- 総行数が、除いた行数と使った行数の合計と合う。
- 結果の数行が、元データの手計算と合う。
- 観察の節に、原因の話と改善策が混ざっていない。
- 結論の数字を 1 つ選んで、スクリプトの行と生データの行まで辿れる。

どれか 1 つでも辿れなければ、その数字は結論に使わない。

## 失敗したとき {#when-it-fails}

起きたことから、見る先を選ぶ。

| 起きたこと | 見る先 |
| --- | --- |
| 数字の出どころが分からない | 上の「再実行できる形で集計させる」で、スクリプトとして書き直させる |
| 再実行すると数字が変わる | 入力のファイルが更新されていないか、定義の除外条件が曖昧でないかを確かめる |
| 文字化けや空欄が多い | <!-- link:begin character-encodings -->[文字コード（Shift\_JIS の CSV など）](../japanese/character-encodings.md)<!-- link:end --> |
| 完了と報告されたが数が合わない | <!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](../verify/evidence-not-reports.md)<!-- link:end --> |
| 自分の仮説に合う分析ばかり返る | <!-- link:begin ask-without-sycophancy -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)<!-- link:end --> |
| 結果が良すぎる | <!-- link:begin suspect-too-good-results -->[良すぎる結果を疑う](../verify/suspect-too-good-results.md)<!-- link:end --> |
| 預かったデータを渡してよいか迷う | <!-- link:begin entrusted-data -->[預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)<!-- link:end --> |

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [ファイル作成とコード実行](../app/files-and-code-execution.md)
- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)

**次に読む**

- 機械学習のパイプラインを点検させる（準備中）

**関連**

- [観察の道具を作らせる（可視化・集計・ログ）](build-observation-tools.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [文字コード（Shift\_JIS の CSV など）](../japanese/character-encodings.md)
- [変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)
- [評価指標そのものを確かめる](../eval/check-the-metric.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [MCP か CLI か](../extend/mcp-or-cli.md)
- [事務作業の半自動化（経費・報告）](office-paperwork.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
