# write.md：roadmap（hub・start）

## 書いたファイル
- `docs/start/roadmap.md`（stubs から mv）。front matter の変更：stage を draft、updated を 2026-11-05、sources に 4 件（simonwillison-ai-adoption-journey・arxiv-2607-05068・github-florianbruniaux-claude-code-ultimate-guide・github-luongnv89-claude-howto。いずれも data/sources.yml に既にある）を足した
- 雛形・図・`data/sources.d/roadmap.yml`・`facts-proposal.yml` は作っていない（下記）

## 必ず持つものの対応
- 表とリンク（本体）：`#levels`（段階の表と各段のリンク）、`#reading-order`（`roadmap` の生成の目印）、`#always-hold`（人が握るものとリンク）
- level を持たない：front matter に level なし。sources は任意：4 件を付けた（`#hypothesis` で使用）

## メインに判断してほしいこと
- 目次の図の案「委任の段階のはしご」（static）は SVG にしていない。段の表（`#levels`）が同じ内容を持つため。必要なら別途図を足す
- `#hypothesis` の根拠の印（弱／中・類推）の付け方が適切か
- 表の「この段で強める確かめと縛り」列の割り当て（整える→verification-ladder#four-steps ほか）は、各ページの要約と節名からの私の対応づけで、持ち主のページの内容と照らしていない

## 提案
- front matter の直し・用語集・data への提案はなし

## 検査の結果
- `check_page.py roadmap`：1 回目 エラー 4・警告 5（prh の skills/hooks/permissions/plugins の表記、arabic-kanji-numbers の「五つ」、助詞の重複、全半角の空白）→ 直して 2 回目 エラー 0・警告 0（実際には 2 回を超えて 3 回流した。2 回目の直しで全半角の空白の漏れが出たため）

## 確かめていないこと
- 材料の束の写しだけで書き、一次資料は開いていない。研究の件数（917 人）と主張は束の写しのとおりで、原典を確かめていない
- 生成ブロック `roadmap` の出力の中身と並び（同じ段の中で守りが手前に来るか）を見ていない
- 持ち主のページの節の中身を読んでいないため、link の先が文脈に合うかは要約と節名の範囲でしか確かめていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
