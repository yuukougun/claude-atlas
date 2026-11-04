# write.md：hits-limits-quickly（執筆）

## 書いたファイル
- docs/symptoms/hits-limits-quickly.md（stubs から mv。stage を draft、updated を 2026-11-05）
- front matter で変えたキー：sections（7 節）・stage・updated・sources（cc-docs-costs・hc-usage-limits・hc-usage-credits・cc-docs-interactive-mode。すべて既存の id）
- 雛形・図・data/sources.d は置いていない（目次の templates と visual が「なし」。新しい出典もなし）

## 必ず持つものの対応
- 診断のチェックリスト（安く確かめられる順。関われば人の側の落とし穴）：#diagnosis（項目 1〜6。人の側の落とし穴〔並列に任せすぎ〕は同節の末尾の段落）
- 原因ごとの振り分け先（routes）：#routes（`gen:begin routes`）
- 冒頭の要点・よくある形・判断例・予防：#forms・#examples・#prevention
- 追加の節：#when-stopped（止まった後の手）・#outdated（台帳の 3 行へ）

## メインに判断してほしいこと
- 診断の並びは、cause の名前（散らかっている・合っていない）の下に 5 項目を置いた（長さ・常駐・手戻り・モデルと effort）。「六つの原因を site.yml の並びで」は、このページの prevents が 2 つだけなので、手戻り→モデルと effort の順（saving-priorities の優先順位）に合わせた。site.yml の並びとの整合を見てほしい
- 診断の先頭に「長さの上限との取り違え」と、末尾に「枠の側（上限の種類・課金の経路）」を原因の外の項目として足した
- 面のタブ（アプリ・Claude Code・API）は診断の冒頭の「残りと内訳を見る場所」に置いた。API のタブは、束の check-billing-path の要約（従量課金・経路）だけに基づく

## 提案
- なし（用語集・prh・data・front matter への提案はない）。数値の提案もなし（数値は本文に書いていない）

## 検査の結果
- 1 回目：エラー 0・警告 3（助詞「が」「に」の重複。textlint）→ 3 か所を直した
- 2 回目：エラー 0・警告 0

## 確かめていないこと
- 「モデル別の上限だけ、別のモデルに替えて続けられる／全モデルの上限は替えても戻らない」は、research/05 の 1-12（cc-docs-costs の写し）による。一次の文書で再確認していない
- 「開いたままのセッションで待ち、戻ると自動で続ける機能」は台帳の行の記述による。版と回数の制限は数値になるので本文に書いていない
- アプリの「設定の Usage」と Claude Code の `/usage` の画面の見え方は、台帳の how_to_find と data の記述による。画面での確認はしていない
- 「別の会話で同じ作業ができれば長さの上限」という確かめ方は、束の long-chat-limits の要約からの推論。実機では試していない
- API の面の振る舞い（API 側の上限の形）は束にないので書かなかった
- 本文の link 先の節が、公開時に存在するか（指せる節の一覧にあるものだけ使った）

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
