# 工程3 C0：目次の全候補の一覧（registry.yaml）の報告

- 担当：C0（2026-11-04）
- 書いたもの：[planning/catalog/registry.yaml](../../catalog/registry.yaml)（pages 378・ledger 35・notes 17）
- 形式：catalog/README §2 のキー（id・field・title・type・priority・level・origin・wave_core、ledger は id・title・origin）。1行に1項目の flow 形式にした（YAML としては README の例と同じ。担当が自分の分野を grep で拾えるように）
- 確かめたこと：指定のコマンドで `378 35` を確認した。加えて手元のスクリプトで、schema/site.yml の語彙（分野・型・優先度・段階）、id の一意と書式、ledger と pages の id の重なり、ledger・guide・hub と start に level がないこと、wave_core が核の分野だけにあること、自分の分野名を頭に付けていないこと、catalog/README §5 の機能の id と同じ綴りでないこと、00 §3 の300行を1回ずつ使ったことを検査し、エラーは0

## 1. 分野ごとの候補数

| 分野 | 目安 | 候補 | 必須 | 推奨 | 任意 | うち新しい候補 | wave_core |
| --- | --- | --- | --- | --- | --- | --- | --- |
| start | 8 | 8 | 8 | 0 | 0 | 1 | 4 |
| basics | 20 | 20 | 14 | 6 | 0 | 1 | 0 |
| surfaces | 11 | 11 | 3 | 5 | 3 | 0 | 0 |
| models | 14 | 14 | 6 | 5 | 3 | 1 | 0 |
| prompting | 24 | 24 | 13 | 10 | 1 | 2 | 0 |
| context | 19 | 19 | 12 | 5 | 2 | 1 | 0 |
| app | 22 | 22 | 11 | 8 | 3 | 0 | 0 |
| cli | 19 | 19 | 7 | 8 | 4 | 1 | 0 |
| extend | 26 | 26 | 17 | 8 | 1 | 0 | 0 |
| verify | 17 | 17 | 6 | 10 | 1 | 4 | 0 |
| eval | 13 | 13 | 4 | 8 | 1 | 10 | 6 |
| enforce | 15 | 15 | 8 | 6 | 1 | 2 | 0 |
| safety | 17 | 17 | 8 | 8 | 1 | 3 | 0 |
| delegate | 23 | 23 | 7 | 12 | 4 | 6 | 0 |
| judgment | 11 | 11 | 5 | 5 | 1 | 11 | 5 |
| api | 14 | 14 | 2 | 7 | 5 | 0 | 0 |
| cost | 12 | 12 | 5 | 5 | 2 | 2 | 0 |
| japanese | 12 | 12 | 3 | 7 | 2 | 0 | 4 |
| recipes | 22 | 22 | 4 | 11 | 7 | 8 | 0 |
| team | 16 | 16 | 1 | 8 | 7 | 7 | 0 |
| contest | 12 | 12 | 2 | 6 | 4 | 12 | 0 |
| symptoms | 25 | 26 | 16 | 10 | 0 | 6 | 26 |
| changes | 5 | 5 | 2 | 3 | 0 | 0 | 2 |
| 計 | 377 | 378 | 164 | 161 | 53 | 78 | 47 |

- 00 §3 の300行（必須151・推奨110・任意39）は 00 の優先度のまま。新しい候補78の優先度（必須13・推奨51・任意14）と、新しい候補の level は C0 の見当
- 「新しい候補」は 00 §3 にない候補（eval の3つは 00 分野09 から移したので数えていない）
- 目安と違うのは symptoms だけ（+1。§4 の1）

## 2. ledger の数

35。00 §5 の31項目と、research/22 §3.4 の「足す候補」4項目（Max の 5x と 20x → Ultra への改名、5時間の上限は待つしかない、Customize の各タブ、temperature を下げる）。research/22 §3.4 が「台帳ではなく数値ファイルと aliases で持つ」とした4つは入れていない。

## 3. まとめた候補

1. 00 §3 分野00「三つの原理」と requirements §3.1・§4.2 の「四つの原理」→ `four-principles`
2. 00 §3 分野09 の3つ（変更が効いたかを測る・体感と実測・/insights と /usage）と requirements §4.3 の「※ 00 分野09 から移す」→ eval の `measure-changes`・`felt-vs-measured`・`insights-and-usage-review`
3. requirements §4.3（eval 10・verify 4・judgment 11・contest 12）と §4.4（delegate 6・team 6・recipes 7・safety 3・enforce 2・cost 2・symptoms 5）の候補は、11 第1節の元の行と1項目にまとめ、origin に両方の行を書いた
4. requirements §4.2 の「主な変更」（basics・models・prompting・context・cli の5分野の6つ）も、11 第1節の行とまとめた
5. 11 第1節の中で、ほかの候補に含めたもの：小項目「採点の正本は一か所に」→ `test-the-verifier`、分野17 p56#21 と分野09 p34#175 → `agreement-is-not-evidence`、分野11 の解説節「なぜ規則が割れるか」→ safety の `checking-ai-rules` と contest の `competition-rules`
6. 00 の中で重なる候補（00 が別の分野に別のページとして置いたもの）はまとめず、registry の notes に組を挙げた（tokens と more-tokens-in-japanese など10組）

## 4. 判断に迷った点

詳しくは registry.yaml の `notes`（17項目）。主なもの：

1. **symptoms が目安より1多い**：11 第1節 分野01 が「分野18 に症状『要約が原文より断定的になる』も置く」と書くので `summary-overstates-source` を足した
2. **作らなかった候補**：11 の新「チームで使う意味」は、唯一の根拠の行に【2026-11-03 注記】があるので作らなかった（team の担当に判断を残した）。代わりに 11 の新ページ「AI は増幅器」を team に入れ、team は目安どおり16。ほかに、節「教える側」（decisions で教える側を読者に足さない）、「AI が最初の相談相手になると…」（既存ページへの追加）、データ点「ハーネスの価値」、「能力の凸凹」を分野01 に置く案は作っていない
3. **start**：人の側の落とし穴の入口（`human-pitfalls-intro`）と judgment の総論（`human-pitfalls`）が重なる。start は design §3.1 の規則2に合わせて level を持たせず、型を guide か hub にした。生成のページ（roadmap・reverse-index・glossary ほか）の型は仮
4. **境界**：api の「プロンプトの評価（eval）入門」は requirements §4.2 の数に合わせて api に残した（design §4.2 では評価の指標は eval）。contest の規則のページは、design §4.2 に合わせて「大会の規則の早見」とし、一般の類型と確認表は safety に置いた
5. **wave_core**：eval の `measure-changes` と `felt-vs-measured` に付けるかで迷い、付けた。felt-vs-measured は人の側の落とし穴エのページなので、judgment のア・イ・ウ・オのページとそろえた
6. **注記に合わせて題名を変えた**：Styles を外した（app）、fan-out の語を外した（delegate）、「5時間・週」を外した（cost）、output style の種類を並べない（cli）。origin に 00 の題名を残した
7. **decisions と食い違う候補**：cli の `for-non-engineers`（非エンジニア向けの説明は省く）。材料にあるので入れ、cli の担当に判断を残した
8. **設計書の例の id**：`instructions-ignored`・`request-vs-lock`・`hooks-basics`・`verifier-defines-problem`・`important-caps` は例のまま。例の `permissions-deny` に当たるのは `permission-rules`。`instructions-ignored` の level は 00 の L3 に従い「任せる」（設計書の例は「整える」）

## 5. 提案（共有のファイル・道具）

1. tools/check_catalog.py（T1）：「分野名を頭に付けない」の検査は、自分の分野の名前だけを見る形にしてほしい。basics の `context-rot` は用語そのもので、ほかの分野（context）の名前で始まる
2. 設計書 §2.2：生成のページ（逆引き・用語索引・ロードマップ・台帳の表など）を catalog でどう書くか（type を持たせるか、別の印を付けるか）を決めると、start と changes の担当が迷わない

## 6. 確かめていないこと

- 一次資料は見ていない（Web を使わない指示）。題名と id の英語の機能名は、調査資料の表記による
- 11 第1節の元ID の中身は 11 の要約で読み、作業ノート（11a〜11c）は読んでいない
- 00 §4（逆引き73項目）と §6 は読んでいない。逆引きから新しいページの候補が出るかは見ていない
- research/23〜28 は、00 §3 と 11 第1節の注記が案内する範囲でだけ参照した
- 同じ内容の候補が複数の材料に出るかは、題名と要点を目で照合した（機械的な照合はしていない）
- tools/check_catalog.py（作成中）では検査していない
