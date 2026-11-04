---
id: replies-in-english
title: 英語で返ってくる
aliases: [英語に戻る, 返事が英語になる, 日本語で返してくれない]
type: symptom
field: symptoms
chapter: 日本語の出力
order: 190
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る, 見せる]
prevents: [見えていない, 散らかっている, 縛っていない, 合っていない]
pitfalls: []
scenes: [開発, 文章]
summary: 日本語で頼んでいるのに英語で返る原因を、設定・読み込んだ英語の出力・モデル・面の順に切り分け、指示で足りるか仕組みで止めるかを決める。
signs:
  - {type: symptom, text: 返事が英語になる}
  - {type: symptom, text: 途中から英語に切り替わって戻らない}
  - {type: symptom, text: ツールの結果を読んだ後の一言だけ英語になる}
wave: 1
prerequisites: [request-vs-lock]
related: [can-i-prompt-in-japanese, commit-and-comment-language, hook-recipes, output-style-modes, forgot-after-compaction, instructions-ignored, inconsistent-japanese-style, isolate-with-safe-mode, six-causes]
routes:
  - {cause: 見えていない, to: [keep-replies-in-japanese#language-setting, settings-layers, what-subagents-dont-inherit]}
  - {cause: 散らかっている, to: [keep-replies-in-japanese#when]}
  - {cause: 縛っていない, to: [keep-replies-in-japanese#stop-hook, align-japanese-output#lock-layer, stop-hooks]}
  - {cause: 合っていない, to: [model-quirks, keep-replies-in-japanese#app-and-api, cloud-sessions-and-teleport#settings]}
tracks: [language-setting, settings, output-styles, claude-md, hooks]
outdated_advice: []
sources: [cc-docs-settings-reference, cc-docs-settings, cc-docs-output-styles, cc-docs-memory, cc-docs-hooks-guide, cc-docs-hooks, cc-issue-96326, cc-issue-96601, cc-issue-99704, cc-issue-99800, cc-issue-101940, cc-changelog]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：繰り返すなら仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：日本語で頼んでいるのに英語で返る原因を、設定・読み込んだ英語の出力・モデル・面の順に切り分け、指示で足りるか仕組みで止めるかを決められる。
    - **いつ引くか**：返事が英語になったとき。途中から英語に切り替わって戻らないとき。ツールの結果を読んだ後の一言だけ英語になるとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：英語に戻る・返事が英語になる・日本語で返してくれない
<!-- textlint-enable -->

英語で返ってくる症状は、設定が効いていない場合だけでなく、設定は効いていても読んだ英語に引きずられる場合や、モデルや面との相性の場合がある。このページは、確かめる手間が小さい順に原因を切り分ける。日本語で返させる手順の本体は、持ち主のページに任せる。

## よくある形 {#forms}

読者の言葉ごとに、先に疑う原因を添える。確かめ方は、下の診断にある。

- **返事が英語になる**：最初の返事から英語である。まず、設定が Claude に届いているかを疑う（見えていない）。
- **途中から英語に切り替わって戻らない**：始めは日本語で、作業が進むと英語になり、直すように頼んでも次の返事で英語に戻る。英語の資料や出力が積み上がっていないかを疑う（散らかっている）。モデルや面との相性も疑う（合っていない）。
- **ツールの結果を読んだ後の一言だけ英語になる**：ファイルやコマンドの出力、サブエージェントの報告を読んだ直後に、短い一言だけ英語になる。ほとんどの返事は日本語のままである。読んだ英語の直後かを確かめ、縛っていない原因まで進む。

起きやすさは、公開された報告で見当を付けられる。GitHub の anthropics/claude-code には、日本語などで頼んでも英語に戻る issue が複数ある（2026-11-03 の確認。根拠：中）。日本語の利用者の報告も、新しいモデルの公開後の報告も含まれる。報告は多く、言語も複数にわたる。一方、公式の認知と、統制した測定はない。

issue に書かれた件数や割合は、利用者が自分の記録を数えた自己申告である。同じ設定でもモデルによって英語の返答が増えたと、複数の報告がある（2026-11-03 の確認、根拠：弱）。この辞典は、自分の環境で起きる頻度を自分で記録して判断することを勧める。

## 原因を安く確かめる順 {#diagnosis}

英語になった返事を 1 つ選び、その直前に何があったかを控える。最初の返事か、出力を読んだ後か、サブエージェントが終わった後か、圧縮の後かを見る。使っている面とモデルも控える。上から順に確かめる。上の原因ほど、確かめる手間が小さい。

各項目で原因を直したら、新しい会話で同じ依頼を出し、日本語で返るかを見る。直らなければ、次の項目に進む。

指示で足りるか、仕組みで止めるかの判断には、プロンプトや CLAUDE.md のような指示は Claude が読んで判断するお願いで、フックのような仕組みは範囲の中で毎回効く鍵だという区別を使う。区別の中身は「<!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->」にある。

1. **見えていない**：返答の言語を決める指示が、英語になった時点の Claude の手元に入っていない。設定がどの層にあるか、別の値や英語の指示で上書きされていないかを確かめる。

    === "アプリ"

        - アプリでは、返答の言語を決める指示を、アプリの指示（Claude への指示・プロジェクトの指示など）に書く。公式に確かめられた、言語だけを決める設定は、この教材では確認できていない（未確認）。
        - 書いた場所の指示が、英語になったチャットに届くかを見る。たとえば、プロジェクトの指示は、そのプロジェクトの中のチャットにだけ効く。手段の整理は「<!-- link:begin align-japanese-output#request-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示](../japanese/align-japanese-output.md#request-layer)<!-- link:end -->」にある。

    === "Claude Code"

        - **設定の層**：`language` の設定を、ユーザー・プロジェクト・手元だけ・管理のどの層に書いたかを思い出し、`/status` で読み込まれた層を確かめる。確かめ方は「<!-- link:begin settings-layers#verify -->設定ファイルの階層と優先順位 › 効いているかを確かめる（準備中）<!-- link:end -->」にある。
        - **値の綴り**：`language` の値は検証されず、綴りを誤ってもエラーにならない。公式は、値をそのまま「いつもその言語で答える」指示として Claude に渡すと書く。settings.json を開き、キー名と値の綴りを見る。
        - **JSON の誤り**：JSON の構文の誤りで設定ファイルが読まれていない可能性も見る。公式の文書に診断の手順としては書かれていない、妥当な推測である。
        - **別の層の値**：同じキーは、優先順の高い層の値が使われる。リポジトリの設定（プロジェクトや手元だけの層）に別の言語の値がないかを見る。合わさる設定と上書きされる設定の違いは「<!-- link:begin settings-layers#merge -->設定ファイルの階層と優先順位 › 合わさる設定、上書きされる設定（準備中）<!-- link:end -->」にある。
        - **出力スタイル**：選んでいるスタイルの本文に、言語の指示や英語での応答を促す書き方がないかを見る。出力スタイルも、守らせる仕組みではなくお願いである。関係は「<!-- link:begin output-style-modes#japanese -->出力スタイルで応答の仕方を切り替える › 日本語の応答との関係（準備中）<!-- link:end -->」にある。
        - **CLAUDE.md の英語の指示**：CLAUDE.md や、取り込んだファイルに、英語で答える指示や英語だけの例がないかを見る。CLAUDE.md は強制する設定ではなく、文脈として渡される。
        - **サブエージェント**：英語が、サブエージェントに任せた作業の報告から来ているなら、会話の指示や出力スタイルはサブエージェントに届かない。届かないものは「<!-- link:begin what-subagents-dont-inherit -->サブエージェントに引き継がれないもの（準備中）<!-- link:end -->」にある。

    === "API"

        - API では、送る側が組む指示（システムプロンプトなど）に、返答の言語を書く。リクエストに書いた指示が実際に送られているかを、送信の内容で見る。
        - API 固有の詳しい確かめ方は、この教材ではまだ確かめていない（未確認）。手段は「<!-- link:begin keep-replies-in-japanese#app-and-api -->[日本語で返し続けさせる › アプリと API の場合](../japanese/keep-replies-in-japanese.md#app-and-api)<!-- link:end -->」にある。

2. **散らかっている**：指示は届いているが、読み込んだ英語の量に押されている。英語になる場面が、英語のツール出力やサブエージェントの報告、圧縮の要約の直後に偏っていないかを確かめる。

    - 英語になった返事の直前に読んだものを控える。英語のファイル、英語の出力を出すコマンド、サブエージェントの報告、圧縮の後の要約のどれかが直前にあれば、この原因が濃い。
    - 自分が貼った資料や、依頼文の言語も見る。英語の資料を大量に貼った直後だけ英語になるなら、読み込んだ英語に引きずられている可能性がある。
    - #99800 には、圧縮の要約が英語で書かれるというコメントがある（根拠：弱）。圧縮の後なら、「<!-- link:begin forgot-after-compaction -->[圧縮の後に約束を忘れた](forgot-after-compaction.md)<!-- link:end -->」も見る。
    - 英語のツール出力を減らす手が効くかを確かめた資料は、いまのところない。この原因の対処は、英語に戻りやすい場面を知って、その直後を確かめることにとどまる。場面は「<!-- link:begin keep-replies-in-japanese#when -->[日本語で返し続けさせる › 英語に戻りやすい場面](../japanese/keep-replies-in-japanese.md#when)<!-- link:end -->」にある。
    - アプリと API でも、読んだ英語の直後に同じことが起きるかは、この教材では未確認である。

3. **縛っていない**：1 と 2 を直しても英語に戻るなら、指示は届いていて、埋もれてもいない。`language` の設定、CLAUDE.md、出力スタイルは、Claude が読んで判断するお願いである。読まれたうえで外れることがある。

    === "アプリ"

        - アプリには指示しかなく、返答の言語を機械で確かめて差し戻す仕組みの記述は、公式の資料に見つからない。英語になったら人が気づいて頼み直す前提で運用する。
        - 指示の層の整理は「<!-- link:begin align-japanese-output#app -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › アプリには指示しかない](../japanese/align-japanese-output.md#app)<!-- link:end -->」にある。

    === "Claude Code"

        - 同じ場面で繰り返し英語になるかを見る。#96326 には、UserPromptSubmit のフックで毎ターン指示を注入しても英語になった、という報告がある（根拠：弱）。指示を増やしても直らないなら、お願いの限界である。
        - Stop フックで最後の返事を確かめ、英語なら差し戻すと、最後の返事は減らせる。ターンの終わりとツールの前後は止められるが、ツールの合間の短い一言を、画面に出る前に止める仕組みはない。作り方は「<!-- link:begin keep-replies-in-japanese#stop-hook -->[日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)<!-- link:end -->」にある。
        - 差し戻しを続けると止まらなくなる恐れがあるので、続けて止められる回数の上限を先に知る。上限は「<!-- link:begin stop-hooks#block-cap -->Stop フックで「終わらせない」 › 続けて止められる回数の上限（準備中）<!-- link:end -->」にある。
        - 英語の一言が一度画面に出ることは、公式の仕組みでは防げない。それを許せるかを、仕組みにする前に決める。

    === "API"

        - API では、Claude Code のフックに当たる仕組みを、この教材では確かめていない（未確認）。返答を受け取った側のプログラムで言語を確かめ、英語なら頼み直す組み方が考えられるが、効くかは試していない。

4. **合っていない**：指示が届いていて縛っていても、モデルや面、実行の場所が症状に合っていない。

    - **モデル**：報告の多くは Opus 5.5 である（確認日 2026-11-03）。#96601 は、出力スタイルの言語の規則が、ツールを何度も使った後に外れやすいと報告する（英語の割合が増えたという自己申告、根拠：弱）。`/model` でモデルを替え、同じ依頼と同じ設定で比べる。傾向は版で変わるので、暗記せず記録する。比べ方は「<!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end -->」にある。
    - **クラウドのセッション**：クラウドで動かしたセッションは、手元の設定の一部を読まない。手元の `language` が効いているのに、クラウドでだけ英語になるなら、これを疑う。違いは「<!-- link:begin cloud-sessions-and-teleport#settings -->クラウドセッションと teleport › 手元の設定との違い（準備中）<!-- link:end -->」にある。
    - **面**：アプリと API は、使える手段が Claude Code と違う。面ごとの手段は「<!-- link:begin keep-replies-in-japanese#app-and-api -->[日本語で返し続けさせる › アプリと API の場合](../japanese/keep-replies-in-japanese.md#app-and-api)<!-- link:end -->」にある。

1 から 4 のどれを直しても英語に戻るときは、設定を外して同じ依頼を比べ、不調が自分の設定から来るかを切り分ける。方法は「<!-- link:begin isolate-with-safe-mode#compare -->設定を外して切り分ける（--safe-mode） › 比べ方（準備中）<!-- link:end -->」にある。ほかの規則も破られるなら、「<!-- link:begin instructions-ignored -->[CLAUDE.md や指示が守られない](instructions-ignored.md)<!-- link:end -->」を見る。文体や表記だけが揃わないなら、「<!-- link:begin inconsistent-japanese-style -->[文体や表記が揃わない](inconsistent-japanese-style.md)<!-- link:end -->」を見る。

原因が分かったら、次の表の先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [日本語で返し続けさせる › 言語の設定と、効かないときに確かめること](../japanese/keep-replies-in-japanese.md#language-setting)<br>設定ファイルの階層と優先順位（準備中）<br>サブエージェントに引き継がれないもの（準備中） |
| 散らかっている | [日本語で返し続けさせる › 英語に戻りやすい場面](../japanese/keep-replies-in-japanese.md#when) |
| 縛っていない | [日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)<br>[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 確かめて差し戻す層：フックと lint](../japanese/align-japanese-output.md#lock-layer)<br>Stop フックで「終わらせない」（準備中） |
| 合っていない | モデル別の癖と、プロンプトの合わせ方（準備中）<br>[日本語で返し続けさせる › アプリと API の場合](../japanese/keep-replies-in-japanese.md#app-and-api)<br>クラウドセッションと teleport › 手元の設定との違い（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：サブエージェントの報告の後の一言だけ英語になる"
    - **状況**：Claude Code で、`language` を日本語にし、CLAUDE.md にも日本語で返すと書いた。サブエージェントが英語の報告を返した直後に、短い一言だけ英語になる。最後の返事は日本語である。
    - **迷う候補**：CLAUDE.md の指示を強い言葉に書き直す。Stop フックで最後の返事を確かめる。直後の一言は見かけたら頼み直すと割り切る。
    - **選んだもの**：設定の層と綴りを確かめ、サブエージェントに言語の指示が届いているかを見たうえで、頼み直すと割り切る。最後の返事が英語になる日が出てきたら、Stop フックを足す。
    - **理由**：診断の 1 と 2 で原因が見つかれば、直せば足りる。見つからなければ縛っていないで、指示を強くしても、お願いのままである。ツールの合間の一言は、Stop フックでも画面に出る前には止められない。困るのが最後の返事だけなら、Stop フックが効く範囲と、困る範囲が合う。

!!! example "判断例：アプリで英語になる"
    - **状況**：アプリで、日本語のチャットが長くなると、返事が英語に切り替わる。
    - **迷う候補**：アプリの指示に日本語で返すと書き足す。仕組みで止める方法を探す。新しいチャットに替える。
    - **選んだもの**：指示を書き、英語になったら新しいチャットで続ける。
    - **理由**：アプリで使える、返答の言語を機械で確かめて差し戻す仕組みは、この教材では確かめられていない。指示はお願いなので、完全には防げない。指示を足しても戻るなら、症状が出る長さの手前で替える運用が、確実に取れる手である。

## 予防：繰り返すなら仕組みに移す {#prevention}

英語に戻る症状は、指示を足すだけでは減らないことがある。次の順で備える。

- 例外を許さない場合は、Stop フックに移す。許せる場合は、お願いのまま、日本語で返す理由を CLAUDE.md や設定に 1 か所だけ書く。お願いと鍵の分け方は「<!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->」にある。
- 同じ指示を複数の層に書かない。層をまたぐと、食い違いで古い値が残り、診断の 1 が長引く。
- 仕組みにする規則は少なく保つ。保ち方は「<!-- link:begin align-japanese-output#keep-few -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 縛る規則は少なく保つ](../japanese/align-japanese-output.md#keep-few)<!-- link:end -->」にある。
- モデルや版を替えたときは、英語になる割合を記録して比べる。記録の付け方は「<!-- link:begin keep-replies-in-japanese#measure -->[日本語で返し続けさせる › 検証の方法](../japanese/keep-replies-in-japanese.md#measure)<!-- link:end -->」にある。
- コミットメッセージやコメントの言語は、返答の言語の設定とは別に決める。決め方は「<!-- link:begin commit-and-comment-language -->コミットメッセージ・コメントの言語（準備中）<!-- link:end -->」にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] Replies drift into English right after reading English tool output, despite a CLAUDE.md rule requiring Japanese; corrections do not hold（Issue #96326）](https://github.com/anthropics/claude-code/issues/96326)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Opus 5.5 ignores output-style language rule after tool chains (0.4% -&gt; 4.2% English)（Issue #96601）](https://github.com/anthropics/claude-code/issues/96601)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Opus 5.5 ignores the CLAUDE.md language rule: 33% of replies in English vs 0% on Opus 5 (same session, same CLI)（Issue #99704）](https://github.com/anthropics/claude-code/issues/99704)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Responses drift into English mid-task despite \`language: "japanese"\` and CLAUDE.md language rules（Issue #99800）](https://github.com/anthropics/claude-code/issues/99800)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[BUG\] Claude switches to English mid-session despite Japanese conversation and "language": "japanese" (Windows desktop app)（Issue #101940）](https://github.com/anthropics/claude-code/issues/101940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**次に読む**

- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- 設定ファイルの階層と優先順位（準備中）
- サブエージェントに引き継がれないもの（準備中）
- [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- Stop フックで「終わらせない」（準備中）
- モデル別の癖と、プロンプトの合わせ方（準備中）
- クラウドセッションと teleport（準備中）

**関連**

- 日本語で指示して大丈夫か（準備中）
- コミットメッセージ・コメントの言語（準備中）
- 代表的なフックのレシピ（準備中）
- 出力スタイルで応答の仕方を切り替える（準備中）
- [圧縮の後に約束を忘れた](forgot-after-compaction.md)
- [CLAUDE.md や指示が守られない](instructions-ignored.md)
- [文体や表記が揃わない](inconsistent-japanese-style.md)
- 設定を外して切り分ける（--safe-mode）（準備中）
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
