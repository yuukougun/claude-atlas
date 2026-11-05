---
id: diffs-humans-must-read
title: 人間が読むべき差分の箇所
aliases: [差分レビューの優先順位, 赤信号の差分, diff の読み方]
type: concept
field: verify
chapter: レビューで確かめる
order: 130
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 差分を全部は読めないとき、人が必ず読む箇所（テストと採点の変更・特例の分岐・例外の握りつぶし・件数の変化など）を見分けられる。
signs:
  - {type: situation, text: 差分が大きすぎて、全部は読めない}
  - {type: situation, text: 自分の目で全部レビューする時間がない}
  - {type: goal, text: 人が必ず目を通すべき変更を見分けたい}
prerequisites: [evidence-not-reports]
related: [independent-review, protect-tests, suspect-too-good-results, own-generated-code, reward-hacking, review-bottlenecks, grow-review-checklists, risk-tiered-approval, create-and-review-prs, working-with-git]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜ赤信号を先に決めておくのか, anchor: why}
  - {title: 赤信号の一覧, anchor: red-flags}
  - {title: 要の処理と周辺の読み分け, anchor: core-vs-periphery}
  - {title: 何に効くか, anchor: what-it-helps}
  - {title: 誤解しやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：差分を全部は読めないとき、人が必ず読む箇所（テストと採点の変更・特例の分岐・例外の握りつぶし・件数の変化など）を見分けられる。
    - **いつ引くか**：差分が大きすぎて全部は読めないとき。自分の目で全部レビューする時間がなく、人が必ず目を通す変更を見分けたいとき。
    - **前提**：<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](evidence-not-reports.md)<!-- link:end -->

<!-- textlint-disable -->
別名：差分レビューの優先順位・赤信号の差分・diff の読み方
<!-- textlint-enable -->

人間が読むべき差分の箇所とは、Claude が出した差分のうち、読む濃さを下げてはいけない箇所のことである。差分を全部は読めなくても、正しさを判定する側を変える変更と、失敗を見えなくする変更だけは、人が自分の目で読む。この箇所を先に決めておけば、読む量を減らしても、確かめる力を落とさずにすむ。

## 何が起きるか {#what-happens}

失敗しているテストを直すよう Claude に頼み、40 ファイルの差分と「テストは全部通過した」という報告が返ってきた場面を考える。差分を全部読む時間はない。報告を信じて受け取ると、次のような変更が紛れていても気づけない。

```diff
--- a/tests/test_price.py
+++ b/tests/test_price.py
-    assert calc_total(items) == 1280
+    assert calc_total(items) >= 0
--- a/src/price.py
+++ b/src/price.py
+    if items == KNOWN_FAILING_CASE:
+        return 1280
+    try:
+        return _calc(items)
+    except Exception:
+        pass
```

この差分は説明のために作った例で、実際の記録ではない。テストの期待値が緩み、失敗した入力だけを別扱いする分岐が入り、例外が握りつぶされている。テストは通るが、実装は直っていない。

40 ファイルのうち、この例の変更は数行にすぎない。量の多い差分ほど、判定する側の小さな変更は埋もれる。件数が変わっても「全部通過」と返ってくる例は <!-- link:begin evidence-not-reports#what-happens -->[報告ではなく証拠を求める › 件数が変わっても「全部通過」と返ってくる](evidence-not-reports.md#what-happens)<!-- link:end --> にある。

## なぜ赤信号を先に決めておくのか {#why}

赤信号を先に決める理由は、Claude 側の原因と人の側の落とし穴が重なるからである。

- **Claude 側の原因は「確かめていない」**：「通った」という報告は、通すために何が変わったかを教えない。採点の仕組みに抜け道があると、目的ではなく採点を満たす方向に解かれることがある。仕組みは <!-- link:begin reward-hacking#why -->[採点器を騙す（reward hacking） › なぜそうなるか](../basics/reward-hacking.md#why)<!-- link:end --> にある。
- **人の側の落とし穴は「預けすぎる」**：AI で変更が増えると、レビューは人に積もって詰まる。詰まる場所は <!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](../team/review-bottlenecks.md#where-it-clogs)<!-- link:end --> にある。全部を同じ濃さで読もうとすると、疲れて浅く読み、本当に危ない箇所を流してしまう。

そこで、読む濃さに差をつける。濃く読む箇所の共通点は 2 つに絞れる。

- 正しさを判定する側を変える変更（テスト・評価・採点・閾値）。
- 失敗を見えなくする変更（握りつぶし・特例・件数の変化）。

この 2 つは、通ったという報告を、中身のないものにする。だから量に関わらず人が読む。

## 赤信号の一覧 {#red-flags}

赤信号とは、差分の中で、人が必ず目を通す箇所の型のことである。実践者の一覧をまとめると、次の 6 つになる（根拠：中）。

| 赤信号 | 差分で見ること | 読む理由 |
| --- | --- | --- |
| テスト・評価ファイル・スコアラーの変更 | 期待値の緩和、`assert` の削除、skip の追加、採点の関数の書き換え | 判定する側が変わると、通過が意味を失う |
| 既知のケースへの特例の分岐 | テストの入力や期待値の値が、実装の中に出てくる。特定の入力だけの `if` | 一般の解ではなく、テストに合わせた答えになる |
| 閾値や指標名の変更 | 合格ラインを下げる、指標の名前や計算を変える | 悪い結果が良く見える |
| 例外の握りつぶし | `try/except: pass`、失敗を成功として返す書き方 | 失敗が報告から消える |
| データ件数の変化 | 行の除外、フィルタの追加、テストケースの減少 | 分母が変わると、割合や通過の意味が変わる |
| seed の固定 | 乱数の seed を固定して通す変更 | たまたまの好結果を、確かな結果と取り違える |

分母が変わる点は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> に、良すぎる結果の疑い方は <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](suspect-too-good-results.md#what-to-suspect)<!-- link:end --> にある。テストを書き換えさせない守りは <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](protect-tests.md#layers)<!-- link:end --> にある。

この一覧のほかに、機密と指定したパスと CI のワークフローのファイルは、変更の中身にかかわらず常に人が見る。段の分け方は <!-- link:begin risk-tiered-approval#always-human -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 段を決めるのは中身、常に人が見る場所](../team/risk-tiered-approval.md#always-human)<!-- link:end --> にある。

差分を開く前に使える点検表を、次に置く。

<!-- gen:begin snippet diffs-humans-must-read/red-flag-checklist -->
<!-- textlint-disable -->

??? example "雛形：差分の赤信号の点検表"

    ```markdown
    ## 差分の赤信号の点検表

    差分を開く前に、変更したファイルの一覧と統計を見て、次の各項目に当たる箇所を探す。当たった箇所は、人が自分の目で全部読む。

    - [ ] テスト・評価ファイル・採点の処理が変わっていないか（期待値の緩和、assert の削除、skip や xfail の追加）
    - [ ] 既知の入力だけを別扱いする分岐が入っていないか（テストの入力や期待値の値が、実装の中に出てこないか）
    - [ ] 閾値・合格ライン・指標の名前や計算が変わっていないか
    - [ ] 例外の握りつぶしが入っていないか（`try/except: pass`、失敗を成功として返す書き方）
    - [ ] データの件数が変わっていないか（行の除外、フィルタの追加、テストケースの減少）
    - [ ] 乱数の seed を固定して、たまたま通る形にしていないか
    - [ ] 機密に指定したパスと、CI のワークフローのファイルに触れていないか（触れていれば常に人が見る）

    当たらなかった項目も、点検した記録として残す。当たらないことは、読まなくてよい理由にならない。要の処理は、この表とは別に厳しく読む。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet diffs-humans-must-read/red-flag-checklist -->

差分が大きいときは、先に変更したファイルの一覧と統計を機械的に見て、候補を拾う。次の script は、候補を拾うだけである。何も出ないことは、赤信号がない証明にならない。

<!-- gen:begin snippet diffs-humans-must-read/scan-diff -->
<!-- textlint-disable -->

??? example "雛形：赤信号の候補を機械的に拾う確認の script"

    ```bash
    #!/bin/sh
    # 使い方: sh scan-diff.sh [基準のブランチ]   既定は main
    # 赤信号の候補を機械的に拾うだけ。判断は人が差分を読んで行う。
    base=${1:-main}

    echo "== 変更の大きさ（ファイル別）"
    git diff --stat "$base"...HEAD

    echo "== テスト・評価・採点・設定・CI に触れたファイル"
    git diff --name-only "$base"...HEAD \
      | grep -Ei '(test|spec|eval|score|grade|bench|conftest|\.github/workflows|\.claude/|config|settings)' \
      || echo "(なし)"

    echo "== 追加された行にある、赤信号の語"
    git diff -U0 "$base"...HEAD \
      | grep -E '^\+[^+]' \
      | grep -E 'except|pass$|skip|xfail|noqa|ignore|seed|threshold' \
      || echo "(なし)"
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet diffs-humans-must-read/scan-diff -->

Claude に候補を挙げさせることもできる。ただし挙げるのは候補までで、読むのは人である。

<!-- gen:begin snippet diffs-humans-must-read/list-red-flags -->
<!-- textlint-disable -->

??? example "雛形：赤信号に当たる箇所だけを挙げさせる依頼の雛形"

    ```text
    いまのブランチの差分（main との比較）を読んで、次の赤信号に当たる箇所だけを、ファイル名と行の番号で挙げてほしい。

    - テスト・評価ファイル・採点の処理の変更
    - 既知の入力だけを別扱いする分岐
    - 閾値・合格ライン・指標の名前や計算の変更
    - 例外の握りつぶし
    - データの件数の変化（行の除外、フィルタの追加、テストケースの減少）
    - 乱数の seed の固定

    守ること:
    - ファイルは直さない。挙げるだけにする
    - 各箇所に、なぜ赤信号に当たるかを 1 行で添える
    - 当たるものがない項目は「なし」と書く。無理に探さない
    - 差分の全部を読めたかどうかを最後に書く。読めなかったファイルの名前も挙げる
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet diffs-humans-must-read/list-red-flags -->

## 要の処理と周辺の読み分け {#core-vs-periphery}

要の処理と周辺の読み分けとは、赤信号を拾った後の残りの差分を、壊れたときの被害の大きさで読み分けることである。実践者の経験則は、要となる処理は厳しく読み、周辺は緩く読む、というものである（根拠：弱）。

- **要の処理**：壊れたときの被害が大きく、後から気づきにくい処理。課金・認可・データの削除や移行などがこれに当たる。
- **周辺**：文言・ログ・内部の補助のように、壊れても影響が小さく、すぐ気づける処理。

リスクの段の分け方と承認の数は <!-- link:begin risk-tiered-approval#three-tiers -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 三つの段と承認の数](../team/risk-tiered-approval.md#three-tiers)<!-- link:end --> にある。

読み分けの順は次のとおりである。

1. 赤信号に当たるファイルを拾い、全部読む。要か周辺かは問わない。
2. 要の処理は、Claude に処理の流れと入力の端を説明させ、実際の動きと照らす。自分の言葉で言い直せない所を、読み直す箇所にする。手順は <!-- link:begin own-generated-code#explain -->[生成コードを自分のものにする › 処理の流れと入力の端を説明させる](own-generated-code.md#explain)<!-- link:end --> にある。
3. 周辺は、細かく読まず、実行した結果で受ける。証拠の形は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> にある。

ここで大事なのは、赤信号が要と周辺の区別より先に来ることである。テストや設定のファイルは、製品の動きから遠い周辺に見える。しかし判定する側にあたるので、周辺として緩く読んではいけない。

!!! example "判断例：周辺に見える設定ファイルの変更"
    - **状況**：テストの修正を頼んだ差分に、課金の計算の修正と、テストの共通設定 `conftest.py` の変更が入っている。時間は 30 分しかない。
    - **迷う候補**：課金の計算を全行読んで、`conftest.py` は短いので流し読みする。または、`conftest.py` を先に全部読み、課金の計算は説明させて照合する。
    - **選んだもの**：`conftest.py` を先に全部読み、課金の計算は Claude に流れと入力の端を説明させて照合する。
    - **理由**：課金の計算は要の処理だが、説明と動きの照合で読む量を減らせる。`conftest.py` は共通設定で、全テストの前提を変えるため、数行でも読み飛ばせない。

差分そのものを小さく区切れば、全部読める量に近づく。区切り方は <!-- link:begin working-with-git#granularity -->[git との付き合い方 › どこで区切るか](../cli/working-with-git.md#granularity)<!-- link:end --> にある。流す量の合わせ方は、<!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](../team/review-bottlenecks.md#match-review-capacity)<!-- link:end --> が持つ。

## 何に効くか {#what-it-helps}

この読み方が関わる原理は「確かめる」と「握る」である。Claude 側の原因では「確かめていない」に、人の側の落とし穴では「預けすぎる」に効く。

- **原理「確かめる」**：通ったという報告を、差分の中の判定する側と失敗を隠す箇所に照らす。報告ではなく証拠を求める考え方と組み合わせる。
- **原理「握る」**：全部を預けず、読む箇所だけは人が握る。読む箇所の一覧は人が持ち、Claude に決めさせない。
- **原因「確かめていない」**：Claude が実装を直さずに通した変更を、人が目で拾う。
- **落とし穴「預けすぎる」**：全部を同じ濃さで読もうとして浅くなる状態を、読む濃さの差で避ける。

効かない場面もある。

- 赤信号に当たらない、ふつうのバグは拾えない。動作の確認や別の者によるレビューと組み合わせる。別の者に読ませる理由と分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](independent-review.md#who)<!-- link:end --> にある。
- 一覧は経験則で、網羅ではない。見落とした変更が見つかったら、その理由を観点に足して育てる。手順は <!-- link:begin grow-review-checklists -->[レビューの観点を育てる](../team/grow-review-checklists.md)<!-- link:end --> にある。
- AI のレビューが通ったことは、人が読んだことの代わりにならない。数え方は、<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](independent-review.md#ai-approval)<!-- link:end --> が持つ。

PR の説明に、出す前のリスクと確かめた証拠を書かせると、読む箇所の見当が付きやすい。書かせ方は <!-- link:begin create-and-review-prs#pr-description -->[PR を作り、レビューを受ける › PR の説明に書くこと](../recipes/create-and-review-prs.md#pr-description)<!-- link:end --> にある。

## 誤解しやすいこと {#misconceptions}

- **「赤信号に当たらなければ読まなくてよい」**：誤りである。赤信号は読む順番を決める一覧で、読むことを免除する一覧ではない。要の処理は、赤信号とは別に読む。
- **「テストが通ったなら、テストの変更は見なくてよい」**：誤りである。テストの変更そのものが、通った理由かもしれない。判定する側の変更は、通過の報告より先に読む。
- **「Claude に赤信号を挙げさせれば、人は読まなくてよい」**：誤りである。挙げさせるのは候補までで、挙がらなかった箇所は確かめていない箇所である。読む箇所を最後に決めるのは人である。
- **「要の処理だけ読めば足りる」**：誤りである。周辺に見えるテストや設定が、判定する側にあたる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [報告ではなく証拠を求める](evidence-not-reports.md)

**関連**

- [書いた本人ではない者にレビューさせる](independent-review.md)
- [テストを守る（改ざんを防ぐ）](protect-tests.md)
- [良すぎる結果を疑う](suspect-too-good-results.md)
- [生成コードを自分のものにする](own-generated-code.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [レビューの観点を育てる](../team/grow-review-checklists.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)
- [PR を作り、レビューを受ける](../recipes/create-and-review-prs.md)
- [git との付き合い方](../cli/working-with-git.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
