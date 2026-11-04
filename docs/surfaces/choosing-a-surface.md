---
id: choosing-a-surface
title: アプリ・Claude Code・API の選び方
aliases: [面の選び方, どの Claude を使うか, Claude Code と Cowork の使い分け, 統合された Claude, Chat と Cowork の統合]
type: comparison
field: surfaces
chapter: 面の選び方
order: 10
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [合っていない]
pitfalls: []
scenes: [開発, 文章, 調べもの, データ分析]
summary: 頼みたい作業を、アプリ・Claude Code・API のどれで進めるかを、誰が手を動かすか・何に触れるか・どこで動くかの三つで選べる。迷ったら、触れる必要のあるものから決める。
signs:
  - {type: goal, text: この作業をアプリと Claude Code のどちらでやるべきか決めたい}
  - {type: goal, text: コードを書かない仕事は、アプリと Claude Code のどちらが向くか知りたい}
  - {type: situation, text: 古い記事の「Cowork は別のアプリ」という説明が、今の画面と合わない}
  - {type: goal, text: 自分のプログラムから Claude を呼ぶべきか、今ある面で足りるかを決めたい}
prerequisites: []
related: [where-it-runs, claude-code-surfaces, what-each-surface-cannot-do, product-map, tasks-and-schedules-in-the-app, permission-modes-in-the-app, sdk-comparison, headless-basics, office-paperwork, browser-control, peripheral-products]
tracks: [app-tasks]
outdated_advice: [cowork-separate-app]
sources: [hc-cowork-and-chat, hc-cowork-surfaces, hc-release-notes, cc-docs-claude-code-on-the-web, cc-docs-agent-sdk-overview]
volatility: 高
sections:
  - {title: 三つの面を比べる, anchor: compare-surfaces}
  - {title: アプリはチャットとタスクを一つの会話で扱う, anchor: app-chat-and-tasks}
  - {title: アプリのタスクか Claude Code か, anchor: app-tasks-or-claude-code}
  - {title: 自分のプログラムから呼ぶとき（API・SDK）, anchor: when-to-build-with-api}
  - {title: 判断例, anchor: examples}
  - {title: 組み合わせ方, anchor: combine}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手元の文書やブラウザの作業ならアプリ、リポジトリとコマンドの作業なら Claude Code、自分のプログラムから呼ぶなら API、と選べる。
    - **いつ引くか**：アプリと Claude Code のどちらで頼むか迷うとき、コードを書かない仕事の面を決めるとき、古い記事の「Cowork は別のアプリ」が今の画面と合わないとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：面の選び方・どの Claude を使うか・Claude Code と Cowork の使い分け・統合された Claude・Chat と Cowork の統合
<!-- textlint-enable -->

アプリ・Claude Code・API の選び方は、頼みたい作業を 3 つの面のどれで進めるかを決める基準である。基準は「誰が手を動かすか」「何に触れるか」「どこで動くか」の 3 つで、迷ったときは、作業が触れる必要のあるものから決める。面ごとの細かい差は、それぞれの分野のページに任せる。

## 三つの面を比べる {#compare-surfaces}

3 つの面は、作業に手を動かす主体と触れるものが違う。次の表は、その違いを 3 つの軸で並べたものである。

| 面 | 誰が手を動かすか | 何に触れるか | どこで動くか |
| --- | --- | --- | --- |
| アプリ | 結果を頼み、Claude が手順を進める | 会話に渡した文書、コネクタ、成果物のファイル | クラウドが基本。手元のファイルやブラウザは Desktop を開いている間 |
| Claude Code | 人と Claude が同じ作業場で往復する | リポジトリ、シェル、テスト、プロジェクトの設定 | 手元（ターミナル・IDE・Desktop）かクラウド |
| API | 自分のプログラム（ループも自分で書く層と、任せる層がある） | プログラムがツールとして渡したもの | 自分のプログラムが動く場所か、Anthropic が持つ環境 |

どこで動くかによって、触れられるファイル・ブラウザ・設定・秘密が変わる。理由は <!-- link:begin where-it-runs#three-locations -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 三つの実行場所](where-it-runs.md#three-locations)<!-- link:end --> にある。面ごとに使えない機能は <!-- link:begin what-each-surface-cannot-do#table -->[面ごとにできないこと（早見表） › 早見表（面 × 機能）](what-each-surface-cannot-do.md#table)<!-- link:end --> で引ける。

次の表は、アプリのタスクの機能について、数値ファイルの属性を道具が引いたものである。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 面 | 成熟度 | 入った版 | 確認日 |
| --- | --- | --- | --- | --- |
| [アプリのタスクと定期タスク（Claude Cowork）](../app/tasks-and-schedules-in-the-app.md) | アプリ | GA | 2026-01-12 | 2026-11-04 |

<!-- textlint-enable -->
<!-- gen:end compare -->

面の全体の地図と、周辺の製品の位置づけは <!-- link:begin product-map#surfaces -->[全体地図：Claude の面と層 › 面の地図](../start/product-map.md#surfaces)<!-- link:end --> と <!-- link:begin peripheral-products#list -->周辺製品の一覧 › 一覧（確認日つき）（準備中）<!-- link:end --> にある。

## アプリはチャットとタスクを一つの会話で扱う {#app-chat-and-tasks}

アプリでは、チャットとタスクが 1 つの会話にまとまった。軽い質問から、調べてファイルに仕上げる多段の作業までを、同じ会話の中で頼める。どちらのモードで始めるかを先に選ぶ必要はなく、Claude が要る道具を選んで進める。

- 結果を伝えると、Claude が手順を進める。成果物は編集できるファイルとして返る。頼み方は <!-- link:begin tasks-and-schedules-in-the-app#ask-for-results -->[タスクと定期タスク（Cowork） › 結果で頼む](../app/tasks-and-schedules-in-the-app.md#ask-for-results)<!-- link:end --> にある。
- クラウドで動くタスクは、PC を閉じても続く。手元のファイルやアプリを使うタスクは、Desktop を開いておく必要がある。
- スマホからは、タスクの進み具合を見て、質問に答え、向きを直せる。
- Web 検索にトグルはなく、役に立つときに Claude が自分で検索する。調査を深くやらせたいときは `/deep-research` か「+」から選ぶ。

展開は段階的に進んでいて、同じプランでもアカウントによって見え方が違う。入力欄に「Chat」と「Cowork」の選択が残っているアカウントは、まだ前のやり方のままである。

「Cowork は別のアプリ」「Web 検索はトグルで入れる」という古い説明が、今の画面と合わないのは、この統合のせいである。古い助言の台帳では <!-- link:begin outdated-advice-ledger#cowork-separate-app -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#cowork-separate-app)<!-- link:end --> が該当する。手順書に「Cowork に切り替える」とあったら、自分のアカウントがどちらの体験かを、入力欄で先に確かめる。

統合の後も残る制約がある。Incognito は前の体験のままで、ファイルの作成やコードの実行ができない。Add from GitHub や会話の途中からの分岐も使えない（2026-10-29 の確認）。制約は変わりやすいので、必要な機能がその面で使えるかは <!-- link:begin what-each-surface-cannot-do#table -->[面ごとにできないこと（早見表） › 早見表（面 × 機能）](what-each-surface-cannot-do.md#table)<!-- link:end --> で確かめる。

## アプリのタスクか Claude Code か {#app-tasks-or-claude-code}

アプリのタスクと Claude Code の違いは、作業が触れるものと、人がどこで見張るかである。コードを書くかどうかは決め手にならない。

| 作業が触れるもの | 向く面 | 理由 |
| --- | --- | --- |
| 文書、表、ブラウザ、コネクタ先のサービス | アプリ | 結果で頼み、成果物のファイルを受け取る形に合う |
| リポジトリ、シェル、テスト、フック、プロジェクトの設定 | Claude Code | 変更が差分として見え、検査を同じ場所で回せる |
| 手元のファイルだけで、コードではない | どちらでもよい | 見張りたい粒度と、手順を育てたいかで決める |

コードを書かない仕事でも、Claude Code を使う選択はある。Desktop の Code タブで、作業用のフォルダを決め、手動のモードで始める使い方が日本語の実務記事で紹介されている（根拠：弱）。手順をファイルやスキルに育てたい事務作業は <!-- link:begin office-paperwork#work-folder -->[事務作業の半自動化（経費・報告） › 作業用のフォルダと権限の設定で始める](../recipes/office-paperwork.md#work-folder)<!-- link:end --> にある。

日本語の実務記事には、Cowork から始め、繰り返す作業になったら Claude Code へ移す、という整理もある（根拠：弱。二次の情報で、公式の文書の推奨ではない）。この辞典は、これを目安の 1 つとして扱う。繰り返す作業は、手順が固まるほど、ファイルやスキルとして育てやすい面が向く。

任せる幅を広げるときは、守りを先に決める。定期タスクや無人の作業へ広げる前に、次の 2 つを読む。

- 読める範囲と行動できる範囲を同時に広げない置き方は、<!-- link:begin permission-modes-in-the-app#two-conditions -->[アプリの権限モード（Auto と Manual）と安全 › 読める範囲と行動できる範囲を同時に広げない](../app/permission-modes-in-the-app.md#two-conditions)<!-- link:end --> にある。
- 専用のフォルダと低いリスクの作業から始める手順は、<!-- link:begin permission-modes-in-the-app#start-small -->[アプリの権限モード（Auto と Manual）と安全 › 専用のフォルダと、低いリスクの作業から](../app/permission-modes-in-the-app.md#start-small)<!-- link:end --> にある。

定期タスクにしないものは <!-- link:begin tasks-and-schedules-in-the-app#what-not-to-schedule -->[タスクと定期タスク（Cowork） › 定期タスクにしないもの](../app/tasks-and-schedules-in-the-app.md#what-not-to-schedule)<!-- link:end --> にある。

Claude Code の中の面（ターミナル・IDE・Desktop・Web・モバイル）の選び方は、同じエージェントループの別の窓口を選ぶ話である。<!-- link:begin claude-code-surfaces#how-to-choose -->Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル） › 選び方（準備中）<!-- link:end --> に任せる。

## 自分のプログラムから呼ぶとき（API・SDK） {#when-to-build-with-api}

API は、自分のプログラムの一部として Claude を呼ぶ面である。人が会話を開く代わりに、プログラムが入力を渡し、結果を受け取る。

まず、今ある面で足りないかを確かめる。次の箇条のうち、最初の 2 つは API を選ばなくても済む例で、3 つ目が API の出番である。

- スクリプトや CI から Claude Code を動かすだけなら、非対話モードで足りる。無人では確認に答える人がいないので、許す道具と止まる上限を決めて渡す。手順は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> にある。
- 週次の報告のような繰り返しの事務は、アプリの定期タスクで足りる。
- 自分のサービスの利用者に Claude の機能を出す、独自のループや画面に組み込む、というときは API の出番である。

API を選んだ後は、ループを誰が回すかで層が分かれる。

- Client SDK は、API を直接呼んでループを自分で書く。
- Agent SDK は、Claude Code と同じツールとループをライブラリとして自分のプロセスに組み込む。
- Managed Agents は、Anthropic にループと環境を持たせる。

選び方は <!-- link:begin sdk-comparison#comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）](../api/sdk-comparison.md#comparison)<!-- link:end --> にある。判断例は <!-- link:begin sdk-comparison#examples -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 選び方の判断例](../api/sdk-comparison.md#examples)<!-- link:end --> にある。

API を使うと、課金の経路が変わりうる。API キーがあるときの扱いは <!-- link:begin headless-basics#billing-path -->[非対話モード（claude -p）の基本 › 課金の経路（API キーがあるとき）](../delegate/headless-basics.md#billing-path)<!-- link:end --> で確かめる。

## 判断例 {#examples}

!!! example "判断例：週次の売上を集計して報告にまとめる"
    - **状況**：毎週、売上の CSV を受け取り、集計して報告の文書にまとめる。コードは書かない。
    - **迷う候補**：アプリのタスク。Desktop の Code タブの Claude Code。
    - **選んだもの**：最初はアプリのタスクにする。
    - **理由**：触れるのは渡した CSV と、仕上げる文書だけで、リポジトリとシェルは要らない。結果で頼めば足りる。毎週の手順が固まり、ファイルやスキルとして育てたくなったら、Claude Code へ移す。

!!! example "判断例：リポジトリのテスト失敗を直す"
    - **状況**：既存のリポジトリで、テストが落ちている。原因は分からない。
    - **迷う候補**：アプリのタスク。ターミナルの Claude Code。
    - **選んだもの**：Claude Code にする。
    - **理由**：触れるのはリポジトリ、シェル、テストである。変更を差分で見て、検査を同じ場所で回せる。アプリでも頼めるが、結果の確かめが手作業になる。

!!! example "判断例：問い合わせの返信の下書きを自社サービスに組み込む"
    - **状況**：自社のサービスで、問い合わせが届くたびに返信の下書きを作りたい。人が会話を開く場面がない。
    - **迷う候補**：アプリの定期タスク。非対話モードの Claude Code。API。
    - **選んだもの**：API にする。
    - **理由**：サービスの処理の一部として、プログラムが入力を渡して結果を受け取る形になる。会話を開く人がいないので、アプリの面は合わない。ループの持ち方は <!-- link:begin sdk-comparison#comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）](../api/sdk-comparison.md#comparison)<!-- link:end --> で決める。

## 組み合わせ方 {#combine}

面は 1 つに決めなくてよい。作業の段階ごとに、触れるものが変わるからである。

- 調べものや資料の下書きをアプリのタスクで進め、その結果のファイルをリポジトリに置いて、Claude Code で実装に使う。
- 外出先から手元の作業を見るなら、Claude Code のリモート操作で、実行とファイルを手元に残したまま画面だけ移せる。クラウドで動かすか手元に残すかは <!-- link:begin where-it-runs#remote-control -->[実行場所の違い（クラウド・自分の PC・リモート操作） › リモート操作は実行を手元に残す](where-it-runs.md#remote-control)<!-- link:end --> で決める。
- ブラウザや画面の操作が要る作業は、コネクタがあればそれを先に使う。順番は <!-- link:begin browser-control#which-to-use -->[Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ](browser-control.md#which-to-use)<!-- link:end --> にある。

面を移すと、使える機能が変わる。移す前に、必要な機能が移る先にあるかを <!-- link:begin what-each-surface-cannot-do#moving-between-surfaces -->[面ごとにできないこと（早見表） › 別の面に移すとき](what-each-surface-cannot-do.md#moving-between-surfaces)<!-- link:end --> で確かめる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)
- [アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md)
- [Client SDK・Agent SDK・Managed Agents・CLI の比較](../api/sdk-comparison.md)

**関連**

- Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル）（準備中）
- [面ごとにできないこと（早見表）](what-each-surface-cannot-do.md)
- [全体地図：Claude の面と層](../start/product-map.md)
- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- [事務作業の半自動化（経費・報告）](../recipes/office-paperwork.md)
- [Claude in Chrome と computer use（ブラウザと画面の操作）](browser-control.md)
- 周辺製品の一覧（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
