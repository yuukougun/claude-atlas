# write.md：requesting-prose

## 書いたファイル

- `docs/prompting/requesting-prose.md`（stubs から移動。stage を draft、updated を 2026-11-05、sources に既存の id 3 つ〔ruben-hours・api-docs-prompting-best-practices・api-docs-prompting-claude-fable-5-1〕、sections に guards・check・failure を足した。既存の 3 anchor は変えていない）
- `snippets/requesting-prose/write-brief`・`dislike-examples`・`revise-pass`（各 .txt と .expect.yaml。目次の templates は「なし」だったので、分かりやすさのために 3 つ足した）
- 新しい出典ファイルは作っていない（既存の id だけを使った）

## 必ず持つものの対応

- 用途ごとの進め方：reader（読み手・目的・分量・手本を渡す）、concrete-dislikes（嫌な点を例で示す）、revise（推敲の手順）
- 手順：revise（3 段。各段に確かめを付けた）
- 確かめる・縛るのページへの道：guards（disclosure-and-provenance#four-points）、check（consistent-politeness#lint）、failure（show-examples#overfit・output-shape#length・consistent-politeness#failure・less-ai-sounding-japanese#failure）。front matter の prerequisites は show-examples、related は 5 ページ
- level：整える（front matter のまま）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：guards → reader・concrete-dislikes・revise → check → failure の順

## メインに判断してほしいこと

- 本文の「公式のモデル別の手引きにも…装飾的な文体を外すよう一文で頼む例がある」は、モデル名を書かず（今のモデル名は目印で書く決めのため）、束 6.3 の Fable 5.1 の手引きの一文に基づく。出典 id は sources に入れた。モデル名を出す要不要の判断をお願いする
- 「AI っぽい」は読みやすさの品質として扱い、AI が書いたと分からなくする方法は書いていない（方針 B4）

## 提案

- なし（front matter・用語集・data への提案はない）

## 検査の結果

- check_page.py：1 回目 エラー 0・警告 8（助詞の重複 6、冗長表現 2）→ 直して 2 回目 エラー 0・警告 0
- 冗長表現の警告は、嫌な言い回しの実例として書いた「〜することが可能です」が原因だったので、例を「〜という点が挙げられます」に替えた

## 確かめていないこと

- 雛形 3 つの動作（動かしていない。expect は想定）
- 「形容詞より具体例が直る」の根拠は束にある実践者 1 件と、公式の「具体的に書く」助言だけ（根拠：弱と印を付けた）。効き方の程度は未確認
- 雛形 dislike-examples.txt の先頭が「After：」で始まる。本文の Before との対応を示すためだが、そのまま貼る使い方では不要なので、検証の担当が見直してよい
- sources の 3 つの id の URL・内容の再確認はしていない（既存の登録を使った）

## 使用量

- 道具の呼び出し 約 12 回、Web の取得 0 回
