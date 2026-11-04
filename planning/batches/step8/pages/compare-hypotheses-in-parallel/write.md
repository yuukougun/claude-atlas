# write.md：compare-hypotheses-in-parallel（recipe・delegate）

## 書いたファイル

- `docs/delegate/compare-hypotheses-in-parallel.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections を追加。ほかのキーは変更なし）
- `snippets/compare-hypotheses-in-parallel/compare-procedure.md`、`compare-procedure.expect.yaml`（目次の templates の案 1 件。kind: other、safety: false）
- 出典ファイルと図のファイルはなし（sources は空のまま。Mermaid の図は本文中）

## 必ず持つものの対応

- 手順：`#steps`（各段に「確かめ」を付けた 7 段）。雛形は `#template`
- 確かめる・縛るページへの道（前提か関連。比例則）：`#guards`（experiment-log#hypothesis-first・experiment-log#verifier-version・decide-when-to-quit#write-criteria-first・open-ended-loop-trap・humans-set-the-parallel-limit#mainline-vs-scouting・parallel-with-worktrees#per-worktree-setup を link）。前提の 2 つは要点の「前提」と front matter。関連は `#check`・`#when-it-fails` でも指す
- level：front matter の「仕組みにする」のまま
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：`#guards`・`#steps`・`#check`・`#when-it-fails`。雛形の `#template` を手順と確かめ方の間に足した

## メインに判断してほしいこと

- 要点の項目名を、型の既定の形から変えた（「決めるのは人」を足した）。仮説・物差し・採否は人が決める、という catalog の notes（requirements §6.3）を要点に出すため
- 「失敗したとき」に症状ページへの振り分けはない（routes が空で、束に症状ページがない）。当たった形ごとに、指せる節へ送った

## 提案

- front matter、用語集、data への提案はなし
- 根拠の印は付けていない。「負けた案は取り込まないので衝突の解決が要らない」は仕組みから言えることとして書いた（catalog の根拠は「実践（章:中）」）。印が要るなら、メインが付ける

## 検査の結果

- `check_page.py` を 2 回流した（書いた直後、直した後）。2 回目はエラー 0・警告 2
- 残した警告：44 行目 max-ten（導入の 1 文目の読点が 4 つ以上）。181 行目 no-doubled-joshi（太字の見出しと本文で助詞「に」が重なる）。どちらも文の形の指摘で、誤検出ではない。直した後に流せる回数を使い切ったため、検証と直しの担当に任せる
- 1 回目の警告（二つ、助詞の重なり 5 件）は直した

## 確かめていないこと

- 雛形の git コマンドと評価器（`../eval/evaluate.sh`）は実機で動かしていない
- `git worktree list` の出力で基点が同じと読み取れる、という確かめは、実機では見ていない
- Mermaid の図の見た目と、スマホでの表の表示は見ていない
- Web の取得はしていない。本文の事実は束の材料（調査資料の写し）と、つながるページの要約に基づく

## 使用量

- 道具の呼び出し：約 12 回（Read 3、Write 4、Bash 5 前後）。Web の取得：0 回
