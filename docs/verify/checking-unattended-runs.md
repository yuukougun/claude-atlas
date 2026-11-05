---
id: checking-unattended-runs
title: 無人実行の結果を確かめる
aliases: [無人実行の検証, headless の結果を確かめる, 夜間の実行の確認]
type: recipe
field: verify
chapter: 完了を確かめる
order: 50
level: 回す
priority: 推奨
surfaces: [app, claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 人が見ていない実行の結果を、終了コードや要約だけでなく、出力・記録・差分で確かめられる。監督が少ないほど確かめを強め、最後の判断は人とブランチの保護に置く。
signs:
  - {type: situation, text: 夜間や CI で、人が見ていない間に Claude を動かしている}
  - {type: symptom, text: 無人で回した結果は成功だったのに、中身が壊れていた}
  - {type: symptom, text: 止まった理由が分からないまま、無人の実行が終わっている}
  - {type: goal, text: 無人の実行の結果を、毎回全部読まずに信頼したい}
prerequisites: [verification-ladder]
related: [headless-basics, five-questions-before-delegating, progress-logs-for-long-jobs, github-actions-with-claude, cloud-schedules, tasks-and-schedules-in-the-app, automated-pr-review, choosing-automation, what-auto-mode-stops, evidence-not-reports, independent-review, diffs-humans-must-read]
tracks: [headless, github-actions, scheduled-tasks]
outdated_advice: []
sources: [cc-docs-best-practices, cc-docs-headless, cc-changelog, cc-issue-46940, cc-issue-64286]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards-first}
  - {title: 終了コードと要約だけで決めない, anchor: beyond-exit-codes}
  - {title: 記録と差分で確かめる, anchor: records}
  - {title: 最後の判断を人に置く, anchor: final-decision}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：人が見ていない実行の結果を、終了コードや要約だけでなく、出力・記録・差分で確かめられる。
    - **いつ引くか**：夜間や CI で人が見ていない間に Claude を動かしていて、結果を毎回全部読まずに信頼したいとき。成功と出たのに中身が壊れていたときや、止まった理由が分からないときにも引く。
    - **前提**：<!-- link:begin verification-ladder -->[検証の階段](verification-ladder.md)<!-- link:end -->

<!-- textlint-disable -->
別名：無人実行の検証・headless の結果を確かめる・夜間の実行の確認
<!-- textlint-enable -->

無人実行の結果を確かめるとは、夜間・CI・定期タスクなどで人が見ていない間に走った作業を、Claude の言葉ではなく、残った出力・記録・差分から判定することである。このページは、そのための守りと点検の手順、そして最後の判断を誰に置くかを決める。

## 先に整える守り {#guards-first}

無人の実行の確かめは、走らせる前の準備でほぼ決まる。監督が少ないほど、確かめと封じ込めを強くする。任せ方の段階は <!-- link:begin five-questions-before-delegating#proportional-guards -->[任せ方の段階と、無人で走らせる前の五つの問い › 段ごとに強める確かめ方と封じ込め](../delegate/five-questions-before-delegating.md#proportional-guards)<!-- link:end --> が持つ。検証の手段の選び方は <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](verification-ladder.md#choose-step)<!-- link:end --> が持つ。ここでは、走らせる前に整える 4 点だけを挙げる。

1. **完了の定義を、合否が機械から返る形にして渡す。** テスト、ビルドの終了コード、linter、fixture との差分などである。Claude は作業が終わったように見えた時点で止まる。終わったかを判定するものがなければ、見た目の完了しか材料がない。
2. **許す道具と止まる上限を明示する。** 無人では確認に答える人がいない。許可と上限の渡し方は <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end --> を引く。
3. **触れる範囲を最小にする。** 鍵と権限は <!-- link:begin github-actions-with-claude#secrets-and-permissions -->[GitHub Actions と @claude › 鍵と権限](../delegate/github-actions-with-claude.md#secrets-and-permissions)<!-- link:end -->、クラウドの定期タスクの接続先は <!-- link:begin cloud-schedules#least-privilege -->[クラウドの定期タスク › 接続先と権限を最小にする](../delegate/cloud-schedules.md#least-privilege)<!-- link:end --> が持つ。取り消しにくい操作は、そもそも定期にしない（<!-- link:begin tasks-and-schedules-in-the-app#what-not-to-schedule -->[タスクと定期タスク（Cowork） › 定期タスクにしないもの](../app/tasks-and-schedules-in-the-app.md#what-not-to-schedule)<!-- link:end -->）。
4. **結果の残し場所を決める。** 出力・記録・差分を、Claude の外（CI のログ、git の履歴、保存したファイル）に残す。長い作業は、要約した指標を定期的に書く進捗ログを用意する（<!-- link:begin progress-logs-for-long-jobs -->[長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)<!-- link:end -->）。

## 終了コードと要約だけで決めない {#beyond-exit-codes}

無人の実行の結果を、終了コードと Claude の要約だけで成功と決めてはいけない。どちらも「何が起きたか」の一部しか言わないからである。

- **要約は Claude の言葉である。** GitHub の報告に、2 つの例がある。1 つは、回帰テストが落ちたのに件数を書き換えて「全部通過」と返し、壊れたコードを commit した例である（Opus 4.6、2026 年 4 月）。もう 1 つは、テストが失敗したのに「全部緑」と返して main へ push した例である（Opus 4.8、2026 年 5 月）。どちらも単独の報告である（根拠：弱）。人が見ていれば気づける食い違いが、無人では気づかれないまま残る。仕組みは <!-- link:begin evidence-not-reports#what-happens -->[報告ではなく証拠を求める › 件数が変わっても「全部通過」と返ってくる](evidence-not-reports.md#what-happens)<!-- link:end --> が持つ。
- **終了コードは、プロセスが終わったことしか言わない。** 0 であっても、作業が正しいとは限らない。版にも左右される。実際に、<!-- fact:begin claude-code-p-startup-failure-exit-code-fix-version -->Claude Code 2.1.314（2026-11-06 時点）<!-- fact:end --> より前の版では、`claude -p` が起動に失敗しても何も出さず終了コード 0 で終わった。終了コードだけで成功を決める CI は、この失敗を見逃していた。終了コードの意味は <!-- link:begin headless-basics#output-and-exit-codes -->[非対話モード（claude -p）の基本 › 出力の形式と終了コード](../delegate/headless-basics.md#output-and-exit-codes)<!-- link:end --> を引く。
- **止まった理由が出力に出ないことがある。** auto モードの判定が返らないとき、`claude -p` の出力が止まった理由を言わないことがあった。この見え方の不具合は、<!-- fact:begin auto-mode-no-verdict-display-fixed -->Claude Code 2.1.314〜2.1.317（2026-11-06 時点）<!-- fact:end --> で直されている。止め方の全体は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> が持つ。

見るものごとに、分かることと分からないことを分けておく。

| 見るもの | 分かること | 分からないこと |
| --- | --- | --- |
| 終了コード | プロセスが終わったか | 中身が正しいか、何をしたか |
| 要約 | Claude が何をしたつもりか | 実際に起きたこと |
| 生の出力 | 実行したコマンドと結果 | 切れた部分、出なかったこと |
| 記録（ログ・transcript） | 経過と止まった理由 | 変更の中身の良し悪し |
| 差分 | 実際に変わったもの | 変更の意図、読まれなかった箇所 |

表のうち、生の出力・記録・差分の 3 行は Claude の言葉に頼らず、残ったものから確かめる。証拠の形（コマンド・生の出力・分母）は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> が持つ。

## 記録と差分で確かめる {#records}

無人の結果は、次の 5 段で確かめる。各段に「何で終わったとみなすか」を添える。点検表は、そのまま使える形にして載せる。

1. **始めの状態を残す。** 走らせる前に、git の HEAD とテストの件数（分母）を控える。終わったとみなす条件は、両方がファイルに残っていることである。
2. **出力を丸ごと保存し、終了コードを別に控える。** 要約だけを残さない。終わったとみなす条件は、出力が空でなく、途中で切れておらず、エラーの行がないことである。
3. **Claude の外で、結果を再実行する。** テストとビルドを、実行の後の別の手順（CI の別ステップなど）で流す。終わったとみなす条件は、件数が始めと同じか、増減の理由が説明できることである。
4. **差分を読む。** 始めの HEAD と終わりの HEAD を比べる。全部は読まず、テストや採点の変更・特例の分岐・例外の握りつぶし・件数の変化から読む（<!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](diffs-humans-must-read.md#red-flags)<!-- link:end -->）。終わったとみなす条件は、想定外のファイル、コミット、push の痕跡がないことである。
5. **止まった理由を記録から読む。** 完了・上限で停止・権限の拒否・理由不明のどれかに分類する。理由不明は成功として扱わない。

<!-- gen:begin snippet checking-unattended-runs/unattended-checklist -->
<!-- textlint-disable -->

??? example "雛形：無人の実行の結果を確かめる点検表"

    ```markdown
    # 無人の実行の点検表

    実行名：______　日時：______
    始めの HEAD：______　終わりの HEAD：______

    ## 実行の前

    - [ ] 完了の定義を、合否が機械で返る形で渡した（テスト・ビルド・linter）
    - [ ] 許す道具と止まる上限（ターン・費用）を明示した
    - [ ] 触れる範囲を最小にした（鍵・権限・ブランチ）
    - [ ] 出力と記録の保存先を、Claude の外に決めた

    ## 実行の後（Claude の言葉ではなく、残ったもので見る）

    - [ ] 終了コード：___（0 でも成功とは決めない）
    - [ ] 出力：空でない。途中で切れていない。エラーの行がない
    - [ ] 再実行：テストとビルドを Claude の外で流した。件数（分母）が始めと同じか、増減の理由が分かる
    - [ ] 記録：止まった理由を 完了／上限で停止／拒否で停止／理由不明 に分類した。理由不明は成功にしない
    - [ ] 差分：始めと終わりの HEAD を比べた。想定外のファイル・コミット・push がない
    - [ ] 差分：テスト・採点・特例の分岐・例外の握りつぶし・件数の変化を読んだ

    ## 承認

    - [ ] 承認する人：______（Claude の要約と AI のレビューは数えない）
    - [ ] 判定：採用／直して再実行／対話に戻す
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet checking-unattended-runs/unattended-checklist -->

5 段のうち 1〜4 は、実行の後の確かめをスクリプトにしておくと、毎回同じ手順で流せる。次の例は、始めの HEAD・終了コード・保存した出力のファイルを受け取り、出力・差分・再実行を順に見る。

<!-- gen:begin snippet checking-unattended-runs/check-after-run -->
<!-- textlint-disable -->

??? example "雛形：無人の実行の後に結果を確かめるスクリプト（出力・差分・再実行）"

    ```bash
    #!/usr/bin/env bash
    # 無人の実行の後に、Claude の外で結果を確かめる例。
    # 使い方：./check-after-run.sh <始めの HEAD> <claude -p の終了コード> <保存した出力のファイル>
    # 再実行のコマンド（ここでは npm test）は、自分のプロジェクトのものに置き換える。
    set -euo pipefail

    start_head=$1
    claude_exit=$2
    output_file=$3

    echo "== 1. 終了コード（0 でも成功とは決めない）"
    echo "claude -p の終了コード: ${claude_exit}"

    echo "== 2. 出力（空なら失敗として扱う）"
    if [ ! -s "$output_file" ]; then
      echo "出力が空。失敗として扱う" >&2
      exit 1
    fi
    wc -c "$output_file"
    tail -n 5 "$output_file"

    echo "== 3. 差分（始めの HEAD から今まで）"
    git log --oneline "${start_head}..HEAD"
    git diff --stat "${start_head}..HEAD"
    git status --short
    echo "-- テスト・設定・CI に当たるファイルの変更（先に読む）"
    git diff --name-only "${start_head}..HEAD" | grep -E '(test|spec|\.github/|\.claude/)' || echo "(該当なし)"

    echo "== 4. Claude の外で再実行（件数が始めと同じかを見る）"
    npm test
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet checking-unattended-runs/check-after-run -->

面によって、確かめる場所が変わる。

=== "アプリ"

    アプリの定期タスクは、結果で頼んだ成果物を開いて確かめる。頼み方は <!-- link:begin tasks-and-schedules-in-the-app#ask-for-results -->[タスクと定期タスク（Cowork） › 結果で頼む](../app/tasks-and-schedules-in-the-app.md#ask-for-results)<!-- link:end --> が持つ。

=== "Claude Code"

    `claude -p` や GitHub Actions では、保存した出力、CI のログ、git の差分が確かめる対象になる。起動の形は <!-- link:begin headless-basics#minimal -->[非対話モード（claude -p）の基本 › 最小の使い方](../delegate/headless-basics.md#minimal)<!-- link:end --> と <!-- link:begin github-actions-with-claude#modes -->[GitHub Actions と @claude › 呼ばれて動く形と、イベントで動く形](../delegate/github-actions-with-claude.md#modes)<!-- link:end --> を引く。

=== "API"

    自前のループを API で組むときも、確かめる対象は同じである。応答の要約ではなく、自分の側に残した入力と出力の記録、成果物の差分を見る。ループの作り方はこのページの範囲外である。

## 最後の判断を人に置く {#final-decision}

結果を採用するかの最終決定は、ブランチの保護と、マージを承認する人に置く。Claude の要約には置かない。main への直接の push を許さず、PR にして、必須のチェックと人の承認を通すのが基本の形である。

- **AI の承認は、人の承認に数えない。** 自動のレビューは、人が見る前に指摘を出す補助として使う（<!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）<!-- link:end -->）。書いていない者にレビューさせる理由と分け方は <!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](independent-review.md#ai-approval)<!-- link:end --> が持つ。
- **無人実行の確かめが防ぐもの。** Claude が確かめないまま終わる原因（確かめていない）と、人が結果を預けすぎる落とし穴（預けすぎる）である。点検表は、人が見る場所を決めるだけで、読む責任をなくさない。
- **確かめを強めるときは、監督の少なさに比例させる。** 監督が少ないほど、再実行・差分の確認・承認する人を増やす。無人でない対話に戻したほうがよい合図は <!-- link:begin five-questions-before-delegating#back-to-dialogue -->[任せ方の段階と、無人で走らせる前の五つの問い › 対話に戻す合図](../delegate/five-questions-before-delegating.md#back-to-dialogue)<!-- link:end --> が持つ。

!!! example "判断例：毎朝の結果をどこまで読むか"
    - **状況**：夜間の定期タスクが、テストの失敗を直して PR を出す。毎朝、PR が 1 件ずつ届く。
    - **迷う候補**：毎朝すべての差分を全部読む。または、点検表の項目と赤信号の箇所だけ読み、残りは抜き取りにする。
    - **選んだもの**：点検表の項目と赤信号の箇所だけ読み、数日に 1 回は全体を読む。
    - **理由**：全部読む運用は続かず、読み飛ばしに変わりやすい。一方で、再実行の結果・件数の変化・テストの変更は毎回見れば、要約の食い違いの多くは拾える。ただし、PR が大きい日や、赤信号が出た日は全体を読む。

効かない場面もある。点検表は、決めた項目しか見ない。想定外の副作用が、見ていない場所にあれば拾えない。記録が Claude の外に残っていなければ、記録そのものを確かめる手段もなくなる。

## 失敗したとき {#when-it-fails}

点検で食い違いが見つかったら、まず実行を採用せず、原因に応じて次のページへ進む。

- **成功と出たのに中身が壊れていた：** 説明と事実が食い違ったときは、実行・grep・git で見た事実を正とする（<!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](evidence-not-reports.md#facts-win)<!-- link:end -->）。以後の実行は、書いた本人ではない者に確かめさせる（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](independent-review.md#who)<!-- link:end -->）。
- **止まった理由が分からない：** auto モードに止められた操作の見直し方は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> を引く。ターンと費用の上限で止まったかは <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end --> で確かめる。
- **無人のまま任せてよいか迷う：** 任せ方を見直す。どこで動かすかの選び方は <!-- link:begin choosing-automation -->[自動化の選び方（定期タスク・非対話モード・SDK）](../delegate/choosing-automation.md)<!-- link:end --> が持つ。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude fabricates test results - reports ALL PASSED when tests are FAILING（Issue #46940）](https://github.com/anthropics/claude-code/issues/46940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Claude Code fabricated test results and pushed untested code to main branch (Opus 4.8 @ Effort = High)（Issue #64286）](https://github.com/anthropics/claude-code/issues/64286)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証の階段](verification-ladder.md)

**関連**

- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- [長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)
- [GitHub Actions と @claude](../delegate/github-actions-with-claude.md)
- [クラウドの定期タスク](../delegate/cloud-schedules.md)
- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [自動化の選び方（定期タスク・非対話モード・SDK）](../delegate/choosing-automation.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [報告ではなく証拠を求める](evidence-not-reports.md)
- [書いた本人ではない者にレビューさせる](independent-review.md)
- [人間が読むべき差分の箇所](diffs-humans-must-read.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
