# write.md：deleted-something-important（執筆）

## 書いたファイル
- docs/symptoms/deleted-something-important.md（stubs から mv。stage を draft、updated を 2026-11-05）
- front matter で変えたキー：sections（forms・examples・prevention を足した）、sources（10 件。すべて既存の id）、stage、updated
- 雛形・図・data/sources.d は作らない（目次の notes が「雛形はここに載せない」）。目印の組は routes と references のみ

## 必ず持つものの対応
- 診断のチェックリスト（安く確かめる順、人の側の落とし穴）：#diagnosis（縛っていない→境界がない→預けすぎる〔人の側の落とし穴〕）
- 原因ごとの振り分け先（routes）：#diagnosis の末尾の `routes` の目印
- 冒頭の要点：abstract 囲み。構成の目安のうち、よくある形：#forms、判断例：#examples、予防：#prevention
- 目次 notes の初動：#recover（チェックポイントと git で戻せるか・何が戻らないか）

## メインに判断してほしいこと
- 「止める」の項の「復旧のつもりのコマンドが戻せる状態を変えることがある」は、束に出典がない一般的な助言で、「この辞典の推奨」と付けた。不要なら削る
- git の復旧手順（`git restore`・`git reflog`）は束にない一般の知識で、一次資料で確かめていない

## 提案
- front matter の直しの提案はなし

## 検査の結果
- check_page.py：エラー 0、警告 7（no-doubled-joshi。長い箇条の行の誤検出と判断し、直さなかった）。prh の checkpoint は「チェックポイント」に直した

## 確かめていないこと
- アプリでの復旧・権限・サンドボックスの確かめ方は束にないので「未確認」と書いた
- git の復旧手順は実機で試していない。Issue の報告の内容は束の写しのまま
- Opus 4.6 についての記述は束の写し（現行のモデルの傾向ではない）

## 使用量
- 道具の呼び出し 10 回ほど、Web の取得 0 回
