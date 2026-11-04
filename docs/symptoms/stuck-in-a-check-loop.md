---
id: stuck-in-a-check-loop
title: 同じ確認のループにはまる
aliases: [無限検証ループ, 実行と確認の繰り返し, ベンチを回すだけになる]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 240
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる, 握る]
prevents: [見えていない, 散らかっている, 合っていない]
pitfalls: [預けすぎる]
scenes: [開発, コンテスト]
summary: 実行と確認を繰り返すだけで進まないループを見分け、新しい仮説や情報を入れるか、止める条件を決めるか、新しい会話に移すかを選ぶ。
signs:
  - {type: symptom, text: ベンチを回してスコアを見るだけの繰り返しになる}
  - {type: symptom, text: 同じ修正と確認を利用上限まで繰り返す}
  - {type: symptom, text: 何時間も回したのに途中から進んでいない}
wave: 1
prerequisites: [agent-loop]
related: [performance-tuning, permission-to-stop, parallel-and-loop-costs, going-in-circles, wont-rethink-approach, blames-the-tools, misses-broken-evaluation, hits-limits-quickly, six-causes]
routes:
  - {cause: 見えていない, to: [share-targets-and-bounds, keep-failure-lessons, experiment-log]}
  - {cause: 散らかっている, to: [when-to-start-fresh, handoff-documents]}
  - {cause: 合っていない, to: [goal-until-done#writing-conditions, stop-hooks#avoid-loops, open-ended-loop-trap]}
  - {cause: 預けすぎる, to: [decide-when-to-quit, progress-logs-for-long-jobs, checking-unattended-runs]}
tracks: [goal, loop]
outdated_advice: [ralph-loops]
sources: [zenn-microsoft-78e01f59, zenn-hkdeveloper-claudeco, cc-docs-goal, cc-docs-scheduled-tasks]
volatility: 中
sections:
  - {title: よくある形, anchor: pattern}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの振り分け, anchor: routes}
  - {title: 判断例, anchor: example}
  - {title: 回す前に決めておくこと, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：実行と確認を繰り返すだけで進まないループを見分け、新しい情報を入れるか、止める条件を決めるか、新しい会話に移すかを選べる。
    - **いつ引くか**：ベンチを回してスコアを見るだけの繰り返しになったとき。同じ修正と確認を、利用上限まで繰り返しているとき。何時間も回したのに、途中から進んでいないとき。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：無限検証ループ・実行と確認の繰り返し・ベンチを回すだけになる
<!-- textlint-enable -->

同じ確認のループにはまるとは、Claude が実行と確認を何周も回しているのに、周ごとに新しい情報や仮説が入らず、結果が動かなくなる状態である。長い作業を任せて席を外した人が出会いやすい。

## よくある形 {#pattern}

同じ確認のループは、「回している」ことと「進んでいる」ことが別だと気づいたところで見つかる。最初に、ループかどうかを安く見分ける。

- 直近の数周で、見ている指標がほぼ同じ値のまま動いていない。
- 周ごとの変更が、同じファイルの同じ箇所への小さな手直しに偏っている。
- 周の合間に、新しいデータ（プロファイル・エラーの全文・別の計測）を取りに行っていない。
- 返答の中身が「再実行して確認する」「結果を見て調整する」の言い換えになっている。

実例が 2 つある。どちらも単独の報告で、旧世代や別の仕組みの結果を現行の Claude の傾向にしてはいけない。

- ISUCON13 の問題にエージェントを挑ませた企業の報告（Azure SRE エージェント）では、開始から約 1 時間で上位に近いスコアに届いた。3〜4 時間経った時点で伸びが止まり、ベンチの実行とスコアの確認を繰り返すだけになった。プロファイルの取り直しも、別の方針の検討もなかった。報告は今後の改善として、手法の知識を与える仕組みや検索を挙げる。試して効いたとは書いていない（根拠：中。単独の事例で、Claude とは限らないため類推）。
- 開発者の集まりの参加レポートに、同じ修正を利用上限に達するまで繰り返す「無限検証ループ」が止めるべき失敗の兆候として出る（根拠：弱。単独の経験談）。

どちらにも、時間をかければ良くなるという前提が崩れる所がある。長く回すだけでは足りないことは、<!-- link:begin open-ended-loop-trap#longer-is-not-better -->AI に改善を回させ続ける罠（開いたループ） › 長く回せば良くなるとは限らない（準備中）<!-- link:end --> でも扱う。

訂正を重ねても同じ誤りが戻ってくるなら、会話の中の堂々巡りである。その場合の入口は <!-- link:begin going-in-circles -->[同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)<!-- link:end --> から入る。この症状は、実行と確認を繰り返す長い作業のループの中で起きる点で分けている。

## 原因を安く確かめる順 {#diagnosis}

原因は 4 つに絞れる。ループの記録を見るだけで済む順に確かめる。全体の診断の考え方は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

1. 見えていない（原則「見せる」）
    - 原因：Claude の手元に、次の一手の材料がない。スコアなどの 1 つの指標しか見えておらず、遅い箇所を示すプロファイルや、失敗の内訳が入ってこない。
    - 何を見る：直近の数周で、Claude が取りに行った情報の種類。
    - どう確かめる：周ごとに、新しい情報が入った周があるかを数える。入っていなければ、この原因が濃い。依頼に目標値や上界があるかも見る。
2. 散らかっている
    - 原因：会話に過去の試行の出力が積み重なり、同じ試みを思い出せず、繰り返してしまう。
    - 何を見る：会話の長さと、同じ修正が複数回出ていないか。
    - どう確かめる：新しい会話で、状況を書いた短い文書だけを渡して続ける。進み方が変われば、この原因が濃い。見分け方の詳細は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
3. 合っていない
    - 原因：ループの組み方が課題に合っていない。止める条件がないまま、開いた課題（改善に終わりがない課題）を回している。
    - 何を見る：完了の条件が書かれているか、上限があるか、確認の結果が条件に結びついているか。Stop フックで終わらせない仕組みを使っているなら、止め続けていないか。
    - どう確かめる：条件を一文で言えるかを試す。言えなければ、条件が足りない。
4. 預けすぎる（人の側の落とし穴、原則「握る」）
    - 原因：止める基準と見る頻度を決めないまま、判断まで Claude に預けている。
    - 何を見る：最後に人が結果と記録を見たのはいつか。やめる基準を着手前に書いたか。
    - どう確かめる：基準を書いた日付が着手より後なら、基準が結果に引きずられている。進捗を人が追える形で出しているかも見る。

原因は重なることが多い。1 と 2 は安く試せるので先に確かめ、3 と 4 はループの組み方の見直しになる。

利用上限に早く当たっているだけで、ループの形でないなら <!-- link:begin hits-limits-quickly -->[すぐ上限に当たる](hits-limits-quickly.md)<!-- link:end --> へ。「環境が壊れた」と言い出したら <!-- link:begin blames-the-tools -->[環境や道具が壊れたと言い出す](blames-the-tools.md)<!-- link:end --> で、長い作業の劣化の兆しかを切り分ける。スコアが上がり続けるのに本番で通用しないときは <!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](misses-broken-evaluation.md)<!-- link:end --> である。

## 原因ごとの振り分け {#routes}

原因が分かったら、対処の本体は各分野のページで読む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | 目標値・上界を伝える（準備中）<br>失敗の教訓は捨てずに書き残す（準備中）<br>[実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md) |
| 散らかっている | [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[handoff 文書と document-and-clear](../context/handoff-documents.md) |
| 合っていない | [/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](../delegate/goal-until-done.md#writing-conditions)<br>Stop フックで「終わらせない」 › 止め続けるループを避ける（準備中）<br>AI に改善を回させ続ける罠（開いたループ）（準備中） |
| 預けすぎる | [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)<br>長時間ジョブの進捗ログを設計する（準備中）<br>無人実行の結果を確かめる（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：一晩回したベンチが朝から横ばいのとき"
    - **状況**：性能改善を Claude に任せて一晩回した。朝に見ると、スコアは数時間前から同じ値で、記録には「ベンチ実行→スコア確認」が並ぶ。会話はまだ短く、プロファイルを取ったのは最初の 1 回だけである。
    - **迷う候補**：A は、新しい会話に移して、状況をまとめた文書から続ける。B は、同じ会話のまま、プロファイルを取り直すよう指示する。
    - **選んだもの**：B。ただし、プロファイルを取り直した後の周でも結果が動かなければ A に切り替える。
    - **理由**：会話が短いので散らかっているとは言いにくく、新しい情報が入っていないことのほうが濃い原因だからである。プロファイルの取り直しは一言の指示で済み、会話を捨てずに試せる。A は捨てる分の学びを文書に残す手間がかかる。どちらも筋が通るが、安く確かめられるほうから試す。

## 回す前に決めておくこと {#prevention}

ループを回し続ける作業は、任せる幅を広げる。守りを先に置く。回す前に決めておくのは次の 3 つである。

1. 止める条件と上限。完了の条件、周の上限、使う量の上限を先に決める。書き方は <!-- link:begin goal-until-done#writing-conditions -->[/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](../delegate/goal-until-done.md#writing-conditions)<!-- link:end --> にあり、本数と回数の掛け算で費用が膨らむ理由は <!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> にある。
2. やめる基準。結果を見る前に、頭打ちの判断を書いておく。判定は作った本人から離す（<!-- link:begin decide-when-to-quit#plateau -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図](../judgment/decide-when-to-quit.md#plateau)<!-- link:end -->）。
3. 見える進捗。要約した指標を定期的に書き出し、人と Claude の両方が状況を追えるようにする。人が見ていない実行の結果は、終了コードだけでなく記録と差分で確かめる（<!-- link:begin checking-unattended-runs#beyond-exit-codes -->無人実行の結果を確かめる › 終了コードと要約だけで決めない（準備中）<!-- link:end -->）。

反復させてよいのは、仕様が決まり、止める条件のある実装の作業に限る。戦略そのものを回し続けさせる開いたループは、手元の評価への過適合を進めるので避ける（<!-- link:begin open-ended-loop-trap#closed-vs-open -->AI に改善を回させ続ける罠（開いたループ） › 閉じた反復と開いたループ（準備中）<!-- link:end -->）。

自作のループで同じ依頼を流し直す回し方は、古くなった助言として台帳にある。<!-- link:begin outdated-advice-ledger#ralph-loops -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#ralph-loops)<!-- link:end --> を見て、今の手段に置き換える。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)

**次に読む**

- 目標値・上界を伝える（準備中）
- 失敗の教訓は捨てずに書き残す（準備中）
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- Stop フックで「終わらせない」（準備中）
- AI に改善を回させ続ける罠（開いたループ）（準備中）
- ほか 3 ページ

**関連**

- 性能改善を頼む（プロファイルが先・出力の一致と実測）（準備中）
- 止まって報告する権利を渡す（準備中）
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](wont-rethink-approach.md)
- [環境や道具が壊れたと言い出す](blames-the-tools.md)
- [手元の評価は良いのに本番で通用しない](misses-broken-evaluation.md)
- [すぐ上限に当たる](hits-limits-quickly.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Azure SRE エージェントは ISUCON で戦えるか？パフォーマンスチューニングに挑戦してみた](https://zenn.dev/microsoft/articles/78e01f5932c025)：Zenn（microsoft）・確認日 2026-11-04
- [Claude Code Meetup Japan #3 参加レポート（前編）- 開発手法・実践編](https://zenn.dev/hkdeveloper/articles/claude-code-meetup-japan-3)：Zenn（hkdeveloper）・確認日 2026-11-04
- [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)：Anthropic・英語・確認日 2026-11-04
- [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
