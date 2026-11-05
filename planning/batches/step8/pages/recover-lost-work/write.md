# write.md：recover-lost-work

## 書いたファイル
- docs/cli/recover-lost-work.md（stubs から移動。stage を draft、updated を 2026-11-05、sources を cc-docs-sessions・cc-docs-commands・cc-docs-checkpointing・cc-docs-data-usage に、sections に guards・check・when-it-fails を足した。既存の order・transcripts・retention は変えず）
- snippets/recover-lost-work/find-transcripts.sh・.expect.yaml（kind other。語が出るファイル名だけを出す）
- snippets/recover-lost-work/ask-search-transcripts.md・.expect.yaml（kind prompt。過去のトランスクリプトを読むだけで検索させる依頼）
- data/sources.d/recover-lost-work.yml は作っていない（新しい出典なし。既存の id だけを使った）

## 必ず持つものの対応
- 手順：order（探す順の 4 段と図）・transcripts（読み方 3 通り）
- 確かめる・縛るのページへの道（front matter の前提か関連）：前提は resume-and-branch・checkpoints-and-rewind、関連は protecting-secrets・what-feedback-sends・working-with-git・deleted-something-important#recover など。本文では guards で working-with-git#granularity・protecting-secrets#keep-out・what-feedback-sends#before-sending へ link
- level：front matter の「任せる」のまま
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：冒頭の囲み → guards → order・transcripts・retention → check → when-it-fails

## メインに判断してほしいこと
- 方針の文は足していない。保持期間を延ばす助言は、秘密が長く残る点と並べて書いた（判断例 retention）。承認が要る文には当たらないと考えた

## 提案
- facts は新規なし。使った既存の id：local-transcript-cleanup-days・checkpoint-retention-days・key-transcript-and-background（status 未確認のまま）
- data/facts.yml の sessions 機能の note に、「JSONL の記録に圧縮の前のやり取りがどこまで残るか」は未確認と足す案（本文では確かめていないと書いた）

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告 2（no-doubled-joshi「に」）。どちらも link の目印の間に道具が入れた、相手の題名と節名の中の「に」が原因と見ている。目印の間は手で直せないので残した

## 確かめていないこと
- `~/.claude/projects/` の下のディレクトリ構成、JSONL の中身（道具の呼び出しの記録がどこまで残るか）、圧縮の前のやり取りが記録に残るか。束にないので断定せず、「確かめていない」と書いた
- 雛形 2 つの動作（expect は試し用セッションが前提）。macOS・Windows・IDE 拡張の動作
- `claude --resume` の一覧の細かな挙動は束の記述の範囲で書いた

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 0 回
