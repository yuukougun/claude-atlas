# write.md：destructive-commands

## 書いたファイル
- docs/safety/destructive-commands.md（stubs から移動。stage を draft、updated を 2026-11-05、sources に既存の 10 件を記入、sections に principle と misconceptions を追加）
- snippets/destructive-commands/：guard-settings.json、block-destructive.py、reversibility-rule.md と、それぞれの .expect.yaml（計 6 ファイル）
- data/sources.d は新しい出典がないので書いていない。facts-proposal.yml は書いていない（提案は下）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle・prevents を本文で名指し）：`#principle`（縛る・握る／境界がない・縛っていない）
- level（任せる）・要点の最初は「何が分かるか」：冒頭の要点
- 構成（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#how-it-happens`、`#not-recoverable`、`#guard`、`#principle`、`#misconceptions`。関連はテンプレートが出す
- pitfalls：空なので該当なし
- 比喩（お願いと鍵）：`#guard`
- 比例則（守りを先に示す）：`#guard` の「鍵」と「本番とリモートは、権限ごと握る」で、bypass の記述の前に鍵を置いた

## メインに判断してほしいこと
- 見逃しの割合（auto モード、公式記事の 17%、n=52）は facts にないので、本文に書かず、`what-auto-mode-stops#limits` へ指した。facts へ足すなら下の提案
- アプリの面（surfaces に app）は材料がなく、タブを作らず「未確認」と一文で書いた。app の調査が要るか
- 本文に Opus 4.6 の名がある（prompting ガイドの記述の時点の名として）。ルール上は変わりやすい名前なので、扱いを見てほしい

## 提案
```yaml
proposals:
  - fact: {id: auto-mode-overeager-miss-rate, title: "auto モードの分類器が実トラフィックの過剰に積極的な行動を見逃した割合", value: "17%（n=52）", sources: [anthropic-eng-code-auto-mode], checked: 2026-11-05, status: 要確認}
    used_in: [destructive-commands#misconceptions]
```

## 検査の結果
- 書いた後：エラー 0・警告 8（文の長さ・助詞の重複など）。直して再実行：エラー 0・警告 1
- 残った警告 1：判断例（Before / After）の箇条の 1 項目が「。」で終わっておらず、文の長さの警告に数えられた。再実行の後に「。」を足した（再確認はしていない）

## 確かめていないこと
- 雛形（設定・フック・CLAUDE.md の規則）の動作は実機で試していない。deny の `Bash(git push --force *)` の照合の細部、フックと権限ルールの優先順位は未確認
- 出典の記述（issue の内容・公式の文書）は束の写しによる。Web の取得はしていない
- アプリでの動作、Windows ネイティブ・IDE 拡張の動作

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
