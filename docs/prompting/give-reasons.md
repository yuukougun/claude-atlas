---
id: give-reasons
title: 理由を添える
aliases: [背景と目的を伝える, Add context, なぜを書く]
type: concept
field: prompting
chapter: 頼み方の原則
order: 20
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
scenes: [開発, 文章]
summary: 規則や依頼に理由を添えると、Claude は書いていない場面にも意図を当てはめられる。禁止を並べるより、なぜそうしたいかを一文で書く。
signs:
  - {type: symptom, text: 書いた規則を、少し違う場面になると守らない}
  - {type: symptom, text: 指示の文字どおりにだけ従い、意図を汲まない}
prerequisites: [brief-a-new-colleague]
related: [say-what-you-want, emphasis-words, four-specifics, when-requests-are-refused, what-to-put-in-claude-md, request-vs-lock]
sources: [api-docs-prompting-best-practices]
volatility: 低
sections:
  - {title: 禁止より理由（読み上げの例）, anchor: tts-example}
  - {title: 理由を添えると何が変わるか, anchor: what-changes}
  - {title: なぜ理由が効くのか, anchor: why}
  - {title: CLAUDE.md には理由と相談の基準を書く, anchor: claude-md}
  - {title: 理由の雛形, anchor: templates}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：規則に理由を添えると、書いていない場面にも意図が当てはまる。その書き方と限界が分かる。
    - **いつ引くか**：書いた規則を少し違う場面で守らないとき。指示の文字どおりにだけ従い、意図を汲まないとき。
    - **前提**：<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end -->

<!-- textlint-disable -->
別名：背景と目的を伝える・Add context・なぜを書く
<!-- textlint-enable -->

理由を添えるとは、規則や依頼に「なぜそうしたいか」を一文付けることである。理由は、Claude から見えない事情を見せる手段になる。禁止の文を増やすより、理由を 1 つ書くほうが、書いていない場面まで意図が届く。

## 禁止より理由（読み上げの例） {#tts-example}

禁止だけの指示と、理由を添えた指示の違いは、公式の文書にある読み上げの例で見るのが早い。公式は、禁止だけの書き方より、理由を添えた書き方のほうが効くと案内している。出典は[公式のプロンプトの指針](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)である。

Before は、禁止だけを書いた指示である。

```text
省略記号（…）を使うな。
```

After は、同じ内容に理由を添えた指示である。

```text
この返答は音声合成エンジンが読み上げる。
エンジンは省略記号の読み方が分からないので、省略記号は使わないでほしい。
```

After で足したのは、返答の行き先（音声合成エンジン）と、省略記号が困る理由（読み方が分からない）の 2 点である。禁止の中身は Before と変わらない。

!!! example "判断例：文章の依頼に理由を添えるか"
    - **状況**：社外の顧客に送る返信の下書きを頼む。文体は「ですます調で」と指定したい。
    - **迷う候補**：「ですます調で書く」とだけ書く。または「初対面の顧客に送るので、丁寧で距離のある文体にしたい」と理由まで書く。
    - **選んだもの**：理由まで書く。
    - **理由**：理由があると、「ですます」の語尾だけでなく、くだけた言い回しや省略を避ける判断にも意図が届く。ただし届くかどうかは、返答を読んで確かめる。

## 理由を添えると何が変わるか {#what-changes}

変わるのは、書いていない場面での判断の拠り所である。公式の文書は、理由を伝えると Claude がその意図を他の場面にも当てはめられると案内している。

- 禁止だけの規則は、文面に当たる場面にだけ効く。文面から少し外れると、守られているかどうかが読み取れない。
- 理由付きの規則は、理由に当たる場面にも効く。読み上げの例なら、読み方の分からない別の記号にも考えを及ぼす余地がある。

公式の例が示すのは省略記号だけである。ほかの記号まで実際に及ぶかは、公式の例からは分からない。自分の環境で、規則の文面にない近い場面を 1 つ試して確かめる。

## なぜ理由が効くのか {#why}

このページが名指しする原理は「見せる」で、防ぐ原因は「見えていない」である。Claude は会話の外の事情を知らない。読み上げに使われること、顧客に送られること、過去に事故があったことは、書かないかぎり Claude からは見えない。

禁止だけの規則は、Claude に線引きだけを渡す。線がどこまで引かれているか、なぜ引かれたかは分からない。理由を添えると、線の向こうにある事情が見える。新人の同僚に「この資料に数字を載せるな」とだけ伝えるより、「社外秘の数字が混じっているから」と伝えたほうが、新人が迷わないのと同じである（「新人の同僚に頼む」の考え方は<!-- link:begin brief-a-new-colleague#why -->[新人の同僚に頼むつもりで › なぜ文脈を書くと効くのか](brief-a-new-colleague.md#why)<!-- link:end -->が持つ）。

内部でどう処理されて意図が当てはまるのかは、公式の文書にも書かれていない。ここまでの説明は、見える事情が増えると判断の材料が増える、という筆者の推論である（推論・実践例なし）。

## CLAUDE.md には理由と相談の基準を書く {#claude-md}

CLAUDE.md の規則にも、理由を添える書き方は使える。CLAUDE.md は Claude が読んで判断するお願いなので、禁止の一文より、理由と迷ったときの動き方を書くほうが、書いていない場面に届きやすい。この辞典の推奨は、次の二層である。

- 例外を許さない禁止：deny ルールやフックで強制する。CLAUDE.md には、理由と相談の基準だけを書く。
- 状況で変わる規則：CLAUDE.md に、守ってほしいことと理由と相談の基準を書く。

Before は、禁止だけを書いた CLAUDE.md の例である。

```markdown
- テストで実際の外部 API を呼ばない。
```

After は、理由と相談の基準を添えた例である。

```markdown
- テストでは外部 API をモックに差し替える。実 API を呼ぶと、課金が発生し、外部のデータを書き換えるおそれがあるため。
- モックでは確かめられない挙動が疑わしいときは、実 API を呼ぶ前に質問する。
```

After は、禁止を「モックに差し替える」という望む形にし（<!-- link:begin say-what-you-want#rewrite -->否定形ではなく、望む形で書く › 禁止を望む形に書き換える（準備中）<!-- link:end -->）、理由を添えた。さらに、迷ったときの動き方（質問する）を相談の基準として加えた。

!!! example "判断例：本番データベースへの書き込み"
    - **状況**：Claude に本番のデータベースを書き換えさせたくない。例外はない。
    - **迷う候補**：CLAUDE.md に理由付きで「本番には書き込まない」と書く。または deny ルールやフックで止める。
    - **選んだもの**：deny ルールかフックで止め、CLAUDE.md には理由だけを書く。
    - **理由**：CLAUDE.md の文は Claude が読んで判断するお願いなので、理由を添えても必ず守られる保証はない。例外のない規則は鍵に移す（<!-- link:begin request-vs-lock#two-layers -->[お願いと鍵（決定論的か、非決定論的か） › 二層で書く](../basics/request-vs-lock.md#two-layers)<!-- link:end -->）。理由は、鍵の外にある近い場面（たとえばステージングの扱い）での判断に残す。

CLAUDE.md に残す行と外す行の見分け方は、<!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end -->が持つ。

## 理由の雛形 {#templates}

依頼の本文に使う雛形と、CLAUDE.md の規則に使う雛形を置く。動作の確認は、規則の文面にない近い場面を 1 つ試して行う。

<!-- gen:begin snippet give-reasons/request-with-reason -->
<!-- textlint-disable -->

??? example "雛形：理由を添える依頼の雛形"

    ```text
    <やってほしいこと。例：返答の書き方に関する指定>

    理由：<この指定が要る事情。Claude から見えない読み手・使い道・失敗したときの困りごと>
    範囲：<この指定を当てはめてほしい場面と、当てはめなくてよい場面>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet give-reasons/request-with-reason -->

<!-- gen:begin snippet give-reasons/claude-md-rule -->
<!-- textlint-disable -->

??? example "雛形：CLAUDE.md の規則に理由と相談の基準を添える雛形"

    ```markdown
    ## <規則の題>

    - <守ってほしいこと>
    - 理由：<なぜそうしたいか。破ったときに何が困るか>
    - 迷ったとき：<相談の基準。例：判断がつかなければ、実行する前に質問する>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet give-reasons/claude-md-rule -->

## 効かない場面とやりすぎ {#limits}

理由を添えても効かない、または逆効果になる場面がある。

- **例外のない規則**：理由を添えても、守られる保証は生まれない。仕組みに移す（<!-- link:begin say-what-you-want#two-layers -->否定形ではなく、望む形で書く › 例外のない禁止は仕組みへ（二層）（準備中）<!-- link:end -->）。
- **強調語で補う**：理由の代わりに「必ず」「IMPORTANT」を重ねても、守られるようにはならない。強い言い方は、かえって過剰に当てはめられることがある（<!-- link:begin emphasis-words#overreaction -->強調語（IMPORTANT・必ず）の現在 › 強い言い方が過剰に効く（準備中）<!-- link:end -->）。
- **当てはめすぎ**：理由が広いと、意図が広い場面に及ぶ。当てはめてほしくない場面があるなら、理由に加えて範囲も書く。雛形の「範囲」の欄がそのためのものである。
- **長すぎる理由**：1 つの規則に事情を何行も書くと、規則そのものが読みにくくなる。理由は一文にし、要る事情だけを書く。
- **事実と違う理由**：理由が実際と違えば、意図は間違った方向に当てはまる。理由は本当のことを書く。

よくある誤解は、理由を書くと丁寧になるだけ、というものである。理由は丁寧さではなく、判断の材料として働く。もう 1 つの誤解は、理由があれば必ず意図どおりになる、というものである。理由は意図が届く可能性を上げる書き方であり、届いたかどうかは返答で確かめる。

依頼が誤って断られたときに、本当の目的と文脈を足すことは、<!-- link:begin when-requests-are-refused#official-steps -->正当な依頼が断られたとき › 公式が案内する手段（準備中）<!-- link:end -->が持つ。偽った理由を添えることはしない。

理由と合わせて、依頼に対象・状況・完了・手本を書くと、推測で埋める所がさらに減る（<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [新人の同僚に頼むつもりで](brief-a-new-colleague.md)

**次に読む**

- 否定形ではなく、望む形で書く（準備中）

**関連**

- 強調語（IMPORTANT・必ず）の現在（準備中）
- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)
- 正当な依頼が断られたとき（準備中）
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
