# write.md：suspected-degradation（執筆）

## 書いたファイル
- docs/models/suspected-degradation.md（stub から移動。stage を draft、updated を 2026-11-05、sources を 7 件に）
- snippets/suspected-degradation/degradation-log.md と .expect.yaml（確かめ記録の表。kind other）
- snippets/suspected-degradation/update-channel.json と .expect.yaml（autoUpdatesChannel を stable。kind settings）
- data/sources.d/suspected-degradation.yml（status-claude-com を新規。check_noai で noai の指定なし）

## 必ず持つものの対応
- 手順：#measure（「手順」の番号付きの 5 段。各段に「確かめ」）
- 確かめる・縛るのページへの道：前提 felt-vs-measured（#measure の冒頭と結果の読み方）、measure-changes（#measure の先に決めること・手順 4〜5）、nondeterminism（#measure）。front matter の prerequisites と related に既にある
- level：整える（front matter）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：守り＝#measure の「先に決めておくこと」、確かめ方＝#measure の「結果の読み方」、失敗したとき＝#if-product-side の末尾（seems-less-capable#diagnosis へ）

## メインに判断してほしいこと
- #postmortem-example の表の日付とモデル名は、ポストモーテム本文（WebFetch の要約）で確かめた過去の固定の記録として本文に直接書いた。facts に置くべきなら、そう指示してほしい
- 「API は含まれない」は WebFetch の要約の記述。報告の原文の該当文で再確認してほしい（要約を通した確認のため）

## 提案
- 用語集：「ポストモーテム」（事後報告）が用語集にあるか未確認。なければ追加を提案する
- 出典：status-claude-com は data/sources.d に置いた。共有の data/sources.yml へ移す必要があればメインが反映

## 検査の結果
- 1 回目：エラー 0・警告 5（助詞「が」の重なり。リンクの題名「気がする」との連続を含む）。言い換えて 2 回目：エラー 0・警告 0

## 確かめていないこと
- `/effort` と `/model` が現在の値を表示する動き、アプリのメニューに effort があること（facts の note に基づく）は手元で実行していない
- `autoUpdatesChannel` の設定ファイル上の置き場所（user の settings.json 直下）と、stable が実際に遅れた版を渡すことは、research/22 の記述（settings-reference の autoUpdatesChannel）に基づき、動かして確かめていない
- `/feedback` で送られる内容は確かめていない（本文は「公式の文書で確かめる」と書いた）
- Pro・Max と API キー等で戻しの時期が違う点は research/23 F3 の CHANGELOG の記述に基づく。版番号は本文に書いていない
- 報道が挙げる教訓の部分は二次情報（根拠：弱）

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 2 回（status.claude.com、Anthropic のポストモーテム）
