# write.md：rewind-dont-correct（concept・context）

## 書いたファイル

- `docs/context/rewind-dont-correct.md`（stubs から mv。stage を draft、updated を 2026-11-05）
- front matter で変えたキー：`sections`（`effect`・`misconceptions` の 2 節を足した。既存の why・how・what-is-lost は変えていない）・`sources`（data/sources.yml にある id 7 件）・`stage`・`updated`
- 雛形・図・`data/sources.d/` は作っていない。目次の templates が「なし」で、Before/After は本文の表と、依頼の例の text ブロックで足りるため。図の案（static Before/After）は表で代えた

## 必ず持つものの対応

- 原理（principle：見せる）を名指して結び付ける：`#effect`（「原理で言えば「見せる」にあたる」の段落）
- 原因（prevents：散らかっている）を名指して結び付ける：`#effect`（先頭の段落）
- pitfalls：front matter が空のため、持たない
- level（整える）・要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（技法寄り）の「頼み方の例」：`#why`（表と Before/After）／「何が変わるか・なぜ効くか」：`#why`・`#effect`／「効かない場面」：`#misconceptions`

## メインに判断してほしいこと

- 断られたときの巻き戻し（research/26 §3.3 (b)）は `#how` の末尾に 1 段落で入れた。利用ポリシーを避ける頼み方とは分けて書いてある。置き場所が合うか確認してほしい
- アプリでの編集の詳細（編集後に元の枝が見えるか・戻せるか）は、材料になく、確かめていないので、本文に「画面で確かめる」と書いた。確かめられる担当がいれば書き足せる

## 提案

なし（用語集・data・front matter の他キーへの提案はない）。

## 検査の結果

- `check_page.py` 1 回目：エラー 0・警告 7（助詞の重なりと長文）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと

- アプリでのメッセージ編集の挙動（枝の扱い、後続メッセージの扱い）。材料は「前のメッセージを直して送る」という公式・実践者の言及だけ
- 数値（チェックポイントの保持数・期間）は本文に書いていない
- 巻き戻しの Claude Code の挙動は、checkpointing の公式文書（Web で 1 回取得）に合わせた。WSL・Linux 以外の OS と IDE 拡張の動作は未確認で、本文でも触れていない
- Chroma の研究を会話の訂正に当てはめる所は（類推）と書いた。Claude への当てはまりは確かめていない
- 「根拠：中」の付け方（実践者 3 件の一致）は、ページ内の判断である

## 使用量

- 道具の呼び出し：約 12 回（Read 2、Bash 5、Write 2、ToolSearch 1、WebFetch 1、その他）
- Web の取得：1 回（code.claude.com/docs/en/checkpointing）
