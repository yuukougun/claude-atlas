---
id: create-and-review-prs
title: PR を作り、レビューを受ける
aliases: [プルリクエストを作らせる, PR の説明文, pull request, コードレビューを受ける]
type: recipe
field: recipes
chapter: 作る・変える
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, 同意を根拠にする]
scenes: [開発, チーム]
summary: 変更から PR を作らせ、出す前にリスクと確かめた証拠を書き出させる。説明は自分の言葉で書けるまで読み、AI のレビューが通ったことを人の承認の代わりにしない。
signs:
  - {type: goal, text: PR の作成と説明文の下書きを任せたい}
  - {type: situation, text: AI が書いた変更を、チームのレビューに出す}
  - {type: symptom, text: AI のレビューで問題なしと出たのに、人のレビューで欠陥が見つかった}
prerequisites: [working-with-git, independent-review, own-generated-code, agreement-is-not-evidence]
related: [diffs-humans-must-read, automated-pr-review, github-actions-with-claude, risk-tiered-approval, grow-review-checklists, review-bottlenecks, separate-roles, disclosure-and-provenance, instructing-reviewers, commit-and-comment-language, resume-and-branch, refactor-and-migrate]
sources: [cc-docs-common-workflows, claude-dev-blog-solving-code-review-anthropic]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards-first}
  - {title: 出す前にリスクを挙げさせる, anchor: risks-before-submitting}
  - {title: PR の説明に書くこと, anchor: pr-description}
  - {title: レビューの指摘を直させる, anchor: address-review}
  - {title: 全体の確かめ方, anchor: verify-overall}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：変更から PR を作らせ、出す前にリスクと確かめた証拠を書き出させる。説明は自分の言葉で言い直せるまで読み、AI のレビューが通ったことを人の承認の代わりにしない。
    - **いつ引くか**：PR の作成と説明文の下書きを任せたいとき。AI が書いた変更をチームのレビューに出すとき。AI のレビューで問題なしと出たのに、人のレビューで欠陥が見つかったとき。
    - **前提**：<!-- link:begin working-with-git -->[git との付き合い方](../cli/working-with-git.md)<!-- link:end -->・<!-- link:begin independent-review -->[書いた本人ではない者にレビューさせる](../verify/independent-review.md)<!-- link:end -->・<!-- link:begin own-generated-code -->[生成コードを自分のものにする](../verify/own-generated-code.md)<!-- link:end -->・<!-- link:begin agreement-is-not-evidence -->[同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)<!-- link:end -->

<!-- textlint-disable -->
別名：プルリクエストを作らせる・PR の説明文・pull request・コードレビューを受ける
<!-- textlint-enable -->

PR を作り、レビューを受けるレシピは、Claude Code が書いた変更をチームのレビューに出すまでの進め方である。Claude に任せるのは、PR の作成、説明文の下書き、出す前のリスクの洗い出し、レビューの指摘への案と直しである。人が握るのは、説明の理解、承認、マージの判断である。

## 先に整える守り {#guards-first}

PR を任せる前に、確かめる守りと縛る守りを整える。任せる幅を広げる前に、見合う守りを先に置く。

- 区切りと、コミットを握る人：変更を小さく区切り、コミットと push を人が握るか任せるかを決めておく（<!-- link:begin working-with-git#who-commits -->[git との付き合い方 › 誰がコミットするか](../cli/working-with-git.md#who-commits)<!-- link:end -->）。
- 書いた本人ではない者のレビュー：変更を書いたセッションとは別のセッションや人に点検させる（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->）。
- 理解の関門：生成された変更は、処理の流れを説明させ、自分の言葉で言い直せてから採る（<!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end -->）。
- 人が必ず読む箇所：テストや採点の変更、特例の分岐、例外の握りつぶしなどは、差分を全部は読めなくても人が読む（<!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](../verify/diffs-humans-must-read.md#red-flags)<!-- link:end -->）。
- 承認の数え方：AI のレビューの通過は、人の承認に数えない（<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end -->、<!-- link:begin risk-tiered-approval#ai-approval-doesnt-count -->[リスク段階別の承認（AI の承認を人の承認に数えない） › AI の承認を数えない](../team/risk-tiered-approval.md#ai-approval-doesnt-count)<!-- link:end -->）。

PR 1 本の大きさにも上限を置く。大きな変更は、小さく確かめられる単位に分けて PR を分ける（<!-- link:begin refactor-and-migrate#small-steps -->[リファクタリングと大規模な移行 › 小さく分けて一つずつ確かめる](refactor-and-migrate.md#small-steps)<!-- link:end -->）。人のレビューの量には限りがあり、変更を出す速さではなく、レビューできる量に流す量を合わせる（<!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](../team/review-bottlenecks.md#match-review-capacity)<!-- link:end -->）。

## 出す前にリスクを挙げさせる {#risks-before-submitting}

出す前にリスクを挙げさせる手順は、レビューへ出す前の段階で、変更の危ない所と確かめていない点を人が先に知るための手順である。公式の Common workflows は、PR の作成の流れで、提出前のレビューとリスクの洗い出しを示している。

進め方は次の 4 段で、各段の終わりに印を決めておく。

1. 変更の要約を作らせる。終わりの印は、要約を読んで、自分の意図と合っていると言えること。
2. リスクと、まだ確かめていない点を挙げさせる。終わりの印は、リスクの表の各行に場所と確かめ方が付くこと。
3. 挙げたリスクのうち、実行して確かめられるものを実行させる。終わりの印は、実行したコマンドと出力が付いた行と、実行していない行が分かれていること。
4. 人が表を読み、実行していない行と、表にない場所を決める。終わりの印は、人が読む箇所の一覧ができること。

依頼の例を次に示す。リスクごとに確かめ方を付けさせ、実行したものと実行していないものを分けさせる点は、レビュー役への頼み方と同じ考え方である（<!-- link:begin instructing-reviewers#per-finding -->[レビュアーへの指示の書き方 › 指摘ごとに確かめ方を付けさせる](../verify/instructing-reviewers.md#per-finding)<!-- link:end -->）。

<!-- gen:begin snippet create-and-review-prs/risk-request -->
<!-- textlint-disable -->

??? example "雛形：出す前にリスクと確かめていない点を挙げさせる依頼"

    ```markdown
    これから PR を出す。出す前に、この変更のリスクと、まだ確かめていない点を洗い出してほしい。ファイルは書き換えず、読んで実行するだけにする。

    対象は、現在のブランチと `main` の差分とする。

    出してほしいもの

    1. 変更の要約（何を、なぜ変えたか。3〜5 行）
    2. リスクの表。列は「場所（ファイル・行）」「何が起きうるか」「確かめ方」「確かめたか（実行した／実行していない）」とする
    3. 実行して確かめた項目には、実行したコマンドと出力の該当の行を付ける。実行していない項目は、そう書く
    4. この変更が触れた、入力の端（空・最大・重複・境界の値）の一覧と、それぞれを確かめたか
    5. テスト・設定・期待値のファイルに入った変更の一覧（あれば）

    リスクがないと判断した場合も、見た範囲と見ていない範囲を書く。見立てを断定せず、根拠の分かる書き方にする。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet create-and-review-prs/risk-request -->

Claude が挙げたリスクの一覧は、完全ではない。一覧にない所の見落としは残るので、別のセッションや人のレビューで補う。依頼に「このあたりは問題ない」と自分の見立てを書き添えると、その見立てに引きずられやすい（<!-- link:begin instructing-reviewers#hide-your-view -->[レビュアーへの指示の書き方 › 自分の見立てを書き添えない](../verify/instructing-reviewers.md#hide-your-view)<!-- link:end -->）。見立てを書かずに頼む。

## PR の説明に書くこと {#pr-description}

PR の説明は、コードの要約ではなく、レビューする人が判断するための材料である。下書きは Claude に作らせてよい。ただし、次の 5 項目を欄として決めておくと、欠けた所が見える。

- AI の使用と任せた範囲：どこを AI が書き、どこを人が書いたか。開示の求め方は場ごとに違うので、規則で確かめる（<!-- link:begin disclosure-and-provenance#four-points -->[AI 利用の開示と出所の記録 › 開示・相談・出所・意図の四つの観点](../safety/disclosure-and-provenance.md#four-points)<!-- link:end -->）。
- 検証の証拠（分母つき）：「テストが通った」ではなく、実行したコマンドと、通った数／実行した数を書く。飛ばした数も書く。
- 自分の言葉での短い説明：書いた人が AI の文章を見ずに書く。書けない所は、読み直す箇所である（<!-- link:begin own-generated-code#check-explanation -->[生成コードを自分のものにする › 説明を実際の動きと照らす](../verify/own-generated-code.md#check-explanation)<!-- link:end -->）。行数は例であり、3 行に根拠はない。
- 想定した境界の場合と確かめ方：空・最大・重複・境界の値のうち、何を想定して、どう確かめたか。
- リスク区分と承認者：変更の中身で段を決め、段ごとに必要な人の承認を決める（<!-- link:begin risk-tiered-approval#three-tiers -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 三つの段と承認の数](../team/risk-tiered-approval.md#three-tiers)<!-- link:end -->）。

雛形を次に示す。PR テンプレートの置き場に置くと、新しい PR の説明欄に最初から入る。

<!-- gen:begin snippet create-and-review-prs/pr-template -->
<!-- textlint-disable -->

??? example "雛形：PR の説明の雛形"

    ```markdown
    ## AI の使用と任せた範囲

    - AI を使ったか：使った／使っていない
    - 任せた範囲：（例：テストの追加と、`src/parser/` の分岐の修正。設計と API の形は人が決めた）
    - 使った道具：（例：Claude Code）

    ## 検証の証拠（分母つき）

    - 実行したコマンド：
    - 結果（通った数／実行した数／飛ばした数）：（例：42 件中 42 件が通過、飛ばした件数 0）
    - 実行していない確認と、その理由：

    ## 自分の言葉での短い説明

    この変更が何をするかを、書いた人が AI の文章を見ずに書く。行数は例で、3 行に根拠はない。

    1.
    2.
    3.

    ## 想定した境界の場合と確かめ方

    | 場合（空・最大・重複・境界の値など） | 確かめ方 | 確かめたか |
    |---|---|---|
    |  |  |  |

    ## リスク区分と承認者

    - リスク区分：（チームの段の名前）
    - 承認者（人）：
    - AI のレビューの結果は参考として貼ってよいが、承認の数には入れない
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet create-and-review-prs/pr-template -->

Claude に説明文を下書きさせるときは、この雛形の見出しに沿うよう頼む。下書きのうち、人が書き直すのは「自分の言葉での短い説明」である。ほかの欄も、下書きが実際の差分と実行結果に合っているかを、人が照らして確かめる。コミットメッセージや PR の説明の言語は、チームの決まりとして共有の指示に書く（<!-- link:begin commit-and-comment-language#team-vs-personal -->[コミットメッセージ・コメントの言語 › チームの決まりと個人の好みを分ける](../japanese/commit-and-comment-language.md#team-vs-personal)<!-- link:end -->）。

PR そのものを作らせるときは、上の 4 段と説明文の下書きがそろってから、Claude Code に「PR を作って」と頼む。公式の Common workflows が示す方法である。`gh pr create` で作られた PR はセッションに紐づき、`claude --from-pr <番号>` で再開できる。この挙動は公式の文書によるもので、この辞典では試していない。

## レビューの指摘を直させる {#address-review}

レビューの指摘を直させる手順は、指摘を受け入れるかを人が決め、直しだけを Claude に任せる手順である。指摘をそのまま「直して」と渡すと、根拠の弱い指摘にも従う方向に傾きやすい（<!-- link:begin agreement-is-not-evidence#agreement-depends-on-asking -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 賛成は聞き方と押し方で増える](../judgment/agreement-is-not-evidence.md#agreement-depends-on-asking)<!-- link:end -->）。案を先に出させ、人が採否を決めてから直させる。

1. 指摘を貼り、直さずに、指摘ごとの案を出させる。終わりの印は、各指摘に「直す／直さない／人に確認する」と根拠が付くこと。
2. 人が採否を決める。終わりの印は、採る指摘の番号を人が返すこと。
3. 採った指摘だけを、指摘ごとの小さな変更で直させる。終わりの印は、直した箇所と、直った後に実行した確認が示されること。
4. 採らなかった指摘には、理由を書いてレビューした人に返す。終わりの印は、すべての指摘に答えがあること。
5. 直しの差分を、人が読む。終わりの印は、テスト・期待値・設定のファイルが変わっていれば、その理由を人が確かめたこと。

依頼の例を次に示す。

<!-- gen:begin snippet create-and-review-prs/address-request -->
<!-- textlint-disable -->

??? example "雛形：レビューの指摘ごとに案を出させる依頼"

    ```markdown
    この PR にレビューの指摘が付いた。指摘は下に貼る。まず、直さずに、指摘ごとの案だけを出してほしい。

    指摘ごとに次を書く。

    1. 指摘の番号と、指摘の要約
    2. 指摘が正しいかの見立てと、その根拠（コードの該当の行、または実行した結果）
    3. 案：直す／直さない／人に確認する
    4. 直す案なら、直す箇所と、直った後に何を実行して確かめるか

    次を守る。

    - 指摘に賛成することを前提にしない。根拠が見つからない指摘は、そう書く
    - テスト・期待値・設定のファイルは変えない。変えないと直らないと思う場合は、直さずに理由を書いて人に確認する
    - 案の表を返すところまでで止める。私が「この番号を直して」と返してから、直す

    <ここにレビューの指摘を貼る>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet create-and-review-prs/address-request -->

直しの往復が長く続くときは、往復の上限を先に決めておく。上限の回数は例（2 回など）で、根拠のある数ではない。上限に達したら、Claude に続けさせず、人が方針を決め直す。

PR を作ったセッションは、`claude --from-pr <番号>` や、名前を付けたセッションの再開で戻れる（<!-- link:begin resume-and-branch#resume -->[セッションに名前を付けて再開・分岐する › 再開する](../cli/resume-and-branch.md#resume)<!-- link:end -->）。再開したセッションは、変更を書いたときの推論を引き継いでいる。指摘が正しいかの見立ては、新しいセッションなど、その推論を見ていない者にも出させて比べる。

自動の PR レビュー（Code Review・/ultrareview）の指摘も、人のレビューの指摘と同じ扱いにする。使い方は <!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）<!-- link:end --> に任せる。指摘の採否と承認は人が決める。

## 全体の確かめ方 {#verify-overall}

PR を出す前に、次の 4 点を人が確かめる。1 つでも欠けるなら、出さずに戻る。

- 検証の証拠に、実行したコマンドと、分母つきの結果が付いている。
- 説明を、AI の文章を見ずに言い直せる。
- 差分の赤信号（テストの変更・特例の分岐・例外の握りつぶしなど）を、人が読んだ。
- 承認者が人である。AI のレビューの結果は、承認の数に入れていない。

Claude Code チームのレビュー運用は、変更をリスクの段に分け、段ごとに人の承認の数を決めている（根拠：中。企業の一次の報告で、Anthropic 自身のリポジトリでの運用）。その原文には、次の一文がある。

> An agent's approval never counts as a person's, either.
> （出典：[How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)）

同じ運用では、機密と指定されたパスと CI のワークフローのファイルは、常に人が見る。段の考え方と承認の数は、持ち主のページに任せる（<!-- link:begin risk-tiered-approval#always-human -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 段を決めるのは中身、常に人が見る場所](../team/risk-tiered-approval.md#always-human)<!-- link:end -->）。役割を分けて、疑う役を持ち回りにする方法もある（<!-- link:begin separate-roles#roles -->[役割を分ける（書く人・承認する人・疑う人） › 三つの役割が持つもの](../team/separate-roles.md#roles)<!-- link:end -->）。

!!! example "判断例：AI のレビューが通った PR を、人の承認なしに進めるか"
    - **状況**：Claude が作った文言だけの変更の PR に、自動のレビューが「問題なし」と返した。
    - **迷う候補**：人が 1 人見るまで待つ。チームの規則が許すなら、人の承認なしで進める。
    - **選んだもの**：チームが段の規則を持ち、文言だけの変更を人の承認が要らない段と決めているなら進める。規則がないなら、人が 1 人見るまで待つ。
    - **理由**：人の承認を省いてよいかは、AI のレビューの結果ではなく、変更の中身とチームの規則で決まるからである。認証・設定・CI のワークフローに触れる変更なら、規則があっても人が見る。

## うまくいかないとき {#when-it-fails}

AI のレビューで問題なしと出たのに、人のレビューで欠陥が見つかったときは、次の順に原因を見る。

- 同じ推論が、書く側と確かめる側に入っていなかったか。書いたセッションに自分の変更を点検させても、別の見落としは出にくい（<!-- link:begin independent-review#what-happens -->[書いた本人ではない者にレビューさせる › 同じ会話で確かめさせると何が起きるか](../verify/independent-review.md#what-happens)<!-- link:end -->）。
- AI の賛成や、複数の AI レビュアーの一致を、正しさの証拠に数えていなかったか（<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end -->）。証拠として数えるものは別に決める（<!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end -->）。
- 人が説明を読まずに承認していなかったか。出す前の確かめ（この記事の「全体の確かめ方」の 4 点）を飛ばしていなかったか。
- レビューが人に積もり、読む量が足りなくなっていなかったか（<!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](../team/review-bottlenecks.md#where-it-clogs)<!-- link:end -->）。

見つかった欠陥は、見落とした理由を抜き出して、レビューの観点に足す（<!-- link:begin grow-review-checklists -->[レビューの観点を育てる](../team/grow-review-checklists.md)<!-- link:end -->）。観点は、人の承認を経て足す。

GitHub Actions から Claude に PR を作らせる場合は、鍵と権限を絞り、外の人が書いた issue や PR の扱いに注意する（<!-- link:begin github-actions-with-claude#secrets-and-permissions -->[GitHub Actions と @claude › 鍵と権限](../delegate/github-actions-with-claude.md#secrets-and-permissions)<!-- link:end -->）。どの場合も、マージの前に人がレビューする。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04
- [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)：Anthropic（claude.dev Blog）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [git との付き合い方](../cli/working-with-git.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)

**関連**

- [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)
- [GitHub Actions と @claude](../delegate/github-actions-with-claude.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)
- [レビューの観点を育てる](../team/grow-review-checklists.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [役割を分ける（書く人・承認する人・疑う人）](../team/separate-roles.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)
- [レビュアーへの指示の書き方](../verify/instructing-reviewers.md)
- [コミットメッセージ・コメントの言語](../japanese/commit-and-comment-language.md)
- [セッションに名前を付けて再開・分岐する](../cli/resume-and-branch.md)
- [リファクタリングと大規模な移行](refactor-and-migrate.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
