# 報告：直し（outdated-advice-ledger）

- 手引きの版：共通 2026-11-04 第1版・型（ledger）2026-11-04 第1版・指示 brief-page v2
- 対象：`verify-clarity.md` の指摘 24 件（直す 1・直したほうがよい 14・軽い 9）。24 件すべてを扱った
- 結果：本文と雛形だけで直したのが 12 件（1・2・3・5・6・7・12・13・16・18・19・24）。本文で受けたうえで data と生成の層の提案も出したのが 5 件（4・8・9・10・17）。提案だけにしたのが 7 件（11・14・15・20・21・22・23）。検査はエラー 0、警告 1（5 の 1）
- 再開：使用量の上限で中断したあとに再開した。中断の前に、本文・雛形・この報告は書き終わっていた（ページと雛形の更新時刻が、この報告より前）。再開後は検査を流し直して照らしただけで、本文・雛形・front matter は変えていない（7・9）

## 1. 書いたファイル
- `docs/changes/outdated-advice-ledger.md`：手書きの部分だけ。front matter は変えていない（`updated` は今日の 2026-11-04 のまま。`stage` は draft のまま）。目印の間は `gen_site.py --page` で作り直した（変わったのは、雛形の写しと link の目印の中身だけ）
- `snippets/outdated-advice-ledger/find-old-advice.sh`・`find-old-advice.expect.yaml`
- この報告

## 2. 直したこと
- 1（直す）：雛形の出力を `[#important-caps]` の形にし、雛形のコメントと `.expect.yaml` をそろえた。本文に「行頭の `[#…]` は台帳の行の id で、このページの URL の末尾に付けると、その行へ移る」と 1 文足した。偽の HOME とダミーのファイルで流し、`[#id]` が付くことと、該当がなければ何も出ないことを確かめた
- 2：要点の「いつ引くか」の 3 つ目に、台帳の行（`#think-hard-keywords`）へのリンクを足した。答えの文は足していない（答えは行の「今どうするか」と thinking-keywords が持つ。共通 §10）
- 3：台帳の節の頭に段落を足した（載るのは一部で、載っていない小技が今も有効とは限らない。見つからないときは回避策の 2 つの問いで見当をつけ、そこの手順で確かめる）。行数は書いていない
- 4（本文で一部）：行が時期・状態・面のどの順にも並ばないことと、言い回しで探すことを台帳の節の頭に書いた。一覧表は生成の層の仕事なので提案 T1
- 5：アプリのタブに主な行 6 つ、API のタブに `budget_tokens`・`temperature`・prefill・`<thinking>` の行への手書きのリンクを足した。強調と決まり文句の探し方にも行へのリンクを付けた
- 6：欄の説明に 4 つの原理の定義を移し（元の定義の段落は消した）、four-principles への link の目印を付けた。導入に 4 つの名前を足し、回避策の節の頭に 4 つの原理を一言ずつで言い直した
- 7：定義を行の付け方に合わせて広げた（確かめるに、考える量や出力の安定の調整を含める）。four-principles の定義が決まったらそろえ直す（5 の 2）
- 8（本文で一部）：導入と欄の説明に、名前や画面だけが変わった行も載せること、その行の原理は機能が受け持つ原理であることを書いた。欄の見出しの直しは提案 T4
- 9（本文で一部）：時期の読み方に「〜」の項目を足した（順に展開された行と、日までは絞れなかった行。始まりより前は前のやり方、終わりより後は新しいやり方、間はどちらもありうる）。各端が何の日かは行ごとに違い、本文では書けない。提案 T3・D1
- 10（本文で一部）：台帳の節の頭で、think hard の行の時期は ultrathink が戻った版の日で、段階のキーワードが外れた日は確かめられていない、と断った。時期の値は提案 D1
- 11（提案のみ）：「今どうするか」は data から生成する文で、本文では直せない。結論を 1 文目にする書き直しを提案 D2
- 12：雛形の前後とコメントに「探すのは言い回しで探せる一部の行だけ。API の引数と画面の道順は探さない。出力が空でも、古い助言が残っていないとは言えない」を足した。件数は書いていない。雛形の見出しに「探せるものだけ」を足した
- 13：回避策の節に 2 つ目の判断例を足した（自作のループが置き換わる候補かを、2 つの問いで見る）。2 つ目の問いに「5 組の移り先のようなもの」と添えた。条件付きの行を引く例は足していない（状態ごとの行動は読み方の節にある。add-double-check の行は 14 が直るまで例に向かない）
- 14（提案のみ）：data の直し。提案 D3（Opus 5.5 の手引きは Opus 5 の型を出発点にできるとする。原文で確かめた）
- 15（提案のみ）：data の直し。提案 D4（「クラウドの予定のタスク」で通し、Desktop の予定のタスクと `/loop` は手元で動く別の機能と書く。routines の文書の原文で確かめた）
- 16：判断例の迷う候補を「全部すぐ移す／何もしない／必要なものだけ移す」にした。選んだものに、スキルの働き 3 つ（補助のファイルを置く・自分で読み込む・呼ぶ人を決める）と行へのリンクを足した
- 17（本文で一部）：台帳の節の頭に、状態の凡例を 1 文で足した（詳しくは読み方の節）。見出しの直下の 1 行は生成の層の仕事で、提案 T2
- 18：「版が確かめられた行には版が付く。付かない行は日付で比べる」に直した
- 19：台帳の節の頭を 3 段落に分けた。回避策の節は、規則の使い方（問い・判断例）と「動き続ける」の段落に分けた。「同じ型」を「同じ事情の回避策」に直した
- 20（提案のみ）：data の直し。提案 D5
- 21（提案のみ）：data の直し。提案 D6
- 22（提案のみ）：data の直し。提案 D7
- 23（提案のみ）：data と生成の層の直し。提案 T5
- 24：「自分の設定や記事で見つける」の最後に 2 文足した（動かなくなるもの・安全に関わるものから直す。今も動くものは急がず、新しく書くときから今のやり方にする）

## 3. 範囲を越えたこと
- なし。textlint が見ない字下げした部分（タブ・判断例の枠）は、字下げを外した写しをスクラッチ（リポジトリの外）に作ってかけた
- 再開後の確認で、字下げを外した写しを一度 `docs/changes/` に隠しファイルとして置いてしまい、数秒で消した。ページ本体は変わっていない（md5 が同じ）。以降の写しはスクラッチ（リポジトリの外）だけに置いた

## 4. 止められた操作
- なし

## 5. メインに判断してほしいこと
1. 警告 1 件を残した（`四つ => 4つ`、arabic-kanji-numbers）。原因は link の目印が書く four-principles の題名「四つの原理と比例則（…）」で、本文の文ではない（執筆の報告 5 の 3 と同じ件）。選ぶのは、(a) four-principles の題名を「4 つの原理と比例則」にする、(b) textlint が link の目印の間を見ない設定にする、(c) このまま、のどれか。リンクを外せば警告は 0 になるが、指摘 6 の「四つの原理へのリンク」が戻る。決まるまでリンクを置いた
2. 本文の 4 つの原理の意味は、requirements §3.1 の一文を台帳の使い方に合わせて広げたもの。four-principles を書くときはそちらを正にして直す。行の原理が定義に合いにくい行（budget-tokens・lower-temperature・action-beta-direct-prompt・avoid-opus-as-expensive・think-hard-keywords）は、付け直すか確かめてほしい
3. 方針の文に当たるかの確認。(a)「台帳に載っていない小技が、今も有効とは限らない」は使い方の案内として書いた。方針の文なら削る。(b)「名前や画面だけが変わった行は、その機能が受け持つ原理を示す」は、検証の案から推した。data の書き手の意図と違えば直す
4. 台帳の行 ralph-loops の題に、第三者のプラグインの名前（Ralph）が出る。共通 §15 の「否定的な文脈で名指ししない」に当たるか。本文の判断例には名前を出していない
5. 提案はどれも台帳の状態（撤回・置換・条件付き）を変えない。作者の承認（共通 §19）は要らないと見た

## 6. 提案
前の報告（write.md）の提案は、そのまま残っている。この直しで足す front matter の提案はない。

生成の層（tools/gen・schema/keys.yml。共有のファイル）
```yaml
tools:
  - id: T1
    findings: [4]
    files: [tools/gen/ledger.py, tools/gen/config.yml, schema/keys.yml, data/outdated-advice.yml]
    change: "gen:begin ledger の前に置く一覧表の block（例：ledger-index）を足す。列は、古い助言（行へのリンク）・状態・変わった時期・面。面の列のために、data の各行に surfaces（app・claude-code・api）を足す。できたら、ページの台帳の節の頭に <!-- gen:begin ledger-index --> の組を置く"
    reason: "台帳が 37 個の小見出しと箇条の連続で、状態・時期・面を見比べられない。型の手引き ledger の「データから作る表」に当たるものが今はない"
  - id: T2
    findings: [17]
    files: [tools/gen/ledger.py]
    change: "行の見出しの直下に「古い助言（状態：撤回）」の 1 行を出す"
    reason: "行だけを切り出して読む AI と、ページ内検索で行に飛んだ人が、その行を現行の機能と読まないため"
  - id: T3
    findings: [9, 10, 22]
    files: [tools/gen/terms.py, schema/keys.yml, data/outdated-advice.yml, data/facts.yml]
    change: "data の changed と names の changed に、読者に見せる短い注 label を足し、period_text が時期の後に「（<label>）」を付ける。今の changed.note は内部のメモで、ページには出ない。label の中身は D1"
    reason: "範囲（〜）の始まりと終わりが何の日かが、行を読んでも分からない。think-hard-keywords の時期は一部の変化の日にすぎないが、時期の欄だけ読むと全体の日に見える"
  - id: T4
    findings: [8]
    files: [tools/gen/ledger.py, schema/keys.yml, data/outdated-advice.yml]
    change: "名前や画面だけが変わった行は、原理の欄の見出しを「この機能が受け持つ原理」に替える。対象は code-on-the-web-remote・routines-name・slash-cost-and-stats・fork-to-branch・max-5x-or-20x・customize-tabs・styles-for-tone・cowork-separate-app・memory-daily-summary。name を持たない 3 行（styles-for-tone・cowork-separate-app・memory-daily-summary）には、印（例：principle_kind: feature）を data に足す"
    reason: "今の見出し「どの原理の回避策だったか」は、改名や画面の変更の行では意味をなさない。本文は断り書きで当面しのいだ"
  - id: T5
    findings: [23]
    files: [tools/gen/ledger.py, schema/keys.yml, data/outdated-advice.yml]
    change: "data に see_also（台帳の行の id の配列）を足し、「同じ話題の行：」として行へのリンクを出す。付ける行は tell-it-to-use-subagents・subagent-per-step・subagents-to-save-context の 3 行で、互いを指す"
    reason: "3 行が同じ使いどころを別の状態・出典で書き、相互の参照がない。1 行だけ読む人は残りの 2 行を知らない"
```

data/outdated-advice.yml と data/facts.yml（共有のファイル。メインが写す。版と日付は data の note による）
```yaml
data:
  - id: D1
    findings: [9, 10, 22]
    note: "T3 の label の中身。行 id → label"
    labels:
      think-hard-keywords: "ultrathink が戻った版。think hard などの段階のキーワードが外れた時期は、確かめられていない"
      yolo-skip-permissions: "始まり：Pro・Max・Team の新しいセッションで auto モードが既定になった日。終わり：対話のセッション全体で既定になった日"
      approve-everything-first: "始まり：Pro・Max・Team の新しいセッションで auto モードが既定になった日。終わり：どのプランと提供元でも既定になった日。2.1.283 は、公式の文書が既定の境とする版"
      tell-it-to-use-subagents: "始まり：Opus 5 の頼み方の手引きの公開日。終わり：Best practices の改稿の日"
      subagent-per-step: "始まり：Opus 5 の頼み方の手引きの公開日。終わり：Best practices の改稿の日"
      interactive-tutorial: "始まり：Claude 4.6 以降のモデルが prefill を受け付けなくなった日。終わり：チュートリアルが使う Claude 3 Haiku が退役した日"
      removed-commands: "始まり：最初に消えた /pr-comments の日。終わり：最後に消えた TaskOutput ツールの日。機能ごとの版は「今どうするか」に書く"
      ralph-loops: "始まり：/goal が入った日（2.1.139）。終わり：dynamic workflows が入った日（2.1.154）"
      tmux-agent-orgs: "始まり：エージェントチームが入った日（2.1.32）。終わり：agent view が入った日（2.1.139）"
      names/web-to-cloud-sessions: "日までは絞れない。公式の文書の題が、始まりの日の写しでは旧名、終わりの日の写しでは新名だった"
      names/customize-to-plugins: "始まり：Free・Pro・Max・Ultra・Team で順に展開が始まった日。終わり：Enterprise で既定で有効になる予定の日（2026-11-04 の時点）"
  - id: D2
    findings: [11]
    row: think-hard-keywords
    key: now
    before: "考える深さは effort（/effort・--effort・設定）で決める。think・think hard・「熟考」などの言い回しはキーワードとして扱われず、effort の範囲で少し後押しするふつうの文として渡る。ultrathink だけが、そのターンだけ深く考えるよう頼む言葉として認識され、セッションの effort は変えない。Anthropic の API の Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 では、そのターンを xhigh で動かす。効くのは対話のターミナル（2.1.311 以上）と VS Code（2.1.316 以上）。CLAUDE_CODE_DISABLE_ULTRATHINK（2.1.316 以上）で切れる。"
    after: "think・think hard・think harder・「熟考」・「よく考えて」と書いても、effort は上がらない。これらはキーワードとして扱われず、effort の範囲で少し後押しするふつうの文として渡る。考える深さは effort（/effort・--effort・設定）で決める。ultrathink だけは、そのターンだけ深く考えるよう頼む言葉として認識され、セッションの effort は変えない。Claude Code が Anthropic の API で Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 を使うときは、ultrathink のターンを xhigh で動かす。この動きは、対話のターミナル（2.1.311 以上）と VS Code（2.1.316 以上）で働く。CLAUDE_CODE_DISABLE_ULTRATHINK（2.1.316 以上）で切れる。"
    reason: "答えが 2 文目にあり、1 文目は effort の話。「API の Opus 5.5…では」は API を直接使う読者の話に読める。「効くのは」に主語がない。事実は変えず、結論を先にして主語を補った"
  - id: D3
    findings: [14]
    row: add-double-check
    key: now
    before: "…（消す）。ほかのモデルでは、終わる前に基準と照らして確かめるよう頼むのは今も効く。"
    after: "…（消す）。Opus 5.5 の公式の手引きは、Opus 5 の頼み方を出発点として使えるとするので、同じ扱いから始め、自分の作業で比べる。ほかのモデルでは、終わる前に基準と照らして確かめるよう頼むのは今も効く。"
    also: {key: how_to_find, before: "…使うモデルが Opus 5 か Opus 5.5 かを確かめる。", after: "…使うモデルを確かめる。Opus 5 と Opus 5.5 は、一言を消して比べることから始める。ほかのモデルは残してよい。"}
    reason: "Opus 5.5 の読者が、消すのか残すのか分からない。2026-11-04 に Prompting Claude Opus 5.5 の冒頭（「Existing Claude Opus 5 prompts should perform well without changes, and the patterns in Prompting Claude Opus 5 remain a reasonable starting point」）で確かめた。5.5 が言われなくても確かめるとまでは、そこに書かれていない"
  - id: D4
    findings: [15]
    row: routines-name
    key: now
    before: "今の名前は予定のタスク（cloud scheduled tasks）。claude.ai/code/routines か Desktop の Code タブ、CLI の /schedule で作る。"
    after: "今の名前はクラウドの予定のタスク（cloud scheduled tasks）。claude.ai/code/routines か Desktop の Code タブ（Local と Cloud の選択が出たら Cloud）、CLI の /schedule で作る。"
    also:
      - {key: how_to_find, before: "手元で動く予定（Desktop の予定のタスク、/loop）は別の機能なので、どれを指すかを確かめる。", after: "手元で動く Desktop の予定のタスクと /loop は、クラウドの予定のタスクとは別の機能なので、どれを指すかを確かめる。"}
      - {file: data/facts.yml, names: routines-to-scheduled-tasks, key: current, before: "予定のタスク（cloud scheduled tasks）", after: "クラウドの予定のタスク（cloud scheduled tasks）"}
    reason: "「予定のタスク」が新旧どちらの機能か決まらない。2026-11-04 に routines の文書で確かめた（「A cloud scheduled task, formerly a routine」「Two other features schedule work on your machine instead of in the cloud: Desktop scheduled tasks and /loop」「if a menu with Local and Cloud opens, select Cloud」）。names の current は用語索引など他のページにも出るので、変えてよいかはメインが決める"
  - id: D5
    findings: [20]
    rows:
      architecture-in-claude-md: {key: why_then, before: "公式は、この表の助言はどれも…", after: "公式の Best practices は、「もうやめてよい助言」の表の助言はどれも…"}
      keep-going-dont-be-lazy: {key: why_then, before: "公式は、この表の助言の多くは…", after: "公式の Best practices は、「もうやめてよい助言」の表の助言の多くは…"}
    reason: "「この表」が行の中になく、行だけ読むと何の表か分からない"
  - id: D6
    findings: [21]
    rows:
      interactive-tutorial:
        key: now
        before: "第 5 章の prefill（Speaking for Claude）は Claude 4.6 以降のモデルで、temperature を 0 にする呼び方は Claude 4.7 以降のモデルか API の版 2026-10-21 で、400 エラーになる。"
        after: "第 5 章の prefill（Speaking for Claude）は、Claude 4.6 以降のモデルで 400 エラーになる。temperature を 0 にする呼び方は、Claude 4.7 以降のモデルで、または API の版 2026-10-21 で、400 エラーになる。"
      lower-temperature:
        key: now
        before: "API の版 2026-10-21 では、この 3 つを送ると既定の値でも 400 エラーになる。それより前の版でも、Claude 4.7 以降のモデルは既定以外の値で 400 になる。既定以外の値を受け付けるモデル（Sonnet 4.6 など）を古い版で呼ぶときだけ今も効くが、版を上げると効き目がなくなり、代わりの設定はない。"
        after: "API の版 2026-10-21 では、この 3 つを送ると、既定の値でも 400 エラーになる。それより前の API の版でも、Claude 4.7 以降のモデルは、既定以外の値で 400 エラーになる。既定以外の値を受け付けるモデル（Sonnet 4.6 など）を古い API の版で呼ぶときだけ、今も効く。API の版を上げると効き目がなくなり、代わりの設定はない。"
    reason: "1 文に条件が 2〜3 入る。「版」が API の版とモデルの世代の両方に読める。条件ごとに文を分け、「API の版」「モデルの世代」と書き分けた。事実は変えていない"
  - id: D7
    findings: [22]
    rows:
      removed-commands:
        key: now
        before: "どれも消えた。Vim の操作は /config の Editor mode で切り替える。PR のコメントは Claude に直接頼んで読ませる。ultraplan の代わりは plan mode。背景の作業の出力は、Claude が Read でその出力のファイルを読む。/tag の代わりの案内は文書にない。"
        after: "どれも消えた。/pr-comments（2.1.91）の代わりは、PR のコメントを Claude に直接頼んで読ませること。/vim（2.1.92）の代わりは、/config の Editor mode で Vim の操作を切り替えること。/tag（2.1.92）の代わりの案内は文書にない。ultraplan（2.1.222）の代わりは plan mode。TaskOutput ツール（2.1.83 から非推奨、2.1.277 で削除）の代わりは、Claude が Read でその出力のファイルを読むこと。"
      customize-tabs:
        key: now と how_to_find
        change: "how_to_find の末尾の「Team と Enterprise で「Skills」を切っている組織は、2026-11-30 から Desktop のプラグインも止まる。」を now の末尾へ移す"
    reason: "removed-commands は 5 つの機能の削除を 1 行に束ね、時期は 1 つの範囲で、機能ごとの日付も版もない。customize-tabs の 11-30 の予告が「見つける方法」の末尾に埋まっている。版は data の note と research/01 KQ4 4-2 による"
```

## 7. 検査の結果
- `gen_site.py --page outdated-advice-ledger`：注意 0（2 回流した）。`--check` で古いのは nav.yml だけ（担当外）
- `check_pages.py --page`：エラー 0・警告 0。`check_templates.py --page`：0・0。`check_svg.py --page`：0・0
- `npm run lint:text` と `npx textlint`（自分のページ）：エラー 0・警告 1（`四つ => 4つ`。理由は 5 の 1）。ほかのページの指摘（agreement-is-not-evidence.md・how-to-use.md）は担当外
- textlint が見ない字下げした部分は、字下げを外した写しをスクラッチでかけた。結果は同じ 1 件
- 再開後（2026-11-05）に同じ検査を流し直した。`gen_site.py --page`：書き換え 0。`check_pages.py --page`・`check_templates.py --page`・`check_svg.py --page`：0・0。textlint は、ページ本体・字下げを外した写し・`npm run lint:text`（自分のページ）のどれも警告 1（`四つ => 4つ`）のみ。結果は上と同じ

## 8. 確かめていないこと
- 描画（幅 390px のライトとダーク）。ビルドしていない。入れ子の箇条だけ、Python-Markdown で HTML にして構造を見た
- 本文に足した事実の出どころは、台帳の行（data）と束の材料。一次資料を読み直したのは、Opus 5.5 の手引き（D3）と routines の文書（D4）だけ。D7 の版と日付は data の note による。判断例の `/goal` は ralph-loops の行に基づき、`/goal` の文書は読み直していない
- 「URL の末尾に `#id` を付けると行へ移る」は、見出しの `{#id}` の書き方から言っていて、ブラウザでは試していない
- 雛形は偽の HOME とダミーのファイルで流しただけで、雛形の動作確認（verified.yaml）ではない。macOS の grep・bash 3.2 は試していない
- 提案 T1〜T5 と D1〜D7 を当てたあとの生成結果。当てていないので、ページに出る形を見ていない
- 提案 D2〜D7 の `before`（`…` で略した所は、略していない部分だけ）は、再開後にページの生成された文と照らして一致した（D2 は、ページでは `CLAUDE_CODE_DISABLE_ULTRATHINK` の下線が `\_` と escape されて見えるだけ）。`after` の事実は照らし直していない

## 9. 使用量
- 道具の呼び出し 約 70 回（読み取りと確認が大半）。Web の取得 2 回（curl。platform.claude.com の Opus 5.5 の手引き、code.claude.com の routines の文書）
- 再開後：道具の呼び出し 約 25 回（読み取りと検査の流し直しが大半）。Web の取得 0 回
