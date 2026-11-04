# write.md：split-models-by-role

## 書いたファイル
- docs/models/split-models-by-role.md（stubs から mv。stage を draft、updated を 2026-11-05）
- snippets/split-models-by-role/log-triage-subagent.md と .expect.yaml
- data/sources.d/split-models-by-role.yml（`sources: []`。新しい出典なし）
- planning/batches/step8/pages/split-models-by-role/facts-proposal.yml
- front matter で変えたキー：sections（what-it-helps・misconceptions を追加。既存 3 つは不変）、sources（既存 id 5 つ）、stage、updated

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 見せる・prevents 合っていない を本文で名指す）：#what-it-helps
- level 任せる・要点の最初は「何が分かるか」：冒頭の要点。守りを先に示す比例則は #lighter-models（確かめる手段を先に決める）
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#patterns（何が起きるか）・#when-to-split（なぜ・いつ）・#what-it-helps・#misconceptions。関連はテンプレート。比喩付きの図は持たない（理由：判断の表と判断例で足りると見て、図は置かなかった）

## メインに判断してほしいこと
- 図を置かなかった。必要なら「分ける形」の表を図にする案を別の担当へ

## 提案
- facts-proposal.yml：opusplan の割り当て（plan mode は上位の系統、実行は日常の系統）。本文は系統の名前だけで書き、数値・版は書いていない。承認後に目印へ差し替える
- front matter（YAML）：
```yaml
frontmatter:
  - {id: split-models-by-role, key: related, before: [...], after: [..., choosing-a-model#verify], reason: "本文が choosing-a-model#verify を指している（前提に含まれるので不要なら無視してよい）"}
```
- 用語集：「上位の系統・日常の系統・軽い系統」を本文で使った。current-models の表と言い方を合わせてよいか確認してほしい
- 台帳：既存の avoid-opus-as-expensive の行を本文で指した。変更の提案なし

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告 4（no-doubled-joshi：88 行・99 行・122 行・155 行。どれも文意が自然で、誤検出に近いと見て残した）。1 回目の警告 6 のうち 2 件（一つ→1 つ）と 2 件の助詞は直した

## 確かめていないこと
- 雛形の動作（log-triage が本当に起動し、表が返るか）
- CLAUDE_CODE_SUBAGENT_MODEL と定義の `model` の優先順（公式の model-config に記述なし。本文はそう書いた）。コミュニティの解説に頼る部分は（根拠：弱）
- `opusplan` の割り当ては 2026-11-05 に model-config で確かめた（Web の取得 1 回）。ほかの記述は束の材料（2026-10-29 確認）
- 計画と実装の切り替えでキャッシュや使用量がどう変わるか
- 「計画は会話に残る」は plan mode が同じ会話の中の状態であることからの推論
- 軽いモデルへ割り当てた時の effort の挙動の版（fact は status 未確認のまま）

## 使用量
- 道具の呼び出し：約 14 回（Read 3・Bash 8・Write 4・WebFetch 1・ToolSearch 1 ほか）。Web の取得 1 回
