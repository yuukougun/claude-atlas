---
id: usage-context-statusline
title: /usage・/context・ステータスラインで状態を見る
nav_title: /usage・/context・ステータスライン
aliases: [/usage, status line, ステータスライン, /statusline, /cost, /stats, 使用量を見る]
type: feature
field: cli
chapter: 見る・切り分ける
order: 100
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 見せる]
prevents: [合っていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 上限の使い方は /usage、文脈の内訳は /context で見て、遅い・高い・言うことを聞かない理由を推測せずに測る。ステータスラインに出しておけば、長い作業の途中でも気づける。
signs:
  - {type: goal, text: 上限やコンテキストの使用量を、いつも見えるようにしたい}
  - {type: symptom, text: 上限に近づいていることに、止まるまで気づけない}
prerequisites: [how-usage-limits-work]
related: [inspect-context#reading, what-uses-up-limits#find-what-uses-it, insights-and-usage-review, felt-vs-measured, hits-limits-quickly, isolate-with-safe-mode, command-cheatsheet]
tracks: [usage, statusline, context-window]
outdated_advice: [slash-cost-and-stats]
sources: [cc-docs-statusline, cc-docs-costs, cc-docs-commands, cc-changelog, cc-docs-context-window]
volatility: 中
sections:
  - {title: 三つの道具で見えるもの, anchor: instruments}
  - {title: ステータスラインに出すもの, anchor: statusline}
  - {title: いつ見るか, anchor: when}
  - {title: 効かない場面と落とし穴, anchor: pitfalls}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：上限の使い方は /usage、文脈の内訳は /context で見て、ステータスラインに使用率を出し続けられる。
    - **いつ引くか**：上限やコンテキストの使用量をいつも見えるようにしたいとき。上限に近づいていることに、止まるまで気づけないとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)<!-- link:end -->

<!-- textlint-disable -->
別名：/usage・status line・ステータスライン・/statusline・/cost・/stats・使用量を見る
<!-- textlint-enable -->

/usage・/context・ステータスラインは、Claude Code の状態を測る 3 つの道具である。遅い・高い・言うことを聞かない理由を、推測せずに数字で見られる。見るだけの道具で、使用量を減らす力は持たない。減らす方法は、見て分かった原因ごとに別のページが持つ。

## 三つの道具で見えるもの {#instruments}

3 つの道具は、見える範囲が違う。上限の使い方は /usage、今の会話の文脈は /context、常に見える小さな表示がステータスラインである。画面の項目の読み方は持ち主のページが書くので、ここでは何が分かるかと、どこを読むかだけを示す。

| 道具 | 見えるもの | 読み方の持ち主 |
| --- | --- | --- |
| /usage | 費用の見積もり、プランの上限の使用量、何が上限に数えられたかの内訳 | <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> |
| /context | 今の会話で、文脈のどれだけを何が占めているか | <!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end --> |
| ステータスライン | 画面の下に出しっぱなしにする、設定したスクリプトの出力 | 次の節 |

使用量を見るコマンドの今の名前は <!-- name:begin cost-stats-to-usage -->/usage<!-- name:end --> である。以前の /cost と /stats は別名として残り、/usage の該当のタブを開く。内訳に出る項目は、プランや版で変わる。

3 つの道具の属性は、次の表のとおりである。

<!-- gen:begin compare 成熟度 コンテキストのコスト 入った版 -->
<!-- textlint-disable -->

| 機能 | コンテキストのコスト | 入った版 |
| --- | --- | --- |
| [/usage](usage-context-statusline.md) | — | 2.0.0（2025-09-29） |
| [ステータスライン（status line）](usage-context-statusline.md) | ゼロ | 1.0.71（2025-08-07） |
| [コンテキストウィンドウ](../basics/attention-budget.md) | — | — |

すべて共通：成熟度 GA。

<!-- textlint-enable -->
<!-- gen:end compare 成熟度 コンテキストのコスト 入った版 -->

測る道具を使う理由は、原因を取り違えないためである。上限が早く減るときも、返答が遅いときも、原因は会話の長さ、常駐するもの、モデルと effort、手戻りのどれかであることが多い。数字を見ずに直すと、実際の原因に合っていない対処に手間をかける（防ぐ原因：合っていない）。見えるようにして確かめることが、この道具の効き方である。

上限そのものの仕組みは、<!-- link:begin how-usage-limits-work#shared-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 面をまたいで一つの枠](../cost/how-usage-limits-work.md#shared-limit)<!-- link:end -->が持つ。残りを見る場所は <!-- link:begin how-usage-limits-work#where-to-check -->[利用上限の仕組み（面をまたいで共有する枠） › 残りを見る場所](../cost/how-usage-limits-work.md#where-to-check)<!-- link:end --> にある。

## ステータスラインに出すもの {#statusline}

ステータスラインは、設定したシェルのスクリプトの出力を画面の下に出し続ける機能である。スクリプトはセッションの JSON を受け取って表示するだけで、API のトークンを使わない。文脈にも入らない。コンテキストのコストは <!-- gen:begin feature statusline/context_cost -->ゼロ<!-- gen:end feature statusline/context_cost --> である。

渡される JSON には、モデル名、作業ディレクトリ、費用、文脈の使用率、短い周期の上限の使用率などが入る。項目の名前は版で変わりうるので、本文には書かない。雛形と、公式の「Customize your status line」で確かめる。

何を出すかは、止まると困るものから選ぶ。次の 2 つは、長い作業の途中で気づきたい数字である。

- **文脈の使用率**：会話が長くなって、指示が効きにくくなる前に気づける。
- **短い周期の上限の使用率**：作業が上限で止まる前に気づける。

この 2 つを常に出す使い方は、公式が勧める手順ではなく、実践の例である（根拠：中）。出すだけなので、迷ったら小さく始めてよい。`/statusline` に出したい内容を日本語で頼むと、設定を作らせることもできる。手で書くなら、次の 2 つの雛形を使う。1 つ目が設定、2 つ目がスクリプトである。スクリプトは実行できる状態にして、設定の `command` からそのパスを指す。

<!-- gen:begin snippet usage-context-statusline/statusline-settings -->
<!-- textlint-disable -->

??? example "雛形：ステータスラインのスクリプトを登録する設定"

    ```json
    {
      "statusLine": {
        "type": "command",
        "command": "~/.claude/statusline.sh"
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.71。

<!-- textlint-enable -->
<!-- gen:end snippet usage-context-statusline/statusline-settings -->

<!-- gen:begin snippet usage-context-statusline/statusline -->
<!-- textlint-disable -->

??? example "雛形：文脈と上限の使用率を出すステータスラインのスクリプト"

    ```bash
    #!/bin/bash
    # ステータスラインに、文脈の使用率と、短い周期の上限の使用率を 1 行で出す。
    # Claude Code が標準入力に渡すセッションの JSON を読み、値のある項目だけを並べる。
    input=$(cat)

    ctx=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
    limit=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')

    line=""
    [ -n "$ctx" ] && line="文脈 $(printf '%.0f' "$ctx")%"
    [ -n "$limit" ] && line="${line:+$line | }上限 $(printf '%.0f' "$limit")%"

    echo "${line:-(値なし)}"
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.71。

<!-- textlint-enable -->
<!-- gen:end snippet usage-context-statusline/statusline -->

スクリプトは `jq` を使う。値が渡されない項目は空になり、その項目は出さない。どの環境で上限の項目が渡るかは、未確認である。対象は WSL・Linux の CLI で、ほかの OS と IDE 拡張の表示は未確認である。

## いつ見るか {#when}

見る道具は、問いごとに使い分ける。数字を見る目的は、次の行動を決めることである。

- **作業の途中、常に**：ステータスラインの使用率を見る。上限が近づいたら、区切りのよい所で作業を畳む。当たった後の動きは <!-- link:begin how-usage-limits-work#when-you-hit-the-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 上限に当たったとき](../cost/how-usage-limits-work.md#when-you-hit-the-limit)<!-- link:end -->にある。
- **会話が重い、指示が効かない**：/context で、会話・読み込んだファイル・常駐するもののどれが場所を取っているかを見る。起動直後の値を控えておくと、増えた分が分かる。片付け方は <!-- link:begin inspect-context#what-to-do -->[/context で中身を見る › どの片付け方を選ぶか](../context/inspect-context.md#what-to-do)<!-- link:end --> にある。
- **上限が早く減った**：/usage の内訳で、何が数えられたかを見る。長い会話の送り直し、大きな添付、並列の作業などを、自分の場合で突き合わせる。切り分けの順は <!-- link:begin hits-limits-quickly#diagnosis -->[すぐ上限に当たる › 原因を安く確かめる順](../symptoms/hits-limits-quickly.md#diagnosis)<!-- link:end --> にある。
- **設定のせいか疑う**：数字だけでは分からないので、設定を外して同じ依頼で比べる。やり方は <!-- link:begin isolate-with-safe-mode -->設定を外して切り分ける（--safe-mode）（準備中）<!-- link:end --> にある。
- **振り返る**：/usage の内訳から、削るものを選ぶ。<!-- link:begin insights-and-usage-review#usage-breakdown -->/insights と /usage で振り返る › /usage の内訳から削るものを選ぶ（準備中）<!-- link:end --> がそのやり方を持つ。

!!! example "判断例：遅くなった理由を測る"
    - **状況**：長い作業の後半で、返答が遅くなり、最初に頼んだ書き方も守られなくなってきた。
    - **迷う候補**：モデルが劣化したと見て、すぐ新しい会話に切り替える。または、先に /context で文脈の内訳を見る。
    - **選んだもの**：先に /context で内訳を見て、数字を控えてから決める。
    - **理由**：体感だけでは、モデルの問題か、会話の長さの問題かが分からない。内訳で文脈が埋まっていると分かれば、片付けるのが筋になる。埋まっていなければ、別の原因を探せる。体感と実測のずれは <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end --> にある。

コマンドの早見は <!-- link:begin command-cheatsheet -->主要コマンド早見表（準備中）<!-- link:end --> から引ける。

## 効かない場面と落とし穴 {#pitfalls}

- **見るだけで、止めない**：ステータスラインと /usage は、使用量を抑えない。作業を止める力はなく、強制力は持たない道具である。
- **原因までは出ない**：ステータスラインの使用率は、増えたことだけを示す。何が使ったかは、/usage の内訳か /context で見る。
- **数字は今の値で、将来の予測ではない**：使用率が低くても、次の依頼で大きく増えることがある。余裕の目安として読み、ぎりぎりまで使い切る判断の根拠にしない。
- **表示を信じすぎない**：画面の項目の名前や出る条件は、版で変わりうる。表示が空でも、使用量がゼロとは限らない。疑わしいときは /usage で確かめる。
- **公式の勧めと混ぜない**：ステータスラインで常に監視する使い方は、実践の例である。公式の文書が勧めているわけではない。

## 古くなった助言 {#outdated}

使用量を見るのは /cost、使い方の統計を見るのは /stats、という助言は古い。今は /usage で見る。/cost と /stats は今も打てる別名で、新しく書く手順は /usage で書く。経緯は <!-- link:begin outdated-advice-ledger#slash-cost-and-stats -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#slash-cost-and-stats)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Customize your status line](https://code.claude.com/docs/en/statusline)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)

**関連**

- [/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)
- [上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)
- /insights と /usage で振り返る（準備中）
- [体感と実測](../eval/felt-vs-measured.md)
- [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- 設定を外して切り分ける（--safe-mode）（準備中）
- 主要コマンド早見表（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
