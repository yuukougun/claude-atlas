# write.md：misses-broken-evaluation（執筆）

## 書いたファイル
- docs/symptoms/misses-broken-evaluation.md（stubs から mv。stage draft、updated 2026-11-05）
- snippets/misses-broken-evaluation/audit-evaluation.txt と .expect.yaml（評価の点検を頼む依頼。目次の templates は「なし」だったので、診断の分かりやすさのために足した）
- front matter で変えたキー：sections（forms・routes-to-fixes・example・prevention を足した。diagnosis は変えず）、sources（既存の id 7 件）、stage、updated。data/sources.d/misses-broken-evaluation.yml は、新しい出典がないので作っていない

## 必ず持つものの対応
- 診断のチェックリスト（原因を安く確かめる順。人の側の落とし穴も）：#diagnosis（差の確定 → 1 リーク・採点の誤り → 2 書き換え → 3 本番を代表しない → 4 指標のずれ → 5 預けすぎる〔人の側〕）
- 原因ごとの振り分け先（routes）：#routes-to-fixes（routes の目印）
- 型の構成の目安のうち、要点・よくある形・判断例・予防：冒頭の要点、#forms、#example、#prevention

## メインに判断してほしいこと
- 「よくある形」の最初の 2 件の出典は束の材料メモ（10 第8章。ANDPAD の 10 実験目の話と、Pebblous の要約が伝える研究）にだけ頼り、元の記事は開いていない。ANDPAD の例の対象モデルは「未確認」と書いた。公開の前に原文での確認を勧める
- 診断の項目 5 の「エージェントが自分の作業を高く評価しやすい」は、anthropic-eng-harness-design-long-running（束の 10 第18章の写し）に基づく。同じ流れで評価を確かめる役を持たせない、という書き方にした

## 提案
- 用語集：OOF（学習に使わなかった分の予測）を本文で短く定義した。用語集に項目があるか、なければ追加を提案する
- 数値の提案：なし（研究の固定の結果だけを、名前・年・対象のモデルを添えて書いた）

## 検査の結果
- 1 回目：エラー 0・警告 6。直した後：エラー 0・警告 4
- 残した警告：確認を実行（症状の言い回しとして「計画した確認を実行しない」を使った。誤検出に近い）、「に」の重複と文の長さ各 1〜2 件（link の目印の間に道具が入れる題名が長いため）

## 確かめていないこと
- 本文の事実は束の材料メモにだけ基づく。一次資料（ANDPAD・Pebblous・SpecBench・Lukyanenko・DrivenData・Battlecode・harness-design の各記事）は開いていない（Web の取得 0 回）
- 数値（QWK 約 1.0 と 0.44 前後、43〜48 ポイント、70% 超）は、束の写しのまま。Pebblous は二次の要約のため根拠を弱にした
- 雛形は動作を確かめていない
- 未公開のページへの link（suspect-too-good-results など）は「準備中」で出る

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
