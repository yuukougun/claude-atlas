---
id: doesnt-know-latest
title: 最新の情報を知らない
aliases: [知識カットオフ, 古い情報で答える, 新しい版を知らない]
type: symptom
field: symptoms
chapter: 事実と出典
order: 90
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [調べもの, 開発]
summary: 最近の出来事や新しい版について間違える原因を知識の締め切りから切り分け、検索・公式の資料・日付の確かめ方のどれを使うかを決める。
signs:
  - {type: symptom, text: 最近の出来事や新しい版について間違える}
  - {type: symptom, text: Claude Code の新しい機能について聞くと古い答えが返る}
  - {type: symptom, text: 古い書き方のコードや設定を出してくる}
wave: 1
prerequisites: [knowledge-cutoff]
related: [using-research, connectors-in-the-app, old-advice-doesnt-work, dating-information, plausible-falsehoods, uses-nonexistent-apis, six-causes]
routes:
  - {cause: 見えていない, to: [search-research-thinking, choose-what-to-read, ask-claude-code]}
tracks: [web-search, research]
outdated_advice: []
sources: [hc-up-date-training-data, api-docs-models-overview, hc-web-search, hc-research, includesecurity-ctfs-ai-era]
volatility: 中
sections:
  - {title: よくある形, anchor: shapes}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処へ, anchor: to-fixes}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：間違いの原因が Claude の知識の締め切りにあるかを切り分け、今日の日付・検索・公式の資料のどれを渡すかを決められる。
    - **いつ引くか**：最近の出来事や新しい版について間違える。Claude Code の新しい機能を聞くと古い答えが返る。古い書き方のコードや設定が出てくる。
    - **前提**：<!-- link:begin knowledge-cutoff -->[知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)<!-- link:end -->

<!-- textlint-disable -->
別名：知識カットオフ・古い情報で答える・新しい版を知らない
<!-- textlint-enable -->

最新の情報を知らない症状は、Claude の知識が学習の締め切りで止まっていて、今日の日付も会話に入っていないときに起きる。間違いの多くは、Claude に最新の情報が見えていないだけで、頼み方の問題ではない。このページは、原因を安い確かめから順に切り分け、振り分け先を決める。

## よくある形 {#shapes}

「最新の情報を知らない」は、次の 3 つの形で現れる。どれも、Claude は古い内容を自信のある口調で答える。

- 最近の出来事や発表について、尋ねても古い状況のまま答える。あるいは、起きていないと答える。
- Claude Code の新しい機能や設定を聞くと、存在しない、または前の仕様の答えが返る。
- ライブラリや設定の書き方が一世代前のものになる。動くが、今は非推奨の書き方であることがある。

3 つ目は、動く書き方が出るので気づきにくい。古い書き方が出たときも、同じ手順で切り分ける。

## 原因を安く確かめる順 {#diagnosis}

最新の情報を知らないときの原因は、Claude に最新の情報が見えていないこと（6 つの原因のうち「見えていない」）である。確かめは、手間の小さい順に並べる。上から順に見て、当てはまった所で手を打つ。6 つの原因の全体と、ほかの症状への入口は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

1. **質問が締め切りより後の事柄か**（何を見る：質問の対象が出た時期）
    - 知識の締め切りには、確かな知識の日付と、学習データの日付の 2 種類がある。モデルによって一致しないことがある。現行のモデルの学習データの日付は、<!-- fact:begin model-knowledge-cutoffs 現行のモデル training -->2026年6月（2026-11-04 時点）<!-- fact:end -->。モデルごとの日付は、公式の文書で確かめる（[Models overview](https://platform.claude.com/docs/en/models/overview)、[How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)）。
    - 確かめ方：対象が出た時期を、使っているモデルの締め切りと比べる。Claude 自身に締め切りを尋ねても答えは出るが、自己申告なので目安にとどめる。
    - 当てはまったら：Claude が知りえない事柄である。2 番以降で、日付と資料を渡す。仕組みは <!-- link:begin knowledge-cutoff#why -->[知識カットオフと「今」を知らない問題 › なぜ知らないのか](../basics/knowledge-cutoff.md#why)<!-- link:end --> にある。
2. **今日の日付と使っている版を渡したか**（何を見る：会話に日付と版があるか）
    - Claude は今日の日付を知らない。「最新」「現行」の基準がずれるので、締め切り時点の最新を答える。
    - 確かめ方：新しい会話で今日の日付を尋ねる。ずれていれば、日付を渡していない。使っている版（ライブラリ・Claude Code の版など）も、書かないと伝わらない。
    - 当てはまったら：依頼に日付と版を書く。予防の節に、日付・版・資料を渡す依頼の雛形がある。
3. **検索や URL の取得が使われたか**（何を見る：返答に検索の跡と出典があるか）
    - 確かめ方：返答に出典の URL や、検索した旨が出ているかを見る。面によって、使える手段が違う。

    === "アプリ"

        Web 検索は、有効にしておく要がある（Team と Enterprise は owner が組織で有効にする）。有効なときも、要るときに Claude が検索するので、検索が走ったかは返答で確かめる。広く調べるときは、リサーチを使う。違いと選び方は <!-- link:begin search-research-thinking#choose -->[web 検索・リサーチ・拡張思考の使い分け › 選び方](../app/search-research-thinking.md#choose)<!-- link:end --> にある。

    === "Claude Code"

        検索や URL の取得ができるかは、自分の環境の許可の設定で変わる（WSL・Linux の CLI の基準。ほかの OS と IDE 拡張の動作は未確認）。使われたかは、実行中の道具の表示で見る。

    === "API"

        検索は、リクエストに検索の道具を載せたときだけ使われる。載せていなければ、モデルは学習した知識だけで答える。道具の詳細は API の分野のページに任せる。

    - 当てはまったら：検索を有効にするか、公式の文書の URL を渡して読ませる。
4. **最新の資料を渡したか**（何を見る：根拠にさせる文書が会話にあるか）
    - 検索が使えないとき、または検索が正しいページに届かないときは、公式の文書の URL か抜粋を渡すのが確実である。
    - 確かめ方：資料を付けて同じ質問を出し、答えが資料に沿うかを見る。Claude Code の機能については、Claude Code 自身に聞く手がある。ただし、答えは手元の版より新しい機能を含みうる。版は <!-- link:begin ask-claude-code#check-version -->Claude Code 自身に聞く › 答えの版を確かめる（準備中）<!-- link:end --> で確かめる。
    - 当てはまったら：資料を渡す。読ませる範囲の絞り方は <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> にある。
5. **検索で拾った情報自体が古くないか**（何を見る：出典の日付と版）
    - 検索に成功しても、古い記事を拾うと古い答えが返る。
    - 確かめ方：出典の日付と、対象の版を見る。日付と版の確かめ方は <!-- link:begin dating-information#check-date-and-version -->いつの情報かを見分ける › 日付と版の確かめ方（準備中）<!-- link:end -->、リサーチの出典の確かめ方は <!-- link:begin using-research#checking-sources -->リサーチを使いこなす › 出典の確かめ方（準備中）<!-- link:end --> にある。
    - 当てはまったら：新しい資料を指定して、もう一度調べさせる。
6. **締め切りより前でも、資料の薄い領域か**（何を見る：公開の文書が少ない話題か）
    - 公開の資料が少ない領域や、文書と実際のソースが食い違う領域では、締め切りより前の事柄でも間違えやすい。セキュリティ競技（CTF）の難問が最後まで残った観察から一般化した見方である（根拠：弱・類推）。
    - 確かめ方：同じ問いに資料を付けると答えが変わるかを見る。変わるなら、知識の不足である。
    - 当てはまったら：資料を渡すか、確かめられない部分を分けて答えさせる。作り話が混ざる症状は <!-- link:begin plausible-falsehoods#diagnosis -->[もっともらしい嘘・出典の誤り › 原因を安く確かめる順](plausible-falsehoods.md#diagnosis)<!-- link:end --> に進む。

人の側にも落とし穴がある。読んだ記事や前に覚えたやり方が古いために、Claude の答えと食い違っているように見えることがある。その場合は、Claude ではなく情報の日付と版を疑う。切り分けは <!-- link:begin old-advice-doesnt-work#diagnosis -->[記事や前のやり方が通じない › 原因を安く確かめる順](old-advice-doesnt-work.md#diagnosis)<!-- link:end --> にある。

存在しない関数やパッケージを出されたときは、知識の古さに加えて読ませた資料の不足も原因になる。切り分けは <!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](uses-nonexistent-apis.md#diagnosis)<!-- link:end --> にある。

## 原因ごとの対処へ {#to-fixes}

最新の情報を知らない症状の原因は「見えていない」に絞られる。対処の本体は、次の持ち主のページにある。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)<br>[@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)<br>Claude Code 自身に聞く（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：Claude Code の新しい機能を聞いたら古い答えが返った"
    - **状況**：Claude Code の最近の機能について尋ねると、「その機能はない」と返った。公式の文書には載っているはずである。
    - **迷う候補**：Web 検索で調べさせる。公式の文書の URL を渡して読ませる。Claude Code 自身に聞く。
    - **選んだもの**：Claude Code 自身に聞き、答えに添えられた版を確かめる。
    - **理由**：Claude Code 自身に聞くと、公式の文書を調べて答える。URL を探す手間が要らない。ただし答えは手元の版より新しい機能を含みうるので、版を確かめてから使う。検索結果が古い記事に偏る不安があるときは、URL を渡す手に切り替える。

!!! example "判断例：古い書き方のコードが出る"
    - **状況**：ライブラリの設定を頼むと、動くが今は非推奨の書き方で出てきた。
    - **迷う候補**：検索させて新しい書き方を探させる。使っている版と公式の移行の文書の抜粋を渡して書き直させる。
    - **選んだもの**：使っている版と移行の文書の抜粋を渡す。
    - **理由**：書き方が古くなる速さは、対象によって違う。版と抜粋を渡せば、どの版の書き方かが確定する。検索は、古い記事を拾う可能性が残る。記事の古さを疑う場合は <!-- link:begin dating-information#layers -->いつの情報かを見分ける › 古くなる速さの三つの層（準備中）<!-- link:end --> で速さの層を見る。

## 予防 {#prevention}

毎回同じ補いをするなら、頼み方の工夫ではなく、仕組みに移す。

- 日付・使っている版・根拠にする資料を、依頼の型にして毎回付ける。この節の終わりの雛形がその型である。
- 使っている主要な製品やライブラリの版は、CLAUDE.md に書いて毎回の前提にする。版を上げたら書き換える。
- 公式の文書は、URL か @ 参照で直接読ませる。選び方は <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> にある。
- 最新が要る調べものは、検索かリサーチを使い、出典の日付を確かめる手順までを依頼に含める。リサーチの頼み方は <!-- link:begin using-research#requesting -->リサーチを使いこなす › 頼み方（範囲・出典の条件・出力の形）（準備中）<!-- link:end --> にある。

<!-- gen:begin snippet doesnt-know-latest/date-and-source -->
<!-- textlint-disable -->

???+ example "雛形：日付・版・資料を渡して最新の情報を答えさせる依頼の雛形"

    ```text
    ＜質問をここに書く＞

    答えるときの前提：
    - 今日の日付は＜今日の日付＞です。
    - 対象の製品やライブラリの版は＜使っている版＞です。
    - 最新の情報は、あなたの学習した知識ではなく、次の資料を根拠にしてください：＜公式の文書の URL、または貼った抜粋＞

    答えの扱いについて：
    - 資料に書かれていることと、あなたの知識から補ったことを分けて書いてください。
    - 資料に書かれていない新しい機能や版は、推測せずに「資料には書かれていない」と答えてください。
    - 答えに使った資料の箇所の日付か版を添えてください。

    理由：この答えをそのまま設定やコードに使うので、古い情報を今の情報として読むより、分からないと分かるほうが困りません。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet doesnt-know-latest/date-and-source -->

雛形は、日付・版・資料を渡し、資料にないことを分けて答えさせる。古い知識が混ざらなくなるとは限らない。設定やコードへ使う前に、出典の箇所を自分で確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)：Anthropic・英語・確認日 2026-11-04
- [Models overview](https://platform.claude.com/docs/en/models/overview)：Anthropic・英語・確認日 2026-11-04
- [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)：Anthropic・英語・確認日 2026-11-04
- [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)：Anthropic・英語・確認日 2026-11-04
- [CTFs in the AI Era](https://blog.includesecurity.com/2026/04/ctfs-in-the-ai-era/)：Include Security・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)

**次に読む**

- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- Claude Code 自身に聞く（準備中）

**関連**

- リサーチを使いこなす（準備中）
- [コネクタ（MCP）をアプリで使う](../app/connectors-in-the-app.md)
- [記事や前のやり方が通じない](old-advice-doesnt-work.md)
- いつの情報かを見分ける（準備中）
- [もっともらしい嘘・出典の誤り](plausible-falsehoods.md)
- [存在しない関数やパッケージを使う](uses-nonexistent-apis.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
