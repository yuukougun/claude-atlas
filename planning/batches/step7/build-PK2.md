# build-PK2：束に「型の必ず持つもの」の節を足す

## 変えたこと
- tools/make_packet.py：節「## 1b. 型の必ず持つもの」（`sec_type_musts`）を「1 ページ」の直後に足した。型の手引き planning/guides/<型>.md の「## 1.」「## 2.」を、見出しを1段下げて中身はそのまま写す。手引きのない型は「この型の手引きはない」の1行。束の冒頭の構成の行・--stats の内訳・道具の説明（docstring）も合わせた。既存の節の番号は変えていない（番号が固定なので 1b とした）。
- tests/tools/test_make_packet.py：試験を2つ足し（節の写し・手引きのない型）、--stats の正規表現を8区分に直した。
- tests/tools/fixtures/packet/planning/guides/concept.md：試験用に §1〜§3 を足した。

## 試験
test_make_packet.py 92 件が通った（最後の実行）。

## 束の大きさの増え（一時フォルダに作成。state/packets は未変更）
- agent-loop（concept）：+532 字（20387 字になった）
- experiment-log（recipe）：+258 字（15724 字になった）

## メインに判断してほしいこと
- 節の名前を「1b」にした（番号固定を崩さないため）。「2」以降を繰り下げる案もある。
- 既存の束は作り直していない。反映は `make_packet.py` の再実行が要る。

## 道具の呼び出し
約 11 回。
