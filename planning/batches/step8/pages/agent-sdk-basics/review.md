# review.md：agent-sdk-basics（検証と直し）

## 指摘の表
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #setting-sources のフック段落 | `onFailure` が何かが書かれず「確かめる」だけで、読者が何をすべきか分からない | `onFailure: "block"` の意味（コールバック自体が失敗したとき止める側へ倒す）を書き、Python での可否と版は公式で確かめると明記 |
| 2 | 直したほうがよい | #minimal の末尾 | 「この 3 つが、次の 3 つの節」は、3 つの項目（設定・道具・権限モード）と 3 つの節（設定・権限・課金）が合わない | 設定は次の節、道具と権限モードは「権限と承認」の節、と対応を書き直した |
| 3 | 軽い | #same-and-different の表 | 「設定の読み込み：自動で読む」と、本文の「省略に頼らず指定する」が食い違って見える | 「省略に頼らず指定で決める」に直した |
| 4 | 指摘のみ | 冒頭の要点 | feature 型の「強制力」が要点にない（data の agent-sdk に enforcement がなく、目印を置くと止まる恐れ） | 直さず、メインの判断へ（write.md の提案と同じ） |
| U6 | 合う | 全体 | write.md の対応と本文が合う。tracks・level・節（same-and-different・minimal・setting-sources・permissions・billing・templates・pitfalls・compare）と構成の目安の並びが一致。古くなった助言は台帳の行なしで節なし | 直しなし。強制力のバッジのみ 4 のとおり未確認 |

U1〜U5・U7〜U10 は、上の指摘以外に問題なし（判断例は 4 行で答えが見え、迷う候補も筋が通る。タブは surfaces と合う）。

## 検査の結果
- 直した後の 1 回：エラー 0・警告 4（長い節題の link 展開による sentence-length 3 件、no-doubled-joshi 1 件。write.md と同じ誤検出）

## メインに判断してほしいこと
- 強制力のバッジ（指摘 4）：data の agent-sdk に enforcement を入れるか決める
- stage は draft のまま（直したため）

## 使用量
- 道具の呼び出し：約 12 回、Web の取得 0 回
