# write.md：usage-credits-basics（執筆）

## 書いたファイル

- docs/cost/usage-credits-basics.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に hc-usage-credits・hc-usage-limits・hc-api-credits・hc-release-notes を入れた）
- sections に節を足した：when-to-use（先頭）・pitfalls・outdated。既存の 3 つの anchor はそのまま
- 雛形・図・data/sources.d は作っていない（目次の templates が「なし」。下書きに要る雛形も思いつかなかった）

## 必ず持つものの対応

- 冒頭の要点（何ができるか・いつ引くか・前提）：冒頭の囲み
- 機能の属性のバッジ（強制力など）：バッジ列はテンプレートが出す。本文の「強制力」の項は置いていない。data の usage-credits に enforcement などの属性がなく、`feature` の目印を置くと壊れるため（下の提案）
- tracks：front matter の `tracks: [usage-credits]`（既存）
- 使いどころ（どの原因を防ぐか）：#when-to-use
- 最小の使い方（面のタブ）：#set-a-cap（アプリ・Claude Code のタブ）
- 雛形：持たない（目次の templates が「なし」）
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#vs-api-credits（プランに付く API credits）。comparison のページは該当がなく、related の check-billing-path を指した
- 古くなった助言：#outdated（台帳の行を link、今どうするかを一言）
- level：front matter の「整える」（既存）

## メインに判断してほしいこと

- usage-credits の機能の属性（強制力・読み込みの時期など）が data にない。feature 型の「強制力」の項を置けていない。属性を足すか、このページは項を省くかを決めてほしい

## 提案

```yaml
proposals:
  - fact: {id: usage-credits-expiry-japan, title: usage credits の失効の期間（日本など）, value: "購入から 6 か月（2026-09-10 以降の購入分）", sources: [hc-usage-credits], checked: 2026-11-04, status: 確認済み}
    used_in: [usage-credits-basics#how-it-works]
```

本文は今、期間を書かずに「公式の記事で確かめる」としている。fact が入れば、#how-it-works の失効の段落に目印を置く。

## 検査の結果

- check_page を 2 回流した（書き終えた後と直した後）。エラー 0。警告 5（no-doubled-joshi）
- 警告のうち 2 つ（76 行・78 行）は、道具が作る link の題名（「並列・ループ・workflows のコスト › …」）が文に入って助詞が重なるもの。73〜74 行と 121 行は地の文で、直しきれていない。検証の担当が見てほしい

## 確かめていないこと

- 上限額に達したときの挙動（止まるか、通知だけか）。本文は断言していない
- Claude Code の `/usage-credits` コマンドの動作の詳細（本文は「コマンドがある」までしか書いていない）
- 自動の補充の細かい仕組み、Settings > Usage の画面の文言、Team・Enterprise の記事の内容
- 失効の期間・日付（提案の fact は data の note による。一次資料は開いていない）
- WSL・Linux 以外の OS と IDE 拡張（本文に「未確認」と書いた）

## 使用量

- 道具の呼び出し：約 11 回（Read 2・Bash 5・Write 2 など）。Web の取得：0
