# write.md：attention-budget（コンテキストウィンドウと注意の予算）

## 書いたファイル
- docs/basics/attention-budget.md（stubs から mv。stage: draft、updated: 2026-11-05、sources に既存の 4 件、sections に 5 節を追加）
- docs/img/attention-budget/wide-desk.svg（広い机の模式図。400x220）
- 雛形・data/sources.d/attention-budget.yml は置いていない（templates なし、新しい出典なし）

## 必ず持つものの対応
- 原理・原因への結び付け（principle=見せる、prevents=散らかっている）：#effects（「見せる」「散らかっている」を名指し）
- pitfalls：front matter に無いので持たない
- level（使う）と要点の最初が「何が分かるか」：冒頭の囲み
- 構成（要点→何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #why（図付き）→ #effects → #examples（判断例）→ #misconceptions → 関連はテンプレート
- 古くなった助言（save-context-for-200k）：#effects で台帳へ link

## メインに判断してほしいこと
- 窓の大きさの数値は本文に書かず、数値の目印も置いていない（束に該当の facts id が無いため）。large-context-window を指すだけにした
- #why の n の 2 乗の説明は、束の Inferences（提案）と記憶に基づく。Anthropic の記事（anthropic-eng-effective-context-engineering-ai）を本文で開いて確かめていない。「（根拠：中）」を付けたので、検証で原文との突き合わせが要る

## 提案
なし

## 検査の結果
- 1 回目：エラー 0・警告 7。2 回目（直した後）：エラー 0・警告 4
- 残した警告：no-doubled-joshi 4 件（53・59・93・95 行）。2 回の規定のため直していない。意味は通る

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0 回）。アテンションの n² の説明と「高シグナルなトークンの最小集合」の言い回しは記憶と束による
- 「資料を絞ると制約に触れた答えが返ることがある」は筋書きの例で、実測していない
- 図の見え方（描画）を目で確かめていない

## 使用量
- 道具の呼び出し：約 9 回、Web の取得 0 回
