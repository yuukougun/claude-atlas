---
id: hook-recipes
title: 代表的なフックのレシピ
aliases: [フックの例, hooks の例, フォーマッタのフック, 危ないコマンドを止めるフック]
type: recipe
field: enforce
chapter: フック
order: 120
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム]
summary: 編集後の整形・危ない操作の遮断・決めたコマンドへの誘導・テスト出力の絞り込み・終わりの通知・担当にだけ禁じる操作を、フックで組める。どの型も、当てる範囲を狭くし、効いたかを確かめてから常設する。
signs:
  - {type: goal, text: 編集のたびにフォーマッタをかけさせたい}
  - {type: goal, text: pip ではなく uv のように、決めたコマンドを必ず使わせたい}
  - {type: goal, text: テストやログの出力で会話が埋まるのを防ぎたい}
  - {type: goal, text: サブエージェントにだけ commit を禁じたい}
prerequisites: [block-with-exit-2, writing-safe-hooks]
related: [hooks-basics, stop-hooks, textlint-hook, protecting-secrets, destructive-commands, what-to-put-in-claude-md#what-to-write, freeze-eval-assets, lock-side-effects, writing-subagents, what-subagents-dont-inherit, completion-notifications]
tracks: [hooks]
sources: [cc-docs-hooks, cc-docs-hooks-guide, cc-docs-features-overview]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: フックを登録する, anchor: register}
  - {title: 編集の後に整形する, anchor: format-after-edit}
  - {title: 危ない操作を止める, anchor: block-dangerous}
  - {title: 決めたコマンドへ誘導する（pip の代わりに uv など）, anchor: redirect-commands}
  - {title: テストの出力を絞る, anchor: filter-test-output}
  - {title: 終わったら知らせる, anchor: notify}
  - {title: 担当にだけ禁じる（agent_id）, anchor: subagent-only}
  - {title: 常設する前に確かめる, anchor: verify}
  - {title: 動かないとき・止めすぎるとき, anchor: failures}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：整形・危ない操作の遮断・決めたコマンドへの誘導・出力の絞り込み・通知・担当だけへの禁止を、フックで組める
    - **いつ引くか**：編集のたびにフォーマッタをかけさせたいとき。pip ではなく uv のように、決めたコマンドを必ず使わせたいとき。テストやログの出力で会話が埋まるとき。サブエージェントにだけ commit を禁じたいとき
    - **前提**：<!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)<!-- link:end -->、<!-- link:begin writing-safe-hooks -->[フックを安全に書く](writing-safe-hooks.md)<!-- link:end -->

<!-- textlint-disable -->
別名：フックの例・hooks の例・フォーマッタのフック・危ないコマンドを止めるフック
<!-- textlint-enable -->

代表的なフックのレシピは、よくある 6 つの用途に、そのまま写せる雛形を付けたものである。どの型も、フックを当てる範囲を狭くし、動いたことを確かめてから常設する。CLAUDE.md に書いたお願いが守られない行を、フックという鍵に移すときの具体例として引く。

## 先に整える守り {#guards}

フックは、書き方を誤ると静かに効かなくなる。レシピを写す前に、次の 3 つを整える。

- **止める型は、理由と代わりの手段を返す**。止めるだけだと、Claude は別の道具で同じことをしようとする。返し方は <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](block-with-exit-2.md#reason)<!-- link:end --> に従う
- **止める用途では、フックの失敗を止めに倒す**。フックは、既定ではスクリプトが失敗すると操作を通す。ポリシーとして止めたい規則は、この既定を知ったうえで書く。<!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end --> を見る
- **当てる範囲を狭くする**。`matcher` を道具の名前に絞り、スクリプトの中でも対象を絞る。広く当てると、関係のない操作まで止める。<!-- link:begin writing-safe-hooks#matcher -->[フックを安全に書く › matcher で止めすぎない](writing-safe-hooks.md#matcher)<!-- link:end --> を見る

縛る規則そのものは、機械で判定でき、破ったときの害が大きいものに絞る。選び方は <!-- link:begin lock-side-effects#what-to-lock -->縛りすぎの害と見直し（止めすぎ・回り込み） › 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）（準備中）<!-- link:end --> にある。判断を含む規則（何が小さな直しか、など）は、フックにせず CLAUDE.md に任せる。

他人が書いたフックを入れるときは、利用者の権限で動くコードなので、中身を読んでから使う（<!-- link:begin writing-safe-hooks#runs-as-you -->[フックを安全に書く › フックは利用者の権限で動く](writing-safe-hooks.md#runs-as-you)<!-- link:end -->）。

## フックを登録する {#register}

このページのレシピは、どれも同じ手順で入れる。スクリプトを `.claude/hooks/` に置き、`.claude/settings.json` に登録する。次の設定は、このページの 5 つのスクリプトと、通知の 2 つをまとめて登録する例である。要るものだけを残して使う。止める用途で使うときは、<!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end --> の書き方（失敗したときに止める設定など）に直す。

<!-- gen:begin snippet hook-recipes/register-hooks -->
<!-- textlint-disable -->

??? example "雛形：このページのフックをまとめて登録する設定"

    ```json
    {
      "hooks": {
        "PostToolUse": [
          {
            "matcher": "Edit|Write",
            "hooks": [
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format-after-edit.py"
              }
            ]
          }
        ],
        "PreToolUse": [
          {
            "matcher": "Bash",
            "hooks": [
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-bash.py"
              },
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/redirect-pip-to-uv.py"
              },
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/filter-test-output.py"
              },
              {
                "type": "command",
                "if": "Bash(git *)",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/deny-subagent-commit.py"
              }
            ]
          }
        ],
        "Notification": [
          {
            "matcher": "permission_prompt|idle_prompt",
            "hooks": [
              {
                "type": "command",
                "command": "notify-send 'Claude Code' '確認か入力を待っている'"
              }
            ]
          }
        ],
        "Stop": [
          {
            "hooks": [
              {
                "type": "command",
                "command": "notify-send 'Claude Code' '作業が終わった'"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/register-hooks -->

読み方は次のとおり。

- `matcher` は、フックを走らせる道具の名前（`Edit|Write`、`Bash`）。Notification では通知の種類を指す
- `if` は、権限ルールの書き方で 1 つだけ指定する絞り込みである。`Bash(git *)` と書くと、git を含むコマンドのときだけ走る。ただし `if` の判定は best-effort で、Bash のコマンドを読み取れないときは、フックが走る。確実に止めたいなら、deny ルールと組む
- 同じ `Bash` の matcher の下に、4 つのフックが並ぶ。それぞれが自分の対象だけを判定し、当たらなければ何もせずに終わる

登録したら、`/hooks` の一覧に出ることを確かめる。ここで出なければ、後の節のフックは動かない。置き場所と効く範囲は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](hooks-basics.md#locations)<!-- link:end --> にある。

## 編集の後に整形する {#format-after-edit}

編集のたびにフォーマッタをかけさせたいときは、PostToolUse の `Edit|Write` にフックを置く。CLAUDE.md に「整形してから終える」と書くより、毎回確実に走る。

手順は次のとおり。

1. スクリプトを `.claude/hooks/format-after-edit.py` に置く。確かめ：`ruff` が PATH にあり、手で `ruff format <ファイル>` が通る
2. 「フックを登録する」の節の設定で登録する。確かめ：`/hooks` に PostToolUse の `Edit|Write` が出る
3. Claude に整形の崩れた Python のファイルを 1 行直させる。確かめ：直した直後に、ファイル全体が整形された状態になる

<!-- gen:begin snippet hook-recipes/format-after-edit -->
<!-- textlint-disable -->

??? example "雛形：編集の後に ruff format をかけるフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/format-after-edit.py
    # PostToolUse（Edit・Write）で、書き換えた Python のファイルに ruff format をかける。
    # 整形に失敗したら exit 2 で stderr を返す。PostToolUse は操作を止められないが、
    # stderr の文は Claude に届くので、構文エラーなどを直させられる。
    import json
    import subprocess
    import sys

    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")

    # 当てる範囲を狭くする：Python のファイルだけ
    if not path.endswith(".py"):
        sys.exit(0)

    try:
        result = subprocess.run(
            ["ruff", "format", path], capture_output=True, text=True, timeout=30
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        # フォーマッタが無い・遅いときは、何もせず通す（整形は止める用途ではない）
        sys.exit(0)

    if result.returncode != 0:
        print(
            f"ruff format が失敗した。構文エラーなら該当の行を直す。（対象：{path}）\n"
            f"{result.stderr}",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/format-after-edit -->

見るべき点が 3 つある。

- 対象は拡張子で絞る。すべてのファイルに同じフォーマッタをかけると、設定ファイルや文書まで書き換わる
- PostToolUse の時点では、編集は終わっている。exit 2 でも操作は止められないが、stderr は Claude に返るので、整形が失敗した理由（構文エラーなど）を直させる用途に使える
- フォーマッタが無い環境では、何もせずに通す。整形は止める用途ではないので、失敗を通す側に倒してよい

日本語の文書の表記を機械で揃える textlint の型は <!-- link:begin textlint-hook -->[textlint をフックで回す](../japanese/textlint-hook.md)<!-- link:end --> が持つ。ここでは繰り返さない。

## 危ない操作を止める {#block-dangerous}

取り返しのつかない Bash のコマンドを、実行の前に止めるには、PreToolUse の `Bash` にフックを置き、理由と代わりを返す。

手順は次のとおり。

1. 止める操作を、機械で判定できるものに絞って決める。確かめ：1 つの操作が、1 つの照合の式に対応する
2. 止めるときに返す文を、理由と代わりの手段の組で書く。確かめ：その文だけを読んで、次に何をすればよいかが分かる
3. 壊れても困らない場所で、止めたい操作を実際に頼む。確かめ：止められ、返した文が Claude に見える

<!-- gen:begin snippet hook-recipes/block-dangerous-bash -->
<!-- textlint-disable -->

??? example "雛形：危ない Bash のコマンドを止めて理由を返すフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/block-dangerous-bash.py
    # PreToolUse（Bash）で、取り返しのつかない操作を止め、理由と代わりを返す。
    # 文字列の照合なので、書き方を変えた同じ操作は拾えない。確実に止めたい操作は deny ルールと組む。
    import json
    import re
    import sys

    # (照合する式, 止める理由と代わりの手段)
    DANGEROUS = [
        (
            r"\brm\s+-[a-zA-Z]*(?:rf|fr)[a-zA-Z]*\s+(?:/|~|\$HOME|\.|\*)(?:\s|$)",
            "ルート・ホーム・カレントディレクトリ全体の再帰削除は止めた。"
            "消したい対象を具体的なパスで指定し直す。",
        ),
        (
            r"\bgit\s+push\b.*(?:--force(?![-\w])|\s-f(?:\s|$))",
            "git push の強制上書きは止めた。"
            "上書きが要るなら --force-with-lease を使うか、利用者に確認する。",
        ),
        (
            r"\bgit\s+reset\s+--hard\b",
            "git reset --hard は未コミットの変更を消すので止めた。"
            "戻したいファイルを git restore で指定するか、git stash で退避する。",
        ),
    ]

    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")

    for pattern, reason in DANGEROUS:
        if re.search(pattern, command):
            result = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
            print(json.dumps(result, ensure_ascii=False))
            break

    sys.exit(0)
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/block-dangerous-bash -->

この雛形のスクリプトは、自分が落ちたときに操作を通す既定のままである。止める規則として常設するなら、「先に整える守り」の節で指した方法で、失敗を止めに倒す。

このレシピは、コマンドの文字列を照合している。そのため、書き方を変えた同じ操作（`git -C . push -f` のように、オプションの位置を変えたもの）は拾えないことがある。照合に抜けがあると分かったうえで、使い方を決める。

- 抜けがあっても害が小さい操作は、このフックで止める
- 抜けが許されない操作（秘密の読み取り、消えたら戻らないデータ）は、フックだけに頼らない。権限ルールとサンドボックスを重ねる。<!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> と <!-- link:begin destructive-commands#guard -->[消されたくないもの（破壊的コマンド） › 確認を求めさせる頼み方と、鍵](../safety/destructive-commands.md#guard)<!-- link:end --> を見る

フックの判定と権限ルールの評価の順番は <!-- link:begin block-with-exit-2#precedence -->[フックで止めて理由を返す（exit 2 と JSON） › 権限ルールとの順番](block-with-exit-2.md#precedence)<!-- link:end --> にある。

## 決めたコマンドへ誘導する（pip の代わりに uv など） {#redirect-commands}

プロジェクトで決めたコマンドを使わせたいときは、決めていないコマンドを PreToolUse で止め、決めたコマンドを理由として返す。Claude は、uv を使うプロジェクトでも、pip に戻ったり `uv pip install` を使ったりすることがある。

手順は次のとおり。

1. 決めたコマンドを CLAUDE.md に書く。確かめ：新しい会話で、Claude が決めたコマンドを最初から使うか
2. 守られない回数が続くなら、フックを足す。スクリプトを `.claude/hooks/redirect-pip-to-uv.py` に置いて登録する。確かめ：`/hooks` に出る
3. `pip install` を頼む。確かめ：止められ、`uv add` と `uv run` を案内する理由が見え、続けて Claude が uv に切り替える

<!-- gen:begin snippet hook-recipes/redirect-pip-to-uv -->
<!-- textlint-disable -->

??? example "雛形：pip を止めて uv を案内するフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/redirect-pip-to-uv.py
    # PreToolUse（Bash）で、pip での導入を止め、決めたコマンド（uv）を理由とともに返す。
    # 「uv pip install」は先頭が uv なので照合に当たらない。許すかどうかは規則として決める。
    import json
    import re
    import sys

    # コマンドの各部分の先頭にある pip（python -m pip を含む）の install・uninstall
    PIP = re.compile(
        r"(?:^|&&|\|\||;|\|)\s*(?:python3?\s+-m\s+)?pip3?\s+(?:install|uninstall)\b"
    )

    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")

    if PIP.search(command):
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    "このリポジトリでは Python の依存を uv で管理する。pip は使わない。"
                    "パッケージの追加は `uv add <名前>`、コマンドの実行は `uv run <コマンド>` で行う。"
                ),
            }
        }
        print(json.dumps(result, ensure_ascii=False))

    sys.exit(0)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/redirect-pip-to-uv -->

!!! example "判断例：決めたコマンドを守らせる手段の選び方"
    - **状況**：uv で依存を管理するリポジトリで、Claude が pip で導入しようとする。
    - **迷う候補**：CLAUDE.md に 1 行書く／PreToolUse のフックで止めて uv を案内する／PATH に pip を差し替えるラッパーを置く。
    - **選んだもの**：CLAUDE.md に 1 行書き、それでも守られない回数が続くときにフックを足す。
    - **理由**：コマンドの指定は、まず指示で足りることが多い。指示で足りない場合は、機械で判定できるフックへ移す。フックの `if` の判定は best-effort なので、フックでも抜けるなら、PATH の差し替えを使った実践者の例もある（根拠：弱）。ただし PATH の差し替えは環境に依存するため、手段の 1 つとして並べるにとどめる。

CLAUDE.md に何を残すかは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> にある。

この教材のリポジトリ自身も、この型を使っている。生成物を手で書き換えさせない規則は、強制を権限ルールの deny ルール（生成物のパスへの Edit）に任せ、同じ範囲に当たるフックを 1 つ置いて、「生成物は `gen_site.py` で作り直す」と代わりを返す。強制は依存のない deny が担い、フックは理由を返す役を受け持つ、という分担である。

## テストの出力を絞る {#filter-test-output}

テストやログの出力で会話が埋まるのを防ぐには、PreToolUse でコマンドを書き換え、失敗の行と最後の要約だけを残す。JSON の `updatedInput` に、書き換えたコマンドを入れて返す。

手順は次のとおり。

1. 対象のコマンドを、テストの実行だけに絞る。確かめ：スクリプトの照合の式が、`pytest` で始まるコマンドだけに当たる
2. スクリプトを置いて登録する。確かめ：`/hooks` に出る
3. 失敗するテストを含めて実行させる。確かめ：会話に出る出力が、失敗の行とその後の数行、最後の要約に縮み、コマンドの終了コードは 0 にならない

<!-- gen:begin snippet hook-recipes/filter-test-output -->
<!-- textlint-disable -->

??? example "雛形：テストの出力を失敗の行だけに絞るフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/filter-test-output.py
    # PreToolUse（Bash）で、pytest の実行コマンドを、失敗の行と最後の要約だけを残す形に書き換える。
    # 書き換えは JSON の updatedInput で返す。元のコマンドの終了コードは pipefail で保つ。
    import json
    import re
    import sys

    # 当てる範囲を狭くする：pytest（uv run pytest を含む）で始まるコマンドだけ
    TEST = re.compile(r"^\s*(?:uv run\s+)?pytest\b")

    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")

    if not TEST.match(command):
        sys.exit(0)

    filtered = (
        "set -o pipefail; "
        f"({command}) 2>&1 "
        "| grep -E -A3 'FAILED|ERROR|Error|passed|failed' "
        "| tail -n 80"
    )

    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": {**data.get("tool_input", {}), "command": filtered},
        }
    }
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/filter-test-output -->

注意する点は次のとおり。

- 絞りすぎると、失敗の原因の行まで消える。`grep` の `-A3`（失敗の行の後の 3 行）と `tail` の行数は、自分のテストの出力を見て調整する
- 書き換えたコマンドの終了コードは、`set -o pipefail` で元のコマンドのものを保つ。これがないと、パイプの最後の `tail` の終了コード（0）になり、失敗が成功に見える
- このレシピは、書き換えと一緒に `allow` を返す。確認の画面を飛ばす判定を含むため、対象を `pytest` の実行に狭く絞る。deny と ask のルールは、フックの allow の後も評価される（<!-- link:begin block-with-exit-2#precedence -->[フックで止めて理由を返す（exit 2 と JSON） › 権限ルールとの順番](block-with-exit-2.md#precedence)<!-- link:end -->）
- 出力を絞るのは、会話に入る量を減らすための手段である。大量のログを調べる作業そのものは、別の文脈で動くサブエージェントに任せる手もある（<!-- link:begin writing-subagents#when-to-use -->[サブエージェントの作り方と使いどころ › 使いどころと、使わない場面](../extend/writing-subagents.md#when-to-use)<!-- link:end -->）

## 終わったら知らせる {#notify}

作業の終わりや、確認待ちを知らせるには、Notification と Stop のイベントにフックを置く。登録の例は、「フックを登録する」の節の設定に含めてある。

- **Notification**：Claude が許可を求めたとき（`permission_prompt`）や、入力を待っているとき（`idle_prompt`）に走る。`matcher` で通知の種類を絞る
- **Stop**：Claude が 1 回の応答を終えるたびに走る。長く任せた作業の終わりを知るのに向く

雛形の通知のコマンドは `notify-send` で、Linux のデスクトップを前提にする。WSL・macOS・Windows の通知の出し方は、未確認である。端末ごとの手段は <!-- link:begin completion-notifications#channels -->終わったら知らせてもらう › 知らせる手段（端末の設定とフック）（準備中）<!-- link:end --> にある。

手順の確かめは、短い作業を頼んで、終わったときに通知が出ることを見る。

知らせを増やしすぎると、作業が細切れになる。Stop のたびに通知を出すか、時刻を決めて自分で見に行くかは、<!-- link:begin completion-notifications#when-to-notify -->終わったら知らせてもらう › 知らせるか、時刻を決めて見るか（準備中）<!-- link:end --> で選ぶ。Stop のフックには、別の使い方もあり、確かめる処理が通るまでターンを終えさせない型は <!-- link:begin stop-hooks -->Stop フックで「終わらせない」（準備中）<!-- link:end --> が持つ。

## 担当にだけ禁じる（agent_id） {#subagent-only}

サブエージェントにだけ `git commit` を禁じ、メインの会話では許したいときは、PreToolUse のフックで、入力の `agent_id` の有無を見て分ける。

メインとサブエージェントを見分けるほかの手段は、どれも合わない。

| 手段 | メインも止まるか | 問題 |
| --- | --- | --- |
| 権限ルールの deny ルール | 止まる | メインの commit も止める |
| サブエージェントの定義の `disallowedTools` | 止まらない | `Bash(git commit *)` のように指定子を付けても、Bash のツール全体が外れる |
| フックで `agent_type` を見る | 止まる場合がある | `--agent` で起動したメインにも付く |
| フックで `agent_id` を見る | 止まらない | 照合は文字列なので、書き方を変えた操作は拾えない |

`agent_id` は、サブエージェント（または in-process の teammate）の中で発火したときにだけ入力に付く。メインの会話には付かない。

手順は次のとおり。

1. スクリプトを置いて登録する。確かめ：`/hooks` の PreToolUse に、`if` を `Bash(git *)` とした項目が出る
2. 壊れても困らない場所で、サブエージェントに `git commit` を頼む。確かめ：止められ、「commit はメインが行う」旨の理由がサブエージェントに見える
3. メインの会話で同じ `git commit` を頼む。確かめ：止められない

<!-- gen:begin snippet hook-recipes/deny-subagent-commit -->
<!-- textlint-disable -->

??? example "雛形：サブエージェントにだけ git commit を禁じるフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/deny-subagent-commit.py
    # PreToolUse（Bash）で、サブエージェントの中から来た git commit・git push だけを止める。
    # 見分けは入力の agent_id の有無。agent_type は --agent で起動したメインにも付くので使わない。
    import json
    import re
    import sys

    # git のオプション（-C <パス>、-c <キー=値>、--long-option）を飛ばして commit・push を探す
    GIT_WRITE = re.compile(
        r"\bgit\s+(?:(?:-C|-c)\s+\S+\s+|--\S+\s+)*(?:commit|push)\b"
    )

    data = json.load(sys.stdin)

    # agent_id が無い＝メインの会話。何もせず通す
    if not data.get("agent_id"):
        sys.exit(0)

    command = data.get("tool_input", {}).get("command", "")

    if GIT_WRITE.search(command):
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    "担当（サブエージェント）は git commit と git push をしない。"
                    "commit はメインが行う。変更したファイルと内容を報告に書いて終える。"
                ),
            }
        }
        print(json.dumps(result, ensure_ascii=False))

    sys.exit(0)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-recipes/deny-subagent-commit -->

この型には、2 つの落とし穴がある。

- `agent_id` が入力に付かない環境（古い版や、サブエージェントの外）では、このフックは何も止めない。フックの失敗は既定で通す側に倒れる点と同じ向きの穴である。自分の環境で、実際にサブエージェントの commit が止まることを確かめる
- 照合は文字列なので、`git -C . commit` のような書き方はスクリプトで拾う必要がある。雛形は `-C`・`-c` と長いオプションを飛ばして照合するが、すべての書き方は覆えない

この教材のリポジトリも、同じ型を使っている。担当（サブエージェント）に、読むだけの git（status・diff・log・show）以外を使わせず、止めたときは「担当の git は読むだけ。commit はメインが行う。変更は報告に書いて終える」と返す。制作の印があるときだけ働く縛りで、読者がリポジトリを開いたときは動かない。ワークフローの担当でも効くかは、文書に書かれていないため、確かめた結果を見てから頼る。

サブエージェントに、規則がそもそも届かない仕組みは <!-- link:begin what-subagents-dont-inherit -->サブエージェントに引き継がれないもの（準備中）<!-- link:end --> にある。サブエージェントの定義の書き方は <!-- link:begin writing-subagents#define -->[サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）](../extend/writing-subagents.md#define)<!-- link:end --> を見る。

## 常設する前に確かめる {#verify}

フックは、置いただけでは効いたか分からない。全レシピで、常設する前に次の順で確かめる。

1. **登録を見る**。`/hooks` に、期待した matcher と一緒にフックが出る
2. **スクリプトだけを動かす**。実機の前に、入力の JSON を手で渡す。たとえば次のコマンドを実行し、止める JSON が stdout に出ることを見る。通す入力では、何も出ずに exit 0 で終わる

    ```bash
    echo '{"tool_input":{"command":"git push --force"}}' | python3 .claude/hooks/block-dangerous-bash.py
    ```

3. **実機で止まるか、変わるかを見る**。壊れても困らない使い捨てのリポジトリで、止めたい操作を実際に頼む
4. **止めすぎていないか見る**。ふつうの操作（`--force-with-lease`、`uv add`、`git status`）を頼み、止められないことを確かめる
5. **常設する**。プロジェクトの設定に入れてチームで共有するなら、利用者の権限で動くコードなので、中身を読んでからコミットする。置き場所は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](hooks-basics.md#locations)<!-- link:end -->
6. **止めた記録を見直す**。止めたのに回り込まれたり、意図しない操作が止まったりしていないかを、あとで見る。<!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end --> を見る

フックは、確かめる側（動作の確認）と縛る側（常設）の両方の性質を持つ。確かめを飛ばすと、効いていない鍵を、効いていると思い込む。

## 動かないとき・止めすぎるとき {#failures}

症状ごとの見る先は次のとおり。

| 見えたこと | 見る先 |
| --- | --- |
| フックが走っていないように見える | <!-- link:begin hooks-basics#not-running -->[フックの考え方とイベント › 動いていないように見えるとき](hooks-basics.md#not-running)<!-- link:end --> |
| スクリプトが落ちたのに、操作が通った | <!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end --> |
| 関係のない操作まで止まる | <!-- link:begin writing-safe-hooks#matcher -->[フックを安全に書く › matcher で止めすぎない](writing-safe-hooks.md#matcher)<!-- link:end -->、<!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end --> |
| 止めたのに、Claude が理由を分からず同じ操作を繰り返す | <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](block-with-exit-2.md#reason)<!-- link:end --> |
| 書き方を変えられて、止めた操作が通る | <!-- link:begin destructive-commands#guard -->[消されたくないもの（破壊的コマンド） › 確認を求めさせる頼み方と、鍵](../safety/destructive-commands.md#guard)<!-- link:end --> |
| 確かめる処理が通るまで、ターンを終えさせたくない | <!-- link:begin stop-hooks#avoid-loops -->Stop フックで「終わらせない」 › 止め続けるループを避ける（準備中）<!-- link:end --> |

評価ファイルなど、触らせたくないファイルを守る型は <!-- link:begin freeze-eval-assets -->評価資産を凍結し、触れる範囲を絞る（準備中）<!-- link:end --> が持つ。権限ルールだけでは子プロセスの書き込みを止められないので、サンドボックスと組む。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)
- [フックを安全に書く](writing-safe-hooks.md)

**関連**

- [フックの考え方とイベント](hooks-basics.md)
- Stop フックで「終わらせない」（準備中）
- [textlint をフックで回す](../japanese/textlint-hook.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)
- 評価資産を凍結し、触れる範囲を絞る（準備中）
- 縛りすぎの害と見直し（止めすぎ・回り込み）（準備中）
- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)
- サブエージェントに引き継がれないもの（準備中）
- 終わったら知らせてもらう（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
