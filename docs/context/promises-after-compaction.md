---
id: promises-after-compaction
title: 圧縮で消えない場所に約束を置く
aliases: [圧縮のあとに残る約束、消える約束, 圧縮の後も守らせたい, 会話で言ったことが圧縮で消える]
type: concept
field: context
chapter: 圧縮
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 圧縮のあとも守らせたい決めごとを、圧縮の後に読み直される CLAUDE.md や計画のファイルに書き、例外を許さないものはdeny ルールやフックに移す。会話の中だけで伝えた約束は要約に溶けうる。
signs:
  - {type: goal, text: 圧縮のあとも守らせたい約束を、どこに書けばよいか知りたい}
  - {type: goal, text: 長いセッションで、最初に決めた約束を最後まで守らせたい}
prerequisites: [what-survives-compaction]
related: [compact-and-auto-compact, when-to-lock#spoken-rules-fade, permission-rules, path-scoped-rules, what-to-put-in-claude-md, how-skills-load, handoff-documents, forgot-after-compaction, request-vs-lock]
tracks: [compaction, claude-md, rules]
outdated_advice: []
sources: [cc-docs-context-window, cc-docs-memory, cc-docs-best-practices, cc-docs-costs, cc-docs-permission-modes]
volatility: 中
sections:
  - {title: 読み直される場所と、要約に溶ける約束, anchor: what-comes-back}
  - {title: 約束の種類ごとの置き場所, anchor: where-to-put}
  - {title: paths 付きの rules とスキルの本文の注意, anchor: caveats}
  - {title: 何に効くか（縛る・見せる）, anchor: effects}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：圧縮のあとも守らせたい約束を、種類ごとに、圧縮で消えない場所へ置き分ける判断が分かる。
    - **いつ引くか**：圧縮のあとも守らせたい約束を、どこに書けばよいか知りたいとき。長いセッションで、最初に決めた約束を最後まで守らせたいとき。
    - **前提**：<!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end -->

<!-- textlint-disable -->
別名：圧縮のあとに残る約束、消える約束・圧縮の後も守らせたい・会話で言ったことが圧縮で消える
<!-- textlint-enable -->

圧縮で消えない場所に約束を置くとは、守らせたい決めごとを、圧縮のあとに読み直されるファイルか、会話の外の仕組みに書いておくことである。圧縮は会話を要約に置き換える。会話の中だけで伝えた約束は、要約に残るとは限らない。本文は Claude Code の CLI（WSL・Linux）を基準にする。ほかの OS と IDE 拡張の動作は未確認である。

## 読み直される場所と、要約に溶ける約束 {#what-comes-back}

圧縮のあとに約束が残るかは、その約束がどこに書かれていたかで決まる。圧縮は、議事録だけを残して録音を捨てる作業にたとえられる。議事録に載らなかった口頭の約束は、後から見返せない。

例えば、作業の初めに「レビューが済むまで push しないで」と頼んだとする。数時間後に自動圧縮が走ると、この一文は要約に溶けうる。公式の文書は、会話の中だけで伝えた指示が要約に溶ける、と書く。一方、プロジェクトの根の CLAUDE.md は、圧縮のあとにディスクから入れ直される。会話の外にあるファイルは、要約の出来に左右されない。

残るもの・消えるものの全体は、<!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end --> の表が持つ。このページが押さえるのは、置き場所の判断に要る 2 点だけである。

1. 会話の中だけの指示は消えうる。くわしくは <!-- link:begin what-survives-compaction#dissolved -->[圧縮（compaction）で何が残り、何が消えるか › 要約に溶けて消えるもの](../basics/what-survives-compaction.md#dissolved)<!-- link:end --> にある。
2. 根の CLAUDE.md のように、ディスクから入れ直されるものは残る。くわしくは <!-- link:begin what-survives-compaction#reloaded -->[圧縮（compaction）で何が残り、何が消えるか › 入れ直されるもの](../basics/what-survives-compaction.md#reloaded)<!-- link:end --> にある。

約束を忘れた後に、原因を切り分けたいときは、<!-- link:begin forgot-after-compaction#diagnosis -->[圧縮の後に約束を忘れた › 原因を安く確かめる順](../symptoms/forgot-after-compaction.md#diagnosis)<!-- link:end --> から始める。

## 約束の種類ごとの置き場所 {#where-to-put}

守らせたい約束は、続く期間と、破られたときの重さで 3 種に分ける。種類ごとに置き場所が違う。

| 置き場所 | 向く約束 | 例 |
| --- | --- | --- |
| 根の CLAUDE.md | 続く規則 | テストの流し方、生成物を手で直さない理由 |
| 計画や handoff のファイル | この作業の決めごと | 触る範囲、方針、進み具合 |
| deny ルールとフック | 例外を許さない禁止 | `main` への push、秘密のファイルの読み書き |

**続く規則**は、根の CLAUDE.md に書く。圧縮のあとにディスクから入れ直されるからである。何を書き、何を外すかは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> にある。ただし、入れ直されるのは文脈であって、強制ではない（公式の文書は、CLAUDE.md を強制する設定ではなく文脈として扱うと書く）。

**この作業の決めごと**は、計画や handoff のファイルに書く。作業が終われば消せるものを、続く規則と混ぜないためである。plan mode で書いた計画はディスクから入れ直される。ふつうのファイルは自動では戻らないので、根の CLAUDE.md に「圧縮されたら、まずこのファイルを読む」と 1 行書いておく（この辞典の推奨）。置き場所の考え方は <!-- link:begin handoff-documents#where -->[handoff 文書と document-and-clear › 置き場所（圧縮で消えない所）](handoff-documents.md#where)<!-- link:end --> と同じである。

**例外を許さない禁止**は、deny ルールかフックで強制する。CLAUDE.md には理由と、止められたときの相談の基準だけを書く。会話で「レビューまで push しないで」と伝えると、auto モード（権限の確認を分類器に任せる動作）の分類器は止める合図として扱う。ただし公式の文書は、その一文は圧縮で失われうるので、確実にしたいことは deny ルールに書くよう勧める。どの規則を鍵に移すかの判断は <!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end --> と <!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end --> にある。deny ルールの書き方は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end --> にある。

3 種を 1 つの CLAUDE.md に書き分けた例を示す。

<!-- gen:begin snippet promises-after-compaction/carry-over-claude-md -->
<!-- textlint-disable -->

??? example "雛形：圧縮を越えて残す約束を 3 区分で書く CLAUDE.md の例"

    ```markdown
    # 作業の決めごと

    ## 続く規則（この repo の間ずっと）

    - テストは `make test` で流す。通ってから「終わった」と報告する。
    - `src/generated/` は手で直さない。`make codegen` で作り直す。理由は、手で直した分が次の生成で消えるため。

    ## この作業の決めごと（作業が終わったら消す）

    - 対象は `src/billing/` の請求計算だけ。ほかのモジュールの公開の関数は変えない。
    - 変更はブランチ `fix-billing-rounding` に積む。`main` への push は、レビューの後に人が行う。
    - 途中経過は `docs/billing-plan.md` に書く。会話が圧縮されたら、まずこのファイルを読み直す。

    ## 例外を許さない禁止（理由だけをここに書く）

    - `main` への push は deny ルールで止めてある。止まったら、回り込まずに人へ聞く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet promises-after-compaction/carry-over-claude-md -->

会話で伝えた禁止を、deny ルールに移した例を示す。

<!-- gen:begin snippet promises-after-compaction/deny-push -->
<!-- textlint-disable -->

??? example "雛形：会話で伝えた「push するな」を deny ルールに移す設定"

    ```json
    {
      "permissions": {
        "deny": [
          "Bash(git push *)",
          "Bash(git push)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet promises-after-compaction/deny-push -->

この雛形は `git push` をすべて止める。`main` だけを止めたいときは、パターンを自分のブランチ名に合わせて書き換える。deny ルールは、シェルから呼ばれる子プロセスの中の操作には効かない。効く範囲は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> で確かめる。

圧縮のあとに文脈を足し直したいだけなら、`compact` を matcher にした SessionStart フックが使える。このフックは圧縮のあとにもう一度走り、出力を圧縮後の文脈に足す。ただし足されるのは文脈であり、強制ではない。要約の方針を決めたいときは、CLAUDE.md に `# Compact instructions` の節を書くか、`/compact` に残す焦点を渡す。焦点の渡し方は <!-- link:begin compact-and-auto-compact#focused-compact -->[/compact と自動圧縮 › /compact に焦点を指示する](compact-and-auto-compact.md#focused-compact)<!-- link:end --> にある。

!!! example "判断例：最初に伝えた 2 つの約束をどこに置くか"
    - **状況**：長い作業の最初に、「`main` へ push しない」と「請求計算の範囲だけを触る」の 2 つを会話で伝えた。作業は数時間続き、自動圧縮が走る。
    - **迷う候補**：CLAUDE.md に 2 つとも書く。圧縮のたびに会話で言い直す。
    - **選んだもの**：push の禁止は deny ルールに移し、理由だけを CLAUDE.md に書く。範囲は計画のファイルに書き、CLAUDE.md にそのファイルを読む 1 行を足す。
    - **理由**：push の禁止は、破られると取り返しが付きにくい。毎回必ず効く鍵に移すのが筋である。範囲は、作業が終われば不要になる。CLAUDE.md に書き込むと、次の作業にまで残る。言い直しは、忘れた回に破られるので、守りとして足りない。

## paths 付きの rules とスキルの本文の注意 {#caveats}

根の CLAUDE.md に書いたつもりでも、圧縮のあとに戻らないものがある。次の 4 つに気を付ける。

- **paths 付きの rules**：`paths:` を持つ rules は、圧縮のあと、引き金のファイルを読むか書くまで戻らない。圧縮を越えて残したい規則は、`paths:` を外すか、根の CLAUDE.md に移す。戻る時期は <!-- link:begin path-scoped-rules#after-compaction -->[.claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期](../extend/path-scoped-rules.md#after-compaction)<!-- link:end --> にある。
- **サブフォルダの CLAUDE.md**：要約に消え、Claude がそのフォルダのファイルを扱ったときに読み直される。守らせたい規則は、根の CLAUDE.md に置く。
- **スキルの本文**：呼び出したスキルの本文は、上限付きで入れ直される。古いものから落ち、先頭を残して切られる。大事な指示は SKILL.md の上のほうに置く。説明文は、今のスキルから作り直して入れ直される。くわしくは <!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](../extend/how-skills-load.md#after-compaction)<!-- link:end --> にある。
- **フックが前に足した文脈**：会話と一緒に要約に溶けることがある。残したい内容は、フックの出力ではなくファイルに置く。

どの項目も、公式の文書の「圧縮の後に残るもの」の表に基づく。数値の上限は版で変わりうるので、ここには書かない。

## 何に効くか（縛る・見せる） {#effects}

この置き分けは、2 つの原理と 2 つの原因に結び付く。

- **縛る**：deny ルールとフックは、会話の外で毎回効く。Claude の記憶に頼らないので、圧縮に左右されない。原因の「縛っていない」を防ぐ。
- **見せる**：根の CLAUDE.md と計画のファイルは、圧縮のあとも Claude の目に入る場所に置き続ける。長い会話に埋もれた約束を、会話の外へ出す。原因の「散らかっている」を防ぐ。

縛るのは破られたくない禁止、見せるのは判断の材料になる規則や決めごと、と使い分ける。両方を使うのは、禁止の理由を見せ、禁止そのものは縛るときである。任せる幅を広げるほど、縛る側を先に整える。お願いと鍵の分け方は <!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end --> にある。

## 誤解されやすいこと {#misconceptions}

- **誤解：「入れ直される」なら守られる**：根の CLAUDE.md は圧縮のあとに戻る。だが公式の文書はそれを強制ではなく文脈として扱う。例外を許さない規則は、鍵に移す。
- **誤解：焦点を付けた `/compact` で約束を守らせられる**：残すよう促せるが、要約を作る側へのお願いである。保証にはならない。
- **誤解：スキルの一覧は圧縮で戻らない**：スキルの説明文は、今のスキルから作り直して入れ直される。説明文を CLAUDE.md に写す必要はない。
- **誤解：圧縮を避ければ済む**：圧縮を減らしても、会話の中だけの約束は、要約に溶けうる状態のままである。置き場所を移すほうが確実である。圧縮か、書き出して `/clear` するかは <!-- link:begin compact-and-auto-compact#compact-or-clear -->[/compact と自動圧縮 › 圧縮か、書き出して /clear か](compact-and-auto-compact.md#compact-or-clear)<!-- link:end --> で選ぶ。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)

**関連**

- [/compact と自動圧縮](compact-and-auto-compact.md)
- [お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [.claude/rules と paths で必要なときだけ読ませる](../extend/path-scoped-rules.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)
- [handoff 文書と document-and-clear](handoff-documents.md)
- [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
