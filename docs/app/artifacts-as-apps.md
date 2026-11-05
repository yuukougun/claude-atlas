---
id: artifacts-as-apps
title: アーティファクトを小さなアプリにする
aliases: [Claude を呼ぶアーティファクト, アーティファクトのデータ保存]
type: feature
field: app
chapter: 調べる・作る
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [app]
principle: [確かめる]
prevents: [境界がない]
scenes: [開発, データ分析]
summary: アーティファクトに Claude の呼び出し・アプリの接続・データの保存を持たせ、繰り返し使う道具にできる。共有したとき誰の権限と枠で動くかも分かる。
signs:
  - {type: goal, text: 簡単な計算ツールや入力フォームを作って使い回したい}
  - {type: goal, text: チームで使う小さな道具を会話から作りたい}
prerequisites: [artifacts-overview]
related: [connectors-in-the-app, prompt-injection-in-practice, shared-artifacts-and-files, entrusted-data, what-uses-up-limits, build-observation-tools]
tracks: [artifacts]
sources: [hc-artifacts]
volatility: 高
sections:
  - {title: 使いどころ, anchor: when}
  - {title: Claude を呼ぶ・アプリにつなぐ・データを残す, anchor: runtime}
  - {title: 共有したときに誰の権限と枠で動くか, anchor: whose-account}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：アーティファクトに Claude の呼び出し・アプリの接続・データの保存を持たせ、繰り返し使う道具にできる。
    - **いつ引くか**：簡単な計算ツールや入力フォームを作って使い回したいとき、チームで使う小さな道具を会話から作りたいとき。
    - **強制力**：<!-- gen:begin feature artifacts/enforcement -->なし<!-- gen:end feature artifacts/enforcement -->。道具の動きを止める仕組みではない。初回の承認の画面で、使う側が許可を決める。
    - **前提**：<!-- link:begin artifacts-overview -->[アーティファクト（会話の中で作る文書・スライド・デザイン）](artifacts-overview.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Claude を呼ぶアーティファクト・アーティファクトのデータ保存
<!-- textlint-enable -->

アーティファクトを小さなアプリにするとは、会話の中で作ったアーティファクトに、Claude の呼び出し、接続したアプリの読み書き、データの保存を持たせることである。1 回見せて終わりの成果物が、何度も開いて使う道具になる。その代わり、共有したときに誰のアカウントの枠と接続で動くかを、作る側が先に知っておく必要がある。

## 使いどころ {#when}

小さなアプリにする価値があるのは、同じ道具を繰り返し使うときである。

- 入力フォームを作り、記入した内容を残して集計したい。
- 計算ツールを作り、数値を変えながら何度も使いたい。
- チームで使うチェックリストや記録帳を、会話から作って配りたい。
- 集めた文章を、Claude に要約させる画面を付けたい。

一度きりの計算や短い答えは、ふつうの返答で足りる。道具にするのは、開き直して使う場面があるときだけにする。

防ぐ原因は「境界がない」である。小さな道具は作るのが簡単なので、誰のデータが誰に見え、誰の枠で動き、誰のアプリにつながるかを決めないまま配ってしまう。この境界を、作る前に頼みの中で決めておく。決める項目は、データの保存先（個人用か共有か。「Claude を呼ぶ・アプリにつなぐ・データを残す」の節で説明する）と、共有したときに誰の枠と接続で動くか（「共有したときに誰の権限と枠で動くか」の節で説明する）である。

道具の出す値は、見た目が整っていても合っているとは限らない。渡す前に、小さな例を手で計算した結果と合うかを確かめる。やり方は <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end --> にある。計算そのものは、Claude を呼ばずに通常のコードで書かせる。Claude を呼ぶ処理は、文章の要約や分類のように、答えが 1 通りに決まらない部分だけに使う。これは設計上の推論であり、実践例による裏づけはない（推論・実践例なし）。

## Claude を呼ぶ・アプリにつなぐ・データを残す {#runtime}

アーティファクトが持てる実行時の能力は 3 つある。公式の記事（確認日 2026-11-05）で確かめた内容を、次に分けて書く。アプリへの接続とデータの保存が使えるプランは <!-- fact:begin artifact-runtime-plans -->Pro・Max・Ultra・Team・Enterprise（Web とデスクトップ）（2026-11-05 時点）<!-- fact:end --> である。

- **Claude を呼ぶ**：アーティファクトの中から、Claude を直接呼べる。API キーは要らない。呼んだ分は、道具を使う人それぞれのプランの枠から引かれる。新しく作った道具は、初めて Claude を使おうとするときに許可を求める。
- **アプリにつなぐ**：接続したアプリやカスタムのコネクタを、読み書きできる。初めて使うときに、使うアプリと道具が画面に示され、承認する。個々の道具をオフにでき、その選択は残る。1 回ごとの承認が要る接続の道具は、アーティファクトからは使えない。
- **データを残す**：道具を閉じても残るデータを持てる。保存先は、使う人ごとに非公開の個人用と、使う全員が同じデータを見る共有の 2 つである。入れられるのは文字だけで、画像・ファイル・バイナリは入らない。保存の上限は <!-- fact:begin artifacts-storage-limit -->1 つのアーティファクトにつき 20MB まで。テキストのみ（2026-11-05 時点）<!-- fact:end --> である。個人用と共有のデータは、分けて保存される。共有に初めて書くときは、他の人にも見える旨の確認が出る。

接続は書き込みもできるので、使い方を広げる前に守りを決める。道具に読ませた内容へ指示が仕込まれる経路は <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](../safety/prompt-injection-in-practice.md#channels)<!-- link:end --> で分かる。防ぐ手立ては、持たせる権限と通信の側にある。その考え方は <!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](../safety/prompt-injection-in-practice.md#what-works)<!-- link:end --> にまとまっている。接続できるアプリの種類は <!-- link:begin connectors-in-the-app#types -->[コネクタ（MCP）をアプリで使う › コネクタの種類](connectors-in-the-app.md#types)<!-- link:end -->、信頼の判断は <!-- link:begin connectors-in-the-app#trust -->[コネクタ（MCP）をアプリで使う › 信頼してよいか](connectors-in-the-app.md#trust)<!-- link:end --> で分かる。

保存先は、道具を作る人が決める。どのデータを個人用に置き、どれを共有に置くかは、作る時点で依頼に書く。次の雛形は、保存するデータと保存先の区分を、作り終えた後の返答に一覧で書かせる。

<!-- gen:begin snippet artifacts-as-apps/request-data-tool -->
<!-- textlint-disable -->

??? example "雛形：データを残す小さな道具を頼む文の雛形"

    ```text
    次の小さな道具を、アーティファクトとして作ってください。

    - 目的：＜何をする道具か。例：チームの週次ふりかえりの記入と集計＞
    - 使う人：＜誰が使うか。例：自分を含む 5 人のチーム＞
    - 入力：＜入力欄。例：今週よかったこと、困ったこと、次に試すこと＞
    - 保存するデータ：＜残すもの。例：記入した文章と日付＞
    - 保存先：＜個人用（使う人ごとに非公開）か、共有（全員が同じデータを見る）か＞
    - Claude を呼ぶ処理：＜要るか。要るなら何を任せるか。例：集めた文章の要約だけ。数の集計は Claude を呼ばず、通常のコードで行う＞

    守ること：
    - 保存するのは文字だけにしてください。画像やファイルは保存しないでください。
    - 共有の保存先に置くデータは、使う全員に見えてよいものに限ってください。個人の入力を共有に置く場合は、入力欄の近くに「全員に見えます」と表示してください。
    - 接続したアプリは、読むだけで足りるところでは書き込まないでください。
    - 作り終えたら、この道具が保存するデータの一覧と、それぞれが個人用か共有かを、返答に書いてください。

    理由：作った道具を他の人にも使ってもらうので、誰のデータが誰に見えるかを、渡す前に私が確かめたいからです。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet artifacts-as-apps/request-data-tool -->

作られた道具は、返答の一覧と実際の動きが合うかを、自分で一度使って確かめる。個人用のつもりのデータが共有に置かれていないか、画面に出る確認の表示と照らす。

古い形のアーティファクト（legacy artifacts）は扱いが違う。公式の記事は、legacy ではデータの保存に公開が要り、公開を取り消すと保存したデータが完全に消える、と書いている（確認日 2026-11-05）。新しく作った道具は、公開しなくても保存できる。legacy の背景は <!-- link:begin artifacts-overview#pitfalls -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 効かない場面・落とし穴](artifacts-overview.md#pitfalls)<!-- link:end --> にある。

## 共有したときに誰の権限と枠で動くか {#whose-account}

道具を共有すると、動く場所は作った人のアカウントから、使う人のアカウントに移る。次の表は、何が誰のものになるかをまとめたものである。

| 動くもの | 誰のものか |
| --- | --- |
| Claude の呼び出し | 使う人それぞれのプランの枠。作った人の枠ではない |
| アプリの接続 | 使う人が自分で接続する。共有や公開された道具でも同じ |
| 個人用の保存 | 使う人ごとに非公開。他の人からは見えない |
| 共有の保存 | 使う全員が同じデータを見る |

公式の記事は、共有された道具でも閲覧者が自分のアプリを接続すると書いている。組織の管理者は、この接続を組織全体で無効にできる。組織のプランでは、共有された道具を組織の人が使っても、作った人の費用は増えない、とも書かれている。

この表から、作る側と使う側で気をつけることが分かれる。

- **作る側**：自分の接続や権限で動くと思い込まない。他の人が使うと、その人の接続と枠で動く。共有の保存に置くデータは、使う全員に見える。個人の入力や機微な内容を共有に置かない。顧客のデータや規約付きのデータは、扱いを決める契約のある面だけで使う。判断は <!-- link:begin entrusted-data#whose-data -->[預かったデータ・規約付きのデータを AI に渡してよいか › 誰のデータで、何が決まっているか](../safety/entrusted-data.md#whose-data)<!-- link:end --> と <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end --> にある。
- **使う側**：道具が求めるアプリと道具を、承認の前に読む。他人が公開した道具は、知らない送り主から届いたファイルと同じに扱う。開く前の確かめ方は <!-- link:begin shared-artifacts-and-files#opening-others -->[共有リンクと公開アーティファクトの扱い › 他人が公開したものを開くとき](../safety/shared-artifacts-and-files.md#opening-others)<!-- link:end --> にある。
- **配る側**：道具を使うほど、使う人の枠が減る。配るときに、枠を使うことを伝える。何が枠を早く減らすかは <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](../cost/what-uses-up-limits.md#causes)<!-- link:end --> にある。

共有のしかたと、取り消せるもの・取り消せないものは、持ち主のページが扱う。共有の入口は <!-- link:begin shared-artifacts-and-files#how-to-share -->[共有リンクと公開アーティファクトの扱い › 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有）](../safety/shared-artifacts-and-files.md#how-to-share)<!-- link:end -->、取り消しは <!-- link:begin shared-artifacts-and-files#revoke -->[共有リンクと公開アーティファクトの扱い › 取り消せるもの・取り消せないもの](../safety/shared-artifacts-and-files.md#revoke)<!-- link:end --> にある。共有で渡るのはその時点の写しなので、渡した後に気づいた誤りは、すでに見られている可能性がある。公開の手順は <!-- link:begin artifacts-overview#sharing -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 公開と共有](artifacts-overview.md#sharing)<!-- link:end --> にもまとまっている。

!!! example "判断例：チームの週次ふりかえりを集める道具"
    - **状況**：5 人のチームで、毎週のふりかえりを記入して、全員が互いの記入を読めるようにしたい。
    - **迷う候補**：記入を個人用の保存に置き、集計の画面だけ共有する。記入を共有の保存に置き、全員が同じ一覧を見る。
    - **選んだもの**：記入は共有の保存に置き、入力欄の近くに「全員に見えます」と表示する。人事評価の内容は、この道具に書かない取り決めも決める。
    - **理由**：目的が互いの記入を読むことなので、共有の保存が合う。個人用の保存では、他の人の記入が見えない。ただし共有は全員に見えるため、書いてよい内容を先に決め、画面でも知らせる。

## 効かない場面・落とし穴 {#pitfalls}

- **作った人の権限で動くと思い込む**：道具は使う人のアカウントの接続と枠で動く。自分の環境で動いた通りに、他の人の環境でも動くとは限らない。
- **個人の入力を共有の保存に置く**：共有の保存は全員に見える。作る時点で、どのデータをどちらに置くかを決める。
- **画像やファイルを保存しようとする**：保存できるのは文字だけである。画像は、別の置き場に置いて、その場所を文字で残す形を検討する。
- **承認が毎回要る接続は使えない**：1 回ごとの承認が要る接続の道具は、アーティファクトからは使えない。使いたい道具が出ないときは、まずこれを疑う。
- **Claude を呼ぶ処理の出力が揺れる**：同じ入力でも、答えの書き方が変わることがある。計算と集計は通常のコードで書かせ、結果を小さな例で確かめる。
- **使う人の枠を知らせない**：道具を使うと、使う人の枠が減る。配る相手に、あらかじめ伝える。
- **アプリ以外の面は未確認**：この機能は、アプリ（Web とデスクトップ）での動きを扱う。Claude Code と API で同じ動きをするかは、確かめていない。モバイルの動作も未確認である。
- **プランで使えないことがある**：接続とデータ保存は、使えるプランが限られる（<!-- fact:begin artifact-runtime-plans -->Pro・Max・Ultra・Team・Enterprise（Web とデスクトップ）（2026-11-05 時点）<!-- fact:end -->）。使えないときは、公式の記事と料金のページで確かめる。

## 比べる相手 {#compare}

小さなアプリにするのは、道具を繰り返し使う場面の選択肢の 1 つである。ほかの手段との分担を次に示す。

- **ふつうのアーティファクト**：読んで渡すだけの文書・スライド・モックなら、実行時の能力は要らない。テンプレートの選び方は <!-- link:begin artifacts-overview#templates -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › テンプレートの選び方](artifacts-overview.md#templates)<!-- link:end --> にある。
- **コネクタを会話から使う**：道具を作らず、会話の中でアプリを呼ぶだけなら、コネクタで足りる。読ませ方と信頼の判断は <!-- link:begin connectors-in-the-app#on-demand -->[コネクタ（MCP）をアプリで使う › 使うときだけ読ませる（On demand）](connectors-in-the-app.md#on-demand)<!-- link:end --> にある。
- **観察の道具を作らせる**：結論を出させる代わりに、集計や可視化の道具を作らせる使い方は、<!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [アーティファクト（会話の中で作る文書・スライド・デザイン）](artifacts-overview.md)

**関連**

- [コネクタ（MCP）をアプリで使う](connectors-in-the-app.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [共有リンクと公開アーティファクトの扱い](../safety/shared-artifacts-and-files.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
