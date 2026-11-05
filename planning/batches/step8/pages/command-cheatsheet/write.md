# command-cheatsheet 執筆報告

## 書いたファイル
- `docs/cli/command-cheatsheet.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-commands・cc-changelog・cc-docs-changelog、sections を 5 節で追加）
- 雛形・図・`data/sources.d/` は置いていない（目次に templates・visual がなく、出典は既存の id だけ）

## 必ず持つものの対応
- 冒頭の要点：先頭の囲み（要点）
- データから作る表：`#by-old-name`（旧名→今の名前は names の `name:` の目印で出す）。コマンド→ページの表 `#by-command` は、対応する生成の目印がないため手書き（下の「メインに判断してほしいこと」1）
- 読み方（台帳は「どの原理の回避策だったか」）：`#patterns`（名前が変わる型と、回避策が正式な仕組みに置き換わる規則）、`#how-to-read`、`#find-in-your-setup`
- level：持たない（型の規定どおり）

## メインに判断してほしいこと
1. コマンド→判断のページの表は、材料の束の方針「生成のページ」に反して手書きになった。gen に、コマンドと行き先のページを持つ表の目印がないため。案：data/facts.yml の features か新しい項目にコマンドの行（コマンド・一言・page・anchor）を持たせ、`command-table` の目印を足す。足すまでは、手書きの表を暫定として残す
2. 手書きの表の「何ができるか」の一言は、束の材料（公式の表の抜粋・行き先のページの要約）の範囲で書いた。`/skills`・`/hooks`・`/mcp`・`/plugin` の一言は名前と行き先の題名から書いたもので、公式の表で一言ずつは確かめていない
3. 台帳の行にない旧名 `/review`・`/allowed-tools` を names の目印で載せた。台帳に行を足すかは任せる（足すなら ledger の提案）

## 提案
- 目印 `command-table` の新設（上の 1）
- `/review`・`/allowed-tools` の台帳の行の追加（任意。上の 3）

## 検査の結果
- `check_page.py command-cheatsheet`：1 回目でエラー 0・警告 0（流したのは 1 回）

## 確かめていないこと
- 実機での各コマンドの動作（どれも打っていない）。公式の Commands の表との 1 対 1 の照合
- `/plan` が plan mode に入るコマンドであること、`/statusline`・`/status`・`/memory`・`/ide`・`/remote-control`・`/teleport` の一言は、行き先のページの要約と名前からの記述
- `/powerup`・`/insights` の行き先を ask-claude-code にしたこと（材料の「Claude Code 自身に聞く」の行の要点に基づく）
- `/review` が今も別名として打てるかどうか（names は旧名としか記さない）
- IDE 拡張と WSL・Linux 以外の OS の動作

## 使用量
- 道具の呼び出し：17 回前後。Web の取得：0 回
