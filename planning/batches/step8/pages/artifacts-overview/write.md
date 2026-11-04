# write.md：artifacts-overview

## 書いたファイル
- docs/app/artifacts-overview.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 6 件、sections に when・pitfalls を追加）
- snippets/artifacts-overview/create-request.{txt,expect.yaml}、scoped-edit-request.{txt,expect.yaml}
- planning/batches/step8/pages/artifacts-overview/facts-proposal.yml
- data/sources.d は作っていない（sources は data/sources.yml にある id だけ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す（本文に書かない）。強制力は data の artifacts に値がなく、`feature` の目印を置いていない
- tracks：artifacts・code-execution（変えていない）
- level：整える（変えていない）
- 構成の目安：要点（冒頭）／使いどころ #when／最小の使い方と雛形 #templates（create-request）・#editing（scoped-edit-request）／効かない場面・落とし穴 #pitfalls／比べる相手 #claude-design／古くなった助言は台帳の行がなく置いていない

## メインに判断してほしいこと
- 強制力の要点の項目：data の artifacts に強制力がなく、要点に足していない。足すなら data へ値の提案が要る
- 成熟度・プラン・上限・2026-09-16 の日付は本文に書かず、facts-proposal.yml に提案した。採用後は #templates の表に fact-table 等の目印を置く案（今の本文はプランと成熟度を公式の記事へ誘導している）
- 書き出し先の形式（Word・PDF など）を本文の表に確認日つきで手書きした。変わりやすい値に当たるなら、数値の提案へ移す

## 提案
- facts-proposal.yml（5 件）
- 用語集：legacy artifacts を短く定義して足す案

## 検査の結果
- 書いた後：警告 7・エラー 0 → 直して 1 回流した：エラー 0・警告 3（助詞「に」「が」の重複。冒頭の導入 1 件、#pitfalls の 1 件、#claude-design の 1 件。文の分割で直せるが、検査は 2 回までなので残した）

## 確かめていないこと
- 事実は束の写しだけが根拠。公式の記事を直接開いていない（Web の取得 0 回）
- 範囲を選ぶ「Edit with Claude」が Docs と Markdown のみか、モバイル・Desktop で同じかは確かめていない
- 共有の細部（取り消しの範囲・プラン差）は持ち主のページに任せ、内容を確かめていない
- 雛形 2 件の動作は試していない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得 0 回
