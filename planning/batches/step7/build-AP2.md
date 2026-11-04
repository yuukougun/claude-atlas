# 報告：承認された文の反映（AP2）

## 手順ごとにしたこと
1. 段階 reviewed：意味「書いた担当とは別の担当が、分かりやすさを確かめ直した」、表示名「分かりやすさ確認済み」、verified は出典を読み直したページにだけ。直した所：tools/gen/config.yml（表示名）、planning/design.md（キーの表の stage・verified、§10.2 の段階の移り方、§12 の8・9）、planning/guides/common.md §19、docs/start/how-to-use.md（バッジの表・レベルの節・節 stage の本文と表）、docs/start/ai-and-sources.md（done の表の reviewed の行と、その下の「準備中」の1文）。overrides/main.html と card.md は直す所なし（表示名は config から出る。card.md は「reviewed 以上にしない」のみ）
2. ai-and-sources の summary：案のとおり（ページ、planning/catalog/start.yaml）
3. how-to-use：節 freshness に案 A、節 report に案 B（返事と直す時期は約束しない、の1文つき。承認 2-2）。summary の報告の文、signs の「辞典の内容に誤りや古い情報を見つけた」を戻した（ページ、start.yaml は元から入っている）。要点の「何ができるか」と「いつ引くか」にも報告の1項を足した
4. competition-rules・outdated-advice-ledger：触れていない（現行のまま）
5. data/outdated-advice.yml：6行の status を替えた（prefill-for-json 置換、budget-tokens 置換、thinking-tags 条件付き、mcp-sse-transport 置換、cowork-separate-app 条件付き、tell-it-to-use-subagents 撤回）。台帳のページは生成し直していない
6. design §6.7 に「対象は…研究の結果のような固定の記録は除く」の1項を足した。§12 の5にも同句

## 検査と試験
- check_page how-to-use、ai-and-sources：どちらもエラー0・警告0（各1回）
- tests/guides：OK。tests/tools：637件中2件失敗
  - test_gen_site の test_extra_for_templates（tests/tools/test_gen_site.py:72）：期待が reviewed「検証済み」のまま。「分かりやすさ確認済み」に直す必要がある（書いてよい範囲の外なので直していない）
  - test_gen_catalog の test_generated_files_are_fresh：生成物が古い（nav.yml・llms.txt・台帳ほか。第一波ページの移動と今回の data/本文の変更のため）。メインの生成で解消する見込み

## メインの直しの確かめ
- CLAUDE.md の1行目：「（…大会の規則。研究の結果のような固定の記録は除く）」で、決定の「括弧に足す」と作者の答えに合っている。ほかの行に差分なし
- decisions.md 末尾の節：reviewed の意味・表示名・verified の条件、方針の文の承認（返事と直す時期は約束しない、規則のページで「読ませてよいか」に触れない、台帳の小技の文を残す、免責は決まった文だけ、thinking-tags は条件付き）、Codeforces の URL を載せない、が approval.md の案1・各推奨案と一致。問題なし

## メインに判断してほしいこと
- tests/tools/test_gen_site.py:72 の期待値の更新
- 生成：台帳のページ、ai-and-sources・how-to-use のリンク目印（準備中の表記）は未生成。design §12 の8・9 と §10.2 は文言を作者承認の趣旨で整えたので、念のため目を通してほしい
- ai-and-sources の contact の節はすでに「返事と直す時期は約束しない」を含む。how-to-use の節 report にも同じ文を入れた（案 B は 2-2 で足す扱い）

## 道具の呼び出し
Bash 11、Edit/Write 0（Bash内の python で編集）
