# 工程7 PF1 の報告

7ページすべて `check_page.py` はエラー0・警告0（how-to-use は試行で3回流した）。

## 番号ごと

- 5：3ページ（instructions-ignored・how-to-use・keep-replies-in-japanese）の「この辞典の推奨」の前後を確かめた。自然に読める。直しなし
- 7：how-to-use の volatility を 中（ページ・start.yaml）
- 12：four-specifics の title を「具体性の 4 点」に（ページ・prompting.yaml）。summary の「4 点」も目次に合わせた。節 misreadings の題を「境界の入力」に（目次）
- 18：writing-skills の雛形を `skill-override-off` から `local-settings`（local-settings.json・.expect.yaml）に改め、本文の目印も合わせた。名前を `settings.local.json` そのものにしなかったのは、check_templates が「settings.json で終わる名前」だけを settings として見るため
- 22：data/facts.yml の rules に `survives_compaction: null`・`conditional: [survives_compaction]`。claude-md-vs-rules-skills-styles と instructions-ignored の compare の列を「強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか」に絞り、本文の「未確認」を「条件による」に直し、「入った版」の説明を外した
- 26・27：four-specifics（four-principles#show・#verify、six-causes）・request-vs-lock（four-principles、outdated-advice-ledger#important-caps）・writing-skills（outdated-advice-ledger#commands-directory）を link の目印に戻した
- 32：keep-replies-in-japanese の「新しい版」3か所を `fact:begin subagent-handback-min-version` に。1か所にあった「版を本文に書かず」の文は削った
- 33：節 #measure の題を「検証の方法」に（ページ・japanese.yaml・本文内のリンク文言）。結果は載せていない
- 34(a)：keep-replies の4雛形を `open: true` に
- 34(c)：使わなかった。合う facts がない。skill-doctor-min-version はあるが、writing-skills の雛形（SKILL-with-script・allowed-tools・skillOverrides・`${CLAUDE_SKILL_DIR}`）に当たる版の項目がない。keep-replies の Stop フックの雛形（`last_assistant_message` が入った版）にもない。subagent-handback-min-version は別の意味なので当てていない
- 35：cli.yaml の cloud-sessions-and-teleport の notes に追記
- 36：雛形 claude-md-root の文を指示のとおり弱めた
- 39：eval.yaml の model-based-grading の notes に追記
- 42(c)：facts の academy-claude-rename を 未確認 に。how-to-use の名前を目印にする件は当てなかった（下）
- 43：(a) 症状辞典の入口を `link:begin field:symptoms` に (b) 雛形は残した (c) 目次に trust の節を足し、official-docs の題を直した（ページは直す前から合っていた） (d) 「どのレベルでも」は本文は元からそろっていた。残る「どの段階でも」は roadmap の節の題で、生成されるリンク文言
- 44：request-vs-lock の surfaces を `[claude-code]`（ページ・basics.yaml）。notes に戻す旨を足した
- 46：basics.yaml の request-vs-lock、symptoms.yaml の instructions-ignored に templates を足した。extend.yaml の claude-md-loading-order の notes（元は null）に AGENTS.md の件を足した
- request-vs-lock の2雛形の expect.yaml を `when`・`then` に直した

## メインに判断してほしいこと

1. 42(c)：names を書く目印がない。`fact:begin` は facts だけを引き、names の id を指すと check_pages が止める（`terms old` は表のみ）。how-to-use の「Claude Academy」は手書きのまま（表の中の名前と、参考の題）。names を引く inline の目印が要る。かつ status を 未確認 にしたので、出力が文として読めるかは確かめられていない
2. check_page.py は textlint の目印の間の除外をしない（textlint_targets.py の `--run` はする）。link の目印の題に「四つ」「二つ」が入ると警告が出るため、four-specifics と request-vs-lock の該当1段落を `textlint-disable/enable` で囲んだ。check_all 側では要らないはず
3. 目次の how-to-use・four-specifics の summary や signs は、ページの front matter と元から差があり（目次が新しい文を持つ所あり）、今回は指定の項目だけを合わせた
4. 18 の雛形名 `local-settings`（案）

## 提案

- tools：check_page.py の textlint に目印の除外を入れる。names を引く inline の目印を足す
- data：writing-skills の雛形の最低の版（skillOverrides・allowed-tools・`${CLAUDE_SKILL_DIR}`）と、Stop フックの `last_assistant_message` の版を facts に足せば、min_version_fact を使える

## 道具の呼び出し

約 75 回
