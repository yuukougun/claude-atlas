# 工程7 build-TC 報告

## 1 check_page.py の run_textlint の確かめ
- 結論：誤りなし。tools/textlint_targets.py の `--run` と同じ作り（根の下の `.textlint-mask-*` に写しを置き、`mask_generated` を当て、出力のパスを元のページに戻し、finally で消す）。行数は変わらず、行番号も元のページのまま出る。
- 本物の textlint で確かめた：目印の間の「四つ」は警告にならず、目印の外の「四つ」だけが `元のパス:行:列` で警告になる。
- 変わった点（誤りではない）：目印のあるページは textlint に絶対パスの写しを渡す（以前は相対パス）。既存の試験 2 件（引数が相対パスの `II` と等しい）を、写しを渡す形に直した。
- 試験（tests/tools/test_check_page.py）：偽の textlint を、渡された写しの中身を残し、`__FIRST__` を写しのパスに置き換える作りにした。TestMask（写しに disable が入る・元は無傷で写しは消える・出力が読めなくても消える・指摘が元のページに戻る・目印のないページは写さない）と、本物の textlint がある環境だけで動く TestMaskWithRealTextlint（目印の中の「四つ」は出ず、外は出る。なければ skip）。

## 2 検査の回避を外す
- docs/prompting/four-specifics.md と docs/basics/request-vs-lock.md の、段落を囲んだ textlint-disable〜enable（「対象・状況・手本は…」「原理の「縛る」は…」の段落）を外した。`check_page.py four-specifics request-vs-lock` はエラー0・警告0（gen あり・なし両方）。
- 別名の行を囲む disable〜enable は、検査「別名の行」が求めるので残した（外すとエラーになる）。

## 3 name の目印
- 形：`<!-- name:begin <names の id> -->今の名前<!-- name:end -->`（段落の中。id だけを書く）。
- 変えたもの：tools/lib/markdown.py（MARKER_RE・MARKER_KINDS）、tools/lib/pages.py（`name_ids`）、tools/gen/facts.py（`name_text`。確認済みでなければ「未確認」、ない id は note を出して空）、tools/gen/markers.py、tools/checks/data_checks.py（新しい検査「names の id」：ない id はエラー、骨格のページだけなら警告）、tools/checks/body.py と tools/gen_site.py（説明文）、tools/textlint_targets.py（GEN_BEGIN_RE・GEN_END_RE に name）、planning/guides/card.md §9 に 1 行。
- 試験：test_lib_read（読み取り・対のずれ）、test_textlint_targets（マスク）、test_gen_parts（今の名前・未確認・ない id・余分な引数）、test_check_pages（names の id）。

## 4 改名の時期が分からない名前
- schema/keys.yml の names.changed.date の required を外し、`uv run python tools/make_schema.py` で schema/facts.schema.json を作り直した。
- tools/gen/terms.py の旧名の一覧：時期が空なら「（不明）」と出す（言葉は labels.period_unknown で変えられる。既定は「不明」）。年表は元から date のない項目を出さない（変更なし）。
- data/facts.yml の academy-claude-rename：status を確認済みに、changed は note だけ（date・until・label を省く。note は「改名の時期は不明。…」）。
- 試験：test_gen_ledger（TestRenameWithoutDate：旧名の一覧は「不明」・年表に出ない）、test_check_pages（date を省いても data の形は通る）。

## 5 how-to-use
- 本文の段落に、手で書いた Claude Academy の名前はなかった（「公式の教材」とだけある）。あるのは 235 行の表の中と 297 行の参考の節だけで、どちらも替えなくてよい指定なので、how-to-use.md は変えていない。`check_page.py how-to-use` はエラー0・警告0。

## 試験の結果
- 変えた所の試験：test_check_page・test_gen_ledger・test_lib_read・test_textlint_targets・test_check_pages は通る。
- 全体（`discover -s tests/tools`）：637 件、失敗 2、skip 5（本物の textlint がある環境でも、既存の skip が 5）。失敗 2 件は私の変更に由来しない。
  - test_gen_catalog.test_generated_files_are_fresh：nav.yml が古い（メインの目次の直しの後に gen_site.py で作り直す）。
  - test_gen_parts.test_host_page_without_its_markers_is_noted：tools/gen/config.yml の hosts に ledger-index が足されていて、試験の期待が「1: roadmap」のまま（期待を「2: roadmap、ledger-index」に直すか、config を戻す）。

## メインに判断してほしいこと
- 上の失敗 2 件の直し方（nav.yml の再生成は、目次を直し終えてから）。
- 5 は、本文に名前を書く段落がない。how-to-use の本文に名前を出したいなら、段落を足して `<!-- name:begin academy-claude-rename -->Claude Academy<!-- name:end -->` を置く（執筆の担当へ）。表の中のリンクの文字に name の目印を入れるのは、リンクの書き方が崩れるので勧めない。
- name の目印は、freshness（期限）の計算にまだ入れていない（names の checked は期限に効かない）。必要なら別の仕事にする。

道具の呼び出し：約 45 回。
