# 工程7 道具（TA）の報告

試験：`uv run python -m unittest discover -s tests/tools` は 624 件で失敗 1（`test_gen_catalog.TestRealRepository.test_generated_files_are_fresh`）。原因は、本物のリポジトリの生成物が新しい道具より古いこと（routes の `<br>`・compare の共通の列）。メインが `tools/gen_site.py` を流せば直る。`gen_site.py --check` の古い 5 ファイル：outdated-advice-ledger・competition-rules・claude-md-vs-rules-skills-styles・caves-when-pushed・instructions-ignored（ledger は TB の台帳の直しも関わる）。TB の所の失敗は出なかった。`check_templates.py` はエラー 0。

## 番号ごと

- **18**：`tools/checks/template_keys.yml` の `settings.top` に `skillOverrides`（language は既にあった）。試験：test_check_templates.py。
- **22**：`tools/gen/facts.py`（compare）・`blocks.py`・`markers.py`（引数を省ける `param_optional`）・`config.yml`（言葉 common・conditional）・`schema/keys.yml` と `schema/facts.schema.json`（make_schema 済み）。
  - (1) 列の指定：`<!-- gen:begin compare 強制力 読み込みの時期 確認日 -->`〜`<!-- gen:end compare 強制力 読み込みの時期 確認日 -->`。属性の id でも表示の名前でも `確認日` でもよい。書いた順。知らない列は注意に出して外す。省くと今の列。
  - (2) 機能 2 つ以上で全行が同じ値の列は表から外し、表の下に「すべて共通：成熟度 GA。」。列がすべて共通なら外さない。指定した列にも効く。
  - (3) null の出し分け：features の項目に新しいキー `conditional: [survives_compaction]`（null の属性の id のリスト）を足すと「条件による」。書かない null は今までどおり「未確認」。compare と `feature` の目印の両方。conditional に挙げた属性は、全機能が null でも既定の列に出す。
- **26**：`tools/checks/body.py`。`gen:begin ledger` を持つページへの `id#<行の id>` は、行の id が data/outdated-advice.yml の advice にあれば通す（なければ従来どおり誤り）。gen 側は元から台帳の id を anchor に持っていたので変更なし。
- **28**：`tools/gen/facts.py`（fact-table）。セルの `sources` を、表の下の「出典（行ごと）：」の箇条で出す（行のセルの出典がすべて同じなら「行：出典」、違えば「行：API 出典；Claude Code 出典」）。行に出なかった項目の sources は「そのほかの出典：」。セルに sources が 1 つもなければ今までの 1 段落。`tools/checks/data_checks.py`：`gen:begin fact-table <id>` の未登録の id を `fact` と同じく止める（骨格のページだけなら警告）。
- **31(b)**：`schema/site.yml` の `source_kinds` に **公式の投稿** を足した（公式ブログの次。schema は make_schema で同期済み）。
- **34**：`tools/gen/snippets.py`・`tools/checks/templates.py`。(a) expect.yaml の `open: true` で `???+`。(c) `min_version_fact: <facts の id>`（確認済みの facts の value を版にする。features・tracks の since より優先。ない・未確認なら注意に出して features に戻す）。check_templates が、min_version_fact の id が facts にないこと・open が真偽でないことを止める。(b) は変更なし。(d) card §10 に 1 つの形で書いた。
- **41(a)**：`overrides/assets/css/ca.css` に、`.highlight.language-text`・`.language-markdown` の pre/code を `pre-wrap` と `overflow-wrap: anywhere` にする規則。bash・json などは変えない。描画は未確認（Material の div クラスは `language-text highlight` の想定）。
- **43(a)**：形は `<!-- link:begin field:symptoms --><!-- link:end -->`。間に分野の名前、`<分野>/index.md` への相対リンク。公開するページのない分野は「名前（準備中）」。知らない分野は注意に出して文字のまま（check_pages は fields にない分野を誤りにする）。`lib/base.py` に `FIELD_PREFIX`、`gen/core.py` に `field_link`。`#anchor` は付けない。
- **45**：`tools/gen/routes.py`。行き先を `<br>` で並べる（`causes` の表は変えていない）。

## ページで使う形

- 列の絞り：`<!-- gen:begin compare 強制力 読み込みの時期 圧縮で残るか -->`
- 条件による：data/facts.yml の rules の項目に `survives_compaction: null` と `conditional: [survives_compaction]`（data は TB かメイン。私は触れていない）
- 分野の入口：`<!-- link:begin field:symptoms --><!-- link:end -->`
- 台帳の行：`<!-- link:begin outdated-advice-ledger#important-caps --><!-- link:end -->`
- 雛形：expect.yaml に `open: true`、`min_version_fact: subagent-handback-min-version`

## 試験

新しい `tests/tools/test_gen_step7.py`（26 件：compare の列・共通・条件による・fact-table の行ごとの出典・open と min_version_fact・分野のリンク・link と fact-table の検査・CSS）。`test_check_templates.py` に 2 件。既存の routes の試験 2 件を `<br>` に合わせて直した。

## メインに判断してほしいこと

1. card.md：指示の「§3（目印）」は、実際の card.md では §9「目印の一覧」だった。§9 と §10 に書いた（§8 の link の説明には触れず、§9 の箇条に分野の入口の形を足した）。
2. 雛形の既存 expect.yaml（snippets/request-vs-lock など）は `{do, result}` の形。card §10 は `{when, then}` を 1 つの形にして `do`・`result` を使わないと書いた。直す担当（PF）が要る。
3. conditional は私の案（キー名・形）。「rules の圧縮で残るか」を data に入れるのはメイン（か TB）。入れるまで rules の欄は「未確認」のまま。
4. 「すべて共通」の行は、指定した列にも効く。指定した列を必ず表に残したい場合は、別の決めが要る。
5. source_kinds の名前は「公式の投稿」とした（他に案があれば置き換え可。common §11 の文はメイン）。
6. 本物の生成物の更新（`gen_site.py`）はメイン。ledger.md が古いのは TB の台帳の直しかもしれず、私の直しだけが原因かは未確認。

## 道具の呼び出し

約 35 回（読み 15・編集 10・試験 8 ほか）。
