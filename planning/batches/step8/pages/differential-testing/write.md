# write.md：differential-testing（recipe・eval）

## 書いたファイル
- docs/eval/differential-testing.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 3 件、sections を 3 節足して 5 節）
- snippets/differential-testing/stress-test.txt・.expect.yaml、legacy-compare.txt・.expect.yaml
- data/sources.d/differential-testing.yml（usaco-guide-general-debugging-general を 1 件）
- sections の追加：guard-first・examples・check-and-failure（既存の steps・protect-the-oracle は変えず）

## 必ず持つものの対応
- 手順：#steps（各段に終わりの印）
- 確かめる・縛るのページへの道：前提 verifier-three-conditions（要点・#guard-first）、#guard-first で test-the-verifier・build-test-harness・pitfalls-of-ai-written-tests、#protect-the-oracle で禁止と deny ルール／フック
- level：任せる（front matter。変えていない）
- 構成の目安（守り→手順→確かめ方→失敗したとき）：#guard-first → #steps → #protect-the-oracle・#examples → #check-and-failure

## メインに判断してほしいこと
- USACO Guide の出典は、実際に開くと、ストレステストの詳しい手順ではなく「生成器を書き、遅い単純解と比べる」の 1 文だけだった（詳細は別の節への案内）。本文は 1 文の範囲に抑え、根拠は弱とした
- 「deny ルールやフックで止める」は、リンクなしの一言にした（enforce 分野の対応ページの id が束にないため）。必要なら link を足してほしい

## 提案
- front matter：なし
- 用語集：「愚直解」「本解」を本文で短く定義した（用語集にあるかは未確認）。なければ追加の提案
- data：数値の提案なし。研究の割合（59.6〜68.1%）は研究名と年付きで本文に置いた

## 検査の結果
- 1 回目：エラー 0・警告 6。2 回目（link 重複の整理と文の分割後）：エラー 0・警告 3（助詞「に」「で」の重複）。その 3 件は 2 回目の後に文を直したが、検査の回数の上限のため再検査していない
- 残るかもしれない警告：リンクの題名が長い文（生成後の長さ）

## 確かめていないこと
- 雛形 2 つの動作（expect は未実測）
- Mathews & Nagappan の割合の対象モデル（束の写しに書かれておらず、「LLM ベースのテスト生成ツール」とだけ書いた）
- C コンパイラ事例は束の写しの範囲だけ（原文は開いていない）
- mermaid の描画（検査は通ったが目視していない）

## 使用量
- 道具の呼び出し：約 20 回、Web の取得 1 回（usaco.guide）
