# review.md：why-prompt-caching

## 指摘の表
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #what-happens の表 | effort を変えると「全部を読み直す」とあるが、#effects の API では messages だけが外れるとあり食い違う | 「その分を読み直す」にした |
| 2 | 直したほうがよい | #what-happens の判断例 | 「選んだもの」が迷う候補のどちらを選んだか曖昧 | 「区切りまで進めてまとめて切り替える。どうしても要るときだけすぐ上げる」にした |
| 3 | 直したほうがよい | #effects のタブ Claude Code | 「cost の分野のページを引く」で行き先が不明 | what-uses-up-limits#find-what-uses-it の link にした |
| 4 | 軽い | U6 | 対応表と本文は合う（principle・prevents は #effects、積み木の図は #why、構成の並びも目安どおり。pitfalls は値なし） | 直し不要 |
| 5 | 軽い | U1〜U5・U7〜U10 | 冒頭は用が足り、各節は単独で通じる。タブは surfaces と合う。判断例は 4 行 | 直し不要 |

## 検査の結果
- check_page.py（直した後の 1 回）：エラー 0・警告 0
- stage：直したので draft のまま

## メインに判断してほしいこと
- write.md の数値の提案（寿命・読み取りの倍率）を facts に入れるか。入れれば #what-happens と #why に目印を置ける

## 使用量
- 道具の呼び出し 8 回、Web の取得 0 回
