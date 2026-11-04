# write.md：what-subagents-dont-inherit（feature・extend）

## 書いたファイル
- docs/extend/what-subagents-dont-inherit.md（stubs から mv。stage は draft。front matter の変更は sections〔7 節〕・sources〔cc-docs-sub-agents・cc-docs-features-overview・cc-docs-features-overview-ja・cc-docs-hooks〕・stage・updated だけ）
- snippets/what-subagents-dont-inherit/delegate-with-rules.txt と .expect.yaml（prompt）
- snippets/what-subagents-dont-inherit/skills-in-definition.md と .expect.yaml（subagent）
- data/sources.d/ のファイルは作っていない（新しい出典がないため）

## 必ず持つものの対応
- 冒頭の要点：abstract の 4 項目（何ができるか・いつ引くか・前提・強制力）
- 機能の属性のバッジ：abstract の「強制力」の行の feature 目印（maturity・load_timing・context_cost）。強制力は data に属性がないので、writing-subagents と同じく文で書いた（お願いと鍵）
- tracks（subagents）：front matter。バッジの目印が tracks の最初を指す
- level：front matter（仕組みにする）
- 使いどころ（どの原因を防ぐか）：`#what-arrives`（「見えていない」を名指し）
- 最小の使い方（面のタブ）：`#hand-over`（Claude Code のタブ。surfaces が claude-code のみ）
- 雛形：`#hand-over`（delegate-with-rules）・`#skills-field`（skills-in-definition）
- 効かない場面・落とし穴：`#pitfalls`
- 比べる相手：`#compare`
- 古くなった助言：置かない（outdated_advice なし）
- 追加の節：`#enforce`（フック）・`#language`（日本語で報告）

## メインに判断してほしいこと
- 目次の visual（親から担当へ届くもの・届かないものの図）は、図を作らず `#what-arrives` の表で代えた。図が要るなら別途
- 強制力の属性が data の features にない。他の feature ページも文で書いているが、道具で出す形にするか

## 提案
- なし（数値の提案も、front matter の提案もなし）

## 検査の結果
- 1 回目：エラー 2・警告 2（prh の auto memory と front matter の表記、助詞の重複 2 件）
- 2 回目：エラー 0・警告 1（助詞「と」の重複）。その後、その 1 文を Edit で直したが、再検査は回数の上限のため流していない

## 確かめていないこと
- 公式の文書を再び開いていない。表の届く・届かないは束の資料（確認日 2026-11-04）に基づく
- 最後の Edit の後の textlint の結果。雛形の動作。「自動の委任では委任の文を Claude が書く」は束の資料の直接の記述ではなく、仕組みからの説明
- 「報告の先頭に守った規則を書かせる」は（推論・実践例なし）の印で書いた

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
