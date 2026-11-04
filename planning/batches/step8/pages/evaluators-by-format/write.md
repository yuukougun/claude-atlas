# write.md：evaluators-by-format（concept・contest）

## 書いたファイル
- docs/contest/evaluators-by-format.md（stub から移した。stage を draft、updated を 2026-11-05、sections に `what-it-prevents`・`misconceptions` を末尾へ足した。ほかのキーは変えていない）
- snippets/evaluators-by-format/tester-request.md と .expect.yaml（ローカルテスタを先に作らせる依頼）
- snippets/evaluators-by-format/arena-bots-request.md と .expect.yaml（基準のボットを仕様どおりに作らせる依頼）
- data/sources.d/evaluators-by-format.yml は作っていない（下の「メインに判断してほしいこと」）

## 必ず持つものの対応
- 要点の最初の項目は「何が分かるか」：冒頭の要点の囲み
- principle（確かめる）・prevents（確かめていない）を本文で名指す：`#what-it-prevents`（冒頭の段落で両方を名指し）
- pitfalls：front matter が空なので持たない
- 原理の構成（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#evaluator-first`（なぜ・形式の表）、`#stress-test` 〜 `#arena`（形式ごとの場面）、`#what-it-prevents`、`#misconceptions`。関連はテンプレートが出す
- 比喩付きの図：置かなかった（形式の表で足りると判断。図の案が目次にない）

## メインに判断してほしいこと
- 出典：このページの sources は空のまま。本文の研究・事例（ISUCON14 の再挑戦の事後報告、Battlecode の事後報告、Kaggle 風の CV 実験のブログ）に付ける出典を、新しいドメインの確認のうえで足すか。この担当は Web を取得していない
- 第三者のツール（pahcer・psyleague など）は、成熟度と確認日を添える決め（DR-17）の材料が束にないので、名前を出していない。必要なら確認日付きで足す
- 誤答で提出が止まる大会の例は、目次の備考に従い、数字を書かず規則の確認に回した

## 提案
- 数値の提案はなし（変わりやすい値は書いていない）
- 用語集：ローカルテスタ、ベンチマーカー、CV、referee（対戦の審判）が用語集にあるかを未確認。なければ追加を提案する

## 検査の結果
- `check_page.py` を 2 回流した。最後はエラー 0・警告 7
- 警告の内訳：no-doubled-joshi 5 件と sentence-length 1 件は、link の目印の間に入る長い題名による誤検出が主（行 58・70・203）。行 136・151 の「が」は、文の構造を変えずに読みやすさを保てると判断して残した

## 確かめていないこと
- 雛形 2 つの動作（expect の内容）は実際に試していない
- ハッカソンの節の「機械で確かめられる部分を評価器に置く」は材料にない推論で、（推論・実践例なし）の印を付けた
- データ分析の節の分割の仕方（時間で分ける・分布を比べる）は一般の実務の記述で、束の材料には CV の記述が短い。出典は未登録
- 束の研究の写し（調査資料 10 第8章の 2810 字以降）は、略された部分を読んでいない

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 4、Write 7 のうち報告を含む）。Web の取得：0 回
