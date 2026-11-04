# spec-first 検証と直し

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | goal-with-stop-conditions 冒頭近く | 「判定役」が節の中で定義されず、リンク先頼みで断片では通じない（U3・U5） | 「/goal で条件を満たしたかを各ターンの後に判定する役（判定役）」と初出で定義 |
| 2 | 直したほうがよい | goal-with-stop-conditions 末尾 | ほかの手順の節にある「この段の終わりの印」がない（U6 の手順の揃い） | 終わりの印（コマンド出力が会話に出ている、または上限で止まり報告）を 1 文足した |
| 3 | 軽い | mock-first | 根拠が「推論・実践例なし」。必須ページの題名に入る節（write.md が判断依頼済み） | 直さない（メインの判断事項） |
| 4 | 軽い | 警告 6 件 | doubled-joshi 5・max-ten 1。3 件は生成 link の題名入りの行 | 直さない（題名は道具が入れる） |
| U6 | 確認済み | 全体 | write.md の対応と本文が合う。手順（guards-first→interview→…→goal）、確かめる・縛るへの道（define-done・state-the-scope・tests-first・does-more-than-asked）、level、構成の目安（要点→守り→手順→verify→when-it-fails）はすべて本文にある | 直し不要 |

## 検査の結果
- check_page.py を直した後に 1 回：エラー 0・警告 6（直す前と同数）

## メインに判断してほしいこと
- mock-first の根拠の弱さ（write.md と同じ）
- 他ページの snippet を gen:begin で取り込む形でよいか（write.md と同じ）
- 直したので stage は draft のまま。別の担当による直しの差分の確認が要る

## 使用量
- 道具の呼び出し 約 8 回、Web の取得 0 回
