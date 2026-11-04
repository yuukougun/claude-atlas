# write.md：how-skills-load（concept・extend）

## 書いたファイル
- `docs/extend/how-skills-load.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections を 8 節に、sources を既にある id 5 つに変えた）
- `docs/img/how-skills-load/layers.svg`（段階的な読み込みの図。static の案どおり）
- `planning/batches/step8/pages/how-skills-load/facts-proposal.yml`（数値の提案 1 件）
- 雛形・`data/sources.d/how-skills-load.yml` は置かない（雛形の案がなく、出典は既存の id で足りた）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 見せる／prevents 散らかっている・見えていない）：`#effects`
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#what-happens`・`#why`・`#effects`・`#misconceptions`、関連は page-links
- pitfalls は空なので名指す対象なし（入れすぎのコストは `#residual-cost`）
- 比喩付きの図：`#why`（広い机＝コンテキスト）
- 圧縮の後に戻るもの（front matter 既存の節）：`#after-compaction`

## メインに判断してほしいこと
- 説明文が圧縮の後に作り直される挙動は、入った版を本文に書かず「公式の変更履歴で確かめる」とした。facts に版の項目を足せば目印にできる（下の提案）。

## 提案
- facts-proposal.yml を参照（`skill-description-rebuild-min-version`）。本文の足し先は `how-skills-load#after-compaction` の「説明文」の項目。
- front matter の変更の提案：なし。

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 5（助詞「に」「が」の重なり）。直して 2 回目 エラー 0・警告 0。

## 確かめていないこと
- 事実は束の写し（research/01 D-2・23・02 §1-10）と data の項目に基づく。公式の文書は開いていない（Web の取得 0 回）。
- API の読み込みの段階が Claude Code と同じ順かは未確認で、本文にもそう書いた。
- アプリの画面の操作（Customize の名前の変更）は展開中なので、本文では画面名を書かず skills-in-the-app に回した。
- claude.ai のスキルが Claude Code に同期される件、Agent Skills の財団への移管は、束の備考どおり一次資料で確かめていないため書いていない。
- 補助ファイルの中身が圧縮で要約に溶けうるという記述は、束の「必要になったら読み直す」「要約に溶ける」の表からの推論で、公式の明文は確かめていない。
- 目印の展開（`feature skills/load_timing` など）の見え方は、ビルドして目で見ていない。

## 使用量
- 道具の呼び出し 約 16 回、Web の取得 0 回
