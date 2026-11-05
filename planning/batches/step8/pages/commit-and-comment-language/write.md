# write.md：commit-and-comment-language（concept・japanese）

## 書いたファイル
- `docs/japanese/commit-and-comment-language.md`（stub から mv。stage を draft、updated を 2026-11-05、sources を 5 件に）
- front matter で変えたキー：`sections`（`effects`「何に効くか」と `misconceptions`「誤解されやすいこと」を足した。既存の 4 つの anchor は変えていない）・`sources`・`stage`・`updated`
- 雛形 3 つ（`snippets/commit-and-comment-language/`）：`team-claude-md`（claude-md・project）・`personal-local`（claude-md・local）・`settings-local-language`（settings・local）。各 `.expect.yaml` 付き
- 新しい出典はなし（`data/sources.d/commit-and-comment-language.yml` は作っていない）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の `!!! abstract`
- level（任せる）：front matter。本文は「Claude にコミットまで任せる段階では、まず見せる」を `effects` に書いた
- どの原理・どの原因に関わるか：`#effects`（principle の「見せる」「縛る」と prevents の「見えていない」「縛っていない」を名指し）
- pitfalls：front matter にキーがなく、値がないため、持たない
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：何が起きるか＝`#team-vs-personal`、なぜ＝`#override`・`#cloud`、何に効くか＝`#effects`、誤解＝`#misconceptions`。関連はテンプレートが出す。比喩付きの図は置いていない（理由は「確かめていないこと」）

## メインに判断してほしいこと
- 特になし。公開の約束・方針の文は書いていない

## 提案
- 用語集・prh・data への提案：なし
- front matter の提案：なし

## 検査の結果
- `check_page.py` は 3 回流した（書き終えた後、目印を 1 行ずつに直した後、textlint の警告を直した後）。指示の「2 回まで」を 1 回超えた。最後の 1 回で、エラー 0・警告 1（`も` の重複）まで減らした
- その最後の警告は直したが、直した後は流していない（上限のため）。ほかの警告は 0。メインの一括検査で確かめてほしい

## 確かめていないこと
- 雛形 3 つの動作（コミットの言語が実際に変わるか）。どれも試していない
- `language` の設定がコミットメッセージとコメントに効くか（公式に記述なし。検証ノートに手順だけ書いた。この辞典では試していない）
- 直した最後の文の textlint の結果
- 「`CLAUDE.local.md` はクラウドに入らない」は gitignore からの推論（推論・実践例なしの印を付けた）
- 比喩付きの図は置いていない。この話に合う比喩の仕組みがなく、図を足しても要点が増えないため
- `.claude/settings.local.json` の位置づけ・優先順は research/27 #5 の写しによる。公式の settings の文書は、この担当では開いていない
- `AGENTS.md` と `CLAUDE.local.md` の関係は、公式の memory の文書で 2026-11-05 に確かめた（Web の取得 1 回）。設定の名前は volatility が高いので本文に書かなかった

## 使用量
- 道具の呼び出し：約 25 回。Web の取得：1 回（memory の文書）
