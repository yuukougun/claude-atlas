# write.md：product-map（hub・start）

## 書いたファイル
- `docs/start/product-map.md`（stub から移した。stage: draft、updated: 2026-11-05。front matter で変えたキー：`sources` 4 件、`sections` 5 節、`stage`、`updated`）
- `docs/img/product-map/map.svg`（面を横、層を縦に置いた静的な地図。文字はテキスト、400x290）
- `stubs/start/product-map.md` は削除（移動）。雛形・`data/sources.d/product-map.yml` は作っていない（目次の templates なし、新しい出典なし）

## 必ず持つものの対応（hub：表とリンクが本体）
- 表：`#surfaces`（面の表）・`#layers`（層の表）・`#find-by-trouble`（困りごと→分野の表）・`#where-next`（知りたいこと→ページの表）
- リンク：上の各表の行き先は link の目印。分野の入口は `field:` の目印（`#find-by-trouble`）
- level：持たない型。`sources` は任意で 4 件付けた

## メインに判断してほしいこと
- `#identify-surface` の見分けの手がかり 4 項目（`claude` コマンド・Messages API・チャット画面・Office のサイドパネル）は、束の材料からの言い換えで、一次資料では確かめていない。載せるか確認してほしい
- 旧称の読み替え 3 件（Claude Code on the web・Claude in Slack・Claude Code SDK）の旧称は手で書き、今の名前は name の目印にした。旧称の手書きが方針に合うか確認してほしい

## 提案
- なし（数値・用語集・front matter の提案はない）

## 検査の結果
- `check_page.py product-map` を書き終えた後に 1 回：エラー 0・警告 0（直しの再検査は不要だった）

## 確かめていないこと
- 面の表と層の表の短い説明は、束の要約・つながるページの要約に基づく。一次資料は開いていない
- 図の見た目は目で確かめていない（検査は通っている）
- 名前の目印の間に入る語が、文の流れで自然に読めるかは、生成後の表示を見ていない
- 図の「周辺製品」が層の重なりの対象かどうかは設計上の案（目次の visual）に従った

## 使用量
- 道具の呼び出し：約 11 回（読み 3、確認 Bash 5、Write 3 など）。Web の取得：0
