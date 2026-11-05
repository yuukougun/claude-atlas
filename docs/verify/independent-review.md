---
id: independent-review
title: 書いた本人ではない者にレビューさせる
aliases: [独立したレビュー, 新しいセッションでレビュー, Writer/Reviewer パターン, /code-review, /security-review]
type: concept
field: verify
chapter: レビューで確かめる
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, 文章, チーム]
summary: 変更を生んだ推論を見ていない者（新しいセッション・サブエージェント・別の人）にレビューさせる理由と分け方が分かる。AI の承認は人の承認に数えない。
signs:
  - {type: situation, text: 自分の目で全部レビューする時間がない}
  - {type: symptom, text: Claude に自分の作業を確認させると、いつも問題なしと言う}
  - {type: goal, text: 書いた本人ではない目でレビューさせたい}
  - {type: goal, text: AI が書いたコードに脆弱性がないか見させたい}
prerequisites: [verification-ladder, subagent-isolation]
related: [instructing-reviewers, agreement-is-not-evidence, diffs-humans-must-read, second-opinion-from-another-model, own-generated-code, writing-subagents, risk-tiered-approval, separate-roles, sycophancy, ask-without-sycophancy, automated-pr-review, create-and-review-prs, review-bottlenecks]
tracks: [code-review, subagents, security-review]
outdated_advice: []
sources: [cc-docs-best-practices, cc-docs-commands, cc-docs-code-review-local, cc-docs-sub-agents, claude-dev-blog-solving-code-review-anthropic]
volatility: 中
sections:
  - {title: 同じ会話で確かめさせると何が起きるか, anchor: what-happens}
  - {title: 誰にレビューさせるか, anchor: who}
  - {title: 推論を見せない, anchor: hide-reasoning}
  - {title: AI の承認を人の承認に数えない, anchor: ai-approval}
  - {title: セキュリティのレビューを頼む（脆弱性を探させる）, anchor: security-review}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面と誤解, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：変更を生んだ推論を見ていない者にレビューさせる理由と分け方が分かる。AI の承認は人の承認に数えない。
    - **いつ引くか**：自分の目で全部レビューする時間がないとき。Claude に自分の作業を確認させると、いつも問題なしと言うとき。AI が書いたコードに脆弱性がないか見させたいとき。
    - **前提**：<!-- link:begin verification-ladder -->[検証の階段](verification-ladder.md)<!-- link:end -->、<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->

<!-- textlint-disable -->
別名：独立したレビュー・新しいセッションでレビュー・Writer/Reviewer パターン・/code-review・/security-review
<!-- textlint-enable -->

書いた本人ではない者にレビューさせるとは、変更を生んだ推論を見ていない相手に、成果物と基準だけを渡して確かめさせることである。相手は、新しいセッション、サブエージェント、別の人のどれかになる。このページは、誰を選び、何を見せ、何を任せないかを扱う。

## 同じ会話で確かめさせると何が起きるか {#what-happens}

変更を書いた会話の中で「確認して」と頼むと、問題なしと返ることが多い。想定する場面を挙げる。

- Claude に入力検証の追加を頼み、テストが通ったところで「見直して」と頼む。
- Claude は、自分が書いた方針に沿って読み返し、「要件を満たしている」と答える。
- 後で、空の入力の扱いが抜けていると分かる。

同じ会話の Claude は、変更を書いたときの推論をすべて文脈に持っている。その推論に沿って読むので、前提を疑う読み方になりにくい。また、利用者の考えに合う応答が好まれる形で訓練されているので、Claude は同意しやすい。仕組みは <!-- link:begin sycophancy#why -->[迎合（sycophancy） › なぜそうなるか](../basics/sycophancy.md#why)<!-- link:end --> にある。

これは「確かめていない」という Claude 側の原因の 1 つである。完了の報告は出ているが、確かめた中身は書いた側の見方の繰り返しに過ぎない。確かめ方の段の中での位置づけは、<!-- link:begin verification-ladder#four-steps -->[検証の階段 › 四つの段](verification-ladder.md#four-steps)<!-- link:end --> にある。

## 誰にレビューさせるか {#who}

レビューさせる相手は 4 つに分けて考える。違いは、推論を見たか、編集できるか、責任を持つかの 3 点である。

| 相手 | 推論を見たか | 編集できるか | 責任を持つか |
| --- | --- | --- | --- |
| 書いた本人（同じ会話の Claude） | 見た | 既定でできる | 持てない |
| 新しいセッション | 見ない（渡したものだけ） | 既定でできる | 持てない |
| サブエージェント | 見ない（渡した依頼だけ） | 道具を絞れば、できなくなる | 持てない |
| 別の人 | 見せなければ見ない | できるが、レビューでは指摘を返すだけにする取り決めが多い | 持てる |

表の読み方は 3 つある。

- 新しいセッションとサブエージェントは、推論を見ないという点で同じ役を果たす。最も簡単な独立レビュアーは、2 つ目のセッションである。
- サブエージェントは、道具を `Read`・`Grep`・`Glob` に絞ると、編集できないレビュアーになる。道具の制限は鍵であり、「直さないで」と頼むだけのお願いより強い（道具を絞る書き方は <!-- link:begin writing-subagents#tools-and-model -->[サブエージェントの作り方と使いどころ › 道具・モデル・effort を絞る](../extend/writing-subagents.md#tools-and-model)<!-- link:end --> にある）。
- サブエージェントの中でも、fork は親の会話を引き継ぐ。親の推論を見るので、独立したレビューにならない。

責任は、AI には持てない。変更を受け入れる責任を持つのは、人だけである。

面ごとの手段は、次のとおりである。

=== "アプリ"

    新しい会話を開き、変更を書いた会話の文面ではなく、成果物と基準だけを貼る。会話を分けることが、独立の中身になる。

=== "Claude Code"

    次の 3 つの手段がある。

    - 新しいセッションを開き、成果物と基準を渡す。
    - 読み取りだけのサブエージェントに頼む。
    - `/code-review` を使う。今の差分か、渡した PR・ブランチ・パスの正しさの誤りを、選んだ effort でレビューするバンドルのスキルである。成熟度は <!-- gen:begin feature code-review/maturity -->GA<!-- gen:end feature code-review/maturity --> である（[Commands](https://code.claude.com/docs/en/commands)、[Review locally with /code-review](https://code.claude.com/docs/en/code-review-local)）。`--fix` で直しを当て、`--comment` で PR に行ごとのコメントを付ける。

古い記事の `/review` は、今は <!-- name:begin review-to-code-review -->/code-review<!-- name:end --> と読み替える。

編集できないレビュアーのサブエージェントの例を示す。

<!-- gen:begin snippet independent-review/reviewer-subagent -->
<!-- textlint-disable -->

??? example "雛形：編集できないレビュアーのサブエージェント"

    ```markdown
    ---
    name: reviewer
    description: 渡された変更を、書いた側の事情を知らない立場でレビューする。コードを直さず、指摘だけを返す。変更のレビューを頼まれたときに使う
    tools: Read, Grep, Glob
    ---

    あなたは、この変更を書いていないレビュアーである。変更の経緯や、書いた側の意図は知らされない。渡された成果物と基準だけを根拠にする。

    手順:

    1. 依頼に書かれたファイルと基準を読む。基準が書かれていなければ、先にそれを聞き返す。
    2. 基準に照らして、気づいた問題を省かずに全部挙げる。重要度で絞らない。絞るのは別のパスで行う。
    3. 指摘ごとに、場所（ファイルと行）、何が問題か、それが本当かを確かめる方法を書く。

    ファイルは編集しない。直し方の提案は、指摘に添える 1 行までにする。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet independent-review/reviewer-subagent -->

編集できないレビュアーの雛形は、レビューの基準と成果物を依頼で受け取り、全部挙げさせ、指摘ごとに確かめ方を書かせる。網羅と選別の分け方は <!-- link:begin instructing-reviewers#exhaustive-then-filter -->[レビュアーへの指示の書き方 › 網羅と選別を分ける](instructing-reviewers.md#exhaustive-then-filter)<!-- link:end --> が、指摘ごとの確かめ方は <!-- link:begin instructing-reviewers#per-finding -->[レビュアーへの指示の書き方 › 指摘ごとに確かめ方を付けさせる](instructing-reviewers.md#per-finding)<!-- link:end --> が扱う。

!!! example "判断例：どの独立したレビューを使うか"
    - **状況**：認証の周りを直した変更がある。自分で全部は読めないが、午後までにマージしたい。
    - **迷う候補**：新しいセッションに読ませて、その結果で済ませる。新しいセッションの指摘を見たうえで、人に認証の部分だけを読んでもらう。
    - **選んだもの**：新しいセッションに読ませたうえで、認証の部分は人に読んでもらう。
    - **理由**：新しいセッションは推論に引きずられないが、責任を持てない。認証は誤ると被害が大きい場所なので、人の目を残す。変更の中身で常に人が見る場所を決める考え方は、<!-- link:begin risk-tiered-approval#always-human -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 段を決めるのは中身、常に人が見る場所](../team/risk-tiered-approval.md#always-human)<!-- link:end --> にある。

## 推論を見せない {#hide-reasoning}

レビュアーに見せるものは、成果物と基準だけにする。変更を生んだ推論、つまり「なぜこう書いたか」「どこが不安だったか」は見せない。

公式は、`/code-review` を会話を見ていないサブエージェントとして、コードを生んだ推論に引きずられない、と説明する（[Best practices](https://code.claude.com/docs/en/best-practices)）。推論を渡すと、その長所は消える。レビュアーは書いた側の見方をなぞり、同じ見落としを繰り返す。

同じ依頼の Before と After を並べる。

!!! example "Before：推論と結論を渡す"
    - 認証の変更を入れた。トークンの期限は、設計の都合で確認を省いている。ここは問題ないと思う。レビューしてほしい。

!!! example "After：成果物と基準だけを渡す"
    - 次のファイルを、次の基準でレビューしてほしい。対象は `auth/session.py`。基準は、期限切れのトークンを受け付けないこと、失敗時に理由を返さないこと。

After では、次の 3 つを変えている。

- 「問題ないと思う」という自分の見立てを外した。見立てを書き添えると、レビュアーが同意に流れる（<!-- link:begin instructing-reviewers#hide-your-view -->[レビュアーへの指示の書き方 › 自分の見立てを書き添えない](instructing-reviewers.md#hide-your-view)<!-- link:end -->）。
- 省いた確認の理由を外した。理由が妥当かどうかは、レビュアーが判断する材料にする。
- 基準を、確かめられる形で足した。基準がないと、何を見るべきかも決まらない。

新しいセッションに渡す依頼の雛形を示す。

<!-- gen:begin snippet independent-review/fresh-session-request -->
<!-- textlint-disable -->

??? example "雛形：新しいセッションに渡すレビューの依頼"

    ```markdown
    別の会話で、次の変更をレビューしてほしい。あなたはこの変更を書いていない。

    レビューする対象:
    <変更したファイルの名前、または貼り付けた差分>

    基準:
    <満たすべき仕様、またはチェックリスト。例: SPEC.md の全要件が実装され、列挙したエッジケースにテストがある>

    見てほしい観点:
    <例: 正しさ、エラーの扱い、テストが何を確かめているか>

    次の形で返してほしい。
    - 指摘ごとに、場所、問題、それが本当かを確かめる方法
    - 問題がなければ、何を見て問題がないと判断したか

    変更を書いた側の考えや、変更の理由は渡さない。渡された対象と基準だけで判断する。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.147。

<!-- textlint-enable -->
<!-- gen:end snippet independent-review/fresh-session-request -->

成果物と基準だけを新しい文脈で批評させる考え方は、<!-- link:begin ask-without-sycophancy#fresh-context-critique -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる](../judgment/ask-without-sycophancy.md#fresh-context-critique)<!-- link:end --> でも扱う。批判を強めすぎない加減は、<!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない](../judgment/ask-without-sycophancy.md#dont-overdo-criticism)<!-- link:end --> にある。

## AI の承認を人の承認に数えない {#ai-approval}

AI のレビューが通っても、それを人の承認に数えない。AI が書いた変更は、新しいコンテキストの AI レビュアーと、別の人の両方に通す。前者は推論に引きずられない役を、後者は責任と理解を担保する役を持つ。

Claude Code のチームのレビュー運用を述べた記事も、エージェントの承認を人の承認に数えない、という運用を書いている。

（出典：[How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)。Anthropic の開発者向けのブログである。）

変更をリスクの段に分け、段ごとに人の承認の数を決める方法の本体は、<!-- link:begin risk-tiered-approval#ai-approval-doesnt-count -->[リスク段階別の承認（AI の承認を人の承認に数えない） › AI の承認を数えない](../team/risk-tiered-approval.md#ai-approval-doesnt-count)<!-- link:end --> にある。AI のレビューが付いた PR の扱いは、<!-- link:begin create-and-review-prs#risks-before-submitting -->[PR を作り、レビューを受ける › 出す前にリスクを挙げさせる](../recipes/create-and-review-prs.md#risks-before-submitting)<!-- link:end --> と <!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）<!-- link:end --> が扱う。

AI のレビュアーを何体並べても、全員の一致は正しさの証拠にならない。決め手は実行と計測である。理由は <!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end --> と <!-- link:begin second-opinion-from-another-model#agreement -->別のモデルに第二の意見を求める（一致は証拠にならない）<!-- link:end --> にある。

## セキュリティのレビューを頼む（脆弱性を探させる） {#security-review}

AI が書いたコードに脆弱性がないか見させたいときも、書いていない者に頼む。同じ会話の Claude は、自分が書いたコードの前提に沿って読むので、前提そのものの穴を見落としやすい。

Claude Code には、組み込みのコマンド `/security-review` がある。今のブランチと origin の既定のブランチとの差分を、注入・認証・データの露出などの脆弱性の点で見る。成熟度は <!-- gen:begin feature security-review/maturity -->GA<!-- gen:end feature security-review/maturity --> である（[Commands](https://code.claude.com/docs/en/commands)）。使うには、origin のリモートが要る。セキュリティの別の道具（`security-guidance` や Claude Security のプラグイン）とは別物である。

自分で観点を決めて頼むときは、書いていない者に、見る観点を渡して脆弱性を探させる。

<!-- gen:begin snippet independent-review/security-review-request -->
<!-- textlint-disable -->

??? example "雛形：脆弱性を探させるレビューの依頼"

    ```markdown
    別の会話で、次の変更に脆弱性がないかをレビューしてほしい。あなたはこの変更を書いていない。

    対象:
    <変更したファイルの名前、または貼り付けた差分>

    この変更が扱うもの:
    <例: 利用者が入力した文字列を受け取り、データベースを検索する>

    見てほしい観点:
    - 外から来た入力を、検証や無害化をせずに使っていないか
    - 認証と、操作してよい人かの確認が、抜けていないか
    - 秘密情報や個人情報が、ログや返答に出ていないか
    - 外部のコマンドやクエリを、文字列の連結で組み立てていないか

    見つけた問題は、指摘ごとに、場所、何が起きうるか、それが本当かを確かめる方法を書く。確信が持てないものは、その旨を付けて挙げる。

    見つからなかったときは、見つからなかった観点と、見ていない範囲を書く。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.1.147。

<!-- textlint-enable -->
<!-- gen:end snippet independent-review/security-review-request -->

この依頼の雛形では、見つからなかったときに、見た観点と見ていない範囲を書かせる。「問題なし」の一言では、何を確かめたのか分からないからである。観点の決め方や指摘の出させ方の一般則は、<!-- link:begin instructing-reviewers -->[レビュアーへの指示の書き方](instructing-reviewers.md)<!-- link:end --> が扱う。

AI のレビューで見つからなかったことを、安全の証拠に数えない。見つからなかったのは、見た観点では見つからなかった、という意味に限られる。本番に出す前の判断は、人が持つ。

## 何に効くか {#effects}

独立したレビューは、原理の「確かめる」に当たる。防ぐ原因は、Claude 側の「確かめていない」である。書いた側の見方をなぞった確認は、確かめたことにならない。書いていない者を通すと、別の見方での確かめが 1 回入る。

人の側の落とし穴は、「同意を根拠にする」である。レビューが通ったという同意を、そのまま正しさの根拠にしてしまう。AI の承認を人の承認に数えない決まりが、この落とし穴を塞ぐ。組織で役割に分けて守る方法は、<!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)<!-- link:end --> にある。

差分を全部は読めないとき、人が必ず読む箇所は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](diffs-humans-must-read.md#red-flags)<!-- link:end --> で見分ける。生成されたコードを自分のものにする確かめ方は <!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](own-generated-code.md#gate)<!-- link:end --> にある。

## 効かない場面と誤解 {#limits}

効かない場面と、よくある誤解を挙げる。

- **役を変えただけでは足りない**。同じ会話の中で「次はレビュアーとして読んで」と頼んでも、推論は文脈に残っている。会話を分けるか、サブエージェントに渡す。
- **新しいセッションは、人の代わりではない**。責任を持てないので、人の承認に数えない。
- **独立していれば正しい、ではない**。新しいセッションも、迎合の傾向を持つ。基準を渡さず「確認して」とだけ頼むと、問題なしと返りやすい。
- **サブエージェントは、道具を絞らなければ編集できる**。編集させたくないレビューは、道具で絞る。
- **レビュアーの数を増やしても、証拠は増えない**。一致は、実行と計測の代わりにならない。
- **レビューが増えると、人に積もる**。AI の指摘が増えるほど、採否を決める人の負担が増える。流す量の合わせ方は <!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](../team/review-bottlenecks.md#match-review-capacity)<!-- link:end --> にある。

「Writer/Reviewer」は、改稿前の Best practices にあった語で、今の文書では確かめ方の段の 1 つとして書いている。この辞典では「書いていない者のレビュー」の名前で扱う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Review locally with /code-review](https://code.claude.com/docs/en/code-review-local)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)：Anthropic（claude.dev Blog）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証の階段](verification-ladder.md)
- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**次に読む**

- [レビュアーへの指示の書き方](instructing-reviewers.md)
- [PR を作り、レビューを受ける](../recipes/create-and-review-prs.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)
- [役割を分ける（書く人・承認する人・疑う人）](../team/separate-roles.md)

**関連**

- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [人間が読むべき差分の箇所](diffs-humans-must-read.md)
- [生成コードを自分のものにする](own-generated-code.md)
- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)
- [迎合（sycophancy）](../basics/sycophancy.md)
- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
