---
id: build-observation-tools
title: 観察の道具を作らせる（可視化・集計・ログ）
nav_title: 観察の道具を作らせる
aliases: [ビジュアライザを作らせる, ダッシュボードを作らせる, 集計スクリプト, デバッグ用の表示]
type: recipe
field: recipes
chapter: 確かめる道具を作らせる
order: 130
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [握る, 見せる]
prevents: [見えていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析, コンテスト]
summary: 結論を出させる代わりに、可視化・集計・ログなど観察のための道具を作らせ、浮いた時間を自分の観察に回す。道具の出す値は、小さな例で手計算と合うかを先に確かめる。
signs:
  - {type: goal, text: 結果やログを見やすくする道具を手早く作りたい}
  - {type: goal, text: 原因を AI に推測させるより、自分で見て考えたい}
prerequisites: [think-before-asking]
related: [data-analysis, fix-a-bug, performance-tuning, build-test-harness, artifacts-as-apps, test-the-verifier, over-reliance, how-much-understanding-to-keep]
tracks: [artifacts]
sources: []
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards-first}
  - {title: 何を作らせるか, anchor: what-to-build}
  - {title: 進める順番, anchor: flow}
  - {title: 道具の値を手計算で確かめる, anchor: hand-check}
  - {title: 全体の確かめ方, anchor: how-to-check}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：結論の代わりに可視化・集計・ログの道具を作らせ、浮いた時間を自分の観察に回せる。道具の値は先に手計算で確かめる。
    - **いつ引くか**：結果やログを見やすくする道具を手早く作りたいとき。原因を AI に推測させるより、自分で見て考えたいとき。
    - **前提**：<!-- link:begin think-before-asking -->[頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ビジュアライザを作らせる・ダッシュボードを作らせる・集計スクリプト・デバッグ用の表示
<!-- textlint-enable -->

観察の道具を作らせる用途は、原因や改善案の判断を Claude に頼まず、人が見て考えるための表示・集計・ログのスクリプトだけを任せる進め方である。任せるのは道具を作る手間までだ。道具が見せたものを読んで、何が起きているかを考えるのは人が握る。

## 先に整える守り {#guards-first}

観察の道具を任せる前に、守りを 4 つ先に整える。道具は見た目が整っているぶん、出す値が間違っていても気づきにくいからだ。

1. **結論を頼まない線を引く**：作らせるのは道具までで、原因の推測や改善案は頼まない。先に自分の案と疑問を書き、AI には問い・反論・観察の道具を頼む順序は <!-- link:begin think-before-asking#questions-rebuttals-tools -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › AI に頼むもの：問い・反論・観察の道具](../judgment/think-before-asking.md#questions-rebuttals-tools)<!-- link:end --> にある。
2. **道具の値は確かめてから使う**：道具が出す数や図は、手で計算できる小さな例と合うかを先に確かめる。確かめ方の考え方は <!-- link:begin test-the-verifier#hand-calculated -->[検証器そのものを確かめる（red/green・手で計算したケース） › 手で計算したケース](../eval/test-the-verifier.md#hand-calculated)<!-- link:end --> と同じ形である。
3. **判断を手元に残す**：道具の表示を読むことと、次の一手を選ぶことは、人が決める。手元に残す判断の線引きは <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end --> にある。
4. **理解を手放す範囲を決める**：道具のコードを中身まで読むのは、結果の読み方を左右する計算の部分だけでよい。表示の整形などの周辺は任せきりにできる。線引きは <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](../judgment/how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end --> にある。

## 何を作らせるか {#what-to-build}

作らせるのは、人が観察するときに繰り返す手作業を肩代わりする道具である。結論を出す道具は作らせない。見えていなかったものを見えるようにする道具だけにする。

- **可視化**：解や状態を絵にするもの。要素ごとのスコアへの寄与を表示するビジュアライザや、1 手ずつ進められる再生が例になる。
- **集計**：ケース別・条件別に結果を数えるもの。データの集計を再実行できる形にする話は <!-- link:begin data-analysis#reproducible-queries -->[データを分析する › 再実行できる形で集計させる](data-analysis.md#reproducible-queries)<!-- link:end --> が持つ。
- **ログ**：実行の途中経過を残すもの。ベストが更新された時刻や、リプレイから統計を取り出すスクリプトが例になる。
- **デバッグ用の表示**：不具合の調査で、途中の値や呼び出しの流れを出すもの。再現と仮説の確かめは <!-- link:begin fix-a-bug#hypotheses-before-fixes -->[バグを直す › 直す前に仮説を確かめさせる](fix-a-bug.md#hypotheses-before-fixes)<!-- link:end --> が持つ。
- **性能調査の表示**：実行時間の内訳を出すもの。計測の取り方は <!-- link:begin performance-tuning#profile-first -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › プロファイルを先に取る](performance-tuning.md#profile-first)<!-- link:end --> が持つ。

コンテストの上位者が語る考察の手順は、単純な解で試し、可視化で解を阻んでいる要因を見つけ、予想外の結果は必ず原因を調べる点で共通する（根拠：中）。この「見つけて調べる」回数を増やすために、見る道具を手早く作る。

道具を作らせる側の問いは、「いま自分は何が見えていないのか」である。見えていないものを言葉にできないうちは、道具を頼む段階に進まず、先に自分で入力と出力を読む。

!!! example "判断例：スコアが伸びない解の調べ方"
    - **状況**：最適化の課題で、改良した解のスコアが伸びない。実行ごとのログと、解の出力ファイルがある。
    - **迷う候補**：A は、ログを渡して「何が悪いか」を分析させる。B は、要素ごとのスコアの寄与を表示するビジュアライザと、ケース別の集計を作らせ、自分で見る。
    - **選んだもの**：B。
    - **理由**：A は原因の推測が返り、確かめる手間が人に残る。B は見えていなかった制約要因を人が自分の目で見つけられ、新しい操作の案も自分の言葉で書ける。ただし、ログが数行しかなく一目で読めるなら、道具を作らず直接読むほうが速い。

コンテストで使うときは、大会の規則で AI の利用が許されているかを、主催者の最新の規則で先に確かめる。

## 進める順番 {#flow}

道具づくりは、依頼・実行・手計算での確かめ・観察の 4 段で進める。各段の終わりに、次へ進んでよい印を置く。

1. **依頼する**：見たいもの・入力の場所・結論を書かせない旨を伝える。終わりの印は、再実行できるスクリプトが手元に残り、各値の計算の意味が 1 行ずつ書かれていること。
2. **実行する**：実データで動かし、出力を自分で受け取る。終わりの印は、読み飛ばした行や欠けた入力の数が出力に出ていること。
3. **手計算で確かめる**：「道具の値を手計算で確かめる」の節の手順で、小さな例の値と合うかを確かめる。終わりの印は、食い違いがなくなること。
4. **観察する**：道具の表示を自分で読み、気づいたことを自分の言葉で書く。終わりの印は、次に試す小さな実験が 1 つ書かれていること。

面によって、道具の置き場所と見せ方が違う。

=== "アプリ"

    手元のデータをファイルで渡し、グラフや表を見せる画面として作らせる。繰り返し使う道具にしたいときや、共有したときに誰の権限で動くかは <!-- link:begin artifacts-as-apps#runtime -->[アーティファクトを小さなアプリにする › Claude を呼ぶ・アプリにつなぐ・データを残す](../app/artifacts-as-apps.md#runtime)<!-- link:end --> と <!-- link:begin artifacts-as-apps#whose-account -->[アーティファクトを小さなアプリにする › 共有したときに誰の権限と枠で動くか](../app/artifacts-as-apps.md#whose-account)<!-- link:end --> で確かめる。

=== "Claude Code"

    プロジェクトの中のスクリプトとして作らせ、ログのファイルを直接読ませて実行させる。出力は人が受け取る。スクリプトはコミットして残すと、次の実行と別の人の確かめに使える。

依頼の雛形を次に示す。

<!-- gen:begin snippet build-observation-tools/ask-for-tool -->
<!-- textlint-disable -->

???+ example "雛形：結論は書かせず、観察の道具だけを作らせる依頼の雛形"

    ```text
    〔対象〕の出力を見て、私が自分で原因を考えるための観察の道具を作ってほしい。結論や改善案は書かないでほしい。

    見たいもの：
    - 〔例：要素ごとのスコアへの寄与／1 ステップずつの状態／ケースごとの集計／ベスト更新の時刻〕

    入力：
    - 〔ログ・出力ファイルの場所と形式〕

    条件：
    - 道具は、あとで同じ入力から再実行できるスクリプトにする。結果を会話の中の文章だけで返さない。
    - 表示する値は、元のデータの何をどう計算したものかを、道具の出力か README に 1 行ずつ書く。
    - 推測で埋めた値、欠けた入力、読み飛ばした行があれば、道具の出力に数を出す。
    - 作ったら、私が手で計算できる小さな入力（〔3〜5 件程度〕）で動かし、出力をそのまま見せる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet build-observation-tools/ask-for-tool -->

## 道具の値を手計算で確かめる {#hand-check}

道具が出す値は、入力が数件の小さな例を手で計算した結果と合うかを、実データで使う前に確かめる。手計算の例は、人が式を追って確かめられる大きさにする。

確かめる手順は次のとおりである。

1. 入力が 3〜5 件ほどの小さな例を用意し、各値を手計算する。計算の途中の式も残す。
2. その例を道具に通し、出力と手計算を 1 つずつ突き合わせる。
3. 部分と全体の関係を確かめる。要素ごとの寄与の合計が全体のスコアと一致するか、ログの行数が実行した回数と一致するか、といった関係である。
4. 食い違いは、どちらが間違いかを人が決める。道具を直させる前に、食い違いの一覧だけを出させる。

手計算の例を Claude に作らせるときも、式つきの例を先に出させ、人が式を追って確かめてから、道具を動かさせる。道具の出力を見てから例を作らせると、出力に合わせた例になりやすい。

<!-- gen:begin snippet build-observation-tools/ask-for-hand-check -->
<!-- textlint-disable -->

??? example "雛形：道具の出す値を、手計算の例で確かめさせる依頼の雛形"

    ```text
    作ってもらった道具の出す値が正しいかを、小さな例で確かめたい。

    1. 入力が 3〜5 件ほどの小さな例を作り、各値を手計算した結果を、計算の途中の式つきで先に書いてほしい。道具はまだ動かさない。
    2. 次に、その例を道具に通した出力をそのまま貼ってほしい。
    3. 手計算と食い違う値があれば、直さずにその一覧だけを出してほしい。

    あわせて、次も確かめて結果を見せてほしい。
    - 〔例：要素ごとの寄与の合計が、全体のスコアと一致する〕
    - 〔例：ログの行数が、実行した回数と一致する〕
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet build-observation-tools/ask-for-hand-check -->

検証器そのものを確かめる、より広い手順は <!-- link:begin test-the-verifier -->[検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)<!-- link:end --> が持つ。観察の道具は判定には使わず、読むための道具なので、確かめる範囲はこの節の手順で足りる。道具の出力で合否を決めるようになったら、そちらの手順に切り替える。

## 全体の確かめ方 {#how-to-check}

観察の道具づくりが狙いどおりに働いたかは、次の 3 つで確かめる。

- **観察が自分の言葉になっているか**：道具を使ったあと、気づいたことを、道具の表示を見ずに 3 つ書けるか。書けないなら、道具が見せたものを読み切れていない。
- **次の実験が決まったか**：表示を読んで、次に試すことが 1 つ具体的に決まったか。決まらないなら、見たいものが道具に映っていない。
- **結論を AI に頼み直していないか**：道具の表示を貼って「で、原因は何か」と聞いていないか。聞いたなら、道具づくりの狙いが外れている。先に自分の案を書く順序に戻る（<!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end -->）。

## 失敗したとき {#when-it-fails}

観察の道具づくりでよくある失敗と、その戻り先を並べる。

- **手計算と値が合わない**：道具の計算か、手計算のどちらかの誤りである。どちらかを人が決めたうえで、食い違った例を添えて道具を直させる。手計算が正しいのに道具が直らないときは、検証器を確かめる手順（<!-- link:begin test-the-verifier#when-it-fails -->[検証器そのものを確かめる（red/green・手で計算したケース） › 失敗したとき](../eval/test-the-verifier.md#when-it-fails)<!-- link:end -->）に戻る。
- **表示が整っていて、何を示す値か分からない**：各値の計算の意味を 1 行ずつ書かせる。書かせても説明できないものは、読み取りに使わない。
- **道具をいくら作り直しても見たいものが映らない**：見たいものが言葉になっていない。依頼を止めて、入力と出力を自分で読む。生データで裏取りする手順は <!-- link:begin data-analysis#when-it-fails -->[データを分析する › 失敗したとき](data-analysis.md#when-it-fails)<!-- link:end --> にある。
- **道具の表示を見るだけで安心してしまう**：表示が整っていると、判断まで預けてしまう。手元に残す判断を <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end --> で見直す。
- **不具合が直らない**：道具で見えた事実を渡して、直し方を頼み直す。巻き戻して頼み直す手順は <!-- link:begin fix-a-bug#when-stuck -->[バグを直す › 直らないときは巻き戻して頼み直す](fix-a-bug.md#when-stuck)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)

**関連**

- [データを分析する](data-analysis.md)
- [バグを直す](fix-a-bug.md)
- [性能改善を頼む（プロファイルが先・出力の一致と実測）](performance-tuning.md)
- [検証環境・テスト基盤を作らせる](build-test-harness.md)
- [アーティファクトを小さなアプリにする](../app/artifacts-as-apps.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
