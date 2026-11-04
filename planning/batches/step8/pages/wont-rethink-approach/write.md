# write.md：wont-rethink-approach（執筆）

## 書いたファイル
- `docs/symptoms/wont-rethink-approach.md`（stub から移した。front matter で変えたキー：`sections`〔forms・routes・examples を足した。diagnosis は維持〕・`stage`〔draft〕・`updated`〔2026-11-05〕・`sources`〔既存の 7 件〕）
- `snippets/wont-rethink-approach/recheck-approach.md` と `.expect.yaml`（prompt。方針を見直させる依頼。動作は未確認）
- 新しい出典はなく、`data/sources.d/wont-rethink-approach.yml` は作っていない（7 件とも `data/sources.yml` にある）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめられる順。関われば人の側の落とし穴も）：`#diagnosis`（散らかっている → 確かめていない → やめられない → 預けすぎる）
- 原因ごとの振り分け先（routes）：`#routes`（`routes` の目印で生成）
- 構成の目安の要点・よくある形・判断例・予防：冒頭の要点／`#forms`／`#examples`（判断例 2 つと予防）。目安の「六つの原因」のうち、このページの `prevents` は 2 つ（散らかっている・確かめていない）で、残りは関わらないため診断に出していない

## メインに判断してほしいこと
- 診断の並び（散らかっている → 確かめていない）は front matter の `prevents` の順に従った。site.yml の並びは見ていない
- 「疑いすぎにも注意する」の段落を診断の末尾に置いた（decide-when-to-quit#dont-switch-too-often への案内。出典は Schulman、根拠：弱）
- 研究名のない言及（2012 年のメタ分析・166 標本・根拠：強）は Sleesman らの出典に基づく。ρ の値は書いていない

## 提案
なし（front matter・用語集・数値への提案はない）。

## 検査の結果
- 1 回目：エラー 0・警告 5（助詞の重なり）。直した後の 2 回目は流さず、警告 2 を直した文面の再確認は未実施（brief の「2 回だけ」に従い、1 回目の後の直しで 2 回目を流した。その結果は エラー 0・警告 2 で、残りの 2 件を文面を直して解消したが、再検査はしていない）

## 確かめていないこと
- 最後の直し後の textlint（警告 2 件を直した後の再検査）。助詞の重なりが残る可能性がある
- 雛形 `recheck-approach` の動作（expect は未確認の記録）
- 「会話が長くなると撤退を勧める」「直し続ける」の現象は、束の材料の写しだけに基づく（原文の記事は開いていない）
- 診断 4 の「評価・採否・撤退は人が握る」は what-not-to-delegate の要旨に従った。そのページ本文との整合は見ていない

## 使用量
- 道具の呼び出し 13 回（読み取り 5・検査 2・書き込み 6 ほか）、Web の取得 0 回
