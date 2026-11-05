---
id: claude-code-surfaces
title: Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル）
nav_title: Claude Code の面
aliases: [Desktop の Code タブ, Claude Code をどこで使うか]
type: comparison
field: surfaces
chapter: 面ごとの違い
order: 30
level: 整える
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [合っていない]
pitfalls: []
scenes: [開発]
summary: Claude Code をターミナル・IDE・Desktop・Web・モバイルのどれで使うかを、動く場所・読む設定・画面の機能の違いで選べる。中で動くエージェントループは同じである。
signs:
  - {type: goal, text: ターミナルと VS Code の拡張のどちらで Claude Code を使うか決めたい}
  - {type: symptom, text: ターミナルではできたことが、IDE や Desktop ではできない}
  - {type: goal, text: ブラウザやスマホから Claude Code に作業を頼みたい}
prerequisites: [where-it-runs]
related: [choosing-a-surface, using-ides#vs-cli, cloud-sessions-and-teleport, control-from-phone, settings-layers, agent-view-and-background, what-each-surface-cannot-do]
tracks: [ide-extensions, desktop-code, cloud-sessions, remote-control]
outdated_advice: [code-on-the-web-remote]
sources: [cc-docs-vs-code, cc-docs-jetbrains, cc-docs-desktop, cc-docs-claude-code-on-the-web, cc-docs-remote-control, cc-docs-feature-availability, cc-docs-cli-reference]
volatility: 高
sections:
  - {title: 同じエージェントループ、違う窓口, anchor: same-loop}
  - {title: 面ごとの違い（表）, anchor: comparison-table}
  - {title: 選び方, anchor: how-to-choose}
  - {title: 組み合わせ方, anchor: combine}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手元で見ながら進めるなら端末・IDE・Desktop、閉じても任せるならクラウド、手元の実行を離れて操るなら Remote Control を選べる。
    - **いつ引くか**：ターミナルと IDE のどちらにするか迷うとき、ターミナルでできたことが別の面でできないとき、ブラウザやスマホから頼みたいとき。
    - **前提**：<!-- link:begin where-it-runs -->[実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Desktop の Code タブ・Claude Code をどこで使うか
<!-- textlint-enable -->

Claude Code の面とは、同じ Claude Code を使う窓口のことである。この記事は、ターミナル・IDE・Desktop・Web・モバイルのどれを選ぶかを、動く場所・読む設定・画面の機能の違いで決めるための比較である。

## 同じエージェントループ、違う窓口 {#same-loop}

Claude Code の面が違っても、中で動くエージェントループは同じである。ファイルを読み、編集し、コマンドを動かし、結果を見て次の手を決める。この繰り返しは、どの面でも変わらない。

違うのは、ループの外側の 3 つである。

- **動く場所**：自分の PC か、Anthropic のクラウドか。触れるファイルやブラウザと、PC を閉じても続くかが変わる。詳しくは <!-- link:begin where-it-runs#three-locations -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 三つの実行場所](where-it-runs.md#three-locations)<!-- link:end --> にある。
- **読む設定**：手元で動く面は手元の設定を読む。クラウドのセッションは、user 設定・local 設定・手元のプラグインを読まない。層ごとの扱いは <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end --> にある。
- **画面の機能**：差分の見せ方、選択範囲の渡し方、並列セッションの管理など、画面が持つ道具が違う。

「Web」と「モバイル」は、動く場所ではなく窓口の名前である。ブラウザの claude.ai/code やスマホのアプリは、クラウドのセッションを開く窓口にも、手元の PC で動くセッションを操る窓口（Remote Control）にもなる。同じ画面でも、実行がどちらにあるかを先に確かめる。

ターミナルの CLI は、この記事の基準である。WSL と Linux の CLI を基準にして書いており、ほかの OS と IDE の拡張の動作は未確認である。

## 面ごとの違い（表） {#comparison-table}

次の表は、ターミナルのほかの面を機能ごとに並べたものである。表は数値ファイルから道具が作るので、成熟度や入った版は表を見る。この節の文は、表に出ない読み方だけを補う。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 強制力 | 入った版 |
| --- | --- | --- |
| IDE の拡張 | — | — |
| [Desktop アプリの Claude Code](claude-code-surfaces.md) | — | 2.0.51（2025-11-24） |
| [クラウドのセッション](../cli/cloud-sessions-and-teleport.md) | なし | — |
| Remote Control | — | — |

すべて共通：面 Claude Code、成熟度 GA、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

表の読み方を 4 つ挙げる。

- **IDE の拡張**：VS Code の拡張と JetBrains のプラグインがあり、どちらも IDE の中で Claude Code を使う。以下は VS Code の拡張の機能である。ターミナルの CLI と同じ設定ファイルを共有し、計画を文書として開いてコメントで返せる。編集の前に差分を出して、変更ごとに受け入れるか戻せる。選んだ範囲と開いているファイル名は自動でメッセージに入る。CLI と違い、コマンドとスキルは一部だけで、`!` の Bash の近道とタブ補完はない。JetBrains のプラグインは、差分を IDE の差分表示で出し、選択範囲と開いているタブを渡す。
- **Desktop の Code タブ**：Desktop アプリの中で Claude Code を動かす。並列のセッションを画面で管理でき、worktree のオプションがある。ターミナルで始めたセッションは `/desktop` で Desktop に移せる。
- **クラウドのセッション**：Anthropic のクラウドで動き、手元を閉じても続く。<!-- name:begin web-to-cloud-sessions -->クラウドセッション（cloud sessions）<!-- name:end -->という名前で、ブラウザの入口は今も Claude Code on the web とも呼ばれる。手元の設定の一部を読まないので、計画と縛りはリポジトリに置いてから送る。
- **Remote Control**：手元で動くセッションを、ブラウザやスマホから見て指示し、承認する。実行とファイルは手元に残る。API キーでは使えない。

IDE の拡張の動作は、公式の文書による記述で、この辞典の環境では試していない。JetBrains の拡張が提供する機能の細部は、<!-- link:begin using-ides#vs-cli -->IDE（VS Code・JetBrains）で使う<!-- link:end --> を先に読む。

各面で使えない機能を引くときは、<!-- link:begin what-each-surface-cannot-do#table -->[面ごとにできないこと（早見表） › 早見表（面 × 機能）](what-each-surface-cannot-do.md#table)<!-- link:end --> の早見表が早い。

## 選び方 {#how-to-choose}

選ぶ基準は、触れる必要のあるものから決めることである。手元のファイルや環境に触れるなら手元で動く面を選ぶ。手元を閉じても続けたいならクラウド、席を離れて手元のセッションを進めたいなら Remote Control である。アプリ・Claude Code・API のどれにするかの前段は、<!-- link:begin choosing-a-surface -->[アプリ・Claude Code・API の選び方](choosing-a-surface.md)<!-- link:end --> にある。

Claude Code の中で迷う場面は、おおよそ次の 3 つである。

!!! example "判断例：ターミナルか VS Code の拡張か"
    - **状況**：日常の開発を VS Code で進めていて、Claude Code をどちらで使うか決めたい。
    - **迷う候補**：統合ターミナルで CLI を使う。VS Code の拡張を使う。
    - **選んだもの**：変更の確認が多い作業は拡張、コマンドとスキルを多く使う作業は CLI。
    - **理由**：拡張は、計画の文書レビューと変更ごとの差分の受け入れに強い。CLI は `!` の近道とタブ補完があり、コマンドとスキルが揃う。会話の履歴は共通なので、途中で切り替えても続けられる。

!!! example "判断例：席を離れても作業を進めたい"
    - **状況**：夜に重いリファクタリングを始めて、ブラウザやスマホから様子を見たい。
    - **迷う候補**：クラウドのセッションに送る。手元のセッションを Remote Control で操る。
    - **選んだもの**：手元の秘密やローカルの環境に触れる作業は Remote Control、手元に依存しない独立した作業はクラウド。
    - **理由**：Remote Control は実行とファイルが手元に残るので、クラウドに出したくない作業に合う。クラウドは手元を閉じても続くが、手元の設定の一部を読まない。何が届かないかは <!-- link:begin where-it-runs#what-cloud-cannot-reach -->[実行場所の違い（クラウド・自分の PC・リモート操作） › クラウドで動くときに届かないもの](where-it-runs.md#what-cloud-cannot-reach)<!-- link:end --> で確かめる。

!!! example "判断例：ターミナルでできたことが別の面でできない"
    - **状況**：ターミナルで使えたコマンドが、IDE の拡張や Desktop で出てこない。
    - **迷う候補**：設定が壊れたと考えて直す。面の違いと考える。
    - **選んだもの**：先に面の違いを疑い、その面で使えない機能かを確かめる。
    - **理由**：面ごとに使える機能の集合が違う。設定を直す前に、<!-- link:begin what-each-surface-cannot-do#table -->[面ごとにできないこと（早見表） › 早見表（面 × 機能）](what-each-surface-cannot-do.md#table)<!-- link:end --> で、その機能がその面にあるかを引く。設定が効かないだけなら、`/status` で読み込まれた層を見る（確かめ方は <!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](../cli/settings-layers.md#verify)<!-- link:end --> にある）。

任せる幅を広げる面（クラウドと背景のセッション）では、先に守りを決める。投げる前に決める守りは <!-- link:begin agent-view-and-background#guards-first -->[agent view と背景セッション › 投げる前に決める守り](../delegate/agent-view-and-background.md#guards-first)<!-- link:end --> にある。IDE では、権限を緩めたモードで IDE が自動で実行する設定ファイルを Claude が書き換えうる。安全の注意は <!-- link:begin using-ides#safety -->IDE（VS Code・JetBrains）で使う<!-- link:end --> を読む。

古い助言として、ターミナルからクラウドのセッションを始めるフラグを `--remote` と書く手順が残っている。今のフラグは <!-- name:begin remote-to-cloud-flag -->--cloud<!-- name:end --> なので、そちらに替える。`--remote-control` は別の機能なので替えない。台帳の行は <!-- link:begin outdated-advice-ledger#code-on-the-web-remote -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#code-on-the-web-remote)<!-- link:end --> にある。

## 組み合わせ方 {#combine}

面は 1 つに決めなくてよい。セッションを面の間で移しながら使うのが実際の使い方である。

- **計画は手元、実行はクラウド**：手元の plan mode で計画を作り、計画ファイルをリポジトリに置いてから、クラウドに送る。クラウドは手元の設定の一部を読まないので、縛りもリポジトリに置く。
- **クラウドで始めて、手元に取り込む**：終わったセッションは teleport で手元の端末に取り込める。取り込み方は <!-- link:begin cloud-sessions-and-teleport#teleport -->[クラウドセッションと teleport › teleport で取り込む](../cli/cloud-sessions-and-teleport.md#teleport)<!-- link:end --> にある。
- **手元で動かして、外から見る**：手元のセッションを Remote Control でつなぎ、スマホから承認だけ返す。手元の PC は動かし続ける必要がある。手順は <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）<!-- link:end --> にある。
- **ターミナルを基準にして、IDE を足す**：IDE の拡張が動いていると、ターミナルの CLI も IDE の差分表示を使える。統合ターミナルで CLI を使うなら、CLI は別に入れる。

独立した作業を複数投げるなら、背景のセッションに置く手もある。使い方は <!-- link:begin agent-view-and-background -->[agent view と背景セッション](../delegate/agent-view-and-background.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)：Anthropic・英語・確認日 2026-11-04
- [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)：Anthropic・英語・確認日 2026-11-04
- [Desktop application](https://code.claude.com/docs/en/desktop)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Continue local sessions from any device with Remote Control](https://code.claude.com/docs/en/remote-control)：Anthropic・英語・確認日 2026-11-04
- [Feature availability](https://code.claude.com/docs/en/feature-availability)：Anthropic・英語・確認日 2026-11-04
- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)

**関連**

- [アプリ・Claude Code・API の選び方](choosing-a-surface.md)
- [クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)
- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [agent view と背景セッション](../delegate/agent-view-and-background.md)
- [面ごとにできないこと（早見表）](what-each-surface-cannot-do.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
