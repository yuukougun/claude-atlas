---
id: refine-in-conversation
title: 頼み方は一回で決めない（会話で詰める）
aliases: [完璧なプロンプトは要らない, 平易に頼んでから足す, 反復して詰める]
type: concept
field: prompting
chapter: 詰め方と頼み直し
order: 150
level: 使う
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
scenes: [開発, 文章, 調べもの]
summary: 最初は平易に頼み、返事を見て足りない情報だけを足すほうが、完璧な依頼文を先に作るより速い。ずれが大きいときは、訂正を重ねるより元の依頼を直して頼み直す。
signs:
  - {type: symptom, text: 完璧なプロンプトを書こうとして、頼む前に時間がかかる}
  - {type: goal, text: 返事を見ながら、依頼を少しずつ詰めたい}
prerequisites: [brief-a-new-colleague]
related: [rewind-dont-correct, build-on-results, let-claude-ask, going-in-circles, when-to-start-fresh, four-specifics, measure-changes]
sources: [cc-docs-best-practices]
volatility: 低
sections:
  - {title: まず平易に頼み、足りない分を足す, anchor: start-plain}
  - {title: 訂正を重ねるより依頼を直す, anchor: edit-the-request}
  - {title: 良くなったかを確かめる, anchor: check}
  - {title: なぜ返事を見て詰めると効くのか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：返事を見て依頼を詰めるほうが、完璧な依頼文を先に作るより速い。ずれが大きいときは、元の依頼を直して頼み直す
    - **いつ引くか**：完璧なプロンプトを書こうとして、頼む前に時間がかかるとき。返事を見ながら、依頼を少しずつ詰めたいとき
    - **進め方**：平易に頼む。返事で足りない情報を見つけ、その分だけ足す。ずれが大きければ、訂正を重ねずに依頼を直す。足した後は、返事が近づいたかを確かめる
    - **関わる原理と原因**：原理は「見せる」。返事が、Claude に見えていないものを教えてくれる。防ぐ原因は「見えていない」と「散らかっている」である
    - **前提**：<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end -->

<!-- textlint-disable -->
別名：完璧なプロンプトは要らない・平易に頼んでから足す・反復して詰める
<!-- textlint-enable -->

頼み方を一回で決めないとは、最初は平易に頼み、返事を見て足りない情報だけを足し、大きくずれたら元の依頼を直して頼み直すことである。依頼文は、完成させてから送るものではなく、会話の中で詰めていくものとして扱う。

## まず平易に頼み、足りない分を足す {#start-plain}

最初の依頼は平易な一文でよい。Claude Code の公式文書 [Best practices](https://code.claude.com/docs/en/best-practices) は、2026-11-03 に確かめた版で、多くの場合は既定のままで最初の平易な依頼が正しく動くと書く。既定で足りないのは、Claude に見えない情報があるとき、結果を確かめる手段がないとき、例外を許さない規則があるとき、既定の手間やコストが合わないときである。依頼文に全部を先回りして書く必要はなく、足りない分は返事を見てから分かる。

次は、説明のために作った依頼の例で、Claude に試した結果ではない。

**Before**（頼む前に、考えられる条件を全部書こうとする）

```text
ログイン周りのバグを直して。環境は Node 20 で、認証は JWT、リフレッシュトークンは
Cookie にあり、SSO もあり、テストは Jest で、既存の書き方に合わせて、副作用を出さず、
エラー処理も入れて、コメントも足して、あとテストも書いて……
```

**After**（平易に頼み、返事を見て足す）

1. 最初の依頼：「セッションが切れた後に、ログインできなくなる。原因を調べて」
2. 返事を見る：Claude が `src/auth/` を読み、トークン更新の処理を疑った。ただし、再現できるかは確かめず、いきなり直そうとしている。
3. 足す 1 通：「再現するのは SSO でログインしたときだけ。まず再現する失敗テストを書いて、それが通るように直して」

最初の一文は短いが、返事は方向を示した。足した 2 点は、再現の条件（状況）と、終わりの形（完了）である。何を足すかは、返事のずれ方から決める。ずれ方と足す点の対応は <!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](four-specifics.md#which-to-add)<!-- link:end --> にある。

足す 1 通は、次の形にそろえると書きやすい。

<!-- gen:begin snippet refine-in-conversation/follow-up -->
<!-- textlint-disable -->

??? example "雛形：返事を見て足す 1 通"

    ```text
    合っていた点：<返事のうち、そのままでよい所を 1 行>
    ずれた点：<期待と違った所を 1 行。どこを読み違えたかが分かるように>
    足す情報：<対象・状況・完了・手本のうち、足りなかった点だけ>
    次にやること：<次の一手。例：まず再現する失敗テストを書く>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet refine-in-conversation/follow-up -->

この雛形で足すのは、返事を見て足りないと分かった点だけである。合っていた所を先に書くと、直さなくてよい所を Claude が触りにくくなる。

## 訂正を重ねるより依頼を直す {#edit-the-request}

返事が大きくずれたときは、「違う」と返して訂正を重ねるより、元の依頼を直して頼み直す。理由と操作は <!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end --> が持つ。この辞典では、本体をそこに置いている。

見分け方は、ずれの大きさである。次の判断例で、足すか直すかの分かれ目を示す。

!!! example "判断例：足すか、依頼を直すか"
    - **状況**：テストを書いてと頼んだら、対象の関数ではなく、別のモジュールのテストが返ってきた。
    - **迷う候補**：「そうではなく、`cart.ts` のほうです」と 1 通足す。または、前の依頼を直して、対象を書き込んだ形で頼み直す。
    - **選んだもの**：前の依頼を直して頼み直す。
    - **理由**：対象を読み違えたあとの返事は、間違った対象を前提に積み上がる。小さな欠けなら足すだけで済むが、前提を取り違えたときは、取り違えた返事を会話に残さないほうが次の返事が安定する。

訂正を重ねても直らないときの切り分けは <!-- link:begin going-in-circles#choose -->[同じ失敗を繰り返す（堂々巡り） › 訂正・巻き戻し・新しく始めるの選び方](../symptoms/going-in-circles.md#choose)<!-- link:end --> にある。話題が変わったときなど、新しい会話にする合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。

## 良くなったかを確かめる {#check}

足したあとは、返事が期待に近づいたかを確かめる。確かめるには、何が起きれば終わりかを、先に決めておく。完了の形が決まっていれば、返事を読まなくても、コマンドの結果や出力の形で合否が分かる。

1 回の返事で良し悪しを決めない。モデルの返事は毎回同じにならないので、足した情報が効いたかを知りたいときは、同じ依頼を数回走らせて比べる。CLAUDE.md やスキルの変更のように、何度も使うものを変えたときは、<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> の手順で、変更の前後を比べる。

詰め終わった依頼は、取っておく。次に同じ種類の仕事を頼むとき、足した点が最初から入った依頼で始められる。

## なぜ返事を見て詰めると効くのか {#why}

返事は、Claude に何が見えていないかを教えてくれる。原理は「見せる」である。見えていない情報は、Claude の返事から逆算して見つかる。最初から全部を書こうとすると、何が見えていないかを知らないまま推測で書くことになり、書いても要らない条件が増え、必要な条件が抜ける。

効く原因は 2 つある。

- 見えていない：対象や再現の条件を Claude が知らないまま作業している。返事のずれが、足すべき点を示す。依頼に何を書けばよいかの見当は <!-- link:begin brief-a-new-colleague#colleague-test -->[新人の同僚に頼むつもりで › 文脈のない同僚に見せて確かめる](brief-a-new-colleague.md#colleague-test)<!-- link:end --> で付けられる。
- 散らかっている：長く詰め込んだ依頼や、積み重なった訂正が、会話の中で焦点を散らす。依頼を平易に保ち、ずれたら直して頼み直すと、会話に残るものが減る。

実務家の記事には、結果がいまいちなときにやり直すのではなく、制約を具体的にして詰めるという進め方が、Claude Code の作者のチームの習慣として紹介されている（根拠：弱）。公式の立場は、既定で足りる依頼は平易でよいというもので、この辞典の推奨は、足りない点を返事から見つけて足す進め方である。

## 効かない場面とやりすぎ {#limits}

返事を見て依頼を詰める進め方は、返事を見て戻せる作業に向く。戻せない作業（共有の環境への書き込みや、削除を伴う作業など）では、最初の平易な依頼でそのまま実行させない。何をしてよいかの範囲を先に決めてから頼む。

自分でも要件が固まっていないときは、足す点が返事から見つからない。その場合は、Claude に質問させて決めるべき点を洗い出す。頼み方は <!-- link:begin let-claude-ask#how -->[質問させる・インタビューさせる › 質問させる頼み方](let-claude-ask.md#how)<!-- link:end --> にある。大きな作業は、質問で仕様を文書にしてから新しい会話で作る（<!-- link:begin let-claude-ask#spec-then-fresh -->[質問させる・インタビューさせる › 仕様を文書にしてから新しい会話で作る](let-claude-ask.md#spec-then-fresh)<!-- link:end -->）。

よくある誤解を 2 つ挙げる。

- 雑に頼んでよい、という意味ではない：最初から分かっている対象や完了の形は、最初の依頼に書く。省くのは、まだ分からない条件を先回りして並べることである。
- 足し続ければいつか直る、という意味ではない：同じずれが 2 回続いたら、足し方ではなく依頼そのものを直す合図と考える。それでも直らないときの扱いは <!-- link:begin going-in-circles#diagnosis -->[同じ失敗を繰り返す（堂々巡り） › 原因を安く確かめる順](../symptoms/going-in-circles.md#diagnosis)<!-- link:end --> にある。

依頼を直して頼み直すと、前の失敗の跡が会話から消え、同じ失敗を繰り返しやすくなるという注意もある。頼み直すときは、分かったことをファイルに残す。両立のさせ方は <!-- link:begin build-on-results#with-clear -->[やり直させるより、結果を踏まえて直させる › /clear・巻き戻しとの両立](../context/build-on-results.md#with-clear)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [新人の同僚に頼むつもりで](brief-a-new-colleague.md)

**関連**

- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [やり直させるより、結果を踏まえて直させる](../context/build-on-results.md)
- [質問させる・インタビューさせる](let-claude-ask.md)
- [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
