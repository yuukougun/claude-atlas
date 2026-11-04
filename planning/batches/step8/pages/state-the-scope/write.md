# write.md：state-the-scope

## 書いたファイル
- `docs/prompting/state-the-scope.md`（stub から移動。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（templates・effects・limits を足した。既存 3 つの anchor は不変）、`sources`（既存の id 6 つ）、`stage`、`updated`
- `snippets/state-the-scope/scope-request.{md,expect.yaml}`、`scope-claude-md.{md,expect.yaml}`（`data/sources.d/state-the-scope.yml` は、出典がすべて既存の id なので作っていない）

## 必ず持つものの対応
- どの原理・原因に関わるか（`principle`：見せる・縛る／`prevents`：見えていない・合っていない）：`#effects`（`#two-layers` の「縛る」も補う）
- level を持つ・要点の最初は「何が分かるか」：冒頭の要点（level は front matter の「整える」）
- 構成（技法）：Before/After は `#anti-goals`、何が変わるかは `#anti-goals`・`#minimum`、なぜ効くかは `#anti-goals` の第 3 段落と `#effects`、効かない場面は `#limits`
- `pitfalls`：front matter に無いので持たない

## メインに判断してほしいこと
- 本文から `give-reasons`（related にない）を link で指した。check は通ったが、related に足すかを判断してほしい（下の提案）
- `#two-layers` の「アプリ」タブに「アプリで依頼の範囲を仕組みで縛る手段は未確認」と書いた。確認できる資料が束になかったため

## 提案
```yaml
frontmatter:
  - {id: state-the-scope, key: related, before: [does-more-than-asked, say-what-you-want, suggest-or-do, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks], after: [does-more-than-asked, say-what-you-want, suggest-or-do, give-reasons, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks], reason: "本文で give-reasons を指したため"}
```

## 検査の結果
- 1 回目：エラー 1（system prompt の表記）・警告 6。直した
- 2 回目：エラー 0・警告 1（`no-doubled-joshi` の「で」、「長いセッションで薄れる」の項。意味は通るので直さず残した）

## 確かめていないこと
- 雛形 2 つの動作は試していない
- 引用した英文 2 つと Best practices の文は、束の抜き出し（確認日 2026-10-29）に基づく。原文は開いていない
- 「長いセッションで薄れる」「圧縮で消えうる」は束の when-to-lock の要約に基づく
- 「アプリ」タブの記述と API タブの「ツールを実行するのは自分のコード」は、一般的な構成に基づく

## 使用量
- 道具の呼び出し 約 12 回、Web の取得 0 回
