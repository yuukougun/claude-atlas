# write.md：explore-a-codebase（執筆）

## 書いたファイル
- docs/recipes/explore-a-codebase.md（stubs から移動。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（guards-first・overall-check・when-it-fails を足した。既存 4 節の anchor はそのまま）、`sources`（cc-docs-common-workflows・cc-docs-best-practices。どちらも data/sources.yml に既にある id）、`stage`、`updated`
- snippets/explore-a-codebase/ に 3 つ（各 .md と .expect.yaml）：trace-flow（目次の案）、recheck-claims、write-map（分かりやすさのために足した）
- data/sources.d/explore-a-codebase.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- 手順：`#broad-to-narrow`（4 段。各段に終わりの印）、`#check-against-code`（確かめる 3 つの手）、`#keep-a-map`
- 先に整える守り（確かめる・縛る）：`#guards-first`（確かめる守り・縛る守り・戻れる状態・読む量の守り）
- 確かめ方（全体）：`#overall-check`
- 失敗したとき：`#when-it-fails`
- 確かめる・縛るのページへの道：前提の fact-checking・choose-what-to-read（冒頭と `#guards-first`）、関連の own-generated-code・how-much-understanding-to-keep・uses-nonexistent-apis・fix-a-bug（`#check-against-code`・`#overall-check`・`#when-it-fails`）
- level：整える（front matter）

## メインに判断してほしいこと
- `#guards-first` で plan mode を「編集を止めたまま調べさせる手」と一言だけ書いた（束に plan mode の説明の節がなく、suggest-or-do ページの言い回しに合わせた）。plan mode の使いどころの節は束の「指せる節」にないため link していない。確かめる担当に、この一言の正確さを見てほしい
- `#when-it-fails` の「繰り返し合わないときは、新しいセッションで範囲を狭めてやり直す」は、束の材料に根拠がない実務上の助言（推論）。残すか削るか判断してほしい

## 提案
- なし（数値の提案なし、front matter の提案なし、用語集の提案なし）

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 1（textlint no-doubled-joshi）→ 直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形 3 つの動作（実際のリポジトリで流していない。expect は予想）
- plan mode が編集を止めるという記述、Claude Code で `claude` をルートから起動して進めるという記述は、束の材料（Common workflows の要約）と既存ページの言い回しに頼った。公式の原文は開いていない
- 「型のあるコードベースでは言語サーバーで定義へ飛べる」は、束の related の要約に基づく
- 用語集の語の最初の出現を link していない（サイトの用語集の id を束で確かめられなかったため）

## 使用量
- 道具の呼び出し：約 10 回（Read 2、Bash 4、Write 7 を含む）。Web の取得：0 回
