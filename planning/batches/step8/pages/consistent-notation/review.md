# review.md：consistent-notation

| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #glossary 冒頭 | 手順 2 で pattern を使うが定義が雛形の後 | 冒頭の説明に「探す形（pattern）」を足した |
| 2 | 直したほうがよい | #single-source prh 辞書の前 | 括弧が入れ子で、パスを渡す先が読み取りにくい | 文を分けて link を独立させた |
| 3 | 直したほうがよい | #single-source 末尾 | link の題名が入ると「…読ませる（準備中）で必要なときだけ読ませる」と重複する | 文を組み直した |
| 4 | OK | U6 | 手順（glossary・open-kanji・single-source）、確かめる・縛るへの道（guard、prerequisites・related）、level 整える、構成 guard→手順→verify→failure。write.md の対応と本文が合う | なし |
| 5 | 軽い | #verify | specs が読み込みで確かめられる点は prh 仕様の要約に基づく（write.md も未確認と記載） | 直さない（事実の検証の範囲） |

## 検査の結果
check_page.py：エラー 0・警告 0（直した後の 1 回）

## メインに判断してほしいこと
- #5 の prh specs の挙動を、事実の検証役に確かめてほしい。

## 使用量
道具の呼び出し 9 回、Web の取得 0 回
