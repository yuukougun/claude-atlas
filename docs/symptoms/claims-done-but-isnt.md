---
id: claims-done-but-isnt
title: 「完了」と言うが終わっていない
nav_title: 完了と言うが終わっていない
aliases: [偽の完了, 全部通ったと言うのに動かない, 完了の報告が信用できない]
type: symptom
field: symptoms
chapter: 完了と検証
order: 210
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析]
summary: 「完了」「全部通った」という報告が事実と違う原因を切り分け、完了の定義と証拠を渡す・別の者に確かめさせる、のどこから足すかを決める。
signs:
  - {type: symptom, text: 「全部通りました」と言うが信用できない}
  - {type: symptom, text: 完了と報告されたのに動かない}
  - {type: symptom, text: 計画したはずの確認を実際にはやっていない}
  - {type: symptom, text: 「ほかに該当する箇所はない」と言い切られたが残っていた}
wave: 1
prerequisites: [agent-loop]
related: [tests-first, fix-a-bug#no-symptom-patches, visual-checks, goal-until-done, stop-hooks, rewrote-tests-to-pass, misses-broken-evaluation, blames-the-tools, six-causes]
routes:
  - {cause: 見えていない, to: [define-done]}
  - {cause: 確かめていない, to: [evidence-not-reports, verification-ladder, independent-review]}
  - {cause: 預けすぎる, to: [over-reliance#cheap-verification, checking-unattended-runs]}
tracks: [goal, hooks]
outdated_advice: [add-double-check]
sources: [cc-docs-best-practices, cc-issue-46940, cc-issue-64286, drivendata-ai-agents-data-science-competitions, mercari-ai-lied-me-thats-learned, cc-changelog]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 似た症状との見分け, anchor: lookalikes}
  - {title: 判断例, anchor: example}
  - {title: 予防：仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：「完了」という報告が事実と違う原因を 3 つに切り分け、完了の定義と証拠を渡す・別の者に確かめさせる、のどれから足すかを決められる。
    - **いつ引くか**：「全部通りました」と言うが信用できない・完了と報告されたのに動かない・計画した確認をやっていない・「ほかに該当する箇所はない」と言い切られたが残っていた、とき。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：偽の完了・全部通ったと言うのに動かない・完了の報告が信用できない
<!-- textlint-enable -->

「完了」と言うが終わっていない症状は、Claude の報告と実物が食い違うことである。報告の文は「通った」「直した」「ほかにない」と言い切るのに、実行すると失敗する。見落とすと、壊れたものがそのまま commit や push に進む。

公式の Best practices は、この症状の背景を次のように説明する。Claude は、作業が終わったように見えた時点で止まる。本当に終わったかを判定するものを実行できなければ、判断材料は「終わったように見える」ことだけである。この仕組みは前提の <!-- link:begin agent-loop#why-stops -->[エージェントループと tool use › 確かめる手段がないと、終わったように見えたところで止まる](../basics/agent-loop.md#why-stops)<!-- link:end --> にある。このページは、起きたときに原因を切り分け、どこから足すかを決める入口である。

## よくある形 {#forms}

「完了」の報告が外れる形は、次の 5 つに分けると見分けやすい。いずれも公開された事例の報告で、起きた条件は版やモデルで違う。

- **分母の入れ替え**：落ちたテストの件数を伏せ、分母ごと変えて「全部通った」と書く。GitHub の issue に、4992 件中 7 件が失敗していたのに、「4966/4966 ALL PASSED」と報告されて壊れたコードが commit された例がある（Opus 4.6、2026-04-12。根拠：弱）。
- **失敗の見落としと未検証の push**：別の issue に、「162 tests green」と報告されたが、実際は 3 件が失敗していた。それでも main に統合して push された例がある（Opus 4.8、effort は High。根拠：弱）。
- **計画した確認をやっていない**：データ分析のコンテストで、5-fold の交差検証を計画しながら実行せず、単一の分割で済ませた例がある。過去の自分の版より悪い提出を最終に選ぶこともあった（実践者の報告。根拠：弱）。実践者の記事には、指定した静的解析の道具を使わず別の方法で作り、動くことだけを確かめて完了と報告した例もある（根拠：弱）。
- **都合のよい部分集合だけの報告**：評価や集計の要約で、結果の良い部分だけを強調する。全体の数字が書かれていないときに疑う（実践者の報告。根拠：弱）。
- **「ない」の言い切り**：検索の結果が途中で打ち切られていたのに、全部の結果とみなして「ほかに該当する箇所はない」と言い切る。過去の版には、検索が時間切れで途中までしか返さなかったのを全部とみなす不具合や、起動に失敗しても終了コード 0 で終わる不具合があり、のちの版で直った（CHANGELOG の記録）。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。最初に、報告と実物の食い違いを事実で確定する。報告された確認のコマンドを自分で実行するか、`git diff` と `git status` で変更の中身を見る。食い違いがなければ、症状は別の原因なので、このページを閉じてよい。食い違いが確定したら、次の順に確かめる。

1. **見えていない**：Claude に「終わり」の形が渡っていない。
    - 見るもの：依頼と CLAUDE.md に、どのコマンドがどう返れば終わりかが書いてあるか。そのコマンドは Claude の環境で動くか。
    - 確かめ方：依頼の文面を読み返す。合否を返すコマンドがどこにもなければ、Claude は「終わったように見える」ところで止めるしかない。渡し方は <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> にある。
    - 検索や起動の出力が途中で切れていないかも、ここで見る。「ない」と言い切られたときは、検索の打ち切りや、失敗を成功として返した起動を疑う。見分け方は <!-- link:begin evidence-not-reports#tool-output -->[報告ではなく証拠を求める › 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動）](../verify/evidence-not-reports.md#tool-output)<!-- link:end --> にある。
2. **確かめていない**：確かめる手段はあったのに、確かめた形跡がない。
    - 見るもの：報告に、実行したコマンドと生の出力と、通った件数・全体の件数がそろっているか。最初の計画にあった確認が、報告から消えていないか。
    - 確かめ方：報告の直後に、根拠を出させる依頼を出す（雛形はこの節の末尾にある）。出てきたコマンドを自分で実行して突き合わせる。説明と事実が食い違うときは、実行や grep や git で見た事実を正とする。見方は <!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end --> にある。
    - 手段が依頼の一言にとどまっているなら、段を上げる。選び方は <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end -->、書いた本人に確かめさせない分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end --> にある。
3. **預けすぎる**（人の側）：報告を確かめないまま受け取る習慣が、症状を通している。
    - 見るもの：最後に自分の目か自分の手で結果を確かめたのはいつか。誰も見ていない実行の結果を、終了コードや要約だけで受け取っていないか。
    - 確かめ方：直近の完了の報告のうち、元の出力や差分まで見たものを数える。ほとんどなければ、確かめる手間を下げる工夫が先に要る。手元に残す判断は <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end -->、無人の実行は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->無人実行の結果を確かめる › 終了コードと要約だけで決めない（準備中）<!-- link:end --> にある。

根拠を出させる依頼の雛形を、次に置く。報告の直後の、同じセッションで使う。

<!-- gen:begin snippet claims-done-but-isnt/ask-for-basis -->
<!-- textlint-disable -->

??? example "雛形：完了の報告の根拠を出させる依頼"

    ```text
    さっきの「完了」の報告について、根拠を出して。答えるのは次の 3 点だけで、説明や言い訳は要らない。

    1. 実際に実行したコマンドを、そのまま 1 行ずつ書く。
    2. それぞれの出力の末尾を、そのまま貼る。通った件数と全体の件数がある場合は、両方を書く。
    3. 最初の計画に入っていたが、実行しなかった確認があれば、その一覧を書く。なければ「なし」と書く。

    実行していないものを実行したことにしない。出力が手元になければ、「出力は残っていない」と書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.139。

<!-- textlint-enable -->
<!-- gen:end snippet claims-done-but-isnt/ask-for-basis -->

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持ち、対処の本体は書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [「完了」を定義して渡す](../verify/define-done.md) |
| 確かめていない | [報告ではなく証拠を求める](../verify/evidence-not-reports.md)<br>[検証の階段](../verify/verification-ladder.md)<br>[書いた本人ではない者にレビューさせる](../verify/independent-review.md) |
| 預けすぎる | [判断を預けすぎる（過度依存） › 確かめる手間を下げる](../judgment/over-reliance.md#cheap-verification)<br>無人実行の結果を確かめる（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 似た症状との見分け {#lookalikes}

報告が外れる症状は、「完了」の言い方以外にも出る。次のように見分ける。

- テストが書き換えられたり、特例の分岐で通されたりしている：<!-- link:begin rewrote-tests-to-pass#diagnosis -->[テストを書き換えて通した › 原因を安く確かめる順](rewrote-tests-to-pass.md#diagnosis)<!-- link:end --> で、書き換えられる状態だったかを切り分ける。
- 手元の評価は良いのに本番で通用しない：<!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](misses-broken-evaluation.md#diagnosis)<!-- link:end --> で、評価の仕組みそのものを確かめる。
- 「直った」と言うが症状を隠しただけだった：<!-- link:begin fix-a-bug#no-symptom-patches -->[バグを直す › 症状を隠す修正を認めない](../recipes/fix-a-bug.md#no-symptom-patches)<!-- link:end --> で、再現と「直った」の定義から直す。
- 環境や道具が壊れたと言い出す：<!-- link:begin blames-the-tools#diagnosis -->[環境や道具が壊れたと言い出す › 原因を安く確かめる順](blames-the-tools.md#diagnosis)<!-- link:end --> で、本当に壊れたのかを確かめる。
- どの原因から疑うか迷う：<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> が、Claude 側の 6 つの原因を安く確かめる順に並べている。

## 判断例 {#example}

!!! example "判断例：「全部通った」の報告が信用できない"
    - **状況**：Claude に不具合の修正を任せたら「全テスト通過、修正済み」と報告された。手元で実行すると、2 件が落ちる。
    - **迷う候補**：A は、「完了の前に全テストを実行して」と依頼に書き足して、同じ流れでもう一度やらせる。B は、合否を返すテストのコマンドと、変えてはならないものを完了の定義として渡し、報告に実行結果を付けさせる。
    - **選んだもの**：B。さらに、同じ症状が続くなら、テストを実行する役を書いた本人から別のセッションに移す。
    - **理由**：A は、合否を返す手段そのものを渡していないので、書き足した一言だけでは同じ「終わったように見える」報告が出やすい。B は、落ちたことを Claude 自身が見える形にして、実行結果と報告を突き合わせられる。症状が続くのは、推論を引きずった同じセッションが確かめているからかもしれない。その場合は、見ていない者に確かめさせる。

## 予防：仕組みに移す {#prevention}

予防の考え方は、「確かめて」と頼み続けるのをやめ、確かめる手段を仕組みに置くことである。任せる幅を広げるほど、先に確かめる手段を整える。

- 依頼に完了の定義を書く。どのコマンドがどう返れば終わりか、止まって報告する条件は何かを決める。書き方は <!-- link:begin define-done#stop-and-report -->[「完了」を定義して渡す › 止まって報告する条件](../verify/define-done.md#stop-and-report)<!-- link:end --> にある。
- 報告は、実行したコマンドと生の出力と分母を付けた証拠で受け取る。形は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end --> にある。
- 実装の前に、落ちるテストを用意させる。<!-- link:begin tests-first#steps -->テストを先に書かせる › 手順（準備中）<!-- link:end --> の手順で、後追いのテストが今の挙動をそのまま正解にするのを防ぐ。
- 画面を持つ成果物は、人が使うのと同じ操作で確かめさせる。<!-- link:begin visual-checks#as-a-user -->画面で確かめる（ブラウザ・スクリーンショット・/verify） › 人のユーザーとして確かめさせる（準備中）<!-- link:end --> を使う。
- 席を外す実行には、2 つの仕組みがある。`/goal` は、完了の条件を別のモデルが毎ターン判定する。判定役が読むのは会話に出た証拠だけなので、証拠を会話に出させる条件を書く（<!-- link:begin goal-until-done#evaluator-reads-conversation -->[/goal（完了するまで続けさせる） › 判定役は会話しか読まない](../delegate/goal-until-done.md#evaluator-reads-conversation)<!-- link:end -->）。判定はモデルが行うので、強制ではない。Stop フックは、確かめる処理が通るまでターンを終わらせない。決まったコマンドの結果で止めるフックは強制になる。ただし、続けて止められる回数には上限がある（<!-- link:begin stop-hooks#block-cap -->Stop フックで「終わらせない」 › 続けて止められる回数の上限（準備中）<!-- link:end -->）。使い分けは <!-- link:begin stop-hooks#vs-goal -->Stop フックで「終わらせない」 › /goal との使い分け（準備中）<!-- link:end --> にある。
- 「最後に double-check して」と書き足す助言は、新しいモデルでは消してよいものがあり、ほかのモデルでは今も効く。どちらに当たるかと、自分の設定に残っていないかを、<!-- link:begin outdated-advice-ledger#add-double-check -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#add-double-check)<!-- link:end --> で確かめる。確かめる手段を渡すほうが、一言の書き足しより確実に効く。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Claude fabricates test results - reports ALL PASSED when tests are FAILING（Issue #46940）](https://github.com/anthropics/claude-code/issues/46940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Claude Code fabricated test results and pushed untested code to main branch (Opus 4.8 @ Effort = High)（Issue #64286）](https://github.com/anthropics/claude-code/issues/64286)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [AI Agents in Data Science Competitions: Lessons from the Leaderboard](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)：DrivenData・英語・確認日 2026-11-04
- [The AI Lied to Me — And That’s When I Learned How to Use It](https://engineering.mercari.com/en/blog/entry/20251028-the-ai-lied-to-me-and-thats-when-i-learned-how-to-use-it/)：Mercari Engineering・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)

**次に読む**

- [「完了」を定義して渡す](../verify/define-done.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [検証の階段](../verify/verification-ladder.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- 無人実行の結果を確かめる（準備中）

**関連**

- テストを先に書かせる（準備中）
- [バグを直す › 症状を隠す修正を認めない](../recipes/fix-a-bug.md#no-symptom-patches)
- 画面で確かめる（ブラウザ・スクリーンショット・/verify）（準備中）
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- Stop フックで「終わらせない」（準備中）
- [テストを書き換えて通した](rewrote-tests-to-pass.md)
- [手元の評価は良いのに本番で通用しない](misses-broken-evaluation.md)
- [環境や道具が壊れたと言い出す](blames-the-tools.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
