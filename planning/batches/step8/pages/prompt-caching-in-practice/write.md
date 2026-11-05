# write.md：prompt-caching-in-practice（feature・api）

## 書いたファイル
- `docs/api/prompt-caching-in-practice.md`（stub から移した。stage を draft、updated を 2026-11-05、sources を [api-docs-prompt-caching, api-release-notes]、sections に when・minimal・pitfalls・compare を足した。既存の prefix・invalidation・breakpoints は変えていない）
- `snippets/prompt-caching-in-practice/minimal-request.json` と `.expect.yaml`（kind: other。目次の templates は「なし」だったが、最小の使い方の節に要るので足した）
- `docs/img/prompt-caching-in-practice/prefix-blocks.svg`（目次の visual の案：3 段の積み木と、変えた段から後ろが無効になる図）
- `planning/batches/step8/pages/prompt-caching-in-practice/facts-proposal.yml`

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す（本文には書かない）。
- `tracks`（prompt-caching）：front matter に既にある。
- 1機能1ページ・公式の網羅をしない：全体（`#prefix` `#invalidation` `#breakpoints`）。API のパラメータは公式の文書へのリンクで済ませた（`#minimal`）。
- level（仕組みにする）：front matter に既にある。
- 構成の目安：要点（冒頭）→ 使いどころ `#when` → 最小の使い方 `#minimal`（面は api だけなのでタブは置かない）→ 雛形（`#minimal` の中の snippet）→ 効かない場面・落とし穴 `#pitfalls` → 比べる相手 `#compare`。古くなった助言は台帳の行がないので節を置かない。

## メインに判断してほしいこと
- 変わりやすい値（寿命・倍率・最小の長さ・区切りの数の上限）は本文に書かず、数字なしで読める形にした。facts に置いて目印で指すなら、facts-proposal.yml を取り込み、`#pitfalls` `#breakpoints` に目印を足してもらいたい。
- 比例則の警告（level が仕組みにする）が 1 件残る。目次の備考にあるとおり、任せる幅を広げる内容ではないので誤検出と考える。

## 提案
- facts：`facts-proposal.yml` の 4 件（status は要確認。確認日は調査資料 02 §5-2 の 2026-10-29 のまま）。
- front matter の提案：なし。

## 検査の結果
- 1 回目：エラー 0・警告 3（比例則 1、textlint の助詞「も」の重なり 2）。助詞を直して 2 回目：エラー 0・警告 1（比例則のみ、上の理由で残した）。

## 確かめていないこと
- 雛形の JSON の動作（API キーが要るので実行していない）。自動のキャッシュ（要求の外側の指定）の具体的な書き方は、一次資料を開いていないので本文に書いていない。
- 「messages の先頭側を書き換えると、その箇所から後ろが無効になる」「履歴を置き換える処理も一致を崩す」「最小の長さに届かない部分は対象にならない」は、束の「先頭が 100% 一致したときだけ」から導いた説明で、個別に公式で確かめていない。出力の順序や空白の揺れは（推論・実践例なし）と明記した。
- 区切りを複数置く「頻度の低い部分の末尾にも置く」は一般的な考え方で、公式の勧めは「変わらない最後のブロック」だけと束にある。
- 面は api だけなので、アプリ側は `#compare` で project knowledge の再利用に触れただけ（出典は調査資料の support 文書で、本ページの sources にはない）。

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 5、Write 7、Edit 2、検査 2 を含む）。Web の取得：0 回。
