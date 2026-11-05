---
id: blames-the-tools
title: 環境や道具が壊れたと言い出す
aliases: [環境のせいにする, ツールが壊れたと言う, 道具への不満が増える]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 260
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 見せる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 「環境や道具が壊れた」と言い出したときに、本当に壊れたのか、長い作業の劣化の兆しなのかを自分で確かめて切り分け、続けるか新しく始めるかを決める。
signs:
  - {type: symptom, text: 「環境が壊れている」と言って作業をやめる}
  - {type: symptom, text: ツールが動かないと言うが、自分で実行すると動く}
  - {type: symptom, text: 長く動かすうちに道具への不満が増えていく}
wave: 1
prerequisites: [agent-loop, context-rot]
related: [progress-logs-for-long-jobs, inspect-context, stuck-in-a-check-loop, insists-on-mistakes, claims-done-but-isnt, forgets-in-long-chats, lock-side-effects, six-causes]
routes:
  - {cause: 見えていない, to: [sandboxing, isolate-with-safe-mode]}
  - {cause: 散らかっている, to: [handoff-documents, when-to-start-fresh]}
  - {cause: 確かめていない, to: [evidence-not-reports#tool-output, checking-unattended-runs]}
tracks: [sandbox]
outdated_advice: []
sources: [cc-docs-sandboxing]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 判断例, anchor: example}
  - {title: 予防：仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：「環境や道具が壊れた」と言われたとき、本当に壊れたのか長い作業の劣化の兆しなのかを自分で切り分け、続けるか新しく始めるかを決められる。
    - **いつ引くか**：「環境が壊れている」と言って作業をやめたとき、ツールが動かないと言うのに自分で実行すると動くとき、長く動かすうちに道具への不満が増えていくとき。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->、<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：環境のせいにする・ツールが壊れたと言う・道具への不満が増える
<!-- textlint-enable -->

環境や道具が壊れたと言い出す症状は、Claude が失敗の原因を「環境の故障」に決めて、作業をやめたり不満を重ねたりする状態である。原因は 3 通りに分かれる。本当に壊れている、Claude から見えていない制限に当たっている、長い作業で文脈が劣化している、である。最初の一手は、人が同じ操作を自分で実行して確かめることだ。

## よくある形 {#forms}

読者が出会う形は 3 つある。

- 「環境が壊れている」と言って作業をやめる。テストの実行やビルドが 1 回失敗しただけで、続きを試さずに止まる。
- ツールが動かないと言うが、自分で実行すると動く。Claude の側でだけ失敗している。
- 長く動かすうちに道具への不満が増えていく。最初は時折だった「この道具は不安定だ」という言及が、時間とともに増える。

3 つ目は、劣化の前兆として報告されている。CTF の長時間運用の報告では、道具への不満の増加が劣化の前兆だった。経過時間を認識できず、数ミリ秒で「基盤が壊れた」と判断した例もある（根拠：中）。これは報告の時点の運用の観察で、版によって変わりうる。一般のエージェント運用への当てはめは類推である。

## 原因を安く確かめる順 {#diagnosis}

「壊れた」と言われたら、安く確かめられるものから順に潰す。Claude 側の 6 つの原因のうち、この症状に関わるのは 3 つで、全体の順は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

1. **人が同じ操作を自分で実行する**。いちばん安い確かめである。Claude が失敗したと言うコマンドを、同じ場所で人が実行する。人の側でも失敗するなら、本当に環境が壊れている。環境を直すのは人の仕事で、直してから作業を続ける。人の側で動くなら、Claude の実行の仕方に原因があるので、次に進む。
2. **見えていない**。Claude が実行する環境に制限があり、その制限が Claude から見えていない。見るのは、失敗の出力に拒否・時間切れ・権限を示す文言があるかと、サンドボックスの有無と範囲である。サンドボックスが効くのは、Claude が動かすコマンドとそこから起きたプロセスだ。Claude のファイルの道具・MCP サーバー・フックはサンドボックスの外で動く。この範囲を <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> で照らし、制限が原因なら、その制限の中身（拒否される場所や時間の上限）を、次の依頼に書いて Claude に見える形で伝える。自分の設定が原因かは <!-- link:begin isolate-with-safe-mode#compare -->[設定を外して切り分ける（--safe-mode） › 比べ方](../cli/isolate-with-safe-mode.md#compare)<!-- link:end --> の比べ方で切り分ける。この手は設定を外して挙動を比べるもので、権限と管理の設定は効いたままである。安全の設定を外して試す手ではない。
3. **散らかっている**。長い作業で、失敗した試みや無関係な情報が会話に溜まっている。見るのは、作業の長さと、同じ失敗の話が何度も残っていないか、不満が増えていないかである。<!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end --> で、何が場所を取っているかを見分ける。確かめは、引き継ぎを書かせて新しい会話で同じ依頼を出し、「壊れた」が消えるかを見ることだ。消えるなら劣化で、新しくする合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
4. **確かめていない**。向きは 2 つある。1 つは、Claude が出力を読まずに「壊れた」と決めた場合。もう 1 つは、道具が本当に誤った結果を返していた場合で、検索が途中で打ち切られたり、起動に失敗しても成功の終了コードで終わったりする。見るのは、Claude が「壊れた」の根拠にした出力そのものである。確かめは、実行したコマンドと生の出力を出させ、人が同じ出力を再現することだ。道具の出力を疑う例は <!-- link:begin evidence-not-reports#tool-output -->[報告ではなく証拠を求める › 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動）](../verify/evidence-not-reports.md#tool-output)<!-- link:end --> にある。

根拠を出させる依頼は、次の雛形が使える。要約を求めず、コマンド・生の出力・終了コード・再実行の結果を求める。

<!-- gen:begin snippet blames-the-tools/ask-for-raw-output -->
<!-- textlint-disable -->

???+ example "雛形：「壊れている」の根拠を生の出力で出させる依頼"

    ```text
    「環境が壊れている」と判断した根拠を、推測を混ぜずに出してほしい。次の順で答える。

    1. 失敗したコマンドを、実行したとおりに一字一句そのまま書く。
    2. そのコマンドの生の出力（エラー文を含む）と終了コードを、要約せずに貼る。
    3. 同じコマンドをもう一度実行し、結果が同じかを書く。
    4. 失敗の文言に、権限の拒否・時間切れ・サンドボックスの制限を示すものがあるかを書く。あれば該当の行を引く。

    出力がなかった、または確かめられなかった項目は、推測で埋めず「確かめていない」と書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet blames-the-tools/ask-for-raw-output -->

人の側の落とし穴も 2 つある。1 つは、「壊れた」を聞いて、再現する前に環境の修理を始めること。もう 1 つは、長い作業の途中の報告を読まず、不満が増えていく様子を見逃すことだ。人の側の落とし穴の全体は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にある。

## 原因ごとの対処 {#routes-to-fixes}

切り分けた原因ごとに、対処の本体は次のページにある。この症状のページでは対処を繰り返さない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [サンドボックスで封じ込める](../enforce/sandboxing.md)<br>[設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md) |
| 散らかっている | [handoff 文書と document-and-clear](../context/handoff-documents.md)<br>[新しい会話を始めるタイミング](../context/when-to-start-fresh.md) |
| 確かめていない | [報告ではなく証拠を求める › 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動）](../verify/evidence-not-reports.md#tool-output)<br>[無人実行の結果を確かめる](../verify/checking-unattended-runs.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

似た症状もある。同じ確認を繰り返して進まないなら <!-- link:begin stuck-in-a-check-loop -->[同じ確認のループにはまる](stuck-in-a-check-loop.md)<!-- link:end -->、完了の報告が事実と違うなら <!-- link:begin claims-done-but-isnt -->[「完了」と言うが終わっていない](claims-done-but-isnt.md)<!-- link:end -->、長い会話で前提を忘れるなら <!-- link:begin forgets-in-long-chats -->[長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)<!-- link:end --> を引く。

## 判断例 {#example}

!!! example "判断例：長い作業の途中で「テストランナーが壊れた」と言われた"
    - **状況**：数時間続けているリファクタリングの途中で、Claude が「テストランナーが壊れている」と言って止まった。人が同じコマンドを実行するとテストは動いた。
    - **迷う候補**：環境を作り直して続けさせる。または、引き継ぎを書かせて新しい会話で再開する。
    - **選んだもの**：先に、根拠を生の出力で出させた。出力に拒否・時間切れを示す文言はなく、似た不満が過去にも何度か出ていた。そこで、引き継ぎを書かせて新しい会話で再開した。
    - **理由**：人の側で動くので環境の故障ではなく、失敗の文言に制限の手がかりもない。不満が増えている点は劣化の前兆と合う。環境の作り直しは、原因が見えないまま手間だけ増やす。出力に時間切れの文言があれば、見えていない制限を先に疑うのが筋になる。

## 予防：仕組みに移す {#prevention}

「壊れた」と言われてから動くより、見える状態を先に作る。

- 長い作業には進捗ログを用意し、人と Claude の両方に状況が見えるようにする。道具への不満が増える様子を早く拾える。設計は <!-- link:begin progress-logs-for-long-jobs -->[長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)<!-- link:end --> にある。
- 「壊れた」と判断する前に、実行したコマンドと生の出力を出す決まりを、依頼に書く。上の雛形を、そのまま依頼に足せる。
- 無人で走らせる作業は、終了コードと要約だけで決めず、出力と記録で確かめる。確かめ方は <!-- link:begin checking-unattended-runs -->[無人実行の結果を確かめる](../verify/checking-unattended-runs.md)<!-- link:end --> にある。
- フックや deny ルールで操作を止めているなら、止めるときに理由と代わりの手段を返す設計かを見直す。見直し方は <!-- link:begin lock-side-effects#reason-and-alternative -->[縛りすぎの害と見直し（止めすぎ・回り込み） › 止めるときに返すこと](../enforce/lock-side-effects.md#reason-and-alternative)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)
- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)

**関連**

- [長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)
- [/context で中身を見る](../context/inspect-context.md)
- [同じ確認のループにはまる](stuck-in-a-check-loop.md)
- [誤りを認めずに言い張る](insists-on-mistakes.md)
- [「完了」と言うが終わっていない](claims-done-but-isnt.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [縛りすぎの害と見直し（止めすぎ・回り込み）](../enforce/lock-side-effects.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
