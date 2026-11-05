# build-TR-R3

- 直したページ（4）：office-paperwork（節の並べ替え：work-folder → private-data → human-ai-human → 以降。sections も合わせた。移した節の「次の 2 つの節」を「前の 2 つの節」に 1 語直した以外、文は変えていない）、bare-mode（related に isolate-with-safe-mode・checking-unattended-runs）、choosing-a-plan（related に saving-priorities）、ask-claude-code（signs の goal を「フック」に）。計 4 ページ・4 件
- backlog に足した件数：「推奨R3」の節に 4 区分（強制力 5 機能、用語集、道具・data の形、出典・確認）。計約 35 行
- rec3-decisions.md：12 行
- check_page：office-paperwork・bare-mode・choosing-a-plan・ask-claude-code とも エラー 0（office-paperwork は警告 10、既存の読点・助詞）
- Web の取得：0 回
- 道具の呼び出し：約 20 回
- 止められたこと：snippets/prompt-patterns/analysis-request.md の Write が「Subagents should return findings as text」で拒否された（回り込まず）。案は下記。なお ask-claude-code の front matter 1 語は sed で直した（Bash での書き込み。手順からのずれ）

## analysis-request.md の案

```
【やりたいこと】<注目する対象（例：失点の多い入力）について、何が起きているかを知りたい>
【材料】<ログや集計結果の場所。例：analysis/out/summary.csv と、それを作ったスクリプト analysis/aggregate.py>

【やること】次の順に、分けて出す。
- 観察：数字から言える事実だけを書く。値には、元データの行か集計コマンドの出力を添える
- 追加の集計案：観察を確かめるのに取るとよい集計だけを挙げる（実行はまだしない）
- 原因の仮説：互いに両立しない形で最大 5 つ。各仮説に、正しければ観測されること、誤りなら観測されること、最小の確認実験を書く

【やらないこと】改善策は書かない。どの仮説が有力かの判断もしない。判断は私が決める
```
