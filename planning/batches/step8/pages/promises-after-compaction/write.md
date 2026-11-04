# write.md：promises-after-compaction

## 書いたファイル
- docs/context/promises-after-compaction.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 5 件〔cc-docs-context-window・memory・best-practices・costs・permission-modes〕に）
- front matter の sections に 2 節を足した：`effects`（何に効くか）、`misconceptions`（誤解されやすいこと）。既存 3 節の anchor は不変
- snippets/promises-after-compaction/carry-over-claude-md.md、deny-push.json（各 .expect.yaml 付き）
- 新しい出典は足していない（data/sources.d/ のファイルなし）

## 必ず持つものの対応
- どの原理に関わるか（principle：縛る・見せる）：#effects
- どの原因に関わるか（prevents：縛っていない・散らかっている）：#effects
- pitfalls：front matter が空のため、名指す対象なし
- level（任せる）と要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（起きること→なぜ→何に効くか→誤解→関連）：#what-comes-back（例と議事録の比喩）→ #where-to-put → #caveats → #effects → #misconceptions。関連は末尾にテンプレートが出す

## メインに判断してほしいこと
- 図の案（static の対応図）は、SVG にせず #where-to-put の表（置き場所｜向く約束｜例）で代えた。図が要るなら別途
- 「ふつうのファイルは自動では戻らないので、CLAUDE.md に読む 1 行を書く」は「この辞典の推奨」と明記した独自の提案。公式の記述ではない

## 提案
- 変わりやすい値の提案なし（版・上限・トークン数は本文に書かず「上限付き」「数値は版で変わりうる」とした）
- front matter の提案なし
- 用語集：`auto モード`（prh が auto mode を auto モードに直すため、本文はそれに従った）

## 検査の結果
- 1 回目：エラー 1（prh：auto mode）・警告 5。2 回目：エラー 0・警告 4
- 残した警告 4（no-doubled-joshi。助詞「に」「と」の重なり）：76 字前後の文が同じ主語で続く箇所で、分けると意味が切れるため残した。誤検出に近い

## 確かめていないこと
- 本文の事実は束の材料（research/23 §3.4・05 1-6・01 C-1）に基づき、公式の文書そのものは開いていない（Web の取得 0）
- 雛形 2 つは動作を試していない。deny-push の features: [permissions] の最低の版は未確認
- SessionStart フックの matcher が `compact` であることは束の記述による。設定の書き方は載せていない
- CLAUDE.md の `# Compact instructions` 節の挙動は 05 1-6 の記述（Manage costs）による
- Windows・macOS・IDE 拡張の動作は未確認（本文にもそう書いた）

## 使用量
- 道具の呼び出し：約 12 回（check_page 2 回）、Web の取得 0
