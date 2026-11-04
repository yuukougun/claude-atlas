# write.md：using-research（執筆）

## 書いたファイル
- docs/app/using-research.md（stubs/app/using-research.md を移した。stage は draft）。front matter で変えたキー：`sections`（使いどころ・効かない場面と落とし穴・比べる相手を足した。既存の 3 anchor はそのまま）、`sources`（hc-research・claude-blog-research・claude-blog-integrations・hc-cowork-and-chat・hc-web-search-extended-thinking）、`stage`、`updated`
- snippets/using-research/research-request.md と .expect.yaml（目次の templates の案）
- snippets/using-research/claims-table-request.md と .expect.yaml（出典の対応表を作らせる依頼。分かりやすさのために足した）
- data/sources.d/using-research.yml は作っていない（出典はすべて data/sources.yml にある id）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す（本文には書かない）。強制力の 1 文は要点の囲みに手で書いた。data の research の項目に enforcement の属性がなく、`feature` の目印は使っていない（下の「メインに判断してほしいこと」）
- `tracks`（research・connectors）：front matter に変更なし。本文は #when-to-use・#with-connectors が当たる
- 1機能1ページ：リサーチ 1 機能を扱い、コネクタは #with-connectors で組み合わせだけを書いて持ち主のページ（connectors-in-the-app）を指した
- level：整える（変更なし）
- 構成の目安：要点（冒頭）→ 使いどころ #when-to-use → 最小の使い方 #requesting（面は app のみなのでタブなし）→ 雛形 #requesting・#checking-sources → 効かない場面・落とし穴 #limits → 比べる相手 #compare。古くなった助言は台帳に行がなく、置いていない

## メインに判断してほしいこと
- 強制力：data の research に enforcement がないため、要点に「リサーチは調べる機能で、条件は依頼に書くお願い」と手で書いた。バッジが要るなら、data の research に enforcement（お願い）の追加を検討してほしい
- 要点の「前提」の link が、生成後に search-research-thinking の題名で出ることだけ確認してほしい

## 提案
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし。使うモデルの名前を本文に出していない（束の data の note が「モデルは facts の値」とするが、research のモデルを指す fact がない）。出すなら次の fact の追加が要る
```yaml
proposals:
  - fact: {id: research-model, title: リサーチが使うモデル, value: 未記入（hc-research で確かめる）, sources: [hc-research], checked: 2026-11-05, status: 未確認}
    used_in: [using-research#when-to-use]
```

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 4（助詞の重複 3、「一つ」1）。直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 事実はすべて束（公式の Help Center とブログの写し）に基づく。一次資料は開いていない（Web の取得 0 回）
- 「使えるプラン」「面ごとの違い」は束の note の範囲で書き、プラン名は書かず公式の記事に回した
- 「起動しないときの安い順の 3 点」の順序は、束の事実（web 検索の有効化、問いの単純さ）からの整理で、公式の手順ではない
- 日本語の情報源の扱いと引用の質は、束の Gaps のとおり確かめた資料がない。本文もそう書いた
- 雛形の動作は確かめていない（アプリは制作の環境で試せない）
- 社内の資料と web が食い違うときの扱い、モバイルのローカル MCP の扱いは、束の記述の範囲を超えて断定していない

## 使用量
- 道具の呼び出し：約 14 回（読み込み 6、書き込み 7、検査 2）。Web の取得：0 回
