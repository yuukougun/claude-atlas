# build-PL1：数値と強制力の目印（推奨 14 ページ）

## 置いた目印（ページごと）

- agent-sdk-basics：fact 2（setting-sources-default、permission-mode-default-noninteractive）
- asking-for-reasoning：fact 2（reasoning-extraction-since、refusals-billing-by-category。ともに未確認で「未確認」と出る）
- bare-mode：fact 3（partial-limits-before、setting-sources-leak-fix-version〔未確認〕、default-plan。後ろ 2 つは箇条を新設）
- character-encodings：fact 2（edit・write の版。未確認。括弧の形に置いた）
- choosing-a-plan：fact-table 1（plan-prices-individual）。「月額は表にない」を直した
- code-intelligence-plugins・insights-and-usage-review・side-questions-btw：feature 各 1（手書きの強制力の語を目印に替えた。補足の文は残した）
- loop-and-scheduling：fact 6（self-paced 範囲、expiry-days、max-tasks〔箇条を新設〕、loop-min、desktop-min、cloud-min）
- prompt-caching-in-practice：fact 4（max-breakpoints〔未確認〕、price-multipliers、min-length〔未確認〕、default-ttl）
- stateless-messages-api：fact 1（message-threads-lifetime。未確認）
- usage-credits-basics：fact 1（usage-credits-expiry-japan。未確認）
- visual-checks：既存の feature 目印の「値は数値ファイルの登録待ち」の括弧を外した（お願い と出る）
- postmortems：目印なし。「30% は理由の数」の一文を削った（rec3 の決め）

合計：置いた目印 24 組（fact 20、fact-table 1、feature 3）＋ visual-checks の括弧外し 1 ＋ postmortems の削除 1

## 置かなかった行

- choosing-a-plan の top-model-by-plan（任意の 2 行）：値の文が長く、未確認で「未確認」とだけ出るため、箇条の中で読めない。節（#plan-table）も今のページの文と合わない
- bare-mode の setting-sources-leak-fix-version など未確認の項目は、読める括弧の形に置いたので置いた

## check_page.py

全 14 ページ エラー 0（各ページ 1 回）。警告は既存の textlint（助詞・文の長さ）と prompt-caching-in-practice の比例則（前提・関連の追加）で、今回の目印によるものではない。

## 道具の呼び出し

約 26 回（Read 1、Bash 数回、Edit 約 28、check_page 14）。止められた操作なし。
