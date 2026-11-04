# write.md：must-know-operations（執筆）

## 書いたファイル

- docs/cli/must-know-operations.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-interactive-mode・cc-docs-commands・cc-docs-permission-modes、sections に when・pitfalls・compare・outdated を足した。既存の 4 節の anchor は変えず）
- snippets/must-know-operations/long-instruction.md と .expect.yaml（prompt）
- snippets/must-know-operations/screenshot-request.md と .expect.yaml（prompt）
- planning/batches/step8/pages/must-know-operations/facts-proposal.yml
- data/sources.d/must-know-operations.yml は作らなかった（出典は data/sources.yml に既にある 3 件のみ）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す。要点の「強制力」に `feature interactive-mode/enforcement` と `feature permission-modes/enforcement` の目印を置いた（冒頭）
- tracks：front matter に interactive-mode・permission-modes（変更なし）
- level：整える（変更なし）
- 構成の目安（使いどころ→最小の使い方→雛形→効かない場面→比べる相手→古くなった助言）：使いどころ #when、最小の使い方 #modes・#input・#watch-and-background、雛形 #input（2 つ）、効かない場面 #pitfalls、比べる相手 #compare、古くなった助言 #outdated。面のタブは surfaces が claude-code だけなので置かない

## メインに判断してほしいこと

- キーの割り当て（Shift+Tab・Ctrl+G・Ctrl+O・Ctrl+B・画像の貼り付けなど）を、目次の notes どおり data に置くか。今は data に項目がないので、本文はバッククォートで手書きした。facts-proposal.yml に案がある。置くなら、本文の該当箇所を目印に差し替える
- 目次の templates は「なし」だったが、分かりやすさのために雛形を 2 つ足した（長い指示の骨組み・画像で渡す依頼文）。不要なら外す

## 提案

- front matter：直さない（sections・stage・updated・sources のみ変更）
- 数値の提案：facts-proposal.yml（キー割り当て 4 件）
- 用語集・prh：なし

## 検査の結果

- check_page.py：1 回目 エラー 0・警告 6（snippet 目印の改行 2、助詞の重複 4）。直した後 エラー 0・警告 0。途中で直しのスクリプトが失敗し、直さずに 1 回余分に流した（結果は同じ）

## 確かめていないこと

- キーの割り当ては、束に写された調査資料（確認日 2026-10-29）による。実機でも公式の文書でも確かめていない。Windows・WSL の `Alt+V`、iTerm2 の `Cmd+V` も同じ
- `Ctrl+G` で開く外部エディタの決まり方・戻ったあとの動き。計画の編集に使えるか（目次の notes が確かめるよう書く点）は、書いていない
- `Shift+Tab` が巡るモードの並びと、押した後の表示の場所。本文は「表示されたモードの名前を確かめる」までにした
- `Esc` 2 回押しの分かれ方（入力のクリアか rewind か）の条件
- 背景のタスクの出力を「Claude に頼んで読ませる」書き方は、ledger の TaskOutput の行（Read でファイルを読む）の言い換え
- IDE の記述（`!` の近道とタブ補完がない・`Option+K`/`Alt+K`）は research/26 の写しで、動作は試していない
- 判断例の「10 回ほど続けて頼む」は例の数で、根拠のある数値ではない

## 使用量

- 道具の呼び出し：約 14 回（Read 4・Bash 5・Write 6 を含む見込み）。Web の取得：0 回
