---
id: working-with-git
title: git との付き合い方
aliases: [コミットを任せるか, 小さくコミットする, draft PR, git を Claude に任せる]
type: concept
field: cli
chapter: 巻き戻しとセッション
order: 70
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 変更を小さく区切ってコミットし、コミットと push を人が握るか任せるかを段階で決める。一つの変更を一つの評価と一つのコミットに対応させると、悪くなったときにすぐ戻せる。
signs:
  - {type: goal, text: コミットや PR の作成をどこまで任せてよいか決めたい}
  - {type: situation, text: Claude の変更が大きくなり、どこで区切ればよいか分からない}
prerequisites: [checkpoints-and-rewind]
related: [create-and-review-prs, diffs-humans-must-read, destructive-commands, measure-changes, parallel-with-worktrees, bisect-regressions, own-generated-code, commit-and-comment-language, resume-and-branch]
tracks: []
outdated_advice: []
sources: [cc-docs-permission-modes, google-cloud-ai-machine-learning-introducing-doras, infoq-dora-state-ai-dev, dolthub-claude-code-gotchas, awesomeclaude-code-tips]
volatility: 低
sections:
  - {title: どこで区切るか, anchor: granularity}
  - {title: 誰がコミットするか, anchor: who-commits}
  - {title: 1変更1評価1コミット, anchor: one-change-one-eval}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：変更を 1 つの確かめと 1 つのコミットに対応させる区切り方と、コミットと push を人が握るか任せるかの段階が分かる。
    - **いつ引くか**：Claude の変更が大きくなって区切りが分からないとき、コミットや PR の作成をどこまで任せてよいか決めたいとき。
    - **前提**：<!-- link:begin checkpoints-and-rewind -->[チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)<!-- link:end -->

<!-- textlint-disable -->
別名：コミットを任せるか・小さくコミットする・draft PR・git を Claude に任せる
<!-- textlint-enable -->

git との付き合い方は、Claude Code の変更をどの単位でコミットに切り、コミットと push を誰が握るかを決める話である。区切りが粗いと、悪くなったときに戻す先が粗くなる。任せる幅を先に広げると、確かめる機会が減る。

## どこで区切るか {#granularity}

区切りの単位は「1 つの確かめで合否が出て、単独で戻せる変更」にする。Claude は頼まれた範囲を一気に進められるので、区切りは頼み方で決めることになる。

次のような場面で差が出る。

- 「認証まわりを直して」と頼み、十数個のファイルが 1 回の作業で書き換わった。テストは赤になったが、どの変更が原因か分からない。
- 同じ依頼を「まずセッション管理だけ。テストが通ったら止まって」と区切ると、赤くなったのがどの区切りかがすぐ分かる。戻す先もその区切りの直前になる。

区切りを細かくする理由は 3 つある。

- **戻す先が細かくなる**：悪くなった変更だけを戻せる。
- **人が読める量になる**：差分が大きいと、人は全部を読めない。読む箇所の選び方は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](../verify/diffs-humans-must-read.md#red-flags)<!-- link:end --> で扱う。
- **原因を絞り込みやすい**：コミットが小さいと、後から退行を探すときに候補が少ない。手順は <!-- link:begin bisect-regressions -->退行の原因を git bisect で探させる（準備中）<!-- link:end --> にある。

小さく頻繁にコミットする根拠は、実践者の経験則だけではない。DORA の AI ケイパビリティモデルは、AI 支援の開発で効く能力に、強いバージョン管理（頻繁なコミットとロールバック）と、小さなバッチでの作業を挙げる（根拠：中。企業の一次の報告）。ただし、これは開発チーム全体についての報告で、Claude Code の個別の頼み方を測ったものではない。

試している最中と、確定した区切りでは、使う道具が違う。

- **試している最中**：チェックポイントで戻す。ただし、Bash で変えたファイルや外での変更は戻らない。範囲は <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> にある。
- **確定した区切り**：コミットにする。git と組み合わせる流れは <!-- link:begin checkpoints-and-rewind#with-git -->[チェックポイントと /rewind（git との違い） › git と組み合わせる](checkpoints-and-rewind.md#with-git)<!-- link:end --> にある。

関係のない作業が混ざりそうなときは、区切りをコミットで切る前に、作業の側を分ける。別の案を試すなら <!-- link:begin resume-and-branch#branch -->[セッションに名前を付けて再開・分岐する › 分岐して別案を試す](resume-and-branch.md#branch)<!-- link:end --> を、同時に進めるなら <!-- link:begin parallel-with-worktrees#per-worktree-setup -->[git worktree で並列にする › worktree ごとの準備（依存・秘密・データベース）](../delegate/parallel-with-worktrees.md#per-worktree-setup)<!-- link:end --> を使う。

## 誰がコミットするか {#who-commits}

コミットと push を誰が握るかは、任せる前に守りを置き、守りに見合う幅まで任せる、という順で決める。この論点は実践者の立場が割れるので、公式の立場・実践者の幅・この辞典の推奨の 3 段で書く。

**公式の立場**：権限モードの文書は、auto モードの分類器が止める操作に、force push、`git reset --hard`、未承認の PR のマージを挙げる。同じ文書は、会話で「push しないで」と伝えると分類器は尊重するとしている。ただ、その発言は圧縮で失われうるので、確実にしたいときは deny ルールを使うよう書く（確認日 2026-10-29。止める操作の一覧は版で変わる）。コミットをどこまで任せるべきかという推奨は、確かめた範囲では見つからなかった。

**実践者の幅**：立場が割れている。

- 人が握る側は、git の操作を Claude に任せず、人が差分を見てコミットする（根拠：弱。実践者の単独の報告）。
- 任せる側は、PR の作成まで Claude に任せる（根拠：弱。実践者の経験談）。

**この辞典の推奨**：慣れるまでは人が握り、慣れたら draft PR まで任せる。「慣れた」の目安は、赤信号の差分を自分で見つけられることと、巻き戻しを実際に一度使ったことの 2 つである。これは辞典の目安で、研究で測った基準ではない。

任せる幅を広げる前に、先に置く守りが 3 つある。

- **差分を読む箇所を決める**：テストの変更や特例の分岐など、人が必ず読む箇所を先に決める。一覧は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](../verify/diffs-humans-must-read.md#red-flags)<!-- link:end --> にある。
- **取り返しのつかない操作を止める**：force push や `git reset --hard` は、会話の頼みでなく deny ルールで止める。守り方は <!-- link:begin destructive-commands#guard -->[消されたくないもの（破壊的コマンド） › 確認を求めさせる頼み方と、鍵](../safety/destructive-commands.md#guard)<!-- link:end --> にある。
- **出す前にリスクと証拠を書かせる**：PR の前に、リスクと確かめた証拠を書き出させる。手順は <!-- link:begin create-and-review-prs#risks-before-submitting -->PR を作り、レビューを受ける › 出す前にリスクを挙げさせる（準備中）<!-- link:end --> にある。

守りを置いたうえで、任せる幅を 3 段で考える。

| 段階 | Claude に任せること | 人が握ること | 先に要る守り |
| --- | --- | --- | --- |
| 1. 人が握る | 編集と、コミットの文面の案 | 差分を読み、コミットと push をする | 読む箇所を決める |
| 2. コミットまで任せる | 区切りごとのコミット | push と、push 前の差分の確認 | 取り返しのつかない操作を deny ルールで止める |
| 3. draft PR まで任せる | push と draft PR の作成 | PR の説明を読み、マージと承認をする | 出す前のリスクと証拠 |

段階 3 でも、マージと承認は人が握る。AI のレビューが通ったことは、人の承認の代わりにならない。説明の書き方は <!-- link:begin create-and-review-prs#pr-description -->PR を作り、レビューを受ける › PR の説明に書くこと（準備中）<!-- link:end --> にある。

コミットメッセージの言語は、チームの決まりとして共有の指示に書く。分け方は <!-- link:begin commit-and-comment-language#team-vs-personal -->コミットメッセージ・コメントの言語 › チームの決まりと個人の好みを分ける（準備中）<!-- link:end --> にある。

!!! example "判断例：コミットをどこまで任せるか"
    - **状況**：個人のリポジトリで、Claude Code を使い始めて数週間たつ。テストは整っていて、巻き戻しはまだ使ったことがない。
    - **迷う候補**：区切りごとのコミットまで任せる。または、これまでどおり人がすべてコミットする。
    - **選んだもの**：段階 1 のまま、まず巻き戻しを一度使う。
    - **理由**：コミットを任せる前に、悪くなった変更を戻せることを自分で確かめておきたい。戻し方を知らないまま任せると、小さく区切った利点が使えない。戻せると分かった後で、段階 2 に上げる。

## 1変更1評価1コミット {#one-change-one-eval}

1 つの変更を 1 つの評価と 1 つのコミットに対応させると、評価が悪化したときに、戻す対象が 1 つのコミットに決まる。実験の単位をそろえる考え方で、コード以外の変更にも当てはまる。

- **コードの変更**：変更を入れ、テストを流し、通ったらコミットする。
- **CLAUDE.md・プロンプト・スキルの変更**：変更を 1 つだけ入れ、失敗したタスクを前後で走らせて比べ、結果が良いときにコミットする。比べ方は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。

PR でも同じで、1 つの PR には 1 つのアイデアだけを入れる。スコアが下がったら、その PR をすぐ戻す（根拠：弱。複数の実務家の一致とされるが、一次の記事は確かめていない）。

頼み方で、対応を Claude に守らせる。

Before：

```text
評価の点数が上がるまで、プロンプトをいろいろ直して。
```

After：

```text
プロンプトの直しを 1 つだけ入れて。評価を流して前の結果と比べ、
差と結果を書いてから、その 1 つだけをコミットして。
悪くなったときは、その 1 つのコミットだけを戻して。
```

After で足したのは、変更を 1 つに限ること、前の結果と比べること、結果を書くこと、コミットの単位、悪化したときの戻し方の 5 つである。人がコミットする運用（誰がコミットするかの節の段階 1）なら、「コミットして」を「コミットの文面の案を出して」に替える。

Claude の作業が悪い方向に進み続けているときは、`/clear` と `git reset --hard` を組み合わせて、新旧のコードが混ざらないようにする実践者もいる（根拠：弱。単独の経験談）。ただし `git reset --hard` はコミットしていない変更を消す。直前の区切りでコミット済みのときだけ使い、消える経路は <!-- link:begin destructive-commands#how-it-happens -->[消されたくないもの（破壊的コマンド） › 消える経路](../safety/destructive-commands.md#how-it-happens)<!-- link:end --> で先に確かめる。

## 何に効くか {#effects}

1 変更ずつ区切り、任せる幅を段階で決めるやり方は、原理の「握る」「確かめる」に当たり、防ぐ原因の「確かめていない」「境界がない」に効く。落とし穴の「預けすぎる」にも当たる。

| 関わるもの | git での現れ方 | 効かせ方 |
| --- | --- | --- |
| 原理「握る」 | コミットと push の境界を人が持つ | 任せる段階を決め、取り返しのつかない操作は deny ルールで止める |
| 原理「確かめる」 | 変更ごとに評価を挟む | 1 つの変更ごとに評価を流し、結果が良いコミットだけを残す |
| 原因「確かめていない」 | 評価していない変更が積み重なる | 評価の前にコミットしない |
| 原因「境界がない」 | 変更が大きく、どこまでが 1 つの変更か分からない | 1 つの確かめで合否が出る単位に区切る |
| 落とし穴「預けすぎる」 | 差分を読まずに PR まで流す | 段階を 1 つずつ上げ、各段階の守りを先に置く |

## 誤解されやすいこと {#misconceptions}

- **「チェックポイントがあるから git は要らない」**：チェックポイントは、Bash で変えたファイルや外での変更を戻さない。git の代わりにしない。範囲は <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> にある。
- **「会話で push しないでと言えば守られる」**：会話の指示は、圧縮で失われうる。例外を許さない禁止は deny ルールで止める。
- **「コミットが多いほど良い」**：基準は数ではなく、1 つの確かめで合否が出る単位であること。意味のない細切れは、読む場面でも探す場面でも役に立たない（推論・実践例なし）。
- **「draft PR なら任せても安全」**：draft でも、説明を自分の言葉で言えるまでは出さない。確かめ方は <!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Introducing DORA’s inaugural AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model)：Google Cloud Blog・英語・確認日 2026-11-04
- [DORA Report Finds AI Is an Amplifier in Software Development, But Trust Remains Low](https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025/)：InfoQ・英語・確認日 2026-11-04
- [Claude Code Gotchas](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)：DoltHub・英語・確認日 2026-11-04
- [Claude Code Tips - 40+ Tips from Basics to Advanced](https://awesomeclaude.ai/claude-code-tips)：Awesome Claude（ykdojo の Claude Code Tips）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)

**次に読む**

- [git worktree で並列にする](../delegate/parallel-with-worktrees.md)
- 退行の原因を git bisect で探させる（準備中）
- リファクタリングと大規模な移行（準備中）
- PR を作り、レビューを受ける（準備中）
- ノート・PKM（Obsidian など）（準備中）

**関連**

- [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)
- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- コミットメッセージ・コメントの言語（準備中）
- [セッションに名前を付けて再開・分岐する](resume-and-branch.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
