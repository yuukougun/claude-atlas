# write.md：before-using-top-model（concept・cost）

## 書いたファイル
- `docs/cost/before-using-top-model.md`（stubs から削除して移した。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（what-happens・what-it-prevents・misconceptions を足した。既存の which-limit・when-worth-it は変えず）、`sources`（hc-fable-models-plan ほか 6 件。すべて sources.yml にある）、`stage`、`updated`
- 雛形・図・`data/sources.d/before-using-top-model.yml`：なし（目次の templates・visual が空。新しい出典もない）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- どの原理・どの原因に関わるか（`principle` 確かめる・`prevents` 合っていない を本文で名指す）：#what-it-prevents
- level を持つ：front matter `level: 整える`
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens（例）→ #which-limit・#when-worth-it（なぜ・判断）→ #what-it-prevents → #misconceptions → 関連はテンプレート。「なぜ」は公式が理由を書かないため、比喩付きの図は置かず、#what-happens に「理由は公式が説明していない」と書いた

## メインに判断してほしいこと
1. 公式の食い違い（research/26 #22 の続き）：Fable の記事は「別の週の上限はなく、通常の週の上限の内側」と書く（2026-11-05 に WebFetch で確認）。Max・Ultra の記事と facts の `usage-limit-types-by-plan`・features の `usage-limits` の note は「別の週の上限」と書く。本文は Fable の記事に合わせ、警告の囲みで 3 通りの書き方を並べた。how-usage-limits-work#limit-types の最後の箇条（「Max と Ultra には最上位のモデル向けに別の週の上限がある」）と表の列名の見直しを提案する
2. #which-limit のプラン別の分け方（含まれる／usage credits／API 料金／使えない）を、数値ファイルがないため文の箇条で手書きした。下の提案の表の fact を足したら、箇条を `fact-table` に置き換える
3. 名前の扱い：本文は最上位のモデルの名前（Fable）を aliases の行にしか書かない。用語集に「最上位のモデル」の定義を置くかは任せる

## 提案
```yaml
proposals:
  - fact: {id: top-model-by-plan, title: 最上位のモデルの引かれ先（プランごと）, value: "Max・Ultra・Team と席ごとの Enterprise の premium seat は通常の週の上限の内側（一部まで）。Pro・Team と席ごとの Enterprise の standard seat は usage credits（席ごとの Enterprise は組織が有効にした場合）。使用量に基づく Enterprise と API は標準の API 料金。Free は使えない", sources: [hc-fable-models-plan, claude-pricing, hc-max-plan, hc-ultra-plan], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit, choosing-a-model#plans, choosing-a-plan#plan-table]
  - fact: {id: top-model-weekly-share, title: プランに含まれる最上位のモデルの割合（通常の週の上限のうち）, value: "50%（料金のページは「半分まで」）", sources: [hc-fable-models-plan, claude-pricing], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit]
  - fact: {id: top-model-claude-code-min-version, title: 最上位のモデルを Claude Code で使う最低の版, value: "モデル 5 は 2.1.170、モデル 5.1 は 2.1.255（モデルの世代ごと）", sources: [hc-fable-models-plan], checked: 2026-11-05, status: 確認済み}
    used_in: [before-using-top-model#which-limit]
frontmatter: []
```
- `used_in` の 3 件目の版・割合は、本文に数字を書かず、目印の置き場所だけ #which-limit に想定した。fact が入ったら、割合と版の文に目印を足す
- 正本の更新の提案：facts `usage-limits` の note と `usage-limit-types-by-plan` の「最上位のモデルの別の週の上限」列を、上の食い違いに合わせて見直す

## 検査の結果
- `check_page.py` を 2 回流した。1 回目：エラー 0・警告 5（usage-credits-basics が未公開のリンク警告 2 件＝想定内、textlint の助詞の重なり 3 件）。助詞の 3 件を直した後の 2 回目：エラー 0・警告 0

## 確かめていないこと
- Fable の記事の本文は WebFetch の要約で確かめた（原文の逐語ではない）。ほかの出典（料金のページ、Max・Ultra の記事）は束の写しのままで、今回は開いていない
- Team／Enterprise の standard seat の「一回限りの credit」など、プラン別の細部は本文に入れていない
- 「Settings > Usage」の進捗バーは束の写し（02 §2-2・§2-4）による。Claude Code の `/usage` の内訳の読み方は what-uses-up-limits の持ち分で、確かめていない
- 判断例 2 つは架空の状況で、動作確認はしていない
- 勘定の速さの理由は、公式が書いていないため書かなかった

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 7、ToolSearch 1、WebFetch 1、Write 2 ほか）。Web の取得：1 回
