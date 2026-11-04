# write.md：stuck-in-a-check-loop（執筆）

## 書いたファイル
- docs/symptoms/stuck-in-a-check-loop.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に pattern・routes・example・prevention を足し、sources に zenn-microsoft-78e01f59・zenn-hkdeveloper-claudeco・cc-docs-goal・cc-docs-scheduled-tasks を入れた）
- 雛形・図・sources.d は置いていない（目次の templates・visual が「なし」。出典は data/sources.yml にある id だけ使った）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順。関われば人の側の落とし穴）：#diagnosis（見えていない・散らかっている・合っていない、後に預けすぎる）
- 原因ごとの振り分け先（routes）：#routes（`gen:begin routes`）
- 構成の目安のうち、よくある形：#pattern／判断例：#example／予防：#prevention

## メインに判断してほしいこと
- routes の節を diagnosis の外（#routes）に分けた。stub では diagnosis の中だった。anchor の `diagnosis` は変えていない。他の symptom ページと並びを揃えるなら、戻してよい
- 実例の ISUCON13 の記事（zenn-microsoft-78e01f59）を取得して確かめた。記事に「対処として手法の知識や検索を与えた」記述はなく、今後の改善案として Agent Skills や検索用 MCP を挙げるだけだった。調査資料（11 の行）は「対処は…新しい仮説を入れること」と書く。本文は記事に合わせた。調査資料の表現の見直しを提案する
- 実例の対象は Azure SRE エージェントで、Claude とは限らない。本文は「類推」を付けた

## 提案
- 数値の提案はなし（本文に変わりやすい値を書いていない。時間の「約 1 時間」「3〜4 時間」は報告の時点の記録として、報告の名を添えて書いた）
- front matter の提案はなし

## 検査の結果
- 1 回目：エラー 0・警告 9。直した後（2 回目）：エラー 0・警告 6
- 残した警告：助詞「が・は・に・で」の重複 5 件（うち 2 件は link の目印の間に道具が入れた題名の展開の文が原因、残りは文の自然さを優先）と、126 行の文長 1 件（`page-links` の生成の展開）。生成の部分は手で直せない

## 確かめていないこと
- 「ループかどうか」の見分けの 4 つの目安と、診断の「どう確かめる」の手順は、一次資料に基づくものではなく、束の材料と前提のページの要約からの組み立て（推論）。実機で試していない
- 「基準を書いた日付が着手より後なら引きずられている」は、やめどきのページの趣旨からの言い換えで、元のページの本文は読んでいない
- 参考・page-links の生成後の見え方（準備中の表示を含む）は未確認
- 2 つ目の実例（無限検証ループ）は束の材料の写しだけで、元の記事は開いていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：1 回（zenn.dev の記事）
