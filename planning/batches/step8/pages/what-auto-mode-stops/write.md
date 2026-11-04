# write.md（what-auto-mode-stops・執筆）

## 書いたファイル
- docs/enforce/what-auto-mode-stops.md（stub から移動。stage を draft、updated を 2026-11-05。sections に templates・compare・outdated を足した。sources は束にある既存の id 8 件）
- snippets/what-auto-mode-stops/auto-mode-environment.{json,expect.yaml}（settings・safety: true）
- snippets/what-auto-mode-stops/ask-before-push.{json,expect.yaml}（settings・safety: true。目次の案に足した雛形）
- docs/img/what-auto-mode-stops/classifier-view.svg（目次の図の案：分類器が見るものと見ないもの）
- facts-proposal.yml（数値の提案 2 件）
- data/sources.d は作っていない（使った出典は data/sources.yml に既にある）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。要点の「強制力」は、data の auto-mode に enforcement がなく note も強制力を書かないとしているので、feature の目印を使わず「鍵には数えない」と文で書いた（#defaults の前の要点）
- tracks：front matter の tracks（auto-mode・permission-modes）は変更なし
- 要点→使いどころ（防ぐ原因）：要点と #defaults（#limits で境界がない・縛っていない・預けすぎるを補う守りの表）
- 最小の使い方（面のタブ）：#by-surface（アプリ・Claude Code）
- 雛形（折りたたみ）：#templates
- 効かない場面・落とし穴：#limits
- 比べる相手：#compare（表。comparison ページを指すものは、束に該当ページがないため link は permission-modes-overview#modes のみ）
- 古くなった助言：#outdated（台帳 2 行を link で指した）
- level：front matter の「任せる」のまま

## メインに判断してほしいこと
- 数値の置き方：誤検知率 0.4%・見逃し率 17%・5.7% は、card §7 の「研究の結果は固定の記録」に当たると読み、記事の日付・データの種類・n を添えて本文に書いた（根拠：中）。目次の notes は「数値は data に置く」とあるので、data に置くなら facts-proposal.yml の 2 件目を採り、本文を fact の目印に替える。連続 3 回／合計 20 回の上限は本文に書かず、1 件目の提案にした（本文は「一定の回数」）
- 強制力の書き方：data の auto-mode に enforcement がない前提で、要点の「強制力」を手書きの文にした。feature の目印を使える形（enforcement の値か、値なしの表示）にするか決めてほしい

## 提案
- facts：facts-proposal.yml
- 用語集：「分類器（auto モードの）」は本文で「別のモデル（分類器）」と短く定義した。用語集に入れるか決めてほしい
- 台帳：yolo-skip-permissions の `now` と本文の勧めは合っている。変更の提案なし

## 検査の結果
- check_page.py：最初の実行で警告 6（冗長・読点・文の長さ・助詞の重複）、直した後は エラー 0・警告 0。指示は 2 回だが、直しを 2 回に分けたので計 3 回流した

## 確かめていないこと
- 実機での動作（雛形の expect はすべて未確認。確かめるのは動作確認の担当）
- 既定のブロック・許可の一覧は束の写し（research/01 C-1、確認日 2026-10-29）と設定ページ（今回の取得）によった。permission-modes の本文は今回開いていない
- 「判定が返らないとき」の案内は auto-mode-config の記述に基づく。errors ページの原文は開いていない
- アプリ側で `autoMode` や分類器の設定が使えるかは確かめていない（本文は Claude Code の機能と書いた）
- 作業ディレクトリ内の `.env` の読み取りが分類器に止められるかは、公式に記述を見ていない。「止める保証はない」という書き方にした（推論）

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 7、Write 6、ToolSearch 1、WebFetch 1 を含む概数）
- Web の取得：1 回（https://code.claude.com/docs/en/auto-mode-config）
