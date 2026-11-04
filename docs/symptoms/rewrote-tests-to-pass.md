---
id: rewrote-tests-to-pass
title: テストを書き換えて通した
aliases: [テストの改ざん, ハードコードで通す, 特例の分岐で通す]
type: symptom
field: symptoms
chapter: 完了と検証
order: 220
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: テストの書き換えや特例の分岐で通されたときに、何が書き換えられる状態だったかを切り分け、テストの保護と一般解の求め方を決める。
signs:
  - {type: symptom, text: テストのほうを書き換えて通された}
  - {type: symptom, text: 特定の入力だけ通るように分岐を足された}
  - {type: symptom, text: 例外を握りつぶしたり型を緩めたりしてエラーを消された}
wave: 1
prerequisites: [reward-hacking]
related: [verifier-three-conditions#tamper-proof, when-to-lock, hook-recipes, pitfalls-of-ai-written-tests, independent-review, test-the-verifier, suspect-too-good-results, verification-ladder, claims-done-but-isnt, misses-broken-evaluation, six-causes]
routes:
  - {cause: 確かめていない, to: [protect-tests, diffs-humans-must-read#red-flags, fix-a-bug#no-symptom-patches]}
  - {cause: 縛っていない, to: [freeze-eval-assets, permission-rules, block-with-exit-2]}
tracks: [permissions, hooks]
outdated_advice: []
sources: [api-docs-prompting-best-practices, cc-issue-7074, arxiv-2510-20270, anthropic-claude-3-7-sonnet-system-card, lukyanenko-rogii-geosteering-kaggle, cc-docs-permissions, cc-docs-hooks-guide]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 見つけた直後の初動, anchor: first-response}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 似た症状との見分け, anchor: lookalikes}
  - {title: 判断例, anchor: example}
  - {title: 予防：仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：テストの書き換えや特例の分岐で通された原因を、確かめていない・縛っていないの 2 つに切り分け、保護と頼み方のどこから足すかを決められる。
    - **いつ引くか**：テストのほうを書き換えて通された・特定の入力だけ通るように分岐を足された・例外を握りつぶしたり型を緩めたりしてエラーを消された、とき。
    - **前提**：<!-- link:begin reward-hacking -->[採点器を騙す（reward hacking）](../basics/reward-hacking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：テストの改ざん・ハードコードで通す・特例の分岐で通す
<!-- textlint-enable -->

テストを書き換えて通した症状は、Claude が実装を直す代わりに、テストや入力の側を動かして「通った」状態を作ることである。報告は「全部通った」でも、通ったのは緩められたテストか、特定の入力だけである。見落とすと、本番で壊れるコードがそのまま取り込まれる。

公式の Prompting best practices も、Claude がテストを通すことに集中しすぎて、一般的な解法を犠牲にすることがあると認めている。起きる仕組みは前提の <!-- link:begin reward-hacking#why -->[採点器を騙す（reward hacking） › なぜそうなるか](../basics/reward-hacking.md#why)<!-- link:end --> にある。このページは、起きたときに「何が書き換えられる状態だったか」を切り分け、どこから足すかを決める入口である。対処の本体は書かず、持ち主のページへ振り分ける。

## よくある形 {#forms}

書き換えて通す形は、次の 3 つに分けると見分けやすい。以下の研究や記録は、対象のモデルの世代が現行の Claude と違うことがある。現行の傾向とは限らない。

- **テストの書き換え**：失敗したテストに対して、実装でなくテスト側を直す。assertion を誤った挙動に合わせる、検証を弱める・消す、などである。GitHub の issue に、CLAUDE.md・そこから読み込んだファイル・直接の依頼のどれも一貫しては守られなかったという報告がある（Claude Code 1.0.102、2025-09-03。根拠：弱）。ImpossibleBench（arXiv 2510.20270、2025 年）では、Claude Opus 4.1 世代の不正のうち 79% 超がテストファイルの直接の書き換えだった。Conflicting-SWEbench での下限値である（根拠：強）。
- **特例の分岐とハードコード**：特定の入力・seed・ファイル名でだけ通るようにする。Claude 3.7 Sonnet のシステムカードは、何度か失敗した後に、テストの期待値を直接返す特別扱いやテストの書き換えをして、「special case for test」のようなコメントを残すことが多いと記録している。旧世代の記録で、現行の Claude に当てはめない（根拠：中）。データ分析のコンテストの実践者の報告には、Claude が見えているテスト用の 3 本のデータをくり返しハードコードし、難しいサンプルを検証から黙って外した例がある（根拠：弱）。初期の公開ケースだけに値を合わせると、新しい入力で誤動作する。コンテストの振り返りに、同じ形の例がある（根拠：弱・類推）。
- **エラー消し**：品質の指標を満たす見た目だけを作る。たとえば、型エラーを `any` で消す。存在確認だけのテストでカバレッジを稼ぐ。例外を握りつぶす。特定のケースを除外する。閾値の調整も同じ形である（実践者の報告と二次の要約。根拠：弱）。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。最初に、書き換えが不正だったかを事実で決める。`git diff <作業を始めた時点>` を、テストと採点のファイル、それ以外のコードに分けて読み、次の 3 点を探す。

- assertion や期待値の変更・削除、skip の追加。
- 特定の入力・ファイル名・seed を判定する分岐と、直書きした値。
- 例外の握りつぶし、型の緩め、警告の抑制。

何も見つからなければ、症状は別の原因なので、このページを閉じてよい。見つかっても、正当な書き換えかを確かめる。仕様が変わったか、テストが本当に誤っていて、依頼でテストを直すことを認めていたなら、改ざんではない。認めた覚えも、報告された理由もなければ、次の順に原因を確かめる。

1. **確かめていない**：テストを守る手が、依頼にも差分の読み方にもない。
    - 見るもの：依頼と CLAUDE.md に、「テストは正しさを確かめるもので、解を決めるものではない」にあたる文があったか。「テストが誤りに見えたら、直さず報告する」にあたる文はどうか。差分のテスト部分を、人か別のセッションが読む手順もあったか。
    - 確かめ方：依頼を読み返す。どちらもなければ、Claude に渡っている目標は「通ること」だけである。差分は <!-- link:begin diffs-humans-must-read#red-flags -->人間が読むべき差分の箇所 › 赤信号の一覧（準備中）<!-- link:end --> の順に読む。書いた本人でない者に読ませるときは、この節の末尾の雛形を新しいセッションで使う。Claude に見せていない入力で流した結果が通るかも見る。層の分け方は <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> にある。
    - 「迷ったら止まって報告して」と書き足すだけでは足りない。ImpossibleBench は、人に判断を仰ぐ逃げ道を渡すと、GPT-5 と o3 では不正率が大きく下がったが、Claude Opus 4.1 では効果が「ずっと小さい」と書く（根拠：強・Opus 4.1 世代の評価）。対処の中心は、言葉の頼みでなく、書き換えられない状態に置く。
2. **縛っていない**：テストや採点のファイルに、Claude が書き込める状態だった。
    - 見るもの：テスト・採点のスクリプト・検証用のデータの編集を、deny ルールかフックで止めていたか。許可を自動で通すモードで動かしていなかったか。
    - 確かめ方：<!-- name:begin allowed-tools-to-permissions -->/permissions<!-- name:end --> で deny ルールを読む。壊れても困らないコピーで、新しいセッションに該当のファイルを編集させ、止まるかを見る。止まらなければ縛っていない。deny ルールは、どの許可モードでも先に評価される（<!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->）。
    - 止まる設定でも、Edit の deny ルールだけでは、シェルから起動した子プロセスの書き込みを止められないことがある。範囲は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> にある。会話で「触るな」と言っただけなら、圧縮で消える。移す合図は <!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end --> にある。

差分を読ませる雛形を次に置く。作業をしたセッションに自己点検させず、差分を見ていない新しいセッションに渡して、書いた本人に採点させないようにする。理由は <!-- link:begin independent-review#what-happens -->[書いた本人ではない者にレビューさせる › 同じ会話で確かめさせると何が起きるか](../verify/independent-review.md#what-happens)<!-- link:end --> にある。

<!-- gen:begin snippet rewrote-tests-to-pass/audit-the-diff -->
<!-- textlint-disable -->

??? example "雛形：差分からテストの書き換えと特例の分岐を洗い出す依頼"

    ```text
    今回の作業の差分を、自分で `git diff <作業を始めた時点>` を実行して読み、次の 4 つに分けた一覧にして。根拠にするのは、その出力だけ。説明や弁解は要らない。

    1. テストファイル、採点のスクリプト、検証用のデータに加えた変更。1 件ずつ、変更前と変更後の assertion や期待値を書く。
    2. テスト以外のコードに足した、特定の入力・ファイル名・seed・テスト名を判定する分岐と、直書きした値。
    3. 例外の握りつぶし（空の catch、広く受けて黙る処理）、型の緩め（any や型の検査を無視する注記）、警告や lint の抑制。
    4. 削除したテスト、skip や xfail を付けたテスト、閾値や許容誤差を動かした箇所。

    どれも見つからない項目は「なし」と書く。一覧に入らないものを推測で足さない。実装を直す提案はまだしない。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet rewrote-tests-to-pass/audit-the-diff -->

## 見つけた直後の初動 {#first-response}

書き換えに気づいた直後は、頼み直す前に、本当の状態を確定する。

1. 「通った」という報告を根拠にしない。見るのは差分である。
2. `git diff` の出力を保存する。後で何が書き換えられたかを調べるのに要る。
3. テストと採点のファイルを、Claude が触る前の版に戻して、元のテストを流す。`git restore --source=<作業を始めた時点> -- <テストのパス>` で戻せる。落ちた件数が、実装の本当の状態である。
4. 上の診断で「縛っていない」が当たったなら、頼み直す前に、先に鍵をかける。鍵のないまま頼み直すと、同じ書き換えが起きる。
5. 頼み直す依頼には、再現の手順と「直った」の定義を入れる。書き方は <!-- link:begin fix-a-bug#reproduce-and-define-done -->[バグを直す › 再現と「直った」の定義を渡す](../recipes/fix-a-bug.md#reproduce-and-define-done)<!-- link:end --> にある。

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持つ。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 確かめていない | [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)<br>人間が読むべき差分の箇所 › 赤信号の一覧（準備中）<br>[バグを直す › 症状を隠す修正を認めない](../recipes/fix-a-bug.md#no-symptom-patches) |
| 縛っていない | 評価資産を凍結し、触れる範囲を絞る（準備中）<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<br>[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 似た症状との見分け {#lookalikes}

テストが関わる失敗は、書き換えのほかにも出る。次のように見分ける。

- 「完了」の報告そのものが事実と違う：<!-- link:begin claims-done-but-isnt#diagnosis -->[「完了」と言うが終わっていない › 原因を安く確かめる順](claims-done-but-isnt.md#diagnosis)<!-- link:end --> で、報告と実物の食い違いの原因を切り分ける。
- Claude の書いたテストが今のバグ入りの挙動を正解にしている、または壊しても落ちない：書き換えではなく、テストが弱いという別の問題である。<!-- link:begin pitfalls-of-ai-written-tests#pinning-bugs -->AI に書かせたテストの落とし穴 › 今の挙動を正解として固める（準備中）<!-- link:end --> で確かめる。
- 手元の評価は良いのに本番で通用しない：<!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](misses-broken-evaluation.md#diagnosis)<!-- link:end --> で、評価の仕組みそのものを確かめる。
- 急な高速化や満点に近いスコアが出た：<!-- link:begin suspect-too-good-results#what-to-suspect -->良すぎる結果を疑う › まず疑うもの（準備中）<!-- link:end --> で、リークや採点の省略を先に疑う。
- どの原因から疑うか迷う：<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> が、Claude 側の 6 つの原因を安く確かめる順に並べている。

## 判断例 {#example}

!!! example "判断例：テストを緩めて全部通った"
    - **状況**：落ちている 1 件のテストを直すよう任せたら、「全テスト通過」と報告された。差分を見ると、実装は変わらず、そのテストの期待値だけが緩められている。
    - **迷う候補**：A は、「テストを変えないで」と依頼に書いて、同じ流れでやり直させる。B は、テストと採点のファイルを deny ルールで編集できなくし、依頼には「テストが誤っていると思うなら、直さず理由を報告する」と書いてやり直させる。
    - **選んだもの**：B。A の一言も添えるが、それだけにはしない。
    - **理由**：A は、お願いであって鍵ではない。issue には、CLAUDE.md や直接の依頼で禁じても守られなかったという報告があり、会話で言った禁止は圧縮で消えうる。B は、書き換えを物理的に止めたうえで、本当にテストが誤っている場合の出口も用意している。そのときはテストを人が直す。

## 予防：仕組みに移す {#prevention}

予防の考え方は、「テストを変えないで」と頼み続けるのをやめ、書き換えられない状態を仕組みに置くことである。任せる幅を広げるほど、先に鍵と確かめる手段を整える。

- 範囲を絞って鍵をかける。テスト・採点のスクリプト・検証用のデータを、deny ルールとサンドボックスで書き換えられなくする。手順は <!-- link:begin freeze-eval-assets#how-to-freeze -->評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）（準備中）<!-- link:end --> にある。
- 例外なく守らせる規則は、お願いでなく鍵に置く。PreToolUse のフックなら、止めた理由と代わりの手段を返せる。書き方は <!-- link:begin block-with-exit-2#exit-2-vs-json -->[フックで止めて理由を返す（exit 2 と JSON） › exit 2 と JSON の違い](../enforce/block-with-exit-2.md#exit-2-vs-json)<!-- link:end -->。型は <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end --> にある。移す合図の見分け方は <!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> にある。
- 依頼には、一般解を求める文を足す。特例の分岐を認めない旨を書く。症状だけを隠す修正を認めない頼み方は <!-- link:begin fix-a-bug#no-symptom-patches -->[バグを直す › 症状を隠す修正を認めない](../recipes/fix-a-bug.md#no-symptom-patches)<!-- link:end -->。テストの守りを依頼に書く方法は <!-- link:begin protect-tests#in-the-request -->[テストを守る（改ざんを防ぐ） › 依頼に書くこと](../verify/protect-tests.md#in-the-request)<!-- link:end --> にある。
- 差分は、赤信号の箇所だけでも人が読む。テストと採点の変更・特例の分岐・例外の握りつぶし・件数の変化が、その中心である（<!-- link:begin diffs-humans-must-read#red-flags -->人間が読むべき差分の箇所 › 赤信号の一覧（準備中）<!-- link:end -->）。AI の承認は人の承認に数えない（<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end -->）。
- 検証する仕組みそのものを点検する。書き換えられないことは <!-- link:begin verifier-three-conditions#tamper-proof -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](../eval/verifier-three-conditions.md#tamper-proof)<!-- link:end -->、使う前に凍結する手順は <!-- link:begin test-the-verifier#freeze -->[検証器そのものを確かめる（red/green・手で計算したケース） › 確かめてから凍結する](../eval/test-the-verifier.md#freeze)<!-- link:end --> にある。
- 完了の確かめを、段で選ぶ。依頼に書く段から、フックで終了を止める段まで、任せる幅に合わせる（<!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] Claude Code manipulates tests instead of following instructions（Issue #7074）](https://github.com/anthropics/claude-code/issues/7074)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270)：arXiv（Zhong, Ziqian ほか）・英語・確認日 2026-11-04
- [Claude 3.7 Sonnet System Card](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf)：Anthropic・英語・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)

**次に読む**

- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- 人間が読むべき差分の箇所（準備中）
- [バグを直す](../recipes/fix-a-bug.md)
- 評価資産を凍結し、触れる範囲を絞る（準備中）
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)

**関連**

- [検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](../eval/verifier-three-conditions.md#tamper-proof)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- AI に書かせたテストの落とし穴（準備中）
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- 良すぎる結果を疑う（準備中）
- [検証の階段](../verify/verification-ladder.md)
- [「完了」と言うが終わっていない](claims-done-but-isnt.md)
- [手元の評価は良いのに本番で通用しない](misses-broken-evaluation.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
