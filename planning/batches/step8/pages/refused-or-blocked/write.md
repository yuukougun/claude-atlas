# write.md：refused-or-blocked

## 書いたファイル
- `docs/symptoms/refused-or-blocked.md`（stubs から移動）。front matter で変えたキー：`sections`（forms・examples・prevention を足した。既存 3 つの anchor は不変）・`sources`（hc-switched-models・hc-output-blocked・api-docs-refusals・cc-docs-errors・cc-docs-permission-modes）・`stage`（draft）・`updated`（2026-11-05）
- 雛形・図・`data/sources.d/` は作っていない（templates・visual の案なし。出典は既存 id のみ）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順）：`#diagnosis`（見えていない → 散らかっている → 合っていない の順。残りの原因は six-causes へ振る）。その前の `#what-stopped` で利用ポリシーか操作の停止かを先に見分ける
- 人の側の落とし穴：`#diagnosis` の末尾の段落（言い換え・小分けで通そうとしない。pitfalls は空なので 1 点だけ。why-not-evade を指す）
- 原因ごとの振り分け先（routes）：`#diagnosis` の直後の `gen:begin routes`
- 構成の目安のうち、よくある形 `#forms`・判断例 `#examples`・予防 `#prevention` を持つ

## メインに判断してほしいこと
- 「人の側の落とし穴」は pitfalls が空のため、言い換えて通そうとする癖を 1 段落だけ本文に書いた。pitfalls への追加が要るかは判断を仰ぐ
- 「合っていない」の枝に、フックの停止の見分け方（理由の文面が自分の書いたものと一致する）を書いた。記憶に頼らず束の材料だけで書いたが、面ごとの表示は未確認

## 提案
- 数値・用語集・prh・front matter への提案はなし

## 検査の結果
- 1 回目：エラー 0・警告 1（max-ten）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 面ごとの表示の文・切り替えの対象モデル・版の値は本文に書いていない（when-requests-are-refused に任せた）。リンク先の節の中身は束の要約でしか確かめていない
- 「Recently blocked」で見直せる操作は auto モードが止めたものに限る、という書き方が data の名前の項目と合うかを実機では見ていない
- 4 つのうち「検証の制度」への案内は official-steps に任せ、本文では直接触れていない

## 使用量
- 道具の呼び出し 7 回前後、Web の取得 0 回
