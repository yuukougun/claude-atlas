---
id: claude-md-vs-rules-skills-styles
title: CLAUDE.md・rules・スキル・出力スタイルの違い
aliases: [指示の置き場所, output style と CLAUDE.md の違い, rules と CLAUDE.md の違い]
type: comparison
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 90
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 常に効かせる規則・フォルダごとの規約・場面ごとの手順・応答の形を、どこに置くかを選べる。常駐か条件付きか、知識か応答の形かで分け、例外を許さないものは鍵に移す。
signs:
  - {type: goal, text: 常に守らせたい規則と、ときどき使う手順の置き場所を分けたい}
  - {type: goal, text: 応答の口調や形式を変えたいが、どこに書けばよいか分からない}
prerequisites: [path-scoped-rules, how-skills-load]
related: [output-style-modes#vs-claude-md, what-to-put-in-claude-md, where-to-put-instructions, extensions-at-a-glance, request-lock-table, using-auto-memory, hook-vs-skill, when-to-add-what, keep-replies-in-japanese, what-subagents-dont-inherit, skills-in-the-app#migrated-styles, hooks-basics, cloud-sessions-and-teleport]
tracks: [claude-md, rules, skills, output-styles]
sources: [cc-docs-memory, cc-docs-features-overview, cc-docs-context-window, cc-docs-skills, cc-docs-output-styles, cc-docs-sub-agents, cc-docs-settings, cc-docs-cloud-environments, claude-blog-steering-code-skills-hooks, hc-styles-to-skills, cc-docs-permissions, cc-docs-debug-your-config]
sections:
  - {title: 比較の表, anchor: table}
  - {title: 指示の置き場所の選び方, anchor: how-to-choose}
  - {title: 置き場所の組み合わせ方, anchor: combine}
  - {title: 指示が読み込まれたかの確かめ方, anchor: verify}
  - {title: 指示が届く範囲の違い, anchor: reach}
  - {title: 混同されやすい別の機能, anchor: similar-names}
volatility: 中
stage: draft
updated: 2026-11-04
---

!!! abstract "要点"
    - **何ができるか**：Claude Code で常に効かせる規則は CLAUDE.md、フォルダやファイルごとの規約は rules、ときどき使う手順はスキル、応答の口調や形は出力スタイルに置き分けられる。4 つはどれも守られる保証のないお願いである。例外を許さない禁止は、鍵（Claude が従うかどうかに頼らず Claude Code が実行するフックや deny ルール）に移し、CLAUDE.md には止めている理由と、例外が要るときの相談の基準だけを書く。
    - **いつ引くか**：常に守らせたい規則とときどき使う手順の置き場所を分けたいとき。応答の口調や形式を変えたいが、どこに書けばよいか分からないとき。アプリ（claude.ai）の Styles を探しているときは、別の機能なので「混同されやすい別の機能」の節を見る。
    - **前提**：<!-- link:begin path-scoped-rules -->.claude/rules と paths で必要なときだけ読ませる（準備中）<!-- link:end -->、<!-- link:begin how-skills-load -->スキルの考え方（手順を必要なときだけ読む）（準備中）<!-- link:end -->

<!-- textlint-disable -->
別名：指示の置き場所・output style と CLAUDE.md の違い・rules と CLAUDE.md の違い
<!-- textlint-enable -->

CLAUDE.md・rules・スキル・出力スタイルの違いは、Claude Code で指示がいつ読み込まれ、何を変えるかにある。常に要らない指示を毎回読み込まれる場所に書くと、コンテキストが散らかる。例外を許さない指示を、従ってもらうだけのお願いで済ませると、縛っていないのと同じになる。

## 比較の表 {#table}

CLAUDE.md・rules・スキル・出力スタイルを、属性ごとに比べる表である。置き場所を選ぶときに見る列は、強制力・読み込みの時期・コンテキストのコスト・圧縮で残るかである。全機能で同じ値の列は、表から省いて表の下にまとめてある。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 読み込みの時期 | コンテキストのコスト | 圧縮で残るか |
| --- | --- | --- | --- |
| CLAUDE.md（準備中） | セッション開始 | 常駐 | 残る |
| rules（.claude/rules/）（準備中） | セッション開始か、一致するファイルを扱うとき | 常駐か、一致するファイルのときだけ | 条件による |
| スキル（skills）（準備中） | セッション開始と使うとき | 使うまで小さい | 残る |
| 出力スタイル（output styles）（準備中） | セッション開始と切り替えたとき | 常駐 | 残る |

すべて共通：強制力 お願い。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

表の値だけでは分からない点を補う。まず表の読み方である。rules の「圧縮で残るか」の「条件による」は、`paths` の有無で答えが違い、1 つの値で言い切れないという意味である。「残る」とある CLAUDE.md とスキルも、残るのは一部であり、その違いは読み込みと圧縮の扱いに書いた。

次に強制力である。どの機能も、Claude が従うかどうかに任せる指示（お願い）で、守られる保証はない。公式の文書は、CLAUDE.md を強制する設定ではなく文脈として扱うと述べ、出力スタイルについても何も強制しないと述べている。守らせる仕組みが要る指示は、鍵に移す。鍵とは、フックや deny ルールのように、Claude が従うかどうかに頼らず Claude Code が実行する制御である。

読み込みと圧縮の扱いは、機能ごとに次の違いがある。

- **CLAUDE.md**：作業ディレクトリから上の階層の分は、セッション開始に読み込まれる。サブフォルダの分は、Claude がそのフォルダのファイルを読み書きしたときに読み込まれる。圧縮では、プロジェクトの根の CLAUDE.md がディスクから入れ直される。サブフォルダの分は要約から消え、必要になると読み直される。
- **rules**：`paths` のない rules は CLAUDE.md と同じ扱いで、セッション開始に読み込まれ、圧縮の後もディスクから入れ直される。`paths` のある rules は、一致するファイルを扱うときだけ読み込まれる。圧縮では要約に消え、一致するファイルを再び扱うと読み直される。表の「条件による」は、この二通りで答えが違うことを指す。
- **スキル**：名前と説明がセッション開始から毎回入り、本文は呼ばれたときに入る。`disable-model-invocation: true`（Claude が自分では呼ばず、人が呼んだときだけ動く設定）を付けたスキルは、呼ぶまで説明も入らない。圧縮の後、呼んだスキルの本文は上限つきで入れ直され、古いものから外れる。
- **出力スタイル**：選ばなければ何も足さない。選んだスタイルの指示は、毎回のリクエストと一緒に送られ、圧縮の後も効き続ける。自作のスタイルは、`keep-coding-instructions: true` を付けないと、Claude Code 標準のソフトウェア開発の指示が外れる。コーディングの作業を続けさせるなら、付けておく。

## 指示の置き場所の選び方 {#how-to-choose}

CLAUDE.md・rules・スキル・出力スタイルのどこに指示を置くかは、3 つの軸で決まる。軸 A は、例外を許さないかどうかである。軸 B は、変えたいのが応答の形なのか、知識や手順なのかである。軸 C は、いつ読み込ませるか（毎回、触るファイルに応じて、使う作業に応じて）である。次の 5 つの問いを、この順に当てはめる。

1. **例外を許さないか（軸 A）**：許さないなら、鍵（フックや deny ルールなど、Claude Code が実行する制御）に移す。CLAUDE.md には、鍵で止めている理由と、例外が要るときに人へ相談する基準だけを書く。鍵の考え方は<!-- link:begin request-vs-lock -->お願いと鍵（決定論的か、非決定論的か）（準備中）<!-- link:end -->、手段の選び方は<!-- link:begin request-lock-table -->お願いと鍵の対応表（準備中）<!-- link:end -->を見る。
2. **変えたいのは応答の形か（軸 B）**：口調・説明の量・確認の仕方をセッション全体で変えたいなら、出力スタイルに置く。選ぶには、`/output-style` のコマンドか、`/config` のメニューを使う。まず組み込みのスタイルで足りるかを試す。足りないとき、たとえば文体を指定したいときや役割を大きく変えたいときに、自作する。組み込みの種類と選び方は<!-- link:begin output-style-modes -->出力スタイルで応答の仕方を切り替える（準備中）<!-- link:end -->を見る。日本語で返し続けさせる設定の組み合わせは<!-- link:begin keep-replies-in-japanese -->日本語で返し続けさせる（準備中）<!-- link:end -->を見る。
3. **毎回の作業に要る事実か（軸 C：毎回）**：コマンド・推測できない落とし穴・規則の理由は、プロジェクトの根の CLAUDE.md に置く。ただし長くするほど、コンテキストを使い、守られにくくなると公式の文書は述べている。残す行と外す行の見分け方は<!-- link:begin what-to-put-in-claude-md -->CLAUDE.md に書くこと・書かないこと（準備中）<!-- link:end -->、長さの目安と削り方は<!-- link:begin claude-md-length -->CLAUDE.md の長さと剪定（準備中）<!-- link:end -->を見る。
4. **一部のフォルダやファイルにだけ要るか（軸 C：触るファイルに応じて）**：`paths` を付けた rules に置く。規約が 1 つのフォルダに収まるなら、そのフォルダの CLAUDE.md でもよい。
5. **ときどき使う手順か（軸 C：使う作業に応じて）**：スキルに置く。説明だけが常駐し、本文は使うときに読まれる。

1〜5 で置く種類を決めたあと、自分だけの好みなら、置く階層をユーザーレベルに替える。同じ種類のファイル（`~/.claude/CLAUDE.md`・`~/.claude/rules/`・`~/.claude/skills/`・`~/.claude/output-styles/`）に置き、チームで共有するプロジェクトのファイルには書かない。

最初から全部を分ける必要はない。同じ注意を繰り返すようになってから仕組みに移すほうがよい。その目安は<!-- link:begin when-to-add-what -->拡張を足すタイミング（準備中）<!-- link:end -->を見る。サブエージェントやフック、MCP、プラグインまで含めた全体図は<!-- link:begin extensions-at-a-glance -->拡張機能の全体図と使い分け早見表（準備中）<!-- link:end -->にある。迷いやすい場面を、判断例で示す。

!!! example "判断例：.env を読ませない"
    - **状況**：`.env` の中身を Claude に読ませたくない。今は CLAUDE.md に「`.env` を読まない」と一行書いてある。
    - **迷う候補**：CLAUDE.md の文を強める。rules にする。deny ルールかフックで止める。
    - **選んだもの**：deny ルールかフックで止める。CLAUDE.md には、止めている理由と、値が要るときは人に頼むという基準を書く。
    - **理由**：CLAUDE.md は文脈であり、文を強めても守られる保証は増えない。rules も CLAUDE.md と同じお願いで、置き場所を替えても強さは変わらない。例外を許さない禁止は、Claude が従うかどうかに頼らない鍵で止める。理由を残しておくと、止められたときに何をすればよいかが Claude に伝わる。deny ルールとフックの選び方は<!-- link:begin request-lock-table -->お願いと鍵の対応表（準備中）<!-- link:end -->を見る。

!!! example "判断例：テストファイルだけの規約"
    - **状況**：`*.test.ts` の書き方に規約がある。テストはフォルダのあちこちにあり、根の CLAUDE.md に書くと、テストに触れない作業でも毎回読み込まれる。
    - **迷う候補**：根の CLAUDE.md に書く。フォルダごとに CLAUDE.md を置く。`paths` 付きの rules にする。
    - **選んだもの**：`paths` に `**/*.test.ts` を書いた rules にする。
    - **理由**：`paths` 付きの rules は、一致するファイルを扱うときだけ読み込まれるので、常駐を増やさない。フォルダごとの CLAUDE.md では、同じ内容を何か所にも置くことになる。

!!! example "判断例：月に一度のリリース手順"
    - **状況**：リリースの手順が長く、使うのは月に一度である。今は根の CLAUDE.md に全部書いてあり、毎回の作業で読み込まれている。
    - **迷う候補**：CLAUDE.md に残す。rules にする。スキルにする。
    - **選んだもの**：スキルにする。公開のように副作用のある手順なので、`disable-model-invocation: true` を付けて、人が呼んだときだけ動くようにする。
    - **理由**：rules の読み込み条件はファイルであり、作業ではない。スキルは説明だけが常駐し、本文は使うときに読まれる。手動で呼ぶ設定にすると、説明も呼ぶまで入らない。公式の文書も、特定の作業向けで常には要らない指示にはスキルを勧めている。ただし、この設定が止めるのは、Claude が自分でスキルを呼ぶことだけである。呼んだあとの手順の承認までは止めない。公開の承認を必ず挟みたいなら、`npm publish` を ask ルール（実行の前に人の確認を挟む鍵）で止める。手動のスキルの作り方は<!-- link:begin manual-only-skills -->副作用のあるスキルを勝手に動かさない（準備中）<!-- link:end -->を見る。

!!! example "判断例：毎回頼んでいる文体"
    - **状況**：毎回「である調で、結論から書いて」と頼んでいる。レビューの依頼のときだけは、指摘を重さの順に並べる形式も欲しい。
    - **迷う候補**：どちらも CLAUDE.md に書く。出力スタイルにする。スキルにする。
    - **選んだもの**：文体と書き出しは、出力スタイルに置く。レビューのときだけの形式は、レビューの手順を書いたスキルに入れる。
    - **理由**：口調と形の指定は、CLAUDE.md に書いても指示として働く。ただし出力スタイルは、セッションの全応答に効く口調と形のための置き場所で、コマンド 1 つで切り替えられる。CLAUDE.md に書くと、プロジェクトの事実と口調の指定が混ざる。口調を替えるときは、そのファイルを書き換えることになる。CLAUDE.md は、どのスタイルを選んでもそのまま読み込まれるので、Claude がプロジェクトについて知るべきことだけを置く。一場面だけの形式は、その場面のスキルに入れれば、ほかの応答に広がらない。

!!! example "判断例：長い作業の途中で守られなくなった規約"
    - **状況**：会話が圧縮されたあとから、`paths` 付きの rules に書いた規約が守られなくなった。
    - **迷う候補**：規約の文を強める。根の CLAUDE.md に移す。`paths` を外す。
    - **選んだもの**：その規約が圧縮の後も要るなら、`paths` を外すか、根の CLAUDE.md に移す。どちらも圧縮の後はディスクから入れ直される。
    - **理由**：`paths` 付きの rules は圧縮で要約に消え、一致するファイルを再び扱うまで戻らない。読み込まれていない規約は、文を強めても効かない。公式の文書も、圧縮を越えて残すなら `paths` を外すか根の CLAUDE.md に移すよう勧めている。2 つの違いは、置き場所の整理だけである。ファイルを分けて管理したいなら `paths` を外し、数行なら根の CLAUDE.md に足す。ただし常駐が増えるので、圧縮の後も本当に要る規約だけにする。

## 置き場所の組み合わせ方 {#combine}

CLAUDE.md・rules・スキル・出力スタイルは択一ではなく、指示の種類ごとに分けて同時に使う。どこに何を置き、何を置かないかは次のとおりである。

- **プロジェクトの根の CLAUDE.md**（`CLAUDE.md`）：毎回の作業に要る事実（コマンド・推測できない落とし穴・規則の理由）を置く。長い手順はスキルへ、一部のフォルダだけの規約は rules へ、口調の指定は出力スタイルへ移す。
- **rules**（`.claude/rules/`。`paths` 付き）：一部のフォルダやファイルだけの規約を置く。圧縮の後も要る規約は、`paths` を外すか根の CLAUDE.md に置く。
- **スキル**（`.claude/skills/<名前>/SKILL.md`）：ときどき使う手順と、その場面だけの書式を置く。毎回要る事実は置かない。
- **出力スタイル**（`.claude/output-styles/`）：セッション全体の口調・説明の量・確認の仕方を置く。プロジェクトの知識は置かない。CLAUDE.md との細かい分担は<!-- link:begin output-style-modes#vs-claude-md -->出力スタイルで応答の仕方を切り替える › CLAUDE.md・スキルとの分担（準備中）<!-- link:end -->を見る。
- **鍵**（フック・deny ルール・管理設定）：例外を許さない禁止と、必ず起きるべき処理を置く。管理設定（managed settings）は、組織が配り、利用者のファイルでは上書きできない設定である。判断の基準や理由は置かず、CLAUDE.md に書く。フックとスキルの選び方は<!-- link:begin hook-vs-skill -->フックとスキルの違い（準備中）<!-- link:end -->を見る。
- **ユーザーレベルのファイル**（`~/.claude/` の下）：自分だけの好みを置く。チームで共有する規約は置かない。
- **起動時のフラグ `--append-system-prompt`**：その起動だけ、システムプロンプトに文を足す。起動のたびに渡すので、対話での普段使いより、スクリプトや自動化に向く。自作の出力スタイルと違い、標準の指示を外さず足すだけである。足す指示が増えるほど守られにくくなると、公式のブログは述べている。

分け方の決まりは 1 つである。同じ内容を二か所に書かない。二か所に書くと、片方だけを直したときに食い違う。CLAUDE.md は全階層が足し合わされて同時に効き、食い違う指示があると、Claude はどちらかを任意に選ぶことがある。

分けたあとの各ファイルの最小の例を示す。CLAUDE.md は「.env を読ませない」、rules は「テストファイルだけの規約」、スキルは「月に一度のリリース手順」、出力スタイルは「毎回頼んでいる文体」の判断例の結果にあたる。置き場所は、それぞれの題に書いてある。スキルの手順 4 の承認は、Claude に頼む文であり、止める仕組みではない。

<!-- gen:begin snippet claude-md-vs-rules-skills-styles/claude-md-root -->
<!-- textlint-disable -->

??? example "雛形：CLAUDE.md（プロジェクトの根に置く）"

    ```markdown
    # 開発の前提

    ## コマンド

    - テスト：先に `docker compose up -d db` で DB を起こしてから `npm test` を流す。DB が起きていないと全件が失敗する
    - 型検査：`npm run typecheck`

    ## 落とし穴

    - `generated/` は手で直さない。`npm run codegen` で作り直す

    ## 止めていること

    - `.env` を読む操作は deny ルールで断ってある（別のプログラムを通した読み取りまでは止まらない）。値が要る作業は、読もうとせず人に頼む
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-vs-rules-skills-styles/claude-md-root -->

<!-- gen:begin snippet claude-md-vs-rules-skills-styles/rules-testing -->
<!-- textlint-disable -->

??? example "雛形：.claude/rules/testing.md（paths 付きの rules）"

    ```markdown
    ---
    paths:
      - "**/*.test.ts"
    ---

    # テストファイルの規約

    - テストの名前は「〜のとき〜する」の形で書く
    - 外部の API は呼ばず、`tests/fakes/` の代役を使う
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.64。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-vs-rules-skills-styles/rules-testing -->

<!-- gen:begin snippet claude-md-vs-rules-skills-styles/skill-release -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/release/SKILL.md（人が呼んだときだけ動くスキル）"

    ```markdown
    ---
    name: release
    description: リリースの手順を実行する。バージョンを上げ、タグを付け、公開前の確認をするときに使う
    disable-model-invocation: true
    ---

    # リリースの手順

    1. `git status` で作業ツリーが空であることを確かめる
    2. `npm version patch` でバージョンを上げ、タグを付ける
    3. 公開前の確認として、`npm pack --dry-run` の出力を人に見せる
    4. 人が承認したら `npm publish` を流す
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-vs-rules-skills-styles/skill-release -->

<!-- gen:begin snippet claude-md-vs-rules-skills-styles/output-style-dearu -->
<!-- textlint-disable -->

??? example "雛形：.claude/output-styles/dearu.md（自作の出力スタイル）"

    ```markdown
    ---
    name: Dearu
    description: 説明をだ・である調の短い文で、結論から返す
    keep-coding-instructions: true
    ---

    応答は結論から書く。前置きと、最後のまとめは省く。

    説明の文は、だ・である調で書く。1 文は短くし、1 段落に主張を 1 つだけ置く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet claude-md-vs-rules-skills-styles/output-style-dearu -->

## 指示が読み込まれたかの確かめ方 {#verify}

CLAUDE.md・rules・スキル・出力スタイルに置いた指示が実際に読み込まれているかは、機能ごとに次の方法で確かめる。

- **起動時に読み込まれる CLAUDE.md**：セッションで `/context all` を流し、「Memory files」の一覧に出ているかを見る。一覧にないときは、Claude から見えていない。置き場所が、作業ディレクトリかその上の階層かを確かめる。`/memory` でも、ファイルの場所の一覧を見られる。公式の文書は、rules とスキルの説明が入っているかも `/context` で確かめられると述べている。
- **サブフォルダの CLAUDE.md**：起動時には読み込まれないので、一覧には出ない。そのフォルダのファイルを Claude に読ませると、端末に `Loaded` の行とパスが出る。
- **`paths` 付きの rules と、遅れて読み込まれるファイル**：`InstructionsLoaded` フックで、読み込まれたファイルとその時期と理由を記録できる。いつ読み込まれたかを調べるときに使う。フックは `settings.json` の `hooks` キーに書く。書き方は<!-- link:begin hooks-basics -->フックの考え方とイベント（準備中）<!-- link:end -->を見る。
- **スキル**：`/skills` で、プロジェクト・ユーザー・プラグインのスキルの一覧を見る。一覧にないときは、`.claude/skills/<名前>/SKILL.md` のように、フォルダの中に `SKILL.md` があるかを確かめる。一覧にあるのに Claude が呼ばないときは、一覧の「user-only」の印（人だけが呼べる設定）を確かめ、なければ説明が頼み方に合っているかを見る。
- **出力スタイル**：`/output-style` を引数なしで流すと、選べるスタイルの一覧が出て、今のスタイルに印が付く。自作のスタイルのファイルは、端末では起動時に読まれるので、足したり直したりしたら Claude Code を再起動する。設定の `outputStyle` は大文字と小文字を区別し、合わない値は Default のスタイルになる。

読み込まれているのに守られないときは、指示の書き方や、ファイル同士の食い違いを疑う。機能ごとの調べ方は、公式の [Debug your configuration](https://code.claude.com/docs/en/debug-your-config) にまとまっている。

## 指示が届く範囲の違い {#reach}

CLAUDE.md・rules・スキル・出力スタイルは、同じ置き場所に書いても、サブエージェントやクラウドのセッションには届かないことがある。

- **サブエージェント**：サブエージェントは自分のシステムプロンプトで動くので、出力スタイルは届かない。親の会話とシステムプロンプトを丸ごと引き継ぐ fork だけが例外である。CLAUDE.md とプロジェクトの rules は届くが、組み込みの Explore と Plan は起動時に読まない。親が呼んだスキルの内容と、親の会話の履歴も引き継がれない。詳しくは<!-- link:begin what-subagents-dont-inherit -->サブエージェントに引き継がれないもの（準備中）<!-- link:end -->を見る。
- **クラウドのセッション**：クラウドの環境で動く Claude Code のセッションである。リポジトリに置いた CLAUDE.md・rules・スキルは、クローンに含まれるので届く。ただし claude.ai のプロジェクトの中のスレッドでは、届くのは根の CLAUDE.md と、`paths` のない rules だけである。ユーザーの `~/.claude/CLAUDE.md` と `~/.claude/skills/` は自分のマシンにあるので届かない。セッションの仕組みは<!-- link:begin cloud-sessions-and-teleport -->クラウドセッションと teleport（準備中）<!-- link:end -->を見る。
- **個人の好みをクラウドで効かせる**：リポジトリに置くと、そのリポジトリのセッションを開く全員に効くので、個人の好みは置かない。Anthropic のクラウド環境では、環境の setup script（セッションの開始時、Claude Code が起動する前に走る Bash のスクリプト）で `~/.claude/CLAUDE.md` を書く。書き方は、公式の [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments) を見る。

出力スタイルがクラウドのセッションで効くかは、確かめていない。

## 混同されやすい別の機能 {#similar-names}

CLAUDE.md・rules・スキル・出力スタイルと混同されやすい機能を、別のものとして整理する。

- **claude.ai の Styles**：アプリの機能で、Claude Code の出力スタイルとは別である。2026-06-01 に、Styles をスキルへ移すという告知が出た。告知の記事は、2026-11-04 時点で元の URL では読めない。Styles のメニューが今も画面に出るかは確かめていない。移された Styles の扱いは<!-- link:begin skills-in-the-app#migrated-styles -->アプリでスキルを使う › 移された Styles（準備中）<!-- link:end -->に、アプリで口調や形式を決める場所は<!-- link:begin where-to-put-instructions -->アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）（準備中）<!-- link:end -->にある。
- **カスタムスラッシュコマンド**（`.claude/commands/`）：スキルにまとめられた。`.claude/commands/` のファイルも `.claude/skills/` のスキルも、同じ名前の呼び出しを作り、同じように動く。スキルは、補助ファイルや呼び出しの制御なども足せる。
- **自動メモリ**：Claude が自分で書き溜めるメモである。人が書く CLAUDE.md とは別で、ここで比べた置き場所には含めない。確かめ方と直し方は<!-- link:begin using-auto-memory -->自動メモリ（準備中）<!-- link:end -->を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)：Anthropic・英語・確認日 2026-11-04
- [Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Debug your configuration](https://code.claude.com/docs/en/debug-your-config)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- .claude/rules と paths で必要なときだけ読ませる（準備中）
- スキルの考え方（手順を必要なときだけ読む）（準備中）

**関連**

- 出力スタイルで応答の仕方を切り替える › CLAUDE.md・スキルとの分担（準備中）
- CLAUDE.md に書くこと・書かないこと（準備中）
- アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）（準備中）
- 拡張機能の全体図と使い分け早見表（準備中）
- お願いと鍵の対応表（準備中）
- 自動メモリ（準備中）
- フックとスキルの違い（準備中）
- 拡張を足すタイミング（準備中）
- 日本語で返し続けさせる（準備中）
- サブエージェントに引き継がれないもの（準備中）
- アプリでスキルを使う › 移された Styles（準備中）
- フックの考え方とイベント（準備中）
- クラウドセッションと teleport（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
