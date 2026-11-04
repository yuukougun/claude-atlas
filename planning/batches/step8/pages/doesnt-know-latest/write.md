# write.md：doesnt-know-latest（執筆）

## 書いたファイル
- docs/symptoms/doesnt-know-latest.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 5 件を追加、sections に shapes・to-fixes・examples・prevention を追加。diagnosis の anchor は維持）
- snippets/doesnt-know-latest/date-and-source.txt・.expect.yaml（prompt。日付・版・資料を渡して答えさせる雛形）
- 出典は既存の id だけを使ったので data/sources.d/doesnt-know-latest.yml は作っていない

## 必ず持つものの対応
- 診断のチェックリスト（原因を安く確かめられる順。人の側の落とし穴）：#diagnosis（6 項目。人の側の落とし穴は節の末尾の 2 段落）
- 原因ごとの振り分け先（routes）：#to-fixes（`gen:begin routes`）
- 構成の目安の要点・よくある形：#shapes／判断例：#examples／予防：#prevention

## メインに判断してほしいこと
- 知識の締め切りの日付が data/facts.yml にない（grep で該当なし）。本文は日付なしで書き、fact の目印は置いていない。下の提案を入れたら、#diagnosis の 1 番に目印を足したい
- 型の手引きの「六つの原因を安く確かめる順」に対し、このページの prevents は「見えていない」の 1 つだけなので、1 つの原因の中を 6 つの確かめ（日付・版・検索・資料・検索結果の古さ・資料の薄い領域）に分けた。この解釈でよいか
- 項目 6 の「資料の薄い領域」は、材料 6.5（CTF の観察）を（根拠：弱・類推）で 1 文だけ使った。材料は 2 次の一般化なので、削ってもよい

## 提案
```yaml
proposals:
  - fact: {id: current-models-reliable-knowledge-cutoff, title: 現行モデルの reliable knowledge cutoff, value: "2026-06（モデルごと。Opus 4.6 は 2025-05）", sources: [api-docs-models-overview, api-docs-opus-4-6-overview], checked: 2026-11-04, status: 確認済み}
    used_in: [doesnt-know-latest#diagnosis]
  - fact: {id: current-models-training-data-cutoff, title: 現行モデルの training data cutoff, value: "2026-06（モデルごと。Opus 4.6 は 2025-08）", sources: [api-docs-models-overview, hc-up-date-training-data], checked: 2026-11-04, status: 確認済み}
    used_in: [doesnt-know-latest#diagnosis]
```
- 値は research/26 #12 の写しによる（束の 6.3・6.4）。モデルごとの表にするかは、メインが data の形に合わせて決める
- 用語集への提案：「reliable knowledge cutoff（確かな知識の日付）」と「training data cutoff（学習データの日付）」の区別が、knowledge-cutoff 側にあるか確かめたい（本文は「確かな知識の日付」「学習データの日付」と書いた）

## 検査の結果
- 1 回目：エラー 0・警告 3（助詞の重複 2、「六つ」1）→ 直した。2 回目：エラー 0・警告 0

## 確かめていないこと
- 雛形の動作（実際に Claude へ出していない）
- Claude Code と API の検索・取得の手段の説明は、束の材料にないので一般的な言い方にとどめた（Claude Code の許可の設定の影響、API の検索の道具の有無）。公式の文書では確かめていない
- 「Claude 自身に締め切りを聞く答えは自己申告」は一般的な注意で、出典なし
- アプリの Web 検索の記述は束の data（hc-web-search の要約）による。WSL 以外の OS と IDE 拡張は未確認
- Web の取得は 0 回

## 使用量
- 道具の呼び出し：約 13 回（Read 2、Bash 7、Write 3、ほか）。Web の取得 0 回
