# write.md：over-reliance

## 書いたファイル
- docs/judgment/over-reliance.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に 5 件、sections に `why-we-hand-over` を足した）
- 雛形・図・data/sources.d は無し（目次の templates は「なし」。sources は data/sources.yml に既にある id だけ使った）

## 必ず持つものの対応
- 判断例（状況・迷う候補・選んだもの・理由）：`what-to-keep`（解法の方針を Claude に選ばせる）
- level：front matter の 整える（束のまま）
- 構成の目安（要点→何が起きるか→なぜ→判断例→握るもの→確かめ方）：judgment-tasks・outside-the-frontier／why-we-hand-over／what-to-keep／cheap-verification

## メインに判断してほしいこと
- 節 `why-we-hand-over` を足した（目次の 4 節に「なぜ」がなかったため）。目次側の sections に反映するか
- 判断例は競技の練習の場面にした（scenes にコンテストがあるため）。開発の場面のほうがよければ差し替える

## 提案
- 用語集：「能力の凸凹（jagged frontier）」を本文で短く説明した。用語集に足すなら分野 basics か delegate の持ち主を決めてほしい
- 数値の提案は無し（研究の結果は固定の記録として、研究名・年・対象を添えて本文に書いた）

## 検査の結果
- 1 回目：エラー 0・警告 2（五つ→5 つ、「たとえば」の連続）。直した後の 2 回目：エラー 0・警告 0

## 確かめていないこと
- Dell'Acqua ほか（2023）の「19% 低い」と Vaccaro ほかの数値は、束（research/24 の一次資料の値）に従い、原論文は開いていない。出典は mollick-centaurs-cyborgs-jagged（解説）を sources に入れたが、原論文の id は data に無い
- Vasconcelos ほかは arXiv 2212.06823 の要旨だけ確かめた（N=731・5 つの研究・費用と得の枠組み）。「説明を足しても確かめる手間が大きいままなら依存は減らない」は要旨の示唆の読みで、原文の断定ではない
- 「確かめるのが安いほど依存が減る」を一般の LLM に当てはめる根拠は無く、本文は推論と書いた。Bucinca ほか（認知的な強制）は確かめていないので本文に使っていない
- Lee ほか・CSAW の数値は束の写しのみ。判断例と記録の基準（2 週・0 件）は独自の提案で、実践例なし
- 「Dell'Acqua の課題の難易が外から見えにくい」の一文は凸凹の説明としての一般的な書き方で、個別の出典は付けていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：1 回（arXiv の要旨）
