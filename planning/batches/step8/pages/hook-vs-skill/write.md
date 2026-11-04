# hook-vs-skill 執筆の報告

## 書いたファイル
- docs/extend/hook-vs-skill.md（stubs から移した。stage draft）。front matter で変えたキー：`sections`（4 節）、`sources`（5 件、すべて既存の id）、`stage`、`updated`
- snippets/hook-vs-skill/format-skill.md と .expect.yaml（スキル版の整形）、format-hook.json と .expect.yaml（フック版の整形）。目次の templates の案どおり
- data/sources.d/hook-vs-skill.yml は書いていない（新しい出典なし）

## 必ず持つものの対応
- 冒頭の要点：先頭の `!!! abstract "要点"`（「〜なら A、〜なら B」の基準を 1 文目に置いた）
- 比較の表（compare の目印）：#table
- 判断例：#how-to-choose（整形・リリース・日本語の文体・テストを流す一歩の 4 例）
- 組み合わせ方：#combine
- 確かめ方（任意で足した節）：#verify
- level：front matter に「任せる」のまま

## メインに判断してほしいこと
- 「ほかの OS と IDE 拡張は未確認」の一文を #table の補足に入れた。位置はここでよいか

## 提案
- なし（数値の提案も、front matter の提案もない）

## 検査の結果
- 1 回目：エラー 1（「frontmatter」の表記を prh が指摘）・警告 3（助詞「で」「に」の連続）
- 2 回目：エラー 0・警告 1（#combine の助詞「に」の連続）
- 警告 1 件を直したが、検査の回数の上限のため再実行していない

## 確かめていないこと
- スキルのフロントマターに書いたフックの有効な範囲は、束にないので本文で「確かめる」と書くにとどめた
- 雛形 2 つは動作未確認。prettier の `--ignore-unknown` と、`tool_input.file_path` を stdin から読む形は、hooks-basics の既存の雛形に合わせたが、この環境では流していない
- 「既定ではフックの失敗で作業は止まらない」は束の F-1 の写しに基づく。版による違いは見ていない
- 最後の警告の直しは、検査を流して確かめていない

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
