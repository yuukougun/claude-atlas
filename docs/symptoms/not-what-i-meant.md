---
id: not-what-i-meant
title: 意図と違うものが出てくる
aliases: [思ったものと違う, 期待外れの答え, 平凡な答えしか出ない]
type: symptom
field: symptoms
chapter: 返答と品質
order: 10
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている, 合っていない]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 頼んだものと違う・平凡なものが出る原因を、伝えた情報の不足から順に切り分け、具体性・手本・質問させるのどれを足すかを決める。
signs:
  - {type: symptom, text: 頼んだものと違うものが出てくる}
  - {type: symptom, text: 「いい感じに」と頼むと平凡なものしか出ない}
  - {type: symptom, text: 回答が長すぎる・短すぎる}
  - {type: symptom, text: 文章が AI っぽい}
wave: 1
prerequisites: []
related: [brief-a-new-colleague, output-shape, spec-first, say-what-you-want, requesting-prose, less-ai-sounding-japanese, refine-in-conversation, build-on-results, suggest-or-do, images-and-voice, does-more-than-asked, repeating-the-same-explanation, inconsistent-japanese-style, six-causes]
routes:
  - {cause: 見えていない, to: [four-specifics, show-examples, let-claude-ask]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh]}
  - {cause: 合っていない, to: [model-quirks, effort-levels]}
tracks: []
outdated_advice: []
sources: [api-docs-prompting-best-practices, cc-docs-best-practices, arxiv-2403-08937]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：頼む前に欠けを見る, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：意図と違う出力の原因を、見えていない・散らかっている・合っていないの順に安く確かめ、足すものを決められる。
    - **いつ引くか**：頼んだものと違うものが出るとき。「いい感じに」と頼むと平凡なものしか出ないとき。回答が長すぎる・短すぎるとき。文章が AI っぽいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：思ったものと違う・期待外れの答え・平凡な答えしか出ない
<!-- textlint-enable -->

意図と違うものが出る原因は、大きく 3 つに分かれる。Claude に渡した情報が足りない、会話の中の外れた試みが次の答えを引きずる、モデルや effort の選び方が作業に合っていない、である。このページは、手間の小さい確かめから順に原因を切り分ける。決めるのは、依頼に足すもの、会話を新しくするか、モデルや effort を変えるかである。

## よくある形 {#forms}

困りごとの言い方ごとに、先に疑う原因と、このページで受けるかどうかを添える。

- **頼んだものと違うものが出てくる**：対象のファイルや範囲の取り違え、仕様の読み違え、書かれていない境界の入力の見落としが典型である。先に「見えていない」を疑う。
- **「いい感じに」と頼むと平凡なものしか出ない**：形容詞だけでは、どこにでもある無難な答えに落ち着きやすい。好みや基準が Claude に見えていないので、先に「見えていない」を疑う。
- **回答が長すぎる・短すぎる**：形と分量を指定していないなら「見えていない」である。指定したのに外れるなら「合っていない」を疑う。指定の仕方は「<!-- link:begin output-shape#length -->出力の形と分量を指定する › 長さと要約の有無（準備中）<!-- link:end -->」にある。
- **文章が AI っぽい**：読み手・目的・手本を渡していないことが多い。先に「見えていない」を疑う。頼み方は「<!-- link:begin requesting-prose -->文章を頼むとき（読み手・目的・手本を渡す）（準備中）<!-- link:end -->」、直し方は「<!-- link:begin less-ai-sounding-japanese -->日本語の「AI 臭さ」を減らす（準備中）<!-- link:end -->」にある。です・ますの混在や表記ゆれは、別の原因なので「<!-- link:begin inconsistent-japanese-style -->[文体や表記が揃わない](inconsistent-japanese-style.md)<!-- link:end -->」で受ける。

近い症状は、次のページが受ける。

- 頼んでいない機能やファイルが増えるなら、「<!-- link:begin does-more-than-asked -->[頼んでいないことまでやる（過剰設計）](does-more-than-asked.md)<!-- link:end -->」。
- 提案だけで止まる、または勝手に実行されるなら、「<!-- link:begin suggest-or-do -->[提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)<!-- link:end -->」。
- 毎回同じ背景を説明しているなら、「<!-- link:begin repeating-the-same-explanation -->[毎回同じ説明をしている](repeating-the-same-explanation.md)<!-- link:end -->」を見る。

コード生成の不具合を分類した研究（[Tambon ほか、2024 年](https://arxiv.org/abs/2403.08937)）では、仕様の誤解釈とコーナーケースの漏れが上位の類型だった（根拠：中。旧世代のモデルの結果で、現行の Claude の傾向ではない）。ずれが起きる仕組みは <!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)<!-- link:end --> にある。

## 原因を安く確かめる順 {#diagnosis}

外れた出力を 1 つ選び、その依頼文、外れた所、その会話で訂正を何回したかを控える。上から順に確かめる。上の原因ほど、確かめる手間が小さい。各項目で直したら、新しい会話で同じ依頼を出し、意図に近づいたかを見る。

1. **見えていない**：意図の一部が、依頼の中に書かれていない。書かれていない点は、Claude の推測で埋まる。その推測が外れた所は、意図と違う所になる。

    - 依頼文を、事情を知らない同僚に見せて迷うかを確かめる。迷う所は、Claude も迷う所である。見せ方は「<!-- link:begin brief-a-new-colleague#colleague-test -->[新人の同僚に頼むつもりで › 文脈のない同僚に見せて確かめる](../prompting/brief-a-new-colleague.md#colleague-test)<!-- link:end -->」にある。
    - 外れ方から、欠けている点を探す。対象のファイルや画面、症状と再現の手順、何が起きれば終わりか、倣う既存の手本のどれが書かれていないかを見る。探し方は「<!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](../prompting/four-specifics.md#which-to-add)<!-- link:end -->」にある。対象・状況・完了・手本を書くという助言は、公式の [Best practices](https://code.claude.com/docs/en/best-practices) にある。
    - 手元で最も安いのは、Claude に推測した点を挙げさせることである。下の 2 つの依頼のどちらかを使う。挙がった推測のうち、意図と違うものが、次に足す情報である。
    - 平凡な答えが出るときは、形容詞で頼んでいないかを見る。好みを言葉にしにくいときは、自分の過去の文章や既存のコードを手本に見せる。選び方は「<!-- link:begin show-examples#own-writing -->[例を見せる › 自分の文章を手本にする](../prompting/show-examples.md#own-writing)<!-- link:end -->」にある。画面やエラーは、画像で渡すほうが速いこともある（<!-- link:begin images-and-voice#images -->[画像・スクリーンショット・音声で渡す › 画像で渡すと速いもの](../prompting/images-and-voice.md#images)<!-- link:end -->）。
    - 要件が自分でも固まっていないなら、依頼文を磨く前に、Claude に質問させる。頼み方は「<!-- link:begin let-claude-ask#how -->[質問させる・インタビューさせる › 質問させる頼み方](../prompting/let-claude-ask.md#how)<!-- link:end -->」にある。大きな機能は、仕様を先に固める進め方を「<!-- link:begin spec-first#interview -->[仕様を先に固める（spec・インタビュー・モック先行） › インタビューで仕様を詰める](../recipes/spec-first.md#interview)<!-- link:end -->」で見る。

2. **散らかっている**：依頼は足りているのに、同じ会話の中の外れた試みや、積み重ねた訂正が、次の答えを引きずる。

    - この会話で訂正を 2 回以上重ねたか、話題が途中で変わったかを見る。当てはまれば、疑う。
    - 確かめ方は、同じ依頼を新しい会話にそのまま出すことである。直れば、原因は会話の中にある。直らなければ、1 に戻る。新しくする合図は「<!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end -->」、新しくする前に残すものは「<!-- link:begin when-to-start-fresh#before-clearing -->[新しい会話を始めるタイミング › 新しくする前に残すもの](../context/when-to-start-fresh.md#before-clearing)<!-- link:end -->」にある。
    - 会話を続けたいなら、訂正を重ねる代わりに、前のメッセージを直して送り直す。理由は「<!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end -->」にある。

3. **合っていない**：依頼が足りていて、会話も新しいのに外れる。モデルの傾向や effort が作業に合っていない。

    - 止まりすぎ・やりすぎ・冗長さのように、モデルごとに出やすい傾向がある。傾向は版で変わるので、公式の指針で傾向を知り、自分の環境で観察して記録する。進め方は「<!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end -->」にある。
    - effort は、考える深さと、待ち時間や使用量の釣り合いを変える。既定の段は面とモデルで違うので、先に今の段を確かめる。確かめ方は「<!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end -->」、変え方は「<!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](../models/effort-levels.md#how-to-set)<!-- link:end -->」にある。
    - 確かめ方は、同じ依頼を新しい会話で出し、モデルか effort のどちらか 1 つだけを変えて比べることである。2 つ同時に変えると、どちらが効いたか分からない。

1 から 3 のどれを直しても外れるときは、人の側の落とし穴を疑う。診断の入口は「<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end -->」、人の側の落とし穴は「<!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end -->」にある。

1 の確かめに使う依頼を 2 つ置く。1 つ目は、実行の前に使う。2 つ目は、外れた出力の直後に使う。

<!-- gen:begin snippet not-what-i-meant/restate-first -->
<!-- textlint-disable -->

??? example "雛形：実行の前に、理解と推測した点を書き出させる依頼"

    ```text
    次の依頼を、まだ実行しないでください。
    先に、あなたの理解を次の 4 つで書き出してください。

    1. 対象：どのファイル・画面・文書を変える（作る）と理解したか
    2. 完了：何が起きれば終わりだと理解したか
    3. 推測した点：依頼に書かれておらず、あなたが推測で決めた点
    4. 確かめたい点：分からないので、私に聞きたい点

    私が「進めて」と返したら、実行してください。

    依頼：
    <ここに、実際の依頼を書く>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet not-what-i-meant/restate-first -->

<!-- gen:begin snippet not-what-i-meant/list-assumptions -->
<!-- textlint-disable -->

??? example "雛形：外れた出力のあとで、推測で埋めた点を挙げさせる依頼"

    ```text
    今の出力は、私の意図と違っていました。
    作り直す前に、この出力を作るときに、依頼に書かれていないため推測で決めた点を、すべて箇条書きにしてください。
    各点に、何を選んだか、ほかにどんな選び方があったかを 1 行で添えてください。
    まだ作り直さないでください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet not-what-i-meant/list-assumptions -->

原因が分かったら、次の表の先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)<br>[例を見せる](../prompting/show-examples.md)<br>[質問させる・インタビューさせる](../prompting/let-claude-ask.md) |
| 散らかっている | [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)<br>[新しい会話を始めるタイミング](../context/when-to-start-fresh.md) |
| 合っていない | モデル別の癖と、プロンプトの合わせ方（準備中）<br>[effort の段階と使い分け](../models/effort-levels.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：「いい感じに」で平凡なものが出る"
    - **状況**：「いい感じの紹介文にして」と頼むと、どこにでもある無難な文章が出た。もっと自分らしくしたい。
    - **迷う候補**：「もっとおしゃれに」と形容詞を足して頼み直す。自分の過去の紹介文を手本に見せる。先に質問させて好みを洗い出す。
    - **選んだもの**：先に推測した点を挙げさせて、何が見えていないかを確かめる。そのうえで、自分の過去の紹介文を手本に見せて頼み直す。
    - **理由**：形容詞は基準を渡さないので、足しても無難な答えに戻りやすい。手本は、言葉にしにくい好みまで伝わる。好みを言葉にできないときは、質問させる手が残る。

!!! example "判断例：訂正を 3 回重ねても直らない"
    - **状況**：画面の改修を頼んだが、対象の画面が違った。「違う、こっちの画面だ」と 3 回訂正したが、まだ別の所を直す。
    - **迷う候補**：4 回目の訂正を足す。effort を上げる。最初の依頼を直して、新しい会話で出し直す。
    - **選んだもの**：最初の依頼に、対象の画面と、直ったと分かる状態を書き足し、新しい会話で出し直す。
    - **理由**：外れた試みと訂正が会話に残ると、次の答えがそれに引きずられる。依頼の不足と会話の散らかりは、effort を上げる前に直せる。出し直して直らなければ、そのときに effort やモデルを疑う。

## 予防：頼む前に欠けを見る {#prevention}

意図と違うものを減らす手は、出力を見てから直すより、頼む前に欠けを見ることである。次の 3 つを習慣にする。

- 頼む前に、対象・状況・完了・手本のどれが欠けているかを見る。書き方の雛形は「<!-- link:begin four-specifics#templates -->[具体性の 4 点（対象・状況・完了・手本） › 4 点を書く雛形](../prompting/four-specifics.md#templates)<!-- link:end -->」にある。
- 毎回同じ背景を書いているなら、依頼ごとに書かず、置き場所に移す。移し方は「<!-- link:begin repeating-the-same-explanation -->[毎回同じ説明をしている](repeating-the-same-explanation.md)<!-- link:end -->」にある。
- 例外を許さない決まり（このファイルは触らない、など）は、頼み方を磨かず、仕組みに移す。考え方は「<!-- link:begin say-what-you-want#two-layers -->[否定形ではなく、望む形で書く › 例外のない禁止は仕組みへ（二層）](../prompting/say-what-you-want.md#two-layers)<!-- link:end -->」にある。

最初から完璧な依頼を作らなくてよい。最初は平易に頼み、返事を見て足りない所だけを足す。進め方は「<!-- link:begin refine-in-conversation#start-plain -->頼み方は一回で決めない（会話で詰める） › まず平易に頼み、足りない分を足す（準備中）<!-- link:end -->」にある。良くなったかは、前回の結果と見比べて確かめる。毎回一から作り直させず、前回の結果を踏まえて直させる進め方は「<!-- link:begin build-on-results#regenerate-or-refine -->やり直させるより、結果を踏まえて直させる › 作り直しと直しの違い（準備中）<!-- link:end -->」にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Bugs in Large Language Models Generated Code: An Empirical Study](https://arxiv.org/abs/2403.08937)：arXiv（Tambon, Florian ほか）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- [例を見せる](../prompting/show-examples.md)
- [質問させる・インタビューさせる](../prompting/let-claude-ask.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- モデル別の癖と、プロンプトの合わせ方（準備中）
- [effort の段階と使い分け](../models/effort-levels.md)

**関連**

- [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- 出力の形と分量を指定する（準備中）
- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)
- [否定形ではなく、望む形で書く](../prompting/say-what-you-want.md)
- 文章を頼むとき（読み手・目的・手本を渡す）（準備中）
- 日本語の「AI 臭さ」を減らす（準備中）
- 頼み方は一回で決めない（会話で詰める）（準備中）
- やり直させるより、結果を踏まえて直させる（準備中）
- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- [画像・スクリーンショット・音声で渡す](../prompting/images-and-voice.md)
- [頼んでいないことまでやる（過剰設計）](does-more-than-asked.md)
- [毎回同じ説明をしている](repeating-the-same-explanation.md)
- [文体や表記が揃わない](inconsistent-japanese-style.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
