# write.md：read-specs-yourself

## 書いたファイル
- docs/recipes/read-specs-yourself.md（stubs から mv。stage を stub から draft、updated を 2026-11-05 に。sections に guard・overall-check・when-it-fails を足した。既存の 3 anchor は変えず）
- snippets/read-specs-yourself/：compare-summary（prompt）・scoring-code（prompt）・reading-memo（other）と、それぞれの .expect.yaml
- data/sources.d/read-specs-yourself.yml は作っていない（sources は空のまま。下の「確かめていないこと」）

## 必ず持つものの対応
- 手順：read-first（自分で読んで要約）→ misreading-detector（AI に突き合わせさせる）→ check-by-scoring（採点の処理で確かめる）。各節の末尾に「終わりの確かめ」
- 確かめる・縛るのページへの道：guard（fact-checking#quotes・fact-checking#summaries・summary-overgeneralization#why・think-before-asking#self-first）。前提に fact-checking と summary-overgeneralization。check-by-scoring に tests-first#review-test-changes・tests-first#steps
- 構成の目安：要点 → guard（先に整える守り）→ 手順 3 節 → overall-check（確かめ方）→ when-it-fails（失敗したとき）
- level：整える（front matter のまま）

## メインに判断してほしいこと
- 研究（要約の一般化・LLM のコードの誤りの類型など）と競技の事例は、出典を sources.d に作らず本文に載せなかった。載せるなら出典の登録（arXiv 2種・競技者の記事）と check_noai の確認が要る。研究の数値は前提の summary-overgeneralization が持つため、重複を避けて link に任せた
- 競技の部分は人名・個人の事例を出さず、kyopro-atlas は平文の名前で触れただけ（リンクは付けていない）。リンク形式の指定があれば直してほしい

## 提案
- なし（用語集・data・front matter への提案はない）

## 検査の結果
- check_page.py を 2 回流した。最終はエラー 0・警告 2
- 警告 1（55 行目、助詞「に」の重複）：リンクの題名（「…AI には問い・反論・道具を頼む」）が原因の誤検出。本文側は直したが題名は生成されるため残る
- 警告 2（219 行目付近、助詞「が」の重複）：「うまくいかないとき」1 項目目の文。2 回目の検査の後は流せないため直していない。検証の担当が直すか、残すか判断してほしい

## 確かめていないこと
- 雛形（compare-summary・scoring-code・reading-memo）の動作は実行して確かめていない
- 競技の読み方の部分は、材料の束の記述（実践・章：中）に基づく。一次資料は開いていない（Web の取得 0 回）
- 「先に自分で要約する」順序の効果を比べた研究は確認していない（本文に類推と書いた）
- Claude Code 以外の OS・IDE 拡張の動作は未確認（本文にも書いた）

## 使用量
- 道具の呼び出し：約 12 回（Read 3・Bash 5・Write 8 を含む）。Web の取得 0 回
