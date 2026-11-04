# write.md：seems-less-capable（執筆）

## 書いたファイル
- docs/symptoms/seems-less-capable.md（stubs から mv。stage は draft、updated は 2026-11-05）
- snippets/seems-less-capable/compare-record.txt と compare-record.expect.yaml（kind: other。前と今の条件を並べる記録票）
- front matter で変えたキー：`sections`（forms・routes-to-fixes・example・outdated・prevention を足した。diagnosis は変えず）、`sources`（既にある 6 件）、`stage`、`updated`
- data/sources.d/seems-less-capable.yml は作っていない（新しい出典がないため）

## 必ず持つものの対応
- 診断のチェックリスト（版・effort・モデル・会話の量の順、関われば人の側の落とし穴）：#diagnosis（1〜4 が原因、5 が体感を信じる）
- 原因ごとの振り分け先（routes）：#routes-to-fixes（`routes` の目印。front matter の `routes` は変えていない）
- 構成の目安の「よくある形」：#forms、「判断例」：#example、「予防」：#prevention
- 古くなった助言（think-hard-keywords）：#outdated

## メインに判断してほしいこと
- 診断で「版」を原因の名前に当てはめていない（版・effort・モデルは「合っていない」、会話の量は「散らかっている」と書いた）。catalog の想定と違うなら指示がほしい
- アプリの版の見方は束にないため「未確認」と書いた

## 提案
- 数値の提案なし。既定の effort の値は本文に書かず、`effort-levels#defaults-by-surface` を指した
- front matter の提案なし

## 検査の結果
- 1 回目：エラー 0・警告 4。直した後の 2 回目：エラー 0・警告 1
- 残した警告：58 行目の助詞「が」の重なり（`no-doubled-joshi`）。症状の言い回し（signs の「急に性能が落ちた気がする」）をそのまま見出し語に使ったため残した

## 確かめていないこと
- 雛形の記録票は動作を確かめていない（道具が旨を書く）
- 判断例は想定の場面で、実際に effort の段の違いを再現してはいない
- 変更履歴に `claude --version`・`/model`・`/effort` の挙動が今の版でどうかは、束の外のため一次資料で確かめていない
- 環境変数や設定が既定より優先される点は、束の research/23 §3.2 の写し（Model configuration を出典とする）による
- link の先の節の中身は、束の「指せる節」の題だけで確かめた

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
