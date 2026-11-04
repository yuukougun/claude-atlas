# write.md：permission-to-stop

## 書いたファイル
- docs/prompting/permission-to-stop.md（stub から移した。front matter は `sources`（api-docs-prompting-best-practices・arxiv-2510-20270。どちらも data/sources.yml にある）・`stage`（draft）・`updated`（2026-11-05）だけ変えた）
- snippets/permission-to-stop/stop-conditions.md と stop-conditions.expect.yaml（目次の templates の案。10 付録 A-3 の「禁止」節は使わず、止まる条件の数行だけ）
- data/sources.d/permission-to-stop.yml は作っていない（出典は既存の id で足りた）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`・`prevents` を名指しする）：#with-structure（「縛る」「確かめる」と「縛っていない」「確かめていない」を名指し）
- `pitfalls`：front matter に無いので持たない
- level を持つ／要点の最初が「何が分かるか」：冒頭の要点の囲み（level は front matter の 任せる）
- 技法の構成（頼み方の例 Before/After → 何が変わるか → なぜ効くか → 効かない場面・やりすぎ）：Before/After と何が変わるか・なぜ効くかは #conditions、効かない場面とやりすぎは #limits

## メインに判断してほしいこと
- 判断例の題「止まる条件を書いた後に、tests/ を守るか」を末尾に置いた（#with-structure）。不要なら外してよい
- 「やりすぎ」の1文は (推論・実践例なし) の印を付けた。根拠の資料がない

## 提案
- なし（数値の提案もなし。54%→9% などは研究の固定の記録として、研究名・年・対象を添えて本文に書いた）

## 検査の結果
- check_page.py 2回：1回目 エラー 0・警告 1（「に」の重複。リンクの題の取り込みで出た）、直した後 エラー 0・警告 0

## 確かめていないこと
- 雛形の動作（expect の観察）は未実行
- 一次資料（ImpossibleBench の論文、公式のプロンプトガイド）は開かず、束の写しに基づく。Claude Opus 4.1 で効果が小さいという記述に数値はない
- 「不正率」の定義の細部は書いていない。現行の Claude モデルでの効きは未確認と本文に書いた

## 使用量
- 道具の呼び出し 10 回ほど。Web の取得 0 回
