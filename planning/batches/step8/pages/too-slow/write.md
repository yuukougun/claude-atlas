# too-slow 執筆報告

## 書いたファイル
- docs/symptoms/too-slow.md（stubs から mv。stage を draft、updated を 2026-11-05、sections を 6 節に、sources を [cc-docs-model-config, api-docs-effort, cc-docs-features-overview, cc-changelog] にした）
- 雛形・図・data/sources.d は作っていない（目次の templates と visual が「なし」）

## 必ず持つものの対応
- 診断のチェックリスト（安く確かめる順、人の側の落とし穴つき）：#diagnosis（項目 1〜6 が Claude 側、7 が人の側の「体感を信じる」）
- 原因ごとの振り分け先（routes）：#routes（routes の目印）
- 型の構成の目安（よくある形・判断例・予防）：#forms・#examples・#prevention。面ごとのタブは #by-surface

## メインに判断してほしいこと
- 診断の項目 1（障害・混雑）は六つの原因の外だが、最も安い確認として置いた。要らなければ外す
- 項目 6 は research/22 #21（CHANGELOG）に基づく。docs の sub-agents に記述がないため「2026-11 時点の CHANGELOG」と日付付きで書いた。古くなりやすい
- #prevention の seems-less-capable は節を指さずページを指した

## 提案
- 数値の提案はなし（本文に変わりやすい数値は書いていない。既定の effort は effort-levels#defaults-by-surface へ任せた）
- front matter のほかのキーの直しはなし

## 検査の結果
- 2 回流した。最後の結果はエラー 0・警告 3（no-doubled-joshi の「が」「は」。52 行目・58 行目・69 行目）。誤検出ではなく読みにくさの指摘だが、意味を変えずに直すには文の組み直しが要り、検査の回数の上限のため残した（review の担当が直す）
- 1 回目の警告 5 のうち max-ten の 2 つは直した

## 確かめていないこと
- 一次資料を開いていない（束の材料だけで書いた）。Web の取得は 0 回
- 「考えて」と書いた場合の挙動、アプリの効果は束の記述のみ。Claude Code の `--effort`・`/effort` の挙動を実機で確かめていない
- 診断項目 3 の「`/context` の内訳」を新しい会話の直後に見る手順は、inspect-context の要約に基づく
- 項目 5 の「既定のモデルに戻して比べる」の速さの効き方は材料に実測がなく、手順としての提案である
- 判断例 の「選ぶ順は、既定、effort、モデルの替え方の順である」はやや硬い。review で整えてよい

## 使用量
- 道具の呼び出し 9 回（Read 3・Bash 4・Write 2）、Web の取得 0 回
