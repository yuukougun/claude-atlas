---
id: office-paperwork
title: 事務作業の半自動化（経費・報告）
nav_title: 事務作業の半自動化
aliases: [経費の一覧づくり, 週報を書かせる, 報告書の下書き, 雑務の自動化, 雑務をまとめたリポジトリ]
type: recipe
field: recipes
chapter: 事務とノート
order: 190
level: 任せる
priority: 推奨
surfaces: [app, claude-code]
principle: [握る, 見せる]
prevents: [境界がない, 確かめていない]
scenes: [文章]
summary: 経費の整理や週次の報告など繰り返す事務作業を、人が材料を渡し、Claude が下書きし、人が確かめて出す流れで半自動にする。手順はファイルやスキルに育て、私的な情報は渡す範囲を先に決める。
signs:
  - {type: goal, text: 毎週の報告書づくりを楽にしたい}
  - {type: goal, text: 領収書や明細から経費の一覧を作らせたい}
  - {type: situation, text: コードを書かない仕事に Claude Code を使いたい}
prerequisites: [entrusted-data, default-safety-settings]
related: [where-your-data-goes, notes-and-pkm, data-analysis, permission-modes-overview, writing-skills, how-skills-load, progress-files, tasks-and-schedules-in-the-app, connectors-in-the-app, peripheral-products#office-add-ins, character-encodings, protecting-secrets, what-to-put-in-claude-md]
tracks: [skills, app-skills]
sources: [cc-docs-skills, hc-skills-what, hc-skills-use]
volatility: 中
sections:
  - {title: 作業用のフォルダと権限の設定で始める, anchor: work-folder}
  - {title: 私的な情報を渡す範囲, anchor: private-data}
  - {title: 人 → AI → 人の流れにする, anchor: human-ai-human}
  - {title: 手順をファイルとスキルに育てる, anchor: grow-procedures, level: 仕組みにする}
  - {title: 雑務をまとめたリポジトリ, anchor: chores-repo, level: 仕組みにする}
  - {title: 全体の確かめ方, anchor: check}
  - {title: うまくいかないとき, anchor: troubleshoot}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：繰り返す事務作業を、人が材料を渡し、Claude が下書きし、人が確かめて出す流れで半自動にできる。
    - **いつ引くか**：毎週の報告書づくりを楽にしたいとき。領収書や明細から経費の一覧を作らせたいとき。コードを書かない仕事に Claude Code を使いたいとき。
    - **前提**：<!-- link:begin entrusted-data -->[預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)<!-- link:end -->、<!-- link:begin default-safety-settings -->[安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)<!-- link:end -->

<!-- textlint-disable -->
別名：経費の一覧づくり・週報を書かせる・報告書の下書き・雑務の自動化・雑務をまとめたリポジトリ
<!-- textlint-enable -->

事務作業の半自動化は、経費の整理や週次の報告のような繰り返す作業を、Claude に下書きまでさせて、出すところは人が持つ形にすることである。任せるのは真ん中の 1 段だけにする。渡す材料の範囲と、出す前の確かめを人が握ることで、手間は減らし、誤りが外に出る道は残さない。

## 作業用のフォルダと権限の設定で始める {#work-folder}

作業用のフォルダを 1 つ作り、事務作業はそのフォルダの中だけで動かす。フォルダが、Claude が触れる範囲の境界になる。材料は `inbox/` に原本のコピーとして置き、成果物は `out/` に書かせる。原本は触らせない。手順の説明は、フォルダの `README.md` に書く。

権限は、確認が出る既定のまま始め、最初の数回は 1 つずつ承認して、何を読み何を書くかを見る。確認なしで進める範囲を広げるのは、手順が固まり、出力を毎回確かめる流れができてからである。どのモードにどの設定を足すかは、このページでは決めず、<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> の段階に従う。モードごとに何が確認なしで進むかは <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end -->、既定は版で変わってきたので <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](../cli/permission-modes-overview.md#defaults)<!-- link:end --> で手元の既定を確かめる。

面ごとに、境界の作り方が違う。

=== "アプリ"

    アプリには作業用のフォルダがない。境界になるのは、会話に添付したファイルと、つないだコネクタが読める範囲である。添付は作業に要るものだけにし、コネクタは使うものだけをつなぐ。コネクタの種類と、信頼してよいかの判断は <!-- link:begin connectors-in-the-app#types -->[コネクタ（MCP）をアプリで使う › コネクタの種類](../app/connectors-in-the-app.md#types)<!-- link:end --> と <!-- link:begin connectors-in-the-app#trust -->[コネクタ（MCP）をアプリで使う › 信頼してよいか](../app/connectors-in-the-app.md#trust)<!-- link:end --> にある。

    調べてファイルに仕上げるような多段の作業は、結果で頼むと進められる。定期にもできるが、何を定期にしないかを先に決める。手順は <!-- link:begin tasks-and-schedules-in-the-app#ask-for-results -->[タスクと定期タスク（Cowork） › 結果で頼む](../app/tasks-and-schedules-in-the-app.md#ask-for-results)<!-- link:end --> を引く。Excel や Word の中で使いたいときは、アプリの外の製品の位置づけを <!-- link:begin peripheral-products#office-add-ins -->周辺製品の一覧<!-- link:end --> で確かめる。

=== "Claude Code"

    作業用のフォルダを作り、そのフォルダで Claude Code を起動する。起動したフォルダが作業の範囲の起点になる。コードを書かない仕事でも、材料をファイルで渡し、成果物をファイルで受け取る流れは同じである。ほかの OS と IDE 拡張の動作は、このページでは未確認とする。

    経費の一覧づくりなら、フォルダは次の形から始められる。`inbox/` の下に領収書と明細のコピー、`out/` に一覧、`categories.md` に区分表、`README.md` に手順を置く。

<!-- gen:begin snippet office-paperwork/expense-list-request -->
<!-- textlint-disable -->

??? example "雛形：経費の一覧を作らせる依頼"

    ```markdown
    `expenses/inbox/receipts/` の領収書（画像と PDF）と `expenses/inbox/statement.csv`（カードの明細）から、今月の経費の一覧を作ってほしい。

    - `expenses/out/expenses-YYYY-MM.csv` に、日付・店名・金額・区分・領収書のファイル名・明細との照合（一致・明細なし・領収書なし）の列で出す。
    - 区分は `expenses/categories.md` の区分表から選ぶ。当てはまらないものは「要確認」にする。
    - 読み取りに自信がない値は、推測で埋めずに空にして、備考に理由を書く。
    - 合計は暗算せず、スクリプト（`expenses/out/sum_check.py`）で計算し、明細の合計と並べて報告する。
    - 氏名と口座の情報は、`inbox/` に置く前に伏せてある。伏せた箇所を推測で復元しない。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet office-paperwork/expense-list-request -->

銀行やカードの明細の CSV は、Shift_JIS で保存されていることがある。渡す前に <!-- link:begin character-encodings#check -->[文字コード（Shift\_JIS の CSV など） › 渡す前に文字コードを確かめる](../japanese/character-encodings.md#check)<!-- link:end --> で文字コードを確かめる。確かめずに渡すと、文字化けや集計の空欄になる。

## 私的な情報を渡す範囲 {#private-data}

私的な情報は、渡す範囲を先に決めてから、渡す。決めずに始めると、「作業に要るから」と材料を足していくうちに、範囲が広がる。範囲の線は、`inbox/` に置いたものと、会話に貼ったものである。この 2 つに入れたものだけが渡したものになる。

材料は、渡し方を 3 つに分ける。

| 材料の種類 | 例 | 扱い |
| --- | --- | --- |
| 自分の仕事の資料 | 自分の議事メモ、自分の作業の一覧 | 渡してよい。ただし使う面の保持の扱いを先に確かめる |
| 個人名や金額を含む資料 | 領収書の宛名、同席者の名前、口座・カード番号 | 作業に要る列と行だけにする。要らない氏名と番号は伏せたコピーを渡す |
| 預かったデータ、規約付きのデータ、秘密 | 顧客のデータ、NDA の付いた資料、API キー | 契約で扱いが決まっている面だけで使う。秘密は作業用のフォルダに置かない |

預かったデータを渡してよい面の判断は <!-- link:begin entrusted-data#whose-data -->[預かったデータ・規約付きのデータを AI に渡してよいか › 誰のデータで、何が決まっているか](../safety/entrusted-data.md#whose-data)<!-- link:end --> と <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end --> にある。ここでは繰り返さない。送ったデータが学習に使われる条件と残る期間は、個人のプランと商用のプランで違う。<!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](../safety/where-your-data-goes.md#consumer-vs-commercial)<!-- link:end --> で、使う側のプランを確かめる。渡した内容は、手元にも記録として残る。残り方は <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](../safety/where-your-data-goes.md#local-transcripts)<!-- link:end --> にある。

秘密情報は、作業用のフォルダにも会話にも置かない。置かない設定の作り方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> を引く。

!!! example "判断例：会食の領収書を、そのまま渡すか、伏せて渡すか"
    - **状況**：取引先との会食の領収書の写真に、取引先の会社名と同席者の氏名が写っている。経費の一覧に入れたい。
    - **迷う候補**：写真をそのまま渡す。氏名を伏せたコピーを渡し、同席者の欄は自分で足す。
    - **選んだもの**：氏名を伏せたコピーを渡す。
    - **理由**：一覧づくりに要るのは日付・店名・金額・区分で、氏名は要らない。伏せた氏名を足す手間は小さい。ただし、同席者の記載が精算の要件で、数が多いときは、伏せずに渡す選択も筋が通る。その場合は、先に使う面の保持の扱いを確かめる。

## 人 → AI → 人の流れにする {#human-ai-human}

事務作業を任せる流れは、人 → AI → 人の 3 段にする。人が材料を渡し、Claude が下書きを作り、人が確かめて出す。人の段を「確かめる」と「出す」に分けると、手順は 4 つになる。最初と最後を人が持つのは、事務作業の誤りが、もっともらしい文や整った表の形で出てくるからである。読んだだけでは気づきにくい。確かめていない下書きが外へ出ると、取り消しにくい。

先に整える守りは、前の 2 つの節にある。渡す範囲は「作業用のフォルダと権限の設定で始める」と「私的な情報を渡す範囲」で決める。この節では、守りを決めた後に回す手順を書く。

1. **材料を渡す（人）**：何を渡すかを決め、作業用のフォルダに置く。終わりの確かめ：渡すものだけが入り、渡さないものが入っていない。
2. **下書きを作らせる（Claude）**：出力の形（見出し・列・置き場所）を先に指定する。終わりの確かめ：指定の形のファイルができ、材料にない項目は「材料なし」と書かれている。
3. **確かめる（人）**：数字と日付と名前を、材料の原本と突き合わせて直す。終わりの確かめ：下書きの各項目を、元の材料までたどれた。
4. **出す（人）**：送信・提出・登録は人の手で行う。終わりの確かめ：出した記録が人の側に残っている。

下書きを「見せる」形にするのが、3 段目を成り立たせる鍵である。各項目に元の材料の名前を付けさせ、材料にないことは書かせない。こうすると、確かめる人は全文を読み直さず、項目ごとに元を開いて突き合わせられる。

<!-- gen:begin snippet office-paperwork/weekly-report-request -->
<!-- textlint-disable -->

??? example "雛形：週報の下書きを頼む依頼"

    ```markdown
    今週の週報の下書きを作ってほしい。

    材料：`weekly-report/inbox/` の中のファイルだけを読む（議事メモ、チケットの一覧、先週の週報）。
    形：`weekly-report/out/weekly-YYYY-MM-DD.md` に、「進んだこと」「止まっていること」「来週やること」の 3 見出しで書く。

    決まり：
    - 各項目の末尾に、元にした材料のファイル名を付ける。
    - 材料に書かれていないことは書かず、「材料なし」と書く。
    - 件数や日数は材料から数え直し、材料に書かれた値と食い違うときは両方を書く。
    - 送信や投稿はしない。下書きのファイルだけを作る。

    終わったら、「材料なし」にした項目と、判断に迷った項目を最後に列挙する。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet office-paperwork/weekly-report-request -->

経費の一覧づくりも、この人 → AI → 人の流れで回す。違いは、数字が主役になることである。合計は Claude の暗算にせず、スクリプトで出させて、明細の合計と並べて報告させる。集計の頼み方は <!-- link:begin data-analysis#reproducible-queries -->[データを分析する › 再実行できる形で集計させる](data-analysis.md#reproducible-queries)<!-- link:end --> に、生データでの裏取りは <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](data-analysis.md#check-raw-data)<!-- link:end --> にある。

!!! example "判断例：週報を、そのまま送らせるか、下書きで止めるか"
    - **状況**：毎週の報告を、決まった宛先へメールで送っている。材料は議事メモとチケットの一覧で、Claude が文章にまとめるところまでは安定してきた。
    - **迷う候補**：下書きができたら、そのまま送信まで任せる。下書きのファイルかメールの下書きで止め、送るのは自分の手にする。
    - **選んだもの**：下書きで止め、送るのは自分の手にする。
    - **理由**：送信は取り消しにくく、宛先が社外にも及ぶ。下書きを確かめる手間は小さいが、誤りが出てからの後始末は大きい。定期に回す場合も、送信までは含めない。線引きは <!-- link:begin tasks-and-schedules-in-the-app#what-not-to-schedule -->[タスクと定期タスク（Cowork） › 定期タスクにしないもの](../app/tasks-and-schedules-in-the-app.md#what-not-to-schedule)<!-- link:end --> にある。

## 手順をファイルとスキルに育てる {#grow-procedures}

手順は、最初から作り込まず、3 段で育てる。会話で頼み、うまくいったらファイルに書き、安定したらスキルにする。繰り返す回数が少ないうちに作り込むと、形が変わるたびに作り直すことになる。

1. **会話で頼む**：依頼の本文に、材料・出力の形・決まりを書く。直した指示は、その場で依頼に足す。
2. **手順ファイルに書く**：同じ依頼を数回出したら、業務ごとの `README.md` に、目的・入力・出力の形・手順・注意を書く。以後の依頼は「README の手順で今週分を」だけで済む。
3. **スキルにする**：頼む回数が増え、手順が安定したら、スキルにする。スキルは呼べば手順の本文が読み込まれ、呼ばない間は名前と説明だけが入る。仕組みは <!-- link:begin how-skills-load#what-happens -->[スキルの考え方（手順を必要なときだけ読む） › 何が起きるか](../extend/how-skills-load.md#what-happens)<!-- link:end --> に、作り方は <!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](../extend/writing-skills.md#minimal)<!-- link:end --> にある。

誤りが出た回の直しは、その場で終わらせず、手順の「注意」に 1 行足す。たとえば、区分を間違えた理由と正しい区分の基準を書く。理由を添えると、次の回に似た場面で外さない。書く行と外す行の見分け方は <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> にある。

手順ファイルとスキルは、読ませる指示であって、守らせる鍵ではない。「送信しない」「`inbox/` の外は読まない」のような、破られると困る線は、手順に書くだけで済ませない。権限の設定で縛る。設定の足し方は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> の段階に従う。

<!-- gen:begin snippet office-paperwork/weekly-report-skill -->
<!-- textlint-disable -->

??? example "雛形：週報の手順をスキルにしたもの"

    ```markdown
    ---
    name: weekly-report
    description: 今週の週報の下書きを weekly-report/inbox/ の材料から作る。「週報」「週次の報告」と頼まれたときに使う。
    disable-model-invocation: true
    ---

    # 週報の下書き

    1. `weekly-report/README.md` を読み、出力の形と注意を確かめる。
    2. `weekly-report/inbox/` の中のファイルだけを材料にする。ほかの場所は読まない。
    3. `weekly-report/out/` に、「進んだこと」「止まっていること」「来週やること」の 3 見出しで下書きを書く。
    4. 各項目の末尾に、元にした材料のファイル名を付ける。材料にないことは「材料なし」と書く。
    5. 送信や投稿はしない。最後に、「材料なし」にした項目と判断に迷った項目を列挙して終える。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet office-paperwork/weekly-report-skill -->

週報のスキルの雛形は、自動では呼ばれないように `disable-model-invocation: true` を付けてある。送信前の確かめを挟む事務の手順は、自分が呼んだときだけ動くほうが扱いやすい。スキルを入れすぎたときに残るコストは <!-- link:begin how-skills-load#residual-cost -->[スキルの考え方（手順を必要なときだけ読む） › 入れすぎたときに残るコスト](../extend/how-skills-load.md#residual-cost)<!-- link:end --> にある。スキルを使えるのは、Claude Code とアプリである。アプリ側の設定は面ごとに違うので、使う前に公式の文書で確かめる。

!!! example "判断例：週報の手順を、スキルにするか、手順ファイルのままにするか"
    - **状況**：週報の手順を 3 回ほど `README.md` の指示で回した。形は固まってきたが、材料の置き場所は毎回少し違う。
    - **迷う候補**：スキルにして `/weekly-report` で呼べるようにする。`README.md` のまま、「README の手順で」と頼み続ける。
    - **選んだもの**：`README.md` のまま続ける。
    - **理由**：材料の置き場所が変わるうちは、スキルの本文を直し続けることになる。置き場所が固まり、直す箇所が減ってから、スキルにする。毎週回す業務なら、早めにスキルにする選択も筋が通る。

## 雑務をまとめたリポジトリ {#chores-repo}

業務が増えたら、業務ごとにディレクトリを分けて、1 つのリポジトリにまとめる。各ディレクトリに `README.md` を置き、その業務の手順と注意を書く。これで、業務ごとに文脈が蓄積し、新しいセッションでも、そのディレクトリの README を読ませれば続きから始められる。

<!-- gen:begin snippet office-paperwork/chores-repo-layout -->
<!-- textlint-disable -->

??? example "雛形：雑務のリポジトリの構成例"

    ```text
    chores/
    ├── CLAUDE.md             # 短く。全業務に共通の守りだけ（私的な情報の扱い、確認なしで進めないこと）
    ├── .gitignore            # **/inbox/ と **/out/ を追跡から外す
    ├── .claude/
    │   └── skills/
    │       └── weekly-report/
    │           └── SKILL.md  # 週報の手順をスキルにしたもの
    ├── weekly-report/
    │   ├── README.md         # 目的・入力・出力の形・手順・注意・前回までに決めたこと
    │   ├── inbox/            # 今週の材料のコピー（追跡しない）
    │   └── out/              # 下書き（追跡しない）
    └── expenses/
        ├── README.md         # 同じ項目。区分表への案内を含む
        ├── categories.md     # 経費の区分表
        ├── inbox/            # 領収書と明細のコピー。伏せた後のもの（追跡しない）
        └── out/              # 一覧と合計の確認（追跡しない）
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet office-paperwork/chores-repo-layout -->

リポジトリに入れるのは、手順と区分表のような、再利用する文書だけである。材料と成果物には私的な情報が入るので、追跡から外す。リポジトリを共有する場合も、渡す範囲の線は崩れない。誤って材料を入れても困らないように、`.gitignore` と作業の場所で二重にしておく。

ルートの `CLAUDE.md` は短くし、全業務に共通の守りだけを書く。業務ごとの手順は、その業務の README に置く。頼むときに、その README を指す。こうすると、関係のない業務の手順を毎回読ませずに済む。残す行と外す行の判断は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> にある。

前回までに決めたことと、まだ人に聞くことは、README の末尾か別ファイルに分けて残す。ファイルの分け方と、決めたことを壊されにくくする方法は <!-- link:begin progress-files#files -->[進捗ファイルで、途中から再開できるようにする › ファイルの分け方](../context/progress-files.md#files)<!-- link:end --> と <!-- link:begin progress-files#decided-vs-open -->[進捗ファイルで、途中から再開できるようにする › 決めたことと、聞くべきことを分ける](../context/progress-files.md#decided-vs-open)<!-- link:end --> にある。Obsidian などのノートの保管庫で同じ運用をする場合は <!-- link:begin notes-and-pkm -->ノート・PKM（Obsidian など）<!-- link:end --> を引く。

業務を横断して一度に頼むのは、慎重にする。業務ごとに守りの線が違うので、横断の依頼は、渡す範囲を超えやすい。1 つの業務のディレクトリで起動して頼む形を基本にする。

## 全体の確かめ方 {#check}

出す前に、次の 4 つを確かめる。

- **数字**：合計と件数を、スクリプトで再計算させ、原本の合計と一致させる。方法は <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](data-analysis.md#check-raw-data)<!-- link:end --> にある。
- **事実**：日付・金額・名前を、下書きの各項目から元の材料までたどって突き合わせる。「材料なし」の項目は、人が埋めるか、外す。
- **変更の範囲**：`out/` の外のファイルが変わっていないかを、フォルダを git で管理しているなら `git status` で見る。原本は `inbox/` にあるコピーだけを渡しているので、原本は変わらない。
- **渡した範囲**：何を読んだかを、手元の記録で確かめる。意図しないファイルを読んでいたら、フォルダの置き方か権限の設定を直す。記録の場所は <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](../safety/where-your-data-goes.md#local-transcripts)<!-- link:end --> にある。

新しい手順は、本物の材料の前に、偽の材料で試す。偽の領収書と偽の明細で回せば、私的な情報を渡さずに、出力の形と「材料なし」の動きを確かめられる。

## うまくいかないとき {#troubleshoot}

- **集計が合わない、空欄が出る**：文字コードを疑う。<!-- link:begin character-encodings#convert -->[文字コード（Shift\_JIS の CSV など） › UTF-8 に変えてから渡す](../japanese/character-encodings.md#convert)<!-- link:end --> で UTF-8 に変えてから渡す。それでも合わないときは、スクリプトの出力と原本の合計を並べて、食い違う行を絞る。
- **渡すつもりのないものを渡した**：会話に貼った内容は、手元の記録に残る。対処は <!-- link:begin protecting-secrets#when-it-fails -->[秘密情報（.env・API キー）を守る › 効かなかったとき](../safety/protecting-secrets.md#when-it-fails)<!-- link:end --> と <!-- link:begin where-your-data-goes#retention -->[送ったデータの行方（学習・保持期間） › 残る期間](../safety/where-your-data-goes.md#retention)<!-- link:end --> を引く。
- **手順を無視される**：手順は読ませる指示であり、破られうる。破られると困る線は権限の設定で縛る。足し方は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> にある。
- **定期に回したら、確認なしで先まで進んだ**：定期にする作業を見直す。送信や提出のような、取り消しにくい操作は含めない。線引きは <!-- link:begin tasks-and-schedules-in-the-app#what-not-to-schedule -->[タスクと定期タスク（Cowork） › 定期タスクにしないもの](../app/tasks-and-schedules-in-the-app.md#what-not-to-schedule)<!-- link:end --> にある。
- **ほかの症状**：症状から引くときは <!-- link:begin field:symptoms -->[症状辞典](../symptoms/index.md)<!-- link:end --> から探す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)

**関連**

- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [データを分析する](data-analysis.md)
- [権限モードの選び方](../cli/permission-modes-overview.md)
- [スキルの作り方](../extend/writing-skills.md)
- [スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)
- [進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)
- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [コネクタ（MCP）をアプリで使う](../app/connectors-in-the-app.md)
- [文字コード（Shift\_JIS の CSV など）](../japanese/character-encodings.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
