# write.md：measure-changes

## 書いたファイル
- docs/eval/measure-changes.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に 5 件、sections に末尾の節 when-it-fails を追加）
- snippets/measure-changes/eval-record.md と .expect.yaml（目次の templates の案。kind: other）
- snippets/measure-changes/classify-failures.txt と .expect.yaml（足した雛形。kind: prompt）
- data/sources.d/measure-changes.yml（新しい出典はなく `sources: []`。出典 id は data/sources.yml の既存を使った）

## 必ず持つものの対応
- 手順：small-eval（7 段、各段に確かめ）
- 確かめる・縛るのページへの道：terms（define-done・test-the-verifier・check-the-metric）、small-eval（selection-pressure#defenses・model-based-grading）、when-it-fails（experiment-log など）。front matter の前提に felt-vs-measured・nondeterminism・define-done
- level を持つ：front matter の level（任せる）。compare-skills と by-stratum は仕組みにする
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：冒頭、terms、small-eval、（compare-skills・graders・how-many-runs・by-stratum・read-transcripts）、when-it-fails

## メインに判断してほしいこと
- 「数個〜20 個ほど」の task 数は、目次の備考どおり「推論・実践例なし」と本文に書いた。Anthropic の 20〜50 個は「公式の立場」として併記した
- how-many-runs の 95% 区間の式と、勝率 55% の n=100・400 の値は、research/24 B-53 の検算を使った。成功率の試行への当てはめは、本文に「概算」と書いた
- 判断例と結果の表は架空の数字（本文に「架空」と明記）。検証ノートではない
- by-stratum の「層は先に決める」は、この辞典の助言（根拠の印は「中・類推」）

## 提案
- 数値の提案はなし（変わりやすい値は plugin-eval の成熟度を feature の目印で指しただけ）
- 用語集への提案：task・trial・grader・transcript・outcome・pass@k・pass^k（本文の terms で短く定義した）
- front matter の提案はなし（signs・aliases は変えていない）

## 検査の結果
- check_page.py を 2 回流した。エラー 0・警告 3（初回は警告 20）
- 残した警告：71 行（no-doubled-joshi。link の目印が埋める題名に「に」が含まれる誤検出）、148 行（sentence-length 124。feature の目印の間が長さに入る）、202 行（no-doubled-joshi。判断例の理由の 1 文）。2 回目の検査で見えたため、直しの担当に任せる

## 確かめていないこと
- `claude plugin eval` の実行方法とオプション、skill-creator の使い方は書かず、公式の文書への案内にとどめた。実機では試していない
- アプリの面の手順は一般的な説明で、設定画面の名前などは確かめていない
- CORE-Bench・Terminal-Bench の数字は束の写し（research/24）からで、一次資料は開いていない
- 「frontier のモデルで 0% なら課題か採点を疑う」は束の注記（pass@100）による。表現が原文より強くないか、確かめていない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得 0 回
