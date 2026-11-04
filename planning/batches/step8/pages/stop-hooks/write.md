# write.md：stop-hooks（feature・enforce）

## 書いたファイル
- docs/enforce/stop-hooks.md（stubs から mv。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（when・minimal・templates・pitfalls を足した。既存の 3 つの anchor は変えず）、`sources`（cc-docs-hooks・cc-docs-hooks-guide・cc-docs-goal）、`stage`、`updated`
- snippets/stop-hooks/：stop-until-tests-pass.py（と .expect.yaml）、register-stop-hook.json（と .expect.yaml）
- data/sources.d/stop-hooks.yml（`sources: []`。新しい出典はない）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力など）：冒頭の要点の「強制力」（`feature enforcement` の目印）と、`vs-goal` の `compare 強制力 成熟度`・`feature goal/enforcement`
- `tracks`（hooks・goal）：front matter のまま。本文は `vs-goal` で goal を扱い、hooks は全体で扱う
- 使いどころ（どの原因を防ぐか）：`#when`（原因「確かめていない」）
- 最小の使い方（面のタブ）：`#minimal`。surfaces が claude-code だけなので、タブは置かず、本文に面を書いた（`#pitfalls` 末尾）
- 雛形：`#templates`（Stop フックのスクリプトと登録の設定）
- 効かない場面・落とし穴：`#pitfalls`、上限の注意は `#block-cap`
- 比べる相手：`#vs-goal`
- 古くなった助言：持たない（束に台帳の行がない）
- level：front matter の「仕組みにする」のまま
- 比例則：このページ自体が守り。無人の完了の確かめに使う旨と、上限は「通った」の保証でない旨を `#block-cap` に書いた

## メインに判断してほしいこと
- 目次の templates は 1 つだけだが、登録の設定を足して 2 つにした
- 「Stop フックと `/goal` の併用の挙動」は確かめておらず、本文に「確かめていない」と書いた

## 提案
- 数値の提案はなし（上限は既存の fact `stop-hook-block-cap` を使った）
- front matter の提案（YAML）：なし
- 検証ノート（目次 notes の見せ方）は、制作の環境での記録が要るため作っていない

## 検査の結果
- check_page.py：1 回目 エラー 2・警告 3（空白と助詞の重複）、直した後 エラー 0・警告 0

## 確かめていないこと
- 雛形のスクリプトと設定は実行していない。動作は未確認
- `stop_hook_active` が、差し戻しの間にツールを挟んでも真のままかは、一次資料で確かめていない（雛形はこれを数え直しの目印に使う）
- `systemMessage` が Stop の出力で画面に出ること、`additionalContext` と上限の関係の細部は、束の写し（research/23 #3）の範囲でしか見ていない
- 「ツールを挟むと数えが戻るので、ループが上限に届かないことがある」は、束の記述からの読みで、実機では確かめていない
- 環境変数の既定外の値（上限なしの値）と入った版は、本文に書いていない
- Web の取得は 0 回

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回
