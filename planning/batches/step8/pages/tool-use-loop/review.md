# review.md：tool-use-loop

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | 要点 | 「何が分かるか」が summary の後半（指示でなく設定で縛る）を欠く | 1 文足した |
| 2 | 直したほうがよい | #client-and-server | 「server tool の分にも呼び出し側が関わる」が何を指すか読者に分からず、未確認の主張でもある | 公式の Stop reasons を見る、の案内に絞った |
| 3 | 直す | #forcing 判断例 | 「strict で寄せる」は呼ぶ頻度に効かず、選んだものと理由が噛み合わない | 呼ぶ頻度は説明と軽い一文、形は strict、と分けた |
| 4 | 軽い | #client-and-server の compare 表 | 2 行とも自分のページへの自己リンクで、読者には紛らわしい | 直さず（生成の目印の中。write.md の判断事項と同じ） |
| 5 | 軽い | 全体 | no-doubled-joshi の警告 6 | 直さず（意味が通る。write.md と同じ理由） |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う。要点の最初は「何が分かるか」、principle・prevents は #what-it-helps で名指し、pitfalls は front matter に値なし。構成は目安どおり | - |

## 検査の結果
- check_page.py を直した後に 1 回：エラー 0・警告 6（上記 5）

## メインに判断してほしいこと
- compare 表の自己リンクを許容するか、表を外すか（write.md と同じ）
- 直したので stage は draft のまま

## 使用量
- 道具の呼び出し：約 8 回（Web の取得 0 回、check_page.py 1 回）
