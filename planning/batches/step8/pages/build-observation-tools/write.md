# write.md：build-observation-tools（執筆）

## 書いたファイル
- docs/recipes/build-observation-tools.md（stubs から移した。stage を draft、updated を 2026-11-05、sections を 6 つ足した。ほかのキーは変えていない）
- stubs/recipes/build-observation-tools.md は削除（移動のため。Write で新規に書き、rm した）
- snippets/build-observation-tools/ask-for-tool.txt・.expect.yaml（目次の templates の案。open: true）
- snippets/build-observation-tools/ask-for-hand-check.txt・.expect.yaml（足した。手計算の確かめを頼む依頼）
- data/sources.d/ は作っていない（sources は空のまま。下の「確かめていないこと」を参照）

## 必ず持つものの対応
- 用途ごとの進め方（手順）：#flow（4 段、各段に終わりの印）。#what-to-build が作らせるものの範囲
- 確かめる・縛るのページへの道：#guards-first（think-before-asking・test-the-verifier#hand-calculated・over-reliance・how-much-understanding-to-keep）。前提は front matter の prerequisites の think-before-asking、関連は test-the-verifier ほか
- level を持つ：front matter の level: 任せる
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：要点 → #guards-first → #what-to-build → #flow → #hand-check → #how-to-check → #when-it-fails

## メインに判断してほしいこと
- 出典がない：束の出典の一覧が空で、材料（調査 10 第6章・11）の根拠は threadreaderapp・speakerdeck など check_noai.py 未確認のドメイン。本文の「上位者の考察の手順は共通（根拠：中）」は出典 id なしで置いた。出典を足すなら、ドメインの確認と sources.d の追加が要る
- 失敗のときの振り分け先に症状のページを置いていない（束に routes がなく、指せる症状の節がなかった）

## 提案
- 用語集・prh・data・front matter の提案はない

## 検査の結果
- check_page.py を 2 回流した。エラー 0・警告 3（no-doubled-joshi の「に」「に」「が」）。うち 1 件（54 行）は link の目印の間に道具が書いた他ページの題名を含む文で、手では直せない。残り 2 件（本文の 137・177 行）は、2 回目の後に直す機会がなく残した

## 確かめていないこと
- 雛形 2 つの動作（expect の項目）は試していない
- アプリのタブの記述（ファイルを渡してグラフや表の画面を作らせる）は、アーティファクトの機能の細部を一次資料で確かめていない。成熟度・プラン等は書いていない
- 「大会の規則で AI の利用が許されているかは主催者の規則で確かめる」の一文は、規則の中身には触れていない

## 使用量
- 道具の呼び出し：約 17 回（Read 4、Write 6、Edit 7 を含む Bash 3）。Web の取得：0 回
