---
id: prompt-patterns
title: 用途別プロンプトの型
aliases: [プロンプトのテンプレート, 調査・要約・レビュー・計画の雛形, prompt generator の代わり]
type: recipe
field: prompting
chapter: 型と例文
order: 220
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [開発, 調べもの, 文章, データ分析]
summary: 調査・要約・レビュー・計画・バグ報告などの依頼で毎回書く項目を型にして使い回す。繰り返し使う型はスキルにして呼べるようにし、変えたら効いたかを測る。
signs:
  - {type: goal, text: レビューや要約を頼むときの決まった書き方がほしい}
  - {type: symptom, text: 同じ種類の依頼を毎回ゼロから書いている}
prerequisites: [four-specifics]
related: [before-after-prompts, instructing-reviewers, research-and-reports, data-analysis, writing-skills, measure-changes, repeating-the-same-explanation, xml-tags]
outdated_advice: [console-prompt-generator, interactive-tutorial]
sources: [api-release-notes, api-docs-prompt-engineering-overview, api-docs-prompting-best-practices, gh-prompt-eng-tutorial]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 型を作って使い回す手順, anchor: procedure}
  - {title: 調査と要約の型, anchor: research}
  - {title: レビューの型, anchor: review}
  - {title: 計画とバグ報告の型, anchor: plan-and-bug}
  - {title: 観察と提案を分ける分析の型, anchor: analysis}
  - {title: 下書き・基準でのレビュー・改善をつなぐ, anchor: chaining}
  - {title: 型の効きを確かめる, anchor: check}
  - {title: 型を使ってもうまくいかないとき, anchor: when-it-fails}
  - {title: 公式の道具と教材の今, anchor: official-tools}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：調査・要約・レビュー・計画・バグ報告などの依頼で、毎回書く項目を型にして使い回せる。
    - **いつ引くか**：レビューや要約を頼むときの決まった書き方がほしいとき。同じ種類の依頼を毎回ゼロから書いているとき。
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：プロンプトのテンプレート・調査・要約・レビュー・計画の雛形・prompt generator の代わり
<!-- textlint-enable -->

用途別プロンプトの型は、依頼の種類ごとに「毎回書く項目」を欄として決めておく雛形である。欄を埋めて出せば、依頼のたびに考える量が減り、書き忘れが減る。

型は呪文ではない。効くのは、対象・状況・完了の形・手本という具体的な中身が欄に入っているときだけである。欄が空のまま出すと、型は飾りになる。

## 先に整える守り {#guards}

型を作る前に、依頼の中身を具体的にする。型は書き方の枠であり、中身を足してはくれない。

- 4 点（対象・状況・完了・手本）が書けない依頼は、型にしても同じところでずれる。先に <!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](four-specifics.md#which-to-add)<!-- link:end --> で、ずれ方から足す点を探す。
- 「完了」と「確かめる手段」の欄は、どの型にも残す。確かめる手段がなければ、返答が終わりと言っても、合っているかは自分で見るしかない。書き換えの守りは <!-- link:begin before-after-prompts#guards -->[Before/After プロンプト集 › 先に整える守り](before-after-prompts.md#guards)<!-- link:end --> にある。
- 触ってよい範囲と、やらないことの欄を置く。範囲の欄がない型を使い回すと、頼んでいない所まで手が入る余地も、毎回そのまま残る。
- レビューを頼む型では、基準と確かめ方を欄にする。詳しい頼み方は <!-- link:begin instructing-reviewers -->[レビュアーへの指示の書き方](../verify/instructing-reviewers.md)<!-- link:end --> が持つ。

## 型を作って使い回す手順 {#procedure}

型を作る時機は、同じ種類の依頼が 2 度目に出たときである。初回から作ると、使わない欄が増える。

1. 直近の依頼を 2、3 件並べ、毎回書いた項目に印を付ける。確かめ方：項目が欄の名前として言い切れる。
2. 欄を決める。毎回変わる中身は `<…>` の欄にし、毎回同じ文は固定の文にする。確かめ方：欄の名前だけを見て、何を書くか分かる。
3. 理由が要る欄には、理由を添える枠を置く。制約や好みは、理由があると応用が利く。確かめ方：「なぜ」を書く場所がある。
4. 欄を埋めて出し、返答が「出してほしい形」の欄どおりかを見る。確かめ方：形が外れたら、外れた欄を直す。
5. 何度も使うと分かったら、型をスキルにする（作り方は <!-- link:begin writing-skills -->[スキルの作り方](../extend/writing-skills.md)<!-- link:end --> が持つ）。確かめ方：呼び出して、貼ったときと同じ形の返答が出る。

型をどこに置くかは、面によって違う。

=== "アプリ"

    型は、プロジェクトの指示に置くか、手元のメモから貼る。その場の依頼では、欄の `<…>` を埋めて貼る。毎回貼る型は、置き場所に移すと貼る手間が消える。置き場所の選び方は <!-- link:begin repeating-the-same-explanation#causes -->[毎回同じ説明をしている › 原因ごとの対処](../symptoms/repeating-the-same-explanation.md#causes)<!-- link:end --> にある。

=== "Claude Code"

    型は、スキルや CLAUDE.md に置く。依頼の型はスキルにして呼び出し、守らせたい決まりは CLAUDE.md に書く。スキルの作り方は <!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](../extend/writing-skills.md#minimal)<!-- link:end --> にある。

=== "API"

    型は、自分のコードの中でプロンプトの雛形にする。欄の中身はコードが埋め、指示・資料・例の区切りにはタグを使う。区切り方は <!-- link:begin xml-tags#separate -->[XML タグで区切る › 指示・資料・例を分ける](xml-tags.md#separate)<!-- link:end --> にある。

!!! example "判断例：型を毎回貼るか、スキルにするか"
    - **状況**：週に数回、PR のレビューを同じ基準で頼んでいる。今は手元のメモから型を貼っている。
    - **迷う候補**：このまま貼り続ける。スキルにして呼び出す。
    - **選んだもの**：スキルにする。ただし、基準が毎回変わるなら貼るままにする。
    - **理由**：中身がほぼ変わらず、使う人が増えるなら、スキルのほうが貼り間違いは減る。基準を毎回変えるなら、固定部分が少なく、スキルの利点は小さい。判断の目安は <!-- link:begin writing-skills#when-to-use -->[スキルの作り方 › どんなときにスキルにするか](../extend/writing-skills.md#when-to-use)<!-- link:end --> にある。

## 調査と要約の型 {#research}

調査と要約の依頼は、問い・範囲・出典・書き分けの 4 つを欄にする。問いと範囲が決まっていないと、調べものは広がり、結論に出典が付かなくなる。

型の骨は次のとおりである。

- 問いを 1 文で。何を決めるために知りたいかを添える。
- 範囲と、使ってよい資料。使わない資料も書く。
- 出してほしい形。結論を先に、根拠ごとに出典と原文の短い引用を付ける。
- 書かれていることと、推測を分ける。分からないときは「分からない」と書いてよいと伝える。

<!-- gen:begin snippet prompt-patterns/research-request -->
<!-- textlint-disable -->

??? example "雛形：調べものの依頼の型"

    ```markdown
    【調べたいこと】<問いを 1 文で。「〜を決めるために、〜を知りたい」の形>
    【範囲】<対象の期間・製品・地域・版。ここまでは調べる、ここから先は調べない>
    【使ってよい資料】<公式の文書・指定した URL・手元の資料。Web を探してよいか>
    【使わない資料】<除きたいサイトや種類。なければ「なし」>

    【出してほしい形】
    - 結論を先に 3 行まで
    - 根拠ごとに、出典の URL と、該当する原文の短い引用
    - 書かれていることと、そこからの推測を分けて書く
    - 見つからなかったこと、資料同士が食い違ったことを、別の項目に書く

    【分からないとき】推測で埋めず、「分からない」と書いてよい。
    【完了】<何が書かれていれば、この調べものは終わりか>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/research-request -->

要約を頼むときは、「出してほしい形」の欄を、要約の読み手と長さに差し替える。誰が何のために読むかが分かると、何を落としてよいかが決まる。調べものの進め方と、出典を原文で確かめる手順は <!-- link:begin research-and-reports#steps -->[調べものとレポート › 調べものの進め方](../recipes/research-and-reports.md#steps)<!-- link:end --> が持つ。

## レビューの型 {#review}

レビューの依頼は、対象・目的・基準・出す形の 4 つを欄にする。基準がないと、好みの指摘が混ざり、重要な指摘が埋もれる。

型の要点は、指摘ごとに「場所・問題・重さ・確かめ方」を出させることである。確かめ方が付けば、指摘が本当かを自分で見直せる。

<!-- gen:begin snippet prompt-patterns/review-request -->
<!-- textlint-disable -->

??? example "雛形：レビューの依頼の型"

    ```markdown
    【レビューする対象】<ファイルのパス・差分の範囲・文章の名前>
    【目的】<この変更や文章が、何を満たすためのものか>
    【基準】
    - <基準 1。例：既存の呼び出し元を壊さない>
    - <基準 2。例：境界の入力（空・最大・重複）で動く>
    - <基準 3。例：読む人が前提なしで通じる>

    【やること】基準ごとに、満たしていない箇所を見つけて出す。直すところまではしない。
    【出してほしい形】指摘ごとに、場所・何が問題か・重さ（直す／直したほうがよい／軽い）・確かめ方（流すコマンドや照合する箇所）を書く。
    【やらないこと】<対象外の範囲。好みの指摘は軽いものとして最後にまとめる>
    【見つからないとき】指摘がなければ、確かめた基準と確かめ方を書いて、指摘なしと答える。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/review-request -->

この型は、基準を自分で決めて渡す前提で書いてある。自分の見立てを先に書き添えると、レビューがその見立てに引かれる。網羅と選別を分ける頼み方、見立てを伏せる理由、指摘ごとの確かめ方は <!-- link:begin instructing-reviewers#example -->[レビュアーへの指示の書き方 › 頼み方の例](../verify/instructing-reviewers.md#example)<!-- link:end --> にある。

## 計画とバグ報告の型 {#plan-and-bug}

計画とバグ報告は、どちらも「まだ直さない」段を先に置く型にする。実装の前に計画か原因の見立てを出させれば、方針の違いを手前で見つけられる。

計画の型は、段ごとの確かめ方と、選択肢の推奨案、先に答えてほしい質問を欄にする。

<!-- gen:begin snippet prompt-patterns/plan-request -->
<!-- textlint-disable -->

??? example "雛形：計画の依頼の型"

    ```markdown
    【やりたいこと】<目的を 1 文で。何のために、誰が使うのか>
    【今の状態】<関係するファイル・画面・現状の挙動。倣う既存の実装があればその場所>
    【制約】<変えてはいけないもの、使えない道具、期限。理由が分かるものは理由も 1 文で>

    【やること】実装はまだしない。次の形で計画だけを出す。
    - 作業を、順に確かめられる段に分ける（各段に、終わったと言える確かめ方を付ける）
    - 選択肢が分かれる所は、候補と推奨案と、その理由を出す
    - 分からないことは、推測で進めず、先に質問として並べる

    【完了】<計画に何が書かれていれば、実装に進んでよいか>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/plan-request -->

バグ報告の型は、症状・期待・再現の手順・環境・試したことを欄にする。再現の手順は具体的な値で書く。再現できない報告は、Claude でも人でも推測で直すしかない。

<!-- gen:begin snippet prompt-patterns/bug-report -->
<!-- textlint-disable -->

??? example "雛形：バグ報告の依頼の型"

    ```markdown
    【症状】<何が起きるか。画面の表示・エラーの全文・出力のずれ>
    【期待】<本来どうなるはずか>
    【再現の手順】
    1. <操作や入力。具体的な値で>
    2. <次の操作>
    【環境】<OS・版・ブランチ・関係する設定。分かる範囲で>
    【試したこと】<試して変わらなかったこと、切り分けで分かったこと>
    【関係しそうな場所】<ファイルのパス・関数名。分からなければ「不明」>

    【やること】まず原因を調べて、見立てと根拠を出す。直すのはその後。
    【完了】<再現の手順を流すと、期待どおりになる。失敗するテストを先に書いてから直す、でもよい>
    【確かめる手段】<流すコマンド。結果はそのまま貼ってもらう>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/bug-report -->

症状と再現を書く欄の考え方は <!-- link:begin four-specifics#situation -->[具体性の 4 点（対象・状況・完了・手本） › 状況：症状と再現の手順](four-specifics.md#situation)<!-- link:end --> に、完了の欄の考え方は <!-- link:begin four-specifics#done -->[具体性の 4 点（対象・状況・完了・手本） › 完了：何が起きれば終わりか](four-specifics.md#done)<!-- link:end --> にある。

!!! example "判断例：計画の型を使うか、直接頼むか"
    - **状況**：1 つの関数の戻り値の型を直すだけの小さな変更を頼みたい。
    - **迷う候補**：計画の型で先に計画を出させる。直接「直して」と頼む。
    - **選んだもの**：直接頼む。ただし、完了の形（流すテスト）は書く。
    - **理由**：差分を 1 文で言えるほど小さいなら、計画を出させる手間のほうが大きい。複数のファイルや、選択肢が分かれる変更なら、計画の型で先に方針を見る。

## 観察と提案を分ける分析の型 {#analysis}

分析の依頼では、観察した事実と、改善の提案を別の出力にする。原因をまだ確かめていない段階で改善策を出させると、確かめていない原因に基づく提案が、事実のように並ぶ。

型は、まず集計して観察を出させ、次に原因の仮説を互いに排他的な形で挙げさせる。各仮説には、正しければ観測されること、誤りなら観測されること、最小の確認実験を付けさせる。どれが有力かの判断は、この依頼では頼まない。

<!-- gen:begin snippet prompt-patterns/analysis-request -->
<!-- textlint-disable -->

??? example "雛形：観察と提案を分ける分析の依頼"

    ```markdown
    【やりたいこと】<注目する対象（例：失点の多い入力）について、何が起きているかを知りたい>
    【材料】<ログや集計結果の場所。例：analysis/out/summary.csv と、それを作ったスクリプト analysis/aggregate.py>

    【やること】次の順に、分けて出す。
    - 観察：数字から言える事実だけを書く。値には、元データの行か集計コマンドの出力を添える
    - 追加の集計案：観察を確かめるのに取るとよい集計だけを挙げる（実行はまだしない）
    - 原因の仮説：互いに両立しない形で最大 5 つ。各仮説に、正しければ観測されること、誤りなら観測されること、最小の確認実験を書く

    【やらないこと】改善策は書かない。どの仮説が有力かの判断もしない。判断は私が決める
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/analysis-request -->

この型の雛形は、このページが持ち主である。データ分析の進め方（再実行できる形で集計させる、生データで裏を取る）は <!-- link:begin data-analysis#observation-vs-interpretation -->[データを分析する › 観察と解釈を分ける](../recipes/data-analysis.md#observation-vs-interpretation)<!-- link:end --> が持つ。仮説を「誤りならこう見える」の形で書かせるのは、確かめる実験を最初から決めておくためである。

## 下書き・基準でのレビュー・改善をつなぐ {#chaining}

下書き、基準でのレビュー、改善の 3 つを別々の依頼にして、順につなぐ型である。1 回の依頼で「書いて、見直して、直して」と頼むと、途中の下書きと指摘が見えない。どの直しがどの基準から来たかも、確かめにくい。

公式の Prompting best practices も、中間の出力を確かめたいときは、明示的に連結する方法が有効と述べている。思考やサブエージェントが多段の推論をこなす今も、これは変わらない。代表的なパターンが、この「下書き、基準でのレビュー、改善」である。

<!-- gen:begin snippet prompt-patterns/draft-review-improve -->
<!-- textlint-disable -->

??? example "雛形：下書き、基準でのレビュー、改善の連結"

    ```markdown
    ## 1 回目：下書き
    <文章や変更の依頼。目的・読む人・完了の形を、4 点の欄で書く>
    下書きだけを出してください。見直しは次の依頼で頼みます。

    ## 2 回目：基準でのレビュー（できれば別のセッションに下書きを貼って頼む）
    次の下書きを、基準ごとに確かめてください。直さず、指摘だけを出してください。
    基準：
    - <基準 1。例：読む人が前提なしで通じる>
    - <基準 2。例：数字や固有名は元の資料と合う>
    指摘ごとに、場所・問題・重さ・確かめ方を書いてください。基準を満たしていれば、指摘なしと答えてください。
    <下書きを貼る>

    ## 3 回目：改善
    2 回目の指摘のうち、<採用する指摘の番号>だけを直してください。ほかの箇所は変えず、直した所を一覧で示してください。採用しなかった指摘には触れなくてかまいません。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet prompt-patterns/draft-review-improve -->

つなぐときの注意は 3 つある。

- 基準は、2 回目の前に自分で決めて渡す。基準を Claude 任せで作らせると、下書きへ合わせた基準になりやすい。
- 2 回目は、できれば別のセッションに下書きだけを貼って頼む。下書きを書いた会話の続きでは、書いた側の判断が残る。
- 3 回目は、採用する指摘の番号を指定する。全部直させると、頼んでいない所まで変わる。

レビューの基準の書き方は <!-- link:begin instructing-reviewers#hide-your-view -->[レビュアーへの指示の書き方 › 自分の見立てを書き添えない](../verify/instructing-reviewers.md#hide-your-view)<!-- link:end --> と <!-- link:begin instructing-reviewers#per-finding -->[レビュアーへの指示の書き方 › 指摘ごとに確かめ方を付けさせる](../verify/instructing-reviewers.md#per-finding)<!-- link:end --> にある。

## 型の効きを確かめる {#check}

型を作ったら、効いたかを確かめる。型を変えた直後は良くなったように見えても、1 回の試行では運の差かもしれない。

- 返答の形：「出してほしい形」の欄どおりに返ったかを見る。外れたなら、欄の書き方を直す。
- 型の有り無し：同じ依頼を、型を使った場合と使わない場合で、新しいセッションに出して比べる。比べ方は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。
- 型を変えたとき：前後で同じ依頼を何度か走らせる。試行の数と差の見方は <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> にある。
- 型を使い続けるとき：返答を読み、欄が空のまま出されていないかを見る。

## 型を使ってもうまくいかないとき {#when-it-fails}

型を使っても期待した返答にならないときは、症状ごとに次のページへ進む。

- 欄は埋めたが、対象の取り違えや範囲外の変更が起きる：欄の中身が具体的でない。<!-- link:begin before-after-prompts#when-it-fails -->[Before/After プロンプト集 › 書き換えても直らないとき](before-after-prompts.md#when-it-fails)<!-- link:end --> を見る。
- レビューが甘い、または好みの指摘ばかり出る：基準が曖昧か、見立てを書き添えている。<!-- link:begin instructing-reviewers#limits -->[レビュアーへの指示の書き方 › 効かない場面とやりすぎ](../verify/instructing-reviewers.md#limits)<!-- link:end --> を見る。
- 型を毎回貼るのが手間になっている：置き場所を変える段階である。<!-- link:begin repeating-the-same-explanation -->[毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)<!-- link:end --> で、移す先を決める。
- 型が長くなり、使わない欄が増えた：欄を削る。使わなかった欄は、直近の依頼で空だったものから外す。
- 禁止したことをされる：型の文は依頼であり、強制ではない。例外を許さない決まりは、CLAUDE.md ではなく仕組みで縛る。

## 公式の道具と教材の今 {#official-tools}

プロンプトの下書きを作る公式の道具と、学習用の教材は、いまの状態が変わっている。型を作る出発点として、次の 2 点を押さえる。

Console の prompt generator と improver は、旧 Workbench と一緒に退役した。プロンプトの生成・改善・テンプレート化の実験的な API も退役し、呼ぶとエラーを返す。いま型を作るなら、公式の Prompting best practices を出発点にして、成功の基準を決め、変えた効果を測りながら直す。下書きを機械に作らせたいなら、公式の Prompt engineering overview は Claude Cookbook の metaprompt のノートブックを案内している。経緯と、手順書で探す方法は <!-- link:begin outdated-advice-ledger#console-prompt-generator -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#console-prompt-generator)<!-- link:end --> にある。

公式のインタラクティブチュートリアルは、基本の考え方の練習には使える。ただし、Claude 3 のモデル向けに書かれていて、食い違う所は Prompting best practices に従うよう、公式の文書も注記している。章によっては、いまのモデルでは使えない手が含まれる。どの手が使えないかは <!-- link:begin outdated-advice-ledger#interactive-tutorial -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#interactive-tutorial)<!-- link:end --> にある。

元の文書は、[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)・[Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)・[Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)である。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)：Anthropic・英語・確認日 2026-11-04
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)

**関連**

- [Before/After プロンプト集](before-after-prompts.md)
- [レビュアーへの指示の書き方](../verify/instructing-reviewers.md)
- [調べものとレポート](../recipes/research-and-reports.md)
- [データを分析する](../recipes/data-analysis.md)
- [スキルの作り方](../extend/writing-skills.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [XML タグで区切る](xml-tags.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
