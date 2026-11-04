# BF1 報告

1. context-rot：誤解3項目目に（推論・実践例なし）を付けた。
2. define-done：stop-and-report 冒頭の一文に（推論・実践例なし）を付けた。
3. not-what-i-meant：研究の段落を2文に縮め、仕組みは brief-a-new-colleague を link の目印で指した。
4. replies-in-english：29件・10件・16件・0%・33%・0.4%→4.2% を本文から外し「複数の報告がある（2026-11-03 の確認）」にした。根拠の印は残した（参考の issue 題名は原題のため数字が残る）。
5. sycophancy：公刊版（DOI 10.1126/science.aec8352）の出典は、doi.org が anthropic-ai を robots で断る（check_noai の判定）ため資料にできず、science.org は調査資料でも403で読めていない。よって本文を査読前の版の値（約50%・実験2本・N=1604）に合わせ、「査読前の版の値」と明記した。sources は arxiv-2510-01395 のまま。公刊版の値を使うかは作者の判断に残る。
6. tokens：「Claude 4.7 以降」を「新しい世代のモデル」にした（2か所）。
7. where-to-put-instructions：公式の memory の文書で確かめた。ユーザー単位 CLAUDE.md（~/.claude/CLAUDE.md）とプロジェクトの CLAUDE.md は合う。スキルは on demand と記述があり残した。Styles の行は文書で確かめられないため削った。sources に既存の cc-docs-memory を足した（sources.d は不要）。
8. six-causes：手書きの表を gen:begin/end causes に替え、前後の文を直した。生成は未実行（空の目印）。
9. related：brief-a-new-colleague に where-to-put-instructions、fact-checking に3つ、six-causes に6つ足した（すべて目次にある）。

check_page.py：全10ページ エラー0（six-causes は警告19、ほかは0〜4で、既存の語の警告）。
Web取得：1（code.claude.com/docs/en/memory）。check_noai：2回。道具の呼び出し：約15回。
