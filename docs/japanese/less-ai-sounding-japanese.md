---
id: less-ai-sounding-japanese
title: 日本語の「AI 臭さ」を減らす
aliases: [AI っぽい日本語, 定型の言い回し, 日本語の推敲, 日本語推敲スキル, 読みやすい日本語にする]
type: recipe
field: japanese
chapter: 文体と表記
order: 70
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [文章]
summary: 定型の言い回し・過剰な装飾・硬すぎる漢字遣いなど、読みにくさの型を具体的に挙げて直させる。AI が書いたと分からなくするためではなく、読み手のための品質として直す。
signs:
  - {type: symptom, text: 推敲を頼んでも、日本語の言い回しの癖が直らない}
  - {type: symptom, text: 太字や箇条書きが多く、読み物として読みにくい}
  - {type: goal, text: 推敲の手順を、決まった形で毎回かけたい}
prerequisites: [requesting-prose]
related: [consistent-politeness, consistent-notation, textlint-hook, show-examples, how-skills-load, writing-skills, skills-in-the-app, vetting-extensions, disclosure-and-provenance]
tracks: [app-skills, skills]
sources: [cc-docs-skills, hc-skills-what]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 読みにくさの型を具体的に挙げる, anchor: patterns}
  - {title: 自分の文章を手本にする, anchor: own-writing}
  - {title: 推敲を書く手順と分ける, anchor: revise-step}
  - {title: 推敲をスキルにする（文体を保つか、構成から直すか）, anchor: proofreading-skill, level: 仕組みにする}
  - {title: lint に任せる所と、判断の要る所, anchor: lint-vs-judgment}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：定型の言い回し・過剰な装飾・硬すぎる漢字遣いなど、読みにくさの型を具体的に挙げて直させ、推敲を毎回同じ形でかけられる。
    - **いつ引くか**：推敲を頼んでも言い回しの癖が直らないとき。太字や箇条書きが多く、読み物として読みにくいとき。推敲の手順を、決まった形で毎回かけたいとき。
    - **前提**：<!-- link:begin requesting-prose -->[文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI っぽい日本語・定型の言い回し・日本語の推敲・日本語推敲スキル・読みやすい日本語にする
<!-- textlint-enable -->

日本語の「AI 臭さ」を減らす手順を、用途の順に並べる。ここで言う「AI 臭さ」は、読み手が読みにくいと感じる言い回しと書式の型である。直す目的は読み手のための品質であり、AI が書いたと分からなくすることではない。

## 先に整える守り {#guards}

推敲を頼む前に、次の 4 つを決める。直す手順より前に決めておくと、推敲が的外れになりにくい。

- **読み手と目的を渡す**：誰が何のために読む文章かを、先に伝える。渡し方は <!-- link:begin requesting-prose#reader -->[文章を頼むとき（読み手・目的・手本を渡す） › 読み手と目的を渡す](../prompting/requesting-prose.md#reader)<!-- link:end --> にある。
- **文体を決める**：です・ますか、だ・であるかを揃える。決め方は <!-- link:begin consistent-politeness#guards -->[です・ます／だ・であるを揃える › 先に決めておくこと](consistent-politeness.md#guards)<!-- link:end --> にある。推敲の依頼が文体まで変えてしまうのを防ぐ。
- **元の文章を残す**：推敲は意味を変えることがある。元のファイルは残し、差分で確かめられる状態にしておく。
- **隠す目的にしない**：この手順が減らすのは読みにくさであり、AI を使ったという事実ではない。AI を使ったことの開示と出所の記録は別の話で、<!-- link:begin disclosure-and-provenance#four-points -->[AI 利用の開示と出所の記録 › 開示・相談・出所・意図の四つの観点](../safety/disclosure-and-provenance.md#four-points)<!-- link:end --> で扱う。

## 読みにくさの型を具体的に挙げる {#patterns}

「もっと自然に」「AI っぽくなく」と形容詞で頼むと、Claude には何を直せばよいかが見えない。嫌な箇所の型を、例つきで挙げて頼む。嫌な点を例で示すと直りやすい理由は <!-- link:begin requesting-prose#concrete-dislikes -->[文章を頼むとき（読み手・目的・手本を渡す） › 嫌な点は例で示す](../prompting/requesting-prose.md#concrete-dislikes)<!-- link:end --> にある。

次の表は、読みにくさの型の例である。測って作った一覧ではないので、自分の読み手が嫌がる型に入れ替えて使う。

| 型 | 例 | 直し方 |
| --- | --- | --- |
| 前置きと締めの定型 | 「見ていきましょう」「いかがでしたか」「と言えるでしょう」 | 削る。結論を先に書く |
| 同じ形の反復 | 「単なる A ではなく B」を何度も使う | B だけを書く |
| ぼかした語 | 「重要」「効果的」「様々な」 | 数値、条件、具体名に替える |
| 過剰な書式 | 段落ごとに太字、小さな見出し、細切れの箇条書き | つながった説明は段落に戻す |
| 硬すぎる漢字遣い | 「実施する」「行う」「に関して」 | 手本の書き方に合わせて開く |
| 冗長な丁寧表現 | 「することが可能です」「させていただきます」 | 「できる」「する」にする |

同じ元の文章で、頼み方を替えた例を並べる。

!!! example "判断例：形容詞で頼むか、型を挙げて頼むか"
    - **状況**：解説文の下書きを推敲させたい。前置きと「単なる A ではなく B」の形が目立つ。
    - **迷う候補**：「もっと自然な日本語に直して」と頼む。または、直す型を挙げて頼む。
    - **選んだもの**：型を挙げて頼む。「見ていきましょう」のような前置きは削る、「単なる A ではなく B」は B だけにする、と書く。
    - **理由**：形容詞の依頼では、直す範囲が毎回変わる。型を挙げた依頼なら、直した箇所が一覧と照らして確かめられる。ただし、挙げていない型は直らないので、残った癖は型として足す。

直しの例を 1 つ示す。

- 前：「それでは、ログの集計について見ていきましょう。集計は単なる作業ではなく、運用を支える重要な工程だと言えるでしょう。」
- 後：「ログの集計は、障害の報告の元になる。」

後の文は、元の文にない事実を足している。具体的にする直しには、Claude の知らない情報が要る。足してほしい情報は書き手が渡し、渡さないときは、ぼかした語を直さず一覧に残させる。

## 自分の文章を手本にする {#own-writing}

型の一覧のほかに、自分が書いた文章を手本として渡す。言葉にしにくい好み（文の長さ、接続の仕方、漢字の開き方）まで伝わるためである。手本の渡し方と理由は <!-- link:begin show-examples#own-writing -->[例を見せる › 自分の文章を手本にする](../prompting/show-examples.md#own-writing)<!-- link:end --> と <!-- link:begin show-examples#why -->[例を見せる › なぜ例が効くのか](../prompting/show-examples.md#why)<!-- link:end --> にある。

- **手本の選び方**：同じ種類の文章（技術メモなら技術メモ）を、自分で書いたものから数本選ぶ。Claude が書いた文章を手本にすると、直したい癖をそのまま手本にしてしまう。
- **何を真似させるか**：文の長さ、文末、語の選び方、書式の量に限る。手本の内容は使わせない。
- **やりすぎの確認**：手本に似すぎて、手本にない題材まで同じ言い回しになることがある。見分け方は <!-- link:begin show-examples#overfit -->[例を見せる › 例にだけ合う出力に気をつける](../prompting/show-examples.md#overfit)<!-- link:end --> にある。

## 推敲を書く手順と分ける {#revise-step}

書かせる依頼と推敲の依頼を、別の手順にする。分ける理由と頼み方は <!-- link:begin requesting-prose#revise -->[文章を頼むとき（読み手・目的・手本を渡す） › 推敲を別の手順に分ける](../prompting/requesting-prose.md#revise)<!-- link:end --> にある。書く依頼に型の一覧を全部入れると、内容の依頼と文体の依頼が混ざる。

1. **書かせる**：内容と構成を決めて書かせる。型の一覧は入れない。終わりの確かめ：書きたかった内容が、抜けなく入っている。
2. **推敲を頼む**：別の依頼で、読み手と目的、型の一覧、手本の文章を渡す。意味を変えないことと、直した箇所の一覧を返すことも指定する。終わりの確かめ：一覧が出ており、一覧にない箇所は元のままである。
3. **差分を見る**：数値、固有名詞、引用、否定と肯定が変わっていないかを、元の文章と並べて見る。終わりの確かめ：意味の変わった箇所がない。
4. **残りを拾う**：機械で見つかる揺れは lint（決めた規則で文章を機械的に検査する道具）に任せ、残りは読み直す。どこまでを lint に任せるかは、この後の「lint に任せる所と、判断の要る所」の節で扱う。終わりの確かめ：lint の指摘が 0 件で、人が判断する箇所も読み終えている。

推敲の依頼の雛形を載せる。<読み手> などの欄を埋めて使う。

<!-- gen:begin snippet less-ai-sounding-japanese/revise-request -->
<!-- textlint-disable -->

???+ example "雛形：推敲の観点を書いた依頼"

    ```markdown
    次の文章を推敲してください。読み手は <読み手>、目的は <目的> です。

    直す点は、次の型だけです。ほかの箇所は直さないでください。
    - 「見ていきましょう」「いかがでしたか」のような前置きと締めの定型は削る
    - 「単なる A ではなく B」の形は、続けて使わない。B だけを書く
    - 「重要」「効果的」「様々な」のようなぼかした語は、根拠が元の文にないなら、直さずに一覧へ「根拠が要る」と書く
    - 太字・箇条書き・見出しは、手本の文章にある量まで減らす
    - 「実施する」「行う」のような硬い語は、手本の文章の書き方に合わせる
    - 文末は <だ・である／です・ます> に揃える

    守ること。
    - 意味、数値、固有名詞、引用は変えない。足りない情報を補わない
    - 手本の文章の中身は使わない。文の長さ、文末、語の選び方だけを参考にする
    - 直した箇所を「前 → 後 → 当てはまった型」の一覧で先に返し、直した文章はその後に置く

    <手本の文章>

    <推敲する文章>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet less-ai-sounding-japanese/revise-request -->

## 推敲をスキルにする（文体を保つか、構成から直すか） {#proofreading-skill}

推敲の手順を毎回同じ形でかけたいときは、スキルにする。スキルは、説明文だけが常に読み込まれ、本文は使うときに読まれる。仕組みは <!-- link:begin how-skills-load#what-happens -->[スキルの考え方（手順を必要なときだけ読む） › 何が起きるか](../extend/how-skills-load.md#what-happens)<!-- link:end --> にある。長い型の一覧を、常駐の指示から外せる。

スキルの作り方は <!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](../extend/writing-skills.md#minimal)<!-- link:end --> にある。ここでは、推敲のスキルに固有の判断を扱う。

### 文体を保つか、構成から直すか

公開されている日本語の推敲スキルには、方針が 2 つに分かれる。1 つは、文体と構成を保って文だけを直す方針である。もう 1 つは、見出しと段落を組み替える方針である。比べた記事は 1 回の出力を見ただけで、どちらがよいとは決められない。選ぶ軸は、自分の文章の状態である。

!!! example "判断例：文だけを直すか、構成から直すか"
    - **状況**：です・ます調の技術ブログの下書き。見出しの順は、自分で決めた。
    - **迷う候補**：文体と構成を保って文だけ直すスキル。または、構成から組み替えるスキル。
    - **選んだもの**：文だけ直すスキル。
    - **理由**：構成が決まっているなら、構成を組み替える直しは意図とずれる。しかも差分が大きく、意味が変わったかを確かめにくい。逆に、書きながら組み立てた下書きで、論の順が崩れているなら、構成から直す方針が合う。

### 自作のスキルの例

文体と構成を保つ方針のスキルの例を載せる。構成を変えたい気持ちが出たときも、直さずに提案として書かせる。

<!-- gen:begin snippet less-ai-sounding-japanese/proofread-ja -->
<!-- textlint-disable -->

??? example "雛形：文体を保つ日本語の推敲スキル（SKILL.md）"

    ```markdown
    ---
    name: proofread-ja
    description: 日本語の文章を推敲するときに使う。文体と構成を保ったまま、前置きや締めの定型、ぼかした語、過剰な書式を直し、直した箇所を一覧で返す。
    ---

    # 日本語の推敲

    ## 進め方

    1. 元の文章から文体（です・ます／だ・である）を読み取る。文体は変えない。
    2. 次の「直す型」に当てはまる箇所を探す。
    3. 意味、数値、固有名詞、引用を変えずに直す。
    4. 直した箇所を「前 → 後 → 当てはまった型」の一覧で返す。直した文章は一覧の後に置く。

    ## 直す型

    - 前置きと締めの定型（「見ていきましょう」「いかがでしたか」など）は削る。
    - 「単なる A ではなく B」の形は続けて使わず、B だけを書く。
    - 太字・箇条書き・見出しは、元の文章の量を超えて足さない。
    - 硬い語（「実施する」「行う」など）は、元の文章の書き方に合わせる。

    ## 守ること

    - 見出しと段落の順（構成）は変えない。変えたほうがよいと思ったら、直さずに提案として一覧の末尾へ書く。
    - 根拠のないぼかした語（「重要」「効果的」「様々な」など）は、直さずに「根拠が要る」と一覧へ書く。
    - 元の文章にない情報を足さない。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet less-ai-sounding-japanese/proofread-ja -->

=== "アプリ"

    自作のスキルを入れる手順は <!-- link:begin skills-in-the-app#upload -->[アプリでスキルを使う › 自作のスキルを入れる](../app/skills-in-the-app.md#upload)<!-- link:end --> にある。設定の場所の名前は変わりつつあるので、画面の名前は上の説明で確かめる。使われないときの確かめ方は <!-- link:begin skills-in-the-app#not-triggered -->[アプリでスキルを使う › 使われないとき](../app/skills-in-the-app.md#not-triggered)<!-- link:end --> にある。

=== "Claude Code"

    「自作のスキルの例」の SKILL.md を `.claude/skills/proofread-ja/SKILL.md` として置く。自分から `/proofread-ja` で呼ぶことも、説明に合う依頼で Claude に選ばせることもできる。補助ファイルへの分け方は <!-- link:begin writing-skills#supporting-files -->[スキルの作り方 › 補助ファイルとスクリプトに分ける](../extend/writing-skills.md#supporting-files)<!-- link:end --> にある。

### 入れる前の確認

他人が公開したスキルを使う場合は、入れる前に出所と中身を確かめる。入れたスキルは自分の権限で動き、後から中身が変わることもある。確かめる観点は <!-- link:begin vetting-extensions#guards -->[MCP・プラグイン・スキルを入れる前の確認 › 先に整える守り](../safety/vetting-extensions.md#guards)<!-- link:end --> と <!-- link:begin vetting-extensions#read-contents -->[MCP・プラグイン・スキルを入れる前の確認 › 中身を読む（道具の説明・フック・スクリプト）](../safety/vetting-extensions.md#read-contents)<!-- link:end --> にある。推敲のスキルでも、本文にスクリプトの実行が書かれていないかを読む。

## lint に任せる所と、判断の要る所 {#lint-vs-judgment}

読みにくさの型のうち、機械で見つけられるものは lint に任せる。機械で見つけられないものは、人が読んで決める。

| 任せ方 | 対象 | 扱う場所 |
| --- | --- | --- |
| lint で見つける | 文末の文体の混在 | <!-- link:begin consistent-politeness#lint -->[です・ます／だ・であるを揃える › 混在を lint で見つける](consistent-politeness.md#lint)<!-- link:end --> |
| lint で見つける | 表記ゆれと、開く漢字の一覧 | <!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](consistent-notation.md#single-source)<!-- link:end --> |
| lint で見つける | 決めた定型句の出現、1 文の長さ、同じ文末の連続 | <!-- link:begin textlint-hook#rules -->[textlint をフックで回す › どのルールを機械に任せるか](textlint-hook.md#rules)<!-- link:end --> |
| 人が判断する | ぼかした語に根拠があるか | 書き手が根拠を渡す |
| 人が判断する | 前置きや締めが、この読み手に要るか | 読み手と目的で決める |
| 人が判断する | 構成と論の順が合っているか | 読み直す |

lint は、書いた直後に走らせて Claude に直させると手間が減る。仕組みは <!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](textlint-hook.md#post-tool-use)<!-- link:end --> にある。規則は少なく保つ。規則を増やしすぎると、本来の内容より規則を満たすことに引かれる。詳しくは <!-- link:begin textlint-hook#failure-and-few -->[textlint をフックで回す › フックが落ちたときと、規則を増やしすぎないこと](textlint-hook.md#failure-and-few)<!-- link:end --> にある。

定型句の一覧を lint に入れると、その句は消えても、別の定型句に置き換わることがある。機械で拾えるのは型の一部であり、残りは判断である。

## 確かめ方 {#verify}

推敲の後に、次の 4 つを順に確かめる。

- **意味が変わっていないか**：元の文章と差分を並べ、数値、固有名詞、引用、否定と肯定を見る。直した箇所の一覧と差分が合っているかも見る。
- **型が減ったか**：挙げた型を、文章の中で検索する。残った箇所は、一覧で「直さなかった」と説明されているかを見る。
- **文体と表記が揃っているか**：lint を流し、文体と表記の揺れを確かめる。
- **読み手に読ませる**：書き手は自分の癖に気づきにくい。同じ種類の文章を読む人に、1 回読んでもらう。

同じ元の文章で、型の一覧を渡す前後の出力を並べて比べると、一覧が効いたかが見える。

## 失敗したとき {#failure}

- **癖が残る**：残った癖を、例つきの型として一覧に足す。足し方は <!-- link:begin requesting-prose#concrete-dislikes -->[文章を頼むとき（読み手・目的・手本を渡す） › 嫌な点は例で示す](../prompting/requesting-prose.md#concrete-dislikes)<!-- link:end --> にある。禁止だけを増やすと別の定型に置き換わるので、「最後の文は結論で止める」のように、望む形も書く。
- **意味が変わった**：「意味、数値、固有名詞、引用は変えない」と指定し、直す範囲を段落ごとに分ける。直した箇所の一覧がないなら、一覧を返すよう頼み直す。
- **文体が変わった・揺れた**：文体の指定を見直す。指定の置き方と、残った混在の直し方は <!-- link:begin consistent-politeness#specify -->[です・ます／だ・であるを揃える › 文体は一行で、理由と一緒に指定する](consistent-politeness.md#specify)<!-- link:end --> と <!-- link:begin consistent-politeness#failure -->[です・ます／だ・であるを揃える › 揺れが残ったとき](consistent-politeness.md#failure)<!-- link:end --> にある。
- **表記が変わった**：用語と漢字の一覧を渡す。手順は <!-- link:begin consistent-notation#glossary -->[表記ゆれと漢字の開き › 表記の一覧（用語集）を作る](consistent-notation.md#glossary)<!-- link:end --> にある。
- **スキルの不発**：説明文が依頼の言葉と合っているかを見る。確かめ方は <!-- link:begin writing-skills#evaluate -->[スキルの作り方 › 効いているかを確かめる](../extend/writing-skills.md#evaluate)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)

**関連**

- [です・ます／だ・であるを揃える](consistent-politeness.md)
- [表記ゆれと漢字の開き](consistent-notation.md)
- [textlint をフックで回す](textlint-hook.md)
- [例を見せる](../prompting/show-examples.md)
- [スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)
- [スキルの作り方](../extend/writing-skills.md)
- [アプリでスキルを使う](../app/skills-in-the-app.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
