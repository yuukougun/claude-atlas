---
id: destructive-commands
title: 消されたくないもの（破壊的コマンド）
aliases: [rm -rf, git reset --hard, force push, 破壊的な操作, 取り返しのつかない操作]
type: concept
field: safety
chapter: 秘密と壊す操作
order: 150
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [境界がない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 取り返しのつかない削除や書き換えが起きる経路と、巻き戻しで戻らないものが分かり、消されたくないものを権限ルール・サンドボックス・バックアップで守れる。
signs:
  - {type: goal, text: 本番のデータベースやリモートのブランチに触らせたくない}
  - {type: goal, text: 取り返しのつかない操作の前には、必ず止めてほしい}
prerequisites: [checkpoints-and-rewind, permission-rules]
related: [deleted-something-important, protected-paths, sandboxing, what-auto-mode-stops, block-with-exit-2, hook-recipes, working-with-git, where-bypass-is-ok]
tracks: [checkpoints, auto-mode, sandbox, permissions]
sources: [cc-docs-checkpointing, cc-docs-permission-modes, cc-docs-permissions, cc-docs-sandboxing, cc-docs-best-practices, api-docs-prompting-best-practices, anthropic-eng-code-auto-mode, cc-issue-10077, cc-issue-75859, simonwillison-quote-from-claude]
volatility: 中
sections:
  - {title: 消える経路, anchor: how-it-happens}
  - {title: 巻き戻しで戻らないもの, anchor: not-recoverable}
  - {title: 確認を求めさせる頼み方と、鍵, anchor: guard}
  - {title: どの原理・どの原因に効くか, anchor: principle}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：取り返しのつかない削除や書き換えが起きる経路と、`/rewind` で戻らないもの。守りは、頼み方（お願い）だけでなく、権限ルール・サンドボックス・バックアップ（鍵）で置く。
    - **いつ引くか**：本番のデータベースやリモートのブランチに触らせたくないとき。取り返しのつかない操作の前には、必ず止めてほしいとき。
    - **前提**：<!-- link:begin checkpoints-and-rewind -->[チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)<!-- link:end -->、<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：rm -rf・git reset --hard・force push・破壊的な操作・取り返しのつかない操作
<!-- textlint-enable -->

消されたくないものとは、Claude が動かした削除や上書きで失われ、実行した後に取り戻せないファイルや履歴やデータを指す。取り戻せるかどうかは、操作が届く範囲で決まる。手元のファイルは戻せることが多く、リモートのブランチや本番のデータは戻せないことが多い。このページは、どこで消えるか、何が戻らないか、どの鍵で止めるかを順に説明する。

## 消える経路 {#how-it-happens}

取り返しのつかない操作は、Claude が悪意で動かすからではなく、対象を取り違えたり、近道を取ったりして起きる。公開された報告と、Anthropic の社内の記録から、型は 3 つに分けられる。

**対象の取り違え**：消す範囲が、書いた人の意図より広くなる。

- 2025 年 12 月に引用された例がある。`rm -rf tests/ patches/ plan/ ~/` の末尾の `~/` が、ホームディレクトリのほぼ全体を指した（[A quote from Claude](https://simonwillison.net/2025/Dec/9/claude/)。二次の引用のため、根拠：弱）。
- Claude Code の issue #10077 は、`--dangerously-skip-permissions` を使っていないのに、`rm -rf` 系の操作でホーム配下のユーザーファイルが消えたと報告する。正確なコマンドはログに残っておらず、issue は「対応しない」として閉じられた（[Issue #10077](https://github.com/anthropics/claude-code/issues/10077)。単独の報告のため、根拠：弱）。
- issue #75859 は、ある Bash 呼び出しで `HOME` を一時ディレクトリに変え、別の呼び出しで `rm -rf "$HOME"` を実行した例を報告する。報告は、Bash の呼び出しの間でシェルの環境変数が引き継がれないため、本物のホームに展開されたと説明する（[Issue #75859](https://github.com/anthropics/claude-code/issues/75859)。単独の報告のため、根拠：弱）。
- Anthropic は、曖昧な「clean up」の指示からのブランチの一括削除や、名前が似ているだけのリソースの削除を、auto モードが止める対象の例に挙げる（[How we built Claude Code auto mode](https://www.anthropic.com/research/claude-code-auto-mode)）。

**近道**：行き詰まったときに、安全の確認を飛ばして先へ進む。公式の prompting ガイドは、障害に当たっても `--no-verify` などで安全確認を迂回したり、見慣れないファイルを捨てたりしないよう、指示で書くことを勧める（[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)）。

**手元の外へ出る操作**：リモートのブランチ、共有の環境、本番のデータに届く操作である。Anthropic の社内には、「過剰に積極的」な行動の記録がある。そこには、指示を誤解したリモートのブランチの削除と、本番のデータベースへの migration の試みが載る（[How we built Claude Code auto mode](https://www.anthropic.com/research/claude-code-auto-mode)。企業の一次の報告のため、根拠：中）。

どの型にも、指示がないと、Claude が元に戻しにくい行動を取ることがあるという共通点がある。公式の prompting ガイドは、指示がなければ、ファイルの削除・force push・外部サービスへの投稿などを取ることがあると書く。ガイドの記述は当時のモデルについてのもので、現行のモデルでの頻度は確かめていない。

## 巻き戻しで戻らないもの {#not-recoverable}

`/rewind` で戻せるのは、Claude のファイル編集の道具が変えたファイルだけである。チェックポイントは、送ったプロンプトごとに、その道具の編集を記録する仕組みで、git の代わりではない（[Checkpointing](https://code.claude.com/docs/en/checkpointing)）。次の表は、消えたものごとに、チェックポイントで戻るかどうかと、代わりの手段を示す。

| 消えたもの | チェックポイントで戻るか | 代わりの手段 |
| --- | --- | --- |
| Claude のファイル編集の道具が書き換えたファイル | 戻る | `/rewind` |
| Bash の `rm`・`mv`・`cp` で変わったファイル | 戻らない | git・バックアップ |
| ホームなど、作業ディレクトリの外のファイル | 戻らない | バックアップ |
| エディタや別のプロセスなど、外での変更 | 戻らない | git・バックアップ |
| ほとんどのサブエージェントの編集 | 戻らない | git |
| リモートのブランチ（force push・削除） | 範囲の外 | 手元のクローンに残る commit |
| 本番のデータベースのデータ | 範囲の外 | データベース側のバックアップ |

戻る範囲の詳しい説明は <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> が持つ。公式のベストプラクティスは、リスクのある試みをさせて、だめなら巻き戻す使い方を勧める一方、Bash で変わったファイルは復元されないと明記する（[Best practices](https://code.claude.com/docs/en/best-practices)）。つまり、チェックポイントは、Claude のファイル編集の誤りには効くが、この表の下の段の消え方には効かない。

消えた直後の復旧の手順は <!-- link:begin deleted-something-important#recover -->[消してはいけないものを消された › まず戻す（復旧の手順）](../symptoms/deleted-something-important.md#recover)<!-- link:end --> が持つ。git で戻せる範囲を広げる区切り方は <!-- link:begin working-with-git#granularity -->[git との付き合い方 › どこで区切るか](../cli/working-with-git.md#granularity)<!-- link:end --> を引く。

## 確認を求めさせる頼み方と、鍵 {#guard}

守りは 2 層に分ける。頼み方で変えられるのは、Claude が試みることである。許すかどうかは、設定とサンドボックスが決める。公式は、権限ルールをモデルではなく Claude Code が強制し、プロンプトや CLAUDE.md の指示は試みることを変えるが、許すことは変えないと書く（[Configure permissions](https://code.claude.com/docs/en/permissions)）。この辞典では、前者を「お願い」、後者を「鍵」と呼ぶ。

### お願い：戻せない操作の前に止まらせる

同じ依頼でも、足す情報で、Claude の動き方が変わる。

!!! example "Before / After：古いブランチの整理"
    - **Before**：「古いブランチを整理して」。
    - **After**：「対象は、マージ済みのローカルのブランチだけ。削除の前に、対象の一覧を出して。削除すると戻らなくなるものも添えて。私の返事を待って。リモートのブランチには触らないで。」
    - **足したもの**：対象の範囲、削除の前の一覧、返事を待つ約束、触らない場所の 4 つ。Before の「整理」は、どこまでを指すかが Claude の推測になる。

規則として常に効かせたいときは、CLAUDE.md に、理由と相談の基準を書く。禁止そのものは、次の鍵に任せる。

<!-- gen:begin snippet destructive-commands/reversibility-rule -->
<!-- textlint-disable -->

??? example "雛形：戻せない操作の前に確認を求める CLAUDE.md の規則"

    ```markdown
    ## 戻せない操作の扱い

    - 作業ディレクトリの中の編集、テストの実行、ローカルの commit は、確認なしで進めてよい。git で戻せるからである。
    - 次の操作は、実行の前に、何を・どこで・何が戻らなくなるかを書いて、私の返事を待つ。
      - ファイルやブランチの削除、`git reset --hard`、`git push --force`
      - リモートや共有の環境（本番のデータベース、他の人に見える場所）への書き込み
    - 行き詰まったときに、`--no-verify` で検査を飛ばしたり、見慣れないファイルを消して先へ進んだりしない。止まって、何が詰まったかを書く。
    - 理由：戻せない操作は、間違いに気づいた後で取り消せない。確認の一往復の費用は、その費用に比べて小さい。
    - 禁止そのものは、このファイルではなく、permissions の deny ルールとフックで強制している。ここに書くのは、迷う場面の判断の基準である。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet destructive-commands/reversibility-rule -->

お願いは万能ではない。会話で言った境界は、記録から読み直されるので、圧縮でその発言が消えると効かなくなりうる。例外を許さない操作は、設定にあるルールへ移す。

### 鍵：止める仕組みを会話の外に置く

鍵は、会話の外にある仕組みである。消されたくないものごとに、次の組を使う。

- **権限ルール**：Claude Code が強制する。強制力は <!-- gen:begin feature permissions/enforcement -->鍵<!-- gen:end feature permissions/enforcement --> である。拒否は先に評価される。ただし、パスのルールが当たらない場合や、子プロセスに効かない場合がある。評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->、効かない子プロセスは <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> が持つ。
- **フック**：PreToolUse のフックは、操作を止めて、理由と代わりの手段を Claude に返せる。書き方は <!-- link:begin block-with-exit-2#reason -->[フックで止めて理由を返す（exit 2 と JSON） › 理由と代わりの手段の書き方](../enforce/block-with-exit-2.md#reason)<!-- link:end -->、効かない場面は <!-- link:begin block-with-exit-2#limits -->[フックで止めて理由を返す（exit 2 と JSON） › 効かない場面と落とし穴](../enforce/block-with-exit-2.md#limits)<!-- link:end --> を引く。決まりきった危ない操作の遮断の型は <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end --> にある。
- **サンドボックス**：OS が強制する境界で、強制力は <!-- gen:begin feature sandbox/enforcement -->鍵<!-- gen:end feature sandbox/enforcement --> である。Bash のコマンドとそこから起きたプロセスの書き込みを、作業ディレクトリなどに閉じる。ホームを消す `rm` が届かなくなる。一方、Claude のファイルの道具・MCP サーバー・フックはサンドボックスの外で動く。囲える範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end -->、使い始めは <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](../enforce/sandboxing.md#minimal)<!-- link:end --> が持つ。
- **保護される場所**：ルートやホームなどへの `rm` は、どのモードでも止まる。止まるのは決まった場所の削除に限られ、force push や `git reset --hard` は含まれない。範囲は <!-- link:begin protected-paths#critical-rm -->[消せない場所・触れない場所（protected paths） › どのモードでも止まる削除](../enforce/protected-paths.md#critical-rm)<!-- link:end --> が持つ。
- **auto モード**：別の分類器が、実行前の操作を見て、範囲を超えるものを止める。ただし、公式は「確認を減らすが安全を保証しない」と書き、判断は決定論ではない。止める対象と見逃しは <!-- link:begin what-auto-mode-stops#defaults -->[auto モードは何を止め、何を止めないか › 既定で止めるもの・通すもの](../enforce/what-auto-mode-stops.md#defaults)<!-- link:end --> と <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> が持つ。

次の設定は、強制 push を拒み、`git reset --hard`・`git clean`・`rm -rf` の前に確認を出し、Bash のフックを登録する。

<!-- gen:begin snippet destructive-commands/guard-settings -->
<!-- textlint-disable -->

??? example "雛形：取り返しのつかない操作を拒む・確認させる設定（.claude/settings.json）"

    ```json
    {
      "permissions": {
        "deny": [
          "Bash(git push --force *)",
          "Bash(git push -f *)"
        ],
        "ask": [
          "Bash(git reset --hard *)",
          "Bash(git clean *)",
          "Bash(rm -rf *)"
        ]
      },
      "hooks": {
        "PreToolUse": [
          {
            "matcher": "Bash",
            "hooks": [
              {
                "type": "command",
                "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-destructive.py"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet destructive-commands/guard-settings -->

フックのスクリプトは、引数の順を変えた強制 push や、`"$HOME"` を指す削除を止める。issue #75859 の `rm -rf "$HOME"` は、コマンドの文字列に `$HOME` が書かれているので、このスクリプトで止まる。

<!-- gen:begin snippet destructive-commands/block-destructive -->
<!-- textlint-disable -->

??? example "雛形：強制 push・ホームの削除・DROP を exit 2 で止めるフック"

    ```python
    #!/usr/bin/env python3
    # .claude/hooks/block-destructive.py
    # PreToolUse（Bash）で、取り返しのつかない操作を止める。
    # exit 2 の返し方：stderr の文がそのまま Claude への理由になる。
    import json
    import re
    import shlex
    import sys

    # ホームやルートを丸ごと指す削除の対象
    DANGEROUS_TARGETS = {
        "~", "~/", "~/*", "/", "/*",
        "$HOME", "${HOME}", "$HOME/", "${HOME}/", "$HOME/*", "${HOME}/*",
    }
    SQL_DESTRUCTIVE = re.compile(r"\b(drop\s+(database|table|schema)|truncate\s+table)\b", re.I)


    def check(command: str) -> str | None:
        # && や ; や | で区切られた各コマンドを見る
        for segment in re.split(r"&&|\|\||[;&|\n]", command):
            try:
                tokens = shlex.split(segment)
            except ValueError:
                continue
            if not tokens:
                continue
            # git push の強制（--force、--force-with-lease、-f、+ref）
            if tokens[:2] == ["git", "push"]:
                rest = tokens[2:]
                if any(t.startswith("--force") or t == "-f" or t.startswith("+") for t in rest):
                    return (
                        "強制 push は止めている。リモートの履歴は書き換えない。"
                        "通常の push で足りない場合は、人に相談する。"
                    )
            # rm -r（-rf など）でホームやルートを指す削除
            if tokens[0] == "rm":
                flags = [t for t in tokens[1:] if t.startswith("-")]
                recursive = any(
                    t == "--recursive" or (not t.startswith("--") and ("r" in t or "R" in t))
                    for t in flags
                )
                if recursive and any(t in DANGEROUS_TARGETS for t in tokens[1:]):
                    return (
                        "ホームやルートを丸ごと消す rm は止めている。"
                        "消す対象は、作業ディレクトリの中の具体的なパスで指定する。"
                    )
        if SQL_DESTRUCTIVE.search(command):
            return (
                "DROP や TRUNCATE を含む SQL は止めている。"
                "データベースを壊す操作は、人が実行する。"
            )
        return None


    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")
    reason = check(command)
    if reason:
        print(reason, file=sys.stderr)
        sys.exit(2)
    sys.exit(0)
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet destructive-commands/block-destructive -->

このスクリプトは、コマンドの文字列を読むだけである。`find -delete` や、スクリプトの中の削除は見えない。文字列の照合で網羅はできないので、囲いの外へ出る書き込みはサンドボックスに任せる。

### 本番とリモートは、権限ごと握る

本番のデータベースやリモートのブランチは、ルールで止めるより前に、届かない状態にする。

- 本番の接続の資格情報を、Claude が動く環境に置かない。読み取り専用の資格情報だけを渡す。
- リモートのブランチは、サーバー側のブランチ保護で強制 push と削除を禁じる。設定の手順はホスティングの文書にある。
- commit と push を人が握るか任せるかは <!-- link:begin working-with-git#who-commits -->[git との付き合い方 › 誰がコミットするか](../cli/working-with-git.md#who-commits)<!-- link:end --> で決める。
- 確認をすべて外すモードや無人の実行は、隔離した使い捨ての環境だけで動かす。理由は <!-- link:begin where-bypass-is-ok#why-isolate -->[bypassPermissions と無人の実行はどこで動かすか › なぜ隔離した環境だけか](where-bypass-is-ok.md#why-isolate)<!-- link:end --> が持つ。確認を減らしたいだけなら、先に鍵を置く。

!!! example "判断例：夜間にブランチを整理させる"
    - **状況**：マージ済みの古いブランチが 40 本ある。夜間の整理を Claude へ任せて、朝に結果だけを見たい。
    - **迷う候補**：CLAUDE.md に「リモートのブランチは消さない」と書く。deny ルールとフックで、リモートの削除と強制 push を止める。
    - **選んだもの**：deny ルールとフックで止め、CLAUDE.md には、ローカルのブランチを消す前に一覧を出す基準と理由だけを書く。
    - **理由**：夜間は、止められる人がいない。お願いは圧縮で消えうるので、リモートの削除は鍵で止める。ローカルの削除は、手元のクローンから戻せる余地があるので、一覧を出す基準で足りる。

## どの原理・どの原因に効くか {#principle}

このページの守りは、原理「縛る」と「握る」に当たる。縛るは、Claude が届く範囲を設定で狭めることで、権限ルール・サンドボックス・フックがこれに当たる。握るは、取り返しのつかない判断を人の手に残すことで、commit と push の担当、本番の資格情報の管理、確認の一往復がこれに当たる。

防ぐ原因は 2 つある。

- **境界がない**：作業ディレクトリの外、リモート、本番のデータに、Claude の操作がそのまま届く状態である。サンドボックスと資格情報の管理が、境界を引く。
- **縛っていない**：境界はあるのに、お願いにしか書いていない状態である。CLAUDE.md の禁止の一文は、守られる保証がない。権限ルールとフックが、縛る。

## 誤解されやすいこと {#misconceptions}

- **「/rewind があるから消えても戻せる」**：戻せるのは、Claude のファイル編集の道具が変えたファイルだけである。Bash の削除と、リモートや本番の変更は戻らない。
- **「`--dangerously-skip-permissions` を使わなければ消えない」**：issue #10077 は、使っていないのに消えたと報告する。権限の確認は、対象の取り違えを防がない。
- **「CLAUDE.md に書けば止まる」**：書いた指示は試みを変えるだけで、許可を変えない。例外を許さない操作は、deny ルールかフックに置く。
- **「サンドボックスで全部守れる」**：作業ディレクトリの中のファイルは、サンドボックスの中でも消せる。中を守るのは、git とバックアップである。
- **「auto モードなら任せてよい」**：分類器は見逃すことがあり、高リスクな基盤の作業で人のレビューの代わりにならない。補う鍵は、権限ルールとサンドボックスである。

アプリで同じ守りがどう効くかは、確かめていない。このページの手順は、Claude Code（WSL・Linux の CLI）を基準にしている。ほかの OS と IDE 拡張の動作は未確認である。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Checkpointing](https://code.claude.com/docs/en/checkpointing)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/research/claude-code-auto-mode)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] ## CRITICAL: Claude Code executed rm -rf deleting entire home directory（Issue #10077）](https://github.com/anthropics/claude-code/issues/10077)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config（Issue #75859）](https://github.com/anthropics/claude-code/issues/75859)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [A quote from Claude](https://simonwillison.net/2025/Dec/9/claude/)：Simon Willison・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**次に読む**

- ノート・PKM（Obsidian など）（準備中）

**関連**

- [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- [消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [git との付き合い方](../cli/working-with-git.md)
- [bypassPermissions と無人の実行はどこで動かすか](where-bypass-is-ok.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
