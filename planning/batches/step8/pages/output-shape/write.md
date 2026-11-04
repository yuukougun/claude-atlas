# write.md：output-shape（執筆）

## 書いたファイル
- docs/prompting/output-shape.md（stub から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（節を 3 つ足した：where・effects・limits。既存の mirror・length・guaranteed は残した）、`sources`（既存の 4 件：api-docs-prompting-best-practices・api-docs-structured-outputs・hc-styles-to-skills・hc-personalization）、`stage`、`updated`
- snippets/output-shape/ の prose-answer・length-and-form・work-summary（各 .txt と .expect.yaml）。目次の templates は「なし」で、分かりやすさのために 3 つ足した
- data/sources.d/output-shape.yml は書いていない（新しい出典なし）

## 必ず持つものの対応
- どの原理に関わるか（`principle`＝見せる）：#effects（「何に効くか」の冒頭で名指し）
- どの原因に関わるか（`prevents`＝見えていない・合っていない）：#effects（2 項目に分けて名指し）
- `pitfalls`：front matter に値がないため持たない（#limits が効かない場面を扱う）
- level（整える）：front matter。要点の最初は「何が分かるか」
- 技法の構成：Before/After は #mirror、何が変わるかは #mirror の後半、なぜ効くかは #effects、効かない場面は #limits

## メインに判断してほしいこと
- 節の順は mirror → length → where → guaranteed → effects → limits。技法の目安（なぜ効くか）が終盤に来るので、入れ替えたほうがよいなら指示がほしい

## 提案
なし（データ・用語集への提案はない）。

## 検査の結果
- 書き終えた後：エラー 1（`system prompt` は prh でシステムプロンプトに）、警告 7。直した後：エラー 0・警告 3
- 残した警告 3（助詞「に」「が」の重複：#where の末尾の文、#effects の「合っていない」の項、#limits の例の項）。意味は通り、直す重さは軽い。検査は 2 回使い切ったので直していない

## 確かめていないこと
- 3 つの雛形の動作（expect は観察の記述で、実機では試していない）
- 長さは「読み手と用途、段落や文の数で示すほうがずれが少ない」とした点は、この辞典の推奨と明記した推論で、公式の根拠はない
- アプリのスタイルのメニューが今も出るかは、束のとおり未確認と書いた
- Claude Code の出力スタイルと CLAUDE.md の分担、structured outputs の使い方は、持ち主のページを指しただけで、本文で確かめていない
- 生成の目印（feature・link・references・page-links）の間は gen_site が埋めたもので、手を入れていない

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 5、Write 8、Edit 7）。Web の取得：0 回
