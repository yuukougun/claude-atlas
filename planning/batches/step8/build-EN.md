# 工程8 EN 報告

## やったこと
- schema/site.yml の enforcements を [お願い, 鍵, モデルの判定, なし] に。語彙の値は日本語そのものなので、tools/gen/config.yml の labels には写す表がなく、足していない（表示は値のまま）。make_schema.py を流し facts.schema.json を更新
- data/facts.yml：effort・mcp・checkpoints・context-window・interactive-mode は「なし」、auto-mode・goal は「モデルの判定」。app-memory は足さない。auto-mode・goal の note の「強制力は書かない」を「強制力は『モデルの判定』」に直した。subagents の note（定義の指示と道具の制限が混ざる）は、決めの対象外なので触っていない
- 強制力を feature の目印に替えたページ：checkpoints-and-rewind・connecting-mcp・effort-levels（「何を止められるか」を「強制力」に）・goal-until-done・what-auto-mode-stops・inspect-context・input-symbols（強制力の行を新設）。verification-ladder は `feature goal/enforcement` の目印で「鍵ではない」に直した
- 数値の目印（facts-placement の行どおり）：checkpoints-and-rewind（保存の数・期間）、connecting-mcp（mcp-output-token-limits）、effort-levels（fact-table と2つの版）、goal-until-done（5つ）、what-auto-mode-stops（block-pause-thresholds）。手書きの「手で書かない」「一定の」等は直した

## 検査
- check_page.py：9ページともエラー0（connecting-mcp・goal-until-done・inspect-context は既存の textlint 警告のみ）。gen の試験は106件中1件が失敗：test_generated_files_are_fresh（生成物が古い。他の担当のページと、目印を置いた私のページの未生成による。メインの gen_site.py で解消）

## 報告・判断
- protect-tests：tracks は permissions・hooks・sandbox（全部「鍵」）。ページに手書きの強制力の行はなく、本文の「お願い」「鍵」は層の名前なので、直していない。要点に強制力の行が要るかはメインが判断
- interactive-mode を tracks に持つページは input-symbols だけ（受け持ち内）
- 語彙の説明の文がある所（メインが直す）：schema/keys.yml:306 の note「強制力（お願いか鍵か。D14）」（SK の担当）、data/facts.yml 冒頭の書き方の例（34行「enforcement: <お願い・鍵>」）、planning/guides/feature.md:25、planning/design.md:351（「強制力（お願いか鍵か）」）、planning/guides/card.md の強制力の説明
- 目印の出力は、生成後に「強制力：なし。…」のように値が入る。goal-until-done・what-auto-mode-stops の続きの文「鍵には数えない。…」は、値が「モデルの判定」になるので重複ぎみ。生成後にメインか検証役が見直すとよい
