# 工程7 PF2 報告

## 当てたこと
1. #16：planning/catalog/judgment.yaml の agreement-is-not-evidence の節 hard-to-notice の題を「迎合された応答は信頼され、好まれる」にした（本文の見出しと同じ）
2. docs/changes/outdated-advice-ledger.md：`## 台帳 {#ledger}` に `ledger-index` の組を ledger の前に置き、導入の文を「一覧表で状態・時期・面を見比べ、古い助言の欄か検索で探す」に直した。表は埋まった。four-principles の指しは既に link の目印。台帳の行を指す所は、ページ内の `[…](#<行の id>)` で、平文ではないので変えていない（自分のページ内の行を指す link の目印は、使い方が card §9 にない）
3. docs/basics/agent-loop.md：節「何に効くか（原理「確かめる」と原因「確かめていない」）」{#what-it-helps} を誤解の前に足し、front matter の sections と planning/catalog/basics.yaml の agent-loop に sections（この1節だけ。context-rot と同じく、足した節だけ書く形）を足した。誤解の「台帳に行がある」は `outdated-advice-ledger#keep-going-dont-be-lazy` と `#add-double-check` の link の目印にした
4. docs/symptoms/caves-when-pushed.md：「よくある形」の後半の研究の要旨を1段落に縮め、仕組みは sycophancy の link で指した
5. docs/enforce/block-with-exit-2.md：「条件付き」、signs の記法を平文にした（ページと planning/catalog/enforce.yaml の364行目の項目。130行目の permission-rules の項目には触れていない）
6. 助詞・数字・文の長さの警告を直した（experiment-log・block-with-exit-2 も）

## check_page.py の結果（最終）
| ページ | エラー | 警告 |
| --- | --- | --- |
| competition-rules | 0 | 0 |
| experiment-log | 0 | 0 |
| block-with-exit-2 | 0 | 0 |
| agreement-is-not-evidence | 0 | 1 |
| outdated-advice-ledger | 0 | 1 |
| agent-loop | 0 | 2 |
| caves-when-pushed | 0 | 2 |

残る6件は、すべて link の目印が書く題の中の漢数字（四つの原理・五つの落とし穴・失敗の二つの軸）で、本文では直せない。competition-rules は fact-table の下の行ごとの出典が読める形で出ていた。caves-when-pushed と block-with-exit-2 は検査を3〜4回流した（2回では足りなかった）。

## メインの直しの確かめ
| 重さ | 場所 | 問題 | 直し方 |
| --- | --- | --- | --- |
| 直したほうがよい | common §11 / card §8 の X の投稿 | 直前の項目の「新しいドメインは check_noai.py で確かめ、断る指定があれば使わない」と並び、x.com には確かめを省くのか、確かめて例外にするのかが読めない。CLAUDE.md の「守ること」には例外がない | 「x.com は check_noai.py の結果が断る指定でも、投稿の本文だけなら使う」のように、例外の範囲を1文で書く。CLAUDE.md への反映は作者に相談 |
| 直したほうがよい | common §9・card §7 の「研究の結果は変わりやすい値に当たらない」 | CLAUDE.md の「数値を本文に手で書かない」と design §6.7 は直っておらず、食い違って読める | CLAUDE.md と design §6.7 に「研究の結果を除く」を足す（decisions に「作者が改めるなら戻す」とあるので、作者の確認の後） |
| 軽い | design §6.13 | 足した1行が区切り線 `---` の後ろ（§7 の直前）にあり、§6.13 に属して見えない | 区切り線の前に移す |
| 軽い | card §11 の concept・symptom | 足した文の前が「。」でなく空白で続く（「…教えない 「何に効くか」の節で…」「…手段だけ 仕組みや…」） | 「。」で区切る |
| 軽い | brief-page.md の版の行 | 「v3 は（v2 から：…）」の入れ子が読みにくい | 「v3.1（…）。v3 は…」と文を分ける |
| 軽い | decisions の「用語の正規形」 | requirements と catalog の「公式ドキュメント」を直さないので、prh の対象と食い違うかは書かれていない | 補足に prh での扱い（本文だけ検査）を1語足す |
| 軽い | design §6.4 と §8.5 のバッジ | 列は一致。「段階」は stage のこと | 問題なし（用語は「段階」で統一されている） |

## メインに判断してほしいこと
- 台帳の行を指す link の目印を、同じページの中の指しにも使うか。今は `[…](#id)`（in-page）で、card §9 の規則は他ページからの指しを想定している
- agent-loop の catalog sections は「足した節だけ」にした。全節を書くべきなら言ってほしい

## 提案
- tools/gen/config.yml の hosts を `outdated-advice-ledger: [ledger-index, ledger]` に（TB の提案）
- check_page の arabic-kanji-numbers：link の目印が書く題の中は、検査から外す（6件が本文で直せない）
- planning/catalog/enforce.yaml 130行目と permission-rules のページの signs にも同じ記法（`.env`）が残る。PF1 かメインが同じ文に直す

## 道具の呼び出し
Bash 約20、Read 0、check_page 約16（ページ複数）。Web 0。
