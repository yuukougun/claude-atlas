---
id: stop-hooks
title: Stop フックで「終わらせない」
aliases: [Stop hook, SubagentStop, 終わらせないフック, stop_hook_active]
type: feature
field: enforce
chapter: フック
order: 130
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: Stop フックで、確かめる処理が通るまでターンを終えさせない仕組みを作れる。続けて止められる回数には上限があり、止め続けるループを避ける書き方が要る。
signs:
  - {type: goal, text: テストが通るまで終わらせたくない}
  - {type: symptom, text: Stop フックを入れたら、同じ確認を延々と繰り返す}
prerequisites: [block-with-exit-2, verification-ladder]
related: [goal-until-done, claims-done-but-isnt, stuck-in-a-check-loop, define-done, evidence-not-reports, hook-recipes, writing-safe-hooks, keep-replies-in-japanese#stop-hook, test-the-verifier, protect-tests]
tracks: [hooks, goal]
sources: [cc-docs-hooks, cc-docs-hooks-guide, cc-docs-goal]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 続けて止められる回数の上限, anchor: block-cap}
  - {title: 止め続けるループを避ける, anchor: avoid-loops}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: pitfalls}
  - {title: /goal との使い分け, anchor: vs-goal}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Stop フックで確かめる処理を走らせ、通るまで Claude にターンを終えさせず、続けさせられる。続けて止められる回数には上限があり、止め続けるループを避ける書き方が要る。
    - **いつ引くか**：テストが通るまで終わらせたくないとき。Stop フックを入れたら、同じ確認を延々と繰り返すとき。
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。終わってよいかをコマンドの結果で決めるので、Claude が「できた」と言っても、確かめが通らなければ終わらない。止められるのはターンの終わりだけで、確かめる処理が見ていないことは通る。
    - **前提**：<!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)<!-- link:end -->・<!-- link:begin verification-ladder -->[検証の階段](../verify/verification-ladder.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Stop hook・SubagentStop・終わらせないフック・stop_hook_active
<!-- textlint-enable -->

Stop フックは、Claude が応答を終えようとするときに走るフックである。確かめる処理が通っていなければ、終わりを止めて理由を返し、ターンを続けさせられる。このページは、その使い方と、止められる回数の上限、ループの避け方、`/goal` との使い分けを扱う。

## 使いどころ {#when}

Claude が確かめないまま「完了」と言って終える、という原因を防ぐときに使う。防ぐ原因は「確かめていない」である。「テストを通してから終わって」と依頼に書くのはお願いで、守られない回がある。Stop フックは、終わる直前にコマンドを走らせ、結果で終わってよいかを決めるので、毎回効く鍵になる。この位置づけは <!-- link:begin verification-ladder#four-steps -->[検証の階段 › 四つの段](../verify/verification-ladder.md#four-steps)<!-- link:end --> の 3 段目にあたる。

向くのは、通ったか通らないかをコマンドで決められる確かめである。

- テスト、型検査、lint、ビルド。終了コードか出力で判定できる
- 最後の返事そのものの確かめ。Stop フックの入力で最後の返事を受け取れる。例は <!-- link:begin keep-replies-in-japanese#stop-hook -->[日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)<!-- link:end --> にある

向かないのは、判定に読み取りや判断が要る確かめである。その場合は、モデルが判定する `/goal`（比べ方は「/goal との使い分け」の節）や、書いていない者に確かめさせる段を使う。終わった合図の通知だけなら、止めずに知らせるだけのフックで足りる（<!-- link:begin hook-recipes#notify -->[代表的なフックのレシピ › 終わったら知らせる](hook-recipes.md#notify)<!-- link:end -->）。

サブエージェントが終わるときには SubagentStop が走る。形は Stop と同じで、このページの内容は両方に当てはまる。

## 最小の使い方 {#minimal}

使い方は 3 手である。

1. 確かめるスクリプトを `.claude/hooks/` に置く。標準入力で JSON を受け取る。ここに `stop_hook_active`（Stop フックの差し戻しで続いている最中かどうか）と、最後の返事を指す `last_assistant_message` がある
2. 設定ファイルの `hooks.Stop` に登録する。Stop には matcher を付けない
3. 通らないとき、終わりを止めて理由を返す。返し方は 2 通りで、exit 2 にして標準エラーに理由を書くか、exit 0 で `{"decision": "block", "reason": "…"}` を標準出力に出す

通るときは、何も出さずに exit 0 で終わる。2 通りの違いと、理由の書き方は <!-- link:begin block-with-exit-2#exit-2-vs-json -->[フックで止めて理由を返す（exit 2 と JSON） › exit 2 と JSON の違い](block-with-exit-2.md#exit-2-vs-json)<!-- link:end --> と <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](block-with-exit-2.md#reason)<!-- link:end --> が正本である。Stop でも返し方は同じ形だが、止める対象が道具の呼び出しではなくターンの終わりになる。

完成した例は後の「雛形」の節にある。本文は WSL・Linux の CLI を基準にしている。ほかの OS と IDE 拡張での動作は未確認である。

## 続けて止められる回数の上限 {#block-cap}

Stop フックと SubagentStop フックには、続けて止められる回数の上限がある。Claude のツールの呼び出しを挟まずに、続けてターンの終了を止めると、上限を超えた差し戻しは上書きされ、警告付きでターンが終わる。<!-- fact:begin stop-hook-block-cap -->続けて止められるのは 8 回まで（2026-11-04 時点）<!-- fact:end -->。

仕組みの要点は次のとおりである。

- 数えは、Claude がツールを呼ぶたびに戻る。「続けて」とは、ツールの呼び出しを挟まずに、という意味である
- 上限は環境変数 `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` で変えられる
- 理由を `additionalContext` で渡して続けさせる場合も、同じ上限が効く
- 上限に当たると、確かめが通っていなくてもターンは終わる

ここから 2 つの注意が出る。

1 つ目は、上限は「通った」の保証ではないことである。警告付きで終わった場合、確かめは通っていない。席を外している間にこうなると、終わった画面だけを見て完了と思い込みかねない。終わった後は、通ったという証拠を自分で見る（<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](../verify/evidence-not-reports.md)<!-- link:end -->）。

2 つ目は、上限をループの歯止めとして当てにしないことである。差し戻された Claude が毎回ツールを呼んで直そうとすると、数えが戻るので、上限に届かないまま長く続くことがある。上限を上げても、通らない原因は直らず、ループが長くなるだけである。止める仕組みは、フックの中に自分で持つ（書き方は「止め続けるループを避ける」の節）。

## 止め続けるループを避ける {#avoid-loops}

Stop フックがループになるのは、差し戻しても確かめが通らないときである。落ちる原因が Claude の手の届かない所にあると、同じ失敗の出力を何度返しても進まない。外部サービスが落ちている、テストが不安定である、環境の権限が足りない、などである。症状の側から引くときは <!-- link:begin stuck-in-a-check-loop -->[同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)<!-- link:end --> を使う。ここでは、フックの書き方で避ける方法を挙げる。

1. **`stop_hook_active` を見る**。真なら、すでに Stop フックの差し戻しで続いている最中である。最も簡単な書き方は、真のときは確かめずに exit 0 で終えることで、差し戻しを 1 回に絞れる
2. **自分の上限を持つ**。差し戻しを 1 回で足りない場面では、回数を自分で数える。組み込みの上限より小さい値を決め、超えたら「通っていない」と画面に残して終える。この節の下の判断例と、「雛形」の節のスクリプトがこの形である
3. **理由を毎回具体的にする**。失敗の出力の要点と、次に何をするかを理由に載せる。同じ理由を返すと、同じ試みを繰り返しやすい
4. **確かめを走らせられないときの扱いを決める**。コマンドが無い、タイムアウトした、のときに差し戻しても直せない。止めずに通すか、止めるかを、スクリプトの中で決める
5. **確かめそのものを疑う**。落ちる理由が不安定なテストなら、直すのは確かめのほうである。確かめの確かめ方は <!-- link:begin test-the-verifier -->[検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)<!-- link:end --> にある

!!! example "判断例：外部サービスに頼るテストで差し戻しを何回にするか"
    - **状況**：統合テストが外部のサービスに接続する。サービスが落ちている日は、コードを直しても通らない。
    - **迷う候補**：`stop_hook_active` が真なら通して、差し戻しを 1 回に絞る。または、自分で回数を数え、3 回まで差し戻す。
    - **選んだもの**：自分で数えて 3 回で打ち切り、通っていない旨を画面に残す。
    - **理由**：本物の失敗は 1 回の直しで終わらないことがあり、1 回では足りない。回数に上限がなければ、サービスが落ちている日には延々と続く。組み込みの上限は、ツールを挟むと数えが戻るので、頼りにならない。

## 雛形 {#templates}

テストが通るまで終えさせない Stop フックの例である。テストを走らせ、落ちたら失敗の出力の末尾を理由に載せて差し戻す。差し戻しは 3 回で打ち切り、打ち切ったことを画面に残す。テストを走らせられないときは止めずに通す。

<!-- gen:begin snippet stop-hooks/stop-until-tests-pass -->
<!-- textlint-disable -->

??? example "雛形：テストが通るまで終えさせない Stop フック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/stop-until-tests-pass.py
    # Stop で、テストが通るまでターンを終えさせない。
    # 差し戻しは MAX_BLOCKS 回までにする。それでも通らなければ、通っていないことを画面に残して終わらせる。
    # 組み込みの上限（ツールの呼び出しを挟まずに続けて止められる回数）とは別に、自分の上限を持つためである。
    import json
    import subprocess
    import sys
    import tempfile
    from pathlib import Path

    TEST_CMD = ["pytest", "-q", "-x"]  # 確かめるコマンド。自分のプロジェクトのものに替える
    TIMEOUT = 300  # 秒。テストがこれより長くかかるなら、確かめる範囲を絞る
    MAX_BLOCKS = 3  # 差し戻す回数の上限
    TAIL_LINES = 40  # 理由に載せる出力の行数

    data = json.load(sys.stdin)
    counter = Path(tempfile.gettempdir()) / f"stop-hook-{data.get('session_id', 'unknown')}.count"

    # stop_hook_active が偽なら、Stop フックの差し戻しで続いているのではない新しい終わりである。数え直す。
    if not data.get("stop_hook_active"):
        counter.unlink(missing_ok=True)

    try:
        done = subprocess.run(
            TEST_CMD,
            cwd=data.get("cwd"),
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        # 確かめを走らせられないときは、止めずに通す。差し戻しても直せないので、ループになるだけである。
        print(f"テストを走らせられなかったので、確かめずに終わらせる: {error}", file=sys.stderr)
        sys.exit(0)

    if done.returncode == 0:
        counter.unlink(missing_ok=True)
        sys.exit(0)

    blocks = int(counter.read_text()) if counter.exists() else 0
    if blocks >= MAX_BLOCKS:
        counter.unlink(missing_ok=True)
        notice = f"テストが通らないまま、差し戻しを {MAX_BLOCKS} 回で打ち切った。確かめが通っていない。"
        print(json.dumps({"systemMessage": notice}, ensure_ascii=False))
        sys.exit(0)

    counter.write_text(str(blocks + 1))
    output = (done.stdout + done.stderr).splitlines()[-TAIL_LINES:]
    reason = (
        "テストがまだ通らないので、終わらせない。"
        "次の出力の失敗を直してから、もう一度テストを走らせて結果を示すこと。\n" + "\n".join(output)
    )
    print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
    sys.exit(0)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet stop-hooks/stop-until-tests-pass -->

登録する設定は次のとおりである。Stop には matcher を付けない。

<!-- gen:begin snippet stop-hooks/register-stop-hook -->
<!-- textlint-disable -->

??? example "雛形：Stop フックを登録する設定"

    ```json
    {
      "hooks": {
        "Stop": [
          {
            "hooks": [
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop-until-tests-pass.py",
                "timeout": 400
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet stop-hooks/register-stop-hook -->

置いたあとは、使い捨てのリポジトリで、わざと落ちるテストを 1 つ置いて確かめる。差し戻しが起きること、打ち切りで終わること、通ると差し戻されないことの 3 つを見る。常設するのはその後である。

## 効かない場面と落とし穴 {#pitfalls}

- **確かめが正しいとは限らない**。Stop フックが見るのは「通ったか」だけで、確かめ自体が正しいかは見ない。Claude がテストを書き換えて通すことがある。テストの守り方は <!-- link:begin protect-tests -->[テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)<!-- link:end --> にある
- **失敗は止めに倒れない**。起動できない、exit 0 と 2 以外で終わる、タイムアウトする、のとき、フックの既定は止めずに通す。`onFailure` の指定は Stop と SubagentStop には効かない。止めに倒したいなら、失敗の扱いをスクリプトの中で書く。既定の考え方は <!-- link:begin writing-safe-hooks#fail-open -->[フックを安全に書く › 既定は失敗すると通す（fail-open）](writing-safe-hooks.md#fail-open)<!-- link:end --> にある
- **ターンごとに走る**。質問に答えるだけで、コードを変えていないターンでも走る。確かめが重いと待たされる。変更の有無を見て、走らせるかを決める書き方もある
- **prompt 型・agent 型のフックは鍵にならない**。別のモデルが判断するので、毎回同じ結果になる保証がない。決まった結果が要るなら command か http のフックを使う
- **面は Claude Code だけ**。アプリと API には、この仕組みはない

## /goal との使い分け {#vs-goal}

`/goal` も、条件を満たすまで Claude にターンを続けさせる。違いは、終わってよいかを誰が判定するかである。Stop フックは、スクリプトがコマンドを走らせて決める。`/goal` は、モデルが各ターンの後に判定する。

<!-- gen:begin compare 強制力 成熟度 -->
<!-- textlint-disable -->

| 機能 | 強制力 |
| --- | --- |
| [フック（hooks）](hooks-basics.md) | 鍵 |
| [/goal](../delegate/goal-until-done.md) | モデルの判定 |

すべて共通：成熟度 GA。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 成熟度 -->

`/goal` の強制力は <!-- gen:begin feature goal/enforcement -->モデルの判定<!-- gen:end feature goal/enforcement --> である。判定役は会話に出た証拠しか読まない（<!-- link:begin goal-until-done#evaluator-reads-conversation -->[/goal（完了するまで続けさせる） › 判定役は会話しか読まない](../delegate/goal-until-done.md#evaluator-reads-conversation)<!-- link:end -->）。コマンドの結果やファイルの中身は、Claude が会話に出さない限り見えない。

選び方は次のとおりである。

- 通ったかをコマンドの結果で決められる：Stop フック。毎回同じ判定になる
- 条件を文章で書くほうが速い、または席を外している間に進めたい：`/goal`。条件の書き方は <!-- link:begin goal-until-done#writing-conditions -->[/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](../delegate/goal-until-done.md#writing-conditions)<!-- link:end --> にある
- 判定が会話の証拠だけで決まる：`/goal` で足りる。コマンドの出力を会話に出させる条件を足す

Stop フックと `/goal` を同時に置いたときの挙動は、このページでは確かめていない。まず片方で試す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [フックで止めて理由を返す（exit 2 と JSON）](block-with-exit-2.md)
- [検証の階段](../verify/verification-ladder.md)

**関連**

- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [代表的なフックのレシピ](hook-recipes.md)
- [フックを安全に書く](writing-safe-hooks.md)
- [日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
