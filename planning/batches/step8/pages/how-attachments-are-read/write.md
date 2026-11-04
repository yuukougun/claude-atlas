# write.md：how-attachments-are-read

## 書いたファイル
- docs/app/how-attachments-are-read.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 7 件、sections に pitfalls を追加）
- snippets/how-attachments-are-read/page-and-quote.{txt,expect.yaml}、what-did-you-read.{txt,expect.yaml}（目次の templates は「なし」。分かりやすさのために 2 つ足した）
- docs/img/how-attachments-are-read/pdf-ranges.svg（帯の図。境目の数字は入れていない）
- data/sources.d/ は新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点：冒頭の囲み（要点）
- 機能の属性のバッジ：テンプレートが出す。強制力は data の機能に値がなく、「強制力」の目印は置いていない（このページは強制の機能ではない）。属性の比べは {#api} の compare
- tracks：front matter の file-uploads・files-api。アプリは {#pdf-and-others}、API は {#api}
- level：使う（front matter）。{#api} は仕組みにする
- 構成の目安（使いどころ→最小の使い方→雛形→効かない場面→比べる相手→古くなった助言）：使いどころ＝{#pdf-and-others}、最小の使い方（面のタブ）＝{#verify}、雛形＝{#verify}、効かない場面＝{#pitfalls}、比べる相手＝{#api} の compare と feature-to-api-mapping#table への link、古くなった助言＝{#pitfalls} の末尾（台帳に行がないと一言）

## メインに判断してほしいこと
- 数値の目印が 1 つもない。data/facts.yml に PDF の上限などの facts がなく、目印を置けなかった。提案（下）が入ったら、{#pdf-and-others} の「境目のページ数と…公式の記事で確かめる」の文と、{#pitfalls} の上限の食い違いの項に目印を置く
- 判断例の「PDF に書き出すと図が残るか」は公式の資料にない（本文は「書き出しの結果次第」と書いた）
- 「強制力」の項目を要点に置かなかった。型の手引きの要求との差をどう扱うか

## 提案
```yaml
proposals:
  - fact: {id: app-pdf-visual-pages, title: アプリで PDF の図まで読まれるページ数の上限, value: 100 ページまで（文字と視覚要素）, sources: [hc-upload-files], checked: 2026-11-04, status: 確認済み}
    used_in: [how-attachments-are-read#pdf-and-others]
  - fact: {id: app-pdf-text-only-pages, title: アプリで PDF の文字だけが読まれるページ数の上限, value: 101〜1000 ページは文字だけ。1000 ページを超えると拒否, sources: [hc-upload-files], checked: 2026-11-04, status: 確認済み}
    used_in: [how-attachments-are-read#pdf-and-others]
  - fact: {id: app-upload-file-size-count, title: アプリのアップロードの大きさと数の上限, value: 会話は 1 ファイル 500MB・最大 20 ファイル、プロジェクトのファイルは 1 ファイル 30MB, sources: [hc-upload-files, hc-files], checked: 2026-11-04, status: 食い違いあり（ファイルの作成の記事はアップロードとダウンロードを 1 ファイル 30MB までと書く）}
    used_in: [how-attachments-are-read#pitfalls]
```

## 検査の結果
- 1 回目：エラー 0・警告 7（助詞の重複・読点）。直した後の 2 回目：エラー 0・警告 0
- 2 回目の後に、71 行目の 1 文を言い回しだけ変えた（検査は流していない）

## 確かめていないこと
- 本文の事実は束の写しに基づく。Web の一次資料は開いていない
- 雛形の動作は試していない
- lost in the middle の研究の対象モデルは確かめていない（本文は「当時の言語モデル」「類推」とした）
- 「ページの番号が PDF の印刷番号とビューアの通し番号でずれる」は一般の知識で、出典がない

## 使用量
- 道具の呼び出し 約 16 回、Web の取得 0 回
