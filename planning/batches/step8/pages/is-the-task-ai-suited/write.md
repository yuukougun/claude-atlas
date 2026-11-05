# write.md：is-the-task-ai-suited（concept・delegate）

## 書いたファイル

- docs/delegate/is-the-task-ai-suited.md（stubs から mv。stage を draft、updated を 2026-11-05。sections に how-to-score・what-it-prevents・misconceptions を足した。sources に既存の 5 件を入れた：sakana-ahc058・zenn-microsoft-78e01f59・includesecurity-ctfs-ai-era・anthropic-research-cyber-competitions・battlecode-2026-lorem-ipsum-pdf）
- snippets/is-the-task-ai-suited/score-five-axes.md と score-five-axes.expect.yaml（目次の templates の案：作業を五つの軸で見積もらせるプロンプト）
- data/sources.d/<id>.yml は作っていない（出典はすべて data/sources.yml にある既存の id）

## 必ず持つものの対応

- 冒頭の要点（何が分かるか・いつ引くか・前提）：冒頭の囲み
- どの原理・どの原因に関わるか（principle 確かめる・握る／prevents 合っていない・確かめていない／pitfalls 預けすぎる）の名指し：`#what-it-prevents`（導入の段落にも「確かめる」「握る」）
- level（任せる）：front matter。要点の最初は「何が分かるか」
- 構成の目安（要点→何が起きるか→なぜ→何に効くか→誤解→関連）：`#five-axes`（軸と事例）、`#where-humans-matter`、`#how-to-score`（判断例・雛形）、`#what-it-prevents`、`#misconceptions`。関連はテンプレートの page-links。図は置かなかった（表で足りるため）

## メインに判断してほしいこと

- 判断例の「ログの集計と障害の原因調査」は、束の材料にない仮想の場面（材料は大会の事例）。業務の作業にも使える旨（p12#63）に沿って作った。不要なら差し替えてよい

## 提案

- なし（変わりやすい値は本文に書いていない。事例の数値〔AHC058 の局所評価、ISUCON の約 1 時間・3〜4 時間、Airbnb CTF の 60 分・30 問中 13 問・最終 15 問 39 位、Battlecode 2026 のローカル勝率 85% 超〕は研究・報告の時点の固定の記録として、出典 id を添えて書いた）

## 検査の結果

- check_page.py を 2 回流した。1 回目：エラー 0・警告 6。2 回目：エラー 0・警告 2（max-ten 1・no-doubled-joshi 1）。2 回目の後に両方の文を書き直した（再実行はしていない）

## 確かめていないこと

- 書き直した 2 文の textlint の結果（検査は 2 回までの決まりのため再実行していない）
- 事例の数値と主張は、束の写し（調査資料 10 第2章）に基づく。一次資料を開いて確かめていない（Web の取得 0 回）。束の注記のとおり、欧州の CTF の約 8,000 ドルは確かめられていないので本文に使っていない。ISUCON の「約 1 時間」「3〜4 時間」の根拠の印は弱（参加者の記事）としたが、出典の種類を原文で確かめていない
- Battlecode の記述は「参加チーム自身の振り返り」という種類の判断を調査資料から写した
- 面のタブは置いていない（面ごとに手段が違う話がないため）

## 使用量

- 道具の呼び出し：約 14 回。Web の取得：0 回
