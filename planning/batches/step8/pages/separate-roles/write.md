# write.md：separate-roles（concept・team）

## 書いたファイル
- docs/team/separate-roles.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に 4 節を追加。既存の against-sycophancy は維持）
- snippets/separate-roles/critic-request.md と .expect.yaml（疑う人の依頼の雛形。kind: prompt）
- docs/img/separate-roles/roles.svg（三つの役割の図）

## 必ず持つものの対応
- 原理・原因との結び付け（principle 握る・確かめる、prevents 確かめていない、pitfalls 3 つ）：#effects
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens → #roles（図付き）→ #against-sycophancy → #effects → #limits（誤解を含む）。関連はテンプレートが出す

## メインに判断してほしいこと
- sources が空のまま。研究（過度依存のメタ分析、迎合、固執のエスカレーション）の印は、研究名を本文に書かず、持ち主のページ（over-reliance・agreement-is-not-evidence）を指して付けた。出典を足すなら sources の提案が要る

## 提案
- なし（front matter・用語集・data への提案はない）

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告 6（no-doubled-joshi 5、sentence-length 1）。link の目印の間に入る長い題名が原因の行（76 行）を含み、残した

## 確かめていないこと
- 雛形（critic-request）の動作は未確認
- 一次資料は開いていない（Web の取得 0 回）。研究の強さの印は、束の research/24 §2.3 の写しによる
- 「チームの人どうしの批評が迎合を減らす」「役割の割り方で結果が変わる」を直接調べた研究は見つけていない旨を本文に書いた（類推・推論）
- 未公開ページ（risk-tiered-approval など）の link の表示は、公開時に変わる

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回
