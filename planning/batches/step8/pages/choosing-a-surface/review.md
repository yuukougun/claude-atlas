# review.md：choosing-a-surface

## 指摘の表
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | examples の 1 つ目の理由 | 「固まったら、…育てるなら、Claude Code へ」で条件が重なり読めない | 「固まり、…育てたくなったら」に直した |
| 2 | 直したほうがよい | when-to-build-with-api の導入 | 「足りることは多い」は根拠がない断定 | 箇条のうち最初の 2 つが API 不要の例、3 つ目が API の出番、という説明に直した |
| 3 | 軽い | compare-surfaces | 手書きの 3 軸の表と compare の表の二重（write.md の判断事項） | 直さず。メインの判断に回す |
| U6 | 確認済み | compare-surfaces / examples / combine | write.md の対応と本文が一致。比較の表・判断例・選び方・組み合わせ方・level がある | 直し不要 |

U1〜U5・U7〜U10 は問題なし（タブは不要、判断例は 4 行で答えを伏せていない）。

## 検査の結果
check_page.py：直した後 1 回、エラー 0・警告 0。

## メインに判断してほしいこと
- 手書きの 3 軸の表を残すか（write.md の提案どおり、catalog の tracks に claude-code・api の機能を足せば compare で置き換えられる）。

## 使用量
道具の呼び出し：約 10 回（Read 6・Edit 3・Bash 1・Write 1）。Web の取得：0
