---
id: let-claude-ask
title: 質問させる・インタビューさせる
aliases: [AskUserQuestion, インタビューして仕様を作る, 確認の質問をさせる]
type: concept
field: prompting
chapter: 詰め方と頼み直し
order: 160
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない]
scenes: [開発, 文章]
summary: 自分でも要件が固まっていないときは、先に Claude に質問させて決めるべき点を洗い出す。大きな作業は、質問で仕様を文書にしてから新しい会話で作らせる。
signs:
  - {type: goal, text: 何を作りたいか、まだ自分でもはっきりしない}
  - {type: symptom, text: 頼んだ後になって、伝え忘れた条件が次々に出てくる}
  - {type: goal, text: 作る前に仕様を詰めたい}
prerequisites: [four-specifics]
related: [spec-first, ask-for-options, when-to-plan, refine-in-conversation, not-what-i-meant, think-before-asking]
tracks: [ask-user-question]
sources: [cc-docs-best-practices, cc-docs-tools-reference, cc-docs-hooks]
volatility: 中
sections:
  - {title: 質問させる頼み方, anchor: how}
  - {title: なぜ質問が効くのか, anchor: why}
  - {title: 仕様を文書にしてから新しい会話で作る, anchor: spec-then-fresh}
  - {title: 決めたことと、確かめることを分ける, anchor: decided-vs-open}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：要件が固まっていないときに、Claude に質問させて決める点を洗い出す頼み方と、決めた内容を文書にして新しい会話で作らせる進め方が分かる。
    - **いつ引くか**：何を作りたいか自分でもはっきりしないとき。頼んだ後になって、伝え忘れた条件が次々に出てくるとき。作る前に仕様を詰めたいとき。
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AskUserQuestion・インタビューして仕様を作る・確認の質問をさせる
<!-- textlint-enable -->

質問させるとは、作業を始める前に Claude から質問を受け、自分が決めていない点を先に洗い出す頼み方である。答えは自分で出し、決まった内容は文書に残す。

## 質問させる頼み方 {#how}

質問させる頼み方の中心は、作らせる前に「インタビューして」と頼み、コードを書く前に止めることである。次の Before/After は、同じ機能の依頼を並べたものである。

**Before**

```text
記事にコメント機能を付けて。
```

**After**

```text
記事にコメントを付けられるようにしたい。実装に入る前に、私にインタビューして仕様を詰めてほしい。
分かりきった質問はしないこと。答えで設計が変わる点だけを聞くこと。
私が答えられない点は決めずに残し、質問が尽きたら仕様を SPEC.md に書くこと。コードはまだ書かないこと。
```

After で足したものは 4 つある。1 つ目は、実装の前にインタビューするという順序である。2 つ目は、質問の絞り方（分かりきったことを聞かない）である。3 つ目は、答えられない点を勝手に決めないことである。4 つ目は、終わりの形（SPEC.md に書く）と、コードを書かない指定である。

現行の Best practices は、ツール名を出さず、spec が書けるまでインタビューして SPEC.md に書くよう頼む形を示す。すると Claude が選択式の質問を返す（[Best practices](https://code.claude.com/docs/en/best-practices)）。頼み方にツール名は要らない。

=== "アプリ"
    同じ依頼の文面が使える。選択式の質問がどう表示されるかは未確認である。質問が文章で返ったら、番号に沿って答える。

=== "Claude Code"
    Claude は、AskUserQuestion という組み込みの道具で選択式の質問をする。成熟度は <!-- gen:begin feature ask-user-question/maturity -->GA<!-- gen:end feature ask-user-question/maturity --> で、入った版は <!-- gen:begin feature ask-user-question/since -->2.0.21（2025-10-18）<!-- gen:end feature ask-user-question/since --> である（[Tools reference](https://code.claude.com/docs/en/tools-reference)）。1 回の呼び出しで聞ける問数と、各問の選択肢の数には上限があり、多くの点を聞くときは何回かに分かれる（[Hooks reference](https://code.claude.com/docs/en/hooks)）。上限の値は、この辞書では確かめていないので、公式の文書で見る。選択肢のほかに、自由に答えを書ける。

依頼の雛形を置く。角かっこの所を自分の依頼に置き換える。

<!-- gen:begin snippet let-claude-ask/interview-feature -->
<!-- textlint-disable -->

???+ example "雛形：インタビューで仕様を詰める依頼の雛形（機能の例）"

    ```text
    <作りたいものを 1〜2 行で。例：記事にコメントを付けられるようにしたい>

    実装に入る前に、私にインタビューして仕様を詰めてほしい。
    - 分かりきった質問はしない。答えで設計が変わる点だけを聞く
    - 選べる点は選択式で聞き、推奨があれば添える
    - 対象は <範囲。例：src/comments/ と、そこから呼ぶ API> に限る
    - 私が答えられない点は、決めずに「要確認」として残す
    - 質問が尽きたら、仕様を SPEC.md に書く。範囲外のことと、動作の確かめ方も書く
    - コードはまだ書かない
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.21。

<!-- textlint-enable -->
<!-- gen:end snippet let-claude-ask/interview-feature -->

## なぜ質問が効くのか {#why}

質問が効く理由は、決めていない点を、頼む側が自分で見つけなくてよくなるからである。この辞典の原理でいう「見せる」（Claude に判断の材料を見える形で渡す）に当たる。防ぐ原因は「見えていない」（Claude が条件を知らないまま作る）である。

Claude には、頼む側の頭の中にある条件が見えない。頼む側も、決めていない点があることに、作ってから気づく。だから、頼んだ後になって伝え忘れた条件が次々に出てくる。質問させると、Claude の側から「ここは決まっているか」を並べてくれる。答える前でも、質問の一覧そのものが、自分の決め忘れの一覧になる。

答えた内容は、依頼に不足していた情報になる。<!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](four-specifics.md#which-to-add)<!-- link:end --> で、足す点を探す手間を、質問が肩代わりする形である。ずれた結果を見てから直す方法は <!-- link:begin refine-in-conversation#edit-the-request -->[頼み方は一回で決めない（会話で詰める） › 訂正を重ねるより依頼を直す](refine-in-conversation.md#edit-the-request)<!-- link:end --> にある。ずれの原因を切り分ける診断は <!-- link:begin not-what-i-meant#diagnosis -->[意図と違うものが出てくる › 原因を安く確かめる順](../symptoms/not-what-i-meant.md#diagnosis)<!-- link:end --> にある。

## 仕様を文書にしてから新しい会話で作る {#spec-then-fresh}

大きな作業では、質問で決めた内容を仕様の文書（SPEC.md など）に書かせ、作る作業は新しい会話で始める。仕様を詰める会話と、作る会話を分ける進め方である。Best practices も、spec ができたら新しいセッションで作る流れを示す。

手順は 3 段である。

1. 質問に答えながら、仕様を詰める。「インタビューして SPEC.md に書いて」と頼む。
2. 書かれた SPEC.md を、自分で読んで直す。
3. 新しい会話を開き、SPEC.md を渡して作らせる。

新しい会話にする理由は 2 つある。1 つ目は、仕様を詰める間のやりとりが、作る会話に残らないことである。作る側は、整理された文書だけを読む。2 つ目は、インタビュー中の思い込みを実装に持ち込まないためだとする実務家の説明である（根拠：弱）。仕様の文書に書かれていないことは、新しい会話の Claude には見えない。書かれていなかった点は、そこで初めて分かる。

この進め方の本体（仕様に書くこと、モックでの合意、新しい会話での実装、停止条件つきの回し方）は <!-- link:begin spec-first -->[仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)<!-- link:end --> にある。このページは、仕様を詰める最初の段の頼み方を持つ。

!!! example "判断例：通知機能を作る"
    - **状況**：アプリに通知機能を付けたい。誰に、どの経路で、どの条件で送るかは、まだ自分でも決めていない。
    - **迷う候補**：思いつく範囲で依頼し、出てきた実装を直していく進め方。質問させて仕様を決めてから作る進め方。
    - **選んだもの**：質問させて仕様を決めてから、新しい会話で作る。
    - **理由**：送る相手と経路が決まっていないと、実装の大半が作り直しになる。決めていない点が多いほど、実装の後で直すより、質問で先に決めるほうが安い。

## 決めたことと、確かめることを分ける {#decided-vs-open}

仕様の文書では、決めたことと、確かめることを分けて書かせる。決めたことは「決定事項」、自分では決められず誰かに確認する点は「要確認事項」とする。分けないと、要確認の点が決定事項に混ざり、確認しないまま実装される。

この分け方は、確認する相手が別にいる作業で効く。たとえば、規約の曖昧な点を主催者に聞く、既存システムの仕様を担当者に聞く、といった場面である。自分で答えられない点を、Claude が推測で決めないようにするには、「答えられない点は決めずに残す」と頼む。

仕様の文書には、次の 3 つも書かせる。この辞典の推奨である。

- 範囲外のこと：やらないことを明記する。実装が範囲を広げるのを防ぐ。
- 関わるファイルとインターフェース：新しい会話の Claude が、文書だけで作業を始められるようにする。
- 確かめる手順：作ったものが正しいと、どう確かめるか。最後に置く。

評価環境（得点を計算する道具など）を作る依頼の例を置く。決定事項と要確認事項を分けること、最後に評価器を確かめる手順を書かせることが入っている。

<!-- gen:begin snippet let-claude-ask/interview-evaluator -->
<!-- textlint-disable -->

??? example "雛形：インタビューで仕様を詰める依頼の雛形（評価環境の例）"

    ```text
    評価環境（ローカルのテスタや、得点を計算する道具）を作りたい。実装に入る前に、私にインタビューして仕様を詰めてほしい。
    対象は docs/rules.md の範囲に限る。分かりきった質問はしないこと。
    特に、次の点を掘り下げること。
    - 問題文と規約の曖昧な点
    - 入力のパラメータの範囲と、端のケース
    - 評価指標と、集計の方法
    - 提出環境（時間・メモリ・オフライン・言語の版）

    決定事項と、要確認事項（運営に質問すべき点）を分けて SPEC.md に書くこと。
    最後に、この評価器が正しいことを確かめる手順を書くこと。コードはまだ書かないこと。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.21。

<!-- textlint-enable -->
<!-- gen:end snippet let-claude-ask/interview-evaluator -->

インタビューでできた仕様の文書は、どの題材でも自分で読む。Claude が、自分が答えていない点を既定の値で埋めていないかを確かめる。

## 効かない場面とやりすぎ {#limits}

質問させる方法は、要件が明確な作業には要らない。ボタンの色を 1 つ変える、誤字を直す、といった作業では、質問が手間を増やすだけである。要件が明確なら、<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end --> の 4 点を書いて頼めば足りる。

やりすぎにも気をつける。

- 質問が多すぎる：分かりきった質問を許すと、答えるだけで疲れる。「答えで設計が変わる点だけを聞く」と絞る。
- 質問に答えず先へ進む：質問の途中で「もう作って」と頼むと、未決の点を Claude が推測で埋める。残る点は要確認として文書に残す。
- 質問の画面を放置する：Claude Code では、既定で、答えるまで質問が開いたままになる。放っておいたら先へ進めたいときは、`askUserQuestionTimeout` で閉じるまでの時間を決める（指定できる値：<!-- fact:begin ask-user-question-timeout -->60s・5m・10m（放っておくと、選んだ分だけ送って先へ進む）（2026-11-06 時点）<!-- fact:end -->）。
- 人がいない実行で頼む：質問の答えは人が出す。サブエージェントからは使えない。`-p` の非対話の実行では、承認を受け持つ仕組みがあるときだけ使われる。質問させるのは、人がいる会話にする（[Hooks reference](https://code.claude.com/docs/en/hooks)）。

選択肢を並べて選ばせる場面は、<!-- link:begin ask-for-options -->[選択肢と推奨案を出させる](ask-for-options.md)<!-- link:end --> が持つ。独自性が要る考察では、質問をさせる前に自分の案を書く（<!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end -->）。方針や範囲に迷う作業で、編集を止めたまま計画を読む方法は <!-- link:begin when-to-plan#when -->[plan mode の使いどころ › 計画が効く作業、省いてよい作業](../cli/when-to-plan.md#when)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Tools reference](https://code.claude.com/docs/en/tools-reference)：Anthropic・英語・確認日 2026-11-04
- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)

**次に読む**

- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)

**関連**

- [選択肢と推奨案を出させる](ask-for-options.md)
- [plan mode の使いどころ](../cli/when-to-plan.md)
- [頼み方は一回で決めない（会話で詰める）](refine-in-conversation.md)
- [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
