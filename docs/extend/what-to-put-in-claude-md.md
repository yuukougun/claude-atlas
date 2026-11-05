---
id: what-to-put-in-claude-md
title: CLAUDE.md に書くこと・書かないこと
aliases: [CLAUDE.md の書き方, CLAUDE.md に書かないこと, 地雷リスト, メモリファイル]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 30
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム, コンテスト]
summary: CLAUDE.md に残す行と外す行を見分け、外す行の移し先を決められる。推測できないコマンド・理由・落とし穴・確かめ方を残し、例外を許さない禁止は鍵に移して理由だけを書く。
signs:
  - {type: goal, text: CLAUDE.md に何を書けばよいか知りたい}
  - {type: goal, text: ビルドやテストのコマンドと落とし穴を、毎回説明せずに伝えておきたい}
  - {type: symptom, text: CLAUDE.md に構成の説明を長く書いたのに、役に立っている気がしない}
prerequisites: [where-instructions-sit, request-vs-lock]
related: [claude-md-length, path-scoped-rules, claude-md-vs-rules-skills-styles, when-to-lock, permission-rules, init-and-first-claude-md, instructions-ignored, repeating-the-same-explanation, how-skills-load, using-auto-memory, agents-md, claude-md-loading-order, hooks-basics, ai-usage-guidelines, share-team-settings, when-to-add-what]
tracks: [claude-md]
outdated_advice: [architecture-in-claude-md, hash-to-memorize]
sources: [cc-docs-memory, cc-docs-best-practices, cc-docs-features-overview, cc-docs-context-window, humanlayer-writing-good, cc-changelog, cc-docs-changelog, cc-docs-interactive-mode]
volatility: 中
sections:
  - {title: 書くこと, anchor: what-to-write}
  - {title: 書かないことと、移し先, anchor: what-to-leave-out}
  - {title: 足すときの手順, anchor: adding-lines}
  - {title: 場面別の例：チームとコンテスト, anchor: scenes}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：CLAUDE.md に残す行と外す行を見分け、外す行の移し先を決められる。残すのは、推測できないコマンド・理由・落とし穴・確かめ方である。
    - **いつ引くか**：CLAUDE.md に何を書けばよいか知りたいとき。ビルドやテストのコマンドと落とし穴を、毎回説明せずに伝えておきたいとき。構成の説明を長く書いたのに、役に立っている気がしないとき。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。Claude が読んで従うだけで、何も止められない。例外を許さない禁止は、鍵（deny ルールやフック）に移し、CLAUDE.md には理由と相談の基準だけを書く。
    - **前提**：<!-- link:begin where-instructions-sit -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)<!-- link:end -->、<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：CLAUDE.md の書き方・CLAUDE.md に書かないこと・地雷リスト・メモリファイル
<!-- textlint-enable -->

CLAUDE.md に書くこと・書かないことは、CLAUDE.md の各行を「残す」「外す」「別の置き場所へ移す」に仕分ける判断である。残す基準は、コードを読んでも Claude に分からないことかどうかである。外した行は、構成の説明のように書かなくてよいもの、手順のように別の置き場所へ移すもの、禁止のように鍵へ移すものの 3 つに分かれる。

## 書くこと {#what-to-write}

CLAUDE.md に書くのは、リポジトリを読んでも Claude に分からないことだけである。CLAUDE.md はセッションの開始で読み込まれる。そして、1 行ごとに関係のない作業でも Claude の注意を少しずつ使う。だから行が多いほど良いわけではない。

ここで防ぐ原因は 2 つある。1 つは、Claude にリポジトリから読み取れない約束や理由が**見えていない**ことである。もう 1 つは、要らない行が増えて、要る行が**散らかった**中に埋もれることである。この辞典の原理でいえば「見せる」にあたる。見せるのは、Claude が自力では見つけられないものに限る。

公式の Best practices を 2026-11-05 に確かめた時点では、CLAUDE.md に入れるものとして、次の 4 種類が挙がっている。

| 書くもの | 例 | 書く理由 |
| --- | --- | --- |
| 確かめ方のコマンド | 全件のテスト、型検査、lint、1 つのテストファイルだけを流す方法 | Claude が自分の作業を、進めながら確かめられる |
| 見た目が紛らわしい場所 | 至る所にあるが新しいコードで真似してはいけない古い書き方、使われていないように見えて生きているフォルダ | コードを読むほど、誤った見本を拾う |
| リポジトリにない決め事 | チームが選んだエラー処理の関数、デプロイの流れ、審査が要る変更 | コードには結果しか残らず、決めた理由が残らない |
| すでに繰り返し直させたこと | 同じ訂正を重ねた規約 | 直し続けるより、1 行で渡すほうが安い |

実務家の記事も、コマンド・理由・落とし穴・検証の手順を書くという点で一致する。中でも落とし穴を並べた「地雷リスト」が効くとする記事が多い（根拠：中）。

### 1 行の形

行の形で、読まれ方が変わる。次の 3 つを守る。

- **コマンドは、そのまま貼って動く形で書く。** 前提（先に DB を起こす、など）も同じ行に書く。前提が抜けていると、Claude は失敗を見て、毎回その場で原因を探すことになる。
- **規約と禁止には、理由を添える。** 実務家の記事は、何・なぜ・どうやってに分けて書くことを勧める（根拠：中）。理由があれば、書いた場面から少し外れたときにも、趣旨に沿って判断しやすい。
- **禁止だけで終わらせず、代わりを書く。** 「手で直さない」だけでなく「`make codegen` で作り直す」まで書く。

確かめ方の行のうち、いちばん有用なのは、検証を走らせるコマンドの行である。公式の文書も、リポジトリに検証の仕組みがあるなら、CLAUDE.md の最も有用な 1 行はそれを走らせるコマンドだとする。ただし、この行は「コマンドを知らせる」だけで、通るまで終わらせない強制にはならない。強制したいなら、Stop フックに移す（<!-- link:begin hooks-basics#events -->[フックの考え方とイベント › 代表的なイベント](../enforce/hooks-basics.md#events)<!-- link:end -->）。

### 最小の使い方

次の短い CLAUDE.md は、確かめ方・落とし穴・決めたことを書き、最後に、鍵へ移した禁止の理由だけを残した例である。コマンドと場所は、自分のリポジトリのものに書き換える。

<!-- gen:begin snippet what-to-put-in-claude-md/short-claude-md -->
<!-- textlint-disable -->

??? example "雛形：短い CLAUDE.md の例（コマンド・理由・落とし穴・確かめ方）"

    ```markdown
    # 開発の前提

    ## 確かめ方

    - 全件のテスト：`make test`。先に `make db-up` で DB を起こす。起きていないと全件が失敗する
    - 1 ファイルだけ：`make test T=tests/foo_test.py`
    - 型検査：`make typecheck`。自分の変更を確かめるのに使う

    ## 落とし穴

    - `src/legacy/` は今も動いているが、新しいコードで書き方を真似しない。移行の途中で、決済の処理だけがここに残っている
    - `generated/` は手で直さない。`make codegen` で作り直す。手で直しても、次の生成で消える

    ## 決めたこと

    - エラーは `src/lib/errors.ts` の関数で投げる。生の文字列を投げない。ログの集計がこの形を前提にしているため

    ## 止めていること

    - `.env` の読み取りは設定で断ってある。値が要る作業は、読もうとせず、人に頼む
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet what-to-put-in-claude-md/short-claude-md -->

読み込まれたかは、セッションの中で `/context all` を流して確かめる。確かめ方の全体は、<!-- link:begin claude-md-vs-rules-skills-styles#verify -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示が読み込まれたかの確かめ方](claude-md-vs-rules-skills-styles.md#verify)<!-- link:end -->にある。最初の叩き台を `/init` で作る進め方は、<!-- link:begin init-and-first-claude-md#run-init -->[/init と最初の CLAUDE.md › /init で叩き台を作る](../cli/init-and-first-claude-md.md#run-init)<!-- link:end -->が持つ。

## 書かないことと、移し先 {#what-to-leave-out}

書かないものは、書かなくてよいものか、CLAUDE.md より合う置き場所があるものである。外した行の行き先を、先に決めておく。

| 書かないもの | 移し先と案内 |
| --- | --- |
| ディレクトリの木、ファイルの一覧、使っているフレームワークの説明 | どこにも書かない。Claude がリポジトリを自分で読む。書くのは、読んでも分からない例外だけ |
| インデントなど、formatter や linter で検査できる規約 | formatter と linter に任せる。毎回確実に直したいときは、フックに移す（<!-- link:begin hooks-basics#deterministic -->[フックの考え方とイベント › 決定的なフックと、モデルが判断するフック](../enforce/hooks-basics.md#deterministic)<!-- link:end -->） |
| 特定のフォルダやファイルにだけ効く規約 | rules と paths に移す（<!-- link:begin path-scoped-rules -->[.claude/rules と paths で必要なときだけ読ませる](path-scoped-rules.md)<!-- link:end -->） |
| たまにしか使わない長い手順 | スキルに移す（<!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end -->） |
| 例外を許さない禁止 | deny ルールかフックに移す（<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->）。CLAUDE.md には理由と相談の基準だけを残す |
| 自分だけの好み | 個人用の `CLAUDE.local.md` に書き、`.gitignore` に入れる（<!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end -->） |
| すぐ古くなるコードの写し | コードの場所を `file:line` で指す（根拠：中） |
| Claude が会話の中で学んだこと | 自動メモリに任せる（<!-- link:begin using-auto-memory -->[自動メモリ](using-auto-memory.md)<!-- link:end -->） |
| 守られない行に足す強調（IMPORTANT や全大文字） | 足さない。行が埋もれているならファイルを短くし、例外のない規則なら鍵に移す |

この表のうち、構成の説明・例外のない規則・手順のスキル・個人の好み・強調の扱いは、公式の Best practices で確かめた。linter に任せることとコードの写しを避けることは、複数の実務家の記事で一致する助言である（根拠：中）。

### 判断例

!!! example "判断例：構成の説明を残すか"
    - **状況**：CLAUDE.md の冒頭に、ディレクトリの木と、フレームワークの説明を書いてある。
    - **迷う候補**：新しく入る人にも役立つので残す。Claude が読めば分かるので外す。
    - **選んだもの**：木と説明を外し、`src/legacy/` のように見た目と実際が食い違う場所だけを残した。
    - **理由**：Claude はリポジトリを自分で読むので、木と説明は新しい情報を足さず、毎回の読み込みの分だけ場所を取る。人の読み物としての案内は、README に任せる。

!!! example "判断例：`.env` を読ませない"
    - **状況**：「`.env` を絶対に読まないこと」と、強調して CLAUDE.md に書いてある。それでも読みに行く場面があった。
    - **迷う候補**：さらに強調を足して残す。deny ルールに移す。
    - **選んだもの**：deny ルールに移し、CLAUDE.md には「値が要る作業は、読もうとせず人に頼む」と理由だけを残した。
    - **理由**：例外がなく、機械で判定できる禁止だからである。強調を足しても直らない行は、鍵に移すサインだと公式の文書もいう。ただし、deny ルールにも効かない場面（子プロセスなど）がある。詳しくは<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->で確かめる。

!!! example "判断例：リリースの手順を残すか"
    - **状況**：CLAUDE.md に、リリースの手順が長く書いてある。使うのはリリースの日だけである。
    - **迷う候補**：確実に読まれるように CLAUDE.md に残す。スキルに移す。
    - **選んだもの**：手順をスキルに移し、CLAUDE.md には「リリースは人が承認する」の 1 行だけを残した。
    - **理由**：スキルは、名前と説明だけが常駐し、本文は必要なときにだけ読まれる。使わない日の作業が、長い手順で押されない。

## 足すときの手順 {#adding-lines}

CLAUDE.md に行を足すのは、見えていないことに気づいたときである。思いつきで足さず、次の順で決める。

1. **足す理由を確かめる。** 同じ訂正を繰り返したか、毎回同じ説明をしているかを見る。まだ一度なら、足さずに様子を見てよい。何回で足すかの目安は、<!-- link:begin when-to-add-what -->[拡張を足すタイミング](when-to-add-what.md)<!-- link:end -->にある。
2. **削除テストにかける。** 「この行を消したら、Claude は誤るか」と問い、誤らないなら足さない。問いの詳しい使い方は、<!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end -->にある。
3. **置き場所を決める。** 「書かないことと、移し先」の表に当てはめ、CLAUDE.md で足りるか確かめる。例外のない規則は、行ではなく鍵で守る。
4. **行を書く。** コマンドは動く形で、規約には理由を、禁止には代わりを添える。
5. **足す。** Claude に「CLAUDE.md に足して」と頼むか、`/memory` でファイルを開いて自分で書く。
6. **効いたかを確かめる。** 新しいセッションで、その行が効く依頼を出し、行が読み込まれたことと、振る舞いが変わったことを見る。変わらなければ、<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end -->の順で原因を切り分ける。

足すだけでは、ファイルは育ち続ける。足した分は、定期的に剪定する。チームで育てる進め方は、<!-- link:begin claude-md-length#team -->[CLAUDE.md の長さと剪定 › チームで育てる](claude-md-length.md#team)<!-- link:end -->にある。`/init` で作った叩き台は、読んで削ってから使う（<!-- link:begin init-and-first-claude-md#prune -->[/init と最初の CLAUDE.md › 叩き台を削ってから使う（削り方は claude-md-length）](../cli/init-and-first-claude-md.md#prune)<!-- link:end -->）。

## 場面別の例：チームとコンテスト {#scenes}

チームで使う CLAUDE.md は、冒頭に「任せてよい・止まって相談する・禁止」の 3 区分を置くと、方針が人と Claude の両方に伝わる。ただし「禁止」の区分は、頼むだけの文である。守らせたい禁止は、deny ルールとフックでも止める。3 区分は、allow ルール・ask ルール・deny ルールとほぼ一対一で対応する。置き場所を二層にする考え方は、<!-- link:begin request-vs-lock#two-layers -->[お願いと鍵（決定論的か、非決定論的か） › 二層で書く](../basics/request-vs-lock.md#two-layers)<!-- link:end -->にある。

<!-- gen:begin snippet what-to-put-in-claude-md/team-three-zones -->
<!-- textlint-disable -->

??? example "雛形：チームの AI の使い方を 3 区分に分けて冒頭に置く例"

    ```markdown
    # AI の使い方

    ## 任せてよい

    - テストで守られている実装と、仕様書で処理が決まっている実装
    - 解法や仕様を変えない高速化とリファクタリング
    - 集計やビジュアライザなど、本体に影響しない補助の道具

    ## 止まって相談する

    - 仕様が曖昧で、読み方が複数ある変更
    - 公開しているインターフェースやデータの形を変える変更
    - 評価の方法やパラメータの範囲の解釈に関わる変更

    ## 禁止

    - 本番の環境への書き込み
    - 秘密情報（`.env`・鍵）の読み取りと出力
    - 評価用のデータとスクリプトの変更

    この 3 区分は頼むだけの文である。「禁止」の項目は、deny ルールとフックでも止めてある。理由は、取り返しがつかないか、結果の信頼を壊すためである。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet what-to-put-in-claude-md/team-three-zones -->

「止まって相談する」の行がどこまで守られるかは、モデルの癖にも左右される。現行のモデルでの挙動は、まだ確かめていない。社内ガイドラインに書く側の話は、<!-- link:begin ai-usage-guidelines#three-categories -->[社内ガイドラインに書くこと › 任せてよい・止まって相談する・禁止](../team/ai-usage-guidelines.md#three-categories)<!-- link:end -->が持つ。

コンテストの CLAUDE.md は、ビルドと評価のコマンド、制限時間、規則の確認先を書く。大会の規則の中身は、CLAUDE.md に写さない。規則は版ごとに変わるので、写すと古くなる。書くのは確認先だけにして、規則そのものは主催者のページで確かめる。

<!-- gen:begin snippet what-to-put-in-claude-md/contest-claude-md -->
<!-- textlint-disable -->

??? example "雛形：コンテスト用の CLAUDE.md の例（ビルドと評価のコマンド・制限時間・規則の確認先）"

    ```markdown
    # コンテスト用の前提

    ## コマンド

    - ビルド：`<ビルドのコマンド>`
    - 手元の評価：`<評価のコマンド>`。結果は `<出力先>` に出る。点数は直前の版と比べて見る
    - 1 ケースだけ：`<1 ケースを流すコマンド>`

    ## 時間と段取り

    - 1 回の評価に使える時間は `<制限時間>`。超えそうな変更は、先に小さい入力で確かめる
    - 提出の操作は人がする。提出用のファイルを作るところで止まる

    ## 規則

    - AI の利用に関する規則は大会ごとに違う。作業の前に、規則のページ `<規則の URL>` を人に確かめてもらう。ここに条文は写さない
    - 規則に当たるかもしれない作業は、進める前に止まって人に聞く

    ## 触らないもの

    - 採点用のデータと評価のスクリプトは、読み取りだけにする。変えると点数が意味を失う
    - 特定の入力だけを見分けて答えを変える分岐は書かない。手元の点数が上がっても、本番では通用しない
    - ここに書いた禁止は、設定（deny ルールとフック）でも止めてある
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet what-to-put-in-claude-md/contest-claude-md -->

評価用のデータとスクリプトを触らせない行は、結果の意味に関わるので、設定でも止める。CLAUDE.md の文と設定は、組にして置く。

## 効かない場面と落とし穴 {#limits}

CLAUDE.md は、強制される設定ではなく文脈として読まれる。何を書いても、守られる保証はない。書いた行が破られる理由は、<!-- link:begin request-vs-lock#what-happens -->[お願いと鍵（決定論的か、非決定論的か） › 何が起きるか](../basics/request-vs-lock.md#what-happens)<!-- link:end -->で確かめられる。

- **長いファイルでは、行が埋もれる。** 行数が増えるほど、1 行あたりの重みは下がる。強調で補わず、短くする。
- **会話で言った禁止は、圧縮で消える。** CLAUDE.md に書いた行は、圧縮の後、プロジェクトの根の分が<!-- gen:begin feature survives_compaction -->残る<!-- gen:end feature survives_compaction -->。入れ子の CLAUDE.md は、いったん要約に消え、必要になったときに読み直される（<!-- link:begin claude-md-loading-order#after-compaction -->[CLAUDE.md の階層と読み込み順 › 圧縮の後と、クラウドのセッション](claude-md-loading-order.md#after-compaction)<!-- link:end -->）。会話で口にしただけの禁止は残らない（<!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end -->）。
- **複数のファイルで指示が食い違うと、どちらかが選ばれる。** CLAUDE.md は上書きではなく連結される。モノレポでほかのチームの指示が混ざる場合は、<!-- link:begin claude-md-loading-order#monorepo -->[CLAUDE.md の階層と読み込み順 › モノレポとほかのチームの指示](claude-md-loading-order.md#monorepo)<!-- link:end -->で確かめる。
- **書いたコマンドや場所は古くなる。** 存在しないファイルへの参照や、矛盾した指示は、`/doctor prompt-audit` が報告する。
- **書いたのに使われないと感じるとき。** 行が長いファイルに埋もれているか、鍵に移すべき規則かのどちらかが多い。切り分けは<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end -->に任せる。毎回同じ説明をしてしまう側からの入口は、<!-- link:begin repeating-the-same-explanation#diagnosis -->[毎回同じ説明をしている › 原因を安く確かめる順](../symptoms/repeating-the-same-explanation.md#diagnosis)<!-- link:end -->にある。

Claude Code は WSL・Linux の CLI を基準に書いている。ほかの OS と IDE 拡張で、CLAUDE.md の読み込みが同じかは未確認である。

## 比べる相手 {#compare}

CLAUDE.md から外した行の置き場所は、目的で選ぶ。

- 常に効かせる規則は CLAUDE.md、フォルダごとの規約は rules、場面ごとの手順はスキル、応答の形は出力スタイルに置く。選び方は<!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end -->にある。
- 人が書く CLAUDE.md と、Claude が自分で書き溜める記録の分担は、<!-- link:begin using-auto-memory -->[自動メモリ](using-auto-memory.md)<!-- link:end -->が持つ。
- ほかのエージェントツールと同じ指示を共有する場合は、<!-- link:begin agents-md -->[AGENTS.md とほかのツールとの共有](agents-md.md)<!-- link:end -->を使う。

## 古くなった助言 {#outdated}

昔の記事にある助言のうち、次の 2 つは今の版に当てはまらない。

- **構成やファイルの並びを CLAUDE.md に書く。** 今は、書かない。Claude はリポジトリを自分で読むので、書くのはリポジトリを読んでも分からないことだけにする。扱いは<!-- link:begin outdated-advice-ledger#architecture-in-claude-md -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#architecture-in-claude-md)<!-- link:end -->にまとめてある。
- **入力の先頭に `#` を付けて、CLAUDE.md に記憶させる。** 今は、この近道はない。足したいことは、Claude に CLAUDE.md の編集を頼むか、`/memory` で自分で書く。扱いは<!-- link:begin outdated-advice-ledger#hash-to-memorize -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#hash-to-memorize)<!-- link:end -->にまとめてある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)：HumanLayer・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04
- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**次に読む**

- [CLAUDE.md の長さと剪定](claude-md-length.md)
- [CLAUDE.md の階層と読み込み順](claude-md-loading-order.md)
- [.claude/rules と paths で必要なときだけ読ませる](path-scoped-rules.md)
- [自動メモリ](using-auto-memory.md)

**関連**

- [CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [/init と最初の CLAUDE.md](../cli/init-and-first-claude-md.md)
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [AGENTS.md とほかのツールとの共有](agents-md.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [社内ガイドラインに書くこと](../team/ai-usage-guidelines.md)
- [チームで設定を共有する](../team/share-team-settings.md)
- [拡張を足すタイミング](when-to-add-what.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
