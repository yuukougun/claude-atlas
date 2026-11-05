# format-cheatsheet 執筆報告

## 書いたファイル
- `docs/contest/format-cheatsheet.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections に `overview`（七つの形式の早見表）を先頭へ追加。既存の anchor は変えず）
- 雛形・図・`data/sources.d/` は作っていない（templates の案なし。sources なし）

## 必ず持つものの対応
- 表とリンクが本体：`#overview`（早見表 2 枚）・`#why-formats-differ`（5 つの軸の表）。各形式の節 `#algorithm` `#heuristic` `#performance-tuning` `#ctf` `#data-analysis` `#hackathon` `#battle-and-team` が持ち主のページへのリンクを持つ
- level なし・sources 任意：どちらも置いていない

## メインに判断してほしいこと
- 規則の列：方針 A4（類型だけを数値ファイルから出す）に対し、`contest-ai-rules` の表の個別セルを目印で埋め込む仕組みがない。そのため類型は書かず、「規則で確かめること」の列と、competition-rules#rules-by-type へのリンクにした。セル単位の目印（例：`fact-cell`）が欲しいか
- 「一つの表」は、読みやすさ（スマホ）のため、早見表を 2 枚（AI・人・評価器／規則・当日の注意）に分けた
- `overview` 節を足した。不要なら外してよい
- 費用の上限の一文（`#why-formats-differ`）は、費用の数値を書かず一般論にした。数値は ai-in-contests-today が持つ想定

## 提案
```yaml
frontmatter:
  - {id: format-cheatsheet, key: sections, before: [7 節], after: [overview を先頭に追加した 9 節], reason: "早見表を 1 節で先に引けるようにした"}
```

## 検査の結果
- 1 回目：エラー 0・警告 7 → 直した後：エラー 0・警告 1
- 残した警告：41 行目の「が」の重なり（要点の「AI が効くところ・人が握るところ」の並列。言い換えると読みにくくなる）

## 確かめていないこと
- 事実は束の調査資料の写しに基づく。一次資料は開いていない（Web の取得 0 回）。表の「AI が効くところ」「人が握るところ」は 11 第1節（p12#53〜#62）の整理で、形式を比べた定量研究はない（根拠：中）
- 5 つの軸の表の各セルは、束の 10 第2章の表と事例からの見当で、独立に確かめていない
- 本文に出典（sources）を付けていない。研究の数値（Airbnb CTF、Battlecode など）は、ai-in-contests-today などの持ち主に任せて書かなかった
- 各リンク先の節が公開後も残るか、手書きのリンク文が題名と合って読めるかは、生成後に未確認

## 使用量
- 道具の呼び出し：約 13 回（Read 2、Bash 5、Write 2、Edit 7 を含む合計）。Web の取得 0 回、check_page.py 2 回
