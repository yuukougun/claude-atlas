# how-memory-works 執筆報告

## 書いたファイル
- docs/app/how-memory-works.md（stub から移動。front matter で変えたキー：sections に `outdated-advice` を足した、stage を draft、updated を 2026-11-05、sources を [hc-memory, hc-incognito, hc-release-notes, lukyanenko-rogii-geosteering-kaggle]）
- snippets/how-memory-works/remember-request.md と .expect.yaml（目次の templates は「なし」。分かりやすさのために 1 つ足した）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す（本文には書かない）
- 「強制力」の目印：置いていない。app-memory の機能に enforcement の属性が束にないため。要点の「止められるもの」の 1 行で、止められるものと止められないものを書いた
- tracks：front matter（app-memory・chat-search・incognito）。本文は #what-is-saved・#chat-search・#turning-off が受ける
- 使いどころ（防ぐ原因）：冒頭の導入と #scope（境界がない）・#manage（散らかっている）
- 最小の使い方：#what-is-saved（面は app だけなのでタブなし）
- 雛形：#what-is-saved（remember-request）
- 効かない場面・落とし穴：#deleted-chats・#turning-off
- 比べる相手：#chat-search（表）・#scope（where-to-put-instructions へ link）
- 古くなった助言：#outdated-advice（台帳 outdated-advice-ledger#memory-daily-summary へ link）

## メインに判断してほしいこと
- 図（static の案）は描かず、#scope の表で代えた。プロジェクトの外の会話がプロジェクトのメモリを読むか、シークレットチャットがメモリを読むかが材料になく、図に断定を書けないため。図が要るなら材料を足してから
- hc-memory の記事の題名が材料の中で 2 つある（05 は旧 URL）。本文は題名を書かず、出典の一覧に任せた

## 提案
- facts-proposal.yml に 2 件（プランごとの既定、過去チャットの検索の対象プラン）。本文は数値・プラン名を書かないので、目印はまだない
- 用語集：「Topics（メモリの項目）」「Pause」「Reset」の追加を提案する（本文で短く説明した）

## 検査の結果
- 1 回目：エラー 0・警告 5（助詞の重複・読点）。直して 2 回目：エラー 0・警告 1（line 181 の助詞「が」の重複。意味が変わるので残した）

## 確かめていないこと
- 事実は束の写し（2026-10-29 確認の調査資料と data）だけに基づく。Web は取得していない。メニュー名（`Settings > Your Claude`・`Your memory`・`Use account memory` など）は画面で確かめていない
- Pause を戻せること（再開できること）は「項目が残る」としか書いていない
- 会話を消した後の過去チャットの検索、プロジェクト外の会話とプロジェクトのメモリの関係は未確認と本文に書いた
- 雛形は動作を確かめていない

## 使用量
- 道具の呼び出し：約 9 回、Web の取得：0
