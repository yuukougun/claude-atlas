# write.md：risk-tiered-approval（concept・team）

## 書いたファイル

- docs/team/risk-tiered-approval.md（stubs から移した。stubs の元ファイルは scratchpad へ退避。front matter で変えたキー：stage→draft、updated→2026-11-05、sections に principles-and-causes・misconceptions を追加、sources に claude-dev-blog-solving-code-review-anthropic〔data/sources.yml にある id〕）
- snippets/risk-tiered-approval/tier-table.md ・ tier-table.expect.yaml（目次の templates の案「リスクの段と承認者の表（例）」。kind: other、safety: false）
- data/sources.d/ は作っていない（出典は既存の id を使った）。図は作っていない（段と人数は表の雛形で足りると判断）

## 必ず持つものの対応

- 冒頭の要点の最初の項目が「何が分かるか」：冒頭の要点（abstract）の1項目目
- level を持つ：front matter の `level: 任せる`
- principle（確かめる・握る）を本文で名指す：#principles-and-causes
- prevents（確かめていない）を本文で名指す：#principles-and-causes
- pitfalls（同意を根拠にする）を本文で名指す：#principles-and-causes（#ai-approval-doesnt-count でも症状として触れた）
- 構成の目安（要点→何が起きるか〔例〕→なぜ→何に効くか→誤解→関連）：例は #three-tiers と判断例（#ai-approval-doesnt-count・#always-human）、なぜは #ai-approval-doesnt-count、何に効くかは #principles-and-causes、誤解は #misconceptions、関連はテンプレートの page-links。比喩付きの図は置いていない（組織の運用の話で、比喩の一覧に当たる語がないため）

## メインに判断してほしいこと

- 人の承認の数（0・1・2 人）と段の中身を、数値の目印にせず、記事（2026-10-15）の固定の記録として本文に書いた。「回数」に当たるなら facts に置く案が要る。当たらないなら今のまま。
- 本文の「承認のコメントに読んだ箇所を 1 行書く」「迷う変更は上の段に倒す」は独自の提案で、（推論・実践例なし）を付けた。
- 「承認の数を実際に強制できるかは、ホスティングの機能で確かめる（未確認）」とした。GitHub 等の設定の手順は束になく、書いていない。

## 提案

```yaml
frontmatter: []
```

用語集・prh・data への提案はない。

## 検査の結果

- check_page.py を 2 回流した。1 回目：エラー 0・警告 8。直した後：エラー 0・警告 5
- 残した警告：no-doubled-joshi 4 件（94 行目は link の目印の間の題名を含む文、109・118・138 行目は「が」の重なり）と max-ten 1 件（145 行目）。流す回数の上限のため直していない。検証と直しの担当に任せる

## 確かめていないこと

- 記事の原文は読んでいない。束の調査資料の写し（research/25 の P4・§3.3）に基づいて書いた
- 低の段の「セキュリティの確認」が具体に何を指すかは、束に説明がなく、本文でも定義していない
- ホスティング側の承認の数の強制の方法（未確認）
- 他の OS・IDE 拡張の動作は扱っていない

## 使用量

- 道具の呼び出し：約 12 回。Web の取得：0 回
