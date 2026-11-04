# write.md：output-style-modes（執筆）

## 書いたファイル
- docs/cli/output-style-modes.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-docs-output-styles, cc-docs-features-overview, cc-changelog]、sections に switch と limits を足した。既存の 4 つの anchor は変えていない）
- snippets/output-style-modes/custom-style.md と .expect.yaml（目次の templates の案）
- snippets/output-style-modes/output-style-setting.json と .expect.yaml（足した雛形）
- data/sources.d は書いていない（出典は既存の id のみ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。要点の強制力は `feature enforcement` の目印（冒頭）
- `tracks`：output-styles（front matter のまま）
- 要点（強制力）：冒頭の要点の囲み
- 使いどころ（どの原因を防ぐか）：#built-in（向く場面の表と判断例）
- 最小の使い方：#switch（面は claude-code のみなのでタブは置かない）
- 雛形：#switch（output-style-setting）・#custom（custom-style）
- 効かない場面・落とし穴：#limits
- 比べる相手：#vs-claude-md（comparison の claude-md-vs-rules-skills-styles を link）
- 古くなった助言：台帳の行なし（outdated_advice が空）なので置かない
- level：整える（front matter のまま）

## メインに判断してほしいこと
- 単独のページとして、組み込みの版の数値（Concise の v2.1.237、/output-style の v2.1.269）を本文に書かず「新しい版が要る」とした。数値の提案は下

## 提案
```yaml
proposals:
  - fact: {id: output-style-concise-min-version, title: Concise スタイルが要る Claude Code の版, value: "2.1.237", sources: [cc-docs-output-styles, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#built-in]
  - fact: {id: output-style-command-min-version, title: /output-style コマンドが要る Claude Code の版, value: "2.1.269", sources: [cc-docs-output-styles, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#switch]
  - fact: {id: output-style-setting-case-sensitive, title: outputStyle の値は大文字小文字を区別し、合わない値は Default になる（/output-style コマンドは区別しない）, value: 区別する, sources: [cc-docs-output-styles], checked: 2026-11-05, status: 確認済み}
    used_in: [output-style-modes#switch]
frontmatter:
  - {id: output-style-modes, key: related, before: [...], after: [... , permission-modes-overview], reason: "本文で Proactive と権限モードの関係から link した（未宣言のまま指している）"}
```
- 用語集：「出力スタイル（claude.ai の Styles とは別）」の区別は既存。フック（hook）の訳は prh どおりにした

## 検査の結果
- 1 回目：エラー 8（hook→フック、Output style、prompt caching の表記）・警告 3。直して 2 回目：エラー 0・警告 0。その後、フックの前後の余分な空白を sed で除いた（再検査はしていない。回数の上限のため）

## 確かめていないこと
- 雛形の動作（実機で試していない）。Concise・Proactive の日本語環境での挙動
- VS Code 拡張・デスクトップアプリの入口は公式の文書のとおりで、動作は未確認（本文にそう書いた）
- アプリの Styles の現状（本文は「未確認」とした）
- 取得した公式の文書（Output styles）は 2026-11-05 時点の内容。提案の checked はこの日付

## 使用量
- 道具の呼び出し 16 回ほど、Web の取得 1 回
