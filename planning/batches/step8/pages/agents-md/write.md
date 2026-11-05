# write.md：agents-md（feature・extend）

## 書いたファイル
- docs/extend/agents-md.md（stub から移動。stage draft。front matter で変えたキー：sections を 7 節で追加、sources を [cc-docs-memory, cc-docs-commands]、updated 2026-11-05、stage draft）
- snippets/agents-md/import-agents-md.md・.expect.yaml、snippets/agents-md/read-both-files.json・.expect.yaml
- planning/batches/step8/pages/agents-md/facts-proposal.yml（数値の提案 3 件）
- data/sources.d/agents-md.yml は作っていない（新しい出典なし。既存の cc-docs-memory・cc-docs-commands のみ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。要点の「強制力」は `feature enforcement` の目印（#abstract の囲み）
- tracks：front matter に `tracks: [claude-md]`（変更なし）
- level：任せる（front matter。変更なし）
- 構成の目安：使いどころ（#when）→ 読み方の選び方（#choose）→ 最小の使い方（#usage。面は claude-code だけなのでタブは 1 つ）→ 雛形（#templates）→ 効かない場面と落とし穴（#limits）→ 比べる相手（#compare）→ 古くなった助言（#outdated。台帳に行がないので link は置かず、今どうするかを書いた）

## メインに判断してほしいこと
- 台帳（outdated-advice）に AGENTS.md の回避策（CLAUDE.md に「読め」と書く・SessionStart フックで出す等）の行がない。#outdated は台帳を指さず本文で書いた。台帳への行の追加を検討してほしい
- 初期の動き（CLAUDE.md があると AGENTS.md を読まない）は既定の動作なので、提案の fact（agents-md-instruction-files-default）を足した後に目印へ置き換えるか決めてほしい。今は目印なしの文で、設定値の名前は本文に出していない（雛形の JSON と判断例だけ）
- 比例則の警告（level 任せる で verify 等のページが前提・関連にない）は、目次の notes どおり対象外。残した

## 提案
- data/facts.yml：facts-proposal.yml を参照（agents-md-direct-read-min-version・agents-md-instruction-files-default・agents-md-plugin-id-rename）
- 用語集：Project instructions（画面の名前）は prh が「プロジェクトの指示」を求める（same-names-across-surfaces）。本文は「読み込みの設定」と言い換えた。画面の名前を確かめたうえで prh か用語集に例外を足すか決めてほしい
- 台帳：上のとおり

## 検査の結果
- 1 回目：エラー 2（prh の Project instructions 表記）・警告 5。2 回目（直した後）：エラー 0・警告 5
- 残した警告：比例則 1（上記）、no-doubled-joshi 4（行 71・172・178・179。直しても同じ助詞の連続が残った箇所で、読みにくさは小さいと判断。検査は 2 回までなので再調整していない）

## 確かめていないこと
- 事実は公式の memory の文書（2026-11-05 に 1 回取得）と束の材料に基づく。CHANGELOG の原文と /import の対応ツールの範囲は確かめていない（本文は「対応するツール」とだけ書いた）
- 雛形の動作（/context all の表示、設定 JSON の効き）は実機で試していない。雛形の設定のプラグイン ID は版で変わった経緯があり、効かない場合は設定画面で同じ値を選ぶと条件に書いた
- Windows・IDE 拡張・macOS の動作は未確認と本文に書いた。シンボリックリンクの Windows の制約は公式の文書の記述の写し
- 判断例（plan mode を使わせる Claude 向けの指示）は説明用の例で、実在のチームの話ではない

## 使用量
- 道具の呼び出し：約 20 回、Web の取得：1 回（code.claude.com/docs/en/memory）
