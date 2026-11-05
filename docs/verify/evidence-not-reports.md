---
id: evidence-not-reports
title: 報告ではなく証拠を求める
aliases: [自己申告ではなく証拠, 実行結果で確かめる, 生の出力を出させる]
type: concept
field: verify
chapter: 完了を確かめる
order: 20
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, データ分析]
summary: 完了の報告を、実行したコマンドと生の出力と分母のそろった証拠で受け取れる。説明と事実が食い違えば、実行・grep・git で見た事実を正とする。
signs:
  - {type: symptom, text: テストの件数が、報告のたびに変わっている}
  - {type: symptom, text: うまくいった場合だけを並べた報告が返ってくる}
  - {type: goal, text: 見ていなかった作業が本当に済んだかを、短い時間で確かめたい}
prerequisites: [define-done]
related: [verification-ladder, claims-done-but-isnt, blames-the-tools, visual-checks, diffs-humans-must-read, looks-are-not-quality, suspect-too-good-results, checking-unattended-runs, insists-on-mistakes, unfaithful-reasoning, experiment-log]
tracks: []
outdated_advice: []
sources: [cc-docs-best-practices, cc-issue-46940, cc-issue-64286, cc-changelog, cc-docs-changelog]
volatility: 低
sections:
  - {title: 件数が変わっても「全部通過」と返ってくる, anchor: what-happens}
  - {title: 証拠の形（コマンド・生の出力・分母）, anchor: what-counts}
  - {title: 説明と事実が食い違ったら, anchor: facts-win}
  - {title: 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動）, anchor: tool-output}
  - {title: 何に効くか、どこまで効くか, anchor: what-it-prevents}
  - {title: 誤解しやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：実行したコマンドと生の出力と分母がそろった証拠で、完了の報告を受け取れる。
    - **いつ引くか**：テストの件数が報告のたびに変わるとき。うまくいった場合だけを並べた報告が返ってくるとき。見ていなかった作業が済んだかを、短い時間で確かめたいとき。
    - **前提**：<!-- link:begin define-done -->[「完了」を定義して渡す](define-done.md)<!-- link:end -->

<!-- textlint-disable -->
別名：自己申告ではなく証拠・実行結果で確かめる・生の出力を出させる
<!-- textlint-enable -->

報告ではなく証拠を求めるとは、「終わった」「通った」という文章を受け取る代わりに、何を実行して何が返ったかを出させることである。説明と事実が食い違えば、実行・`grep`・git で見た事実を正とする。この辞典の原理でいう「確かめる」を、完了の報告の受け取り方に当てはめたものである。

## 件数が変わっても「全部通過」と返ってくる {#what-happens}

完了の報告が文章だけだと、事実とずれていても、読む側には見分けがつかない。公開された事例が 2 つある。

- 事例 1（GitHub の Issue #46940、2026-04-12、Opus 4.6）：回帰テストが 4992/4992 から 4985/4992 に落ちた。Claude は件数を 4966/4966 に変えて「ALL PASSED」と報告し、壊れたコードを commit した。（根拠：弱。単独の報告で、原典の Issue を出典にした）
- 事例 2（GitHub の Issue #64286、Opus 4.8・effort High）：「162 tests green」と報告したが、実際は 3 件のテストが `FileNotFoundError` で失敗していた。利用者は統合の準備ができていないと考えていたのに、Claude は main に統合して push した（根拠：弱。単独の報告）。

2 件とも、報告の文章は「通った」と読める。違いは 2 点ある。分母が途中で変わったことと、失敗の出力が報告に載らなかったことである。

公式の文書は、仕組みの側の理由を次のように説明している。Claude は作業が終わったように見えた時点で止まる。終わったかを判定するものを実行できなければ、「終わったように見える」ことしか判断材料がない（出典は公式の Best practices）。この理由は <!-- link:begin define-done#why-it-stops -->[「完了」を定義して渡す › 終わったように見えた所で止まる](define-done.md#why-it-stops)<!-- link:end --> でも扱う。

## 証拠の形（コマンド・生の出力・分母） {#what-counts}

証拠とは、読む側が自分で再実行しなくても、事実との食い違いを見つけられる材料のことである。次の 3 つがそろっていれば足りる。

- **コマンド**：実際に実行したものを、そのまま。再実行できる形で出させる。
- **生の出力**：要約や言い換えをしない出力。長いときは末尾の行と終了コード、ログの置き場所を添えさせる。
- **分母**：対象の総数、実行した件数、通った件数、失敗した件数、飛ばした件数。分母が前回と変わったら、変わった理由を先に書かせる。

「All tests pass」だけでは情報がほとんどない。見ていなかったセッションでは、実行したコマンドとその出力が唯一の証拠になる。出力を読むほうが、自分でもう一度実行するより速い（出典は公式の Best practices）。

| 受け取るもの | 報告の例 | 見つけられること |
| --- | --- | --- |
| 文章だけ | 全部通りました | 何も見つけられない |
| コマンドと出力 | `uv run pytest` と、その最後の数行 | 実行していない、または別のものを実行した |
| さらに分母 | 通った 4985、失敗 7、飛ばし 0、全体 4992 | 件数のすり替え、飛ばした件数 |

分母が要るのは、件数の変化が最初に出る場所だからである。うまくいった場合だけを並べる報告も、失敗と飛ばした件数の欄が埋まっていないことで見つかる。改善を主張させるときは、前回と同じ対象で比べさせ、最悪の例も 1 件挙げさせる。

!!! example "判断例：改善の報告を受け取る"
    - **状況**：処理を速くする修正を頼んだ。報告は「平均が速くなった」とだけ書いてある。
    - **迷う候補**：報告を信じて統合し、問題が出てから調べる案と、コマンドと分母を出させてから決める案。
    - **選んだもの**：コマンドと分母を出させてから決める。
    - **理由**：平均だけの報告では、対象を減らしたのか、失敗した例を外したのかが分からない。分母を前回と同じにそろえさせれば、比べられる。

コマンド・生の出力・分母の形を依頼に書いておくと、毎回の頼み直しが要らない。

<!-- gen:begin snippet evidence-not-reports/report-with-evidence -->
<!-- textlint-disable -->

??? example "雛形：完了の報告を、コマンド・生の出力・分母・最悪の例・前回との差で書かせる依頼"

    ```markdown
    作業が済んだと報告するときは、次の形で書く。要約だけの報告は受け取らない。

    1. 実行したコマンド：実際に実行したものを、そのまま写す。省略や言い換えをしない。
    2. 生の出力：コマンドの出力を、加工せずに貼る。長いときは、最後の 20 行と終了コードを貼り、ログの置き場所を書く。
    3. 分母：対象の総数、実行した件数、通った件数、失敗した件数、飛ばした件数を書く。件数が前回と違うときは、違う理由を先に書く。
    4. 最悪の例：失敗したもの、または結果が最も悪かったものを 1 件挙げる。
    5. 前回との差：前回の同じコマンドの結果と並べる。分母（対象の集合）は前回と同じにする。変えたいときは、変えずに報告し、変更の案を別に書く。

    コマンドを実行できなかった、または出力が空だったときは、成功とせず、その旨を書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet evidence-not-reports/report-with-evidence -->

「完了」の条件そのものを先に決める方法は <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](define-done.md#what-to-include)<!-- link:end --> で扱う。報告の形を決めても、何をもって終わりとするかが曖昧なら、証拠の対象が定まらない。

## 説明と事実が食い違ったら {#facts-win}

報告の文章と、実行・`grep`・git で見た事実が食い違ったときは、事実を正とする。報告は主張として読み、証拠として読まない。

- 「呼び出し箇所を全部直した」と言うなら、`grep` で古い呼び方が残っていないかを見る。
- 「テストを足した」と言うなら、`git diff` で、足したテストと、変えたテストの両方を見る。
- 「変えていない」と言うなら、`git status` で、変わったファイルの一覧を見る。

食い違いが見つかったら、言い争う代わりに、見つけた事実をそのまま見せる。見せ方は <!-- link:begin insists-on-mistakes#diagnosis -->[誤りを認めずに言い張る › 原因を安く確かめる順](../symptoms/insists-on-mistakes.md#diagnosis)<!-- link:end --> にある。

Claude が書いた「こう確かめた」という説明も、同じである。表示された思考や説明は、内部の処理と一致するとは限らない。説明のもっともらしさを信じず、結果を別の方法で確かめる（仕組みは <!-- link:begin unfaithful-reasoning -->[表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)<!-- link:end --> を参照）。

!!! example "判断例：報告と差分が合わない"
    - **状況**：「テストは変えずに実装だけを直した」という報告が来た。差分には、テストの期待値の変更が含まれている。
    - **迷う候補**：実装が直ったのだから、期待値の変更は小さな整理として見逃す案と、報告と差分の食い違いとして、変更の理由を確かめる案。
    - **選んだもの**：食い違いとして、変更の理由を確かめる。
    - **理由**：テストの変更は、通らないものを通す近道にもなる。説明と差分が合わないなら、差分を正として、その変更が妥当かを見る。読む箇所の見分け方は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](diffs-humans-must-read.md#red-flags)<!-- link:end --> にある。

## 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動） {#tool-output}

証拠として受け取る出力そのものが、不完全なことがある。公式の CHANGELOG には、次の 2 つの不具合を直した記録がある（直った版は各項目に書く。それより前の版で起きうる）。

- **途中で切れた検索**：Grep と Glob の検索が時間切れで途中までしか返さなかったのに、Claude がそれを全部の結果とみなしていた。直った版は、<!-- fact:begin claude-code-search-truncation-fix-version -->Claude Code 2.1.317（2026-11-06 時点）<!-- fact:end -->。「その呼び出しはない」と言い切られたときは、検索が打ち切られていないか、別の語や範囲で検索し直して確かめる。
- **失敗を成功として返す起動**：`claude -p` が、起動に失敗しても何も出さず、終了コード 0 で終わっていた。直った版は、<!-- fact:begin claude-code-p-startup-failure-exit-code-fix-version -->Claude Code 2.1.314（2026-11-06 時点）<!-- fact:end -->。終了コードだけで成功を決める CI は、直る前の版では起動の失敗を見逃した。0 で終わっても、出力が空でないか、期待する成果物ができたかを見る。

どちらも、「検索で出なかった」「終了コードが 0 だった」という安い証拠が、事実を表していない例である。ここでも、出力の中身と分母（何件のうち何件を見たか）を見る。

公開された事例 2（Issue #64286）では、Claude 自身が後に、道具の出力が文字化けして空になり、結果を捏造することもあったと述べている（根拠：弱。単独の報告）。出力が空のときは、成功とせず、実行できなかったものとして扱う。道具が壊れたと言い出したときの切り分けは <!-- link:begin blames-the-tools#diagnosis -->[環境や道具が壊れたと言い出す › 原因を安く確かめる順](../symptoms/blames-the-tools.md#diagnosis)<!-- link:end --> にある。人が見ていない実行の出力は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> で扱う。

## 何に効くか、どこまで効くか {#what-it-prevents}

このページが当てはまる原理は「確かめる」、防ぐ原因は「確かめていない」である。確かめる手段を持たない Claude は、終わったように見えた所で止まる。読む側も、証拠を受け取らなければ、確かめていないまま受け取る。証拠を求めると、確かめていない状態が、報告の段階で見える形になる。

効かない場面もある。

- 証拠の形式を満たしていても、中身が事実とは限らない。重要な判断の前には、自分で 1 回再実行する。
- 分母がそろっていても、そもそも測っているものが間違っていれば、そろった数字は意味を持たない。測るものを決めるのは <!-- link:begin define-done -->[「完了」を定義して渡す](define-done.md)<!-- link:end --> の役目である。
- 結果が良すぎるときは、形式がそろっていても疑う。<!-- link:begin suspect-too-good-results#self-check -->[良すぎる結果を疑う › 報告の前に自己点検させる](suspect-too-good-results.md#self-check)<!-- link:end --> を使う。

## 誤解しやすいこと {#misconceptions}

- **「念のため確認して」と書き足せば、証拠が出る**：言葉で命じるだけでは、確かめる手段が渡っていない。何を実行して何を返すかを書く。違いは <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](verification-ladder.md#verbal-checks)<!-- link:end --> にある。
- **証拠を求めれば、捏造は起きない**：出力の貼り付けも、受け取る側が読んで初めて証拠になる。読む場所は、件数・失敗の行・終了コードの 3 つで足りる。
- **全部の報告で、全部を再実行すべきだ**：そうではない。任せる幅に応じて確かめの段を選ぶ。選び方は <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](verification-ladder.md#choose-step)<!-- link:end --> にある。見た目がそろっているだけで安心することへの注意は <!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](looks-are-not-quality.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Claude fabricates test results - reports ALL PASSED when tests are FAILING（Issue #46940）](https://github.com/anthropics/claude-code/issues/46940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Claude Code fabricated test results and pushed untested code to main branch (Opus 4.8 @ Effort = High)（Issue #64286）](https://github.com/anthropics/claude-code/issues/64286)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [「完了」を定義して渡す](define-done.md)

**次に読む**

- [検証の階段](verification-ladder.md)
- [画面で確かめる（ブラウザ・スクリーンショット・/verify）](visual-checks.md)
- [人間が読むべき差分の箇所](diffs-humans-must-read.md)
- [見た目は品質の証拠ではない](looks-are-not-quality.md)
- [良すぎる結果を疑う](suspect-too-good-results.md)
- [バグを直す](../recipes/fix-a-bug.md)
- [データを分析する](../recipes/data-analysis.md)

**関連**

- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [無人実行の結果を確かめる](checking-unattended-runs.md)
- [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- [表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
