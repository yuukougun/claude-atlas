---
id: block-with-exit-2
title: フックで止めて理由を返す（exit 2 と JSON）
nav_title: フックで止めて理由を返す
aliases: [exit 2 でブロックする, permissionDecision, PreToolUse でブロックする, フックで拒否する]
type: feature
field: enforce
chapter: フック
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: PreToolUse のフックで操作を止め、理由と代わりの手段を Claude に返せる。exit 2 と JSON の返し方の違いと、止めた後に回り込ませない書き方が分かる。
signs:
  - {type: goal, text: 特定のコマンドを、理由を伝えて止めたい}
  - {type: goal, text: .env や migrations を絶対に触らせたくない}
  - {type: symptom, text: フックで止めても、Claude が理由を分からずに同じ操作を繰り返す}
prerequisites: [hooks-basics]
related: [writing-safe-hooks, hook-recipes, lock-side-effects, permission-rules, stop-hooks, protecting-secrets, destructive-commands]
tracks: [hooks]
sources: [cc-docs-hooks, cc-docs-hooks-guide, cc-docs-permissions, cc-docs-features-overview]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: exit 2 と JSON の違い, anchor: exit-2-vs-json}
  - {title: 理由と代わりの手段の書き方, anchor: reason}
  - {title: 権限ルールとの順番, anchor: precedence}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：PreToolUse のフックで、道具の実行の前に操作を止め、理由と代わりの手段を Claude に返せる。返し方は exit 2 と、exit 0 に付ける JSON の 2 つで、理由と代わりを分けて返せるのは JSON のほう
    - **いつ引くか**：特定のコマンドを理由つきで止めたいとき。`.env` や migrations を絶対に触らせたくないとき。フックで止めたのに Claude が理由を分からず、同じ操作を繰り返すとき
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。一致した操作は、Claude の判断に関係なく止まる。止められるのはフックが見ている道具の呼び出しだけで、見ていない経路には効かない
    - **前提**：<!-- link:begin hooks-basics -->[フックの考え方とイベント](hooks-basics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：exit 2 でブロックする・permissionDecision・PreToolUse でブロックする・フックで拒否する
<!-- textlint-enable -->

PreToolUse のフックは、Claude が道具を実行する直前に走り、その操作を通すか止めるかを決められる。止めるだけでなく、止めた理由と代わりの手段を Claude に返せる。このページは、その返し方の 2 通りと、止めた後に Claude が回り込まない書き方を扱う。

## 使いどころ {#when}

「お願い」で縛れない規則を、仕組みで止めるときに使う。公式は、CLAUDE.md やスキルに書く指示は依頼であって保証ではなく、例外なく守らせる規則は PreToolUse のフックで止めるのが強制だとする。

このページが防ぐのは、原因の「縛っていない」である。典型は次の 2 つ。

- 特定のコマンドを止めたい。止めるだけなら権限ルールでもできるが、理由と代わりの手段を返したいならフックが向く
- `.env` や migrations を絶対に触らせたくない。deny ルールで足りるなら、まず <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](permission-rules.md)<!-- link:end --> で書く。足りないとき、たとえば migrations は既存のファイルを直させず新しいファイルで足させたいときに、理由と代わりを返して止める側がこのページである

フックのイベントの全体と置き場所は <!-- link:begin hooks-basics#events -->[フックの考え方とイベント › 代表的なイベント](hooks-basics.md#events)<!-- link:end --> にある。ここでは PreToolUse に絞る。

## exit 2 と JSON の違い {#exit-2-vs-json}

PreToolUse のフックが操作を止める方法は、終了コードの exit 2 と、exit 0 で出す JSON の 2 つである。

| 返し方 | 止める書き方 | 理由の届き方 | 向く場面 |
| --- | --- | --- | --- |
| exit 2 | 終了コードを 2 にする | stderr の文がそのまま理由になる | 短い 1 文で足りるとき |
| JSON | exit 0 で、stdout に判定を出す | `permissionDecisionReason` の文が理由になる | 理由と代わりを分けて返したいとき |

**exit 2** では、stderr が理由として Claude に渡る。Claude には、PreToolUse のフックのエラーとして、コマンドと stderr の文が並ぶ形で届く。終了コードが 0 なら成功で、JSON があれば解釈される。0 と 2 以外の終了コードは、止めない種類のエラーとして扱われ、操作は通る。

**JSON** では、exit 0 で終え、`hookSpecificOutput` に `permissionDecision` と `permissionDecisionReason` を入れて stdout に出す。

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "…"
  }
}
```

- `permissionDecision` は allow・deny・ask・defer のどれか。止めるときは deny にする
- deny の理由は Claude に見える。`additionalContext` を足すと、状況の補足を Claude の文脈に入れられる
- PreToolUse の最上位にある `decision` と `reason` は非推奨である。`hookSpecificOutput` の中に書く
- `systemMessage` は利用者に見せる文で、Claude に向けた文ではない。`systemMessage` に書いた理由は、Claude には届かない

2 つを混ぜると、exit 2 の止めが勝つ。exit 2 で終えるスクリプトに JSON も出しても、JSON の文は使われず、stderr が理由になる。どちらか一方に決めて書く。

複数のフックが同じ操作に別々の判定を返したときは、deny が最も強く、defer、ask、allow の順に弱くなる。

!!! example "判断例：exit 2 と JSON のどちらで返すか"
    - **状況**：migrations の既存ファイルの変更を止め、追加へ向けたい。
    - **迷う候補**：exit 2 で stderr に理由を書く／JSON の deny で理由の欄に書く。
    - **選んだもの**：JSON の deny。
    - **理由**：どちらでも理由は届く。JSON は判定と理由が別の欄で、`additionalContext` で状況も足せる。理由と代わりを組み立てて返すなら JSON が扱いやすい。1 行の理由で足りる小さな規則なら、exit 2 でもスクリプトは短く済む。

## 理由と代わりの手段の書き方 {#reason}

止めるときは、理由と代わりの手段の両方を返す。「禁止」の一言だけだと、Claude は代わりの手段が分からない。すると同じ操作を言い換えて繰り返すか、別の道具で同じことをしようとする。逆引きの「フックで止めても、Claude が理由を分からずに同じ操作を繰り返す」は、この書き方の不足で起きる。

返す文に入れるものは 3 つである。

1. 何が止められたか（対象の操作やファイル）
2. なぜ止めるか（このリポジトリの規則）
3. 代わりに何をすればよいか（具体的な手段）

文の形は、命令ではなく事実の形にする。公式の文書は `additionalContext` について、命令ではなく事実の形で書くよう勧め、システムの命令のような書き方は prompt injection の防御が働き、文脈として扱われずに利用者へ示されることがあると注意している。`permissionDecisionReason` にも同じ注意を当てるのは、この教材の推論である（推論・実践例なし）。実際に届くかは、自分の環境で止めてみて確かめる。

=== "Claude Code"

    | | 書き方 |
    | --- | --- |
    | 弱い例 | 「migrations は編集禁止。」 |
    | 強い例 | 「このリポジトリでは、適用済みの migration は書き換えない。変更は新しい番号の migration ファイルを追加して行う。」 |

    強い例は、規則を事実として述べ、代わりの手段（新しいファイルで足す）まで書いている。弱い例は、何を代わりにするかが無く、回り込みを招く。

止めた理由の書き方の一般論と、止めた記録の見直しは <!-- link:begin lock-side-effects#reason-and-alternative -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めるときに返すこと（準備中）<!-- link:end --> と <!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end --> にある。縛る規則を何にするかの選び方は <!-- link:begin lock-side-effects#what-to-lock -->縛りすぎの害と見直し（止めすぎ・回り込み） › 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）（準備中）<!-- link:end --> を見る。

## 権限ルールとの順番 {#precedence}

フックと権限ルールは両方とも効く。評価の順番は、権限ルールが deny、ask、allow の順で、最初に当たったものが勝つ（<!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](permission-rules.md#evaluation-order)<!-- link:end -->）。フックはこれに次のように絡む。

- exit 2 で止めるフックは、allow ルールより先に効く。allow に書いてある操作でも止まる
- フックが allow を返しても、deny と ask のルールは評価される。フックの allow で deny ルールを外すことはできない。安全側に倒れる設計である
- 権限ルールを書く場所（ユーザー・プロジェクトなど）が違っても、どこかに deny があれば、ほかの場所の allow に勝つ

使い分けの目安は次のとおり。

| 守りたいこと | 先に使うもの | フックを足す場面 |
| --- | --- | --- |
| パスやコマンドを単に禁じたい | 権限ルールの deny | 理由と代わりを返したいとき |
| 条件付きで止めたい（既存ファイルだけ、など） | フック | ― |
| 秘密を読ませたくない | 権限ルールとサンドボックスの二重 | 補助として。<!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> を見る |

`.env` のように「絶対に」触らせたくないものは、フックだけに頼らない。フックは Claude の道具の呼び出しを見て判定するので、書き方の違いで抜ける経路がありうる。権限ルールの落とし穴は <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](permission-rules.md#path-rules)<!-- link:end --> と <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](permission-rules.md#child-processes)<!-- link:end --> にある。

## 雛形 {#templates}

migrations の既存ファイルの書き換えを止め、新しいファイルで足すよう返す例を、exit 2 と JSON の 2 通りで載せる。どちらも、既にあるファイルだけを止め、新しいファイルの作成は通す。

exit 2 の版。

<!-- gen:begin snippet block-with-exit-2/block-migrations-exit2 -->
<!-- textlint-disable -->

??? example "雛形：migrations の既存ファイルを exit 2 で止めるフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/block-migrations-exit2.py
    # PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
    # exit 2 の返し方：stderr の文がそのまま Claude への理由になる。
    import json
    import os
    import sys

    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")
    in_migrations = "/migrations/" in path.replace("\\", "/")

    if in_migrations and os.path.exists(path):
        print(
            "このリポジトリでは、適用済みの migration は書き換えない。"
            "変更は新しい番号の migration ファイルを追加して行う。"
            f"（対象：{path}）",
            file=sys.stderr,
        )
        sys.exit(2)

    sys.exit(0)
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet block-with-exit-2/block-migrations-exit2 -->

JSON の版。

<!-- gen:begin snippet block-with-exit-2/block-migrations-json -->
<!-- textlint-disable -->

??? example "雛形：migrations の既存ファイルを JSON の deny で止めるフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/block-migrations-json.py
    # PreToolUse（Edit・Write）で、migrations の既存ファイルの書き換えを止める。
    # JSON の返し方：exit 0 で終え、stdout に判定と理由を JSON で出す。
    import json
    import os
    import sys

    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")
    in_migrations = "/migrations/" in path.replace("\\", "/")

    if in_migrations and os.path.exists(path):
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    "このリポジトリでは、適用済みの migration は書き換えない。"
                    "変更は新しい番号の migration ファイルを追加して行う。"
                ),
            }
        }
        print(json.dumps(result, ensure_ascii=False))

    sys.exit(0)
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet block-with-exit-2/block-migrations-json -->

フックの登録は、プロジェクトの `.claude/settings.json` に次のように書く（スクリプトは `.claude/hooks/` に置く）。exit 2 の版を使うなら、command のファイル名を `block-migrations-exit2.py` に替える。matcher を Edit と Write に絞り、ほかの道具を巻き込まない（<!-- link:begin writing-safe-hooks#matcher -->[フックを安全に書く › matcher で止めすぎない](writing-safe-hooks.md#matcher)<!-- link:end -->）。この例は雛形なので、守りとして常設するときは、失敗したときに止める設定など、<!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end --> の書き方に直す。

<!-- gen:begin snippet block-with-exit-2/register-hook -->
<!-- textlint-disable -->

??? example "雛形：PreToolUse のフックを登録する設定"

    ```json
    {
      "hooks": {
        "PreToolUse": [
          {
            "matcher": "Edit|Write",
            "hooks": [
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-migrations-json.py"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet block-with-exit-2/register-hook -->

コマンドの止め方（Bash の `rm` など）や、そのほかの代表的な例は <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](hook-recipes.md#block-dangerous)<!-- link:end --> にある。決めたコマンドへ誘導する書き方は <!-- link:begin hook-recipes#redirect-commands -->[代表的なフックのレシピ › 決めたコマンドへ誘導する（pip の代わりに uv など）](hook-recipes.md#redirect-commands)<!-- link:end --> を見る。

## 効かない場面と落とし穴 {#limits}

- **フックが失敗すると操作は通る**。スクリプトの異常終了や JSON の崩れなどの失敗は、止めない種類のエラーになりうる。止める用途では、失敗を止めに倒す書き方が要る（<!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end -->）
- **回り込まれる**。Edit を止めると、Claude が Bash の別のコマンドで同じファイルを変えようとすることがある。代わりの手段を返して、そちらへ向ける。同じ対象を別の道具からも触れるなら、matcher を広げるか権限ルールを重ねる
- **止めすぎる**。matcher が広いと、関係のない操作まで止める。止めた記録を見て絞り直す（<!-- link:begin lock-side-effects#review-blocks -->縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し（準備中）<!-- link:end -->）
- **フックは利用者の権限で動く**。スクリプトも、確かめてから置く（<!-- link:begin writing-safe-hooks#runs-as-you -->[フックを安全に書く › フックは利用者の権限で動く](writing-safe-hooks.md#runs-as-you)<!-- link:end -->）
- **止めるのは操作の前だけ**。終わろうとするターンを止めたいときは、別の仕組みを使う（<!-- link:begin stop-hooks -->Stop フックで「終わらせない」（準備中）<!-- link:end -->）
- **消えたものは戻らない**。消す操作を止められなかったときの備えは <!-- link:begin destructive-commands#not-recoverable -->[消されたくないもの（破壊的コマンド） › 巻き戻しで戻らないもの](../safety/destructive-commands.md#not-recoverable)<!-- link:end --> を見る

本文の動作は WSL・Linux の CLI を基準にしている。ほかの OS と IDE 拡張での動作は未確認である。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [フックの考え方とイベント](hooks-basics.md)

**次に読む**

- [代表的なフックのレシピ](hook-recipes.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)
- Stop フックで「終わらせない」（準備中）
- 縛りすぎの害と見直し（止めすぎ・回り込み）（準備中）

**関連**

- [フックを安全に書く](writing-safe-hooks.md)
- [権限ルール（allow・ask・deny）](permission-rules.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
