# 報告：執筆（competition-rules）

- 手引きの版：共通 2026-11-04 第1版・型（concept）2026-11-04 第1版
- 結果：本文は書き終え、stage を draft にした。検査は自分のページの指摘 0。ただし表は、数値の提案を data/facts.yml に足すまで空（下の 5 の 1）

## 1. 書いたファイル

- docs/contest/competition-rules.md（stubs/contest/ から mv。直したキーは sections〔`hold-the-boundary` を足した〕・stage〔draft〕・sources〔11 件〕。updated は 2026-11-04 のまま）
- docs/img/competition-rules/rules-by-type.svg（静的な図：主な大会を三類型の上に置く。類型を確かめていない大会は破線の欄。確認日 2026-11-04 を図の中に持つ）
- data/sources.d/competition-rules.yml（出典 9 件・domains 5 件〔x.com・ieeextreme.org・contest.ucup.ac・euc.icpc.global・procon.gr.jp〕。isucon2026-regulation と prtimes-u22-programming-contest-2026 は data/sources.yml のものを使った）
- planning/batches/step7/pages/competition-rules/facts-proposal.yml（数値の提案：表 `contest-ai-rules` の 1 項目）
- planning/batches/step7/pages/competition-rules/preview-with-facts.md（提案を足した試験の根〔リポジトリの外〕で表を出した本文の写し。表が空のページを読む検証役のため。直さない）
- 雛形：なし（目次の templates のとおり）

## 5. メインに判断してほしいこと

1. **表が空**：`<!-- gen:begin fact-table contest-ai-rules -->` は、facts-proposal.yml を data/facts.yml の facts に足して `gen_site.py --page competition-rules` を流すと出る。足す前は空で、check_pages は止めない（6 の 1）。検証役には、先に足すか、preview-with-facts.md を渡してほしい。事実の検証を置かない運用なので、足す前の照合は、ページの sources の 11 件の出典との突き合わせになる。
2. **方針の文に当たるか**（手引き §18）：節 unverified-versions の最初の段落「AtCoder と Codeforces のサイトは、AI の利用を断る指定を出している。この教材は、これらの規則の中身と版を確かめていない…」。方針の文なら、前半を削る（後半だけで通じる）。
3. **表に「禁止」の行がない**：ABC・ARC・AGC・短期 AHC・Codeforces は、類型も「未確認」にした（decisions「大会の規則の版」は版を未確認とする書き方で、類型は research/24 §2.4 が「禁止（二次の記録による）」。厳しく読んだ）。「二次の記録では禁止」と添えて類型を載せるなら、決めてほしい。
4. **表の備考は条文の要約に当たるか**（方針 A4）：備考は、類型の根拠を 1 文で書いたもの（例：Human Only は生成 AI 禁止）。当たるなら削ってよい（類型・版・日付は残る）。
5. **図は手書きで、表と食い違いうる**：類型の置き場と確認日を図に持つ。表の更新のたびに直す必要がある。図を生成にするか、更新の手順を決めてほしい。
6. **Codeforces の規則の URL がない**：開かないので所在を確かめられず、サイトのトップだけを置いた。作者が足すなら本文の箇条 1 行。
7. **kyopro-atlas との食い違い**（catalog contest#5 の続き）：atcoder-system#ai-rules へリンクし、「その節が書く版と適用範囲は確かめていない」と添えた。

## 6. 提案

- 数値：facts-proposal.yml（`contest-ai-rules`）。調査資料との違いを冒頭に書いた：ISUCON2026 の AI の許可の項目は「サーバー事項」でなく「ソフトウェア事項」の節にある（research/22 #45）／Universal Cup の録画は「決勝進出を望むチーム」に求める（告知。research/10 の「AI とのやりとりを映す」は規則の PDF の話で未確認）／長期 AHC は「AHC074 から」と公式 X からは言えない
- front matter・用語集・prh：なし
- 道具・手引き：
  1. check_pages「facts の id」は `fact` の目印だけを見る。`gen:begin fact-table <id>` に未登録の id を置いても止まらず、gen_site が「注意」を出すだけで、表が空のまま検査を通る。`fact` と同じに止めるか、手引き §9 に「提案中の表は fact-table の目印を置く」と書く案
  2. fact-table の表の下は、表全体の出典を 1 行に並べる（このページは 11 件）。schema は表のセルに `sources` を許すが、描画は使わない。行ごとの出典が分からないので、セルの `sources` を出す案
  3. リンクの目印の文字（題名 › 節の題＋「（準備中）」）が長く、前後の文が textlint の文の長さ（120 字）に当たりやすい。checking-ai-rules の節の題「なぜ規則が割れるか（三つの型）」は、節へ直接リンクしたページに漢数字の警告（三つ→3つ）を出すので、このページは当該の節へのリンクを避けた。節の題を直すか、手引き §10 に「目印の前後を短く」と書く案
  4. source_kinds に、主催者の公式 X の投稿に当たる種類がない（公式ブログで代用）。X の投稿を出典にする書き方（oEmbed で本文だけを読む・投稿の中のリンクはたどらない・domains は x.com）を手引き §11 に書く案。check_noai.py は x.com を「noai なし」と出すが、robots.txt は `*` にサイト全体の Disallow を置く

## 7. 検査の結果

- `gen_site.py --page competition-rules`：注意 1（fact-table の `contest-ai-rules` が data/facts.yml にない。表が空）。`--check` は最新
- `check_pages.py --page competition-rules`：エラー 0・警告 0。全体：エラー 0・警告 8（他ページの比例則 3・平文の欄 5）
- `npx textlint docs/contest/competition-rules.md`：0。`npm run lint:text`：自分のページの指摘 0（他ページの警告 1）
- `check_svg.py --page competition-rules`：警告 0・エラー 0。雛形はないので check_templates は流していない
- 試験の根（リポジトリの外の複製。提案を facts.yml に足した状態）：check_pages 0・0。自分のページだけの mkdocs build と `render_pages.py`（幅 390px・ライトとダーク）：エラー 0・警告 0

## 8. 確かめていないこと

- atcoder.jp・info.atcoder.jp・codeforces.com の本文は開いていない。本文の AtCoder のリンク先は、第三者の記録から写した URL（research/24 §2.4）。両サイトが AI の利用を断る指定を出していることは、この教材の記録（check_noai.py の KNOWN_NOAI）による
- 読んでいない文書：ISUCON2026 の当日マニュアル、高専プロコンの行動規範と応募要領、Universal Cup の規則の PDF、U-22 の募集要項、X の投稿が指す atcoder.jp の記事。2024-11-15 と 2025-10-04 の告知は、変更の中身を読んでいない
- 一次資料は 2026-11-04 に 1 回読んだだけ（改稿の履歴・写しは見ていない）。X は oEmbed の本文だけ。IOI 2025（ioi2025.bo）は名前が引けず確かめられなかったので載せていない
- CTF・データ分析・ハッカソンの規則は、一次資料で確かめたものがなく、表にない。形式を同じ厚さに扱う規則（手引き §16）は、この表では満たせていない
- 「学習の後に改定された規則は、渡さない限り Claude は知らない」は、一般の性質として書いた（公式の文書で確かめていない）

## 9. 使用量

- 道具の呼び出し 約 110 回（Read 15・Write 5・Bash 約 90）・Web の取得 約 26 回（X の oEmbed 7・規則などのページ 11・noai の確認 8）・かかった時間 約 40 分
