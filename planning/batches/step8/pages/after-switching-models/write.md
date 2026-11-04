# write.md：after-switching-models

## 書いたファイル
- `docs/models/after-switching-models.md`（stubs から mv。front matter は `sections`（`before-you-start`・`verify-whole`・`when-it-fails` を足した。既存の 4 つの anchor は変えず）・`sources`（既存の id 12 個）・`stage: draft`・`updated: 2026-11-05` を変えた）
- 雛形（`snippets/after-switching-models/`）：`switch-checklist.md`（kind other。目次の案）・`find-old-settings.sh`（other）・`audit-request.md`（prompt）。それぞれ `.expect.yaml` 付き
- `data/sources.d/after-switching-models.yml`（`sources: []`。新しい出典なし）
- `planning/batches/step8/pages/after-switching-models/facts-proposal.yml`

## 必ず持つものの対応
- 手順：`#checklist`（5 段。各段に終わりの確かめ）と `#remove-one-at-a-time`（部品を外す 5 手順）
- 確かめる・縛るのページへの道：`#before-you-start`・`#checklist`・`#remove-one-at-a-time`・`#verify-whole` から measure-changes・verification-ladder・emphasis-words・claude-md-length を link で指す。フックと deny ルールは「外さないもの」として `#remove-one-at-a-time` に一言
- 構成の目安：要点 → `#before-you-start`（先に整える守り）→ `#checklist`・`#api-parameters`・`#remove-one-at-a-time`（手順）→ `#verify-whole`（確かめ方）→ `#when-it-fails`（失敗したとき）。`#retirements-and-default-changes` は引き金の節
- level：任せる（front matter のまま）。比例則は `#before-you-start` の「任せる幅」で触れた

## メインに判断してほしいこと
- 退役の日付・既定の値・API の版は変わりやすいので本文に書かず、台帳・年表・公式の文書への link に任せた。提案の fact を数値ファイルに入れたら、`#retirements-and-default-changes`・`#api-parameters` に目印で足せる
- `#api-parameters` の表は、台帳の行の説明を繰り返さず、エラーの出方 → 引数 → 台帳の行の引き方にした。モデルの名前（Opus 5 など）は、変わりやすいので本文に出さず、台帳の add-double-check に任せた。読者に不親切なら、names か fact の目印で足す案を出してほしい
- front matter の提案はなし

## 提案
- 数値の提案：`facts-proposal.yml`（4 件。`/doctor prompt-audit` の最低の版は今日 Commands の文書で確かめた。ほかは束の調査資料の値で、確認日は 2026-11-04 のまま）
- 用語集・prh への提案：なし

## 検査の結果
- `check_page.py`：1 回目 エラー 0・警告 6（助詞の重なりと「一つ」）→ 直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- `/claude-api migrate` などの下位コマンドの中身（Commands の文書に名前だけ見えたが、何をするかは読まず、本文にも書いていない）
- アプリで旧いモデルの会話の続きを置き換え先が答える点は、束の research/22 #23 の要約に基づく。ヘルプセンターの原文は開いていない
- 「一度に大きく削ると、どの部品が効いていたか分からなくなる」は論理として書いた。11 の p34#144 が指す元の報告は開いていないので、根拠の印も出典も付けていない
- 台帳の行の anchor（`outdated-advice-ledger#budget-tokens` など）がレンダリングで正しく解決するかは、check_page の通過までしか見ていない
- 雛形の動作（スクリプトの出力、依頼の返答）は試していない
- Claude Code 以外の OS・IDE 拡張での `/effort status` の動作は未確認

## 使用量
- 道具の呼び出し：約 14 回（Read 3、Bash 6、Write 約 10 を含む）。Web の取得：1 回（Commands の文書。事前に check_noai.py で確認）
