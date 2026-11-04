# review.md：request-lock-table

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #table 手書きの表「出力の形式」の鍵の列 | 「鍵の列は強制できる手段だけ」と直前に書くのに、Claude Code の「指示と検査の組み合わせ」（鍵でない）が入っていた | 「API 以外の面では、鍵はなく、指示と検査の組み合わせ」に直した |
| 2 | 直したほうがよい | #where-locks-act の Bash 書き換えの項 | 「別のきっかけ」だけでは何を使うか分からない | 束の写し（FileChanged）で名指しした |
| 3 | 直したほうがよい | #by-surface Claude Code タブ冒頭 | 「6 つの手段の大半」が曖昧で、structured outputs（API）との関係が読めない | 「structured outputs 以外の 5 つ」に直した |
| 4 | 軽い | 要点の「何ができるか」 | 面による違い（summary の後半）が要点にない | 直さない（文字数の上限に近く、導入と #by-surface で足りる） |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う：要点・比較の表（#table の compare）・判断例（#where-locks-act、#choose）・組み合わせ方と確かめ方（#combine）・level（任せる） | － |

U1・U2・U3・U4・U5・U7（タブは アプリ・Claude Code・API で surfaces と合う）・U8（判断例 4 行、答えは伏せていない）・U9 は問題なし。

## 検査の結果
- check_page.py 1 回（直した後）：エラー 0・警告 0

## メインに判断してほしいこと
- write.md の 2 点（Stop フックで言語を確かめる行の扱い、#combine の推論の段落を残すか）は未判断のまま。stage は直したので draft のまま

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0 回
