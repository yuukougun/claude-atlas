---
id: skill-descriptions
title: スキルの description の書き方
aliases: [スキルの説明文, when_to_use, スキルが使われない]
type: feature
field: extend
chapter: スキル
order: 120
level: 仕組みにする
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: スキルが使われない・余計に使われるときに、説明文を直して起動を合わせられる。いつ使うかを先頭に具体的に書き、ほかのスキルと重ならないようにする。
signs:
  - {type: goal, text: 作ったスキルを、使ってほしい場面で確実に使わせたい}
  - {type: symptom, text: 関係のない場面で、別の手順が勝手に読み込まれる}
prerequisites: [writing-skills]
related: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents, skills-in-the-app, hook-vs-skill, instructions-ignored]
tracks: [skills]
sources: [cc-docs-skills, cc-docs-features-overview, hc-skills-use, api-docs-skill-best-practices]
volatility: 中
sections:
  - {title: 使いどころ：説明文が起動を決める, anchor: purpose}
  - {title: 書き直す場所と確かめ方（面ごと）, anchor: usage}
  - {title: いつ使うかを先頭に具体的に書く, anchor: front-load}
  - {title: ほかのスキルと重ならないようにする, anchor: overlap}
  - {title: 起動を確かめる, anchor: check}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古い記事の助言を読むとき, anchor: old-advice}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：スキルが使われない・余計に使われるときに、説明文を直して起動を合わせられる。いつ使うかを先頭に具体的に書き、ほかのスキルと重ならないようにする。
    - **いつ引くか**：作ったスキルを、使ってほしい場面で確実に使わせたいとき。関係のない場面で、別の手順が勝手に読み込まれるとき。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。説明文は Claude が読むかを決める手がかりで、起動を保証しない。確実に動かしたいときは名前で呼ぶ。毎回必ず動かしたい処理はフックにする。違いは「<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->」にある。
    - **前提**：<!-- link:begin writing-skills -->[スキルの作り方](writing-skills.md)<!-- link:end -->

<!-- textlint-disable -->
別名：スキルの説明文・when_to_use・スキルが使われない
<!-- textlint-enable -->

スキルの description の書き方は、スキルが使われる場面と使われない場面を、説明文で合わせる方法である。いつ使うかを先頭に具体的に書き、似たスキルとの境目を説明文に書く。直した後は、スキルが読み込まれるかを、新しいセッションで確かめる。

## 使いどころ：説明文が起動を決める {#purpose}

スキルが防ぐのは、必要な手順が Claude に見えていないことである。その入口になるのが説明文である。スキルの読み込みの時期は「<!-- gen:begin feature load_timing -->セッション開始と使うとき<!-- gen:end feature load_timing -->」で、名前と説明は毎回の会話に載り、本文は呼ばれたときだけ入る。Claude は、依頼の内容と各スキルの説明を見て、どのスキルを読み込むかを決める。本文がどれだけ良くても、説明が依頼と合わなければ読まれない。

説明文の不具合は、2 つの症状に分かれる。

- **使われない**：説明が曖昧で、利用者が使う言葉と結びつかない。説明が一覧の途中で切られている。アプリでは、スキルがオフになっている。
- **余計に使われる**：説明が広すぎる。別のスキルと説明が重なっていて、関係のない場面で選ばれる。

公式の文書は、スキルの説明文が曖昧か重複していると、誤読み込みや未読み込みが起きると説明している。確実に使わせたいときは、`/名前` で呼ぶように勧めている。実践者の間では、スキルの成否は説明文でほぼ決まるとよく言われるが、その割合は測られた値ではなく経験則である（根拠：弱）。

## 書き直す場所と確かめ方（面ごと） {#usage}

説明文を直す場所と、使われないときの最初の確認は、面によって違う。

=== "アプリ"

    - 説明文は、アップロードしたスキルの `SKILL.md` に書いてある。直したら、スキルのフォルダを ZIP にして上げ直す。
    - 公式は、「いつ使うスキルか」が分かる説明を書くように勧めている。Claude は依頼と説明を見て、使うかを決めるためである。
    - 使われないときは、スキルのトグルがオンになっているかを確かめ、依頼でスキルの名前を挙げる。スキルを使うには、code execution が有効になっている必要がある。
    - スキルの設定画面の名前と場所は、展開中で変わっている。今の手順は「<!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end -->」で確かめる。

=== "Claude Code"

    - 説明文は、`SKILL.md` のフロントマターの `description` に書く。`when_to_use` も同じ一覧に載る。
    - 編集は、ライブリロードで反映される。新しいトップレベルのスキルのフォルダを足したときは、`/reload-skills` で読み込み直す。
    - 使われないときは、`/skills` のメニューで、スキルが一覧にあってオフになっていないかを確かめる。急ぐときは、依頼に `/名前` を使って呼ぶ。

どちらの面でも、直した説明が効いたかは、新しいセッションで依頼し直して確かめる。確かめ方は[起動を確かめる](#check)にある。

## いつ使うかを先頭に具体的に書く {#front-load}

説明文で最初に書くのは、いつ使うスキルかである。公式の文書は、説明文を具体的にし、主な用途を先頭に置くように勧めている。先頭に置く理由は、長い説明が切られるからである。Claude Code が一覧に載せる `description` と `when_to_use` の合計は、<!-- fact:begin skill-listing-entry-max-chars -->1536 字で切られる（2026-11-04 時点）<!-- fact:end -->。後ろに書いた条件は、一覧に載らないことがある。アプリと API（Agent Skills の仕様）では、`description` は<!-- fact:begin skill-description-max-chars -->1024 字まで（2026-11-04 時点）<!-- fact:end -->。

この辞典の勧めは、説明文を次の順に書くことである。

1. **いつ使うか**：利用者が頼むときの言葉を入れる。「リリースノートを書いて」のように、依頼の文そのものに近いほどよい。
2. **何をするか**：1 文で足す。手順の中身は本文に書き、説明文には入れない。
3. **使わない場面**：似た別のスキルや作業があるときだけ足す。

`when_to_use` を使う場合も、`description` と合わせて切られる。どちらに何を書くかにかかわらず、主な用途を先頭に置く。

同じスキルで、直す前と直した後を並べる。

<!-- gen:begin snippet skill-descriptions/description-before -->
<!-- textlint-disable -->

??? example "雛形：直す前の description（何をするスキルか分からない）"

    ```markdown
    ---
    name: release-notes
    description: Git の履歴やリリースまわりの作業を手伝う便利なスキル。コミット、タグ、変更点などを扱う。
    ---

    直近のタグから今までの変更を集めて、リリースノートの下書きを作る。

    1. `git describe --tags --abbrev=0` で直近のタグを調べ、そのタグから HEAD までのコミットを `git log` で集める。
    2. コミットを「追加」「変更」「修正」に分け、1 項目を 1 行で書く。
    3. 出力は Markdown の箇条書きだけにする。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet skill-descriptions/description-before -->

<!-- gen:begin snippet skill-descriptions/description-after -->
<!-- textlint-disable -->

??? example "雛形：直した後の description（いつ使うかを先頭に書く）"

    ```markdown
    ---
    name: release-notes
    description: リリースの準備で「リリースノートを書いて」「変更点をまとめて」と頼まれたときに使う。直近のタグから今までのコミットを集めて、製品の利用者向けの下書きにする。コミット履歴の調査やタグ付けそのものには使わない。
    ---

    直近のタグから今までの変更を集めて、リリースノートの下書きを作る。

    1. `git describe --tags --abbrev=0` で直近のタグを調べ、そのタグから HEAD までのコミットを `git log` で集める。
    2. コミットを「追加」「変更」「修正」に分け、1 項目を 1 行で書く。
    3. 出力は Markdown の箇条書きだけにする。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet skill-descriptions/description-after -->

直した後の説明では、3 つを足している。依頼の言葉（「リリースノートを書いて」「変更点をまとめて」）を先頭に置いた。何を作るか（利用者向けの下書き）を 1 文で足した。使わない場面（コミット履歴の調査やタグ付けそのもの）を最後に足した。本文は変えていない。

## ほかのスキルと重ならないようにする {#overlap}

スキルが増えると、同じ依頼に複数のスキルの説明が当てはまる。重なりは、使われない原因にも、余計に使われる原因にもなる。直す手がかりは、どの依頼でどのスキルが読み込まれたかを見ることである。

!!! example "判断例：リリースノートと PR の説明文が、同じ依頼で取り違えられる"
    - **状況**：「変更点をまとめて」と頼むと、リリースノートのスキルではなく PR の説明文のスキルが読み込まれる。どちらの説明にも「変更点」という語がある。
    - **迷う候補**：それぞれの説明文に、使う場面と使わない場面を書いて境目を作る。または、一方を人だけが呼ぶスキルにして、名前で呼ぶ運用にする。
    - **選んだもの**：先に、説明文で境目を作る。リリースノートには「リリースの準備で」と書き、PR の説明文には「PR を作るときに」と書き、互いに使わない場面を足す。
    - **理由**：どちらのスキルも、Claude が自分の判断で使えるほうが便利である。名前で呼ぶ運用は、直した後も取り違えが残る場合の次の手にする。

人だけが呼べるスキルにする方法は、「<!-- link:begin manual-only-skills -->副作用のあるスキルを勝手に動かさない（準備中）<!-- link:end -->」にある。自分で説明文を直せないスキルは、`skillOverrides` で見え方を調整できる。ただし、プラグインで配られるスキルには効かない（「<!-- link:begin writing-skills#evaluate -->[スキルの作り方 › 効いているかを確かめる](writing-skills.md#evaluate)<!-- link:end -->」）。

## 起動を確かめる {#check}

説明文を直したら、依頼を決めて、スキルが読み込まれるかを数える。次の依頼リストは、読み込まれてほしい依頼と、ほしくない依頼を分けて持つ。

<!-- gen:begin snippet skill-descriptions/trigger-check -->
<!-- textlint-disable -->

??? example "雛形：起動の確認用の依頼リスト（読み込まれてほしいものと、ほしくないもの）"

    ```text
    # 読み込まれてほしい依頼（1 件ずつ、新しいセッションで頼む）
    リリースノートを書いて
    v1.2.0 からの変更点を、利用者向けにまとめて
    次のリリースの下書きを作って

    # 読み込まれてほしくない依頼（読み込まれたら説明文を直す）
    この PR の説明文を書いて
    先週のコミットで壊れた箇所を調べて
    タグを付けて push して

    # 名前で呼ぶ（説明文を介さずに呼ぶ）
    /release-notes v1.2.0
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet skill-descriptions/trigger-check -->

使われないときは、安い確認から順に進める。

1. スキルが一覧にあるか、オンになっているかを確かめる。
2. 説明の先頭に、依頼に近い言葉があるかを見る。
3. ほかのスキルの説明と重なっていないかを見る。
4. 説明が長くて切られていないかを見る。
5. それでも動かないときは、`/名前` で呼ぶ。

一度の依頼では判断しない。同じ依頼でも、毎回同じ結果になるとは限らないためである。直す前と後を比べる手順は、「<!-- link:begin measure-changes#compare-skills -->[変更が効いたかを測る（小さな eval） › スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval）](../eval/measure-changes.md#compare-skills)<!-- link:end -->」にある。会話の記録を読むと、どのスキルがいつ読み込まれたかが分かる（「<!-- link:begin measure-changes#read-transcripts -->[変更が効いたかを測る（小さな eval） › transcript を読む](../eval/measure-changes.md#read-transcripts)<!-- link:end -->」）。

## 効かない場面と落とし穴 {#limits}

- **起動を保証しない**：説明文は、お願いである。最善の説明でも、読み込まれない依頼は残る。毎回必ず動かしたい処理は、フックにする。
- **一覧には上限がある**：一覧全体の予算の既定は、<!-- fact:begin skill-listing-budget-fraction -->コンテキストウィンドウの 1%（2026-11-04 時点）<!-- fact:end -->である。予算を超えると、使われていないスキルから説明が落ちる。使われないスキルが、さらに使われにくくなる。スキルの数が増えたら、使っていないものを外す（「<!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](pruning-extensions.md#measure)<!-- link:end -->」）。
- **読み込まれた後に従わないのは別の問題**：説明文は読み込みを決めるだけで、本文の手順に従うかは決めない。手順が守られないときは、本文の書き方を見直す（「<!-- link:begin writing-skills#limits -->[スキルの作り方 › 効かない場面と落とし穴](writing-skills.md#limits)<!-- link:end -->」）。
- **圧縮の後の扱い**：長い会話で圧縮が起きたときに、説明と本文がどうなるかは、「<!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](how-skills-load.md#after-compaction)<!-- link:end -->」にある。
- **長くしても確実にはならない**：説明を長くすれば確実になるわけではない。長くすると切られやすくなり、一覧の予算も使う。

## 比べる相手 {#compare}

- **名前の指定**：`/名前` で呼ぶと、説明文を介さずに動く。確実に使いたいときの手段だが、説明文の直しの代わりにはならない。Claude の自動の起動を減らしたいスキルにも向く。
- **フック**：毎回必ず起きてほしい処理は、スキルの説明文ではなくフックに置く。スキルは Claude が読んで従う手順で、従わせる力はない（「<!-- link:begin hook-vs-skill -->[フックとスキルの違い](hook-vs-skill.md)<!-- link:end -->」）。
- **サブエージェントの説明文**：サブエージェントの `description` も同じ考え方で、いつ使うかを具体的に書く（「<!-- link:begin writing-subagents#when-to-use -->[サブエージェントの作り方と使いどころ › 使いどころと、使わない場面](writing-subagents.md#when-to-use)<!-- link:end -->」）。
- **読み込まれたのに守られない**：説明ではなく指示の側の問題である。切り分けは「<!-- link:begin instructions-ignored -->[CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)<!-- link:end -->」にある。

## 古い記事の助言を読むとき {#old-advice}

スキルの説明文について、台帳に載せる古い助言は今のところない。ただし、記事によって説明文の上限の字数が違うので、読むときは注意がいる。上限を「<!-- fact:begin skill-description-max-chars -->1024 字まで（2026-11-04 時点）<!-- fact:end -->」と書く資料があるが、これはアプリと API の仕様である。Claude Code は、`description` と `when_to_use` の合計を別の長さで切る。字数は変わるので、記事の数字ではなく、このページの [先頭に書く理由](#front-load) の数値で確かめる。記事を読むときは、どの面の話かを先に見る。


<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)：Anthropic・英語・確認日 2026-11-04
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [スキルの作り方](writing-skills.md)

**関連**

- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- 副作用のあるスキルを勝手に動かさない（準備中）
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [拡張の棚卸しと剪定](pruning-extensions.md)
- [サブエージェントの作り方と使いどころ](writing-subagents.md)
- アプリでスキルを使う（準備中）
- [フックとスキルの違い](hook-vs-skill.md)
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
