---
id: rewind-dont-correct
title: 違うと返すより、巻き戻す・編集する
aliases: [プロンプトを編集して送り直す, 失敗の残骸を残さない, 訂正の往復をやめる]
type: concept
field: context
chapter: 新しくする・巻き戻す
order: 30
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発, 文章]
summary: 期待と違う返答には、訂正を重ねるより、前のメッセージを直して送り直すか巻き戻すほうがよい理由が分かる。間違った試みが会話に残ると、次の答えがそれに引きずられる。
signs:
  - {type: situation, text: 期待と違う返事が来て、訂正を書こうとしている}
  - {type: goal, text: 失敗したやり取りをなかったことにしてやり直したい}
prerequisites: [context-rot]
related: [checkpoints-and-rewind, when-to-start-fresh, keep-failure-lessons, build-on-results, tidy-the-desk, going-in-circles, insists-on-mistakes, refine-in-conversation]
tracks: [checkpoints]
outdated_advice: []
sources: [cc-docs-best-practices, cc-docs-checkpointing, chroma-research-context-rot, marmelab-code-tips-wish-id-had, dsebastien-code-tips-best-practices, ruben-hours, hatebu-wataru86-commands]
volatility: 低
sections:
  - {title: なぜ訂正より巻き戻しか, anchor: why}
  - {title: 何に効くか, anchor: effect}
  - {title: 面ごとの戻し方, anchor: how}
  - {title: 巻き戻すと消えるもの, anchor: what-is-lost}
  - {title: よくある誤解と実践者の幅, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：期待と違う返答には、訂正を重ねるより、前のメッセージを直して送り直すか巻き戻すほうがよい。その理由を説明できる。
    - **いつ引くか**：期待と違う返事が来て、訂正を書こうとしているとき。失敗したやり取りをなかったことにしてやり直したいとき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：プロンプトを編集して送り直す・失敗の残骸を残さない・訂正の往復をやめる
<!-- textlint-enable -->

違うと返す代わりに、前のメッセージを直して送り直すか、会話をその時点まで巻き戻す。これが「巻き戻す・編集する」である。このページは、訂正の往復より巻き戻しが効く理由と、アプリと Claude Code での戻し方、戻すと失うものを扱う。

## なぜ訂正より巻き戻しか {#why}

訂正を書いて送ると、間違った返答と訂正の言葉が、会話にそのまま残る。Claude は次の返答を作るとき、その会話の全体を材料にする。つまり、失敗した試みも材料に入る。

公式の Best practices は、この点を具体的に書いている。同じ点を 2 回直させてもまだ間違っているとき、3 回目の指摘を書いても、Claude は「失敗した 2 回分の試行が入った会話」を読み続けるだけになりやすい。公式はそこで、3 回目を書かずに `/clear` して、学んだことを織り込んだ依頼を 1 つ書き直すよう勧める（[Best practices](https://code.claude.com/docs/en/best-practices)）。

実践者の記事も同じ方向で一致している。Claude Code の記事は、こう書く。悪い応答を同じ会話で直させると、間違いが残る。残った間違いは後の試行を汚す。だから最後に良かった時点へ戻る（[Claude Code Tips I Wish I’d Had From Day One](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)、[Claude Code Tips and Best Practices](https://www.dsebastien.net/claude-code-tips-and-best-practices/)）。claude.ai では、「それは違う」と返信せず、悪い回答の前の依頼を編集するという助言がある（[27 Claude tips after 1,800 hours.](https://ruben.substack.com/p/1800-hours-of-claude)）（根拠：中）。

残るものの違いを、例で見る。同じ依頼で、1 回目の案が外れた場面である。

| 場面 | 訂正を重ねる | 巻き戻して頼み直す |
| --- | --- | --- |
| 1 回目の返答 | タイムアウト値を伸ばす案が返る。原因はそこではない | 同じ案が返る。原因はそこではない |
| 違うと分かったとき | 「違う、タイムアウトは関係ない」と返す | 巻き戻して、元の依頼を直す |
| 2 回目の返答の材料 | 依頼、外れた案、否定の言葉、その否定への返答 | 直した依頼だけ |
| 会話に残る失敗 | 外れた案が 1 つ残り、2 回目も外れるとさらに増える | なし |

巻き戻した側の依頼は、外れた案から分かったことを足して書く。足した所が、巻き戻しで得をする所である。

```text
Before（訂正を重ねる）
違う。タイムアウトは関係ない。もう一度原因を調べて。

After（元の依頼を直して送り直す）
ログイン処理のテスト test_login が落ちる。原因を調べて直して。
タイムアウト値の変更は試して効果がなかったので、原因の候補から外す。
```

After で足したのは、試して外れた候補の 1 行である。外れた案そのものは会話に残らず、分かったことだけが依頼に残る。

## 何に効くか {#effect}

巻き戻しは、このカタログの原因「散らかっている」に効く。会話に失敗した試みと否定の言葉が積もると、似ているが違う情報が増え、答えの質が落ちやすい。この仕組みは <!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> が扱う。そのうえで、失敗した試みは「紛らわしい情報」の典型になる。研究では、もっともらしい誤情報が混ざると性能が下がると示されている（[Context Rot](https://www.trychroma.com/research/context-rot)）。ただし対象は Claude 以外を含む複数のモデルの実験で、会話の訂正にそのまま当てはまると確かめたものではない（類推）。

原理で言えば「見せる」にあたる。Claude が答えの材料にするのは、会話として見せられたものである。見せるものを選べるのは、こちらだけである。巻き戻しは、見せたくない失敗を見せない状態に戻す操作である。訂正は見せるものを増やすだけで、消さない。

どのくらい戻すかの線引きは、別のページが持つ。

- 巻き戻しても直らないとき、話題が変わったときの新しい会話への切り替えは、<!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](when-to-start-fresh.md#signals)<!-- link:end --> が扱う。
- 同じ失敗の繰り返しの原因の切り分けは、<!-- link:begin going-in-circles#diagnosis -->[同じ失敗を繰り返す（堂々巡り） › 原因を安く確かめる順](../symptoms/going-in-circles.md#diagnosis)<!-- link:end --> が扱う。
- 巻き戻さずに依頼の書き方を詰める進め方は、<!-- link:begin refine-in-conversation#edit-the-request -->[頼み方は一回で決めない（会話で詰める） › 訂正を重ねるより依頼を直す](../prompting/refine-in-conversation.md#edit-the-request)<!-- link:end --> が扱う。

## 面ごとの戻し方 {#how}

戻し方は面で違う。どちらも、戻した先で元の依頼を直して送り直すのが要点である。

=== "アプリ"

    - 悪い回答の前のメッセージを編集して、送り直す。「違う」と返信して続けない。
    - 編集で送り直すと、悪い回答に至るやり取りを引きずらずに、同じ地点から別の答えを求められる。
    - 編集のあと、元の枝がどう見えるか、戻せるかは、画面で確かめる。このページでは確かめていない。

=== "Claude Code"

    - `/rewind` を実行するか、入力欄が空のときに `Esc` を 2 回押して、巻き戻しのメニューを開く。入力欄に文字があると、`Esc` 2 回は文字を消すだけでメニューは開かない。
    - メニューで、戻したい時点のプロンプトを選ぶ。コードと会話の両方、会話だけ、コードだけを戻せる。
    - 会話を戻すと、選んだメッセージの元の文が入力欄に戻る。そこで依頼を直して、送り直す。
    - 戻せる範囲と注意は <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> が扱う。

間違いに気づいたら、直す前にまず手を止める。公式は「最初の 1 分を見て、ずれたらすぐ `Esc` で止める」ことも勧める。止めた時点なら、巻き戻す量が少なくて済む。

!!! example "判断例：2 回目の修正も違った"
    - **状況**：テストが落ちる原因を直させたら、1 回目と 2 回目の案は外れた。3 回目の指摘を書こうとしている。
    - **迷う候補**：3 回目の訂正を書く／1 回目の依頼の時点まで巻き戻して、分かったことを足して頼み直す。
    - **選んだもの**：巻き戻して、外れた候補を依頼に書き足して頼み直す。
    - **理由**：外れた 2 回分の試みが会話に残るほど、次の返答がそれに引きずられやすい。公式も 3 回目を書かない線を引いている。

断られたときも、巻き戻しは公式が案内する手段の 1 つである。正当な依頼が止められたとき、公式は、引き金になったやり取りより前に戻って、言い方か進め方を変えることを勧める（Claude Code では `/rewind`、アプリでは前のメッセージを直して送る）。これは、利用ポリシーを避けるための頼み方ではなく、本当の目的や進め方を伝え直す操作である。

## 巻き戻すと消えるもの {#what-is-lost}

巻き戻しは、失敗を消すと同時に、ほかのものも消す。戻す前に、何が消えるかを知っておく。

- **会話**：選んだ時点より後のメッセージが、続きの材料から外れる。失敗した試みだけでなく、その間に Claude が見つけた事実も外れる。
- **コード（Claude Code）**：コードも戻すを選ぶと、その時点より後の Claude のファイル編集が元に戻る。会話だけを戻せば、コードはそのままである。
- **戻らないもの（Claude Code）**：Bash だけが変えたファイル、Claude Code の外での変更、ほとんどのサブエージェントの編集は、巻き戻しで戻らない。これらは git で戻す。チェックポイントは、git の代わりではない。
- **失敗から分かったこと**：「この方法は効かなかった」という知識は、会話と一緒に消える。そのまま巻き戻すと、同じ案を再び出されることがある。

最後の項目への補いは、会話を捨てて学びだけを書き残すことである。何を残し、何を捨てるかは <!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](keep-failure-lessons.md#what-to-keep)<!-- link:end --> が、巻き戻しとの両立は <!-- link:begin keep-failure-lessons#both -->[失敗の教訓は捨てずに書き残す › 巻き戻しと記録の両立](keep-failure-lessons.md#both)<!-- link:end --> が扱う。最小の書き残しは、外れた候補の 1 行を、送り直す依頼に足すことである。たとえば「タイムアウト値の変更は試して効果がなかった」と書く。

戻す範囲の詳細は、チェックポイントのページの節が持つ。

- 戻せるものと戻せないものは、<!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> を見る。
- 途中からの要約は、<!-- link:begin checkpoints-and-rewind#summarize -->[チェックポイントと /rewind（git との違い） › 途中から要約する](../cli/checkpoints-and-rewind.md#summarize)<!-- link:end --> を見る。
- git との組み合わせは、<!-- link:begin checkpoints-and-rewind#with-git -->[チェックポイントと /rewind（git との違い） › git と組み合わせる](../cli/checkpoints-and-rewind.md#with-git)<!-- link:end --> を見る。

## よくある誤解と実践者の幅 {#misconceptions}

**誤解 1：訂正は常に悪い。** 訂正が効く場面もある。1 回目の返答が惜しく、足りない 1 点を足せば済むなら、会話で足してよい。巻き戻したほうがよいのは、方向が外れているときや、訂正が 2 回続けて効かないときである。足りない情報を見て足す進め方は、<!-- link:begin refine-in-conversation#start-plain -->[頼み方は一回で決めない（会話で詰める） › まず平易に頼み、足りない分を足す](../prompting/refine-in-conversation.md#start-plain)<!-- link:end --> が扱う。

**誤解 2：巻き戻せば何でも元に戻る。** 戻るのはチェックポイントが記録した範囲だけである。Bash や外での変更は戻らない。重要な変更は、巻き戻しの前に git で保存しておく。

**誤解 3：巻き戻すと、学びも全部なくなる。** 会話は消えるが、学びはファイルや依頼に移せる。移す手順は <!-- link:begin keep-failure-lessons#both -->[失敗の教訓は捨てずに書き残す › 巻き戻しと記録の両立](keep-failure-lessons.md#both)<!-- link:end --> が扱う。

巻き戻すかどうかには、立場の幅がある。

- **公式の立場**：訂正が 2 回失敗したら、3 回目を書かずに `/clear` して、学んだことを織り込んだ依頼を書き直す。巻き戻しは、戻す手段の 1 つとして案内される。
- **実践者の幅**：巻き戻しと `/clear` を最もよく使うという実践者がいる。一方で、過去のやり取りが消えて改善点を探しにくくなるので使わない、という声もある。後者は、はてなブックマークに表示されたコメントの意見で、量で確かめたものではない（根拠：弱）。
- **この辞典の推奨**：外れた方向への訂正は重ねず、巻き戻して頼み直す。ただし、巻き戻す前に、分かったことだけを依頼かファイルに書き残す。

巻き戻した直後に送る依頼には、足りなかった点と、外れた候補を書く。そうすると、巻き戻しは単なるやり直しではなく、分かったことを持ち越した、きれいな再開になる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Checkpointing](https://code.claude.com/docs/en/checkpointing)：Anthropic・英語・確認日 2026-11-04
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)：Chroma・英語・確認日 2026-11-04
- [Claude Code Tips I Wish I’d Had From Day One](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)：marmelab・英語・確認日 2026-11-04
- [Claude Code Tips and Best Practices](https://www.dsebastien.net/claude-code-tips-and-best-practices/)：Sébastien Dubois・英語・確認日 2026-11-04
- [27 Claude tips after 1,800 hours.](https://ruben.substack.com/p/1800-hours-of-claude)：Ruben Hassid・英語・確認日 2026-11-04
- [『Claude Code を4ヶ月使ってわかった、おすすめコマンド・スキル 10 選 - Qiita』へのコメント](https://b.hatena.ne.jp/entry/s/qiita.com/wataru86/items/b859f1578191a1e15808)：はてなブックマーク（コメントの一覧）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [やり直させるより、結果を踏まえて直させる](build-on-results.md)
- [失敗の教訓は捨てずに書き残す](keep-failure-lessons.md)

**関連**

- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [新しい会話を始めるタイミング](when-to-start-fresh.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)
- [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- [頼み方は一回で決めない（会話で詰める）](../prompting/refine-in-conversation.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
