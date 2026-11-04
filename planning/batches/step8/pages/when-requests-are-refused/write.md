# write.md：when-requests-are-refused

## 書いたファイル

- docs/safety/when-requests-are-refused.md（stub から移して draft。stage=draft・updated=2026-11-05）
- front matter で変えたキー：sections（effect・misconceptions を足した。既存の 3 つは変えず）・sources（8 件。すべて data/sources.yml にある id）・stage・updated
- planning/batches/step8/pages/when-requests-are-refused/facts-proposal.yml（数値の提案）
- 雛形・図・data/sources.d は作っていない（目次の templates と visual が「なし」。Before/After は本文に置いた）

## 必ず持つものの対応

- 冒頭の要点（何が分かるか・いつ引くか・前提）：冒頭の囲み
- 原理 principle「見せる」と原因 prevents「見えていない」を名指す：effect（pitfalls は空）
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：by-surface（何が起きる・なぜ）→ official-steps（手段と Before/After・判断例）→ effect（何に効くか）→ why-not-evade → misconceptions → 関連はテンプレート
- level：使う（front matter のまま。要点の最初は「何が分かるか」）

## メインに判断してほしいこと

- 変わりやすい値は本文に手で書かず、言い方を避けて数値の提案にした（既定の有効・版・表示の文・分類の名前・課金・対象のモデル・検証の制度の段階）。本文に目印を置く場合の場所は used_in に書いた
- Settings > Capabilities と /config の項目名は、日付（2026-11-04 時点）付きで本文に書いた。名称の扱いとして不要なら外す
- Life Sciences Verification Program は束の材料（research/26）が出典。data/sources.yml に該当の id がなく、本文は出典の id で指していない。出典の追加を提案する

## 提案

- sources：Life Sciences Verification Program の公式の記事を data/sources.yml に足す（URL は未取得）
- 数値：facts-proposal.yml のとおり

## 検査の結果

- 1 回目：エラー 3（prh の skill・subagent・output style）。2 回目（直した後）：エラー 0・警告 1
- 残した警告：ja-technical-writing/no-doubled-joshi（89 行目の「誰の環境か・どの範囲か・何のためか」の並べ方）。列挙なので誤検出と考え、検査の回数の上限のため直していない

## 確かめていないこと

- 本文の事実は束の材料と、利用ポリシーの 1 回の取得（禁止の文言・警告や停止がありうること・止められただけでは違反を意味しないこと）による。公式の記事そのものを開き直してはいない
- 他のページとのリンクの表示（目印の間は道具が書く）と、節 anchor の存在は check_page に任せた
- Before/After の After が実際に止まらなくなるかは試していない（効く保証はない旨を本文に書いた）
- Claude Code 以外の OS・IDE 拡張の動作は扱っていない

## 使用量

- 道具の呼び出し：約 14 回（Web の取得は 1 回）
