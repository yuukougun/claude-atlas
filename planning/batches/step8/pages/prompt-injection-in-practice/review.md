# review.md：prompt-injection-in-practice

| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #channels の要点・API タブ | 「判断の段」が図の外で未定義（断片で読むと通じない） | 「Claude の判断」に言い換えた |
| 2 | 直したほうがよい | #why-detection-fails の三段 | 「公式の立場」が検出の話とつながらず、実践者の「一致」も根拠が不明 | 公式の立場に「検出を提供元に任せきれない」の含意を足し、実践者の幅は束の資料の範囲と明記 |
| 3 | 軽い | #why-detection-fails | 「が プロンプト」の余分な空白 | 削除 |
| 4 | 軽い | #patterns 雛形の使い方 | memo.md という名前が本文に出ない | 直さず（雛形の expect に記載済み） |
| U6 | 問題なし | 全体 | write.md の対応と突き合わせた。principle「縛る」・prevents「境界がない」は #what-works で名指し、pitfalls は空、要点の最初は「何が分かるか」、構成の目安は #channels→#patterns→#why-detection-fails→#what-works→#misconceptions で並ぶ | なし |

U1〜U5・U7〜U10：面のタブは surfaces と一致、判断例は 4 行で答えを伏せていない、薄い節なし。

## 検査の結果
エラー 0・警告 2（直した後の 1 回。「管理を行う」は直さず文言を変えた。130 行の長さは link の目印の間の長い題名で誤検出に近い）

## メインに判断してほしいこと
- write.md の 2 点（事例の書き方の方針 B1、WhatsApp の「確認画面」の記述）は未回答のまま

## 使用量
- 道具の呼び出し 約 8 回、Web の取得 0 回
