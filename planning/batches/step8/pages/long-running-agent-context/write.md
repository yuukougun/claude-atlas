# write.md：long-running-agent-context

## 書いたファイル
- docs/api/long-running-agent-context.md（stubs から mv。front matter で変えたキー：sections〔what-happens・effects・misconceptions を足した。既存の three-tools・external-state は残した〕・sources〔data/sources.yml にある 6 件〕・stage〔draft〕・updated〔2026-11-05〕）
- docs/img/long-running-agent-context/where-each-acts.svg（図。3 手段が文脈のどこに効くか）
- 雛形・data/sources.d は置かない（目次の templates は「なし」。出典は data/sources.yml に既にある id を使った）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle` 見せる・`prevents` 散らかっている）：#effects（本文で名指し）
- `pitfalls`：front matter に値がないため、持たない
- level（回す）：front matter。要点の最初の項目は「何が分かるか」（冒頭の要点の囲み）
- 構成の目安（原理・仕組み）：要点 → 何が起きるか #what-happens → なぜ（図つき）#three-tools → 何に効くか #effects → 誤解 #misconceptions → 関連（テンプレートが出す）。#external-state は判断の節として足した

## メインに判断してほしいこと
- 図は SVG 1 枚（代替テキストあり）。目次の visual の案（static）に沿った
- 「迷う候補」の判断例は、公式の説明（memory tool と compaction の併用の推奨）に沿った筆者の例。研究や実践例の根拠ではない

## 提案
- 用語集：path traversal（保存先のパスが許す範囲の外へ出る攻撃）を短く定義して追加する案。本文では説明なしで使った
- front matter の提案：なし

## 検査の結果
- 2 回流した。最終はエラー 0・警告 1（no-doubled-joshi の「が」。助詞の重なりで、意味が通るため残した。#external-state の memory tool の段落）

## 確かめていないこと
- 事実は束の材料と data の note に基づく。一次資料を開き直していない（Web の取得 0）
- 図の表示（SVG の見え方）はブラウザで確かめていない
- 「道具の結果が溜まると決めたことが目立たなくなる」は、公式の「会話が長くなるほど品質が落ちる」を言い換えた説明で、内部の動きの断定ではない

## 使用量
- 道具の呼び出し：約 16 回。Web の取得：0
