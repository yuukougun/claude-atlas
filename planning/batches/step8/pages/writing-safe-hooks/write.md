# write.md：writing-safe-hooks（フックを安全に書く）

## 書いたファイル
- docs/enforce/writing-safe-hooks.md（stubs から mv。stage draft、updated 2026-11-05）
- front matter で変えたキー：sections（`when`・`templates`・`limits` を追加。既存 4 つの anchor は変えず）、sources（cc-docs-hooks・cc-docs-hooks-guide・cc-docs-sandboxing・cc-changelog。いずれも既存の id）、stage、updated
- snippets/writing-safe-hooks/fail-closed-settings.json と .expect.yaml（kind settings。`min_version_fact: hook-on-failure-block-min-version`）
- snippets/writing-safe-hooks/guard-migrations.sh と .expect.yaml（kind hook。jq の有無を先頭で確かめ、無ければ exit 2）
- data/sources.d/writing-safe-hooks.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点の「強制力」行（`gen:begin feature enforcement`）。ほかの属性のバッジはテンプレートが出す
- `tracks`：front matter の `tracks: [hooks]`
- level：front matter の `level: 仕組みにする`
- 1機能1ページ・密接な系統は節に分ける：`#fail-open`・`#matcher`・`#exec-form`・`#runs-as-you`
- 使いどころ（どの原因を防ぐか）：`#when`（縛っていない・境界がない）
- 最小の使い方（面のタブ）：持たない。surfaces が claude-code だけで、最小の使い方は `#templates` の 2 つの雛形が兼ねる
- 雛形（折りたたみ）：`#templates`
- 効かない場面・落とし穴：`#limits`（各節の中にも落とし穴を置いた）
- 比べる相手：`#limits` の表（permission-rules・block-with-exit-2・lock-side-effects）
- 古くなった助言：持たない（台帳の行なし。束の outdated_advice が空）

## メインに判断してほしいこと
- 節の追加：`when`・`templates`・`limits` を sections に足した。カードの型の構成に合わせたもの
- `${CLAUDE_PROJECT_DIR}` を `args` の要素に書く形は、research/28 #23 の「置き換えを使うフックには args を付ける」から組んだ。args の中での置き換えの実際の動きは、動作確認の担当に確かめてほしい
- 本文は permission-rules を、束の「つながるページ」にないが、既存の公開ページなので page 単位で link した。related に足すかは判断を仰ぐ

## 提案
```yaml
frontmatter:
  - {id: writing-safe-hooks, key: related, before: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing], after: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing, permission-rules], reason: "比べる相手の表で permission-rules を指したため（任意）"}
```
- 数値の提案はなし（onFailure の版は既存の fact `hook-on-failure-block-min-version` を使った。タイムアウトの既定値は本文に書いていない）
- 用語集・prh への提案：managed settings は prh で「管理設定」に直された。本文は「管理設定」にした

## 検査の結果
- check_page.py：1 回目 エラー 1・警告 1（prh の managed settings、助詞「が」の連続）→ 直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形 2 つは実際に動かしていない（`onFailure` と `args` を同時に書いた設定が通るか、`bash` + `args` での起動、jq 無しの挙動）
- `onFailure` を付けたときの「スクリプトの失敗が空の文字列になり 0 で終わる」例は、bash の一般的な挙動からの説明で、Claude Code 上では試していない
- 表の「出力の JSON が壊れている → 止まる」は research/28 #17 による。実環境では試していない
- 「http のフックは入力の JSON を送り出す」は 01 F-1 の「http（POST）」からの読み取り
- 「CI の定義と同じ扱い」は 11 の p34#213 に基づく類推として書いた（根拠の印は（類推））
- Windows ネイティブ・IDE 拡張での動作は未確認

## 使用量
- 道具の呼び出し：約 14 回（Read 5・Bash 6・Write 6 のうち本報告を含む）、Web の取得 0 回、check_page.py 2 回
