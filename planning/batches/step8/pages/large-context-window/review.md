# review.md：large-context-window（検証と直し）

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #what-to-stop の判断例の理由 | 「次の節で述べる」は節単独で読むと指すものが不明（U3） | 「理由は『続けること』の節にある」に直した |
| 2 | 軽い | #cost-of-long-context の「料金の仕組み」 | 値を書かず current-models へ送るだけで薄い | 直さない（facts の id がなく、write.md の判断どおり） |
| 3 | 軽い | #what-to-keep の合図・手順 | リンク中心で本文が薄い | 直さない（持ち主のページを指す方針に合う） |
| U6 | 問題なし | 全体 | write.md の対応（effects・what-to-stop・what-to-keep・cost-of-long-context・misconceptions）は本文と合う。pitfalls は空で名指し不要。図なしでも広い机・受験者の比喩が文章にある | 直し不要 |

U1〜U5・U7〜U10 は問題なし（タブは surfaces と一致、判断例は 4 行で答えを伏せていない、演習なし）。

## 検査の結果
- check_page.py（直した後の 1 回）：エラー 0・警告 2（no-doubled-joshi。write.md と同じ 2 件。link の題名が入る文で誤検出に近い）

## stage
- 直したので draft のまま

## メインに判断してほしいこと
- 窓の大きさや長い入力の単価の facts の id を足すなら、費用の節に目印を置ける

## 使用量
- 道具の呼び出し 6 回、Web の取得 0
