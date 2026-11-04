# write.md：where-bypass-is-ok

## 書いたファイル
- docs/safety/where-bypass-is-ok.md（stub から移した。stage draft、updated 2026-11-05）
- snippets/where-bypass-is-ok/disposable-checklist.md と .expect.yaml（起動前の確認の一覧。kind other、safety true）
- front matter で変えたキー：sections（decision・what-it-prevents・misconceptions を足した。既存の 3 節の anchor は変えていない）、sources（束のデータが挙げる cc-docs-permission-modes・cc-docs-permissions・cc-docs-security・cc-docs-claude-code-on-the-web・cc-docs-headless。data/sources.yml にある id のみ）、stage、updated

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 縛る・prevents 境界がない）：#what-it-prevents
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#why-isolate（なぜ・何が起きるか）／#requirements／#not-a-substitute／#decision（判断例）／#what-it-prevents／#misconceptions。関連はテンプレートの page-links
- pitfalls：front matter が空のため持たない

## メインに判断してほしいこと
- 目次の templates の案は「使い捨てのコンテナで無人の実行を動かす手順の例」。カード §10 は、使い捨てのコンテナは試せず、回避された仕組みを守りとして勧める雛形は載せない、とする。そこで Dockerfile や起動コマンドではなく、条件だけの確認の一覧を雛形にした。コンテナの具体の手順を載せるかは判断を仰ぐ
- 本文の「この辞典の推奨」（秘密を入れない・届く範囲を限る・通信の宛先を絞る・差分で取り出す）は、束の材料にない推論で、（推論・実践例なし）と明記した。必須ページの中心にしない形（公式の条件を先に置いた）だが、確認を頼む
- #not-a-substitute と誤解の節で台帳 outdated-advice-ledger#yolo-skip-permissions を指した。束の「指せる節」の一覧にないが、カード §11 の指定どおり。anchor が存在しない場合は check の結果で止まるはず（検査は通った）

## 提案
- 用語集・data・prh への提案はなし
- 数値の提案なし（本文に変わりやすい値を書いていない。permissions.blockWritesOutsideWorkingDirectories の入った版、auto の既定、-p の既定は本文に書かず、持ち主のページと台帳へ回した）

## 検査の結果
- 1 回目：エラー 0・警告 4（助詞の重複 3、1 文の長さ 1）。直した後の 2 回目：エラー 0・警告 1（助詞の重複）。その 1 件は、2 回目の後に語を言い換えて直した。言い換えた後は流していない（検査を 2 回までの決まりのため）

## 確かめていないこと
- 事実は束の材料（01 C-1、research/22 §3.4、05 4-8、台帳）に基づく。一次資料を開いて確かめ直していない（Web の取得 0 回）
- 「クラウドセッション：資格情報が VM に入らず proxy で付与、ブランチの削除とタグの push は拒否、監査ログ」は 05 4-8 経由の二次の記述。現行の Security の文書で確かめていない
- 「root や sudo では起動を拒否」「インターネットを遮断した環境でのみ」は 01 C-1 の写し。現行の文書の文言とは照合していない
- 最後の言い換えの修正後に textlint を流していない
- 手元の PC で auto モードと sandbox を無人で動かす形（判断例の候補）が実際に問題なく回るかは確かめていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
