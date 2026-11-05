---
id: what-each-surface-cannot-do
title: 面ごとにできないこと（早見表）
aliases: [面の制約, モバイルでできないこと, シークレットチャットでできないこと, 機能の対応表]
type: ledger
field: surfaces
chapter: 面ごとの違い
order: 40
priority: 推奨
surfaces: [app, claude-code, api]
principle: []
prevents: []
pitfalls: []
summary: アプリの Web・Desktop・モバイル、Claude Code の各面、API のそれぞれで使えない機能を引ける。使いたい機能がない面では、使える面に移るかを決める。
signs:
  - {type: symptom, text: スマホのアプリだと、Web で使えた機能が出てこない}
  - {type: symptom, text: シークレットチャットではファイルを作ってくれない}
  - {type: goal, text: 使いたい機能がどの面で使えるかを、始める前に確かめたい}
prerequisites: []
related: [choosing-a-surface, claude-code-surfaces, where-it-runs, incognito-chats#limits, voice-and-mobile#mobile, default-safety-settings]
tracks: [incognito, artifacts, file-creation, code-execution, connectors]
outdated_advice: []
sources: [hc-incognito, hc-cowork-and-chat, hc-files, hc-connectors, hc-artifacts, cc-docs-claude-code-on-the-web, cc-docs-settings]
volatility: 高
sections:
  - {title: 早見表（面 × 機能）, anchor: table}
  - {title: 表に出ない面の中の違い, anchor: gaps-within-a-surface}
  - {title: 別の面に移すとき, anchor: moving-between-surfaces}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：アプリ・Claude Code・API のうち、使いたい機能がある面を表で引き、面の中の使えない機能を節で確かめられる。
    - **いつ引くか**：スマホのアプリで Web の機能が出ないとき、シークレットチャットでファイルを作ってもらえないとき、始める前に機能の有無を確かめたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：面の制約・モバイルでできないこと・シークレットチャットでできないこと・機能の対応表
<!-- textlint-enable -->

面ごとにできないことの早見表である。同じ Claude でも、アプリ・Claude Code・API では使える機能が違い、アプリの中でもシークレットチャットやモバイルのように使えない機能がある。表で面を確かめ、足りなければ別の面に移すかを決める。

## 早見表（面 × 機能） {#table}

下の表は、機能ごとに、データで確認できた面を並べたものである。表の「面」の列に載っていない面は、その機能を確認できていない面を指す。「使えないと確認した」という意味ではない。

<!-- gen:begin compare 面 成熟度 確認日 -->
<!-- textlint-disable -->

| 機能 | 面 |
| --- | --- |
| [シークレットチャット（incognito chats）](../app/incognito-chats.md) | アプリ |
| [アーティファクト（artifacts）](../app/artifacts-overview.md) | アプリ・Claude Code |
| [ファイルの作成と編集（create and edit files）](../app/files-and-code-execution.md) | アプリ |
| [コードの実行（code execution。アプリ）](../app/files-and-code-execution.md) | アプリ |
| [コネクタ（connectors）](../app/connectors-in-the-app.md) | アプリ |

すべて共通：成熟度 GA、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare 面 成熟度 確認日 -->

表の読み方は 3 つある。

- 機能の名前が同じでも、面が違えば別の仕組みを使うことがある。たとえばコネクタは、アプリでは「コネクタ」、Claude Code では `mcp`、API では `mcp-connector` に当たる。使いたい面の側の名前で探し直す。
- 表の粒度は「アプリ」「Claude Code」「API」の 3 つである。アプリの中の Web・Desktop・モバイルの差と、シークレットチャットのような使い方による差は、次の節に分けて書く。
- コードの実行は、表ではアプリの機能として載っている。API の code execution tool は別の機能として扱われるので、API で使うときはその側の資料を見る。

## 表に出ない面の中の違い {#gaps-within-a-surface}

同じアプリの中にも、使えない機能がある。制約は段階的に変わるため、2026-10-29 に公式の記事で確かめた内容を書く（記事は展開の途中で、変わりやすい）。

- **シークレットチャット**：新しい体験では、ファイルの作成とコードの実行が使えない。ファイルが要る依頼は、通常の会話で行う。詳しい範囲は <!-- link:begin incognito-chats#limits -->[シークレットチャット（記録を残さない会話） › 使えない機能](../app/incognito-chats.md#limits)<!-- link:end --> にある。
- **統合の後の制約**：Chat と Cowork が 1 つの会話にまとまった後の制約として、公式の統合の記事は次を挙げている。GitHub からの追加、会話の途中からの分岐、古い Cowork タスク（統合の前にアプリで作ったタスク）の検索は使えない。Dispatch という機能は新しいユーザーには提供されない。
- **ローカルの作業**：クラウドで動くタスクは、PC を閉じても続く。ローカルのファイルやアプリを使うタスクは、Desktop を開いておく要がある。この差は <!-- link:begin where-it-runs#what-cloud-cannot-reach -->[実行場所の違い（クラウド・自分の PC・リモート操作） › クラウドで動くときに届かないもの](where-it-runs.md#what-cloud-cannot-reach)<!-- link:end --> で扱う。
- **Claude Code のクラウドのセッション**：user 設定・local 設定・ローカルのプラグインを読まない。手元では効いていた設定が、クラウドでは効かない。面ごとの違いは <!-- link:begin claude-code-surfaces#comparison-table -->[Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル） › 面ごとの違い（表）](claude-code-surfaces.md#comparison-table)<!-- link:end --> で見る。
- **画面操作（computer use）**：使える connector やツールがないときに画面を直接操作する機能で、公式の記事では Desktop の機能として説明されている。優先順位は、connectors、ブラウザ操作、画面操作の順である。Web やモバイルの側で同じ機能を使えるかは確かめていない。
- **モバイル**：タスクの監視・質問への回答・方向の修正・開始はできる。それ以外でモバイルだけ使えない機能は、このページでは確かめていない。範囲は <!-- link:begin voice-and-mobile#mobile -->音声モード・Quick entry・モバイル<!-- link:end --> で確かめる。

## 別の面に移すとき {#moving-between-surfaces}

使いたい機能がない面にいるときは、機能の名前ではなく、やりたい成果から決め直す。「アーティファクトが出ない」ではなく「画面に見える形で成果物がほしい」から考えると、移さずに済む手段が見つかることもある。移すと決めたら、次の 3 つを先に確かめる。

1. **実行場所が変わる**：クラウド・自分の PC・リモート操作のどこで動くかで、触れるファイル・設定・秘密が変わる。<!-- link:begin where-it-runs#how-to-choose -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 選び方と確かめ方](where-it-runs.md#how-to-choose)<!-- link:end --> で確かめる。
2. **記録の残り方が変わる**：シークレットチャットから通常の会話に移すと、履歴とメモリに残る。残したくない理由で選んだ面から出るときは、何を持ち出すかを先に絞る。
3. **安全の既定が変わる**：Claude Code やクラウドに移すと、任せる範囲が広がる。移す前に <!-- link:begin default-safety-settings#defaults-by-surface -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 面ごとの既定（生成の表）](../safety/default-safety-settings.md#defaults-by-surface)<!-- link:end --> で既定を見て、足す設定を決める。

!!! example "判断例：シークレットチャットでスライドを作りたい"
    - **状況**：記録を残したくない相談をシークレットチャットで進めていて、最後に資料のファイルがほしくなった。
    - **迷う候補**：通常の会話に移してファイルを作らせる。または、シークレットチャットでは文章までを作り、ファイルにする作業は自分で行う。
    - **選んだもの**：シークレットチャットで文章まで作り、固有の情報を外した版だけを通常の会話に持ち込んでファイルにする。
    - **理由**：ファイルを作れないのは面の制約であり、記録を残したくない理由は変わらない。通常の会話に移すと履歴とメモリに残るので、持ち込む中身を絞って両方を満たす。

!!! example "判断例：スマホでは出てこない機能を使いたい"
    - **状況**：Web で使えた機能が、スマホのアプリでは出てこない。
    - **迷う候補**：スマホで出る別の手段を探す。または、Web や Desktop を開いて続ける。
    - **選んだもの**：外出先で急がないなら、Web か Desktop を開いて続ける。
    - **理由**：機能が出ない理由は、面の制約か、展開の途中かのどちらかで、手元からは区別しにくい。急ぐ作業だけ、モバイルで出る手段を探す。

移した先で使えるかは、最小の依頼を 1 つ出して確かめる。表の確認日が古いときや、制約が消えたかもしれないときは、公式の記事を見る。「Cowork は別アプリ」といった古い助言は、<!-- link:begin outdated-advice-ledger#cowork-separate-app -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#cowork-separate-app)<!-- link:end --> で今の扱いを確かめられる。今のアプリの形は <!-- link:begin choosing-a-surface#app-chat-and-tasks -->[アプリ・Claude Code・API の選び方 › アプリはチャットとタスクを一つの会話で扱う](choosing-a-surface.md#app-chat-and-tasks)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)：Anthropic・英語・確認日 2026-11-04
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)：Anthropic・英語・確認日 2026-11-04
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [アプリ・Claude Code・API の選び方](choosing-a-surface.md)
- [Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル）](claude-code-surfaces.md)
- [実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)
- [シークレットチャット（記録を残さない会話） › 使えない機能](../app/incognito-chats.md#limits)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
