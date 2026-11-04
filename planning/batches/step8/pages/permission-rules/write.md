# permission-rules 執筆報告

## 書いたファイル
- docs/enforce/permission-rules.md（stubs から mv。front matter で変えたキー：sections に when・minimal・templates・compare・outdated を足した／sources を 9 件／stage を draft／updated を 2026-11-05）
- snippets/permission-rules/deny-secrets.json と .expect.yaml、allow-safe-commands.json と .expect.yaml
- data/sources.d は不要（sources は既存の id だけ）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点の「強制力」（`feature enforcement` の目印）。確認日と版のバッジはテンプレートが出す
- tracks：front matter の `tracks: [permissions, settings]`（変更なし）
- 構成の目安：要点→使いどころ #when→最小の使い方（Claude Code のタブ）#minimal→効かない場面・落とし穴 #evaluation-order #path-rules #child-processes #workspace-trust→雛形 #templates→比べる相手 #compare→古くなった助言 #outdated。雛形を落とし穴の後に置いた（落とし穴を先に読ませ、雛形の注意につなげるため）
- level：任せる（変更なし）。比例則：使いどころで、allow の前に deny と ask・サンドボックス・保護される場所を先に示した

## メインに判断してほしいこと
- 「古くなった助言」は台帳に行がないため link を置かず、名前の目印（allowed-tools-to-permissions）と本文の注記で書いた（束の notes の方針どおり）
- 起動時の警告・Read の deny が Write も止める・worktree での解釈・サブコマンドなど、入った版が絡む挙動は版を書かず「新しい版では」「版による」とした。版の数値の提案はしていない

## 提案
- なし（front matter のほかのキー、用語集、data への提案はなし）

## 検査の結果
- check_page.py：1 回目 エラー 9・警告 6（sandbox の表記と助詞の重複・長い文）、直して 2 回目 エラー 0・警告 0。その後、本文の語句を 1 か所だけ消した（「次の 2 つを重ねる。」。再検査はしていない）

## 確かめていないこと
- 雛形 2 つの動作（`Read(**/.env.*)` の当たり方、`Bash(git status)` が引数なしだけに当たること、`Edit` の deny が `.env` の書き込みを止めること）は実機で試していない
- 非対話の `-p` での allow ルールの扱い（信頼との関係）は調べていない。フックの扱いだけを束のとおりに書いた
- 公式の文書の現在の文面は開いていない。束の写し（research 01・11・22・23・28）に基づく
- Windows・macOS・IDE 拡張の動作は未確認（本文は WSL・Linux の CLI を基準にした）
- `/fewer-permission-prompts` の現在の挙動は束の記述だけに基づく

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 0 回
