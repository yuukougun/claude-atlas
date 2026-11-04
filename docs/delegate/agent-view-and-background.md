---
id: agent-view-and-background
title: agent view と背景セッション
aliases: [claude agents, background sessions, claude --bg, /background, cross-session messaging]
type: feature
field: delegate
chapter: 並べる
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 見張らなくてよい独立した作業を背景のセッションに投入し、一覧で状態を見て、要るときだけ返事をできる。セッションごとに利用枠を使うので、同時に動かす数を決めてから投入する。
signs:
  - {type: goal, text: いくつかの作業を投げておいて、後でまとめて確かめたい}
  - {type: symptom, text: 背景で動かしたセッションがどうなったか分からない}
prerequisites: [choosing-parallel-modes, what-auto-mode-stops]
related: [parallel-with-worktrees, humans-set-the-parallel-limit, pairing-and-delegating, progress-logs-for-long-jobs, checking-unattended-runs, completion-notifications, control-from-phone, cloud-sessions-and-teleport, parallel-and-loop-costs]
tracks: [agent-view, cross-session-messaging]
outdated_advice: [tmux-agent-orgs]
sources: [cc-docs-agent-view, cc-docs-agents, cc-docs-cross-session-messaging, cc-docs-tools-reference, cc-docs-agent-teams]
volatility: 高
sections:
  - {title: 向く作業と向かない作業, anchor: what-fits}
  - {title: 投げる前に決める守り, anchor: guards-first}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 雛形：背景に投げる依頼, anchor: templates}
  - {title: ほかのセッションに知らせる（cross-session messaging）, anchor: cross-session-messaging}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：見張らなくてよい独立した作業を背景のセッションに投げ、一覧で状態を見て、要るときだけ返事ができる。
    - **いつ引くか**：いくつかの作業を投げておいて、後でまとめて確かめたいとき。背景で動かしたセッションがどうなったか分からないとき。
    - **止められるもの**：状態を見て返事をする画面であり、作業の中身は縛らない。縛りは権限とフックで先に置く。
    - **前提**：<!-- link:begin choosing-parallel-modes -->[並列の方式の選び方](choosing-parallel-modes.md)<!-- link:end -->、<!-- link:begin what-auto-mode-stops -->[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)<!-- link:end -->

<!-- textlint-disable -->
別名：claude agents・background sessions・claude --bg・/background・cross-session messaging
<!-- textlint-enable -->

agent view と背景セッションは、見張らなくてよい独立した作業を背景で走らせ、一覧で状態を見て、要るときだけ返事をするための仕組みである。Claude が自分のほかのセッションにメッセージを送る cross-session messaging も、このページで扱う。agent view の成熟度は <!-- gen:begin feature agent-view/maturity -->research preview<!-- gen:end feature agent-view/maturity --> で、画面やキーは変わりうる。そのため操作の手順は最小限にし、使いどころと注意を中心に書く。

## 向く作業と向かない作業 {#what-fits}

背景に向くのは、互いに独立していて、途中で見張らなくても終わりの形が決められる作業である。公式の文書は、バグの修正、PR のレビュー、調査を例に挙げる。投げっぱなしにすると、終わった結果を誰も確かめない状態になりやすい。そこで「終わりの形」を依頼に書き、戻ってきたときに確かめる前提で投げる。

| 作業 | 背景に向くか | 理由 |
| --- | --- | --- |
| 独立したバグの修正 | 向く | 完了の条件をテストで書ける。 |
| PR のレビュー・調査 | 向く | 成果が文章で、読めば確かめられる。 |
| 同じファイルを触る複数の変更 | 向かない | 互いの結果に依存し、衝突の確認が戻ってから集中する。 |
| 方針が決まっていない設計 | 向かない | 途中の判断が多く、返事待ちで止まり続ける。 |
| 手元で見ながら進めたい作業 | 向かない | 伴走のほうが速い。<!-- link:begin pairing-and-delegating -->伴走と委託（準備中）<!-- link:end -->を引く。 |

!!! example "判断例：3 件の作業を投げる"
    - **状況**：朝のうちに、独立したバグ 2 件と、まだ方針の決まっていないリファクタリング 1 件を片付けたい。
    - **迷う候補**：3 件とも背景に投げる。バグ 2 件だけ投げて、リファクタリングは手元で進める。
    - **選んだもの**：バグ 2 件だけを背景に投げ、リファクタリングは手元で進める。
    - **理由**：リファクタリングは途中の判断が多く、背景に置くと返事待ちで止まるだけになる。どちらの候補も筋は通るが、確かめる人の手間は本数で増えるので、返事待ちが確実に出る作業を背景に置くと割に合わない。

## 投げる前に決める守り {#guards-first}

背景へ投げる前に、同時に動かす数、完了の確かめ方、権限の縛りの 3 つを決める。任せる幅を広げると、確かめる側の手間が先に増えるからである。

- **同時に動かす数**：agent view のセッションは、それぞれ別に利用枠を使う。本数の決め方は <!-- link:begin humans-set-the-parallel-limit#why-human-side -->[並列の上限は人間が決める › 上限が人の側にある理由](humans-set-the-parallel-limit.md#why-human-side)<!-- link:end --> を、費用の膨らみ方は <!-- link:begin parallel-and-loop-costs#multiplication -->[並列・ループ・workflows のコスト › 費用が膨らむ掛け算](../cost/parallel-and-loop-costs.md#multiplication)<!-- link:end --> を参照する。
- **完了の確かめ方**：終了したという表示だけで済ませず、出力と差分で確かめる。手順は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある。
- **権限の縛り**：背景のセッションは見ている人がいない。auto モードが何を止め、何をすり抜けさせるかを <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> で確かめてから投げる。

公式の文書は、変更を伴うセッションが、ブランチに push し、ドラフトの PR を開くことがあると書く。また main や master への push、強制 push、マージはしないとも書く（確認 2026-11-05）。それでも最後の判断は人に置く。

## 最小の使い方 {#minimal}

=== "Claude Code"

    シェルから `claude agents` を実行すると、背景のセッションの一覧が開く。下部の入力欄に依頼を書いて決定すると、依頼ごとに別のセッションが始まる。シェルから 1 件だけ投げるなら `claude --bg "<依頼>"` を使う。

    一覧では、各セッションが作業中、返事待ち、待機、完了、失敗、停止のどれかで出る。見るのは返事待ちと失敗から始める。返事が要るセッションは、一覧から中身をのぞいて返事を書ける。会話の全体を見るときは、そのセッションに入る。出ても、セッションは止まらない。

    投入したセッションは、ファイルを編集する前に `.claude/worktrees/` の下の worktree に移る。worktree の考え方と片付けは <!-- link:begin parallel-with-worktrees#cleanup -->[git worktree で並列にする › 片付けと残すもの](parallel-with-worktrees.md#cleanup)<!-- link:end --> にある。いま開いている会話を背景に移すには `/background` を使う。キーの割り当てと細かい操作は変わりうるので、公式の文書で確かめる。

## 雛形：背景に投げる依頼 {#templates}

背景のセッションは、途中で聞き返されないことを前提に動く。依頼に、範囲、完了の条件、止まる条件、終わりの報告の形を先に書いておく。

<!-- gen:begin snippet agent-view-and-background/background-task-prompt -->
<!-- textlint-disable -->

??? example "雛形：背景に投げる依頼の型"

    ```text
    次の作業を、私が見ていない前提で進めてください。

    目的：<何を直す・調べるか。1つだけ>
    触ってよい範囲：<ディレクトリやファイル>。それ以外は読むだけにする
    完了の条件：<確認のコマンド> が通り、変更の要約を書き終えている
    止まる条件：私の判断が要るときは、選択肢と推奨案を 1 つの質問にまとめて待つ。権限の確認が出たときも同じ
    終わったら：変えたファイル、実行した確認とその結果、残った疑問を、この順で書く
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.139。

<!-- textlint-enable -->
<!-- gen:end snippet agent-view-and-background/background-task-prompt -->

終わりの報告の形を依頼に書いておくと、一覧で完了したセッションへ戻ったとき、何を確かめるかが決まっている。

## ほかのセッションに知らせる（cross-session messaging） {#cross-session-messaging}

cross-session messaging は、1 つのセッションの Claude が、自分のほかのセッションにメッセージを届ける機能である。人がターミナルの間で文章を写す代わりになる。背景で動く作業の発見や状態を、見ているセッションへ伝えるときに使う。

- **送るもの**：Claude が書いた文章だけである。会話の履歴やファイルは送らない。会話ごと移したいなら、そのセッションを再開する。
- **送り方**：Claude が `ListAgents` で相手を探し、`SendMessage` で送る。人はこの道具を直接呼ばない。「別のターミナルのセッションに、移行が終わったか聞いて」のように頼む。`/list-agents`（別名 `/peers`）で、届く相手の一覧を見られる。
- **届く範囲**：同じ機械のセッションには、Anthropic のサーバを通さずに届く。別の機械やクラウドのセッションは、Claude のサブスクリプションで認証し、Remote Control につながっているときに届く。ほかの認証では同じ機械の中だけである。
- **待機（idle）の知らせ**：同じ機械のほかのセッションが次に待機（idle）になったとき、一度だけ知らせてもらうよう頼める。長い作業の終わりを待つときに使う。必要な版は公式の文書で確かめる。画面の通知やフックで知らせる流儀との使い分けは <!-- link:begin completion-notifications#when-to-notify -->終わったら知らせてもらう › 知らせるか、時刻を決めて見るか（準備中）<!-- link:end --> にある。

受け取る側には 3 つの扱いがある。設定 `crossSessionInbound` は、届いたメッセージを渡す（accept）、保留して通知だけ出す（hold）、捨てる（refuse）から選ぶ。何も設定しないときの扱いは、両方のセッションの権限モードで決まる。たとえば、権限の確認を飛ばすモードで動くセッションが受け取るメッセージは、既定では保留され、人が承認すると渡る。

メッセージは人の承認にならず、権限の確認の代わりにもならない。受け取ったセッションは、設定や `CLAUDE.md` を、ほかのセッションに頼まれたからといって変えない。メッセージの中の `/compact` のような文字列も、命令としては実行されない。機能は、公式の文書が求める版以上で、何も設定せずに使える（確認 2026-11-05）。

## 効かない場面・落とし穴 {#pitfalls}

- **背景にしたセッションは worktree に移らない**：一覧から投入したセッションは worktree に移る。しかし、`/background` や一覧への移動で背景にした既存のセッションは、元の場所で編集を続ける。Git の外では、セッションどうしの分離もない。同じファイルを触る作業を混ぜない。
- **一覧から消すと worktree も消える**：公式の文書によれば、agent view で消すと、未コミットの変更があっても worktree ごと消える。未 push のコミットがあるときは消せない。消す前にコミットして push する（確認 2026-11-05）。
- **手元を閉じても続くが、機械の電源を切ると止まる**：背景のセッションは、端末を閉じても動き続ける。ただ、機械を止めると止まる。しばらく誰も見ていない idle のセッションも、止められることがある。会話は保存され、次に開くと再開する。手元を閉じても続けたいなら <!-- link:begin cloud-sessions-and-teleport#what-to-send -->[クラウドセッションと teleport › クラウドに送ってよい作業](../cli/cloud-sessions-and-teleport.md#what-to-send)<!-- link:end --> を使う。
- **同時に動かす数は、利用枠と確かめる手間の両方で効く**：本数を増やした分だけ、返事待ちと完了の確認が溜まる。一覧は状態を見せるが、結果が正しいかは見せない。確かめは <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> の流儀で行う。
- **メッセージは確実な連絡路ではない**：受け取る側の設定しだいで、保留されることや捨てられることがある。重要な指示や承認を、メッセージだけに載せない。指示はリポジトリのファイルに書く。

## 比べる相手 {#compare}

このページの 2 つの機能の属性は、次の表のとおりである。

<!-- gen:begin compare 成熟度 入った版 -->
<!-- textlint-disable -->

| 機能 | 成熟度 | 入った版 |
| --- | --- | --- |
| [agent view](agent-view-and-background.md) | research preview | 2.1.139（2026-05-11） |
| [セッションの間のメッセージ](agent-view-and-background.md) | GA | 2.1.224（2026-08-07） |

<!-- textlint-enable -->
<!-- gen:end compare 成熟度 入った版 -->

並列の方式のうち、背景のセッションを選ぶ基準は <!-- link:begin choosing-parallel-modes#compare -->[並列の方式の選び方 › 方式の比較](choosing-parallel-modes.md#compare)<!-- link:end --> にある。ほかの方式との組み合わせ方は <!-- link:begin choosing-parallel-modes#combine -->[並列の方式の選び方 › 組み合わせ方](choosing-parallel-modes.md#combine)<!-- link:end --> を引く。スマホから見て承認するなら <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）（準備中）<!-- link:end --> を、長い作業の途中経過を残すなら <!-- link:begin progress-logs-for-long-jobs -->長時間ジョブの進捗ログを設計する（準備中）<!-- link:end --> を使う。

## 古くなった助言 {#outdated}

tmux で複数の Claude Code を並べ、手で連絡させる自作の組織は、今は公式の仕組みに置き換わりつつある。背景のセッションをまとめて見るなら agent view を使う。リードがチームメイトに仕事を振って調整するなら、実験的な機能のエージェントチームがある。どちらも使う量が増える。まず、サブエージェントやセッションの間のメッセージで足りないかを確かめる。台帳の行は <!-- link:begin outdated-advice-ledger#tmux-agent-orgs -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#tmux-agent-orgs)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [並列の方式の選び方](choosing-parallel-modes.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)

**関連**

- [git worktree で並列にする](parallel-with-worktrees.md)
- [並列の上限は人間が決める](humans-set-the-parallel-limit.md)
- 伴走と委託（準備中）
- 長時間ジョブの進捗ログを設計する（準備中）
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- 終わったら知らせてもらう（準備中）
- スマホから操作する（Remote Control）（準備中）
- [クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Manage multiple agents with agent view](https://code.claude.com/docs/en/agent-view)：Anthropic・英語・確認日 2026-11-04
- [Run agents in parallel](https://code.claude.com/docs/en/agents)：Anthropic・英語・確認日 2026-11-04
- [Message your other Claude Code sessions](https://code.claude.com/docs/en/cross-session-messaging)：Anthropic・英語・確認日 2026-11-04
- [Tools reference](https://code.claude.com/docs/en/tools-reference)：Anthropic・英語・確認日 2026-11-04
- [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
