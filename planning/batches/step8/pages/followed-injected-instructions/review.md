# review.md：followed-injected-instructions（検証と直し）

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | #diagnosis 面のタブ前 | 「1 と 3 で」が手順の番号か能力の番号か紛れる | 「診断の手順 1 と 3 で」に直し、同居しやすい能力を見る旨を足した |
| 2 | 直したほうがよい | #diagnosis 手順 2 | 1 項目に条件が詰まり長い | 手順内で改行して区切った |
| 3 | 直したほうがよい | 雛形 trace-origin | 「要る最低の版：Claude Code 2.0.72」は tracks の claude-in-chrome 由来で、どの面でも使える依頼に不適 | expect.yaml に `features: [auto-mode]`（since なし）を足し、版の表示が消えた |
| 4 | 軽い | #diagnosis 手順 1 | 雛形が表の後ろにあり「このあと置く」で遠い | 直さない（小見出しで分かれ、通じる） |
| 5 | U6 | 全体 | write.md の対応（要点・diagnosis・routes・forms/examples/prevent）は本文と合う。人の側の落とし穴は手順 5 にある | 直し不要 |

## 検査の結果
- check_page.py（直した後）：エラー 0・警告 0

## メインに判断してほしいこと
- 指摘 3 の `features: [auto-mode]` は版の表示を消すための回避。雛形の版の既定を、prompt 種では出さない扱いにするか検討してほしい
- write.md の判断（診断の順、GitHub MCP の事例の重さ）は事実の検証の担当に任せる

## 使用量
- 道具の呼び出し：約 6 回。Web の取得：0 回
