# write.md：mcp-or-cli（comparison・extend）

## 書いたファイル

- `docs/extend/mcp-or-cli.md`（stubs から移動。stage を draft、updated を 2026-11-05、`sections` を 5 節、`sources` を 8 件に変更。ほかのキーは触っていない）
- `snippets/mcp-or-cli/gh-cli-skill.md`・`gh-cli-skill.expect.yaml`（目次の templates の案「CLI の使い方を教えるスキル」。gh の例）
- 出典のファイル `data/sources.d/mcp-or-cli.yml` は作っていない。使った出典は、すべて data/sources.yml に既にある id（cc-docs-mcp・cc-docs-costs・cc-docs-features-overview・cc-docs-how-claude-code-works・composio-content-best-mcp-servers-code・simonwillison-agentic-coding・simonwillison-every-code-feature・simonwillison-designing-agentic-loops）

## 必ず持つものの対応

- 冒頭の要点（「〜なら A、〜なら B」の基準を 1 文）：冒頭の要点の囲み（「何ができるか」）
- 比較の表（`compare` の目印）：`table`
- 判断例：`how-to-choose`（3 つ。GitHub の PR と CI・分析用のデータベース・ログイン済みのブラウザ）
- 組み合わせ方（何をどちらに置くか）：`combine`
- level：front matter の「任せる」（そのまま）
- 確かめ方（common §6）：`verify`
- 公式の立場・実践者の幅・この辞典の推奨の三段（notes の指定）：`stances`

## メインに判断してほしいこと

- 比較の表は、tracks が `mcp` 1 つだけなので 1 行になる。CLI は data の機能にないため行にできない。表を比べる形にするには、tracks に `skills` を足す案がある（スキル側が常駐する説明文のコストを持つ）。CLI 自体の行は data に機能として足すか、足さないかの判断が要る。
- `stances` の「この辞典の推奨」に（根拠：中）を付けた。公式の案内と実務家の一致の重なりを根拠にした判断で、割れる論点なので、強さの印が妥当かを見てほしい。
- Simon Willison を肯定的な文脈で名指しした（出典付き）。Composio はベンダー記事と明記した。

## 提案

```yaml
facts:
  proposals:
    - fact: {id: mcp-output-warning-tokens, title: MCP のツール出力で警告が出る大きさ, value: "10,000 トークン", sources: [cc-docs-mcp], checked: 2026-10-29, status: 要確認（調査資料 01 G-1 の写し。一次は未確認）}
      used_in: [mcp-or-cli#table, mcp-or-cli#verify]
    - fact: {id: mcp-output-default-limit-tokens, title: MCP のツール出力の既定の上限（MAX_MCP_OUTPUT_TOKENS）, value: "25,000 トークン", sources: [cc-docs-mcp], checked: 2026-10-29, status: 要確認（調査資料 01 G-1 の写し。一次は未確認）}
      used_in: [mcp-or-cli#table, mcp-or-cli#verify]
frontmatter:
  - {id: mcp-or-cli, key: tracks, before: [mcp], after: [mcp, skills], reason: "比較の表を MCP とスキルの 2 行にして、常駐の説明文の差を示すため（判断はメイン）"}
```

本文は数字なしで読める形にしてある。目印を置く場所は、`table`（出力の警告と上限の文）と `verify`（出力が大きいときの項目）。

## 検査の結果

- 1 回目：エラー 0・警告 4。直したあとの 2 回目：エラー 0・警告 2。
- 残った警告：44 行目（導入の段落の助詞「が」の重なり）、113 行目（組み合わせ方の箇条の助詞「に」の重なり）。検査の回数を使い切ったので直していない。どちらも意味は通じる。検証の担当に直してもらう。

## 確かめていないこと

- ツール検索（定義の遅延読み込み）が入った後に、CLI と MCP のコンテキストの差がどれだけ残るかは、確かめていない（調査資料に「未確認」とある）。本文にもそう書いた。
- 雛形の gh スキルは、実際に動かしていない。`gh pr view --comments`・`gh pr checks`・`gh run view --log-failed` などの書き方は記憶による。一次資料（gh のマニュアル）は開いていない。動作確認の担当が確かめること。
- `/context all` と `/mcp` の動きは調査資料の写しによる。一次資料は開いていない。
- 圧縮で MCP の情報が残るかは、公式の表に行がないので書いていない（表では「未確認」）。
- macOS・IDE 拡張の動作は未確認（本文に書いた）。
- 目印の間（比較の表・雛形・リンク）は道具が埋めた。

## 使用量

- 道具の呼び出し：約 14 回。Web の取得：0 回。
