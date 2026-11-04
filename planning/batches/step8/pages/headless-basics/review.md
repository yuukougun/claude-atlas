# review.md：headless-basics

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #minimal | 「出力の形式を足す」とあるのに例に `--output-format` がない | 例に `--output-format json` を足した |
| 2 | 直したほうがよい | #output-and-exit-codes | 「次の節で扱う」は節を単独で読むと指す先が分からない | 「この下の『許可と権限モード』の節で扱う」にした |
| 3 | 直したほうがよい | #billing-path | 「忘れるのが典型である」の主語が欠け、鍵がない場合との対比も曖昧 | 「鍵がなく」を足し、典型の原因を明示した |
| 4 | 軽い | #output-and-exit-codes | 「実行の中で起きた失敗は標準出力に出る」の具体例が少ない | 事実確認が要るため直さず |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う。強制力（permission-modes の値を要点で指す）・tracks・構成の目安（#when #minimal #templates #pitfalls #compare #outdated）・level を確認。目次の 5 節は目安の間に置かれ、理由は妥当 | - |

## 検査の結果
- `check_page.py headless-basics`：エラー 0・警告 0

## メインに判断してほしいこと
- stage は draft のまま（直しを別の担当が確かめていないため）

## 使用量
- 道具の呼び出し 8 回ほど、Web の取得 0 回
