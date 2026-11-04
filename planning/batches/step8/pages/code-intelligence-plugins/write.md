# write.md：code-intelligence-plugins

## 書いたファイル
- `docs/extend/code-intelligence-plugins.md`（stub から mv）。front matter で変えたキー：`sections`（use・minimal・templates・limits・compare を追加）、`sources`（cc-docs-code-intelligence・cc-docs-features-overview・cc-docs-plugins-overview・cc-docs-changelog。いずれも data/sources.yml にある）、`stage`（draft）、`updated`（2026-11-05）
- `snippets/code-intelligence-plugins/check-diagnostics.txt` と `.expect.yaml`、`find-by-symbol.txt` と `.expect.yaml`（目次の templates は「なし」。分かりやすさのために 2 つ足した）
- `data/sources.d/code-intelligence-plugins.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応
- 機能の属性のバッジ：`compare` の目印（`#compare`）で、tracks の 2 機能の成熟度・読み込みの時期・コンテキストのコスト・入った版を出す。ページ冒頭のバッジはテンプレートが出す
- 強制力：冒頭の要点に文で書いた（値の目印は使えない。下の提案を参照）
- `tracks`：front matter の `tracks: [code-intelligence, plugins]` のまま（`#compare`）
- level：front matter の `level: 仕組みにする` のまま
- 構成の目安：使いどころ（`#use`）→ 最小の使い方（`#minimal`、面のタブは Claude Code のみ）→ 雛形（`#templates`）→ 効かない場面・落とし穴（`#limits`）→ 比べる相手（`#compare`）。古くなった助言は台帳の行がないので置かない

## メインに判断してほしいこと
- data の features の `code-intelligence` に `enforcement` の値がない。冒頭の「強制力」は、目印を使わず文で「止める働きはない」と書いた。`enforcement: なし` を足せば `<!-- gen:begin feature enforcement -->` に差し替えられる（下の提案）
- 公式の文書にある言語ごとのプラグイン名・実行ファイルの対応表は載せず、公式へのリンクにした（カード §12 の網羅を避ける方針）。`/plugin install typescript-lsp@claude-plugins-official` の 1 行だけ例に載せた。マーケットプレイス名は変わりうる値なので、気になれば数値の目印に直す

## 提案
```yaml
data:
  - {feature: code-intelligence, key: enforcement, after: なし, reason: "診断は自動で返り、LSP の道具は読み取り専用で、Claude の動きを止めない（公式 code-intelligence の文書）。冒頭の強制力を目印に差し替えるため", used_in: [code-intelligence-plugins#top]}
```
front matter の提案、用語集・prh への提案はない。

## 検査の結果
- 1 回目：エラー 1（prh：plugin の表記）・警告 5。2 回目：エラー 1（半角英数字の前の空白）・警告 4。2 回目の後に空白を直したが、3 回目は流していない（回数の決まりのため）。直した 1 文は84行の 1 か所で、エラーは解消しているはず
- 残した警告 4：no-doubled-joshi（助詞「が」「に」の重なり）。意味を変えずに直すと冗長になるため残した。検証の担当が見てほしい

## 確かめていないこと
- 本文の機能の挙動は、公式の文書（Code intelligence plugins、2026-11-05 に取得）と束の材料による。制作の環境で言語サーバーを入れて動かしてはいない。雛形 2 つも動作未確認
- VS Code 拡張・デスクトップアプリでの入れ方は公式が別の手順を案内するとだけ書き、動作は「未確認」とした
- 公式の文書の「5 回無視で止まる」「30 秒で閉じる」などの数は、変わりやすい値なので本文に書いていない
- 2 回目の検査の後に直した 1 文は、検査を流していない

## 使用量
- 道具の呼び出し：約 14 回（Read 2・Bash 6・Write 6 ほか）。Web の取得：1 回（code.claude.com の公式文書）
