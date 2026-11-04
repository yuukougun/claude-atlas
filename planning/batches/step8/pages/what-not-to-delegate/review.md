# review.md：what-not-to-delegate（分かりやすさの検証と直し）

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | verifiable-axis 末尾 | 「この軸」が分ける軸と五つの軸で紛れ、link 題名と「5 つの軸」が重複（U3） | 「欠ける軸があれば、その部分は人が受け持つ」に書き換え |
| 2 | 直したほうがよい | what-to-delegate ICFP | ShinkaEvolve が未定義（U5） | 「進化的探索でコードを改良する道具」を添えた |
| 3 | 軽い | 判断例・what-it-prevents | textlint の助詞重複・「も」重複 | 3 件を言い換えて解消。残り 2 件（51 行の「に」、104 行の「に」）は意味が崩れるため残した |
| 4 | 軽い | what-to-delegate の表 | 直前の節と内容が重なる（U4） | 直さず。表は目次の図の案（二列の表）で、残した |
| U6 | 合格 | 全体 | write.md の対応は本文と合う。principle は what-it-prevents、prevents は同節 2 段落目、pitfalls は箇条 2 つ。「何が起きるか」は独立の節がないが、what-it-prevents の冒頭で持つ | なし |

U1・U2・U7・U8 は問題なし（判断例は 4 行で答えを伏せていない。タブは不要）。

## 検査の結果
- 直した後：エラー 0・警告 2

## メインに判断してほしいこと
- who-adopted の AtCoder World Tour Finals 2026 の箇条は報道の題名ベース（write.md のとおり）。research/25 P1 との照合が要る
- 「考察の出どころが AI であることは、すでに起こりうる」は報道からの推論として強め。照合の結果で弱めるか削る

## 使用量
- 道具の呼び出し：Read 5、Bash 2、Write 1。Web の取得：0 回
