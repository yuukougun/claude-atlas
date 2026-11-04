---
id: align-japanese-output
title: 日本語の出力を揃える：お願いで足りること、仕組みが要ること
nav_title: 日本語の出力を揃える仕組み
aliases: [日本語の出力品質, 返答の言語と文体を固定する, お願いと鍵（日本語の場合）]
type: concept
field: japanese
chapter: 考え方
order: 20
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 確かめる]
prevents: [縛っていない, 確かめていない]
scenes: [開発, 文章, チーム]
summary: 返答の言語・文体・表記を揃える手段を、届く範囲と強制力で選び分けられる。指示はどれも保証にならず、仕組みで止められる場所にも限りがあることを前提に組む。
signs:
  - {type: situation, text: 日本語の指示を足しても揃わず、仕組みにすべきか迷っている}
  - {type: goal, text: 日本語の出力を、いつも同じ文体と表記にしたい}
  - {type: situation, text: チームで日本語の文書を Claude に書かせる}
wave: 1
prerequisites: [request-vs-lock]
related: [keep-replies-in-japanese, consistent-politeness, consistent-notation, textlint-hook, replies-in-english, inconsistent-japanese-style, where-to-put-instructions, claude-md-vs-rules-skills-styles, request-lock-table, when-to-lock, output-style-modes]
tracks: [language-setting, claude-md, output-styles, hooks, personal-instructions, project-instructions, app-skills]
outdated_advice: [styles-for-tone]
sources: [cc-docs-settings-reference, cc-docs-memory, cc-docs-output-styles, cc-docs-hooks, cc-docs-hooks-guide, cc-docs-best-practices, cc-docs-context-window, cc-docs-cloud-environments, api-docs-multilingual-support, hc-personalization, hc-styles-to-skills, hc-projects-manage, hc-skills-what, cc-issue-96326, cc-issue-98633, cc-issue-99704, zenn-yuki-a01e472d]
volatility: 中
sections:
  - {title: 日本語の出力が揃わない形と、手段の分け方, anchor: what-happens}
  - {title: お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示, anchor: request-layer}
  - {title: 確かめて差し戻す層：フックと lint, anchor: lock-layer, level: 仕組みにする}
  - {title: 届く範囲（サブエージェント・圧縮の後・クラウドのセッション）, anchor: reach}
  - {title: アプリには指示しかない, anchor: app}
  - {title: 縛る規則は少なく保つ, anchor: keep-few}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：返答の言語・文体・表記を揃える手段を、届く範囲と強制力で選び分けられる。指示はどれも保証にならず、仕組みで止められる場所にも限りがある。
    - **いつ引くか**：日本語の指示を足しても揃わず、仕組みにすべきか迷っているとき。日本語の出力を、いつも同じ文体と表記にしたいとき。チームで日本語の文書を Claude に書かせるとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：日本語の出力品質・返答の言語と文体を固定する・お願いと鍵（日本語の場合）
<!-- textlint-enable -->

日本語の出力を揃えるとは、返答の言語・文体・表記を、いつも同じにすることである。手段は、指示を置く「お願い」の層と、返答を機械で確かめて差し戻す「鍵」の層に分かれ、どちらにも届く範囲の限りがある。このページは、その手段を選び分ける基準を示す。お願いと鍵の一般的な説明は、「<!-- link:begin request-vs-lock#why -->[お願いと鍵（決定論的か、非決定論的か） › なぜそうなるか](../basics/request-vs-lock.md#why)<!-- link:end -->」にある。

## 日本語の出力が揃わない形と、手段の分け方 {#what-happens}

日本語の出力が揃わない形は 3 つある。返答の言語が英語に戻る、文体（です・ます調とだ・である調）が混ざる、表記（用語の書き方や漢字の開き方）が揺れる、である。

どれも、CLAUDE.md に書いたのに起きる点が共通する。GitHub の issue には、CLAUDE.md とメモリと会話での繰り返しの指示を重ねても英語に戻る、訂正の直後は日本語になるがすぐ英語に戻る、という報告がある（根拠：中。複数の報告が一致する）。公式も、CLAUDE.md を強制される設定ではなく文脈として扱い、厳密に守られる保証はないと書く。指示を増やしても足りない場面があるのは、量の問題ではなく、指示という手段の性質による。

手段は、揃えたいものごとに分ける。ターンとは、依頼を送ってから最後の返事までの 1 区切りである。lint とは、文章やコードの決まり違反を機械で見つける検査である。次の表は、お願いで減らせる範囲と、鍵で止められる範囲を並べたものである。

| 揃えたいもの | 鍵で止められる範囲 | お願いで減らせる範囲 |
| --- | --- | --- |
| 返答の言語 | ターンの終わりの最後の返事（Stop フック）。ツールの合間の一言は止められない | `language` の設定、CLAUDE.md、出力スタイル |
| 文体（です・ます調など） | 書いたファイルの中の混在（lint） | 一行の指定と手本の文章 |
| 表記（用語・漢字の開き方） | 辞書を持たせた lint で見つかる揺れ | 用語の一覧 |
| 読みやすさ・自然さなど判断を含むもの | 鍵にしない | 例と理由を渡す |

表の「鍵で止められる範囲」が機械で判定できるものに限られる理由は、[鍵の層の節](#lock-layer)で述べる。各行の頼み方は、「<!-- link:begin consistent-politeness#specify -->[です・ます／だ・であるを揃える › 文体は一行で、理由と一緒に指定する](consistent-politeness.md#specify)<!-- link:end -->」と「<!-- link:begin consistent-notation#glossary -->[表記ゆれと漢字の開き › 表記の一覧（用語集）を作る](consistent-notation.md#glossary)<!-- link:end -->」が持つ。

## お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示 {#request-layer}

お願いの層は、返答を揃える指示を、Claude が読む場所に置く層である。置き場所は面で違う。Claude Code では、返答の言語を指定する `language` の設定、常に効かせる規則を書く CLAUDE.md、応答の形を決める出力スタイルがある。アプリでは、全部の会話に使われる Claude への指示、プロジェクトの中の会話に使われるプロジェクトの指示、場面ごとの手順を置くスキルがある。次の表は、このページが扱う機能の面と強制力、読み込みの時期、圧縮の後に残るかを並べたものである。

<!-- gen:begin compare 面 強制力 読み込みの時期 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 面 | 強制力 | 読み込みの時期 | 圧縮で残るか |
| --- | --- | --- | --- | --- |
| [language の設定（返答の言語）](keep-replies-in-japanese.md) | Claude Code | お願い | — | 未確認 |
| [CLAUDE.md](../extend/what-to-put-in-claude-md.md) | Claude Code | お願い | セッション開始 | 残る |
| 出力スタイル（output styles）（準備中） | Claude Code | お願い | セッション開始と切り替えたとき | 残る |
| [フック（hooks）](../enforce/hooks-basics.md) | Claude Code | 鍵 | イベントが起きたとき | 残る |
| [Claude への指示（Instructions for Claude）](../app/where-to-put-instructions.md) | アプリ | お願い | — | 未確認 |
| プロジェクトの指示（project instructions）（準備中） | アプリ | お願い | — | 未確認 |
| スキル（アプリ。skills）（準備中） | アプリ | お願い | — | 未確認 |

<!-- textlint-enable -->
<!-- gen:end compare 面 強制力 読み込みの時期 圧縮で残るか -->

お願いの層は、どれも Claude が読んで従うかを決める。`language` は、Claude Code が値を確かめず、「いつもその言語で答える」という指示としてそのまま渡すだけである。CLAUDE.md は文脈として扱われ、出力スタイルは「Claude が従う指示で、何も強制しない」と公式が書く。したがって、お願いの層でできるのは、揃う確率を上げることまでである。

英語に戻る原因は、公式の文書に書かれていない。英語のツール出力を読んだ後に戻る報告が多いが、なぜ戻るかは分かっていない。モデルを替えると増減したという報告もあるが、単独の例で、モデルの切り替えと Claude Code の更新が同じ日に重なった例もある（根拠：弱）。モデルごとの癖は固定した事実として扱わない。

お願いの層で重ねるときの要点は 3 つある。

- 揃えたい対象を名指しする。言語、文体、表記は、別々の指示にする。
- 手本と理由を添える。書き方は「<!-- link:begin consistent-politeness#example -->[です・ます／だ・であるを揃える › 手本の文章を見せる](consistent-politeness.md#example)<!-- link:end -->」にある。
- 置き場所を選ぶ。毎回読まれる場所に置くほど、読み落としは減る。置き場所の比べ方は「<!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](../extend/claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end -->」にある。

出力スタイルと日本語の応答の関係は、「<!-- link:begin output-style-modes#japanese -->出力スタイルで応答の仕方を切り替える › 日本語の応答との関係（準備中）<!-- link:end -->」で扱う。

## 確かめて差し戻す層：フックと lint {#lock-layer}

確かめて差し戻す層は、返答やファイルを機械で見て、揃っていなければ理由を付けて Claude に返し、書き直させる層である。お願いと違い、この層は会話の外で動くので、Claude が従うかどうかに依らず毎回動く。ただし、動く場所は限られる。

2026-11-03 に公式の文書で確かめた範囲では、強制できる場所は、ターンの終わりとツールの前後だけである。

- **ターンの終わり**：Stop フックは、最後の返事を受け取れる。差し戻す理由を返すと、Claude は終わらずに続ける。差し戻しの回数には上限があり、二重に差し戻さないための印も用意されている。
- **ツールの前**：PreToolUse フックは、次のツールの呼び出しを止め、理由を Claude に返せる。
- **ツールの後**：PostToolUse フックは、終了コードで標準エラーを Claude に返せる。書いたファイルを lint にかけて、残った違反を返す用途に向く。

ツールの合間の短い一言は、画面へ出る前に止める仕組みがない。MessageDisplay フックは、表示のときだけ文を差し替える。止めることも、Claude が見る内容を変えることもできない。英語の一言が一度は画面に出ることは、公式の仕組みでは防げない。

鍵にできるのは、機械で判定できる規則だけである。言語は、最後の返事の中の日本語の文字の割合などで判定する。公式の文書に判定の例はなく、判定の書き方は自分で決める。実装の例は「<!-- link:begin keep-replies-in-japanese#stop-hook -->[日本語で返し続けさせる › Stop フックで最後の返事を確かめる](keep-replies-in-japanese.md#stop-hook)<!-- link:end -->」にある。文体と表記は、辞書を持たせた lint で、混在や揺れを見つけられる。textlint や Vale を使う公式の例は、調べた範囲では見つからなかった。ただし、編集の後に整形ツールを走らせる公式の例（Prettier）と、同じ形になる。実践者が textlint を PostToolUse フックで走らせた例もある（根拠：弱。単独の事例）。手順は「<!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](textlint-hook.md#post-tool-use)<!-- link:end -->」にある。

鍵には、拾えない場所もある。PostToolUse を `Edit|Write` に合わせたフックは、シェルで書き換えたファイルには動かない。どこから書き換えても拾うなら、FileChanged を使う。詳しくは「<!-- link:begin textlint-hook#gaps -->[textlint をフックで回す › 拾えない書き込み（シェルで書いたファイル）](textlint-hook.md#gaps)<!-- link:end -->」にある。また、本当に強制するなら、command か http の型のフックを使う。prompt と agent の型は、別のモデルが判断するので決定的ではない。

判断を含む規則（読みやすさ、自然さ）は、機械で判定できないので鍵にしない。この線引きは「<!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](../enforce/when-to-lock.md#what-not-to-lock)<!-- link:end -->」にある。

## 届く範囲（サブエージェント・圧縮の後・クラウドのセッション） {#reach}

手段は、置いた場所によって届く範囲が違う。主の会話に効く手段が、サブエージェントや圧縮の後やクラウドのセッションに届くとは限らない。次の表は、2026-11-03 に公式の文書で確かめた範囲を、手段ごとに並べたものである。「書かれていない」は、調べた範囲の公式の文書に記述がないことを指し、届かないことを意味しない。

| 手段 | サブエージェント | 圧縮の後 | クラウドのセッション |
| --- | --- | --- | --- |
| `language` の設定 | 書かれていない | 書かれていない | ユーザー設定は届かない |
| CLAUDE.md | 届く。ただし組み込みの Explore と Plan、`omitClaudeMd` のサブエージェントには届かない | プロジェクトの根のものは読み直される。入れ子のものは要約に消える | リポジトリのものは届く。ユーザー用の `~/.claude/CLAUDE.md` は届かない |
| 出力スタイル | fork を除くサブエージェントには効かない | 効く | 書かれていない |
| フック | サブエージェント用の SubagentStop が、Stop と同じ形で働く | 会話の外で動くので働く | ユーザー設定のものは効かない。リポジトリの `.claude/settings.json` のものは効く |
| 会話での指示 | 届かない | 要約で消えうる | 同じ会話の中だけ |

表から読める要点は 3 つある。

1. **お願いの層は、手段ごとに届く範囲が違う。** 出力スタイルと CLAUDE.md は、サブエージェントへの届き方が違う。`language` は、届くかどうかが書かれていない。
2. **会話で言った指示は、圧縮で消えうる。** 消えない場所に置く。理由と移し先は「<!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end -->」にある。
3. **面によって届く設定が違う。** ユーザーの設定・CLAUDE.md・フック・プラグインは、クラウドのセッションに届かない。日本語の指示を確実に届けるには、リポジトリの CLAUDE.md と `.claude/settings.json` に置く。

サブエージェントは自分のシステムプロンプトで動く。必ず届けたい規則は、委任の文に書き直す。この点は、チームで共有するときにも効く。リポジトリに入れた CLAUDE.md とフックの設定は、全員のセッションとクラウドのセッションに届く。共有の手順は「<!-- link:begin textlint-hook#share -->[textlint をフックで回す › チームで共有する](textlint-hook.md#share)<!-- link:end -->」にある。届かない場所ごとの対処は、「<!-- link:begin keep-replies-in-japanese#reach -->[日本語で返し続けさせる › 届かない所（サブエージェント・圧縮の要約・クラウドのセッション）](keep-replies-in-japanese.md#reach)<!-- link:end -->」と「<!-- link:begin claude-md-vs-rules-skills-styles#reach -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示が届く範囲の違い](../extend/claude-md-vs-rules-skills-styles.md#reach)<!-- link:end -->」にある。

## アプリには指示しかない {#app}

面ごとに、使える手段が違う。アプリには指示しかなく、機械で確かめて差し戻す仕組みは、調べた範囲では見つからなかった。

=== "アプリ"

    アプリで使える手段は、Claude への指示、プロジェクトの指示、スキルである。どれも指示であり、強制の仕組みではない。置き場所の使い分けは、「<!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](../app/where-to-put-instructions.md#how-to-choose)<!-- link:end -->」にある。組織の指示が入っている場合の扱いは、「<!-- link:begin where-to-put-instructions#org-instructions -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 組織の指示があるとき](../app/where-to-put-instructions.md#org-instructions)<!-- link:end -->」にある。

    調子と形式をスタイル（Styles）で切り替える助言は、すでに古い。スキルへの移行が告知され、いつも同じ調子にするなら Claude への指示に書き、場面ごとに切り替えるならスキルにする。経緯は「<!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->」にある。移行したスキルは既定で無効なので、有効にしたかを確かめる。

    機械で確かめる仕組みがないので、揃えたい文書は、書かせた後の工程を人の側に置く。たとえば、出てきた文書を手元で lint にかける。この工程の置き方は、この辞典の推論で、実践例は確かめていない。

=== "Claude Code"

    Claude Code では、指示（`language` の設定、CLAUDE.md、出力スタイル）に、フックを重ねられる。指示で減らし、機械で判定できる分だけをフックで止める。重ねる順は、「<!-- link:begin keep-replies-in-japanese#language-setting -->[日本語で返し続けさせる › 言語の設定と、効かないときに確かめること](keep-replies-in-japanese.md#language-setting)<!-- link:end -->」から始める。

=== "API"

    API の返答の言語は、会話から推測される。公式は、本番ではシステムプロンプトで明示するのが最も確実だと書く。これもお願いである。API は、呼び出す側のコードが返答を受け取るので、判定して再び呼ぶ処理を自分で書ける。この点は、この辞典の推論で、確かめていない。

!!! example "判断例：アプリで毎回同じ文体にしたい"
    - **状況**：claude.ai のアプリで、会話ごとに文体が変わる。毎回、冒頭で文体を頼むのは手間である。
    - **迷う候補**：全部の会話に効く Claude への指示に書く。特定の案件のプロジェクトの指示に書く。
    - **選んだもの**：複数の案件で同じ文体にしたいなら Claude への指示に、案件ごとに文体が違うならプロジェクトの指示に書く。
    - **理由**：どちらも指示で、守られる保証はない。違いは効く範囲である。揃わない会話が残るなら、アプリには機械で止める手段がないため、出てきた文書を人が確かめる工程を足す。

## 縛る規則は少なく保つ {#keep-few}

鍵にする規則は、少なく絞る。鍵は例外を許さず、会話の外で働くので、増やすほど、状況に合わない規則が Claude を不適切な対処に追い込む。

公式の Best practices は、IMPORTANT などの強調を足しても守られないときの原因を、ファイルが長すぎるか、規則に例外がないかだと見る。対処は、ファイルを短くするか、フックにすることである。つまり、指示を増やして対処するのをやめ、例外のない規則だけを鍵に移す。鍵に移す合図は、「<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->」にある。

縛る規則を絞る基準は 3 つある。

- 機械で判定できる。判定が曖昧なら、お願いに残す。
- 例外がない。例外があるなら、理由と相談の基準をお願いに書く。
- 外れても致命的でない。鍵が誤って止めるときの損害を見る。

止めるときは、理由と代わりの手段を返す。フックが落ちたときの扱いと、規則を増やしすぎないことは、「<!-- link:begin textlint-hook#failure-and-few -->[textlint をフックで回す › フックが落ちたときと、規則を増やしすぎないこと](textlint-hook.md#failure-and-few)<!-- link:end -->」が持つ。

!!! example "判断例：チームの文書の文体が揃わない"
    - **状況**：チームで、Claude Code に日本語の設計文書を書かせている。CLAUDE.md に文体を書いたが、です・ますとだ・である調が混ざる。
    - **迷う候補**：CLAUDE.md の文体の指示を強調して書き足す。書いたファイルを lint にかけるフックを入れる。
    - **選んだもの**：先に、文体の指定を一行に絞り、手本の文章を添える。それでも混在が残る分だけ、lint のフックで見つけて直させる。
    - **理由**：強調の足し算は、守られなかったときの合図であり、解決にならない。一方、文体の混在は機械で見つかる。lint の規則は、混在の検出に絞って少なく保つ。

## 何に効くか {#effects}

このページが扱う原理は「縛る」と「確かめる」である。防ぐ原因は、「縛っていない」と「確かめていない」である。

- **縛る**：指示の置き場所と届く範囲を決め、例外のない規則を鍵に移す。「縛っていない」状態は、規則が会話の中だけにあり、サブエージェントや圧縮の後へ届かない場合である。
- **確かめる**：返答やファイルを機械で見て、揃っていなければ差し戻す。「確かめていない」状態は、守られたかを人が毎回読むしかない場合に当たる。

お願いの層は主に「縛る」、鍵の層は「確かめる」に重なる。ただし、どちらも保証にならない。お願いは守られず、鍵は拾える場所が限られる。

## 誤解 {#misconceptions}

- **強調や繰り返しを足せば守られる。** 強調しても守られないのは、ファイルが長すぎるか、例外のない規則だからである（Best practices）。短くするか、鍵に移す。
- **`language` を設定すれば強制される。** 値は検証されず、指示として渡されるだけである。`language` の強制力は「お願い」である（お願いの層の節の表）。
- **フックを入れれば、英語は一度も画面に出ない。** ツールの合間の一言は、止められない。止められるのは、ターンの終わりとツールの前後である。
- **lint を通せば日本語の文章の質は保証される。** lint が見つけるのは、機械で判定できる混在と揺れだけである。読みやすさは、人が確かめる。
- **アプリでも、スタイルで調子を切り替えられる。** スタイルは、スキルへの移行が告知された。経緯は、台帳の行を見る。

誤読されやすい似た機能の違いは、「<!-- link:begin claude-md-vs-rules-skills-styles#similar-names -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 混同されやすい別の機能](../extend/claude-md-vs-rules-skills-styles.md#similar-names)<!-- link:end -->」にある。症状から引くときは、「<!-- link:begin replies-in-english#diagnosis -->[英語で返ってくる › 原因を安く確かめる順](../symptoms/replies-in-english.md#diagnosis)<!-- link:end -->」と「<!-- link:begin inconsistent-japanese-style#diagnosis -->[文体や表記が揃わない › 原因を安く確かめる順](../symptoms/inconsistent-japanese-style.md#diagnosis)<!-- link:end -->」から入る。用途ごとのお願いと鍵の対応は、「<!-- link:begin request-lock-table#table -->お願いと鍵の対応表 › 用途ごとの対応表（準備中）<!-- link:end -->」にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)：Anthropic・英語・確認日 2026-11-04
- [Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)：Anthropic・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)：Anthropic・英語・確認日 2026-11-04
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] Replies drift into English right after reading English tool output, despite a CLAUDE.md rule requiring Japanese; corrections do not hold（Issue #96326）](https://github.com/anthropics/claude-code/issues/96326)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Model\] Repeatedly switches to English despite CLAUDE.md + memory + repeated in-chat instructions to reply only in Japanese（Issue #98633）](https://github.com/anthropics/claude-code/issues/98633)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Opus 5.5 ignores the CLAUDE.md language rule: 33% of replies in English vs 0% on Opus 5 (same session, same CLI)（Issue #99704）](https://github.com/anthropics/claude-code/issues/99704)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[進化版\] VSCode + Claude Code Hooksでマークダウンの文書作成を爆速化する環境構築方法](https://zenn.dev/yuki_fujisawa/articles/a01e472dc190cf)：Zenn（yuki\_fujisawa）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**次に読む**

- [日本語で返し続けさせる](keep-replies-in-japanese.md)
- [です・ます／だ・であるを揃える](consistent-politeness.md)
- [表記ゆれと漢字の開き](consistent-notation.md)
- [textlint をフックで回す](textlint-hook.md)

**関連**

- [英語で返ってくる](../symptoms/replies-in-english.md)
- [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- お願いと鍵の対応表（準備中）
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- 出力スタイルで応答の仕方を切り替える（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
