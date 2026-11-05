# write.md：postmortems（執筆）

## 書いたファイル

- docs/judgment/postmortems.md（stub を書いた。stubs 側は既になかった）。front matter の変更：`sections` に 3 節を足した（decision-examples・what-you-hold・how-to-check）、`sources` に 3 件、`stage` を draft、`updated` を 2026-11-05
- snippets/postmortems/postmortem-entry.md と .expect.yaml（目次の templates の案。kind: other）
- snippets/postmortems/timeline-prompt.md と .expect.yaml（足した。時間線の抽出の依頼。kind: prompt）
- data/sources.d/postmortems.yml（新しい出典 2 件：sre.google の SRE Workbook 第 10 章、corporate.jcx.au のプレモーテム。ドメインは check_noai.py で確かめ済み）

## 必ず持つものの対応

- 判断例（状況・迷う候補・選んだもの・理由の 4 行）：#decision-examples（2 つ。共有環境のデータ消失〔鍵かお願いか〕、テストが実装をなぞる〔フックかレビューの観点か〕）
- 根拠の印とモデル・世代：#which-gap（SRE の型は根拠：中、AI への当てはめは類推）、#timeline（ELEPHANT は根拠：中、2025 年・当時の複数のモデル、現行の Claude の傾向にしないと明記）、#premortem（根拠：弱）
- 構成の目安（要点 → 何が起きるか → なぜ → 判断例 → 握るもの → 確かめ方）：#which-gap（何が起きる・なぜ）→ #timeline → #where-to-put-fixes → #premortem → #decision-examples → #what-you-hold → #how-to-check
- level：front matter の「仕組みにする」のまま

## メインに判断してほしいこと

- 出典 collins-premortem は本文を取得せず、調査資料の要約に拠る（sources.d の note に明記）。「30% は理由の数」の主張は、メインが原典か本文で確かめてほしい
- SRE Workbook は 1 回取得して確かめた（誰がでなく何が許したか、単一のオーナーと測れる完了状態、レビュー）。「別のメンバーが記録を確かめる」はチェックリストとレビューの記述を根拠にしたやや広い読み
- 目次の備考にある SSW Rules の insights 機能（過去のセッション分析）は、一次資料を開いていないので書かなかった
- 方針・約束の文は足していない（カード §13）

## 提案

- なし（用語集・prh・data・front matter の直しは出さない）
- 数値の提案もなし。ELEPHANT の 72% 対 22%・50 ポイントは、研究の名・年・対象を添えて本文に書いた。「本番の 1 か月前」は出典のない例と明記した

## 検査の結果

- 書き終えた後：エラー 1（sources.d の kind が使えない値）・警告 2。直した後の再実行：エラー 1（kind の直しを入れ損ねた）・警告 1。その後に kind を「実践者」へ、判断例の見出しを短く直したが、3 回目の検査は流していない（回数の決まりのため）
- 警告 1 は sentence-length（判断例の見出し行）で、見出しを短くして対処した。再確認していない

## 確かめていないこと

- 最後の直しの後の check_page.py の結果（上記）。メインの一括検査で確かめてほしい
- 2 つの雛形の動作（確かめていない旨は道具が書く）。判断例の状況は作った例
- 記録からの時間線の抽出の実際の返答
- 「AI が絡む事故の隙間の多くはお願いしかなく鍵がない形」は辞典の見立てで、件数の根拠はない（本文に推論と明記）

## 使用量

- 道具の呼び出し：約 19 回。Web の取得：1 回（SRE Workbook）
