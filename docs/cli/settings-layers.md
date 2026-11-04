---
id: settings-layers
title: 設定ファイルの階層と優先順位
aliases: [設定ファイルの階層（最小限）, settings.json, settings.local.json, user・project・local・managed, /status, /config]
type: feature
field: cli
chapter: 設定と最初の準備
order: 120
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, チーム]
summary: 設定を、誰に効かせたいかでユーザー・プロジェクト・手元だけ・管理の層に書き分け、効かないときは /status で読み込まれた層を確かめて直せる。同じキーは優先順の高い層が勝つが、権限ルールは層をまたいで合わさる。
signs:
  - {type: symptom, text: settings.json に書いた設定が効いていない}
  - {type: goal, text: 自分だけの設定と、チームで共有する設定を分けたい}
prerequisites: []
related: [permission-rules, share-team-settings, managed-settings-enforcement, permission-modes-overview, isolate-with-safe-mode, output-style-modes, claude-md-loading-order, protecting-secrets, keep-replies-in-japanese#language-setting, commit-and-comment-language#override]
tracks: [settings, managed-settings]
outdated_advice: []
sources: [cc-docs-settings, cc-docs-settings-reference, cc-docs-managed-settings, cc-docs-feature-availability]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 層と優先順位, anchor: layers}
  - {title: 合わさる設定、上書きされる設定, anchor: merge}
  - {title: 効いているかを確かめる, anchor: verify}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：設定を、誰に効かせたいかでユーザー・プロジェクト・手元だけ・管理の層に書き分け、効かないときは `/status` で読み込まれた層を確かめて直せる。
    - **いつ引くか**：`settings.json` に書いた設定が効いていないとき。自分だけの設定と、チームで共有する設定を分けたいとき。
    - **強制力**：管理の層だけが <!-- gen:begin feature managed-settings/enforcement -->鍵<!-- gen:end feature managed-settings/enforcement --> である。ほかの 3 つの層は、本人が書き換えられる。
    - **前提**：なし

<!-- textlint-disable -->
別名：設定ファイルの階層（最小限）・settings.json・settings.local.json・user・project・local・managed・/status・/config
<!-- textlint-enable -->

設定ファイルの階層は、Claude Code が `settings.json` を読む 4 つの層と、同じキーが複数の層にあるときの優先順位のことである。このページが扱うのは、設定を書く層の選び方と、効かないときに読み込まれた層を確かめて直す手順である。キーの一覧は公式の「All settings」に任せる。

## 使いどころ {#when}

設定を書く層を間違えると、縛りたい規則が自分の手元にしか効かない状態になる。チームの規則のつもりでユーザーの層に書けば、仲間のクローンには何も届かない。逆に個人の好みをプロジェクトの層に書いてコミットすれば、全員の設定を変えてしまう。この「縛っていない」状態を、層の選び分けで防ぐ。

層を選ぶ基準は、その設定を誰に効かせたいかである。

- 自分の全プロジェクトに効かせたい：ユーザーの層
- そのリポジトリの全員に効かせたい：プロジェクトの層（コミットする）
- 自分だけ、そのリポジトリだけに効かせたい：手元だけの層（コミットしない）
- 組織として外させたくない：管理の層

任せる幅を広げる設定（`allow` ルールの追加など）は、止めるほうの設定を先に置く。チームのファイルでは、`allow` を足す前に `deny` ルールで読ませないものを決める。`deny` は信頼の前から効き、評価でも先に当たる（<!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->）。利用者に外させない縛りが要るなら、管理の層を使う（<!-- link:begin managed-settings-enforcement -->管理設定と組織の強制（準備中）<!-- link:end -->）。

!!! example "判断例：チームの規則と自分の好み"
    - **状況**：リポジトリで `.env` を Claude に読ませたくない。同時に、自分はスピナーの下のヒントを消したい。
    - **迷う候補**：両方をユーザーの層に書く。または両方をプロジェクトの層に書いてコミットする。
    - **選んだもの**：`.env` の `deny` ルールはプロジェクトの層、ヒントの設定は手元だけの層に書く。
    - **理由**：`.env` の規則は、リポジトリを開く全員に効かせたい。ユーザーの層に書くと、仲間のクローンには届かない。ヒントは個人の好みで、コミットすると仲間の表示まで変わる。

## 層と優先順位 {#layers}

設定ファイルの層は 4 つあり、書いたファイルがどこまで効くかは、置き場所で決まる。

| 層 | ファイル | 効く範囲 |
| --- | --- | --- |
| ユーザー | `~/.claude/settings.json` | 自分の、この機械のすべてのプロジェクト |
| プロジェクト | `.claude/settings.json` | そのフォルダで作業する全員。git のリポジトリならコミットして共有する |
| 手元だけ | `.claude/settings.local.json` | 自分の、そのプロジェクトだけ。コミットしない |
| 管理 | `managed-settings.json` など | 組織が配った先の全員 |

`.claude/settings.local.json` は、Claude Code が作るときは git の対象から外す。手で作ったときは、自分で `.gitignore` に追加する。管理の層は組織が配るもので、利用者が作ったり直したりしない。配り方と中身は <!-- link:begin managed-settings-enforcement -->管理設定と組織の強制（準備中）<!-- link:end --> が持つ。

同じキーが複数の層にあるときは、優先順位の高い層の値が使われる。上の 4 つの層に、ファイルではない起動時の `--settings` を加えた高い順は次のとおりである。

1. 管理：ほかの層も `--settings` も、管理のキーを上書きできない
2. コマンドライン：起動時に `--settings` で渡した JSON。そのセッションだけに効く
3. 手元だけ：`.claude/settings.local.json`
4. プロジェクト：`.claude/settings.json`
5. ユーザー：`~/.claude/settings.json`

環境変数はこの順位の層ではない。`model` のように設定のキーと環境変数が対になるものは、キーと環境変数の組ごとにどちらが勝つかが決まる。キーごとの扱いは、公式の「All settings」で引く。

例外が 2 つある。1 つは、利用者を制限する一部のキーで、下の層に書いた厳しい値が管理の値より優先される場合である。もう 1 つは、`model` の管理の値が既定にとどまり、セッションの中で替えられる場合である。例外の範囲は <!-- link:begin managed-settings-enforcement#cannot-override -->管理設定と組織の強制 › 利用者の側から外せない範囲（準備中）<!-- link:end --> と <!-- link:begin managed-settings-enforcement#precedence -->管理設定と組織の強制 › 優先の順番（準備中）<!-- link:end --> に任せる。

Claude Code は、`~/.claude.json` という第 5 のファイルも持つ。アカウント情報や MCP の設定、フォルダごとの信頼の記録などを Claude Code 自身が書くもので、手で直す前提のファイルではない。このページの層の順位には入らない。

## 合わさる設定、上書きされる設定 {#merge}

同じキーが複数の層にあるとき、値の種類で結果が変わる。単独の値のキー（文字列や真偽値）は、優先順位の高い層の値が選ばれ、低い層の値は捨てられる。リストのキーは、層をまたいで合わさる。

`permissions.allow` のような権限ルールのリストがその例である。ユーザーの層に `allow` ルールがあり、プロジェクトの層にも別の `allow` ルールがあれば、両方が効く。各層は、ほかの層のルールを消さずに自分の分を足せる。組織の `allow` ルールも、利用者の分と並んで効く。管理の層が、利用者の層のルールを使わせない設定を持つ場合は別で、それは <!-- link:begin managed-settings-enforcement -->管理設定と組織の強制（準備中）<!-- link:end --> の範囲である。

リストのキーのうち、モデルの一覧や 1 モデルごとの項目を持つ `fallbackModel`・`modelPicker`・`availableModels`・`modelSettings` は例外で、独自の合わせ方をする。モデルの選び方はこのページの範囲外なので、公式の「All settings」で該当のキーを引く。

層をまたいで合わさるのは、ルールの「集まり」までである。集まったルールのどれが勝つかは、層ではなく評価の順番で決まる。`deny` が先に評価され、次に `ask`、最後に `allow` である。この順番と、パスの書き方で当たらないルールの落とし穴は <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end --> が持つ。たとえば、「今後は確認しない」を選んで手元だけの層に保存された `allow` ルールは、プロジェクトや管理の `ask` ルールより強くはならない。

単独の値のキーの上書きは、`spinnerTipsEnabled`（スピナーの下のヒントの表示）で見ると分かりやすい。ユーザーの層で `false` にした場合を考える。

| ほかの層の状態 | 結果 | 取り戻す方法 |
| --- | --- | --- |
| プロジェクトの層が `true` | そのプロジェクトではヒントが出る | 手元だけの層に `false` を書く |
| 管理の層が `true` | どの層でも消せない | 管理者に相談する。`/status` で、どの管理の源が効いているかを見る |
| 起動時に `--settings` で `true` を渡した | そのセッションだけヒントが出る | 次のセッションで元に戻る |

## 効いているかを確かめる {#verify}

書いた設定が効かないときは、書き直す前に、ファイルが読み込まれているかを確かめる。確かめ方は 2 つある。

1. Claude Code の中で `/status` を開き、Status タブの `Setting sources` の行を見る。読み込まれた層が `User settings` や `Project local settings` のように並ぶ。管理の層が効いていれば、その行がどこから届いたかを示す
2. 拒否された項目は、ターミナルで `claude doctor` を流して見る。形の不正な権限ルールや、未知のフックのイベント名などが出る

`Setting sources` の行は、どのファイルを読んだかを示すだけで、どのキーがどのファイルの値かは示さない。キーごとの出どころは、層の順位（上の節）から自分で突き合わせる。`/status` と `/config` は同じ画面の別のタブで、`/config` の画面は `settings.json` の中身の一覧ではない。

読み込まれているのに効かないときの、典型の原因は次のとおりである。

- **上の層が同じキーを持っている**：手元だけの層・コマンドライン・管理のどれかが、書いた層より上で同じキーを設定している。`/status` に並ぶ層を、上から順に確かめる
- **信頼の前である**：プロジェクトの層の `allow` ルール・`additionalDirectories`・多くの `env` の値は、そのフォルダを信頼するまで効かない。`deny` と `ask` は信頼の前から効く（<!-- link:begin share-team-settings#after-trust -->[チームで設定を共有する › 信頼してから効く設定](../team/share-team-settings.md#after-trust)<!-- link:end -->、<!-- link:begin permission-rules#workspace-trust -->[権限ルール（allow・ask・deny） › 信頼の前に効くもの・後に効くもの](../enforce/permission-rules.md#workspace-trust)<!-- link:end -->）
- **その層では効かない値である**：`permissions.defaultMode` の `auto` と `bypassPermissions` は、プロジェクトと手元だけの層では効かない。ユーザーか管理の層に書くか、起動時に `--permission-mode` で渡す。モードの意味は <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](permission-modes-overview.md#defaults)<!-- link:end --> を引く
- **JSON が壊れている**：設定ファイルは厳密な JSON で、コメントと末尾のカンマは構文エラーになる。対話の起動では「Settings Error」のダイアログが出る。`-p` で動かす場合はダイアログが出ず、壊れたファイルや値を黙って飛ばして続ける
- **起動の後に直した**：多くのキーは保存すれば反映されるが、`model` のように起動時にだけ読むキーは、`/model` などの専用の操作を使うか、起動し直す

!!! example "判断例：プロジェクトの allow を書いたのに確認が出る"
    - **状況**：`.claude/settings.json` に `Bash(npm run test *)` の `allow` ルールを書いたが、クローンしたばかりのリポジトリで毎回確認が出る。
    - **迷う候補**：ルールの書き方が間違っている。または層の順位で、ほかの層に負けている。
    - **選んだもの**：先に、フォルダを信頼する前ではないかを確かめる。
    - **理由**：`/status` にプロジェクトの層が並んでいれば、ファイルは読まれている。プロジェクトの `allow` は信頼の後に効く。だから信頼の前なら、書き方が合っていても確認が出る。信頼の後でも出るなら、`claude doctor` で拒否された項目を見る。

設定の読み込みを疑うときに、読む層をユーザー・プロジェクト・手元だけから選んで起動する `--setting-sources` が使える。管理の層は絞れない。設定を外して挙動を比べる手順は <!-- link:begin isolate-with-safe-mode#what-is-disabled -->[設定を外して切り分ける（--safe-mode） › 外れるもの・残るもの](isolate-with-safe-mode.md#what-is-disabled)<!-- link:end --> が持つ。

## 雛形 {#templates}

チームで共有する設定と、自分だけの上書きの 2 つの雛形を載せる。どちらも動作を試した結果ではなく、公式の文書の例に沿った書き方の雛形である。

<!-- gen:begin snippet settings-layers/team-shared -->
<!-- textlint-disable -->

??? example "雛形：チームで共有する設定（.claude/settings.json）"

    ```json
    {
      "permissions": {
        "allow": [
          "Bash(npm run lint)",
          "Bash(npm run test *)"
        ],
        "deny": [
          "Read(./.env)",
          "Read(./.env.*)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet settings-layers/team-shared -->

<!-- gen:begin snippet settings-layers/personal-local -->
<!-- textlint-disable -->

??? example "雛形：自分だけの上書き（.claude/settings.local.json）"

    ```json
    {
      "spinnerTipsEnabled": false
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet settings-layers/personal-local -->

編集中の補完のために、ファイルの先頭に `$schema` の行を足すこともできる。ただし、公式の文書が案内するスキーマは新しい版に追いつかないことがあり、最近足されたキーを正しく書いても警告が出る。警告が出ても、設定が誤りとは限らない。実際に効いているかは、`/status` と `claude doctor` で確かめる。

## 効かない場面・落とし穴 {#limits}

- **管理の層は外せない**：利用者の側の設定では、管理の層が決めた規則を外せない。組織の規則に当たったときは、管理者に相談する。強制の仕組みは <!-- link:begin managed-settings-enforcement -->管理設定と組織の強制（準備中）<!-- link:end --> が持つ
- **クラウドのセッションは、ユーザーと手元だけの層を読まない**：別の機械で動くので、自分の機械にある 2 つのファイルは届かない。コミットしたプロジェクトの層は、クローンの一部として読まれる
- **共有の層に秘密を入れない**：プロジェクトの層はコミットされ、全員に渡る。API キーや認証情報は置かない。読ませない設定は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> に従う。何を共有して何を個人に残すかは <!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end --> が持つ
- **設定は、指示の層とは別である**：`settings.json` は動作を決める設定で、`CLAUDE.md` は読ませる指示（お願い）である。本人が書き換えられない鍵になるのは、管理の層だけである。後者の重なりは <!-- link:begin claude-md-loading-order -->[CLAUDE.md の階層と読み込み順](../extend/claude-md-loading-order.md)<!-- link:end --> で確かめる
- **IDE の拡張とデスクトップアプリ**：公式の文書は同じファイルを読むと書いている。このページでは動作を確かめていない（未確認）

## 比べる相手 {#compare}

設定の層を選ぶときに、近い役目のページと分担する。

- チームで共有する手順（何をコミットし、何を個人に残すか）：<!-- link:begin share-team-settings -->[チームで設定を共有する](../team/share-team-settings.md)<!-- link:end -->
- 組織として外させない規則：<!-- link:begin managed-settings-enforcement -->管理設定と組織の強制（準備中）<!-- link:end -->
- 許可・確認・拒否のルールそのもの：<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->
- 権限モードの既定と切り替え：<!-- link:begin permission-modes-overview -->[権限モードの選び方](permission-modes-overview.md)<!-- link:end -->
- 応答の仕方の設定：<!-- link:begin output-style-modes -->[出力スタイルで応答の仕方を切り替える](output-style-modes.md)<!-- link:end -->
- 言語の設定を層の例として見る：<!-- link:begin keep-replies-in-japanese#language-setting -->[日本語で返し続けさせる › 言語の設定と、効かないときに確かめること](../japanese/keep-replies-in-japanese.md#language-setting)<!-- link:end -->、共有の設定が個人の設定を上書きする場合は <!-- link:begin commit-and-comment-language#override -->コミットメッセージ・コメントの言語 › 共有の設定の言語は個人の設定を上書きする（準備中）<!-- link:end -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Deploy managed settings](https://code.claude.com/docs/en/managed-settings)：Anthropic・英語・確認日 2026-11-04
- [Feature availability](https://code.claude.com/docs/en/feature-availability)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [設定を外して切り分ける（--safe-mode）](isolate-with-safe-mode.md)
- [チームで設定を共有する](../team/share-team-settings.md)
- 管理設定と組織の強制（準備中）

**関連**

- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [権限モードの選び方](permission-modes-overview.md)
- [出力スタイルで応答の仕方を切り替える](output-style-modes.md)
- [CLAUDE.md の階層と読み込み順](../extend/claude-md-loading-order.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [日本語で返し続けさせる › 言語の設定と、効かないときに確かめること](../japanese/keep-replies-in-japanese.md#language-setting)
- コミットメッセージ・コメントの言語 › 共有の設定の言語は個人の設定を上書きする（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
