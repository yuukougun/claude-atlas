---
id: files-and-code-execution
title: ファイル作成とコード実行
aliases: [File creation, Code execution, Cloud code execution and file creation]
type: feature
field: app
chapter: 調べる・作る
order: 100
level: 整える
priority: 必須
surfaces: [app]
principle: [確かめる, 縛る]
prevents: [確かめていない, 境界がない]
scenes: [データ分析, 文章]
summary: 表計算・スライド・文書・PDF のファイルを作らせ、隔離された環境でコードを実行して集計や図を作れる。ネットワークの設定と、その危険も分かる。
signs:
  - {type: goal, text: 表計算やスライドのファイルを作らせたい}
  - {type: goal, text: データを集計して図にしてほしい}
  - {type: situation, text: 社外に出したくないデータを分析させる, anchor: network}
prerequisites: []
related: [artifacts-overview, data-analysis, office-paperwork, prompt-injection-in-practice, entrusted-data, character-encodings, how-attachments-are-read, shared-artifacts-and-files]
tracks: [file-creation, code-execution]
sources: [hc-files, hc-release-notes, claude-apps-release-notes-archive]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 頼み方, anchor: usage}
  - {title: 実行環境とネットワークの設定, anchor: network}
  - {title: 作ったファイルの受け取り方, anchor: outputs}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：表計算・スライド・文書・PDF のファイルを作らせ、隔離された環境でコードを実行して集計や図を作れる。
    - **いつ引くか**：表計算やスライドのファイルを作らせたいとき、データを集計して図にしてほしいとき、社外に出したくないデータを分析させるとき。
    - **止められるもの**：ネットワークの設定は鍵で、外への通信を止められる。依頼の文の「外へ送らないで」はお願いで、通信を止めない。
    - **前提**：なし

<!-- textlint-disable -->
別名：File creation・Code execution・Cloud code execution and file creation
<!-- textlint-enable -->

ファイル作成とコード実行は、アプリ（claude.ai・Desktop・Mobile）で使える機能である。Claude が隔離された環境（サンドボックス）でファイルを作り、コードを動かす。答えを文章ではなく、ファイルや集計の結果で受け取る使い方に向く。受け取ったあとは、確かめて、直させる。

## 使いどころ {#when}

この機能の使いどころは、答えを文章ではなく成果物で受け取りたい場面である。作れるのは、Excel（`.xlsx`）、PowerPoint（`.pptx`）、Word（`.docx`）、PDF のファイルである。実行環境では Python などが動くので、CSV や TSV の集計、PNG の図、簡単な機械学習のモデルの構築もできる。

防ぐ原因は 2 つある。

- **確かめていない**：文章の暗算ではなく、コードで数えた結果が返る。スクリプトが残るので、数字をあとで出し直せる。確かめ方は、データの分析のページに書いた（<!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](../recipes/data-analysis.md#check-raw-data)<!-- link:end -->）。
- **境界がない**：コードは隔離された環境の中で動く。外への通信は設定で縛れる。ただし、縛れる範囲には限りがある（次の「実行環境とネットワークの設定」）。

2 つの機能は同じ設定で入り切りする。設定の名前は、新しい画面では Create and edit files である。ファイルを作る機能と、コードを動かす機能は、別々に選べない。

機能の属性は、次の表のとおり。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 入った版 |
| --- | --- |
| [ファイルの作成と編集（create and edit files）](files-and-code-execution.md) | 2025-09-09 |
| [コードの実行（code execution。アプリ）](files-and-code-execution.md) | 2024-10-24 |

すべて共通：面 アプリ、成熟度 GA、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

## 頼み方 {#usage}

頼み方の基本は、中身・確かめ方・止まる条件を、依頼に書くことである。「集計して xlsx にして」だけだと、何を確かめて終えたのかが返答に出ない。

**Before**

```text
添付の CSV を集計して、xlsx にして。
```

**After**

<!-- gen:begin snippet files-and-code-execution/request-spreadsheet -->
<!-- textlint-disable -->

??? example "雛形：中身・確かめ方・止まる条件を足した、集計ファイルの依頼"

    ```markdown
    添付の `sales_2026q3.csv`（UTF-8、1 行目が見出し）から、月別・店舗別の売上集計を `.xlsx` で作ってほしい。

    - 中身：シート 1 に月別の合計、シート 2 に店舗別の合計、シート 3 に元データ。合計の列は、値ではなく Excel の式にする。
    - 作る前に：行数、列名、欠けた値の数を数えて先に報告する。欠けた値は、捨てずに数だけ報告する。
    - 終わりの条件：シート 1 とシート 2 の総合計が、元データの売上の合計と一致すること。一致を確かめた計算を、最後の報告に書く。
    - 止まって報告する条件：列名が想定と違う、または日付を読めない行があるとき。直さずに、その行の番号を挙げて止まる。
    - 最後の報告：作ったファイル名、各シートの内容を 1 行ずつ、確かめた合計の数字。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet files-and-code-execution/request-spreadsheet -->

After で足したのは、シートごとの中身、作る前の件数の報告、合計を突き合わせる確かめ、止まる条件の 4 つである。合計の列を式にする指定も入れた。値でなく式なら、元の数字を直したときに追従する。

文字コードが Shift_JIS の CSV は、文字化けや空欄の元になる。UTF-8 に変えて渡す手順は、別のページにある（<!-- link:begin character-encodings#convert -->[文字コード（Shift\_JIS の CSV など） › UTF-8 に変えてから渡す](../japanese/character-encodings.md#convert)<!-- link:end -->）。大きな PDF や図を含む資料の読まれ方は、添付ファイルのページで確かめる（<!-- link:begin how-attachments-are-read#splitting -->[添付ファイルはどこまで読まれるか › 大きな資料の分け方](how-attachments-are-read.md#splitting)<!-- link:end -->）。

事務作業の中でこの機能を使うときは、人が材料を渡し、Claude が下書きし、人が確かめて出す流れにする（<!-- link:begin office-paperwork#human-ai-human -->[事務作業の半自動化（経費・報告） › 人 → AI → 人の流れにする](../recipes/office-paperwork.md#human-ai-human)<!-- link:end -->）。

## 実行環境とネットワークの設定 {#network}

実行環境とネットワークの設定は、データが外へ出る道を決める設定である。コードは隔離された環境で動く。環境から外への通信（egress）を許すかどうかを、設定で選ぶ。

選べる状態は、おおむね次の 4 つである。

- **オフ**：入っているパッケージだけを使う。インターネットには出ない。
- **パッケージ管理のみ**：npm・PyPI・GitHub など、パッケージの取得先にだけ出る。
- **パッケージ管理に加えて、足したドメイン**：許すドメインを自分で並べる。
- **すべてのドメイン**：公式がいちばん危険だと書いている選び方である。

既定はプランで違い、組織向けのプランでは管理者（owner）が決める。プランごとの既定は次のとおりである。設定の画面の名前は、版によって変わる。

<!-- gen:begin fact-table code-execution-network-egress-defaults -->
<!-- textlint-disable -->

| プラン | 既定 |
| --- | --- |
| 個人向け（Free・Pro・Max・Ultra） | オン |
| Team | パッケージ管理のみ |
| Enterprise（新しい組織） | オフ |

確認日 2026-11-05。出典：[Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)。

<!-- textlint-enable -->
<!-- gen:end fact-table code-execution-network-egress-defaults -->

### なぜ設定が要るか

公式が挙げる危険は、外部のファイルや Web ページに仕込まれた指示（プロンプトインジェクション）である。信頼できないコードが動いたり、会話の中のデータが外へ送られたりする。

その手立てとして、公式は通信を切ることを挙げている。通信を切れば、データは環境の外に出ない。

仕込まれた指示の経路と、防ぎ方の考え方は、安全のページに書いた（<!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](../safety/prompt-injection-in-practice.md#what-works)<!-- link:end -->）。防ぎ方の中心は、モデルの賢さに頼らず、持たせる権限と通信を絞ることである。ネットワークの設定は、その権限の側にある。

### 設定で止まらないもの

MCP の連携は、ネットワークの設定にかかわらず、外と通信できる。設定をオフにしても、MCP を有効にしていれば、データの出口は残る。社外に出したくないデータを扱うときは、設定と、有効にしている連携の両方を見る。

また、依頼の文に「外へ送らないで」と書いても、通信は止まらない。依頼の文はお願いで、設定が鍵である。依頼の文は、設定を補うものとして使う。下の雛形のように、外へ出さない条件も依頼に書いておく。

!!! example "判断例：顧客のデータを集計させる"
    - **状況**：解約した顧客の一覧（CSV）を、属性ごとに集計して図にしたい。社外には出せないデータである。
    - **迷う候補**：ネットワークをすべて許し、足りない分析のパッケージを自由に取らせる／ネットワークを絞り、入っているパッケージで集計する。
    - **選んだもの**：ネットワークを絞る。先に、このデータをこの面に渡してよいかを確かめる。
    - **理由**：集計に必要なのは、標準のパッケージで足りることが多い。通信を許す利点が小さく、外へ送られる危険が大きいからである。そもそも渡してよいかは、データの持ち主との取り決めで決まる（<!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end -->）。

次の雛形は、外へ出さない条件・再実行できる形・裏取りを、依頼に足したものである。

<!-- gen:begin snippet files-and-code-execution/request-private-analysis -->
<!-- textlint-disable -->

??? example "雛形：外へ出さない条件と、再実行・裏取りを足した分析の依頼"

    ```markdown
    添付の `customers.csv` を集計して、解約の多い属性を調べたい。社外に出せないデータなので、次を守ってほしい。

    - 外へ出さない：インターネットや外部のサービスに、データの一部も送らない。足りないパッケージがあれば、入れずに止まって知らせる。
    - 再実行できる形：集計に使った Python のスクリプトを、最後の報告にそのまま貼る。私が同じスクリプトで同じ数字を出し直せるようにする。
    - 裏を取る：結果の表のうち 3 行を選び、元データの該当の行を数え直して、数字が合うことを報告する。
    - 分けて書く：観察した事実（数字）と、原因の解釈（推測）を別の見出しにする。
    - ファイル：結果の表は `.xlsx`、図は PNG で出す。ファイル名を最後に列挙する。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet files-and-code-execution/request-private-analysis -->

集計を再実行できる形にする考え方と、観察と解釈を分ける考え方は、データの分析のページにある（<!-- link:begin data-analysis#reproducible-queries -->[データを分析する › 再実行できる形で集計させる](../recipes/data-analysis.md#reproducible-queries)<!-- link:end -->・<!-- link:begin data-analysis#observation-vs-interpretation -->[データを分析する › 観察と解釈を分ける](../recipes/data-analysis.md#observation-vs-interpretation)<!-- link:end -->）。

## 作ったファイルの受け取り方 {#outputs}

作ったファイルは、会話の中でダウンロードするか、Google Drive に保存して受け取る。モバイルでは、ダウンロードを押すと、システムのプレビューか別のアプリで開く。アップロードとダウンロードの両方に、大きさの上限がある。<!-- fact:begin file-creation-size-limit -->1 ファイル 30MB まで（超える PDF は、会話に載せず実行環境の中で処理できる）（2026-11-05 時点）<!-- fact:end -->。

受け取ったあとに確かめることを、3 つに絞る。

- **開いて見る**：Excel の式、シートの名前、スライドの体裁は、実際に開いて見る。返答の説明ではなく、ファイルが正本である。
- **数字を突き合わせる**：依頼に書いた確かめ（合計の一致など）の報告と、ファイルの中身を、数か所だけ見比べる。
- **渡す前に見る**：渡す相手に見せない列や注記が、ファイルに残っていないかを見る。

作ったファイルを含む会話の公開リンクでの共有は、<!-- fact:begin shared-chat-with-created-files-restriction -->Free・Pro・Max・Ultra では公開共有できない（Team・Enterprise は公式の文書に記述なし）（2026-11-05 時点）<!-- fact:end -->。会話の共有の扱いと、共有した中身の見え方は、共有のページにある（<!-- link:begin shared-artifacts-and-files#how-to-share -->[共有リンクと公開アーティファクトの扱い › 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有）](../safety/shared-artifacts-and-files.md#how-to-share)<!-- link:end -->）。

## 効かない場面・落とし穴 {#pitfalls}

効かない場面と落とし穴は、次のとおり。

- **ファイルの正しさを Claude の自己申告に任せる**：「合っています」の一言は確認にならない。突き合わせた計算を報告に出させ、数か所は自分で確かめる。
- **有効にしていない**：ファイル作成とコード実行の設定が無効だと、ファイルを作れず、コードも動かない。文章で表やスクリプトが返るだけで、動作の確認は取れない。組織の owner が切っている場合は、自分では入れられない。
- **ほかの機能が、同じ設定に依存する**：スキル・アーティファクト・長い会話の自動のコンテキスト管理は、ファイル作成とコード実行の設定を有効にしておく必要がある。設定を切ると、これらにも影響する。
- **隔離されているが、無害ではない**：隔離された環境でも、通信を許せば、会話の中のデータは外へ出うる。読ませた資料に仕込まれた指示で、コードが動くこともある。動いている間は、見ていて、予想外のデータに触れたら止める。
- **API の code execution tool とは別物**：この機能はアプリの機能である。API のコード実行の道具は、別の機能として追う。
- **作ったものを勝手に正本にする**：会話の中で作ったファイルは、元データを置き換えない。元データは別に残す。

## 比べる相手 {#compare}

比べる相手は、アーティファクトである。会話の中で文書・スライド・デザインを作り、直し、共有する機能である。詳しくは次のページにある（<!-- link:begin artifacts-overview -->[アーティファクト（会話の中で作る文書・スライド・デザイン）](artifacts-overview.md)<!-- link:end -->）。

- **会話の横で見ながら直したい、共有したい**：アーティファクト。テンプレートの選び方は <!-- link:begin artifacts-overview#templates -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › テンプレートの選び方](artifacts-overview.md#templates)<!-- link:end --> にある。
- **`.xlsx`・`.pptx`・`.docx`・PDF のファイルとして持ち帰りたい、コードで集計させたい**：この機能。

2 つは排他ではない。集計はこの機能でさせて、結果の見せ方をアーティファクトで整える、という分け方もできる。

古くなった助言の台帳に、この機能に関わる行はない。ネットワークの既定と画面の名前は変わりやすいので、古い記事の説明は、公式の文書の日付で確かめる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [データを分析する](../recipes/data-analysis.md)

**関連**

- [アーティファクト（会話の中で作る文書・スライド・デザイン）](artifacts-overview.md)
- [事務作業の半自動化（経費・報告）](../recipes/office-paperwork.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [文字コード（Shift\_JIS の CSV など）](../japanese/character-encodings.md)
- [添付ファイルはどこまで読まれるか](how-attachments-are-read.md)
- [共有リンクと公開アーティファクトの扱い](../safety/shared-artifacts-and-files.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Release Notes: Claude Apps](https://web.archive.org/web/20250628195643/https://docs.anthropic.com/en/release-notes/claude-apps)：Anthropic（写し）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
