---
id: where-it-runs
title: 実行場所の違い（クラウド・自分の PC・リモート操作）
nav_title: 実行場所の違い
aliases: [どこで動くか, クラウドで動く, 手元で動く]
type: concept
field: surfaces
chapter: 面の選び方
order: 20
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 縛る]
prevents: [見えていない, 境界がない]
pitfalls: []
scenes: [開発]
summary: 同じ依頼でも、クラウド・自分の PC・リモート操作のどこで動くかで、触れられるファイル・ブラウザ・設定・秘密と、PC を閉じても続くかが変わる理由が分かる。
signs:
  - {type: symptom, text: クラウドで動かすと、手元の設定が効いていない}
  - {type: symptom, text: アプリのタスクが手元のファイルを読めない}
  - {type: goal, text: PC を閉じても作業を進めておいてほしい}
  - {type: goal, text: 外出先から触る作業を、手元とクラウドのどちらで動かすか決めたい}
prerequisites: [choosing-a-surface]
related: [cloud-sessions-and-teleport#settings, tasks-and-schedules-in-the-app#where-it-runs, lethal-trifecta, sandboxing, protecting-secrets, settings-layers, loop-and-scheduling, claude-code-surfaces, browser-control, what-each-surface-cannot-do]
tracks: [cloud-sessions, remote-control, desktop-code, app-tasks]
outdated_advice: [code-on-the-web-remote]
sources: [cc-docs-claude-code-on-the-web, cc-docs-remote-control, cc-docs-desktop, hc-cowork-surfaces, hc-cowork-and-chat]
volatility: 高
sections:
  - {title: 三つの実行場所, anchor: three-locations}
  - {title: クラウドで動くときに届かないもの, anchor: what-cloud-cannot-reach}
  - {title: 手元で動かすときの境界, anchor: local-boundaries}
  - {title: リモート操作は実行を手元に残す, anchor: remote-control}
  - {title: 何に効くか, anchor: what-it-prevents}
  - {title: 選び方と確かめ方, anchor: how-to-choose}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：同じ依頼でも、動く場所で触れるものと、PC を閉じても続くかが変わる理由が分かる。
    - **いつ引くか**：クラウドで動かすと手元の設定が効かないとき。アプリのタスクが手元のファイルを読めないとき。PC を閉じても進めておきたいとき。
    - **前提**：<!-- link:begin choosing-a-surface -->[アプリ・Claude Code・API の選び方](choosing-a-surface.md)<!-- link:end -->

<!-- textlint-disable -->
別名：どこで動くか・クラウドで動く・手元で動く
<!-- textlint-enable -->

実行場所の違いは、Claude に何が見えて、何を縛れるかを決める。同じ依頼でも、Anthropic が管理するクラウドで動くか、自分の機械で動くかで、届くファイル・設定・秘密が変わる。このページは、その違いを 3 つの実行場所に分けて整理する。

## 三つの実行場所 {#three-locations}

実行場所とは、Claude が動いて、ファイルを読み、コマンドを走らせる機械のことである。クラウドの機械は手元とは別物なので、手元にあるものは自動では持ち込まれない。分かれ目は、実行がクラウドで起きるか、自分の機械で起きるかの 2 つだけである。リモート操作は、自分の機械で動くセッションに、別の端末から入る窓口を足す仕組みである。

| 実行場所 | 実行される機械 | PC を閉じたとき | 手元のファイル・設定 |
| --- | --- | --- | --- |
| クラウド（クラウドセッション、クラウドで動くアプリのタスク） | Anthropic が管理する環境 | 続く | 届かない。リポジトリに入れたものだけ |
| 自分の PC（ターミナルの Claude Code、Desktop の Code タブ、Desktop が開いている間のアプリのタスク） | 自分の機械 | 続かない。機械が動いていることが前提 | 届く |
| リモート操作（Remote Control） | 自分の機械。スマホやブラウザは操作する窓口 | 続かない。機械が動いていることが前提 | 届く |

アプリのタスクは、クラウドで動くものと、Desktop を開いた手元で動くものがある。どちらで動くかの今の扱いは、<!-- link:begin tasks-and-schedules-in-the-app#where-it-runs -->[タスクと定期タスク（Cowork） › どこで動くか（クラウドと Desktop）](../app/tasks-and-schedules-in-the-app.md#where-it-runs)<!-- link:end --> にある。Claude Code の側でクラウドへ送る手順は <!-- link:begin cloud-sessions-and-teleport#what-to-send -->クラウドセッションと teleport › クラウドに送ってよい作業（準備中）<!-- link:end --> にある。

API を自分のプログラムから呼ぶ場合は、そのプログラムを動かす機械を実行場所とみなす。この表の外にあり、選び方は <!-- link:begin choosing-a-surface#when-to-build-with-api -->[アプリ・Claude Code・API の選び方 › 自分のプログラムから呼ぶとき（API・SDK）](choosing-a-surface.md#when-to-build-with-api)<!-- link:end --> にある。

## クラウドで動くときに届かないもの {#what-cloud-cannot-reach}

クラウドで動くセッションは、手元の機械にあるものを読まない。届くのは、リポジトリに入っているものと、クラウドの環境に設定したものだけである。

=== "アプリ"

    - 手元のファイル、ブラウザの操作、computer use は、Desktop が開いていることが前提になる。クラウドで動くタスクには届かない。
    - ローカルの connectors（MCP）は Desktop 専用である。クラウドで動くタスクからは使えない。
    - モバイルからは、タスクの監視・質問への回答・方向修正・開始ができる。実行する場所が手元に変わるわけではない。

=== "Claude Code"

    - ユーザー設定、手元だけの設定、手元のプラグインは読まれない。手元の `~/.claude` に書いた規則や許可は、クラウドでは効かない。
    - リポジトリに入っていないファイルは見えない。計画のファイルや `CLAUDE.md` は、コミットして push してから送る。
    - ネットワークへのアクセス、環境変数、セットアップのスクリプトは、クラウドの環境の設定として別に用意する。
    - `ANTHROPIC_API_KEY` などの環境変数は、クラウドのセッションも Desktop も読まない。認証はサブスクリプションの OAuth が使われる。

効かせたい規則は、リポジトリの `CLAUDE.md` と `.claude/settings.json` に置く。設定がどの層から読まれるかは <!-- link:begin settings-layers#layers -->設定ファイルの階層と優先順位 › 層と優先順位（準備中）<!-- link:end --> で見られる。クラウドのセッションで読み込まれた層を同じ手順で確かめられるかは、まだ確かめていない。

PC を閉じても進めさせるのは、見ていない間に動かすことである。任せる幅が広がるので、縛りを先にリポジトリへ置く。秘密は逆向きにも注意が要る。手元だけにある秘密のファイルはクラウドに届かないが、リポジトリにコミットした秘密は届く。置き方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> を見る。

## 手元で動かすときの境界 {#local-boundaries}

手元で動くときは、ファイル・ブラウザ・設定が全部届く。その分、届く範囲を自分で囲う必要がある。

- ターミナルの Claude Code は、コマンドの読み取りが既定で広い。秘密のある場所は明示して塞ぐ。囲み方は <!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end --> にある。
- Desktop の computer use は、Claude とアプリの間にサンドボックスがない。アプリごとに許可を求められる。使う順は、コネクタ、ブラウザ、画面の操作の順である。順の理由は <!-- link:begin browser-control#which-to-use -->Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ（準備中）<!-- link:end --> にある。
- 信頼できない入力を読める状態と、被害につながる行動もできる状態が重なると、仕込まれた指示が被害になる。片方を外せば攻撃は難しくなる。組み立て方は <!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end --> にある。
- 手元で動くアプリのタスクには、Claude 専用の作業フォルダを作る。送信や購入のような取り消しにくい操作は、定期タスクにしない。

手元で動く作業は、Desktop や機械が動いている間しか進まない。PC を閉じても進めたい作業は、クラウドに寄せるか、続きを後で自分でやる前提にする。

## リモート操作は実行を手元に残す {#remote-control}

リモート操作（Remote Control）は、手元の機械で動くセッションを、claude.ai/code やモバイルアプリから操作する仕組みである。実行とファイルは手元の機械に残り、別の端末は窓口になる。クラウドに移るわけではない。

- 手元の設定、手元のファイル、手元のプラグインは、そのまま使われる。
- 手元の機械が止まると、セッションも続かない。
- 名前が似た `--remote-control` と、クラウドへ送る旧フラグの `--remote` は別の機能である。

外出先から状況を見たり、返事をしたりしたいときは、リモート操作が合う。使い方は Claude Code の分野の別のページにある。

## 何に効くか {#what-it-prevents}

実行場所を意識すると、次の 2 つの原因を防げる。

- **見えていない**（原理は「見せる」）：クラウドでは、手元の設定やファイルが Claude に見えない。見えている前提で頼むと、手元と違う結果になる。届くものを先に確かめ、届かないものは依頼かリポジトリに書いて見せる。
- **境界がない**（原理は「縛る」）：手元の縛りは、クラウドに届かない。手元の computer use には、サンドボックスの囲いがない。実行場所ごとに、効く縛りと効かない縛りが違う。縛りは、実行する場所に届く形で置く。

## 選び方と確かめ方 {#how-to-choose}

選ぶときは、触れる必要のあるものから決める。手元のファイル・ブラウザ・設定が要るなら手元かリモート操作、PC を閉じても進めたいならクラウドである。

!!! example "判断例：外出先から触る作業"
    - **状況**：移動中に、手元の PC のリポジトリで進めている修正の続きをスマホから見て、必要なら指示を足したい。
    - **迷う候補**：リモート操作で手元のセッションを操る。作業をクラウドのセッションに送って、PC を閉じる。
    - **選んだもの**：リモート操作。
    - **理由**：修正は、コミットしていないファイルと手元の設定に依存している。クラウドに送ると、それらが届かない。PC を家で開けたままにできるなら、実行を手元に残すほうが安全である。
    - **別の状況**：計画をリポジトリに入れてあり、手元の設定に頼らず、PC を閉じて待ちたいなら、クラウドで筋が通る。

クラウドに送る依頼は、届くものと止まる条件を書いて出す。

<!-- gen:begin snippet where-it-runs/cloud-handoff -->
<!-- textlint-disable -->

??? example "雛形：クラウドに送る依頼に、届くものと止まる条件を書く"

    ```markdown
    `docs/migration-plan.md` に書いた移行計画を、手順 1 から順に実行してほしい。この作業は手元の端末ではなく、クラウドのセッションで走る。

    - 前提：読んでよいのは、このリポジトリにコミットされているファイルだけ。手元のユーザー設定、手元だけの設定、手元のファイルは、このセッションには届かない。
    - 守ること：守ってほしい規則は `CLAUDE.md` と `.claude/settings.json` に書いてある。届いていない規則に頼らず、迷ったらこの 2 つを読み直す。
    - 終わりの条件：`npm test` が全部通ること。通ったら、変更をブランチにコミットして、プルリクエストの説明に実行したコマンドと結果を書く。
    - 止まって報告する条件：計画にない秘密や認証情報が要ると分かったとき。自分で探したり作ったりせず、何が要るかを書いて止まる。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.51。

<!-- textlint-enable -->
<!-- gen:end snippet where-it-runs/cloud-handoff -->

クラウドで動かしたら、結果を手元の結果と突き合わせる。規則が効いたか、テストを走らせたコマンドが出ているかを見る。

古い手順書には、クラウドで動かす機能を Claude Code on the web と呼び、ターミナルから始めるフラグを `--remote` と書いたものがある。機能の今の名前は <!-- name:begin web-to-cloud-sessions -->クラウドセッション（cloud sessions）<!-- name:end --> で、ターミナルのフラグは <!-- name:begin remote-to-cloud-flag -->--cloud<!-- name:end --> である。手順書の `--remote` を替えるときは、別の機能の `--remote-control` まで替えない。台帳の行は <!-- link:begin outdated-advice-ledger#code-on-the-web-remote -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#code-on-the-web-remote)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **クラウドは手元の環境のコピーではない**：手元の設定やファイルは複製されない。リポジトリに入れたものと、クラウドの環境の設定だけが届く。
- **リモート操作はクラウドで動く機能ではない**：実行は手元に残る。PC を閉じても続く機能と取り違えない。
- **アプリのタスクが、いつも手元で動くとは限らない**：クラウドで動くタスクは、手元のファイルやブラウザの操作に届かない。手元のものが要る作業は、Desktop を開いて手元で動かす。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Continue local sessions from any device with Remote Control](https://code.claude.com/docs/en/remote-control)：Anthropic・英語・確認日 2026-11-04
- [Desktop application](https://code.claude.com/docs/en/desktop)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [アプリ・Claude Code・API の選び方](choosing-a-surface.md)

**次に読む**

- Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル）（準備中）
- Claude in Chrome と computer use（ブラウザと画面の操作）（準備中）
- クラウドセッションと teleport（準備中）

**関連**

- クラウドセッションと teleport › 手元の設定との違い（準備中）
- [タスクと定期タスク（Cowork） › どこで動くか（クラウドと Desktop）](../app/tasks-and-schedules-in-the-app.md#where-it-runs)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- 設定ファイルの階層と優先順位（準備中）
- /loop と定期実行の方式（準備中）
- 面ごとにできないこと（早見表）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
