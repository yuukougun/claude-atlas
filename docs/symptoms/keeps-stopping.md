---
id: keeps-stopping
title: 確認ばかりで進まない・途中で止まる
aliases: [途中で止まる, 提案だけで止まる, 毎回確認してくる]
type: symptom
field: symptoms
chapter: 返答と品質
order: 30
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 合っていない]
pitfalls: []
scenes: [開発]
summary: 確認ばかりで進まない・途中で止まる原因を、提案か実行かの伝え方、権限モード、モデルと effort の癖に分けて切り分け、最後まで進めさせる手を選ぶ。
signs:
  - {type: symptom, text: 提案だけで止まり、実行してくれない}
  - {type: symptom, text: 「続けますか」と毎回聞いてくる}
  - {type: symptom, text: 長い作業を途中でやめて報告してくる}
  - {type: symptom, text: 理由を言わずに止まっている}
wave: 1
prerequisites: [agent-loop]
related: [ask-for-outcomes, goal-until-done, permission-to-stop, what-auto-mode-stops#when-blocked, lock-side-effects, wrong-amount-of-approvals, does-more-than-asked, refused-or-blocked, six-causes]
routes:
  - {cause: 見えていない, to: [suggest-or-do, define-done]}
  - {cause: 合っていない, to: [effort-levels, model-quirks, permission-modes-overview]}
tracks: [effort, permission-modes, goal]
outdated_advice: [keep-going-dont-be-lazy]
sources: [api-docs-prompting-claude-sonnet-5-5, cc-docs-best-practices, cc-docs-goal, cc-docs-permission-modes, api-docs-effort, cc-docs-model-config, cc-changelog]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの振り分け先, anchor: routes}
  - {title: 判断例, anchor: example}
  - {title: 予防：仕組みに移す, anchor: prevent}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：止まった理由を、依頼の伝え方・完了の見え方・権限モード・effort とモデルの癖に切り分け、続けさせる手を選べる。
    - **いつ引くか**：提案だけで止まる、「続けますか」と毎回聞かれる、長い作業を途中で報告して終わる、理由が分からず止まるとき。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：途中で止まる・提案だけで止まる・毎回確認してくる
<!-- textlint-enable -->

確認ばかりで進まない・途中で止まる症状は、Claude が自分で聞いて止まる場合と、権限の確認や制限に止められる場合の両方を含む。まず、どちらで止まったのかを見分ける。そのうえで、原因を手間の小さい順に確かめる。止まるべきところで止まっているなら、それは直す対象ではない。

## よくある形 {#forms}

止まり方は 4 つに分かれる。原因は 1 つと決まらないので、診断では上から順に確かめる。

- **提案だけで止まる**：返答が「〜するとよいです」「〜しましょうか」で終わり、ファイルは変わっていない。
- **「続けますか」と毎回聞かれる**：複数の部分に分かれた作業で、1 つ終えるたびに「次へ進むか」と確認が返る。
- **長い作業を途中でやめて報告する**：終わりではない所で、ここまでの経過を報告して手が止まる。
- **理由を言わずに止まる**：返答も確認の画面もなく、動きだけが止まっている。

## 原因を安く確かめる順 {#diagnosis}

手間と費用の小さい順に 6 つ並べる。上から見て、当たったところで直し、同じ症状が続くときだけ次へ進む。原因の分け方の全体は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

1. **止まり方を見分ける**（手間：なし）
    - 見る：止まる直前の返答と画面。Claude が文で聞いているのか、権限の確認の画面が出て待っているのか、何も出ずに止まっているのか。
    - 確かめる：文で聞いているなら手順 2 へ進む。権限の確認が出ているなら手順 4 へ進む。確認の画面を見落としたまま「止まった」と思い込んでいる場合も、ここで見つかる。
    - 拒否や停止の表示が出ている、または何も出ずに止まっているときは、何かに止められた可能性がある。利用ポリシーの判定か、auto モード・フック・権限ルールの停止かの見分け方は <!-- link:begin refused-or-blocked#what-stopped -->[断られた・止められた › 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか）](refused-or-blocked.md#what-stopped)<!-- link:end --> にある。auto モードの分類器やフックに止められたときの見直しは <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> と <!-- link:begin lock-side-effects#reason-and-alternative -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めるときに返すこと（準備中）<!-- link:end --> にある。
    - 古い版の Claude Code には、auto モードの判定が返らないときに表示がおかしくなる不具合があり、止まった理由が出ないことがあった。その不具合は後の版で修正されている。理由が出ない停止は、Claude Code を更新してから見直す。修正の版は更新履歴（CHANGELOG）で確かめる。
    - Claude が懸念やテストの異常を述べて止まっているなら、止まったことは正しい。止まる権利を外さず、その懸念に答える。止まる条件の書き方は <!-- link:begin permission-to-stop#conditions -->止まって報告する権利を渡す › 止まって報告する条件を書く（準備中）<!-- link:end --> にある。
2. **依頼が提案にも読めるか**（原因：見えていない。手間：依頼を 1 回出し直す）
    - 見る：依頼の動詞。「検討して」「どう思う」「案を出して」「見て」は、提案で終えてよい依頼とも読める。
    - 確かめる：同じ依頼を「直して」「実装して、テストまで流して」のように動詞を変えて 1 回だけ出し直す。実行まで進むなら原因はここにある。動詞の書き分けは <!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](../prompting/suggest-or-do.md#verbs)<!-- link:end -->、既定をどちらに寄せるかは <!-- link:begin suggest-or-do#default -->[提案してほしいのか、実行してほしいのか › 既定の振る舞いを決める（すぐ実行するか、指示を待つか）](../prompting/suggest-or-do.md#default)<!-- link:end --> にある。
3. **完了と止まる条件が渡っているか**（原因：見えていない。手間：依頼に 1〜2 行足して出し直す）
    - 見る：依頼に「何が通れば終わりか」が書いてあるか。確かめる手段がないと、Claude は終わったように見えた所で止まる（<!-- link:begin agent-loop#why-stops -->[エージェントループと tool use › 確かめる手段がないと、終わったように見えたところで止まる](../basics/agent-loop.md#why-stops)<!-- link:end -->）。複数の部分に分かれた作業で 1 つ終えて聞いてくるときは、全体の終わりが見えていないことが多い。
    - 確かめる：終わりの条件（コマンドと、どう返れば終わりか）・変えてはならないもの・止まって報告する条件を足して出し直す。足すものは <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end -->、止まる条件は <!-- link:begin define-done#stop-and-report -->[「完了」を定義して渡す › 止まって報告する条件](../verify/define-done.md#stop-and-report)<!-- link:end --> にある。
4. **権限モードと確認の出方**（原因：合っていない。手間：設定を見る）
    - 見る：手元の権限モードと、確認が出る操作。権限モードは Claude Code の機能で、既定は版で変わってきた。手元の既定は <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](../cli/permission-modes-overview.md#defaults)<!-- link:end --> で確かめる。
    - 確かめる：確認が毎回同じ種類の操作で出るなら、Claude が聞いているのではなく、動かしているのはモードか権限ルールである。モードごとに何が確認なしで進むかは <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> にある。承認の数そのものを調整するかどうかは <!-- link:begin wrong-amount-of-approvals -->[承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)<!-- link:end --> で決める。
    - 確認を減らす方向へ動かす前に、止める側の守りを決める。auto モードは確認を減らす仕組みで、安全を保証しない（<!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end -->）。縛る規則の選び方は <!-- link:begin lock-side-effects#what-to-lock -->縛りすぎの害と見直し（止めすぎ・回り込み） › 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）（準備中）<!-- link:end --> にある。
5. **effort の段**（原因：合っていない。手間：段を 1 つ変えて出し直す）
    - 見る：今の effort の段。既定の段はモデルと面で違うので、手元の値は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end --> の表で確かめる。
    - 確かめる：1 段上げて同じ依頼を出し直し、確認の回数が減るかを見る。上げると考える時間と使用量が増えるので、効かなければ戻す。公式の指針は、低めの段（low・medium）の長い作業で、途中で確認を挟みやすくなると書く（2026-11-05 に確認。<!-- link:begin model-quirks#official-guidance -->モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向（準備中）<!-- link:end -->）。

    effort を見る場所は面で違う。

    === "アプリ"
        送信ボタンの横のモデルのメニューで、選べる段と今の段を見る。

    === "Claude Code"
        `/effort` で段を選ぶ。変え方の全体は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](../models/effort-levels.md#how-to-set)<!-- link:end --> にある。

6. **モデルの癖**（原因：合っていない。手間：記録を見る、または別のモデルで試す）
    - 見る：使っているモデルの公式のプロンプトの指針。Sonnet 向けの [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) は、low と medium の段の長い作業について、次の止まり方をすることがあると書く（2026-11-05 に確認）。計画の確認を挟む。自分で答えられる質問をする。複数の部分の 1 つ目で続けるかを聞く。
    - 確かめる：同じ依頼を、effort を上げて、または止まる条件つきの依頼で出し直す。止まる条件つきの依頼の型は、このページの「予防：仕組みに移す」の節に雛形がある。傾向はモデルの版で変わるので、暗記せず、自分の環境で観察して記録する（<!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end -->）。

人の側で起きやすい落とし穴もある。

- 「keep going」「最後までやり切れ」のような一言で済ませる。今のモデルには効きにくく、やりすぎの原因にもなる。台帳の行は <!-- link:begin outdated-advice-ledger#keep-going-dont-be-lazy -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#keep-going-dont-be-lazy)<!-- link:end --> にある。
- 席を外している間に承認の画面で待たれていて、戻ってから「止まった」と気づく。誰も見ていない実行では、承認を待つ前提の設計にしない。
- 止まるべき懸念まで「進めて」と押し切る。止まったことが正しかったかを、先に読んで判断する。

## 原因ごとの振り分け先 {#routes}

診断で当たった原因ごとに、対処は次のページが持つ。ここには対処の本体を書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)<br>[「完了」を定義して渡す](../verify/define-done.md) |
| 合っていない | [effort の段階と使い分け](../models/effort-levels.md)<br>モデル別の癖と、プロンプトの合わせ方（準備中）<br>[権限モードの選び方](../cli/permission-modes-overview.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：1 つ終えるたびに「次へ進みますか」と返る"
    - **状況**：Claude Code で 5 ファイルの移行を頼んだところ、1 ファイル終えるたびに「次のファイルへ進むか」という確認が返ってくる。権限の確認の画面は出ていない。
    - **迷う候補**：effort を 1 段上げる。依頼に終わりの条件と止まる条件を足して出し直す。
    - **選んだもの**：先に、終わりの条件（テストが成功する）と止まる条件（期待値を変えないと通らないとき）を足して出し直す。それでも続くときだけ effort を上げる。
    - **理由**：権限の確認が出ていないので原因は権限ではない。全体の終わりが書かれていないと、1 ファイル終えた所が区切りに見える。依頼を足す手は使用量を増やさず、effort を上げる手は使用量を増やす。安い順に試し、効いた手でやめる。

## 予防：仕組みに移す {#prevent}

毎回「進めて」と言い足すのをやめ、頼み方と仕組みに移す。

- **頼み方の型にする**：動詞（提案か実行か）・終わりの条件・止まって相談する条件を、依頼の型に入れておく。型の例を下に置く。完了の定義を含む依頼の型は <!-- link:begin define-done#templates -->[「完了」を定義して渡す › 完了の定義を含む依頼の雛形](../verify/define-done.md#templates)<!-- link:end --> にもある。
- **目的は成果で渡す**：目的と完了は測れる成果で渡し、着手点は具体的に書く。<!-- link:begin ask-for-outcomes#outcomes -->細かく指図するか、成果で頼むか › 成果で示すもの：目的と完了の条件（準備中）<!-- link:end --> を見る。
- **誰も見ていない実行は仕組みで続けさせる**：席を外す作業は、`/goal` で完了の条件を満たすまでターンを続けさせられる。判定役は会話に出た証拠しか読まないので、条件の書き方に注意する（<!-- link:begin goal-until-done#evaluator-reads-conversation -->[/goal（完了するまで続けさせる） › 判定役は会話しか読まない](../delegate/goal-until-done.md#evaluator-reads-conversation)<!-- link:end -->）。
- **止まる権利は残す**：止まるべきところで止まるのは正しい。止まる条件を書いたうえで、テストを書き換えられない仕組みと組み合わせる（<!-- link:begin permission-to-stop#with-structure -->止まって報告する権利を渡す › 書き換えられない仕組みと組み合わせる（準備中）<!-- link:end -->）。
- **確認を減らすなら先に守りを置く**：権限を緩める前に、止める側の規則を機械的に判定できるものへ絞る。

<!-- gen:begin snippet keeps-stopping/carry-through -->
<!-- textlint-disable -->

??? example "雛形：最後まで進めさせる依頼（止まる条件つき）"

    ```text
    次の作業を最後まで進めてください。

    - 範囲：<どこまでを頼むか。例：src/legacy/ の 5 ファイルの移行>。1 つ終えるたびに続けてよいかを聞かず、次の部分へ進んでください。
    - 終わりの条件：<確認のコマンド。例：npm test が成功する>。失敗したら原因を直して、成功するまで流し直してください。
    - 止まって相談する場合：<止まる条件。例：テストの期待値を変えないと通らない・削除の操作が要る・依頼にない仕様の判断が要る>。そのときだけ止まり、何で止まったかと、選択肢を 1 つ添えて報告してください。
    - 終わったら、変えたもの・流した確認・残りを短く報告してください。依頼にない機能やファイルは足さないでください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.139。

<!-- textlint-enable -->
<!-- gen:end snippet keeps-stopping/carry-through -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)

**次に読む**

- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- モデル別の癖と、プロンプトの合わせ方（準備中）
- [権限モードの選び方](../cli/permission-modes-overview.md)

**関連**

- 細かく指図するか、成果で頼むか（準備中）
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- 止まって報告する権利を渡す（準備中）
- [auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)
- 縛りすぎの害と見直し（止めすぎ・回り込み）（準備中）
- [承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)
- [頼んでいないことまでやる（過剰設計）](does-more-than-asked.md)
- [断られた・止められた](refused-or-blocked.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
