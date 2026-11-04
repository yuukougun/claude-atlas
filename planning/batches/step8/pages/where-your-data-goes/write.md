# write.md：where-your-data-goes

## 書いたファイル
- docs/safety/where-your-data-goes.md（stubs から mv。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：sources（6 件、既存の id）、sections（what-it-prevents・misconceptions を追加。既存 4 つは不変）、stage、updated
- 雛形・図・data/sources.d は置いていない（目次の templates・visual が「なし」）

## 必ず持つものの対応
- 原理・原因への結び付け（principle 握る・prevents 境界がない）：#what-it-prevents
- pitfalls：front matter が空なので持たない
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解）：#consumer-vs-commercial（判断例）・#training-setting・#retention（なぜ）・#what-it-prevents・#misconceptions。比喩の図は置かず表で代えた

## メインに判断してほしいこと
- 数値の目印を置けていない：data/facts.yml に保持期間などの fact がなく、ない id を指すと止まるため、本文は数字なしで書いた。提案の fact を入れた後、#retention・#local-transcripts・#misconceptions に目印を置く
- プラン名（Free・Pro・Max・Ultra・Team・Enterprise）も変わりやすい値なので書かず「個人向け／商用」で書いた。名前の目印の使い方を決めてほしい
- 学校が配るアカウントの扱いは未確認と書いた（11 p34#215）
- 「API キーで使う Claude Code は API の側」は、束の「API は商用」から読んだ。公式で直接は未確認

## 提案
```yaml
proposals:
  - fact: {id: deleted-chat-backend-days, title: 消した会話がバックエンドから消えるまでの期間（日）, value: 30, sources: [privacy-long-store-data], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: training-opt-in-retention-years, title: 学習への利用を許可した会話が学習のパイプラインに残る最長（年）, value: 5, sources: [privacy-long-store-data, anthropic-news-updates-our-consumer-terms], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: violation-retention, title: 違反と判定された会話の入出力・分類スコアの最長（年）, value: 入出力 2・スコア 7, sources: [privacy-long-store-data], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: feedback-retention-years, title: フィードバックと /feedback・/bug・/share の保持（年）, value: 5, sources: [privacy-long-store-data, cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#retention]
  - fact: {id: local-transcript-cleanup-days, title: Claude Code の手元の記録の既定の保持（日。cleanupPeriodDays で変更）, value: 30, sources: [cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [where-your-data-goes#local-transcripts]
```

## 検査の結果
- 書いた後：エラー 0・警告 8（助詞の重なり）。直した後：エラー 0・警告 1
- 残した警告：「設定を切れば、過去に学習に使われた分も…」の助詞の重なり。分けると意味が切れるため

## 確かめていないこと
- 事実は束の写しに基づく。一次資料は開いていない（Web の取得 0 回）
- Claude Code の WSL・Linux 以外、IDE 拡張の動作は未確認と本文に書いた
- 設定の既定（新規利用者）は公式に書かれていないと本文に書いた
- 追加した 2 節の見出しと anchor が目次の sections と違う。目次側の反映が要る

## 使用量
- 道具の呼び出し 10 回ほど、Web の取得 0 回
