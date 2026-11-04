---
id: writing-safe-hooks
title: フックを安全に書く
aliases: [onFailure, fail-open, フックの exec 形式, 他人のフックを確かめる]
type: feature
field: enforce
chapter: フック
order: 110
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: フックは失敗すると操作を通してしまう既定を知り、止める用途で失敗を止めに倒す書き方ができる。他人のフックは、コードとして確かめてから使う。
signs:
  - {type: symptom, text: 止めるはずのフックが、エラーのときは何も止めていなかった}
  - {type: situation, text: 他人のリポジトリやプラグインのフックを使おうとしている}
  - {type: symptom, text: 関係のない道具の呼び出しまでフックに止められる}
prerequisites: [hooks-basics]
related: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing, permission-rules]
tracks: [hooks]
sources: [cc-docs-hooks, cc-docs-hooks-guide, cc-docs-sandboxing, cc-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 既定は失敗すると通す（fail-open）, anchor: fail-open}
  - {title: matcher で止めすぎない, anchor: matcher}
  - {title: シェルを通さずに起動する（args）, anchor: exec-form}
  - {title: フックは利用者の権限で動く, anchor: runs-as-you}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と比べる相手, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：止める用途のフックを、失敗しても操作を通さない形で書ける。他人のフックは、コードとして確かめてから使う
    - **いつ引くか**：止めるはずのフックが、エラーのときは何も止めていなかったとき。他人のリポジトリやプラグインのフックを使う前。関係のない道具の呼び出しまでフックに止められるとき
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。ただし鍵として働くのは、フックが正しく動いている間だけである。壊れたフックは、何も止めずに操作を通す
    - **前提**：<!-- link:begin hooks-basics -->[フックの考え方とイベント](hooks-basics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：onFailure・fail-open・フックの exec 形式・他人のフックを確かめる
<!-- textlint-enable -->

フックを安全に書くとは、フックが壊れたときの挙動を先に知り、止めたい操作を止めたままにする書き方である。このページは、失敗したときに通してしまう既定、matcher の当たり方、シェルを通さない起動、他人のフックを使うときの確かめ方を扱う。

## 使いどころ {#when}

止める用途のフックを常設する段階で、最初に読む。「`.env` を触らせない」のように例外なく守らせたい規則は、CLAUDE.md の依頼ではなく PreToolUse のフックで止めるのが強制になる。ただし、その鍵はフックが壊れたときにも閉じたままとは限らない。壊れたときの挙動を先に知っておく必要がある。

このページが防ぐ原因は 2 つである。

- **縛っていない**：縛ったつもりのフックが、エラーのときに何も止めていない。matcher が外れて、止めたい操作に当たっていない場合も含む
- **境界がない**：フックは利用者の権限で動く。他人が書いたフックを入れると、その人のコードを自分の権限で走らせることになる

フックの考え方とイベントは <!-- link:begin hooks-basics#events -->[フックの考え方とイベント › 代表的なイベント](hooks-basics.md#events)<!-- link:end --> にある。止めた理由と代わりの手段を返す書き方は <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](block-with-exit-2.md#reason)<!-- link:end --> を見る。

## 既定は失敗すると通す（fail-open） {#fail-open}

フックには、失敗すると操作を止めずに通す既定がある（fail-open）。止めるための仕組みが、壊れたときには何も止めないということだ。

次の失敗は、どれも「止めない誤り」として扱われ、操作は進む。

| 失敗の形 | 何も付けないとき | `onFailure` を付けたとき |
| --- | --- | --- |
| フックを起動できない（実行ファイルが無い・依存が欠けている） | 通る | 止まる |
| 0 と 2 以外の終了コードで終わる（exit 1 を含む） | 通る | 止まる |
| タイムアウトになる | 通る | 止まる |
| 出力の JSON が壊れている | 通る | 止まる |
| スクリプトの中で失敗したが、最後は 0 で終わる | 通る | 通る |

止める用途のフックには、`"onFailure": "block"` を付ける。フックの失敗を exit 2 と同じ「止める」に扱うキーで、command と http のフックに使える。使えるのは <!-- fact:begin hook-on-failure-block-min-version -->Claude Code 2.1.295 以降（2026-11-05 時点）<!-- fact:end --> である。

`onFailure` で足りない所が 2 つある。

- **スクリプトの内側の失敗は拾えない**。表の最後の行のとおり、`jq` が無くて途中のコマンドが失敗しても、スクリプトが最後に 0 で終われば通る。判定に要る道具の有無は、スクリプトの先頭で確かめ、無ければ自分で exit 2 にする。雛形の `guard-migrations.sh` がその形である
- **効かないフックの種類がある**。Stop・SubagentStop・TaskCompleted・TeammateIdle のフックと、非同期のフックには、`onFailure` は効かない。これらで「失敗したら止める」を期待しない

!!! example "判断例：jq で入力を読むフックの失敗をどう止めるか"
    - **状況**：migrations の既存ファイルの書き換えを止めるフックを、`jq` で入力の JSON を読む bash のスクリプトで書いた。同僚の環境には `jq` が入っていないかもしれない。
    - **迷う候補**：`onFailure: "block"` だけを付ける／スクリプトの先頭で `jq` の有無を確かめて、無ければ exit 2 で終える／その両方。
    - **選んだもの**：両方。
    - **理由**：`jq` の欠落でスクリプトがそのまま異常終了するなら、`onFailure` が止める。しかし `path=$(… | jq …)` のように失敗が空の文字列になって後続の判定へ進み、最後は 0 で終わると、`onFailure` があっても通る。スクリプトの先頭の確認が、この抜け道を塞ぐ。`onFailure` は、確認に漏れた失敗を拾う二重の備えになる。

フックを入れたら、壊れたときに本当に止まるかを一度試す。スクリプトのファイル名を一時的に変えて起動できなくし、止めたい操作を Claude に頼んで、止められることを見る。`jq` の欠落は、PATH から外したシェルで試す。フックが動いていないように見えるときの切り分けは <!-- link:begin hooks-basics#not-running -->[フックの考え方とイベント › 動いていないように見えるとき](hooks-basics.md#not-running)<!-- link:end --> にある。

## matcher で止めすぎない {#matcher}

matcher は、どの道具の呼び出しにフックを走らせるかを決める。書き方で当たり方が変わるので、止めたい範囲と実際に当たる範囲が合っているかを確かめる。

| matcher の書き方 | 扱い | 例 |
| --- | --- | --- |
| 文字・数字・`_`・`-`・空白・`,`・`\|` だけ | 完全一致。`\|` か `,` で並べる | `Edit\|Write` は Edit か Write にだけ当たる |
| ほかの文字を含む | 前後を固定しない正規表現 | `Edit.*` は NotebookEdit にも当たる |
| `^…$` で囲む | 前後を固定した正規表現 | `^Edit$` は Edit にだけ当たる |

- 大文字と小文字は区別される
- MCP の道具は `mcp__サーバー名__.*` のように、サーバー単位で当てる
- matcher を配列で書くと無効になる。PreToolUse と PermissionRequest の下では、同じ設定ファイルのほかのフックも読まれない。複数を当てたいときは `|` で並べる

止めすぎを避ける基本は、完全一致か `^…$` で書くことだ。`.*` を使うと、名前が似た別の道具まで巻き込む。逆に狭すぎると止めたい操作が抜ける。止めたい操作と通したい操作の両方を 1 つずつ実際に呼んで、止まる側だけが止まることを見る。

`if` のフィールドに権限ルールの構文（`Bash(rm *)` など）を書くと、フックを走らせる呼び出しを絞れる。ただし、書けるのは 1 つの規則だけで、`&&` や `||` はない。Bash の判定は best-effort で、コマンドを読み切れないときは規則にかかわらずフックが走る。`if` はフックの呼び出し回数を減らすために使い、止めるかどうかの判定はスクリプトの中でも行う。

関係のない呼び出しまで止められているときは、止めた記録から原因の規則を探して絞り直す。その見直し方は <!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end --> にある。

## シェルを通さずに起動する（args） {#exec-form}

フックの `command` は、既定ではシェルを通して実行される。`args` を足すと、`command` を実行ファイルとしてシェルなしで起動し、`args` の各要素をそのまま 1 つの引数として渡す。公式は、`${CLAUDE_PROJECT_DIR}` などの置き換えを使うフックには `args` を付けるよう勧めている。

| 書き方 | 起動のされ方 | 注意 |
| --- | --- | --- |
| `command` だけ（シェル形） | シェルが文字列を解釈する | 空白を含むパスや特殊な文字が展開され、別の引数や別のコマンドになりうる。二重引用符で囲む |
| `command` と `args`（exec 形式） | シェルを通さず、要素ごとに 1 つの引数 | パイプ・リダイレクト・glob は使えない。それらはスクリプトの中に書く |

効くのは、パスに空白を含むリポジトリや、置き換えた値に特殊な文字が混じりうる場面である。シェル形では、二重引用符を忘れた 1 か所が、止めるはずのフックの不発や、意図しないコマンドの実行になる。exec 形式なら、その事故の入口が無い。

雛形の設定は、`bash` を実行ファイルにして、スクリプトのパスを `args` で渡している。

## フックは利用者の権限で動く {#runs-as-you}

フックは、ハンドラの種類にかかわらず、利用者の権限で任意のコードを動かす。コマンドのフックは、利用者のファイルを読み書きでき、利用者のネットワークに出られる。公式も、プラグインやリポジトリ由来のフックは確かめてから使うよう警告している。

フックはサンドボックスの外でも動く。組み込みのファイルと Web の道具、フック、MCP などは、サンドボックスの囲いの外にある。サンドボックスを入れていても、フックのスクリプトは守られない。何が囲われ、何が囲われないかは <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](sandboxing.md#scope)<!-- link:end --> にある。

このため、守りは 2 方向に要る。

**自分で書くフック**は、壊す操作を入れない。止める判定は入力を読むだけにして、ファイルの削除や書き換えをしない。外へ送る処理も入れない。

**他人のフック**は、CI の定義と同じように、コードとして読んでから使う（類推）。AI の設定ファイル（`.claude/settings.json` のフックなど）も、他人のものはレビューしてから使う。確かめる流れは次のとおり。

1. **置き場所を洗い出す**。フックは、ユーザー・プロジェクト・ローカルの設定、管理設定、プラグインの `hooks/hooks.json`、スキルとサブエージェントの先頭の設定に書ける。すべてがマージされて効くので、1 か所だけ見ても足りない。`/hooks` で効いている一覧を見られる。置き場所の全体は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](hooks-basics.md#locations)<!-- link:end --> にある
2. **起動するものを読む**。`command` と `args` が何を起動するか、参照しているスクリプトの中身、外へ出す通信（http のフックは入力の JSON を送り出す）を読む。読み切れないものは使わない
3. **開く前に見る**。知らないリポジトリでは、開くだけでフックが動きうる。開く前に見るファイルと、信頼の確認の前後で効くものは <!-- link:begin before-opening-unknown-repos#files-to-check -->[知らないリポジトリを開く前に › 開く前に見るファイル](../safety/before-opening-unknown-repos.md#files-to-check)<!-- link:end --> と <!-- link:begin before-opening-unknown-repos#trust -->[知らないリポジトリを開く前に › 信頼の前と後で効くもの](../safety/before-opening-unknown-repos.md#trust)<!-- link:end --> にある
4. **入れた後の変更を追う**。取り込んだ後に、スクリプトの中身が変わることもある。更新のたびに差分を見る。プラグインやスキルを入れる前の確認の全体は <!-- link:begin vetting-extensions#read-contents -->[MCP・プラグイン・スキルを入れる前の確認 › 中身を読む（道具の説明・フック・スクリプト）](../safety/vetting-extensions.md#read-contents)<!-- link:end --> と <!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end --> にある

## 雛形 {#templates}

migrations の既存ファイルを止めるフックを、失敗を止めに倒す形で書いた例を 2 つ載せる。設定が `onFailure` と `args` を使い、スクリプトが依存の有無を先頭で確かめる。

設定の例。

<!-- gen:begin snippet writing-safe-hooks/fail-closed-settings -->
<!-- textlint-disable -->

??? example "雛形：失敗したら止める設定（onFailure と args）"

    ```json
    {
      "hooks": {
        "PreToolUse": [
          {
            "matcher": "Edit|Write",
            "hooks": [
              {
                "type": "command",
                "command": "bash",
                "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/guard-migrations.sh"],
                "onFailure": "block"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.1.295。

<!-- textlint-enable -->
<!-- gen:end snippet writing-safe-hooks/fail-closed-settings -->

スクリプトの例。

<!-- gen:begin snippet writing-safe-hooks/guard-migrations -->
<!-- textlint-disable -->

??? example "雛形：依存の有無を確かめてから判定するフックのスクリプト"

    ```bash
    #!/usr/bin/env bash
    # .claude/hooks/guard-migrations.sh
    # PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
    # 失敗は止めに倒す：判定に要る道具が無い・入力が読めないときは exit 2 で終える。
    # 終わり方は exit 0（通す）か exit 2（止める）のどちらかに決め、途中の失敗を 0 で終わらせない。

    if ! command -v jq >/dev/null 2>&1; then
      echo "jq が見つからず判定できないため、操作を止める。jq を入れてから再開する。" >&2
      exit 2
    fi

    input=$(cat)
    path=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty') || {
      echo "フックの入力を読めず判定できないため、操作を止める。" >&2
      exit 2
    }

    case "$path" in
      */migrations/*)
        if [ -e "$path" ]; then
          echo "このリポジトリでは、適用済みの migration は書き換えない。変更は新しい番号の migration ファイルを追加して行う。（対象：$path）" >&2
          exit 2
        fi
        ;;
    esac

    exit 0
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet writing-safe-hooks/guard-migrations -->

どちらも、このまま常設せず、作業用のリポジトリで次を試してから使う。

- スクリプトのファイル名を変えて起動できなくした状態で、止めたい操作が止まる
- ファイル名を変えたまま設定の `onFailure` の行を外すと、同じ操作が通る。通ることを見て、`onFailure` が効いていることを確かめる
- migrations の下の新しいファイルは、止められずに通る

止めた後に Claude が回り込まないように、理由と代わりの手段を返す書き方は <!-- link:begin block-with-exit-2#templates -->[フックで止めて理由を返す（exit 2 と JSON） › 雛形](block-with-exit-2.md#templates)<!-- link:end --> にある。代表的なフックの組み方は <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](hook-recipes.md#block-dangerous)<!-- link:end --> を見る。

## 効かない場面と比べる相手 {#limits}

- **スクリプトの内側の失敗**：最後に 0 で終われば、`onFailure` があっても通る。依存の有無はスクリプトで確かめる
- **フックが見ていない経路**：フックが判定するのは、matcher に当たった道具の呼び出しだけである。同じファイルを別の道具から触れるなら、matcher を広げるか、権限ルールを重ねる
- **版の古い環境**：`onFailure` が使えない版では、キーが効かない。使える版は「既定は失敗すると通す（fail-open）」の節で確かめ、古い環境では、スクリプトの側の確認だけが守りになる
- **ほかの OS と IDE 拡張**：本文の動作は WSL・Linux の CLI を基準にしている。ほかの OS と IDE 拡張での動作は未確認である

比べる相手は次のとおり。

| 守りたいこと | 向くもの | このページとの関係 |
| --- | --- | --- |
| パスやコマンドを単に禁じる | <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](permission-rules.md)<!-- link:end --> の deny ルール | スクリプトが無いので、スクリプトの失敗で開くことがない。条件付きの判定や理由の返却が要るときにフックを足す |
| 条件付きで止め、理由と代わりを返す | <!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)<!-- link:end --> | 返し方はそちら。失敗したときに止める書き方はこのページ |
| 縛る規則を増やしすぎた | <!-- link:begin lock-side-effects#what-to-lock -->縛りすぎの害と見直し（止めすぎ・回り込み） › 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）（準備中）<!-- link:end --> | 止めすぎと回り込みの見直しはそちら |

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [フックの考え方とイベント](hooks-basics.md)

**次に読む**

- [代表的なフックのレシピ](hook-recipes.md)

**関連**

- [フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)
- 縛りすぎの害と見直し（止めすぎ・回り込み）（準備中）
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [サンドボックスで封じ込める](sandboxing.md)
- [権限ルール（allow・ask・deny）](permission-rules.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
