# write.md：bare-mode（--bare と再現性）

## 書いたファイル
- docs/delegate/bare-mode.md（stubs から移動。stage draft、updated 2026-11-05、sections を 8 節に増やした〔既存の 2 anchor は維持〕、sources を data の 4 件にした）
- snippets/bare-mode/isolated-run.sh と isolated-run.expect.yaml（サブスクリプションのまま設定を混ぜない起動例）
- data/sources.d/bare-mode.yml（`sources: []`。新しい出典なし）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文では maturity を `feature bare-mode/maturity` の目印で指した（冒頭の導入）。強制力は data の bare-mode の項目に値がないため目印を置かず、要点の「強制力」に値を使わない説明だけ書いた（`#top` の要点）。提案を参照
- tracks：front matter の `tracks: [headless, settings, bare-mode]`（変更なし）
- level：front matter の `level: 回す`
- 構成の目安：要点（冒頭）→ 使いどころ `#when` → 最小の使い方 `#minimal` → 雛形 `#templates` → 効かない場面・落とし穴 `#pitfalls` → 比べる相手 `#compare`。古くなった助言は、台帳の行がない（束の 4 に outdated_advice なし）ので節を置かない

## メインに判断してほしいこと
- 要点の「強制力」：data に enforcement がないため値の目印を使えなかった。起動時に読み込みを止めるので「鍵」に近いが、道具の許可は絞らない。data への追加の可否を決めてほしい（提案参照）
- 雛形：カード §10 の「API キーが要る --bare は載せない」に従い、catalog の案「自分の設定を混ぜない claude -p の起動例」を、API キー不要の組み合わせ（`CLAUDE_CONFIG_DIR`・`--setting-sources project,local`・`--strict-mcp-config`、research/28 §3.4）にした。この組み合わせは文書から組んだ案で、動かしていない
- ページ内で、related にない `isolate-with-safe-mode` と `checking-unattended-runs` を link で指した（check_page は通った）。related への追加を提案する

## 提案
```yaml
frontmatter:
  - {id: bare-mode, key: related, before: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, github-actions-with-claude, batch-and-p-loops, choosing-automation], after: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, isolate-with-safe-mode, checking-unattended-runs, github-actions-with-claude, batch-and-p-loops, choosing-automation], reason: "本文で比べる相手・確かめ方として指している"}
proposals:
  - fact: {id: bare-mode-default-plan, title: "-p の既定を --bare にする予定の有無", value: "公式の headless の文書は、--bare を将来 -p の既定にすると書く（予定。入る版は未定）", sources: [cc-docs-headless], checked: 2026-11-05, status: 確認済み}
    used_in: [bare-mode#pitfalls]
  - fact: {id: setting-sources-leak-fix-version, title: "--setting-sources で外した設定が漏れる不具合の修正の版", value: "v2.1.314（research/22 #6。CHANGELOG の再確認が要る）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [bare-mode#pitfalls]
  - fact: {id: bare-mode-partial-limits-before, title: "--bare の MCP・システムリマインダー・バックグラウンドの制限が完全になった版", value: "v2.1.286 より前は一部だけ（headless の文書）", sources: [cc-docs-headless], checked: 2026-11-05, status: 確認済み}
    used_in: [bare-mode#what-is-skipped]
features:
  - 提案：data/facts.yml の bare-mode の項目に enforcement（候補：鍵。読み込みの時期は「起動時」）を足す
```
本文は、これらの数字・予定がなくても読める形にした。目印は置いていない（承認後に置く）。

## 検査の結果
- check_page.py を 2 回流した。1 回目はエラー 1（`hooks` の表記が prh に当たる）・警告 1（snippet の目印を 1 行に置く）。直して 2 回目はエラー 0・警告 0

## 確かめていないこと
- 雛形の動作（`CLAUDE_CONFIG_DIR` の分離、環境変数の効き）は動かしていない
- `--bare` の細かい挙動（システムリマインダー・バックグラウンドの制限・`--add-dir` の例外）は、公式の headless の文書（2026-11-05 取得）に基づく。CHANGELOG と突き合わせていない
- Claude Code の版・OS 別の動作は確かめていない（WSL・Linux の CLI を基準に書いた）
- 判断例の B（`--setting-sources` と `CLAUDE_CONFIG_DIR`）の混ざりの減り方は、動かして確かめていない
- `--setting-sources` の漏れの不具合は、本文で版を書かず「過去にあった」とだけ書いた

## 使用量
- Web の取得 1 回（code.claude.com/docs/en/headless）。ほかに束とカード、既存ページ（headless-basics）の冒頭を参照。道具の呼び出しは約 15 回
