# write.md：keep-failure-lessons（concept・context）

## 書いたファイル
- docs/context/keep-failure-lessons.md（stubs から mv。stage draft、updated 2026-11-05）
- front matter の変更：`sections` に what-happens・effect・misconceptions を足した（既存の both・what-to-keep・too-much は維持）、`sources` に ronacher-year-vibes・zenn-chiman-b233cc80（どちらも data/sources.yml に既存）、`stage`、`updated`
- snippets/keep-failure-lessons/save-before-rewind.md（prompt）・dead-ends.md（other。DEAD_ENDS.md の例）と、それぞれの .expect.yaml。目次の templates は「なし」だったが、分かりやすさのために 2 つ足した
- data/sources.d/keep-failure-lessons.yml は作らなかった（新しい出典なし）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 見せる・prevents 見えていない）：#effect で four-principles・six-causes を link して名指し
- level（任せる）・要点の最初が「何が分かるか」：冒頭の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #both（比喩は広い机）→ #effect → #too-much → #misconceptions → 関連（page-links の目印）
- pitfalls は空のため、名指すものなし

## メインに判断してほしいこと
- 「見えていない」「見せる」を four-principles・six-causes の whole-page link で指した（節の anchor は束にない）。check は通った
- 目次 notes の指示（「大量に読ませると消極的」は単独の経験談として本文で書く）に従い、#too-much に（根拠：弱・類推）で置いた。仕組みの説明は（推論・実践例なし）と明示

## 提案
- なし（用語集・data への提案なし。数値の fact なし）

## 検査の結果
- 1 回目：エラー 0・警告 3（no-doubled-joshi）。直して 2 回目：エラー 0・警告 2（155 行と 169 行の「に」の重なり）。上限の 2 回に達したので残した。意味は通る

## 確かめていないこと
- 巻き戻し（コードも戻す選び方）で DEAD_ENDS.md の追記が戻るかは、動かして確かめていない。ページには「必ず確かめる」と書いた（根拠は checkpoint の一般的な仕組みの理解のみ）
- 雛形 2 つは動かしていない。Kaggle 事例と Armin の指摘は束の写しのみで、原文は開いていない（Web の取得 0 回）
- アプリの手順（返答をコピーして新しいチャットに貼る）は一般的な手段で、アプリの機能は確認していない
- 判断例は作り物の状況

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回
