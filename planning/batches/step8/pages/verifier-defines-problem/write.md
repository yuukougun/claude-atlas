# write.md：verifier-defines-problem

## 書いたファイル
- `docs/eval/verifier-defines-problem.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections に `why`・`misconceptions` を足した、sources に既存の 5 件を足した）
- `docs/img/verifier-defines-problem/loop.svg`（ループの図。目次の visual 案どおり）
- 雛形・`data/sources.d/verifier-defines-problem.yml` は置かない（理由は「確かめていないこと」）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`・`prevents`・`pitfalls` を名指す）：`#verifier-first`（確かめる・握る・確かめていない・預けすぎる）
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#loops-amplify`・`#why`（図あり）・`#verifier-first`・`#misconceptions`・`#map`（関連はテンプレートが下部に出す）

## メインに判断してほしいこと
- 節を 2 つ足した（`#why`・`#misconceptions`）。構成の目安に合わせたもの。外すなら言ってほしい
- 「評価と実験の地図」`#map` は、related 全 12 ページへの手書きの案内にした。hub 的な役割と重なるなら削ってよい

## 提案
- なし（用語集・prh・data・front matter の他キーへの提案はない）

## 検査の結果
- 1 回目：エラー 0・警告 7。直して 2 回目：エラー 0・警告 1
- 残した警告：62 行目の sentence-length（Before/After の After の依頼文の「」書き。依頼文を 1 つにまとめた引用なので残した）

## 確かめていないこと
- 本文の事実は束の写し（requirements・research 10/11/24）からだけ書いた。一次資料の Web 取得は 0 回。ALE-Bench の数値、CORE-Bench の 42%→95%、Anthropic のサイバー競技の報告の「上位 25%」は、束の写しと注記の範囲
- Before/After の依頼文と 3 つの例（型だけ調べるテスト・手元の採点のずれ・検証用の分割）は仮想の例で、実際に Claude で試していない
- 雛形を置かなかったのは、総論で目次の templates が「なし」、検証器を先に作らせる依頼は build-test-harness の持ち主だから
- Vasconcelos ら（2023）の結果は束の要約（p12#86）だけで書いた。印は保守的に「中・類推」にした
- 新しい出典を足していない（sources は data/sources.yml にある既存の id のみ）

## 使用量
- 道具の呼び出し：約 11 回（Read 2、Bash 7、Write 3 〔図・ページ・報告〕、check_page 2 回を含む）。Web の取得：0
