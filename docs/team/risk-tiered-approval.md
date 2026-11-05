---
id: risk-tiered-approval
title: リスク段階別の承認（AI の承認を人の承認に数えない）
nav_title: リスク段階別の承認
aliases: [リスク別の承認, 承認の段階, AI のお墨付き]
type: concept
field: team
chapter: レビューと判断
order: 60
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [チーム, 開発]
summary: 変更をリスクの段に分け、段ごとに人の承認の数を決められる。AI の承認は人の承認に数えず、危ない場所は常に人が見る。
signs:
  - {type: goal, text: AI が書いた変更の承認の仕方を、危なさで分けたい}
  - {type: situation, text: AI のレビューが通ったら、人の承認は要らないか迷っている}
  - {type: symptom, text: AI のレビューが通った PR を、人がよく見ずに承認している}
prerequisites: [independent-review, agreement-is-not-evidence]
related: [review-bottlenecks, automated-pr-review, separate-roles, protected-paths, freeze-eval-assets, diffs-humans-must-read, ai-usage-guidelines, create-and-review-prs, github-actions-with-claude]
sources: [claude-dev-blog-solving-code-review-anthropic]
volatility: 中
sections:
  - {title: 三つの段と承認の数, anchor: three-tiers}
  - {title: AI の承認を数えない, anchor: ai-approval-doesnt-count}
  - {title: 段を決めるのは中身、常に人が見る場所, anchor: always-human}
  - {title: どの原理・どの原因に関わるか, anchor: principles-and-causes}
  - {title: よくある誤解と効かない場面, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：変更をリスクの段に分け、段ごとに人の承認の数を決められる。AI の承認は人の承認に数えず、危ない場所は常に人が見る。
    - **いつ引くか**：AI が書いた変更の承認の仕方を、危なさで分けたいとき。AI のレビューが通った PR を、人がよく見ずに承認しているとき。
    - **前提**：<!-- link:begin independent-review -->[書いた本人ではない者にレビューさせる](../verify/independent-review.md)<!-- link:end -->・<!-- link:begin agreement-is-not-evidence -->[同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)<!-- link:end -->

<!-- textlint-disable -->
別名：リスク別の承認・承認の段階・AI のお墨付き
<!-- textlint-enable -->

リスク段階別の承認は、変更をリスクの段に分け、段ごとに人の承認の数を変える運用である。AI が変更を書く量が増えると、全部の PR に同じ重さの承認を求める運用は詰まり、全部を AI のレビューに任せる運用は人の責任が消える。このページは、その間の置き方と、AI の承認を人の承認に数えない決まりを扱う。

## 三つの段と承認の数 {#three-tiers}

Claude Code チームのレビュー運用を述べた記事（2026-10-15）は、変更を 3 段に分けている（根拠：中。企業の一次の報告で、書いたのは運用している側）。段ごとに、人の承認の数が違う。

- **低**：文書・文言・社内だけの機能・フラグの裏の追加。AI のレビューとセキュリティの確認（記事の言う自動の確認。中身はこのページでは定義しない）が通れば、人の承認は要らない。
- **中**：ふつうの製品の変更と、キャッシュ・自動更新・システムプロンプトなど敏感な所。人の承認は 1 人。
- **高**：最も危ない所と、常に 2 人が要るパス。人の承認は 2 人。

低の段で人の承認を省けるのは、作者がリポジトリの信頼済みの一覧にいる場合だけである。一覧は主に、持ち主のチームの人である。一覧の外の人の変更は、低の段でも人が見る。

この段の中身は、ある 1 つのチームの運用である。読者のチームの規則として写すものではない。変更の種類・レビューできる人数・壊れたときの被害は、チームごとに違う。写すのは「段に分ける」「段ごとに人の数を決める」「AI の承認を数えない」という形だけにする。

自分のチームで書くときの表の雛形は、次のとおりである。段の中身と人の数は、置き換えて使う。

<!-- gen:begin snippet risk-tiered-approval/tier-table -->
<!-- textlint-disable -->

??? example "雛形：リスクの段と承認者の表（例）"

    ```markdown
    | 段 | 入れる変更（自分のチームの例に置き換える） | 人の承認 | 先に通すもの | 承認する人 |
    | --- | --- | --- | --- | --- |
    | 低 | 文書・文言の修正、社内だけの機能、フラグの裏の追加 | 0 人 | AI のレビューとセキュリティの確認 | なし（信頼済みの作者の一覧にいる人が出した変更に限る） |
    | 中 | ふつうの製品の変更、キャッシュ・自動更新・システムプロンプトなど敏感な所 | 1 人 | AI のレビューとセキュリティの確認 | コードの持ち主のチームの人 |
    | 高 | 最も危ない所、常に 2 人が要ると決めたパス | 2 人 | AI のレビューとセキュリティの確認 | 持ち主のチームの人と、その領域を評価する担当 |
    | 段によらず | 機密と指定したパス、CI のワークフローのファイル | 段を問わず人が見る | 同上 | 持ち主のチームの人 |

    AI の承認は、どの行でも人の承認の数に入れない。段は作者ではなく変更の中身で決める。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet risk-tiered-approval/tier-table -->

表を決めたら、直近の PR を 10 件ほど当てはめる。段の境目で迷う PR が出たら、境目の例を表に書き足す。迷う変更は上の段に倒す（推論・実践例なし）。

承認の数を実際に強制できるかは、使っているコードのホスティングの機能で確かめる（未確認）。決まりを書いただけでは、守られるかどうかはお願いにとどまる。守らせたいものを設定で縛る考え方は <!-- link:begin ai-usage-guidelines#lock-the-prohibitions -->[社内ガイドラインに書くこと › 禁止は設定で縛る](ai-usage-guidelines.md#lock-the-prohibitions)<!-- link:end --> が持つ。

## AI の承認を数えない {#ai-approval-doesnt-count}

AI の承認を人の承認に数えない決まりは、このページが持つ。記事の原文は次の 1 文である。

> An agent's approval never counts as a person's, either.

AI のレビューは、低の段の変更を通す関門にはなる。しかし、中と高の段の人の枠は埋められない。AI のレビューが通ったことと、人が承認したことは、別の記録として残す。

AI の承認が人の承認の代わりにならない理由は、2 つのページが持つ。1 つ目は、変更を生んだ推論を見ていない者に見せる分け方で、次のページにある。<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end --> にある。2 つ目は、AI レビュアーが複数一致しても正しさの証拠にならない理由で、次のページにある。<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end --> にある。

記事は、人が持つものとして、作るかどうかの判断・危ない所のレビュー・設計のレビュー・証拠を読むこと・結果に責任を持つことを挙げている。承認は、このうち結果への責任を引き受ける行為に当たる。責任を持つ人が、証拠を読んで通すから、承認に意味がある。

AI のレビューが通った PR を、人がよく見ずに承認している状態は、人の承認が AI の承認の追認になっている形である。この形では、人の承認の数が増えても、確かめる回数は増えない。防ぐには、承認のコメントに、自分が読んだ箇所と確かめたことを 1 行書く（推論・実践例なし）。「AI も問題なしと言っている」は、書いてよい根拠に入れない。

AI のレビューの扱いについて、記事は次の運用を挙げている（根拠：中）。

- どの PR にも Claude のレビューが付き、指摘は別のエージェントが確かめてから出される。
- 指摘には必ず答える。
- セキュリティの指摘は、解決するまでマージを止める。

PR ごとに AI のレビューを自動で付ける機能の使い方は <!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）（準備中）<!-- link:end --> が持つ。PR を作る側が出す前にリスクと確かめた証拠を書く手順は <!-- link:begin create-and-review-prs#risks-before-submitting -->[PR を作り、レビューを受ける › 出す前にリスクを挙げさせる](../recipes/create-and-review-prs.md#risks-before-submitting)<!-- link:end --> にある。

!!! example "判断例：高の段の変更で、承認できる人が足りない"
    - **状況**：高の段と決めたパスを変更する PR がある。高の段は人の承認が 2 人要る。承認できる人は 1 人だけで、AI のレビューは 2 回通っている。
    - **迷う候補**：AI のレビュー 2 回を 2 人目の承認として数えて通す。もう 1 人の承認者が空くまで待つ。
    - **選んだもの**：もう 1 人の承認者が空くまで待つ。
    - **理由**：AI のレビューは、同じ聞き方・同じ文脈なら似た答えが返りやすく、2 回通ったことは人の承認の代わりにならない。待つ間に、PR の説明を読み直して、リスクと確かめた証拠が足りているかを直せる。

## 段を決めるのは中身、常に人が見る場所 {#always-human}

段は、作者や PR の題ではなく、変更の中身で決める。Claude Code チームのレビュー運用の記事（2026-10-15）では、分類器が変更の中身を見て段を決めている。分類器がないチームは、パスと変更の種類の規則で決めることになる。

段によらず、常に人の目を通す場所がある。同じ記事は、機密と指定されたパスと、CI のワークフローのファイルを挙げている。低の段に見える変更でも、これらは人が見る。

人が必ず読む箇所の見分け方は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](../verify/diffs-humans-must-read.md#red-flags)<!-- link:end --> が持つ。要の処理と周辺の読み分けは <!-- link:begin diffs-humans-must-read#core-vs-periphery -->[人間が読むべき差分の箇所 › 要の処理と周辺の読み分け](../verify/diffs-humans-must-read.md#core-vs-periphery)<!-- link:end --> にある。

常に人が見る場所は、Claude 自身が書き換えられないようにする守りと、組にして使う。どの権限モードでも確認なしには書かせない場所は <!-- link:begin protected-paths#protected -->[消せない場所・触れない場所（protected paths） › 保護される場所と、モードごとの扱い](../enforce/protected-paths.md#protected)<!-- link:end --> が持つ。テストや採点のスクリプトを書き換えさせない設定は <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](../enforce/freeze-eval-assets.md#how-to-freeze)<!-- link:end --> にある。承認の段を決めても、書き換えを止める鍵がなければ、承認の前に書き換わる場所が残る。

低の段の軽い扱いは、任せる幅を広げる決めである。広げる前に、守りが先にそろっている必要がある。守りとは、AI のレビューとセキュリティの確認が通ること、作者が信頼済みの一覧にいること、常に人が見る場所を段の外に置くことである。外の人が出した issue や PR を Claude に読ませる場合の注意は <!-- link:begin github-actions-with-claude#untrusted-input -->[GitHub Actions と @claude › 外の人が書いた issue と PR](../delegate/github-actions-with-claude.md#untrusted-input)<!-- link:end --> が持つ。

!!! example "判断例：文書の修正に見える PR へ CI の設定が混じっている"
    - **状況**：PR の題は「README の文言を直す」で、AI のレビューもセキュリティの確認も通っている。差分を見ると、CI のワークフローのファイルも書き換えている。
    - **迷う候補**：題と大半が文書なので、低の段として人の承認なしで通す。CI のワークフローが入っているので、人が見る。
    - **選んだもの**：人が見る。
    - **理由**：段は題ではなく中身で決める。CI のワークフローのファイルは、記事のチームでも常に人が見る場所に入っている。文書の修正と混ざっていても、その部分を人が読む。

## どの原理・どの原因に関わるか {#principles-and-causes}

このページが関わる原理は**確かめる**と**握る**である。Claude 側の原因は**確かめていない**、人の側の落とし穴は**同意を根拠にする**である。

- **確かめる**：段は、確かめる強さを変える仕組みである。低の段は AI の確認を関門にし、中と高の段は人の目を足す。確かめる手を段ごとに決めておけば、全部の PR を同じ重さで見て疲れることも、全部を軽く見て危ない変更を通すことも減らせる。
- **握る**：危ない場所の承認と、結果への責任は、人が握る。承認の数を人の数で決めるのは、この握る範囲を数に直したものである。握る判断を役割に分ける方法は <!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](separate-roles.md#against-sycophancy)<!-- link:end --> が持つ。
- **確かめていない**：AI の書いた変更を、誰にも確かめられないまま通す形を防ぐ。AI は「問題ない」と言えても、確かめたとは限らない。人の承認の数を決めておくと、確かめる人の最低の人数を、変更を出す前に決められる。
- **同意を根拠にする**：「AI も賛成した」を、人の承認の根拠に使う形を防ぐ。同意が根拠にならない理由と、代わりに数える証拠は <!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end --> が持つ。

人の承認は、全部の PR に求めるとレビューに積もる。流す量をレビューできる量に合わせる考え方は <!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](review-bottlenecks.md#match-review-capacity)<!-- link:end --> が持つ。段に分けると、人の承認を危ない所に集められる。

## よくある誤解と効かない場面 {#misconceptions}

- **「AI のレビューが通れば、人の承認は要らない」**：要らないのは、低の段の変更のうち、作者が信頼済みの一覧にいてセキュリティの確認も通ったものだけである。中と高の段では、AI のレビューは人の枠を埋めない。
- **「この段の中身をそのまま使えばよい」**：段の中身は、ある 1 つのチームの運用である。自分のチームの変更の種類と、承認できる人数に合わせて決め直す。
- **「作者が段を決める」**：段を決めるのは、作者の申告ではなく変更の中身である。作者が信頼済みかどうかは、低の段の軽い扱いを使えるかどうかを決めるだけである。
- **「この運用で品質が上がると分かっている」**：記事は、2026 年 6〜9 月に Claude Code のリポジトリへの merged PR が 2 倍を超え、revert の割合が 40% 超減ったと報告している。revert の数え方と元の値は書かれていない（根拠：弱。運用している側の自己申告で、因果は示されていない）。他のチームで同じ結果が出る保証にはならない。
- **「段を決めたら、あとは自動で回る」**：記事は、一晩で 50 回を超えるレビューと修正を繰り返した PR があったこと、数値が動いたときに承認を締める仕組みはまだないこと、やり方が今も変わっていることを注意として挙げている。段と人の数は、決めて終わりにせず、見直す日を決めておく。

AI の承認の扱いは、チームの AI 利用の決まりに、レビューの責任として書く。書く項目は <!-- link:begin ai-usage-guidelines#what-to-write -->[社内ガイドラインに書くこと › 書くこと（データの区分・面とモード・レビューの責任）](ai-usage-guidelines.md#what-to-write)<!-- link:end --> が持つ。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)：Anthropic（claude.dev Blog）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)

**関連**

- [レビューのボトルネックと疲労](review-bottlenecks.md)
- 自動 PR レビュー（Code Review・/ultrareview）（準備中）
- [役割を分ける（書く人・承認する人・疑う人）](separate-roles.md)
- [消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md)
- [評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)
- [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)
- [社内ガイドラインに書くこと](ai-usage-guidelines.md)
- [PR を作り、レビューを受ける](../recipes/create-and-review-prs.md)
- [GitHub Actions と @claude](../delegate/github-actions-with-claude.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
