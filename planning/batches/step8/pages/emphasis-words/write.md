# emphasis-words 執筆の報告

## 書いたファイル
- docs/prompting/emphasis-words.md（stubs から mv。stage を draft、updated を 2026-11-05 に）
- snippets/emphasis-words/audit-emphasis.md と audit-emphasis.expect.yaml（prompt）
- front matter で変えたキー：sections（rewrite・stances・effects・limits を足した。既存 4 節の anchor は不変）、sources（既存の id 8 件：cc-docs-best-practices・wb-cc-best-practices-2026-10-26・-10-27・cc-docs-goal・api-docs-prompting-best-practices・api-docs-prompting-opus-5・hyperdev-tired-toddler-problem・shareuhack-code-setup-guide）、stage、updated
- data/sources.d/emphasis-words.yml は作っていない（出典は全部 data/sources.yml の既存 id で足りた）

## 必ず持つものの対応
- どの原理に関わるか（principle：縛る）：#history（回避策としての「縛る」）・#effects
- どの原因に関わるか（prevents：縛っていない・散らかっている）：#effects
- pitfalls：front matter に pitfalls キーがない。持たない
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 技法の構成（頼み方の例→何が変わるか→なぜ効くか→効かない場面）：#rewrite（Before/After と足したもの）・#why-not・#overreaction・#limits

## メインに判断してほしいこと
- 台帳の行を指す link に `outdated-advice-ledger#keep-going-dont-be-lazy` と `#important-caps` を使った（カード §11 の指示）。束の「指せる節」にはない行 id なので、検査は通ったが、公開側の解決を確かめてほしい
- モデル名は本文に書かなかった（「システムプロンプトに強く反応するモデルがある」と書き、model-quirks へ送った）。名前を出すなら names か facts への追加が要る

## 提案
- 用語集：「強調語」を本文で短く定義した（IMPORTANT・YOU MUST・全部が大文字・「絶対に」「必ず」）。用語集に追加するか、判断を
- 数値の提案はなし

## 検査の結果
- 1 回目：エラー 2（prh：system prompt→システムプロンプト、permissions→権限）・警告 6。直した
- 2 回目：エラー 0・警告 3（no-doubled-joshi「に」。冒頭の導入と、#why-not の「例外がない」の箇条、#history の台帳の段落）。リンクの題が文に展開された後の文長や助詞の数え方による可能性があり、残した

## 確かめていないこと
- Web は取得していない。事実は束の材料（Best practices の現行と改稿前の版の要約、公式プロンプト指針の「強すぎる表現」、03 C9）だけに基づく。原文は読んでいない
- 「全テストを実行する」の過剰適用の例と、`.env` の判断例、After の文は、この辞典の想定の例で、実機での再現は確かめていない
- 雛形 audit-emphasis の動作は未確認
- `/goal` と Stop フックの説明は束の台帳の行の写しで、cc-docs-goal の原文は開いていない
- 実践者の立場（権限・フックで強制が主流、CRITICAL でも守られなかった）は、束の 03 C9 の写しのみ。原文の記事は開いていない

## 使用量
- 道具の呼び出し：約 14 回（Read 3・Bash 6・Write 4・検査 2 を含む）。Web の取得 0 回
