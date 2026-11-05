---
id: plausible-falsehoods
title: もっともらしい嘘・出典の誤り
aliases: [ハルシネーション, 存在しない出典, 嘘の引用, 答えが毎回違う]
type: symptom
field: symptoms
chapter: 事実と出典
order: 70
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [見えていない, 確かめていない]
pitfalls: []
scenes: [調べもの, 文章, 学習]
summary: もっともらしい嘘や存在しない出典を、見せた資料と確かめ方の不足から切り分け、引用・照合・「分からない」と言わせる手を選ぶ。
signs:
  - {type: symptom, text: もっともらしいが出典が怪しい}
  - {type: symptom, text: 存在しない論文や URL を挙げられる}
  - {type: symptom, text: 同じ質問をするたびに答えが変わり、どれが正しいか分からない}
  - {type: symptom, text: 確かめると数字や引用が原文と違っている}
wave: 1
prerequisites: [why-hallucinations]
related: [nondeterminism, using-research, knowledge-cutoff, citations-basics, second-opinion-from-another-model, agreement-is-not-evidence, summary-overstates-source, uses-nonexistent-apis, doesnt-know-latest, caves-when-pushed, six-causes]
routes:
  - {cause: 見えていない, to: [allow-i-dont-know, search-research-thinking]}
  - {cause: 確かめていない, to: [fact-checking, checking-citations]}
tracks: [web-search, research, citations]
outdated_advice: [lower-temperature]
sources: [api-docs-reduce-hallucinations]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: to-fixes}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevent}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：もっともらしい嘘や存在しない出典を、見せた資料の不足と確かめ方の不足に分け、次の手を選べる。
    - **いつ引くか**：出典が怪しい、存在しない論文や URL が出る、数字や引用が原文と違う、同じ質問で答えが変わるとき。
    - **前提**：<!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ハルシネーション・存在しない出典・嘘の引用・答えが毎回違う
<!-- textlint-enable -->

もっともらしい嘘・出典の誤りは、Claude が根拠を持たないまま、それらしい事実や出典を答えに混ぜる症状である。見た目は丁寧な答えなので、読むだけでは見分けられない。原因は、根拠が Claude の目の前になかったか、出てきた答えを誰も確かめていないかの 2 つに絞れる。

## よくある形 {#forms}

この症状は、次のどれかの形で出る。どの形でも、答えの文面からは正誤を判断できない。

- 存在しない論文・書籍・URL・関数名を、題名や著者つきで挙げる。
- 実在する文献を挙げるが、題名・著者・年・引用の文言のどれかが違う。細部だけ違うので気づきにくい。
- 数字や日付が、渡した資料の原文と違う。
- 同じ質問を繰り返すたびに結論や数字が変わり、どれを採るか決められない。

なぜ作り話が出るのかは前提のページが扱う。ここでは、起きたときにどこから確かめるかだけを決める。

## 原因を安く確かめる順 {#diagnosis}

確かめる費用が低い順に並べる。上の項目で当たりが出たら、下の項目は後回しでよい。このページの症状に関わる原因は、**見えていない**と**確かめていない**の 2 つである。

1. **資料が見えていない（見えていない）**
    - 見ること：答えの根拠にしてほしい資料を、その会話に渡したか。渡していなければ、Claude は記憶だけで答えている。
    - 確かめ方：渡していなければ、先に資料を渡して質問し直す。渡していたなら、同じ会話で「この答えの各主張について、渡した資料の根拠の箇所を引用して。資料にない主張は『資料にない』と書いて」と頼む。引用が出ない主張は、資料なしで書かれた部分である。
2. **知識の締め切りや、非公開の話に当たっている（見えていない）**
    - 見ること：質問が最近の出来事、新しい版、自分の組織の内側の話を含むか。
    - 確かめ方：その話題を扱う公式の資料や検索の結果を渡し、同じ質問をし直す。答えが変われば、見えていなかったのが原因である。詳しい切り分けは <!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](doesnt-know-latest.md#diagnosis)<!-- link:end --> と <!-- link:begin knowledge-cutoff#what-happens -->[知識カットオフと「今」を知らない問題 › 何が起きるか](../basics/knowledge-cutoff.md#what-happens)<!-- link:end --> にある。
3. **分からないと言える余地がなく、答えを迫った（見えていない）**
    - 見ること：依頼に「必ず挙げて」「3 つ出して」のように、答えを出すこと自体を求める文がないか。分からないと答えてよい、という一文があるか。
    - 確かめ方：その一文を足して、同じ質問をし直す。作り話だった部分が「分からない」「推測」に変われば、迫ったことが一因だった。仕組みは <!-- link:begin allow-i-dont-know#pressure -->[「分からない」と言ってよいと伝える › 答えを迫ると作り話が増える](../prompting/allow-i-dont-know.md#pressure)<!-- link:end --> にある。
4. **出てきた出典を、原文で確かめていない（確かめていない）**
    - 見ること：挙がった論文・URL・引用を、自分の目で開いたか。実在するだけでは足りず、題名・著者・年と引用の文言まで照らしたか。
    - 確かめ方：原文を開いて照合する。手順と誤りの形は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> と <!-- link:begin checking-citations#error-types -->[引用や出典の確かめ方 › よくある誤りの形](../verify/checking-citations.md#error-types)<!-- link:end --> にある。
5. **答えが割れることを、確かめる合図にしていない（確かめていない）**
    - 見ること：同じ質問への答えが、回ごとに違っていないか。
    - 確かめ方：同じ質問を数回出して並べる。割れた主張は、根拠が弱い部分の合図として扱い、原文で確かめる。比べ方は <!-- link:begin fact-checking#best-of-n -->[事実を確かめる（引用・照合・best-of-N） › 何度か聞いて比べる（best-of-N）](../verify/fact-checking.md#best-of-n)<!-- link:end -->、割れる理由は <!-- link:begin nondeterminism#why -->[同じ質問でも答えが変わる（非決定性） › なぜ答えが変わるか](../basics/nondeterminism.md#why)<!-- link:end --> にある。

人の側の落とし穴も 1 つ疑う。確かめる手段として、別のモデルや同じモデルの別の回の「同意」を使っていないか。何体が同意しても、それは根拠にならない。同意を数えず、原文や実行の結果で確かめる。理由は <!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end --> と <!-- link:begin second-opinion-from-another-model#agreement -->別のモデルに第二の意見を求める（一致は証拠にならない）<!-- link:end --> にある。

## 原因ごとの対処 {#to-fixes}

原因が絞れたら、次の表の行き先へ進む。対処の手順の本体は、行き先のページにある。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)<br>[web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md) |
| 確かめていない | [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<br>[引用や出典の確かめ方](../verify/checking-citations.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

症状の形によっては、別のページで切り分ける。

- 要約が原文より断定的になっている：<!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](summary-overstates-source.md#diagnosis)<!-- link:end -->
- 存在しない関数やパッケージが出た：<!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](uses-nonexistent-apis.md#diagnosis)<!-- link:end -->
- 押すと答えを変える：<!-- link:begin caves-when-pushed#diagnosis -->[すぐ同意して意見を変える（迎合） › 原因を安く確かめる順](caves-when-pushed.md#diagnosis)<!-- link:end -->
- どの症状か迷う：<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end -->

## 判断例 {#examples}

!!! example "判断例：挙げられた論文が 1 本、開けない"
    - **状況**：調べものの根拠として論文を 5 本挙げさせた。1 本は URL が開けず、1 本は題名が検索結果と少し違う。
    - **迷う候補**：web 検索やリサーチを使って、同じ依頼をやり直させる。または、挙がった題名を自分で検索し、原文を開いて照らす。
    - **選んだもの**：先に、挙がった 5 本を自分で検索して原文を開く。
    - **理由**：確かめる費用がいちばん安く、実在しない文献と、実在するが細部が違う文献を区別できる。やり直した結果にも同じ確認が要るので、検索への切り替えは、原文を開いて見えていない原因だと分かってからにする。

!!! example "判断例：同じ質問で数字が毎回違う"
    - **状況**：資料を渡さずに数字を尋ねたところ、3 回の答えが 3 通りだった。
    - **迷う候補**：いちばん多く出た数字を採る。または、割れたこと自体を、根拠が見えていない合図として扱う。
    - **選んだもの**：割れたことを合図にして、数字が載っている資料を渡し、その箇所を引用させて原文で確かめる。
    - **理由**：回ごとに割れる主張は、根拠が弱い部分の合図として扱える。多く出たからといって、正しいとは限らない。揃った場合も、原文で確かめるまでは採用しない。

## 予防 {#prevent}

事実が要る依頼では、先に確かめる仕組みを依頼の形に入れておく。

- 渡した資料の範囲で答えさせ、根拠の箇所を引用させる。資料にない所は「分からない」と書かせる。頼み方は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> と <!-- link:begin allow-i-dont-know#source-only -->[「分からない」と言ってよいと伝える › 渡した資料だけを根拠にさせる](../prompting/allow-i-dont-know.md#source-only)<!-- link:end --> にある。
- 重要な事実は、引用つきの答えを受け取ったあと、原文で照合する手順まで決めておく。公式の文書も、これらの手で大きく減らせるが無くならないと述べ、重大な判断に関わる情報は検証せよと勧めている（[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)）。
- 答えのばらつきを抑える目的で temperature を下げる助言は、今は使えない。理由と今の方法は <!-- link:begin nondeterminism#temperature-advice -->[同じ質問でも答えが変わる（非決定性） › temperature を下げる助言は今は使えない](../basics/nondeterminism.md#temperature-advice)<!-- link:end --> と <!-- link:begin outdated-advice-ledger#lower-temperature -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#lower-temperature)<!-- link:end --> にある。

面ごとに、資料を見せる手段が違う。

=== "アプリ"

    web 検索とリサーチで、最近の話や公開の資料を見せられる。使い分けは <!-- link:begin search-research-thinking#choose -->[web 検索・リサーチ・拡張思考の使い分け › 選び方](../app/search-research-thinking.md#choose)<!-- link:end -->、リサーチの出典の確かめ方は <!-- link:begin using-research#checking-sources -->[リサーチを使いこなす › 出典の確かめ方](../app/using-research.md#checking-sources)<!-- link:end --> にある。検索を使えたかどうかも確かめる。

=== "Claude Code"

    手元のファイルや文書を読ませ、そのどの箇所が根拠かを引用させる。読ませる前に答えさせると、記憶で書かれる。

=== "API"

    citations という機能で、渡した資料の根拠の箇所を API に返させられる。引用させる指示との違いは <!-- link:begin citations-basics#vs-prompting -->citations（根拠の箇所を返させる）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)

**次に読む**

- [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)

**関連**

- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- [リサーチを使いこなす](../app/using-research.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [要約が原文より断定的になる](summary-overstates-source.md)
- [存在しない関数やパッケージを使う](uses-nonexistent-apis.md)
- [最新の情報を知らない](doesnt-know-latest.md)
- [すぐ同意して意見を変える（迎合）](caves-when-pushed.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
