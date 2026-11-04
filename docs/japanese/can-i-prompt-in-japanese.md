---
id: can-i-prompt-in-japanese
title: 日本語で指示して大丈夫か
aliases: [日本語のプロンプト, 英語で書くべきか, 日本語と英語の精度, CLAUDE.md は英語で書くべきか]
type: concept
field: japanese
chapter: 考え方
order: 10
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
scenes: [開発, 文章]
summary: 日本語で頼んでよく、作業の指示を日本語と英語で比べたデータはない。言語を替えるより、具体性と構造を整え、コマンド・パス・識別子を原文のまま書くほうが先である。
signs:
  - {type: symptom, text: 日本語で頼むと精度が落ちる気がする}
  - {type: goal, text: 英語で書いたほうがよいのか知りたい}
  - {type: symptom, text: 日本語だとトークンや上限を早く使う気がする}
  - {type: goal, text: CLAUDE.md を日本語で書いてよいか知りたい}
prerequisites: [tokens]
related: [four-specifics, felt-vs-measured, keep-replies-in-japanese, what-uses-up-limits, saving-priorities, thinking-keywords, init-and-first-claude-md, documents-in-japanese]
tracks: [token-counting]
outdated_advice: [think-hard-keywords]
sources: [api-docs-multilingual-support, api-docs-glossary, api-docs-token-counting, shingoirie-claude-md-japanese, jinrai-claude-japanese, ssdnodes-claude-japanese, cc-changelog, cc-docs-model-config]
volatility: 中
sections:
  - {title: 日本語と英語を比べた公式の評価と、その限り, anchor: evaluation}
  - {title: 原文のまま書くもの（コマンド・パス・識別子）, anchor: keep-original}
  - {title: CLAUDE.md を日本語で書くか, anchor: claude-md}
  - {title: 日本語のトークン数と、上限への効き方, anchor: tokens}
  - {title: 「熟考」と書けば深く考えるか, anchor: thinking-words}
  - {title: 何に効くか（原理と原因）, anchor: effects}
  - {title: 誤解されやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：日本語で頼んでよい。作業の指示を日本語と英語で比べたデータはなく、言語を替えるより具体性と構造が先である。
    - **いつ引くか**：日本語で頼むと精度が落ちる気がするとき。英語で書いたほうがよいか、CLAUDE.md を日本語で書いてよいか知りたいとき。日本語だとトークンや上限を早く使う気がするとき。
    - **前提**：<!-- link:begin tokens -->[トークンとは](../basics/tokens.md)<!-- link:end -->

<!-- textlint-disable -->
別名：日本語のプロンプト・英語で書くべきか・日本語と英語の精度・CLAUDE.md は英語で書くべきか
<!-- textlint-enable -->

日本語で指示して大丈夫かという問いの答えは、「大丈夫である」。ただし、公式に確かめられているのは知識問題の成績までで、作業の指示の出来は比べられていない。言語を替えて迷うより、対象と状況を Claude に見せる書き方を整えるほうが、結果を変える。

## 日本語と英語を比べた公式の評価と、その限り {#evaluation}

日本語と英語を比べた公式の評価は、知識問題の成績に限られる。Anthropic の文書 [Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support) は、Global-MMLU（選択式の知識問題 MMLU を多くの言語に広げたもの）の成績を、同じモデルの英語の成績を 100% とした割合で載せている。日本語の割合は、表にある現行のどのモデルでも英語に近い（根拠：中。ベンダー自身の評価である）。小さいモデルほど、差がやや開く。

この評価からは、次のことまでしか言えない。

- 公式の注記は、表を同じモデルの中で言語を比べるために使い、モデルの順位付けには使わないよう求めている。ごく小さい差は測定の揺れの内とも書いている。
- 条件は、最大の effort で考えさせた知識問題である。指示の守り方や、ファイルを読んで直すような作業は比べていない。
- 調べた範囲では、作業の指示を日本語と英語で書き分けて比べたデータは見つからなかった。現行のモデルの作業に当てはめるのは類推である。

割れる論点なので、三段で整理する。

- **公式の立場**：返答の言語は会話から推測される。本番の用途では、言語を明示するほうが確実だと勧める。日本語は日本語の文字で書き、ローマ字にしない。
- **実践者の幅**：日本語で書いても精度が落ちる実感はなく、英語にするのは技術用語・コマンド・パスだけでよいという記事がある。一方で、プログラミングの質問は英語のほうが精度の高い場合があるとする記事もある。どちらも経験談で、測定ではない（根拠：弱）。
- **この辞典の推奨**：日本語で頼む。精度が落ちたと感じたら、言語を替える前に、依頼に対象・状況・完了の形が書けているかを見る。それでも英語が良いかを知りたいなら、自分の作業の依頼を 2 通りで書き、同じ物差しで何回か比べる。やり方は <!-- link:begin felt-vs-measured#evidence -->[体感と実測 › 何が起きるか（研究と根拠の強さ）](../eval/felt-vs-measured.md#evidence)<!-- link:end --> にある。

## 原文のまま書くもの（コマンド・パス・識別子） {#keep-original}

日本語で頼むときも、コマンド・パス・識別子・エラーメッセージは、訳さず原文のまま書く。識別子とは、関数名・変数名・設定のキー・機能名のことである。

訳した名前では、Claude はどのファイルのどの関数を指すのかを、推測で埋めるしかない。原文のまま書けば、名前そのものを手がかりに、該当の箇所へ行ける。これは、依頼に「対象」を書くことと同じ働きをする（4 点の全体は <!-- link:begin four-specifics#target -->[具体性の 4 点（対象・状況・完了・手本） › 対象：どのファイル・どの画面か](../prompting/four-specifics.md#target)<!-- link:end --> を参照）。

同じ依頼で並べる。

Before（識別子を訳して書いた依頼）：

> 認証まわりのトークンを更新する関数が、期限の直前に呼ぶと失敗する。直してほしい。

After：

<!-- gen:begin snippet can-i-prompt-in-japanese/request-with-identifiers -->
<!-- textlint-disable -->

???+ example "雛形：識別子を原文のまま書いた依頼"

    ```markdown
    `src/auth/session.ts` の `refreshToken()` が、期限切れの直前に呼ぶと `401 Unauthorized` を返す。直してほしい。

    - 症状：`npm test -- session.test.ts` の「refresh before expiry」が落ちる。エラーは次のとおり。
      `Error: Request failed with status code 401 (at refreshToken, src/auth/session.ts:58)`
    - 完了：そのテストが通り、`npm run lint` にも指摘が出ない。
    - 手本：`src/auth/login.ts` の `retryWithBackoff()` の書き方に合わせる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet can-i-prompt-in-japanese/request-with-identifiers -->

After で足したのは、対象のファイルと関数の原文、失敗するテストのコマンドとエラーの原文（状況）、通るべきテスト（完了）、倣う既存の関数（手本）である。書き方の全体は <!-- link:begin four-specifics#before-after -->[具体性の 4 点（対象・状況・完了・手本） › 同じ依頼を 4 点で書き直す](../prompting/four-specifics.md#before-after)<!-- link:end --> にある。

!!! example "判断例：エラーメッセージを貼るとき"
    - **状況**：英語のエラーメッセージが出た。依頼は日本語で書いている。
    - **迷う候補**：日本語に訳して貼る。原文のまま貼り、前後の説明を日本語で書く。
    - **選んだもの**：原文のまま貼り、前後の説明を日本語で書く。
    - **理由**：エラーの文字列は、ログやソースの中の文字列と照らして探せる。訳すと、照らせる手がかりが消え、Claude に見えなくなる。

## CLAUDE.md を日本語で書くか {#claude-md}

CLAUDE.md は、日本語で書いてよい。日本語で書くと精度が落ちるという実感はないとする実践者の記事がある（根拠：弱）。言語を選ぶ基準は、精度より、そのファイルを読み直して保守する人である。チームの作業の言語で書くほうが、規則の抜けや古くなった行に気づきやすい。

書き方は、言語より構造のほうが効くとされる。見出しで分け、1 行に 1 つの規則を書く。これも実践者の経験則で、測定ではない（根拠：弱）。コマンド・パス・識別子は、ここでも原文のまま書く。

<!-- gen:begin snippet can-i-prompt-in-japanese/claude-md-japanese -->
<!-- textlint-disable -->

??? example "雛形：日本語で書く CLAUDE.md（識別子は原文のまま）"

    ```markdown
    # 作業の決まり

    ## 言語

    - 説明は日本語で書く。
    - コマンド・パス・関数名・設定のキー・エラーメッセージは、訳さずに原文のまま書く。

    ## 検証

    - 変更したら、`npm test` と `npm run lint` を流してから報告する。
    - `src/legacy/` は触らない。移行の途中で、別の担当が編集している。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet can-i-prompt-in-japanese/claude-md-japanese -->

2 つの点に注意する。

- 日本語で書いても、CLAUDE.md の指示は守られる保証のないお願いである。例外を許さない規則は、フックなど、鍵のかかる仕組みで止める。
- CLAUDE.md に日本語で返すよう書いても、英語のツール出力を読んだ後に返答が英語へ戻ることがある。その対処は <!-- link:begin keep-replies-in-japanese#instructions -->[日本語で返し続けさせる › CLAUDE.md と出力スタイル（お願いの層）](keep-replies-in-japanese.md#instructions)<!-- link:end --> にある。

最初の CLAUDE.md を作る手順と、削り方は <!-- link:begin init-and-first-claude-md#run-init -->/init と最初の CLAUDE.md › /init で叩き台を作る（準備中）<!-- link:end --> にある。

## 日本語のトークン数と、上限への効き方 {#tokens}

日本語は英語より多くのトークンになりやすいが、倍率は公式に出されていない。公式の用語集は、1 トークンが表す文字数はモデルと言語で変わるとするだけで、言語ごとの数値は出していない。tokenizer が変わったモデルでは、それ以前のモデルに比べ、同じ文章でトークンが<!-- fact:begin tokenizer-token-increase-opus-4-7 -->約 30%（2026-11-05 時点）<!-- fact:end -->多くなる。

第三者の測定には、日本語が英語より多いとするものがある。ただし、旧い tokenizer の移植版で数えたもので、現行のモデルの値ではない（根拠：弱）。倍率の数字は書かない。自分の文章を、使うモデルで数える。数え方は <!-- link:begin tokens#count -->[トークンとは › 手元で数えて確かめる](../basics/tokens.md#count)<!-- link:end --> にある。token counting は、送る前に入力のトークン数を数える API の機能である。

上限への効き方は、言語だけでは決まらない。使用量は会話全体の大きさに比例し、Claude Code は毎回の依頼で会話全体を送り直す。日本語の依頼文は、その一部でしかない。ツールの出力・読み込んだファイル・長く続いた履歴も数えられる。自分の場合に何が使っているかは、<!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> で確かめる。

トークンを減らすために、依頼を英語に訳してから送るのは勧めない。訳す手間がかかり、識別子や状況のニュアンスが落ちる。節約は、手戻りを減らすことが先になる（<!-- link:begin saving-priorities#order -->[節約の優先順位（手戻りを減らすのが先） › 優先順位](../cost/saving-priorities.md#order)<!-- link:end --> を参照）。

## 「熟考」と書けば深く考えるか {#thinking-words}

「熟考」「よく考えて」と書いても、Claude Code は深く考えない。以前は、英語以外の言語でも思考を起動できる変更が CHANGELOG に記録され、日本語の語の効く時期があった。いまは、これらの語は effort を上げず、ふつうの文として渡る。

深く考えさせたいときは、effort を上げるか、そのターンだけ ultrathink と書く。ultrathink は英語の語のまま書く。それぞれの違いは <!-- link:begin thinking-keywords#plain-text-phrases -->[「考えて」と書くことの現在（ultrathink） › 普通の文として渡る言い回し](../models/thinking-keywords.md#plain-text-phrases)<!-- link:end --> と <!-- link:begin thinking-keywords#ultrathink -->[「考えて」と書くことの現在（ultrathink） › ultrathink の使いどころ](../models/thinking-keywords.md#ultrathink)<!-- link:end --> にある。この動きは Claude Code の話で、アプリでの扱いは未確認である。

古くなった助言としての扱いは、台帳の行にある（<!-- link:begin outdated-advice-ledger#think-hard-keywords -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#think-hard-keywords)<!-- link:end -->）。CLAUDE.md やスキルに「熟考」「よく考えて」を書き込んでいないか、探して確かめる。

## 何に効くか（原理と原因） {#effects}

日本語で頼んでよいという考え方は、原理「見せる」と、防ぐ原因「見えていない」に関わる。Claude は、依頼の文面と読み込んだ内容に見えているものだけで答える。頼む側が、対象と状況を見える形で渡す必要がある。

言語は、見せる内容を変えない。日本語で書いても、ファイルや関数の名前が書かれていなければ、対象は見えていない。逆に、パスや識別子や失敗の文字列を原文のまま出せば、日本語で頼んでも対象は見える。精度が落ちたと感じたときに先に見るのは、言語ではなく、何が書かれていないかである（見つけ方は <!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](../prompting/four-specifics.md#which-to-add)<!-- link:end -->）。

この考え方に隣り合う問いの行き先を挙げる。

- 日本語で頼んでも返答が英語に戻る：<!-- link:begin keep-replies-in-japanese -->[日本語で返し続けさせる](keep-replies-in-japanese.md)<!-- link:end -->
- 日本語の PDF や社内文書を読ませる、敬語や社内用語を使わせる：<!-- link:begin documents-in-japanese -->日本語の資料を読ませる・書かせる（準備中）<!-- link:end -->
- 精度が落ちたという体感が正しいかを確かめる：<!-- link:begin felt-vs-measured -->[体感と実測](../eval/felt-vs-measured.md)<!-- link:end -->

## 誤解されやすいこと {#misconceptions}

- **英語で書けば精度が上がる**：公式の評価では、日本語の知識問題の成績は英語に近い。作業の指示を比べたデータはないので、「上がる」とも「変わらない」とも断定できない。体感は、同じ物差しで測って確かめる。
- **CLAUDE.md は英語でないと守られない**：言語が原因だとする根拠は見つからなかった。守られないときは、規則が長すぎないか、例外のない規則をお願いのまま置いていないかを先に疑う。
- **日本語だと上限を倍の速さで使う**：言語ごとの倍率は公式に出されていない。使用量を決めるのは、会話全体の大きさである。
- **「熟考」と書けば深く考える**：いまは、effort を上げる働きがない。深さは effort か ultrathink で決める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)：Anthropic・英語・確認日 2026-11-04
- [Glossary](https://platform.claude.com/docs/en/about-claude/glossary)：Anthropic・英語・確認日 2026-11-05
- [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)：Anthropic・英語・確認日 2026-11-04
- [Claude Codeを日本語で使いこなすCLAUDE.mdの書き方](https://devtools.shingoirie.com/blog/claude-code-japanese-claude-md-guide/)：入江慎吾（AI Dev Tools Blog）・確認日 2026-11-04
- [Claude日本語精度｜ChatGPT・Gemini比較と自然な出力のコツ](https://jinrai.co.jp/blog/2026/03/26/claude-japanese/)：仁頼・確認日 2026-11-04
- [Claudeを日本語で使う方法：表示言語と返答の設定、使用量の違い](https://www.ssdnodes.com/learn/lang/ja/claude-in-japanese-app-language-and-limits)：SSD Nodes・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [トークンとは](../basics/tokens.md)

**関連**

- [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [日本語で返し続けさせる](keep-replies-in-japanese.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- [「考えて」と書くことの現在（ultrathink）](../models/thinking-keywords.md)
- /init と最初の CLAUDE.md（準備中）
- 日本語の資料を読ませる・書かせる（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
