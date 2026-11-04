# 検査の層の試験の置き場所（tests/tools/test_check_pages.py など）

エラーも警告も出ない小さな置き場所。試験は一時フォルダに写し、本物の schema/（site.yml・keys.yml・*.schema.json）を
足してから、1か所だけ変えて、出るはずの指摘だけが出ることを確かめる。値はすべて作りもので、URL は example.* だけ。

- docs/：how-to-use（guide・draft）・request-vs-lock（concept・reviewed）・instructions-ignored（symptom・draft）・
  completion-check（recipe・draft。nav.yml の exclude_docs で公開から外した試作のページ）と、サイトのトップ
- stubs/：hooks-basics（feature・stub）
- data/：facts（match を持つ sample-limit）・features・names・sources（example.org は noai: true）・sources.d・advice・inspection
- nav.yml：nav・exclude_docs と、面の表示の名前（extra.ca.surfaces。作る層が書く形）
- request-vs-lock の本文：要点・別名の行・fact の目印・面のタブ（アプリと Claude Code）と、面でないタブの組
- .claude/settings.json：example.org を2つの形で deny に入れる
