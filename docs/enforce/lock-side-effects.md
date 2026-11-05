---
id: lock-side-effects
title: 縛りすぎの害と見直し（止めすぎ・回り込み）
nav_title: 縛りすぎの害と見直し
aliases: [縛りの副作用, 止めすぎ, フックの回り込み, 縛りを外す判断]
type: concept
field: enforce
chapter: 縛りの運用
order: 150
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 握る]
prevents: []
pitfalls: []
scenes: [開発, チーム]
summary: 縛りを足しすぎたときに起きる止めすぎと回り込みを見分け、縛る規則を絞り直せる。止めるときは理由と代わりの手段を返し、止めた記録を見直す。
signs:
  - {type: symptom, text: フックで止めたら、別のコマンドで同じことをしようとする}
  - {type: symptom, text: 縛りを増やしたら、作業が進まなくなった}
  - {type: goal, text: 入れた縛りが役に立っているか見直したい}
prerequisites: [block-with-exit-2]
related: [when-to-lock#what-not-to-lock, writing-safe-hooks, permission-rules, hook-recipes, what-auto-mode-stops, stuck-in-a-check-loop, keeps-stopping, blames-the-tools, postmortems, paved-roads]
tracks: [hooks, permissions]
sources: [cc-docs-hooks-guide, cc-docs-permissions]
volatility: 中
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜそうなるか, anchor: why}
  - {title: 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）, anchor: what-to-lock}
  - {title: 止めるときに返すこと, anchor: reason-and-alternative}
  - {title: 止めた記録の見直し, anchor: review-blocks}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：縛りを足しすぎたときの止めすぎと回り込みを見分け、縛る規則を絞り直せる。
    - **いつ引くか**：フックで止めたら別のコマンドで同じことをされた、縛りを増やしたら作業が進まなくなった、入れた縛りが役に立っているか見直したいとき。
    - **前提**：<!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)<!-- link:end -->

<!-- textlint-disable -->
別名：縛りの副作用・止めすぎ・フックの回り込み・縛りを外す判断
<!-- textlint-enable -->

縛るとは、守らせたい規則をフックや権限ルール（鍵）に移して、Claude が破れないようにすることである。縛りすぎの害とは、規則を増やした結果、必要な操作まで止まる「止めすぎ」と、止められた Claude が別の経路で同じ目的を果たす「回り込み」が起きることである。縛りは足すほど安全になるものではなく、足すたびに副作用の見直しが要る。このページは、縛る規則の絞り方、止めるときに返す文、止めた記録の見直し方を扱う。

## 何が起きるか {#what-happens}

縛りの副作用は 2 つの形で現れる。どちらも、規則を足した直後ではなく、しばらく使ってから気づくことが多い。

| 形 | 起きること | 例 |
| --- | --- | --- |
| 止めすぎ | 本来は通したい操作まで止まる | matcher に `Edit.*` と書くと、`NotebookEdit` にも当たる。`^Edit$` で固定する |
| 回り込み | 止められた側が別の道具で同じ目的を果たす | `WebFetch` を拒んでも、Bash の `curl` は別の経路として残る |

回り込みの例は、公式の文書と制作の調査から整理したものである。`WebFetch` の拒否は `curl` などの Bash の取得には効かず、サンドボックスを入れたときに止まる。権限ルールは、Claude が起動した子プロセスの中の動きにも効かない（権限ルール側の説明は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](permission-rules.md#child-processes)<!-- link:end --> にある）。

回り込みが実際にどれだけ起きるかを示す研究は見当たらない。以下の整理は、仕組みと公式の記述からの推論と、制作の経験（根拠：弱）による。

## なぜそうなるか {#why}

止められても、頼まれた目的は残る。Claude は目的を果たす別の経路を探すので、禁止の理由と代わりを知らないと、別の経路が「別の操作」に見える。

公式の頼み方の指針は、障害に当たっても `--no-verify` のような安全確認を迂回する近道をしないよう求めている。auto モードの分類器も、認証エラーの後に設定ファイルを探して別のトークンを見つける行動を止める対象にしている。迂回は、公式の文書に挙がる、起きうる行動の型である。

規則の側にも原因がある。フックや権限ルールは、コマンドの文字列やパスで照合する。照合が狭ければ、同じ目的の別の書き方が一致せず通り抜ける。照合が広ければ、判断を要する操作まで巻き込んで止める。

たとえるなら、お願いと鍵の「鍵」は、かけた扉だけを閉じる。目的地は変わらないので、別の扉があれば人はそちらへ行く。扉を片端から閉めると、必要な行き来まで止まる。

## 縛る規則の選び方（機械的に判定でき、害の大きいものだけ） {#what-to-lock}

縛る規則は、次の 3 つがそろうものに絞る。

- 機械的に判定できる。文字列・パス・コマンドの形で、人が見なくても当たり外れが決まる。
- 破ったときの害が大きい。
- 戻せない、または他人に見える。

| 縛る | 縛らない（CLAUDE.md と指示に任せる） |
| --- | --- |
| AI の利用を断るサイトの取得 | 何が小さな直しかの判断 |
| 生成物の手書き | テストのどれが重要かの判断 |
| 強制上書きの push | 設計の良し悪し |

判断を含む規則を鍵にしない理由と、お願いを鍵に移す合図は、持ち主のページにある。<!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](when-to-lock.md#what-not-to-lock)<!-- link:end --> を先に読む。

縛ると決めた規則も、当てる範囲を狭くする。

- matcher は完全一致か `^…$` で書く。文字・数字・`_`・`-`・空白・`,`・`|` だけなら完全一致になり、ほかの文字を含むと前後を固定しない正規表現になる。詳しくは <!-- link:begin writing-safe-hooks#matcher -->[フックを安全に書く › matcher で止めすぎない](writing-safe-hooks.md#matcher)<!-- link:end --> を引く。
- `if` は、フックを呼ぶ回数を減らすために使う。Bash の判定は best-effort で、読み切れないときは規則にかかわらずフックが走るため、判定はスクリプトの中でも行う。
- 依存が欠けたとき、止めるか通すかを規則ごとに決める。既定は失敗すると通す（<!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end -->）。

強制は権限ルールの deny に任せ、フックは理由の文と記録だけを受け持たせる分け方もある。公式の文書は、確実な許可・拒否には、フックではなく権限ルールを使うよう勧める。deny ルールに理由の文を足す設定は文書に見当たらないので、理由を返したいときは、同じ範囲に当たる `PreToolUse` のフックを足す。

## 止めるときに返すこと {#reason-and-alternative}

止めるときは、理由と、代わりにどうするかを返す。止められた側が、回避策を探さずに次の行動を決められるようにするためである。

| | 返す文 |
| --- | --- |
| Before | 強制上書きは禁止。実行するな。 |
| After | このリポジトリでは、共有ブランチへの強制上書きの push は行わない。履歴を直したいときは、新しいブランチへ通常の push をして、プルリクエストで相談する。 |

After で足したのは、規則の範囲と、代わりの手段である。公式の文書は、フックが Claude に渡す文を、命令ではなく事実の形で書くよう勧める。システムの命令のような書き方は、prompt injection の防御を働かせるという注意もある。

代わりの手段が道具で用意できない規則もある。そのときは「変更は報告に書いて終える」のように、止められた後の終え方を代わりにする。

exit 2 より、exit 0 と JSON の `permissionDecisionReason` のほうが、理由と代わりを構造立てて返せる。返し方の違いと書き方は <!-- link:begin block-with-exit-2#exit-2-vs-json -->[フックで止めて理由を返す（exit 2 と JSON） › exit 2 と JSON の違い](block-with-exit-2.md#exit-2-vs-json)<!-- link:end --> と <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](block-with-exit-2.md#reason)<!-- link:end --> にある。ここでは、止めた記録を同じフックの中で取る雛形を示す。

<!-- gen:begin snippet lock-side-effects/block-and-log -->
<!-- textlint-disable -->

??? example "雛形：強制上書きの push だけを止め、理由と代わりを返して記録するフック"

    ```python
    #!/usr/bin/env python3
    """PreToolUse（matcher は Bash）：git push の強制上書きだけを止める。

    - 当てる範囲は狭くする：`git push` に `--force` か `-f` が付くときだけ。
      `--force-with-lease` は止めない。
    - 止めるときは、理由と代わりの手段を事実の形で返す。
    - 止めた記録を 1 行ずつ残す（見直しの材料）。記録は PreToolUse の中で取る。
    - 入力が読めないときは通す（この規則は、ほかの守りの代わりではない）。
    """
    import json
    import os
    import re
    import sys
    import time

    FORCE = re.compile(r"\bgit\s+push\b[^;&|]*?(?<![\w-])(--force|-f)(?![\w-])")

    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    command = (data.get("tool_input") or {}).get("command", "")
    if data.get("tool_name") != "Bash" or not FORCE.search(command):
        sys.exit(0)

    root = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    who = "担当" if data.get("agent_id") else "メイン"
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%S')}\tR1\t{who}\t{command[:200]!r}\n"
    try:
        with open(os.path.join(root, ".claude", "blocks.log"), "a", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass

    reason = (
        "このリポジトリでは、共有ブランチへの強制上書きの push は行わない。"
        "履歴を直したいときは、新しいブランチへ通常の push をして、"
        "プルリクエストで相談する。"
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=False))
    sys.exit(0)
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet lock-side-effects/block-and-log -->

この雛形が止めるのは、`git push` に `--force` か `-f` が付くときだけである。`--force-with-lease` と通常の push は通す。

回り込みを見つけたときは、塞ぐ規則を足す前に、理由と代わりが届いていたかを見る。塞ぐ規則は、同じ目的を同じ判定で言い表せる範囲に限る。経路ごとに規則を足すと、止めすぎに戻る。

## 止めた記録の見直し {#review-blocks}

止めた操作は、記録に 1 行ずつ残し、まとまった作業の終わりに見直す。記録は、`PermissionDenied` ではなく `PreToolUse` のフックで取る。前の節の雛形（`block-and-log`）は、日時・規則の番号・メインか担当か・コマンドの先頭を 1 行にして残す。コマンドには秘密が混ざりうる。記録には先頭の一部だけを残し、記録のファイルは共有や commit の対象から外す。

規則ごとに見るのは、次の 4 点である。

1. 止めた回数と、止められた直後に起きたこと。別の道具で同じ目的を試したなら、回り込みである。
2. 止めたのは、本当に避けたい操作だったか。通したい操作があれば、止めすぎである。
3. 理由と代わりの文が、次の行動に使えたか。
4. 残す・当てる範囲を狭める・外す、のどれにするか。

この見直しは、Claude に頼んでもよい。

<!-- gen:begin snippet lock-side-effects/review-blocks -->
<!-- textlint-disable -->

??? example "雛形：止めた記録を規則ごとに見直させる依頼"

    ```markdown
    .claude/blocks.log を読んで、止めた操作を規則ごとに見直してください。
    規則ごとに、次の 4 点を答えてください。

    1. 止めた回数と、止められた直後に起きたこと（別の道具で同じ目的を試した、報告に書いて終えた、作業が止まった）
    2. 止めたのは本当に避けたい操作だったか（止めすぎの例があれば、コマンドを引く）
    3. 理由と代わりの手段の文は、その場の次の行動に使えたか
    4. この規則を、そのまま残す・当てる範囲を狭める・外す、のどれにするか

    ログに無いことは推測で埋めず、「ログからは分からない」と書いてください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet lock-side-effects/review-blocks -->

記録が空でも、規則が効いているとは限らない。フックが動いていないだけかもしれないので、確かめ方は <!-- link:begin hook-recipes#verify -->[代表的なフックのレシピ › 常設する前に確かめる](hook-recipes.md#verify)<!-- link:end --> を引く。動かない・止めすぎるときの切り分けは <!-- link:begin hook-recipes#failures -->[代表的なフックのレシピ › 動かないとき・止めすぎるとき](hook-recipes.md#failures)<!-- link:end --> にある。

!!! example "判断例：生成物の書き換えを止めたら、別の経路で書き換えられた"
    - **状況**：生成物を手で書き換えない規則を `Edit` の deny で縛った。記録を見ると、止められた直後に、同じファイルを別の経路で書き換える操作が続けて並んでいる。
    - **迷う候補**：書き込みの経路ごとに規則を足して塞ぐ。または、理由と代わりを返し直し、規則の範囲は生成物のパスのままにする。
    - **選んだもの**：後者。理由に「生成物は生成のスクリプトで作り直す」という代わりの手段を足し、数日分の記録で回数を見る。
    - **理由**：代わりの手段がないと、目的が残って回り込みが続く。経路ごとに規則を足すと、止めすぎが増える。破ると戻せない害が出る規則なら、塞ぐ側に倒してよい。

見直しの結果、狭めても回り込みや止めすぎが減らない規則は、外してお願い（CLAUDE.md の理由と相談の基準）に戻す。外した規則と、その例は記録に残す。失敗から縛りを足すときの置き場所は <!-- link:begin postmortems#where-to-put-fixes -->[失敗を仕組みに戻す（ポストモーテム） › 再発防止をどこに入れるか](../judgment/postmortems.md#where-to-put-fixes)<!-- link:end --> にある。

## 何に効くか {#effects}

このページが扱う原理は、「縛る」と「握る」である。ここでの「縛る」は、規則を鍵（フックと権限ルール）に移すこと。「握る」は、何を任せ、何を人が決めるかを人が持つことである。縛りすぎは、鍵を増やすことで握る範囲が広がりすぎ、任せるはずの判断まで止める状態といえる。

このページは、特定の原因を防ぐ機能のページではなく、鍵を常設した後の運用で起きる副作用を扱う。症状とのつながりは次のとおり。

- 縛りを増やしてから、確認ばかりで進まない・途中で止まる：<!-- link:begin keeps-stopping -->[確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)<!-- link:end -->
- 実行と確認を繰り返すだけで進まない：<!-- link:begin stuck-in-a-check-loop -->[同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)<!-- link:end -->
- 止められた後に環境や道具が壊れたと言い出す：<!-- link:begin blames-the-tools -->[環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)<!-- link:end -->

禁じる代わりに、安全な既定と許す道を用意する考え方は <!-- link:begin paved-roads#defaults-over-attention -->[禁止ではなく安全な道を作る › 注意力に頼らない既定](../team/paved-roads.md#defaults-over-attention)<!-- link:end --> にある。auto モードが止めた操作の見直し方は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](what-auto-mode-stops.md#when-blocked)<!-- link:end --> にある。

## 誤解 {#misconceptions}

- 縛りを増やすほど安全になる、は誤り。照合が広いと止めすぎが増え、狭くても経路が残れば回り込まれる。
- 止められたら Claude は諦める、は誤り。目的が残る限り、別の経路を探すことがある。
- 理由を丁寧に書けば回り込まれない、は誤り。理由と代わりは、迂回する動機を減らすだけで、強制の代わりにはならない。強制が要る規則は、権限ルールやフックで別に縛る。
- 記録が空なら縛りは効いている、は誤り。フックが動いていない場合も空になる。

縛りを足す前の選別は <!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](when-to-lock.md#what-not-to-lock)<!-- link:end -->、フックを壊さない書き方は <!-- link:begin writing-safe-hooks -->[フックを安全に書く](writing-safe-hooks.md)<!-- link:end -->、権限ルールの評価の順番は <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](permission-rules.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)

**関連**

- [お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](when-to-lock.md#what-not-to-lock)
- [フックを安全に書く](writing-safe-hooks.md)
- [権限ルール（allow・ask・deny）](permission-rules.md)
- [代表的なフックのレシピ](hook-recipes.md)
- [auto モードは何を止め、何を止めないか](what-auto-mode-stops.md)
- [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)
- [禁止ではなく安全な道を作る](../team/paved-roads.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
