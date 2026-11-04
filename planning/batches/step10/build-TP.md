# 工程10 TP：サイトのトップ docs/index.md

## 書いたこと

- 古い「ページはまだない」の文を消し、トップを書き直した。front matter は持たない（元のまま。check_pages が読むのは手書きのリンクだけ）。
- 構成：導入（辞書として引くこと・AI が書いていて公式でないこと）→ 引く入口は三つ → 検索で探す → 症状辞典と古くなった助言の台帳 → はじめて開いたとき。
- 三つの入口：困りごと（症状辞典 `field:symptoms`、逆引き `reverse-index#by-symptom`）、やりたいこと（`reverse-index#by-goal`、`roadmap`）、名前（`term-index`、`glossary`）。台帳は `outdated-advice-ledger`、はじめての人は `how-to-use`。
- 逆引きと症状辞典へは、トップから 1 クリックで着く（節の `#by-symptom`・`#by-goal` に直接）。
- 数値・名称・版は書いていない。リンクの中身はすべて道具が書いた。

## 作者に見てほしい文

方針に触れうるのは次の 1 文と 2 文目。新しい約束ではなく、承認済みの ai-and-sources の内容（AI が書く・非公式）の言い直し。詳しい方針は link で ai-and-sources を指している。

> この辞典は AI が書いていて、Anthropic の公式の教材ではない。書き方と確かめ方は（ai-and-sources#ai-writing へのリンク）にある。

連絡先は ai-and-sources#contact を指すだけで、連絡先そのものは書いていない。

## 検査

- `gen_site.py --page index` は使えない（トップは id を持たず「--page の id のページがない」になる）。トップの目印はサイト全体の生成でだけ埋まるので、リポジトリの写しを scratchpad に作り、そこで全体の生成を流して出力を確かめ、同じ中身を Write で本物に置いた。本物のリポジトリでは全体を流していない。
- check_pages.py：エラー 0、警告 4（他ページ分：比例則 3・前提と関連の数 1。index.md の分は 0）。
- textlint（docs/index.md）：直す前は 1 警告（助詞「から」の重複）、直して 0。
- `gen_site.py --check`：docs/assets/data/pages.json が古いと出る。トップの変更ではなく、既存の差（期限の日が日付で変わる類と思われる。未確認）。メインが全体の生成のときに更新される。

## 提案・気づき

- `gen_site.py --page index` が通ると担当が楽になる（トップを id なしで受け付けるか、トップ用の指定）。
- 道具の呼び出し：約 14 回（読み 5・scratchpad での生成 1・検査 6・書き 3）。
