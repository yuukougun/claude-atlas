---
id: wrong-amount-of-approvals
title: 承認の確認が多すぎる・少なすぎる
aliases: [許可を何度も求められる, 確認なしで実行される]
type: symptom
field: symptoms
chapter: 安全と承認
order: 310
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [合っていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 承認の確認が多すぎて読まずに押す、または少なすぎて怖いときに、権限モード・権限ルール・サンドボックスのどれを調整するかを、任せる段階に合わせて決める。
signs:
  - {type: symptom, text: 確認ボタンを読まずに押している}
  - {type: symptom, text: 許可を求められる回数が多すぎて作業にならない}
  - {type: symptom, text: 確認なしで実行されて怖い}
wave: 1
prerequisites: []
related: [where-bypass-is-ok, protected-paths, settings-layers, keeps-stopping, deleted-something-important, parallel-fatigue, lock-side-effects, six-causes]
routes:
  - {cause: 合っていない, to: [permission-modes-overview, permission-rules, permission-modes-in-the-app]}
  - {cause: 境界がない, to: [sandboxing, what-auto-mode-stops]}
  - {cause: 預けすぎる, to: [approval-fatigue, default-safety-settings#by-stage]}
tracks: [permission-modes, auto-mode, permissions, sandbox]
outdated_advice: [yolo-skip-permissions, approve-everything-first]
sources: [cc-docs-permission-modes, cc-docs-permissions, cc-docs-sandboxing, cc-docs-best-practices, cc-changelog]
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
    - **何ができるか**：確認の多さと少なさの原因を、モード・ルール・境界・自分の読み方の順に切り分け、調整する先を選べる。
    - **いつ引くか**：確認を読まずに押している、確認が多すぎて作業にならない、確認なしで実行されて怖いとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：許可を何度も求められる・確認なしで実行される
<!-- textlint-enable -->

承認の確認が多すぎる・少なすぎる症状は、確認が出る回数と、いまの任せ方が合っていないときに起きる。多すぎると読まずに押すようになり、少なすぎると何が実行されたか分からない怖さが残る。どちらも、確認の数そのものより、何を確認なしで通し、何を止めるかの置き方の問題である。原因を手間の小さい順に確かめ、調整する先を選ぶ。

## よくある形 {#forms}

この症状は 3 つの形で出る。上の 2 つは確認が多すぎる側、最後の 1 つは少なすぎる側で、向きが逆である。診断の最初に、どちらかを見分ける。

- **確認を読まずに押している**：画面が出たら中身を見ずに許可している。確認が安全の仕組みとして働いていない。
- **回数が多すぎて作業にならない**：同じ種類の操作のたびに確認が出て、席を離れると作業が止まる。
- **確認なしで実行されて怖い**：許可を求められないまま、ファイルの変更やコマンドの実行が進む。

Claude が文章で「続けますか」と聞いて止まる症状は、権限の確認とは別である。そちらは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](keeps-stopping.md#diagnosis)<!-- link:end --> で切り分ける。

## 原因を安く確かめる順 {#diagnosis}

手間の小さい順に 5 つ並べる。上から見て、当たったところで直す。確認を減らす向きの調整は、任せる幅を広げることである。止める側の守りを先に決めてから減らす。原因の分け方の全体は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

1. **向きと出どころを見分ける**（手間：なし）
    - 見る：出ているのが権限の確認の画面か、Claude の文章での質問か。画面なら、どの操作で出ているか、毎回同じ種類か。確認なしで進んだなら、どの操作が通ったか。
    - 確かめる：Claude が文章で「続けますか」と聞いているだけなら、権限の問題ではない。<!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](keeps-stopping.md#diagnosis)<!-- link:end --> へ移る。並列で何本も回していて、確認が追いつかないだけなら <!-- link:begin parallel-fatigue#diagnosis -->[並列にしたら疲れた・レビューが追いつかない › 原因を安く確かめる順](parallel-fatigue.md#diagnosis)<!-- link:end --> で見る。
    - すでに消されたものがあるなら、この診断の前に <!-- link:begin deleted-something-important#recover -->[消してはいけないものを消された › まず戻す（復旧の手順）](deleted-something-important.md#recover)<!-- link:end --> を見て戻す。
2. **権限モードが合っているか**（原因：合っていない。手間：表示を見る）
    - 見る：いまの権限モード。確認が出る操作と出ない操作が、そのモードの表と合っているか。
    - 確かめる：安全な操作にまで確認が出るなら、モードが慎重すぎる。危ない操作が確認なしで通るなら、モードが緩い。モードごとの違いは <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> で見る。
    - 既定のモードは版で変わってきた。古い記事の「最初は毎回確認が出る」を前提にしない。経緯は <!-- link:begin outdated-advice-ledger#approve-everything-first -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#approve-everything-first)<!-- link:end -->、手元の既定は <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](../cli/permission-modes-overview.md#defaults)<!-- link:end --> で確かめる。毎回確かめる権限モードは、今の表示では <!-- name:begin default-to-manual-mode -->Manual（権限モード。設定の値は default のまま）<!-- name:end --> である。
    - `claude -p` と Agent SDK には確認の画面がない。モードを決めていないと、許可していない操作は実行されずに進まなくなる（公式の権限モードの文書で確認、2026-11-03）。
    - 起動のコマンドの alias・スクリプト・CI の設定に、確認をすべて外すモードの指定が残っていないかも見る。使ってよい場所は <!-- link:begin where-bypass-is-ok#why-isolate -->[bypassPermissions と無人の実行はどこで動かすか › なぜ隔離した環境だけか](../safety/where-bypass-is-ok.md#why-isolate)<!-- link:end --> にある。

    モードの見方は面で違う。

    === "アプリ"
        アプリは、確認なしに進める Auto と、毎回確かめる Manual を選べる。選び方と、読める範囲と行動できる範囲を同時に広げない置き方は <!-- link:begin permission-modes-in-the-app#two-conditions -->[アプリの権限モード（Auto と Manual）と安全 › 読める範囲と行動できる範囲を同時に広げない](../app/permission-modes-in-the-app.md#two-conditions)<!-- link:end --> にある。

    === "Claude Code"
        起動したときのモードは、画面の下の表示（auto mode on・manual mode on など）で分かる。切り替え方は <!-- link:begin permission-modes-overview#switch -->[権限モードの選び方 › 切り替え方](../cli/permission-modes-overview.md#switch)<!-- link:end --> にある。

3. **権限ルールと設定の層**（原因：合っていない。手間：設定を見る）
    - 見る：毎回同じ種類の確認が出る操作と、確認なしで通ってほしくない操作。設定に、それぞれのルールがあるか。
    - 確かめる：安全と分かっているコマンドは、範囲を絞った allow ルールで、毎回確かめさせずに済む。止めたい操作は deny ルールで止める。評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> にある。
    - 会話での頼みや CLAUDE.md の指示は、Claude が試みることを変えるが、許すことは変えない。確実に止めたい操作は、頼むのではなく deny ルールにする。
    - ルールを書いたのに効かないなら、当たらないパスの書き方と、子プロセスに効かない場面（<!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end -->）を疑う。読み込まれた層の確かめ方は <!-- link:begin settings-layers#verify -->設定ファイルの階層と優先順位 › 効いているかを確かめる（準備中）<!-- link:end --> にある。
4. **境界があるか**（原因：境界がない。手間：環境を見る）
    - 見る：確認なしで進む操作が、実際にどこまで及ぶか。auto モードの分類器が何を止め、サンドボックスが何を囲んでいるか。
    - 確かめる：auto モードは確認を減らす仕組みで、安全を保証しない。止めるものとすり抜けうるものは <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> にある。auto モードが止めた操作は、<!-- name:begin recently-denied-to-blocked -->Recently blocked（/permissions のタブ）<!-- name:end --> で見直せる。
    - サンドボックスは、コマンドの読み書きと通信を OS の層で囲む。囲える範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end -->、読み取りは <!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end --> で確かめる。
    - どのモードでも確認なしには書かせない場所は決まっている。保護される場所と、モードごとの扱いは <!-- link:begin protected-paths#protected -->消せない場所・触れない場所（protected paths） › 保護される場所と、モードごとの扱い（準備中）<!-- link:end --> で知る。足りない境界は、作業ディレクトリの外への読み書きを閉じる設定で足せる（<!-- link:begin protected-paths#outside-working-directory -->消せない場所・触れない場所（protected paths） › 作業ディレクトリの外への読み書きを閉じる（準備中）<!-- link:end -->）。
5. **人の側：確認を読めない状態を作っていないか**（落とし穴：預けすぎる。手間：自分の押し方を振り返る）
    - 見る：確認の画面を、中身を読んで押しているか。読めない速さで、同じ画面が続いていないか。
    - 確かめる：確認が多いと中身を読まなくなり、確認が仕組みとして働かなくなる。理由は <!-- link:begin approval-fatigue#why -->承認疲れ › なぜ読まなくなるか（準備中）<!-- link:end --> にある。読まずに押しているなら、確認を減らすか、残す確認を絞る。
    - 任せる段階ごとの足し方：<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end -->。

## 原因ごとの振り分け先 {#routes}

診断で当たった原因ごとに、対処は次のページが持つ。ここには対処の本体を書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 合っていない | [権限モードの選び方](../cli/permission-modes-overview.md)<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<br>[アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md) |
| 境界がない | [サンドボックスで封じ込める](../enforce/sandboxing.md)<br>[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md) |
| 預けすぎる | 承認疲れ（準備中）<br>[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：毎回同じテストのコマンドで確認が出て、読まずに押している"
    - **状況**：Claude Code でテストを流すたびに、同じコマンドの確認が出る。いつの間にか中身を見ずに許可している。
    - **迷う候補**：auto モードに切り替えて確認ごと減らす。そのコマンドだけを allow ルールに入れる。
    - **選んだもの**：先に、安全と分かっているテストのコマンドだけを、範囲を絞った allow ルールに入れる。auto モードは、サンドボックスと止める側の規則を置いてから検討する。
    - **理由**：出ている確認が同じ種類の安全な操作に偏っているので、原因はモードの全体ではなく、権限ルールがないことである。モードを丸ごと緩めると、ほかの操作の確認まで減る。ルールで減らす手は、減らす範囲を自分で決められる。

!!! example "判断例：確認なしでファイルが書き換わって怖い"
    - **状況**：auto モードで作業していたら、頼んでいない場所のファイルが書き換わっていた。確認は出なかった。
    - **迷う候補**：手動の確認に戻す。止めたい場所に deny ルールを足し、サンドボックスの範囲を見直す。
    - **選んだもの**：まず、書き換わった場所とモードを確かめ、戻す必要があれば戻す。そのうえで、止めたい場所を deny ルールに入れ、囲みを確かめる。手動に戻すかは、そのあとで決める。
    - **理由**：auto モードは確認を減らすが、安全を保証しない。手動に戻すだけでは、確認を読まずに押す問題が戻る。止めたいものを機械的に止める境界を足せば、確認を減らしたまま怖さを減らせる。

## 予防：仕組みに移す {#prevent}

確認の量を、その場の気分で変えるのをやめ、置き方を決めておく。

- **減らす前に守りを置く**：確認を減らすのは任せる幅を広げることなので、サンドボックスと deny ルールを先に置く。減らす順番は <!-- link:begin approval-fatigue#reduce-prompts -->承認疲れ › 確認を減らす順番（準備中）<!-- link:end --> にある。
- **残す確認を先に決める**：取り返しのつかない操作の確認は残し、そのほかを減らす。選び方は <!-- link:begin approval-fatigue#keep-prompts -->承認疲れ › 残す確認を選ぶ（準備中）<!-- link:end --> にある。
- **例外を許さない禁止は鍵にする**：頼みではなく deny ルールかフックで止める。縛る規則の選び方：<!-- link:begin lock-side-effects#what-to-lock -->縛りすぎの害と見直し（止めすぎ・回り込み） › 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）（準備中）<!-- link:end -->。止めるときに返すこと：<!-- link:begin lock-side-effects#reason-and-alternative -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めるときに返すこと（準備中）<!-- link:end -->。
- **確認をすべて外す運用は、隔離した環境に限る**：普段の作業では使わない。古くなった助言は <!-- link:begin outdated-advice-ledger#yolo-skip-permissions -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#yolo-skip-permissions)<!-- link:end --> にある。
- **止めた記録を見直す**：止めすぎや回り込みが出ていないかを、記録で確かめる。見直し方は <!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [権限モードの選び方](../cli/permission-modes-overview.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- 承認疲れ（準備中）
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)

**関連**

- [bypassPermissions と無人の実行はどこで動かすか](../safety/where-bypass-is-ok.md)
- 消せない場所・触れない場所（protected paths）（準備中）
- 設定ファイルの階層と優先順位（準備中）
- [確認ばかりで進まない・途中で止まる](keeps-stopping.md)
- [消してはいけないものを消された](deleted-something-important.md)
- [並列にしたら疲れた・レビューが追いつかない](parallel-fatigue.md)
- 縛りすぎの害と見直し（止めすぎ・回り込み）（準備中）
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
