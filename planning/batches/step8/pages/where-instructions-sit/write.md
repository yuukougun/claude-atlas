# write.md：where-instructions-sit

## 書いたファイル
- `docs/basics/where-instructions-sit.md`（stubs から mv。stage を draft、updated を 2026-11-05 にした）
- front matter で変えたキー：`sections`（6 節を足した）・`sources`（既存の id 14 件）・`stage`・`updated`
- 雛形・図の SVG・`data/sources.d/where-instructions-sit.yml` は置かなかった（出典は全部 data/sources.yml か他ページの sources.d に既にある id。図は Mermaid 1 つ）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 縛る・見せる、prevents 縛っていない・散らかっている）：`#effects`（3 項目で名指し）
- level 整える：front matter に保持。要点の最初は「何が分かるか」（冒頭の囲み）
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-happens` → `#positions`・`#why` → `#effects` → `#misconceptions` → 関連（page-links）。`#duration` を足した
- 比喩付きの図：`#positions`（Mermaid の並び図）と `#why`（社内規程と口頭の指示のたとえ）

## メインに判断してほしいこと
- `compare` の表（`#duration`）は、アプリの 2 機能の「読み込みの時期」「圧縮で残るか」が null のため「未確認」と出る。data 側で埋められるなら埋めてほしい（埋まらなければ「未確認」のままで読める書き方にしてある）
- ledger の link（`outdated-advice-ledger#important-caps`）は、台帳ページに anchor がなければ止まる。check は通った

## 提案
- なし（数値・用語集・prh への提案なし）。front matter のほかのキーの直しもなし

## 検査の結果
- 1 回目：エラー 0・警告 1（`に` の連続。文を直した）。2 回目：エラー 0・警告 0

## 確かめていないこと
- Web の取得は 0 回。束の材料（research 26・27、05、data の note）だけで書いた
- アプリで指示が会話のどこに入るか、API でメッセージのどこに入るかは、材料に書かれていないので書かなかった（本文でもそう断った）
- API の節は、CLAUDE.md が Claude Code の機能で API に自動の読み込みがないこと（設計から導いた）と、多言語の案内の一文（api-docs-multilingual-support）だけ。API のシステムプロンプトの詳細は未確認
- 「出力スタイルは主の会話では system reminder として届く」「CLAUDE.md が Explore と Plan に届かない」「クラウドのセッションが `~/.claude/CLAUDE.md` を読まない」は research 27 の写し（2026-11-03 確認）。公式の原文は開いていない
- 書く位置・書き方で守られやすさがどう変わるかは、材料にないので比較しなかった
- 比喩（社内規程と口頭の指示）は目次 notes の案を使った。「根が配り直される」の言い方は圧縮の比喩（議事録）との接ぎ方が少し苦しいかもしれない

## 使用量
- 道具の呼び出し：約 14 回（Read 5・Bash 6・Write 2・Edit 1）。Web の取得：0 回
