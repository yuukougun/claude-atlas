---
id: where-bypass-is-ok
title: bypassPermissions と無人の実行はどこで動かすか
aliases: [--dangerously-skip-permissions, YOLO モード, 全許可モード, 使い捨ての環境, bypassPermissions はどこで使ってよいか, devcontainer, Docker, コンテナ]
type: concept
field: safety
chapter: 既定と承認
order: 30
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: 確認をすべて外すモードや無人の実行を、隔離した使い捨ての環境だけで動かす理由と、その環境の条件が分かる。確認を減らすだけなら、先に auto モードとサンドボックスを使う。
signs:
  - {type: goal, text: --dangerously-skip-permissions で、確認なしに走らせたい}
  - {type: goal, text: コンテナの中で Claude Code を無人で動かしたい}
  - {type: situation, text: 夜間や CI で、人が見ていない間に Claude を動かしている}
prerequisites: [what-auto-mode-stops, sandboxing]
related: [headless-basics, five-questions-before-delegating, default-safety-settings#by-stage, permission-modes-overview, managed-settings-enforcement, protected-paths, before-opening-unknown-repos, github-actions-with-claude, cloud-sessions-and-teleport, checking-unattended-runs, destructive-commands, cloud-schedules]
tracks: [permission-modes, headless, cloud-sessions]
outdated_advice: [yolo-skip-permissions]
sources: [cc-docs-permission-modes, cc-docs-permissions, cc-docs-security, cc-docs-claude-code-on-the-web, cc-docs-headless]
volatility: 中
sections:
  - {title: なぜ隔離した環境だけか, anchor: why-isolate}
  - {title: 使い捨ての環境の条件, anchor: requirements}
  - {title: 書き込みを作業ディレクトリに閉じても代わりにならない, anchor: not-a-substitute}
  - {title: 無人の夜間実行をどこで動かすかの判断例, anchor: decision}
  - {title: どの原理・どの原因に効くか, anchor: what-it-prevents}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：確認をすべて外すモードや無人の実行を、隔離した使い捨ての環境だけで動かす理由と、その環境の条件が分かる。
    - **いつ引くか**：`--dangerously-skip-permissions` で確認なしに走らせたいとき、コンテナの中で Claude Code を無人で動かしたいとき、夜間や CI で人が見ていない間に動かしているとき。
    - **前提**：<!-- link:begin what-auto-mode-stops -->[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)<!-- link:end -->・<!-- link:begin sandboxing -->[サンドボックスで封じ込める](../enforce/sandboxing.md)<!-- link:end -->

<!-- textlint-disable -->
別名：--dangerously-skip-permissions・YOLO モード・全許可モード・使い捨ての環境・bypassPermissions はどこで使ってよいか・devcontainer・Docker・コンテナ
<!-- textlint-enable -->

bypassPermissions は、確認をすべて外して Claude Code に操作を通すモードである。このページは、そのモードと、確認に答える人がいない無人の実行を、どこで動かしてよいかを扱う。答えは、隔離した使い捨ての環境の中だけである。確認を減らしたいだけなら、先に auto モードとサンドボックスを使う。

## なぜ隔離した環境だけか {#why-isolate}

bypassPermissions を隔離した使い捨ての環境だけで使うのは、このモードが確認という内側の止め手を全部取り除くからである。公式の文書は、このモードは prompt injection と意図しない操作の両方に対して守らない、と警告する。使うのは、インターネットから切り離したコンテナや VM のような環境だけにとどめる。

通常の権限モードでは、危うい操作の前に人が確認で止められる。bypassPermissions ではその層が消える。読み込んだファイルに紛れた指示に従っても、勘違いでホームの下を消しても、止める仕組みがない。無人の実行も同じ状態になる。確認が出ても答える人がいないので、確認を外すか、全部拒むかの二択に寄りやすい。外した場合の被害は、環境の外に届くかどうかで決まる。

だから守りを内側から外側へ移す。確認で止める代わりに、壊れても失うものがない場所へ閉じ込める。環境ごと捨てられるなら、最悪の被害はその環境の中で終わる。

確認を外して任せる幅を広げる前に、先に使える守りがある。確認を減らすだけなら、まず auto モードとサンドボックスで足りるかを見る。

- auto モードは確認を減らす仕組みで、安全を保証しない。止めるもの、すり抜けうるものは <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> で確かめる。
- サンドボックスは、Claude が動かすコマンドの読み書きと通信を OS の層で囲う。囲えるもの、囲えないものは <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> にある。
- 取り返しのつかない削除や書き換えが起きる経路は <!-- link:begin destructive-commands#how-it-happens -->[消されたくないもの（破壊的コマンド） › 消える経路](destructive-commands.md#how-it-happens)<!-- link:end --> にある。巻き戻しで戻らないものは <!-- link:begin destructive-commands#not-recoverable -->[消されたくないもの（破壊的コマンド） › 巻き戻しで戻らないもの](destructive-commands.md#not-recoverable)<!-- link:end --> にある。

人が見ていない実行ほど、確認を外す前に環境を囲う。段階ごとの既定は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)<!-- link:end --> を正本とし、ここでは繰り返さない。無人で走らせる前に答える問いは <!-- link:begin five-questions-before-delegating#five-questions -->[任せ方の段階と、無人で走らせる前の五つの問い › 無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md#five-questions)<!-- link:end --> にある。

## 使い捨ての環境の条件 {#requirements}

使い捨ての環境とは、Claude に何をされても、壊れたら捨てて作り直すだけで済む環境である。条件は 2 種類に分けて読む。公式の文書が述べるものと、この辞典の推奨である。

公式の文書が述べる条件は次のとおりである。

- **隔離したコンテナか VM である**：ホストの端末やふだんの作業環境では使わない。
- **外への通信を遮断する**：インターネットを遮断した環境でのみ使うよう、公式は述べる。通信を開ける場合の扱いは次の「この辞典の推奨」に回す。
- **root や sudo で起動しない**：公式の文書は、root や sudo ではこのモードが起動を拒否する、と述べる。一般ユーザーで動かす。

この辞典の推奨として、次の条件を足す。公式の文書の記述ではなく、「縛る」原理からの推論である（推論・実践例なし）。

- **秘密を入れない**：ホームの鍵、本物の `.env`、広い権限のトークンを環境へ渡さない。渡すなら、その作業だけの最小の権限で、捨てても困らないものにする。
- **届く範囲をその作業のコピーに限る**：ホストのホームやほかのリポジトリ、ホストを操作できる入口を、環境から見えるようにしない。
- **通信を開けるなら宛先を絞る**：パッケージの取得など開けざるをえないときも、送り先を必要な分だけにする。
- **結果は差分で取り出し、人が見てから取り込む**：環境の外へ出すのは、ブランチや差分のような確かめられる形だけにする。確かめ方は <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> で、最後の判断を人に置く考え方は <!-- link:begin checking-unattended-runs#final-decision -->[無人実行の結果を確かめる › 最後の判断を人に置く](../verify/checking-unattended-runs.md#final-decision)<!-- link:end --> にある。
- **止まる上限を決める**：無人の実行は、ターンと費用の上限を明示して渡す。上限は <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end --> にある。

最初から条件がそろっている例が、クラウドセッションである。Anthropic がホストする隔離した VM で動き、GitHub の資格情報は VM に入らず proxy 側で付与される。ブランチの削除やタグの push は拒否され、操作は監査ログに残る（公式の Security の文書、2026-11-04 に確認した範囲）。名前は <!-- name:begin web-to-cloud-sessions -->クラウドセッション（cloud sessions）<!-- name:end --> である。送ってよい作業と手元の設定との違いは <!-- link:begin cloud-sessions-and-teleport#what-to-send -->[クラウドセッションと teleport › クラウドに送ってよい作業](../cli/cloud-sessions-and-teleport.md#what-to-send)<!-- link:end --> と <!-- link:begin cloud-sessions-and-teleport#settings -->[クラウドセッションと teleport › 手元の設定との違い](../cli/cloud-sessions-and-teleport.md#settings)<!-- link:end --> にある。

自分で用意するコンテナ（Docker・devcontainer）は、条件を自分で満たす必要がある。コンテナと OS のサンドボックスの使い分けは <!-- link:begin sandboxing#containers -->[サンドボックスで封じ込める › コンテナ（Docker・devcontainer）との使い分け](../enforce/sandboxing.md#containers)<!-- link:end --> にある。GitHub Actions で動かすときの鍵と権限は <!-- link:begin github-actions-with-claude#secrets-and-permissions -->GitHub Actions と @claude › 鍵と権限（準備中）<!-- link:end --> にある。知らないフォルダを非対話で動かすと信頼の確認が出ないので、隔離して動かす。理由は <!-- link:begin before-opening-unknown-repos#headless -->[知らないリポジトリを開く前に › 非対話の実行では確認が出ない](before-opening-unknown-repos.md#headless)<!-- link:end --> にある。

起動前の確認の一覧を、雛形として用意した。環境を作った後、動かす前に使う。

<!-- gen:begin snippet where-bypass-is-ok/disposable-checklist -->
<!-- textlint-disable -->

??? example "雛形：bypassPermissions を使う前の確認の一覧（使い捨ての環境）"

    ```markdown
    bypassPermissions を使う前の確認（使い捨ての環境）

    [ ] 隔離したコンテナか VM の中で動かす（手元の端末では動かさない）
    [ ] root や sudo ではなく、一般ユーザーで起動する
    [ ] 外への通信を遮断した。開けるなら、宛先を必要な分だけに絞った
    [ ] ホームの鍵、本物の .env、広い権限のトークンを渡していない
    [ ] 環境から見えるのは、この作業のコピーだけ（ホストのほかの場所は見えない）
    [ ] ターンと費用の上限を決めた
    [ ] 壊れたら捨てて作り直せる。結果はブランチや差分で取り出し、人が見てから取り込む
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet where-bypass-is-ok/disposable-checklist -->

## 書き込みを作業ディレクトリに閉じても代わりにならない {#not-a-substitute}

`permissions.blockWritesOutsideWorkingDirectories` を有効にしても、環境の隔離の代わりにはならない。この設定は、bypassPermissions でも Write・Edit・NotebookEdit が作業ディレクトリの外へ書くのを止める。一方で、シェルのコマンドは止めない。

つまり、ファイル編集の道具は作業ディレクトリに閉じても、`rm` や `curl`、`git push` のようなシェル経由の操作は、環境が許す範囲にそのまま届く。外への通信も閉じない。この設定は、隔離の上に重ねる 1 枚の守りである。

- 閉じるのは、ファイル編集の道具が書く場所だけである。シェルの読み書きと通信は別の層で囲う。
- 設定の効き方は <!-- link:begin protected-paths#outside-working-directory -->[消せない場所・触れない場所（protected paths） › 作業ディレクトリの外への読み書きを閉じる](../enforce/protected-paths.md#outside-working-directory)<!-- link:end --> にある。
- どのモードでも止まる場所は <!-- link:begin protected-paths#protected -->[消せない場所・触れない場所（protected paths） › 保護される場所と、モードごとの扱い](../enforce/protected-paths.md#protected)<!-- link:end --> にある。
- シェルのコマンドの読み書きと通信を OS の層で囲うのは、サンドボックスの役目である。囲えるものは <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> にある。

「確認を外す代わりに、書き込み先を絞ったから大丈夫」という判断は、この点で成り立たない。古い助言「`--dangerously-skip-permissions` で YOLO 運用」との関係は、台帳の <!-- link:begin outdated-advice-ledger#yolo-skip-permissions -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#yolo-skip-permissions)<!-- link:end --> にある。

## 無人の夜間実行をどこで動かすかの判断例 {#decision}

!!! example "判断例：夜間に大きな書き換えを無人で任せる"
    - **状況**：テストの多いリポジトリで、夜の間に大きな書き換えを任せたい。確認に答える人は朝までいない。
    - **迷う候補**：手元の PC で auto モードとサンドボックスを使い、止められた操作は朝に見直す。使い捨てのコンテナで bypassPermissions を使い、確認なしに最後まで走らせる。
    - **選んだもの**：先に、手元で auto モードとサンドボックスを使う形を試す。それでは作業が進まず、しかも使い捨ての環境の条件をすべて満たせるときだけ、コンテナで bypassPermissions を使う。
    - **理由**：手元の形は確認を減らすだけで、ホストの端末に境界が残る。コンテナの形は止め手を外す代わりに、被害を環境の中に閉じ込める。条件のどれかを満たせないなら、止め手を外すだけで閉じ込めが伴わないので使わない。止められた操作の見直し方は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> にある。

確認を外さずに無人で動かす道もある。許す道具を明示して渡すやり方は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> にある。取り消しにくい操作は、定期実行の対象にしない。接続先と権限を最小にする考え方は <!-- link:begin cloud-schedules#least-privilege -->クラウドの定期タスク › 接続先と権限を最小にする（準備中）<!-- link:end --> にある。

## どの原理・どの原因に効くか {#what-it-prevents}

このページは、原理「縛る」と、Claude 側の原因「境界がない」に関わる。bypassPermissions は、権限の確認という境界を取り除くモードである。境界がない状態で動かすなら、境界を環境の外側に作るしかない。隔離した使い捨ての環境が、その外側の境界になる。

- **縛る**：縛る場所を、確認から環境の隔離へ移す。確認は人の目に頼るが、隔離は人が見ていなくても効く。
- **境界がない**：Claude の触れる範囲に、はっきりした線を引けていない状態である。環境の通信・秘密・マウントを絞ることで、線を引き直す。
- 同じ原因に効く別の手段は、サンドボックス（<!-- link:begin sandboxing#when -->[サンドボックスで封じ込める › 使いどころ](../enforce/sandboxing.md#when)<!-- link:end -->）と、組織の側で強制する設定（<!-- link:begin managed-settings-enforcement#disable-modes -->管理設定と組織の強制 › モードを使えなくする設定（準備中）<!-- link:end -->）である。後者は、bypassPermissions そのものを使えなくする。

## 誤解されやすいこと {#misconceptions}

- **コンテナに入れれば何をしても安全**：コンテナに入れても、外へ出る通信と、中に置いた鍵は守られない。条件を満たしてはじめて、閉じ込めになる。
- **無人だから bypassPermissions が要る**：要るとは限らない。許す道具と上限を明示して渡し、確認を外さずに無人で走らせる道がある。まず <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> を見る。
- **今でも YOLO 運用が普通のやり方**：auto モードが使えるようになる前の近道である。いまは、ふだんの対話は auto モードとサンドボックスで足りる。bypass は隔離環境の中だけにする。経緯は <!-- link:begin outdated-advice-ledger#yolo-skip-permissions -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#yolo-skip-permissions)<!-- link:end --> にある。
- **自分で気を付ければ手元で使ってよい**：このモードの警告は、気を付ける人にも同じである。止め手がないので、どれだけ気を付けても、勘違いや紛れ込んだ指示による操作はそのまま通り、手元の端末やホームの中身に届く。
- **使うかどうかは個人の自由**：組織は、このモードを使えなくする設定を強制できる。優先の順番は <!-- link:begin managed-settings-enforcement#precedence -->管理設定と組織の強制 › 優先の順番（準備中）<!-- link:end --> にある。

権限モードの全体は、<!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> を見る。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)

**関連**

- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)
- [権限モードの選び方](../cli/permission-modes-overview.md)
- 管理設定と組織の強制（準備中）
- [消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md)
- [知らないリポジトリを開く前に](before-opening-unknown-repos.md)
- GitHub Actions と @claude（準備中）
- [クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [消されたくないもの（破壊的コマンド）](destructive-commands.md)
- クラウドの定期タスク（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
