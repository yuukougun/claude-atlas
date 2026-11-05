---
id: ask-claude-code
title: Claude Code 自身に聞く
aliases: [使い方を Claude に聞く, /powerup, Claude Code のヘルプ]
type: concept
field: cli
chapter: 入力と基本の操作
order: 30
level: 使う
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発, 学習]
summary: Claude Code の機能や設定の使い方を Claude Code 自身に聞くと、公式の文書を調べて答える。答えは手元の版より新しい機能を含みうるので、版を確かめてから使う。
signs:
  - {type: goal, text: フックの書き方などを、その場で調べたい}
  - {type: symptom, text: Claude Code に教わった機能や設定が、手元の版にない}
prerequisites: [input-symbols]
related: [checking-for-updates, dating-information, outdated-advice-ledger, insights-and-usage-review, command-cheatsheet]
tracks: []
outdated_advice: []
sources: [cc-docs-common-workflows, cc-docs-how-claude-code-works, cc-docs-settings-reference]
volatility: 中
sections:
  - {title: 何を聞けるか, anchor: what-to-ask}
  - {title: 答えが手元の版より新しくなる理由, anchor: why-newer}
  - {title: 答えの版を確かめる, anchor: check-version}
  - {title: 何に効くか, anchor: what-it-helps}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：Claude Code に機能や設定の使い方を聞くと、公式の文書を調べて答える。答えは手元の版より新しいことがある。
    - **いつ引くか**：フックの書き方などをその場で調べたいとき。教わった機能や設定が手元の版にないとき。
    - **前提**：<!-- link:begin input-symbols -->[入力の記号（/ ! @）と Esc](input-symbols.md)<!-- link:end -->

<!-- textlint-disable -->
別名：使い方を Claude に聞く・/powerup・Claude Code のヘルプ
<!-- textlint-enable -->

Claude Code 自身に聞くとは、Claude Code の機能や設定の使い方を、起動中の Claude Code にそのまま質問することである。公式の文書は、使い方を聞けば Claude が最新の文書を調べて答えるとしている。その答えは、いま動いている版に限られない。便利な反面、手元の版にまだない機能が答えに混じることがある。

## 何を聞けるか {#what-to-ask}

聞けるのは、Claude Code 自身の機能と設定の使い方である。公式の文書は、例として「hooks はどう設定するのか」という質問を挙げている。ほかにも、スキルやサブエージェントの作り方、設定ファイルの置き場所、コマンドの意味など、公式の文書に書かれているものを聞ける。実演を見たいときは `/powerup` がある（公式の文書が実演の入口として挙げている）。

同じ質問でも、聞き方で答えの使いやすさが変わる。次は同じ依頼の Before と After である。

```text
# Before
hooks って何？

# After
.env を編集しようとしたら止めたい。hooks でできるか、公式の文書を調べて答えて。
設定ファイルのどこに何を書くかと、使った文書の URL と、必要な版も添えて。
```

After で足したのは 3 つある。やりたいことを成果で書いた。調べた元の URL を求めた。必要な版を求めた。URL があれば、答えが文書に基づくかを自分で開いて確かめられる。必要な版があれば、手元で動くかをその場で照らせる。

!!! example "判断例：初めてフックを設定する"
    - **状況**：フックを初めて設定する。公式の文書は長く、どの節を読めばよいか分からない。
    - **迷う候補**：公式の文書を頭から自分で読む。Claude Code に聞いて、返ってきた手順で進める。
    - **選んだもの**：Claude Code に聞く。ただし文書の URL と必要な版を添えさせ、設定を書く前に URL を開いて該当の箇所を自分の目で確かめる。
    - **理由**：自分の目的に絞った手順が早く手に入る。一方で、答えの出どころが分からないまま設定に写すと、手元の版にない書き方を持ち込みかねない。

## 答えが手元の版より新しくなる理由 {#why-newer}

Claude Code に使い方を聞くと、Claude は最新の文書を調べて答える。調べる先は、いま動いている版の文書に限られない。つまり答えは、手元の版ではなく、公開されている最新の文書に沿う。

一方で、手元の版は最新より遅れることがある。公式の文書によると、更新の経路（`autoUpdatesChannel`）の stable は、ふつう少し前の版を指し、大きな退行のある版を飛ばす。stable を使う人の手元には、最新の版で入った変更がまだない。

この差が、教わった機能や設定が手元の版にない、という症状を生む。聞いた相手が間違ったのではなく、答えと手元で参照している版がずれている。

## 答えの版を確かめる {#check-version}

答えを設定や作業で使う前に、次の順で確かめる。

1. 手元の版を見る。セッションの中で `!claude --version` と打てば、結果が会話に入る（入力の記号の `!` は <!-- link:begin input-symbols#bang -->[入力の記号（/ ! @）と Esc › ! シェルを自分で走らせる](input-symbols.md#bang)<!-- link:end --> にある）。
2. 答えに、その機能が入った版か、必要な版を書かせる。書かれていなければ、文書のどこにあるかを聞き返す。
3. 手元の版が足りないか、答えから版が読み取れないときは、変更履歴で確かめる。記録の在り処は <!-- link:begin checking-for-updates#where-records-live -->[最新を自分で確かめる方法 › 変更の記録の在り処](../changes/checking-for-updates.md#where-records-live)<!-- link:end --> に、手順は <!-- link:begin checking-for-updates#steps -->[最新を自分で確かめる方法 › 手順](../changes/checking-for-updates.md#steps)<!-- link:end --> にある。
4. 使う前に、新しいセッションで小さく試す。設定に写すときは、差分を自分の目で見てから確定する。

手元の版にない機能だったときの選択肢は 2 つある。更新して使うか、手元の版で通じる別の書き方を探すかである。更新できるか、チームで版を固定しているかは環境で決まる。更新の見分け方と失敗したときの扱いは <!-- link:begin checking-for-updates -->[最新を自分で確かめる方法](../changes/checking-for-updates.md)<!-- link:end --> に任せる。

!!! example "判断例：教わった設定が手元で動かない"
    - **状況**：Claude Code に教わった設定を書いたが、手元では効かない。
    - **迷う候補**：書き方を疑って直し続ける。手元の版が足りないと見て、版を調べる。
    - **選んだもの**：先に手元の版と、答えにあった必要な版を比べる。
    - **理由**：書き方の間違いは文書と見比べれば分かるが、版が足りないときは書き方をいくら直しても効かない。比べるのが安く、原因を二分できる。

## 何に効くか {#what-it-helps}

このページが関わる原理は「見せる」、防ぐ原因は「見えていない」である。

「見えていない」は、Claude が答えに要る情報を、その時点で見ていない状態を指す。Claude Code の機能は頻繁に変わるので、モデルが覚えている知識は、最新の文書とずれうる。「見せる」は、見えていない情報を会話に入れて、Claude の目の前に置くことである。文書を調べさせるのは、まさにこれにあたる。最新の文書が会話に入るので、記憶に頼るより古い書き方が混じりにくい（推論・実践例なし）。

効く範囲は、公式の文書に書かれていることまでである。文書にない内部の動きや、自分の環境の事情は、文書を調べても出てこない。また、答えが新しい文書に基づくほど、手元の版とのずれは大きくなりうる。このずれは、手元の版と答えにある必要な版を比べて埋める。

助言が古くなる速さと見分け方は <!-- link:begin dating-information#layers -->[いつの情報かを見分ける › 古くなる速さの三つの層](../changes/dating-information.md#layers)<!-- link:end --> に、古くなった助言の一覧は <!-- link:begin outdated-advice-ledger -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **聞けば手元で動く答えが返る**：返るのは公式の文書に沿った答えで、手元の版で動くとは限らない。版の確認が要る。
- **Claude Code の答えは、記事より常に正しい**：文書を調べた答えは、古い記事より新しいことが多い。ただし、調べずに答えた分は、記憶に頼っている。URL を付けさせて、どちらかを見分ける。
- **聞けば公式の文書を読まずに済む**：重要な設定は、答えの出どころの文書を自分で開いて確かめる。聞くのは、読む箇所を絞るための近道である。

使い方を聞いたあとの振り返りは <!-- link:begin insights-and-usage-review -->[/insights と /usage で振り返る](../eval/insights-and-usage-review.md)<!-- link:end --> に、よく使うコマンドの一覧は <!-- link:begin command-cheatsheet -->[主要コマンド早見表](command-cheatsheet.md)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [入力の記号（/ ! @）と Esc](input-symbols.md)

**関連**

- [最新を自分で確かめる方法](../changes/checking-for-updates.md)
- [いつの情報かを見分ける](../changes/dating-information.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- [/insights と /usage で振り返る](../eval/insights-and-usage-review.md)
- [主要コマンド早見表](command-cheatsheet.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
