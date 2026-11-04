# write.md：protect-tests（concept・verify）

## 書いたファイル
- docs/verify/protect-tests.md（stub から移動。stage を draft、updated を 2026-11-05。sections に what-it-helps・misconceptions を追加、sources に既存の 7 件を記入）
- snippets/protect-tests/general-solution-request.txt と .expect.yaml（prompt の雛形 1 つ）
- docs/img/protect-tests/layers.svg（守りの層の図）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle・prevents・pitfalls を本文で名指す）：#what-it-helps（確かめる・縛る、確かめていない・縛っていない。pitfalls は front matter が空）
- level（任せる）と、要点の最初の項目「何が分かるか」：冒頭の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#why（例と原因）、#layers（図）、#in-the-request（Before/After）、#what-it-helps、#misconceptions。関連はテンプレートが出す

## メインに判断してほしいこと
- 比喩付きの図は置かず、守りの層の図（catalog の visual 案）だけにした。この型の目安の「比喩付きの図」を満たさない。必要なら足す
- #layers の判断例は「推論・実践例なし」の印を付けた

## 提案
- なし（front matter の他のキー・用語集・data への提案はなし）。数値は本文に手で書いていない。研究の値（79% 超、54%→9%）は固定の記録として、研究名・世代付きで本文に書いた

## 検査の結果
- 1 回目：エラー 0・警告 2（文の長さ、助詞「に」の重複）。箇条に分けて直した
- 2 回目：エラー 0・警告 1（助詞「に」の重複）。「証拠にする前に」を「証拠とみなす前に」に直した。この修正後は検査を流していない（流すのは 2 回までの決めのため）

## 確かめていないこと
- 雛形の動作（Claude が期待どおりに止まるか）は試していない
- 最後の修正後の textlint の結果
- ImpossibleBench の数値・Conflicting-SWEbench の説明は束の写しと記憶による。論文は開いていない
- 判断例と「jq がない環境で素通し」の記述は束の第4節 #19 による。実機では試していない
- 根拠の印「強」は束の評価（強／版依存）に従った

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
