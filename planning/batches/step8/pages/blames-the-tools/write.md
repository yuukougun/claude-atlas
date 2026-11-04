# write.md：blames-the-tools

## 書いたファイル
- docs/symptoms/blames-the-tools.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-sandboxing を追加、sections に forms・routes-to-fixes・example・prevention を追加。diagnosis の anchor は変えていない）
- snippets/blames-the-tools/ask-for-raw-output.txt と .expect.yaml（kind: prompt。「壊れた」の根拠を生の出力で出させる依頼）

## 必ず持つものの対応
- 診断のチェックリスト（安く確かめる順。人の側の落とし穴を含む）：#diagnosis（1 人が自分で実行 → 2 見えていない → 3 散らかっている → 4 確かめていない。末尾に人の側の落とし穴 2 つ）
- 原因ごとの振り分け先（routes）：#routes-to-fixes（`gen routes` の目印）
- 構成の目安の残り：よくある形 #forms／判断例 #example／予防 #prevention

## メインに判断してほしいこと
- 六つの原因の「安く確かめる順」を site.yml で確かめていない。prevents の並び（見えていない → 散らかっている → 確かめていない）のまま並べ、先頭に「人が同じ操作を自分で実行する」を足した。順が違えば直してほしい。

## 提案
- なし（数値の提案・front matter の変更の提案ともになし）

## 検査の結果
- 書き終えた後：エラー 0・警告 3（助詞の重なり 2・算用数字 1）→ 直した後：エラー 0・警告 0

## 確かめていないこと
- CTF の「数ミリ秒で『基盤が壊れた』と判断」の例は、束の 11 と 10 第14章の写しだけに基づく。DEF CON 33 の原文は開いておらず、sources に入れていない（本文は出典 id なしで根拠の印のみ）。出典に足すなら check_noai.py での確認と原文の確認が要る。
- 判断例は想定の場面で、実際の事例ではない。雛形の動作（expect）は実機で試していない。
- 「サンドボックスが効く範囲」は束の data の note（cc-docs-sandboxing）に基づく。公式の原文は開いていない。

## 使用量
- 道具の呼び出し：約 12 回（検査 2 回を含む）。Web の取得：0 回
