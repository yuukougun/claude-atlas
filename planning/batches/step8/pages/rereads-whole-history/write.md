# write.md：rereads-whole-history

## 書いたファイル
- docs/basics/rereads-whole-history.md（stubs から mv。stage を draft、updated を 2026-11-05、sections を 4 節、sources を [cc-docs-costs, api-docs-message-threads] に変えた）
- docs/img/rereads-whole-history/rereads.svg（読む量が回ごとに積み上がる静止図）
- 雛形・data/sources.d は作っていない（目次の templates なし。出典は data/sources.yml に既にある 2 件だけを使った）

## 必ず持つものの対応
- 用途（なぜそうなるか）：`what-happens`（具体例の表）と `why`（比喩付きの図）
- principle「見せる」の名指し：`effects`（冒頭の段落）
- prevents「散らかっている」の名指し：`effects`（1 つ目の箇条）
- prevents「合っていない」の名指し：`effects`（2 つ目の箇条）
- pitfalls：front matter に pitfalls がないため持たない
- level（使う）と、要点の最初の項目「何が分かるか」：冒頭の要点の囲み
- 構成（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`what-happens`・`why`・`effects`・`misconceptions`（関連はテンプレートが出す）

## メインに判断してほしいこと
- 図の主にする「公式の Explore the context window」の対話型の図へのリンクは、URL を確かめていないので入れていない。URL を渡してもらえれば足す
- `effects` に判断例を 1 つ置いた（続けるか新しい会話にするか）。when-to-start-fresh と重なるなら削ってよい

## 提案
- 用語集：「読み直す受験者」「積み木（キャッシュ）」の比喩は、既存の一覧どおり使った。追加の提案なし
- front matter の提案なし

## 検査の結果
- 1 回目：エラー 0・警告 0 以外の指摘なし（生成・参照は通った）
- 2 回目（直した後）：エラー 0・警告 4（no-doubled-joshi の「が」）
- 2 回目のあとに、その 4 つの文を言い換えた。検査は 2 回までの決めなので、再実行していない（警告が残るかは未確認。エラーにはならない種類）

## 確かめていないこと
- 言い換えた 4 文の textlint の結果（上記）
- 公式の文書の確認は Web を 1 回（code.claude.com/docs/en/costs）。message threads の内容（送る量は減るがモデルが読む量・料金は変わらない）は束の research/22 #40 によるもので、api-docs-message-threads は開いていない
- アプリ（claude.ai）が会話の全体をどう送っているかの細部は未確認とし、本文にもそう書いた
- キャッシュの有効期間・料金の割合は数値の目印を使っておらず、本文に書いていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：1 回
