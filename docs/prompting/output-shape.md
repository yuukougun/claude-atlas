---
id: output-shape
title: 出力の形と分量を指定する
aliases: [書式の指定, 冗長さを抑える, 簡潔に答えさせる, markdown を減らす]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 110
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 合っていない]
scenes: [文章, 開発, データ分析]
summary: 書式・長さ・要約の有無は望む形で指定し、頼む文の書き方も出力の形に合わせる。機械が読む出力で形を必ず守らせたいなら、形式を保証する仕組みを使う。
signs:
  - {type: symptom, text: 箇条書きと見出しばかりの返事になる}
  - {type: goal, text: 返事の書式や長さを、用途に合わせて指定したい}
prerequisites: [say-what-you-want]
related: [show-examples, structured-outputs-basics, model-quirks, xml-tags, requesting-prose, less-ai-sounding-japanese, output-style-modes, where-to-put-instructions#styles]
tracks: [structured-outputs]
outdated_advice: [prefill-for-json, styles-for-tone]
sources: [api-docs-prompting-best-practices, api-docs-structured-outputs, hc-styles-to-skills, hc-personalization]
volatility: 中
sections:
  - {title: 頼む文の書き方が出力に映る, anchor: mirror}
  - {title: 長さと要約の有無, anchor: length}
  - {title: いつも揃えたいときの置き場所, anchor: where}
  - {title: 必ず守らせたい形式は仕組みで, anchor: guaranteed}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：書式・長さ・要約の有無は望む形で指定し、頼む文の書き方も出力に合わせる。機械が読む出力で形を必ず守らせたいなら、形式を保証する仕組みを使う。
    - **いつ引くか**：箇条書きと見出しばかりの返事になるとき。返事の書式や長さを、用途に合わせて指定したいとき。
    - **前提**：<!-- link:begin say-what-you-want -->[否定形ではなく、望む形で書く](say-what-you-want.md)<!-- link:end -->

<!-- textlint-disable -->
別名：書式の指定・冗長さを抑える・簡潔に答えさせる・markdown を減らす
<!-- textlint-enable -->

出力の形と分量を指定するとは、返事の書式（見出し・箇条書き・文章）、長さ、作業後の要約の有無を、読み手と用途に合わせて頼むことである。このページでは、頼む文そのものが出力の見本になること、長さと要約の頼み方、いつも揃えたいときの置き場所、形を必ず守らせたいときの仕組みを扱う。

## 頼む文の書き方が出力に映る {#mirror}

返事の書式は、頼む文の書式に引きずられる。公式の指針は、プロンプトの書き方を望む出力の書き方に合わせるよう勧めている。プロンプトから markdown を減らすと、出力の markdown も減る傾向がある（[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)）。

Before は、見出しと箇条書きで書いた依頼に、禁止の注文を並べたものである。

```text
## 依頼
次のエラーログの原因を調べてほしい。

## 条件
- markdown を使わないこと
- 箇条書きにしないこと
- 見出しを付けないこと
```

依頼の文面が見出しと箇条書きで組まれているので、そこが返事の見本になる。注文も「しないこと」の形で、望む形を示していない。禁止を望む形に書き換える理由は <!-- link:begin say-what-you-want#why -->[否定形ではなく、望む形で書く › なぜ望む形のほうが守られやすいか](say-what-you-want.md#why)<!-- link:end --> が扱う。

After は、依頼を文章で書き、望む形と読み手を足したものである。

<!-- gen:begin snippet output-shape/prose-answer -->
<!-- textlint-disable -->

???+ example "雛形：依頼の文も返事の形に合わせた、書式を指定する依頼の雛形"

    ```text
    次のエラーログを読んで、原因として考えられることを説明してほしい。読むのは同じチームの開発者で、チャットで流し読みする。

    返事は、見出しも箇条書きも付けず、短い段落の文章で書く。最初の段落で最も有力な原因を述べ、次の段落で、それを確かめる方法を述べる。

    <log>
    （ここにログを貼る）
    </log>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet output-shape/prose-answer -->

After で足したことは 3 つある。依頼の文面を、見出しや箇条書きのない文章にした。「markdown を使わない」を、「短い段落の文章で書く」という望む形に替えた。読み手と読む場面（チャットで流し読みする同僚）を足した。

何が変わるかというと、返事が段落の文章になる傾向が強まる。ただし、傾向であって保証ではない。必ず守らせたい形は、この後の <!-- link:begin output-shape#guaranteed -->[出力の形と分量を指定する › 必ず守らせたい形式は仕組みで](output-shape.md#guaranteed)<!-- link:end --> で扱う。

形の注文は、ほかにも書ける。

- 数式の記法（LaTeX）が要らないなら、記号を使わない plain text で書くよう頼む。
- 返事の一部を後で取り出したいなら、その部分をタグで囲ませる。タグの使い方は <!-- link:begin xml-tags -->[XML タグで区切る](xml-tags.md)<!-- link:end --> が扱う。
- 形を言葉で説明しにくいなら、望む返事の例を見せる。選び方は <!-- link:begin show-examples#before-after -->[例を見せる › 言葉の説明を例に替える](show-examples.md#before-after)<!-- link:end --> が扱う。

## 長さと要約の有無 {#length}

返事の長さは、依頼の書き方・モデル・場面で変わる。「短く」「詳しく」と形容詞で頼むより、読み手と用途を渡し、段落や文の数で示すほうが、ずれが少ない（この辞典の推奨）。

読み手が違えば、同じ内容でも適切な長さが違う。レビューを頼む同僚には 3 つの短い段落で足りる。設計の判断を残す文書には、根拠まで書いた長さが要る。長さの注文には、何のための長さかを添える。

<!-- gen:begin snippet output-shape/length-and-form -->
<!-- textlint-disable -->

??? example "雛形：読み手と用途から、形と長さを指定する依頼の雛形"

    ```text
    このプルリクエストの変更内容を、レビューを頼む相手への説明として書いてほしい。読み手は、変更の中身をまだ知らない同僚で、最初の 1 分で何を見てほしいかを知りたい。

    形と長さは、3 つの短い段落にする。1 段落目には何を変えたかを、2 段落目にはなぜ変えたかを、3 段落目には特に見てほしい箇所を、それぞれ 3 文以内で書く。変更したファイルの一覧は、差分を見れば分かるので付けない。

    <diff>
    （ここに差分を貼る）
    </diff>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet output-shape/length-and-form -->

この雛形は、読み手、段落の数、各段落に書くこと、書かないものを順に示す。「簡潔に」だけの依頼と違い、どこまで書けば終わりかが分かる。

要約の有無は、別に頼む。公式の指針によると、新しいモデルは簡潔で、道具を使った作業のあとの要約を省くことがある。要約が欲しいなら、書くよう明示する。逆に返事が長すぎるなら、簡潔さを明示して頼む。どのモデルが長めで、どのモデルが短めかは版で変わる。公式の傾向は <!-- link:begin model-quirks#official-guidance -->[モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向](../models/model-quirks.md#official-guidance)<!-- link:end --> で確かめる。

自分の環境の傾向は、<!-- link:begin model-quirks#observe-and-record -->[モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する](../models/model-quirks.md#observe-and-record)<!-- link:end --> の手順で記録する。

<!-- gen:begin snippet output-shape/work-summary -->
<!-- textlint-disable -->

??? example "雛形：作業のあとの要約を書かせる指示の雛形"

    ```text
    道具を使う作業を終えたら、返事の最後に、やったことの要約を書く。要約は、変えたファイル、確かめたこと、確かめていないことの順に、5 文以内の文章で書く。作業の途中の経過は繰り返さない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet output-shape/work-summary -->

この雛形は、要約に書く項目と順、長さの上限、繰り返さないものを決めている。確かめていないことを必ず書かせるのは、要約が「全部できた」の一言で終わらないようにするためである。

## いつも揃えたいときの置き場所 {#where}

毎回同じ形を頼むなら、依頼ごとに書かず、効く範囲の広い置き場所へ移す。書き忘れた回だけ形が崩れるのを防げる。

- **Claude Code**：説明の多さや簡潔さをセッション全体で切り替えるのは、出力スタイルの役目である。使い方は <!-- link:begin output-style-modes#switch -->[出力スタイルで応答の仕方を切り替える › 切り替え方](../cli/output-style-modes.md#switch)<!-- link:end --> が扱い、CLAUDE.md との分担は <!-- link:begin output-style-modes#vs-claude-md -->[出力スタイルで応答の仕方を切り替える › CLAUDE.md・スキルとの分担](../cli/output-style-modes.md#vs-claude-md)<!-- link:end --> が扱う。
- **アプリ**：いつも同じ調子と形式にしたいなら、全会話に効く Claude への指示に書く。プロジェクトの中だけなら、プロジェクトの指示に書く。場面ごとに切り替えたいなら、スキルにする。
- **API**：システムプロンプトに書く。

アプリの Styles（スタイル）は、スキルへの移行が 2026-06 に告知された。2026-11-04 の確認では、告知の記事は取り下げられていて、画面にスタイルのメニューが今も出るかは未確認である。Styles を前提にした古い手順は、上の置き場所に読み替える。台帳の行は <!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end --> にあり、置き場所ごとの比較は <!-- link:begin where-to-put-instructions#styles -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 調子と形式を揃えたいとき（Styles を使っていた場合）](../app/where-to-put-instructions.md#styles)<!-- link:end --> が扱う。

!!! example "判断例：返事の形をいつも揃えたい"
    - **状況**：アプリで、返事をいつも「結論を先に、短い段落の文章で」にしたい。毎回の依頼に書くのは面倒になってきた。
    - **迷う候補**：毎回の依頼に書く。全会話に効く Claude への指示に書く。スキルにして、必要な場面で呼ぶ。
    - **選んだもの**：Claude への指示に書く。
    - **理由**：いつも同じ形なら、場面を選ばず効く置き場所が合う。調査の依頼では詳しい報告書の形にしたいなど、場面で形が変わるなら、スキルにして使い分ける。毎回の依頼に書くのは、その 1 回だけ形を変えたいときに限る。

## 必ず守らせたい形式は仕組みで {#guaranteed}

書式や長さの指定は、依頼に書くお願いである。守られる傾向は上げるが、保証はしない。人が読む返事なら、多少崩れても読めるので、お願いで足りる。

困るのは、コードが返事を読む場合である。返事を JSON として解析して次の処理へ渡すときは、形が 1 か所崩れるだけで処理が止まる。このときは、形式を保証する仕組みを使う。API の structured outputs は、出力を指定したスキーマに合う形にする。依頼に書く「お願い」と違い、形を破る出力を仕組みの側で防ぐ。強制力は <!-- gen:begin feature structured-outputs/enforcement -->鍵<!-- gen:end feature structured-outputs/enforcement --> である。

使い方は <!-- link:begin structured-outputs-basics#two-modes -->[structured outputs（形式を保証する） › JSON outputs と strict tool use](../api/structured-outputs-basics.md#two-modes)<!-- link:end --> が扱う。

Claude Code の `-p` で形を指定する手は <!-- link:begin structured-outputs-basics#claude-code -->[structured outputs（形式を保証する） › Claude Code の -p で形を指定する](../api/structured-outputs-basics.md#claude-code)<!-- link:end --> が扱う。

形が保証されない場合と、形が正しくても中身は別に確かめる理由は、<!-- link:begin structured-outputs-basics#not-guaranteed -->[structured outputs（形式を保証する） › 形が保証されない場合](../api/structured-outputs-basics.md#not-guaranteed)<!-- link:end --> にある。

古い助言に、応答の先頭を書いて続けさせる prefill で JSON の形を強制する手がある。新しい世代のモデルは、最後のターンを assistant の役で書いた要求をエラーで断る。形の強制は structured outputs に替え、前置きを省かせたいときは直接指示する。台帳の行は <!-- link:begin outdated-advice-ledger#prefill-for-json -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#prefill-for-json)<!-- link:end --> にあり、prefill からの移行は <!-- link:begin structured-outputs-basics#from-prefill -->[structured outputs（形式を保証する） › prefill からの移行](../api/structured-outputs-basics.md#from-prefill)<!-- link:end --> が扱う。

!!! example "判断例：返事を JSON で受け取りたい"
    - **状況**：返事を JSON で受け取り、別の処理に渡す小さなスクリプトを作っている。
    - **迷う候補**：形を指示と例で書き、解析できなければ検査して再試行する。structured outputs で形を保証する。
    - **選んだもの**：試作の間は前者。処理が止まると困る本番の経路は後者。
    - **理由**：失敗しても再試行でき、呼び出しの回数や遅れを許せるなら、指示と検査で足りる。失敗の許されない経路は、お願いでなく仕組みに移す。例外を許さない禁止を仕組みへ移す考え方は <!-- link:begin say-what-you-want#two-layers -->[否定形ではなく、望む形で書く › 例外のない禁止は仕組みへ（二層）](say-what-you-want.md#two-layers)<!-- link:end --> と同じである。

## 何に効くか {#effects}

このページの技法は、原理「見せる」に当たる。Claude は、望む形を依頼の文面からしか知れない。文面は、書かれた中身だけでなく、書式そのものが見本になる。形を言葉で注文しながら、文面を別の形で書くと、見本と注文が食い違う。

防ぐ原因は 2 つある。

- **見えていない**：望む書式・長さ・読み手・用途が Claude に見えていない。見えないと、Claude は一般的な書き方で埋め、見出しと箇条書きの多い返事になりやすい。読み手と用途を渡し、望む形を示すと、埋める余地が減る。
- **合っていない**：返事の形と使う場面が食い違っている。チャットで流し読みする返事が報告書の書式になる。コードが読む返事が、人向けの文章になる。場面に合う形を指定し、機械が読むなら仕組みで保証する。

## 効かない場面とやりすぎ {#limits}

形と長さの指定は、次の場面で効きにくい。

- **禁止を重ねても守られないとき**：言葉を足すより、望む形で書き直す。例外を許さないなら、仕組みに移す。どちらも <!-- link:begin say-what-you-want#limits -->[否定形ではなく、望む形で書く › 効かない場面とやりすぎ](say-what-you-want.md#limits)<!-- link:end --> が扱う。
- **形を言葉にしにくいとき**：注文を長くするより、望む形の例を見せる。例を見せる側の注意は <!-- link:begin show-examples#overfit -->[例を見せる › 例にだけ合う出力に気をつける](show-examples.md#overfit)<!-- link:end --> が扱う。
- **短くさせすぎたとき**：上限だけを決めると、残したい根拠や前提まで削られることがある。残したいものは名指しする。
- **注文同士が食い違うとき**：「簡潔に」と「根拠まで詳しく」を同時に頼むと、どちらに寄るかが定まらない。どちらを優先するかを書く。
- **モデルの傾向と合わないとき**：書式を控えめにする傾向のモデルでは、古い「markdown を使うな」の注文が不要なことがある。モデルを替えたら、注文を見直す。その傾向は <!-- link:begin model-quirks#official-guidance -->[モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向](../models/model-quirks.md#official-guidance)<!-- link:end --> で確かめる。
- **文章の質が問題のとき**：書式や長さでなく、言い回しや文体が気になるなら、<!-- link:begin requesting-prose -->[文章を頼むとき（読み手・目的・手本を渡す）](requesting-prose.md)<!-- link:end --> と <!-- link:begin less-ai-sounding-japanese -->[日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)<!-- link:end --> を引く。

注文を細かくしすぎないことも要る。書式の規則を何行も並べると、守らせたいことが埋もれ、依頼の中身より形の話が長くなる。読み手、目的、形の大枠を渡し、崩れた箇所だけ足す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [否定形ではなく、望む形で書く](say-what-you-want.md)

**関連**

- [例を見せる](show-examples.md)
- [structured outputs（形式を保証する）](../api/structured-outputs-basics.md)
- [モデル別の癖と、プロンプトの合わせ方](../models/model-quirks.md)
- [XML タグで区切る](xml-tags.md)
- [文章を頼むとき（読み手・目的・手本を渡す）](requesting-prose.md)
- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)
- [出力スタイルで応答の仕方を切り替える](../cli/output-style-modes.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 調子と形式を揃えたいとき（Styles を使っていた場合）](../app/where-to-put-instructions.md#styles)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
