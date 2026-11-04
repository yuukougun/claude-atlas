# write.md：handing-long-documents

## 書いたファイル
- docs/context/handing-long-documents.md（stubs から mv。stage: draft、updated: 2026-11-05。front matter で変えたキー：sections〔what-happens・effects・misconceptions を足した。既存 3 つの anchor はそのまま〕・sources〔hc-upload-files・api-docs-files・stulberg-code-everything-code-tips-tricks〕・stage・updated）
- snippets/handing-long-documents/read-check.txt と read-check.expect.yaml（読まれたかを引用で確かめる依頼。目次の templates は「なし」だったので、分かりやすさのために足した）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle・prevents を本文で名指す）：#effects（見せる・確かめる／見えていない・散らかっている）。pitfalls は空なので名指す対象なし
- level を持つ：front matter の level: 整える
- 要点の最初は「何が分かるか」：冒頭の要点の囲みの 1 項目目
- 構成（原理のページ：例 → なぜ → 何に効くか → 誤解 → 関連）：例は #what-happens、なぜ・やり方は #split-and-convert（広い机の比喩は attention-budget#why を指す。図は作らず）、限りは #limits、何に効くかは #effects、誤解は #misconceptions、関連はテンプレートが出す

## メインに判断してほしいこと
- 比喩の図は置いていない（attention-budget に持ち主の図がある前提で、link で指した）。足すかは判断を仰ぐ
- Claude Code と API 側の PDF の読み込みの上限は、束にも data にもないので本文で数えず「未確認」「該当ページへ」とした

## 提案
- 数値の提案なし（アプリの PDF の上限は既存の facts の app-pdf-visual-pages・app-pdf-text-only-pages を fact の目印で指した）
- 参考：at-reference-read-limit は status 未確認のため本文で使っていない

## 検査の結果
- check_page.py 2 回：1 回目 エラー 0・警告 3（no-doubled-joshi）、直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形 read-check の動作（実際に長い PDF で試していない）
- markitdown などの変換ツールの現在の成熟度・使い方（実践者の記事〔根拠：弱〕の紹介のみ。名前は考え方の例）
- 「PDF 以外の文書は図や画像が読まれない」は束の調査資料（公式の Upload files の要約）に基づく。本文の記事は開いていない
- Claude Code が PDF を読む範囲、API の PDF の上限
- 本文の link の表示（生成後の題名）と節の指し先は check_page の通過のみで、読み味は未確認

## 使用量
- 道具の呼び出し 約 12 回（Read 2・Bash 6・Write 4 ほか）、Web の取得 0 回
