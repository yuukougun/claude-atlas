---
id: choosing-automation
title: 自動化の選び方（定期タスク・非対話モード・SDK）
aliases: [自動化の比較, cron で動かす]
type: comparison
field: delegate
chapter: 定期と無人の実行
order: 160
level: 回す
priority: 推奨
surfaces: [claude-code, app, api]
principle: [縛る, 確かめる]
prevents: [合っていない, 境界がない]
pitfalls: []
scenes: [開発]
summary: 決まった時刻・イベント・スクリプトから Claude を動かす方法を、どこで動くか・何に触れられるか・どの課金になるかで選べる。
signs:
  - {type: goal, text: 決まった時刻やイベントで、Claude を自動で動かしたい}
  - {type: symptom, text: 自分の作業を自動で回したいが、どの仕組みで動かすか決められない}
prerequisites: [headless-basics, loop-and-scheduling]
related: [cloud-schedules, github-actions-with-claude, bare-mode, tasks-and-schedules-in-the-app, sdk-comparison, agent-sdk-basics, where-it-runs, check-billing-path, checking-unattended-runs, default-safety-settings]
tracks: [loop, scheduled-tasks, headless, github-actions, agent-sdk, managed-agents]
outdated_advice: [routines-name]
sources: [cc-docs-scheduled-tasks, cc-docs-routines, cc-docs-desktop-scheduled-tasks, cc-docs-commands, cc-docs-headless, cc-docs-github-actions, cc-docs-agent-sdk-overview, hc-agent-sdk-plan, hc-api-credits, api-docs-managed-agents, cc-docs-feature-availability]
volatility: 中
sections:
  - {title: 比較の表, anchor: compare}
  - {title: 選ぶ 3 つの軸, anchor: axes}
  - {title: 選び方の判断例, anchor: examples}
  - {title: 組み合わせ方と確かめ方, anchor: combine}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：時刻やイベントなら予定のタスク、スクリプトや CI なら claude -p、自作のプログラムからなら Agent SDK を選ぶ。
    - **いつ引くか**：決まった時刻やイベントで Claude を自動で動かしたいが、どの仕組みで動かすか決められないとき。
    - **前提**：<!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](headless-basics.md)<!-- link:end -->・<!-- link:begin loop-and-scheduling -->[/loop と定期実行の方式](loop-and-scheduling.md)<!-- link:end -->
    - **共通の注意**：どの方式も、人がいない間に動くと確認に答える人がいない。止まる上限と結果の確かめ方を、選ぶ前に決める。

<!-- textlint-disable -->
別名：自動化の比較・cron で動かす
<!-- textlint-enable -->

自動化の選び方は、画面の前で依頼を 1 つずつ出す代わりに、決めた時刻・イベント・スクリプトから Claude を動かす方式を選ぶための比較である。選ぶ軸は 3 つある。どこで動くか、何に触れられるか、どの課金の経路になるかである。成熟度は変わるので本文に書かず、表から読む。

自動化は任せる幅を広げるので、方式を選ぶ前に守りを決める。無人で動かす前の問いは <!-- link:begin five-questions-before-delegating#proportional-guards -->[任せ方の段階と、無人で走らせる前の五つの問い › 段ごとに強める確かめ方と封じ込め](five-questions-before-delegating.md#proportional-guards)<!-- link:end --> にある。段階ごとに足す設定は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> にある。止まる上限は <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](headless-basics.md#limits)<!-- link:end --> にある。

## 比較の表 {#compare}

次の表は、自動で Claude を動かす方式として扱う機能を並べたものである。属性は数値ファイルから道具が作る。

<!-- gen:begin compare 面 成熟度 -->
<!-- textlint-disable -->

| 機能 | 面 | 成熟度 |
| --- | --- | --- |
| [/loop](loop-and-scheduling.md) | Claude Code | GA |
| [予定のタスク（scheduled tasks）](cloud-schedules.md) | Claude Code | research preview |
| [非対話モード（claude -p）](headless-basics.md) | Claude Code | GA |
| [GitHub Actions](github-actions-with-claude.md) | Claude Code | GA |
| [Agent SDK（Claude Agent SDK）](../api/agent-sdk-basics.md) | Claude Code・API | GA |
| [Managed Agents（Claude Managed Agents）](../api/sdk-comparison.md) | API | beta |

<!-- textlint-enable -->
<!-- gen:end compare 面 成熟度 -->

表の読み方は 4 つある。

- 表の予定のタスクは、<!-- name:begin routines-to-scheduled-tasks -->クラウドの予定のタスク（cloud scheduled tasks）<!-- name:end --> を指す。自分の機械で動く Desktop の予定のタスクは別の機能で、<!-- link:begin loop-and-scheduling#where-to-run -->[/loop と定期実行の方式 › どこで走らせるか（セッション・手元・クラウド）](loop-and-scheduling.md#where-to-run)<!-- link:end --> が持つ。
- claude -p・GitHub Actions・Agent SDK は、Claude Code と同じ道具とループを動かす入口である。違いは、誰がどこから呼ぶかにある。
- Managed Agents は、Claude Code を動かす方式ではない。Anthropic がループと環境を持つ仕組みである。自分の製品に組み込む比較は <!-- link:begin sdk-comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較](../api/sdk-comparison.md)<!-- link:end --> が持つ。
- 成熟度が安定版でない方式は、画面や名前が変わりうる。実際に名前が変わった予定のタスクの例は、「古くなった助言」の節で扱う。

アプリで頼むタスクの定期実行は、Claude Code の方式とは別の機能である。<!-- link:begin tasks-and-schedules-in-the-app#where-it-runs -->[タスクと定期タスク（Cowork） › どこで動くか（クラウドと Desktop）](../app/tasks-and-schedules-in-the-app.md#where-it-runs)<!-- link:end --> を引く。

## 選ぶ 3 つの軸 {#axes}

次の表は、方式ごとの動く場所と、触れられるものと、課金の経路をまとめたものである。きっかけの違いは表の下に書く。

| 方式 | 動く場所 | 触れられるもの | 課金の経路 |
| --- | --- | --- | --- |
| /loop | 開いているセッション（自分の機械） | 手元のファイル。セッションの権限を引き継ぐ | そのセッションの認証のまま |
| Desktop の予定のタスク | 自分の機械 | 手元のファイル | 未確認 |
| クラウドの予定のタスク | Anthropic のクラウド | 保存したリポジトリの新しい clone とコネクタ。手元のファイルは見えない | サブスクリプションが要る |
| claude -p | 呼んだ機械（cron・スクリプト・CI） | その機械のファイルと、既定で読み込む設定 | 環境に API キーがあれば API の従量。なければログインの経路 |
| GitHub Actions | GitHub Actions のランナー | チェックアウトしたリポジトリ。鍵と権限は secrets と workflow の設定で決まる | 置いた鍵の種類で決まる |
| Agent SDK | 自分のプログラムが動く機械 | 読み込む設定をプログラムで決める | claude.ai のログインならプランの上限から。API キーなら API の課金 |
| Managed Agents | Anthropic のクラウド | 組み込みの道具の範囲 | API の課金 |

### きっかけ

きっかけは、方式によって誰が持つかが違う。

- 間隔で繰り返す：/loop。開いているセッションの中だけで動く。
- 時刻・API の呼び出し・GitHub のイベント：クラウドの予定のタスク。保存したプロンプトとリポジトリとコネクタから起動する。
- 時刻：Desktop の予定のタスク。
- 呼ぶ側が決める：claude -p と Agent SDK。cron でもスクリプトでも CI でも、呼ぶものが決める。
- メンションとイベントと定時：GitHub Actions。`prompt` を渡さないと `@claude` のメンションに答え、渡すと任意のイベントや定時で動く。

### どこで動くか

機械を閉じても動かしたいなら、クラウドか GitHub Actions である。手元のファイルや道具が要るなら、自分の機械で動く方式になる。クラウドで動くと届かないものは <!-- link:begin where-it-runs#what-cloud-cannot-reach -->[実行場所の違い（クラウド・自分の PC・リモート操作） › クラウドで動くときに届かないもの](../surfaces/where-it-runs.md#what-cloud-cannot-reach)<!-- link:end --> にある。手元で動かすときの境界は <!-- link:begin where-it-runs#local-boundaries -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 手元で動かすときの境界](../surfaces/where-it-runs.md#local-boundaries)<!-- link:end --> にある。

### 何に触れられるか

触れられる範囲は、動く場所で決まる。それに加えて、claude -p は既定で、その場所の CLAUDE.md・フック・MCP などを読み込む。知らないリポジトリのフックや手元の設定が混ざるのを防ぐ方法は <!-- link:begin bare-mode#what-is-skipped -->[--bare と再現性 › 読み込まないもの](bare-mode.md#what-is-skipped)<!-- link:end -->、知らないフォルダで動かすときの注意は <!-- link:begin headless-basics#untrusted-folders -->[非対話モード（claude -p）の基本 › 知らないフォルダで動かすとき](headless-basics.md#untrusted-folders)<!-- link:end --> にある。

Agent SDK は、どの設定を読み込むかをプログラムで決める。決め方は <!-- link:begin agent-sdk-basics#setting-sources -->[Agent SDK（Claude Code をライブラリとして使う） › 読み込む設定を決める](../api/agent-sdk-basics.md#setting-sources)<!-- link:end --> にある。外の人が書いた issue や PR を読ませる GitHub Actions の注意は <!-- link:begin github-actions-with-claude#untrusted-input -->[GitHub Actions と @claude › 外の人が書いた issue と PR](github-actions-with-claude.md#untrusted-input)<!-- link:end --> にある。

### どの課金の経路か

経路は、方式より認証で決まる。環境に API キーがあると、サブスクリプションでログインしていても API の従量になる。claude -p では、変数があれば必ずその鍵を使う。例外はクラウドの予定のタスクで、環境に鍵を置いてもサブスクリプションの認証が使われる（<!-- link:begin cloud-schedules#pitfalls -->[クラウドの定期タスク › 効かない場面・落とし穴](cloud-schedules.md#pitfalls)<!-- link:end -->）。決まる順は <!-- link:begin check-billing-path#how-the-path-is-chosen -->[課金の経路を確かめる（API キーとサブスクリプション） › 経路が決まる順](../cost/check-billing-path.md#how-the-path-is-chosen)<!-- link:end -->、無人で回す前の確かめ方は <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](../cost/check-billing-path.md#check-current-path)<!-- link:end --> にある。

プランに付く月の API credits は、使える方式と使えない方式がある。対象は起動の仕方で変わる。確かめ方は <!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](../cost/check-billing-path.md#monthly-api-credits)<!-- link:end --> にある。Agent SDK の課金の経路は <!-- link:begin agent-sdk-basics#billing -->[Agent SDK（Claude Code をライブラリとして使う） › 課金の経路](../api/agent-sdk-basics.md#billing)<!-- link:end --> にある。--bare を使うときの認証は <!-- link:begin bare-mode#authentication -->[--bare と再現性 › 認証が変わる（サブスクリプションで使うとき）](bare-mode.md#authentication)<!-- link:end --> にある。

## 選び方の判断例 {#examples}

!!! example "判断例：夜間のテストの結果を、別のスクリプトに渡したい"
    - **状況**：毎晩、手元のリポジトリでテストを流し、落ちたものの要約を所定のファイルに書かせる。翌朝、別のスクリプトがそのファイルを読んで通知する。
    - **迷う候補**：Desktop の予定のタスクで毎晩走らせる。cron から claude -p を呼ぶ。
    - **選んだもの**：cron から claude -p を呼ぶ。
    - **理由**：結果を別のスクリプトが読むので、出力の形式と終了コードを指定できる方式が渡しやすい。止まる上限も、呼ぶ側で指定できる。手元のファイルに触れる点は、どちらでも同じである。形式と上限の指定は <!-- link:begin headless-basics#output-and-exit-codes -->[非対話モード（claude -p）の基本 › 出力の形式と終了コード](headless-basics.md#output-and-exit-codes)<!-- link:end --> にある。

!!! example "判断例：PR が開かれるたびに、レビューのコメントを付けたい"
    - **状況**：チームのリポジトリで、PR が開かれるたびに、Claude にレビューのコメントを付けさせたい。誰の PC も開く必要はない。
    - **迷う候補**：GitHub のイベントで起動する、クラウドの予定のタスク。GitHub Actions。
    - **選んだもの**：GitHub Actions。
    - **理由**：どちらも GitHub のイベントで動かせるが、今回はチームの CI の一部として、リポジトリの secrets と権限で管理したい。workflow の timeout と concurrency で費用も抑えられる。外の人が書いた PR を読ませるなら、鍵と権限を最小にする。前提は <!-- link:begin github-actions-with-claude#secrets-and-permissions -->[GitHub Actions と @claude › 鍵と権限](github-actions-with-claude.md#secrets-and-permissions)<!-- link:end --> にある。個人の作業を時刻で回すだけなら、クラウドの予定のタスクが軽い。

!!! example "判断例：自作のツールの中で、調べものを Claude に頼みたい"
    - **状況**：社内で使う自作のツールが Python で動いている。ユーザーの質問を受けて、Claude Code と同じ道具を使って調べさせ、結果をプログラムの変数として受け取りたい。
    - **迷う候補**：claude -p をサブプロセスで呼ぶ。Agent SDK を使う。
    - **選んだもの**：Agent SDK。
    - **理由**：呼び出す側が Python で、結果をプログラムの中で扱いたい。権限と読み込む設定もプログラムから決められる。文字列を 1 回受け取れば足りるなら、claude -p で足りる。自分の製品に組み込む層の選び方は <!-- link:begin sdk-comparison#examples -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 選び方の判断例](../api/sdk-comparison.md#examples)<!-- link:end --> にある。

## 組み合わせ方と確かめ方 {#combine}

方式は、排他の選択ではない。きっかけを持つものと、中身を動かすものを分けて組み合わせられる。

- 時刻は cron などの呼ぶ側に任せ、中身は claude -p に渡す依頼として書く。時刻の管理と、依頼の中身を別々に直せる。
- 実行は GitHub Actions に置き、手元の設定の影響を避けたいところだけ --bare を足す。API キーが要る点は <!-- link:begin bare-mode#authentication -->[--bare と再現性 › 認証が変わる（サブスクリプションで使うとき）](bare-mode.md#authentication)<!-- link:end --> で確かめる。
- 手元のファイルが要る作業は自分の機械で動く方式に置き、手元のファイルが要らない作業はクラウドに置く。分けると、クラウドに渡す接続先と権限を減らせる。減らし方は <!-- link:begin cloud-schedules#least-privilege -->[クラウドの定期タスク › 接続先と権限を最小にする](cloud-schedules.md#least-privilege)<!-- link:end --> にある。
- 守りは、どの方式でも同じ順に決める。許す道具と止まる上限を決め、成功の定義と結果の置き場所を依頼に書く。人が答えられない実行では、確認が要る操作は止まるか、ほかの判断に任される。

動かした後は、終了コードと要約だけで決めない。出力・記録・差分で確かめ、最後の判断は人とブランチの保護に置く。確かめ方は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある。記録の見方は <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> にある。最初は短い間隔や少ない範囲で 1 回だけ動かし、課金の経路と結果の置き場所が想定どおりか見てから、定期に回す。

## 古くなった助言 {#outdated}

「routines で定期実行を作る」という書き方は、古い。今の名前は <!-- name:begin routines-to-scheduled-tasks -->クラウドの予定のタスク（cloud scheduled tasks）<!-- name:end --> である。一部の画面と URL と API には旧名が残るが、同じ機能を指す。古い記事の routines は、予定のタスクに読み替える。ただし、手元で動く Desktop の予定のタスクと /loop は別の機能なので、記事がどれを指すかを確かめる。台帳の行は <!-- link:begin outdated-advice-ledger#routines-name -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#routines-name)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [非対話モード（claude -p）の基本](headless-basics.md)
- [/loop と定期実行の方式](loop-and-scheduling.md)

**関連**

- [クラウドの定期タスク](cloud-schedules.md)
- [GitHub Actions と @claude](github-actions-with-claude.md)
- [--bare と再現性](bare-mode.md)
- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [Client SDK・Agent SDK・Managed Agents・CLI の比較](../api/sdk-comparison.md)
- [Agent SDK（Claude Code をライブラリとして使う）](../api/agent-sdk-basics.md)
- [実行場所の違い（クラウド・自分の PC・リモート操作）](../surfaces/where-it-runs.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)：Anthropic・英語・確認日 2026-11-04
- [Automate work with scheduled tasks](https://code.claude.com/docs/en/routines)：Anthropic・英語・確認日 2026-11-04
- [Schedule recurring tasks in Claude Code Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)：Anthropic・英語・確認日 2026-11-04
- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)：Anthropic・英語・確認日 2026-11-04
- [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)：Anthropic・英語・確認日 2026-11-04
- [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)：Anthropic・英語・確認日 2026-11-04
- [Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)：Anthropic・英語・確認日 2026-11-04
- [Feature availability](https://code.claude.com/docs/en/feature-availability)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
