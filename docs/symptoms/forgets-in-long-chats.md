---
id: forgets-in-long-chats
title: 長い会話で前提を忘れる・雑になる
aliases: [会話が長いと精度が落ちる, 前提を忘れる, context rot]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 130
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 長い会話で前提を忘れ、答えが雑になる原因を、会話に溜まった無関係な情報から切り分け、新しい会話・引き継ぎ・委任のどれで片付けるかを決める。
signs:
  - {type: symptom, text: 会話が長くなると精度が落ちる}
  - {type: symptom, text: 最初に伝えた前提を途中から忘れる}
  - {type: symptom, text: 大量のログやテスト出力で会話が埋まっていく}
wave: 1
prerequisites: [context-rot]
related: [rereads-whole-history, attention-budget, rewind-dont-correct, research-in-subagents, hook-recipes#filter-test-output, inspect-context, large-context-window, compact-and-auto-compact, going-in-circles, forgot-after-compaction, unexpected-memories, seems-less-capable, skipped-later-pages, six-causes]
routes:
  - {cause: 見えていない, to: [handoff-documents, long-chat-limits]}
  - {cause: 散らかっている, to: [when-to-start-fresh, tidy-the-desk, choose-what-to-read#trim-output]}
tracks: [context-window, compaction, clear]
outdated_advice: [save-context-for-200k, subagents-to-save-context]
sources: [cc-docs-how-claude-code-works, cc-docs-best-practices, cc-docs-large-codebases, cc-docs-context-window]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 似た症状との見分け, anchor: lookalikes}
  - {title: 判断例, anchor: example}
  - {title: 古い助言に引きずられない, anchor: outdated}
  - {title: 予防：前提を会話の外に置く, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：長い会話で前提を忘れ、雑になる原因を「前提が見えていない」か「無関係な情報で散らかっている」かに切り分け、片付け方を決められる。
    - **いつ引くか**：会話が長くなると精度が落ちる・最初に伝えた前提を途中から忘れる・大量のログやテスト出力で会話が埋まっていく、とき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：会話が長いと精度が落ちる・前提を忘れる・context rot
<!-- textlint-enable -->

長い会話で前提を忘れる・雑になる症状は、会話を重ねるうちに、最初に伝えた条件が答えに効かなくなることである。Claude 側の原因は大きく 2 通りある。条件が Claude の目の前から落ちている場合と、目の前にはあるが無関係な情報に埋もれている場合である。条件が文面に渡っていない人の側の原因も、同じ見た目で現れる。

どちらも、返答の文面だけでは区別しにくい。このページは、安く確かめられる順に原因を切り分け、新しい会話・引き継ぎ・出力の絞り込み・委任のどれで片付けるかを選ぶところまでを受け持つ。

## よくある形 {#forms}

読者の言葉で現れる形は、次の 3 つに分けると見分けやすい。

- **後半になるほど精度が落ちる**：始めのうちは的確だったのに、会話が進むと、的外れな答えや矛盾した答えが増える。
- **最初の前提を忘れる**：「この言語で」「このファイルは触らない」と最初に伝えたのに、途中から守られない。
- **ログやテスト出力で会話が埋まる**：長い実行結果を何度も貼る、または読ませるうちに、肝心の指示が埋もれて答えが雑になる。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。最初に、「どの前提が、いつ頃から効かなくなったか」を 1 つ特定する。特定できないと、以下の確認が当てられない。

1. **見えていない**：その前提が、会話の中から落ちている。
    - 見るもの：前提を伝えた発言が、まだ会話に残っているか。圧縮や要約が起きていないか。
    - 確かめ方：今把握している目的・完了の条件・前提を列挙させ、自分が最初に伝えた文面と照らす。列挙に出てこない、または言い換わっているなら、その前提は見えていない。依頼の雛形はこの節の末尾にある。
    - 圧縮の背景：圧縮は、会話の履歴を要約に置き換える。自動で圧縮されると初めの指示は失われうるので、続けて効かせたい規則は CLAUDE.md に置くのが公式の勧めである。何が圧縮の後に残るかは仕組みごとに違い、公式の表が正である。圧縮の起き方と備えは <!-- link:begin compact-and-auto-compact#auto-compact -->[/compact と自動圧縮 › 自動圧縮で起きること](../context/compact-and-auto-compact.md#auto-compact)<!-- link:end --> にある。
    - 圧縮の後に、決めた約束や禁止を忘れた場合は、<!-- link:begin forgot-after-compaction#diagnosis -->[圧縮の後に約束を忘れた › 原因を安く確かめる順](forgot-after-compaction.md#diagnosis)<!-- link:end --> に進む。
2. **散らかっている**：前提は残っているが、無関係な情報や失敗の跡が増え、効きにくくなっている。
    - 見るもの：会話に、話題の違う作業が混ざっていないか。失敗した試みや、長い実行結果が残っていないか。
    - 確かめ方：いまの依頼に要る前提と資料だけを書き出して新しい会話に入れ、同じ依頼を出す。答えがよくなるなら、散らかりが原因である。
    - 理屈：関係のない情報が増えるほど、大事な情報への注意が薄くなる。<!-- link:begin attention-budget#why -->[コンテキストウィンドウと注意の予算 › 広い机でも一枚ごとの目配りは薄くなる](../basics/attention-budget.md#why)<!-- link:end --> に詳しい。失敗した試みが会話に残ると紛らわしい情報になるのも同じ理屈で、前提の <!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> が扱っている。
    - 大きなコードベースでも、関係のない指示や読み込みがコンテキストウィンドウを埋めると、トークンを使い、性能も落ちると公式は書く。
3. **人の側**：前提が、そもそも会話の文面に明示されていない、または途中の指示と食い違っている。
    - 見るもの：最初の前提が、実際の文章として書かれているか。後から出した指示と食い違っていないか。
    - 確かめ方：前提を伝えた発言を自分で読み返し、のちの指示と並べる。書いていなかった、または訂正を重ねて前提が変わっていたなら、Claude が忘れたのではなく、一貫した前提が渡っていない。人の側の落とし穴は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にある。

何が会話の場所を取っているかは、面によって見方が違う。

=== "アプリ"

    長い会話の上限が近づくと、自動で要約されるなどの管理が働く。何が要約され何が残るかは <!-- link:begin long-chat-limits#auto-management -->長い会話の自動のコンテキスト管理と長さの上限 › 上限が近づくと何が起きるか（準備中）<!-- link:end --> にある。前提が落ちたと思うときは、まず列挙の依頼で確かめる。

=== "Claude Code"

    `/context` で、会話・読み込んだファイル・常駐するもののどれが場所を取っているかを見分ける。見方は <!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end --> にある。起動直後の値を控えておくと、増えた分が分かる。

=== "API"

    会話の履歴は、呼び出す側のコードが毎回送る。送る内容が Claude に見える全てなので、自分のコードが古いメッセージを切り詰めていないか、同じ内容を重ねて送っていないかを、実際に送った内容で確かめる。毎回全履歴を読み直す仕組みは <!-- link:begin rereads-whole-history#what-happens -->[毎ターン全履歴を読み直す › 何が起きるか](../basics/rereads-whole-history.md#what-happens)<!-- link:end --> にある。

列挙させる依頼の雛形を、次に置く。長くなった会話の途中で、作業の続きを頼む前に使う。

<!-- gen:begin snippet forgets-in-long-chats/premises-check -->
<!-- textlint-disable -->

??? example "雛形：今把握している前提を列挙させる依頼"

    ```text
    作業を続ける前に、今の会話の状態を確認させて。

    1. この作業の目的と、完了の条件を、あなたが今把握している形で書く。
    2. 私が最初に伝えた前提や制約（使う言語、触ってはいけない場所、守る書式など）を、1 つずつ列挙する。
    3. 会話の途中で変わった前提があれば、変わった後の形で書く。
    4. 前提のうち、会話の中で確認できず、推測で補っているものがあれば、そう書く。

    作業はまだ進めず、この確認だけ返して。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 0.2.47。

<!-- textlint-enable -->
<!-- gen:end snippet forgets-in-long-chats/premises-check -->

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持ち、対処の本体は書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [handoff 文書と document-and-clear](../context/handoff-documents.md)<br>長い会話の自動のコンテキスト管理と長さの上限（準備中） |
| 散らかっている | [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[机を整える：新鮮さ・巻き戻し・書き出し・委任](../context/tidy-the-desk.md)<br>[@参照と、何を読ませるかの絞り込み › 出力を絞る](../context/choose-what-to-read.md#trim-output) |

<!-- textlint-enable -->
<!-- gen:end routes -->

ログやテストの出力で埋まる場合は、散らかっている側の対処のうち、出力を要点に絞ってから会話に入れる手が中心になる。同じ絞り込みをフックで仕組みにする手は <!-- link:begin hook-recipes#filter-test-output -->[代表的なフックのレシピ › テストの出力を絞る](../enforce/hook-recipes.md#filter-test-output)<!-- link:end --> にある。出力の多い調査を本筋から離す手は <!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](../context/research-in-subagents.md#when)<!-- link:end --> にある。

## 似た症状との見分け {#lookalikes}

長い会話で起きる症状には、ほかにも似たものがある。次のように見分ける。

- 同じ失敗を何度も繰り返す：<!-- link:begin going-in-circles#diagnosis -->[同じ失敗を繰り返す（堂々巡り） › 原因を安く確かめる順](going-in-circles.md#diagnosis)<!-- link:end --> で、会話に残った失敗の跡から切り分ける。
- 圧縮の後に、決めた約束を忘れた：<!-- link:begin forgot-after-compaction#diagnosis -->[圧縮の後に約束を忘れた › 原因を安く確かめる順](forgot-after-compaction.md#diagnosis)<!-- link:end --> で、約束が圧縮で残る場所にあるかを確かめる。
- 別の会話やプロジェクトの内容が混ざる：<!-- link:begin unexpected-memories#diagnosis -->[別の会話やプロジェクトの内容が混ざる › 原因を安く確かめる順](unexpected-memories.md#diagnosis)<!-- link:end --> で、どの記憶の仕組みかを切り分ける。
- 急に賢くなくなった気がする：<!-- link:begin seems-less-capable#diagnosis -->[急に賢くなくなった気がする › 原因を安く確かめる順](seems-less-capable.md#diagnosis)<!-- link:end --> で、版・effort・モデル・会話の量の順に確かめる。
- 添付した資料の後半が使われない：<!-- link:begin skipped-later-pages#diagnosis -->[添付した資料の後半を読んでいない › 原因を安く確かめる順](skipped-later-pages.md#diagnosis)<!-- link:end --> で、読み込みの範囲と注意の偏りを切り分ける。
- どの原因から疑うか迷う：<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> が、Claude 側の 6 つの原因を安く確かめる順に並べている。

## 判断例 {#example}

!!! example "判断例：テスト出力が溜まった会話で前提が守られない"
    - **状況**：バグ修正の会話で、テストを何度も流し、長い出力を貼り続けた。最初に伝えた「既存の公開関数の名前は変えない」が、途中から守られなくなった。前提を列挙させると、この前提は列挙に出た。
    - **迷う候補**：A は、前提をもう一度強い言葉で書き足し、そのまま同じ会話で続ける。B は、前提と現状の要点だけを書き出して新しい会話で続け、以後のテスト出力は失敗した箇所の数行に絞ってから渡す。
    - **選んだもの**：B。
    - **理由**：前提は残っていたが、長い出力の中で効きにくくなっていた。A は、散らかりを残したまま、重ねた一言がまた埋もれる。B は、焦点の合った文脈で始め直せ、出力を絞れば同じ散らかり方を繰り返さない。列挙にも前提が出なかったなら、原因は見えていないであり、書き出した要点に前提を入れて始める点は同じである。

## 古い助言に引きずられない {#outdated}

長い会話の対処には、コンテキストウィンドウ（以下、窓）が小さかったころの助言が残っている。このページの判断は、次の 2 つの台帳の行と合わせて読む。

- 「窓を最優先で節約する」という助言は、条件付きになった。溢れることはまれになったが、関係のない作業に移るときの新しい会話は、質と費用のために今も勧められる。今の扱いは <!-- link:begin outdated-advice-ledger#save-context-for-200k -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#save-context-for-200k)<!-- link:end --> にある。
- 「コンテキストを守るためのサブエージェント」という助言も、条件付きである。出力の多い調査を本筋から離す委任はよいが、守る目的だけでは使わない。今の扱いは <!-- link:begin outdated-advice-ledger#subagents-to-save-context -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagents-to-save-context)<!-- link:end --> にある。

窓の広さと注意の関係は <!-- link:begin large-context-window#what-to-keep -->広いコンテキストウィンドウとの付き合い方 › 続けること（準備中）<!-- link:end --> にある。窓が広くなっても、関係のない文脈が答えの質と費用を下げる点は変わらない。

## 予防：前提を会話の外に置く {#prevention}

予防の考え方は、会話の履歴に頼らず、守らせたい前提を会話の外か、残る場所に置くことである。

- 話題が変わったら、会話を新しくする。合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
- 長い作業は、目的・今の状態・試して駄目だったこと・次の一手を文書にして引き継ぐ。書かせる項目は <!-- link:begin handoff-documents#four-items -->[handoff 文書と document-and-clear › 書かせる四項目](../context/handoff-documents.md#four-items)<!-- link:end --> にある。
- 続けて効かせたい規則は、CLAUDE.md など、圧縮で消えない場所に置く。置き場所は <!-- link:begin handoff-documents#where -->[handoff 文書と document-and-clear › 置き場所（圧縮で消えない所）](../context/handoff-documents.md#where)<!-- link:end --> にある。
- 長い出力は、要点の数行に絞ってから会話に入れる。出力の多い調査は、本筋から離して任せる。
- 期待と違う返答には、訂正を重ねるより巻き戻す。理由は <!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end --> にある。
- 作業の節目に、今把握している前提を列挙させて、ずれを早めに見つける。
- 例外を許さない禁止は、会話の文面に頼らず、deny ルールかフックで縛る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Set up Claude Code in a monorepo or large codebase](https://code.claude.com/docs/en/large-codebases)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- 長い会話の自動のコンテキスト管理と長さの上限（準備中）
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任](../context/tidy-the-desk.md)
- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)

**関連**

- [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [代表的なフックのレシピ › テストの出力を絞る](../enforce/hook-recipes.md#filter-test-output)
- [/context で中身を見る](../context/inspect-context.md)
- 広いコンテキストウィンドウとの付き合い方（準備中）
- [/compact と自動圧縮](../context/compact-and-auto-compact.md)
- [同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)
- [圧縮の後に約束を忘れた](forgot-after-compaction.md)
- [別の会話やプロジェクトの内容が混ざる](unexpected-memories.md)
- [急に賢くなくなった気がする](seems-less-capable.md)
- [添付した資料の後半を読んでいない](skipped-later-pages.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
