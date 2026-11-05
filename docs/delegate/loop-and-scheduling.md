---
id: loop-and-scheduling
title: /loop と定期実行の方式
aliases: [Desktop scheduled tasks, 定期タスク, Desktop の定期タスク, 予定のタスク]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 170
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 開いているセッションの中で依頼を繰り返す /loop と、手元やクラウドで決まった時刻に走らせる方式を使い分けられる。途中で質問できないので、成功の定義と結果の置き場所を依頼に書く。
signs:
  - {type: goal, text: 毎朝決まった調査をさせたい}
  - {type: goal, text: 数分おきにビルドやデプロイの状態を見張らせたい}
prerequisites: [five-questions-before-delegating, what-auto-mode-stops]
related: [cloud-schedules, tasks-and-schedules-in-the-app, choosing-automation, goal-until-done, checking-unattended-runs, completion-notifications, parallel-and-loop-costs, headless-basics]
tracks: [loop, scheduled-tasks]
sources: [cc-docs-scheduled-tasks, cc-docs-desktop-scheduled-tasks, cc-docs-routines, cc-docs-commands]
volatility: 中
sections:
  - {title: セッションの中で繰り返す（/loop）, anchor: loop}
  - {title: どこで走らせるか（セッション・手元・クラウド）, anchor: where-to-run}
  - {title: 成功の定義と結果の置き場所, anchor: success-and-results}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：開いているセッションで依頼を繰り返す /loop と、決めた時刻に手元やクラウドで走らせる方式を、場面で使い分けられる。
    - **いつ引くか**：毎朝決まった調査をさせたいときや、数分おきにビルドやデプロイの状態を見張らせたいとき。
    - **前提**：<!-- link:begin five-questions-before-delegating -->[任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)<!-- link:end -->・<!-- link:begin what-auto-mode-stops -->[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)<!-- link:end -->
    - **強制力**：繰り返しと時刻の起動だけを担う。守らせたい条件を強制はせず、お願いの扱いになる。

<!-- textlint-disable -->
別名：Desktop scheduled tasks・定期タスク・Desktop の定期タスク・予定のタスク
<!-- textlint-enable -->

/loop と定期実行は、同じ依頼を人がいない間に繰り返し走らせる仕組みである。繰り返す場所は 3 つある。開いているセッションの中、自分の機械、Anthropic のクラウドである。どれも途中で質問に答える人がいないので、依頼に成功の定義と結果の置き場所を書く。

## セッションの中で繰り返す（/loop） {#loop}

/loop は、開いているセッションの中で依頼を間隔をおいて繰り返す同梱のスキルである。デプロイやビルドや PR の状態のように、短い間隔で変わるものを確かめ直す場面に向く。確かめていないまま「終わったはず」と進む原因を、繰り返しの確認で減らす。

書き方は、間隔と依頼の有無で 3 通りに分かれる。

| 書き方 | 例 | 起きること |
| --- | --- | --- |
| 間隔と依頼 | `/loop 5m check the deploy` | 決めた間隔で、依頼を繰り返す |
| 依頼だけ | `/loop check the deploy` | 反復のたびに、Claude が次の間隔を決める |
| 何も書かない | `/loop` | 組み込みの保守用の依頼か、`.claude/loop.md` の内容を実行する |

依頼にスキルを渡すこともできる。ただし、Claude が自分で呼び出してよいスキルだけが動く。`/permissions` などの組み込みコマンドは、実行されず、ただの文字として届く。

間隔を省いた形は、Claude が <!-- fact:begin loop-self-paced-interval-range -->1 分から 1 時間（2026-11-05 時点）<!-- fact:end --> の範囲で間隔を選び、状態が変わらないと長めに待つ。Monitor の道具が使えるセッションでは、Claude が繰り返しの代わりに Monitor を使うこともある。出力を流して受け取れるので、繰り返しよりも無駄が少ない。

### 止め方と限界

止め方は、形によって違う。

- 間隔を Claude が決める形は、待っている間に `Esc` で止められる。仕事が終わったと Claude が判断すれば、自分で終えることもある
- 間隔を固定した形は、`Esc` では止まらない。「デプロイ確認のループを止めて」のように、Claude に取り消しを頼む

限界は、セッションの中で動くことから来る。

- セッションを閉じると止まる。`--resume` や `--continue` で、期限が切れていない固定の間隔の繰り返しは戻る。間隔を Claude が決める形は戻らないので、`/loop` を打ち直す
- Claude が応答の途中のときは発火せず、ターンの間に動く。長い作業の間に過ぎた回は、取りこぼした回数ぶんではなく 1 回だけ動く
- 発火の時刻は少し遅れる。API への集中を避けるために、道具が時刻をずらすからである
- 繰り返しは、作ってから <!-- fact:begin loop-recurring-expiry-days -->7 日で失効する（2026-11-05 時点）<!-- fact:end -->。日数は変わりうるので、公式の文書で確かめる。
- 1 セッションに置ける予定のタスクは <!-- fact:begin loop-max-tasks-per-session -->50 件まで（2026-11-05 時点）<!-- fact:end --> である。
- 長く使いたいときは、作り直すか、手元やクラウドの方式に移す

## どこで走らせるか（セッション・手元・クラウド） {#where-to-run}

走らせる場所は、機械を開けておけるか、手元のファイルが要るか、で選ぶ。

| 方式 | 動く場所 | 向く場面 | 詳しい説明 |
| --- | --- | --- | --- |
| /loop | 開いているセッション（自分の機械） | セッションの間だけの見張り。手元のファイルも使える | この節 |
| Desktop scheduled tasks | 自分の機械。セッションは開けなくてよい | 手元のファイルや道具が要る定期の作業。機械は起きている必要がある | この表の下の説明 |
| クラウドの予定のタスク | Anthropic のクラウド。機械は要らない | 機械を閉じても動かしたい作業。作業は新しい clone の上で動き、手元のファイルは見えない | <!-- link:begin cloud-schedules#triggers -->[クラウドの定期タスク › きっかけ（時刻・API・GitHub のイベント）](cloud-schedules.md#triggers)<!-- link:end --> |

公式の比較表は、権限の扱いも分けている。/loop は、開いているセッションの権限を引き継ぐ。Desktop は、タスクごとの設定である。クラウドは、既定で auto モードが動く。人が答えられない実行では、確認が要る操作は止まるか、分類器の判断に任される。止められたときの見直し方は、<!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> を引く。

Desktop scheduled tasks は、Claude Code Desktop で作る、自分の機械で走る定期タスクである。時刻になると、開いているセッションがなくても新しいセッションが立ち上がる。手元のファイルを読めるのが、クラウドとの違いである。作り方の詳細は、公式の文書を引く。

間隔の下限は、方式ごとに違う。`/loop` は <!-- fact:begin loop-min-interval -->1 分（2026-11-05 時点）<!-- fact:end -->、Desktop は <!-- fact:begin desktop-scheduled-task-min-interval -->Claude が設定すると 1 分、フォームでは 1 時間（2026-11-05 時点）<!-- fact:end -->、クラウドは <!-- fact:begin cloud-scheduled-task-min-interval -->1 時間（2026-11-05 時点）<!-- fact:end --> で、クラウドが最も長い。数値は変わりうるので、公式の文書で確かめる。成熟度と入った版は、道具が次の表に出す。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 成熟度 | 入った版 |
| --- | --- | --- |
| [/loop](loop-and-scheduling.md) | GA | 2.1.71（2026-03-07） |
| [予定のタスク（scheduled tasks）](cloud-schedules.md) | research preview | — |

すべて共通：面 Claude Code、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

クラウドの定期実行は、<!-- name:begin routines-to-scheduled-tasks -->クラウドの予定のタスク（cloud scheduled tasks）<!-- name:end --> が今の名前である。古い記事には routines と書かれている。接続先と権限を最小にする考え方は <!-- link:begin cloud-schedules#least-privilege -->[クラウドの定期タスク › 接続先と権限を最小にする](cloud-schedules.md#least-privilege)<!-- link:end --> にある。アプリで頼むタスクの定期実行は、<!-- link:begin tasks-and-schedules-in-the-app#where-it-runs -->[タスクと定期タスク（Cowork） › どこで動くか（クラウドと Desktop）](../app/tasks-and-schedules-in-the-app.md#where-it-runs)<!-- link:end --> が持つ。名前が似ているが、ここで扱う Desktop scheduled tasks は Claude Code の公式の名前である。

無人に近づくほど、守りを先に厚くする。任せる段階ごとの確かめ方と封じ込めは <!-- link:begin five-questions-before-delegating#proportional-guards -->[任せ方の段階と、無人で走らせる前の五つの問い › 段ごとに強める確かめ方と封じ込め](five-questions-before-delegating.md#proportional-guards)<!-- link:end --> にある。

!!! example "判断例：毎朝の調査"
    - **状況**：毎朝、依存パッケージの更新情報を調べて、前日との差をまとめさせたい。自分の PC は朝に閉じていることが多い。
    - **迷う候補**：Desktop scheduled tasks は手元のファイルが使える。クラウドの予定のタスクは PC を閉じていても動く。
    - **選んだもの**：クラウドの予定のタスク。
    - **理由**：調べる対象は公開の情報とリポジトリだけで、手元のファイルが要らない。PC が閉じていることが多いので、機械が起きている前提の方式は取りこぼす。

!!! example "判断例：デプロイの見張り"
    - **状況**：デプロイを始めてから、終わるまでの数十分、数分おきに状態を見たい。
    - **迷う候補**：/loop で今のセッションに見張らせる。定期タスクを作る。
    - **選んだもの**：/loop。
    - **理由**：見張りはデプロイが終わるまでの短い間で足りる。終わりの条件を依頼に書けば、終わったときにループも終わる。定期タスクは、残して管理する手間のほうが大きい。

## 成功の定義と結果の置き場所 {#success-and-results}

定期の実行と /loop の依頼は、実行中に質問できないので、依頼の中で決めきる。公式も、定期タスクの依頼には成功の定義と結果の扱いを明示するよう勧めている。書くことは 4 つある。

- 成功の定義：何が揃えば「できた」と言えるか。言えないまま終わると、確かめていない結果が成功の顔で残る
- 結果の置き場所：ファイルの経路や PR など、あとから開ける所。会話の中だけに残すと、次の実行や別の日に拾えない
- 触らないもの：読むだけにする範囲と、push や削除のように取り消しにくい操作。許す範囲は、依頼だけでなく権限の設定でも絞る
- 分からないときの動き：質問で止まらず、分かった範囲と未確認を書いて終える

同じ依頼を、書き足す前と後で並べる。

```text
Before: 毎朝、依存パッケージの更新を調べて。

After: 毎朝、依存パッケージの更新を調べて、reports/deps/YYYY-MM-DD.md に書いて。
成功の定義は、更新のあるパッケージごとに、現行の版・最新の版・変更点の URL が
1 行で並んでいること。前日のファイルとの差を先頭に 3 行で書く。
reports/deps/ 以外は変えない。分からない点は「未確認」の見出しにまとめる。
```

After で足したのは、結果の置き場所（経路）、成功の定義（並べる項目）、触らない範囲、分からないときの動きである。

結果は、走り終えた報告だけで決めない。出力・記録・差分で確かめる。この考え方は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある。

最後の判断を人に置く流儀は <!-- link:begin checking-unattended-runs#final-decision -->[無人実行の結果を確かめる › 最後の判断を人に置く](../verify/checking-unattended-runs.md#final-decision)<!-- link:end --> を読む。知らせを待つか、時刻を決めて見に行くかは <!-- link:begin completion-notifications#when-to-notify -->終わったら知らせてもらう<!-- link:end --> で選ぶ。

間隔を短くするほど、実行の回数が増える。費用は、本数・回数・1 回の文脈の掛け算で膨らむ。始める前に、止める条件と上限を決める。手順は <!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> を読む。

## 雛形 {#templates}

定期タスクの依頼文の型と、/loop で見張る依頼の型を置く。動作は、新しいセッションで確かめてから使う。

<!-- gen:begin snippet loop-and-scheduling/scheduled-prompt -->
<!-- textlint-disable -->

??? example "雛形：定期タスクの依頼文（成功の定義と結果の置き場所）"

    ````markdown
    毎朝の調査を、質問できない前提で頼む依頼文の型。<>の中を自分の案件の言葉に替えて使う。

    ```text
    <調べる対象>の最新の状況を調べて、<置き場所>に結果を書いてください。

    成功の定義:
    - <調べる項目 A>と<調べる項目 B>について、それぞれ根拠の URL か該当のファイルの行を添えて 1 段落でまとめてある
    - 前回の結果（<置き場所>の直近のファイル）と比べて、変わった点が先頭に 3 行以内で書いてある

    結果の置き場所:
    - <置き場所>/YYYY-MM-DD.md（日付は実行日。同じ日のファイルがあれば上書きせず末尾に追記する）

    やらないこと:
    - <置き場所>以外のファイルを変えない
    - push、削除、外部への投稿はしない

    途中で分からないことがあっても、質問で止まらない。次のどちらかで終える:
    - 分かった範囲で結果を書き、分からなかった点を「未確認」の見出しにまとめる
    - 調べる対象に到達できなかったときは、到達できなかった旨だけを結果のファイルに書く
    ```
    ````

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.71。

<!-- textlint-enable -->
<!-- gen:end snippet loop-and-scheduling/scheduled-prompt -->

<!-- gen:begin snippet loop-and-scheduling/loop-watch -->
<!-- textlint-disable -->

??? example "雛形：/loop でデプロイを見張る依頼"

    ````markdown
    開いているセッションで、デプロイやビルドの状態を見張らせる /loop の依頼文の型。終わりの条件と、終わったときの動きを依頼に含める。

    ```text
    /loop 5m <デプロイ名>の状態を確かめて、結果を 1 行で報告して。

    - 成功か失敗のどちらかに決まったら、その結果を報告してループを終えて
    - 失敗なら、失敗したジョブのログの該当部分を要約して。修正はしないで
    - 状態が変わっていないときは「変化なし」と 1 行だけ書いて
    - 触ってよいのは読むだけの操作。push、再実行、削除はしないで
    ```
    ````

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.71。

<!-- textlint-enable -->
<!-- gen:end snippet loop-and-scheduling/loop-watch -->

## 効かない場面・落とし穴 {#pitfalls}

- 席を外すとセッションが閉じる。/loop はセッションが開いている間だけ動く。夜や週末をまたぐ見張りは、手元かクラウドの方式に移す
- 固定の間隔の繰り返しは `Esc` で止まらない。取り消しを Claude に頼み、予定の一覧を出させて残っていないか確かめる
- 失効を忘れる。期限が切れた繰り返しは、最後に 1 回動いて消える。毎日の習慣にするなら、定期タスクの側で作る
- 質問で止まる。条件が曖昧な依頼は、無人だと質問の所で止まり、結果が何も残らない。先に手動で 1 回走らせて、止まる所を潰す
- 結果が会話の中だけに残る。置き場所を決めていないと、次の実行で参照できない
- 仕様の決まった実装を完了まで進めたいときは、間隔の繰り返しではなく、完了の条件で続ける仕組みのほうが合う

## 比べる相手 {#compare}

- 完了の条件まで、間隔ではなく条件で続けさせたいときは、<!-- link:begin goal-until-done#when -->[/goal（完了するまで続けさせる） › 使いどころ](goal-until-done.md#when)<!-- link:end --> を選ぶ。/loop は時間の間隔、/goal は条件が軸である
- 決まった時刻・イベント・スクリプトから Claude を動かす方法を、動く場所と課金の違いで選ぶときは、<!-- link:begin choosing-automation -->[自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)<!-- link:end --> を引く
- スクリプトや CI から結果を決まった形式で受け取りたいときは、<!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](headless-basics.md)<!-- link:end --> を使う
- クラウドの定期タスクの詳細は、<!-- link:begin cloud-schedules -->[クラウドの定期タスク](cloud-schedules.md)<!-- link:end --> を引く

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)

**次に読む**

- [自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)
- [クラウドの定期タスク](cloud-schedules.md)

**関連**

- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [/goal（完了するまで続けさせる）](goal-until-done.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [非対話モード（claude -p）の基本](headless-basics.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)：Anthropic・英語・確認日 2026-11-04
- [Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks)：Anthropic・英語・確認日 2026-11-04
- [Automate work with scheduled tasks](https://code.claude.com/docs/en/routines)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
