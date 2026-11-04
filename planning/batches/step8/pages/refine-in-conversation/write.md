# write.md：refine-in-conversation

## 書いたファイル
- docs/prompting/refine-in-conversation.md（stubs から mv。stage を draft、updated を 2026-11-05。sections に why・limits を追加。sources を cc-docs-best-practices に）
- snippets/refine-in-conversation/follow-up.txt・follow-up.expect.yaml（目次の templates は「なし」。分かりやすさのために 1 つ足した）

## 必ず持つものの対応
- 原理 `principle`（見せる）を本文で名指す：#why、要点の「関わる原理と原因」
- 原因 `prevents`（見えていない・散らかっている）を本文で名指す：#why（2 つの箇条）、要点
- `pitfalls`：front matter に無いため持たない（stub に pitfalls キーがない）
- level 「使う」、要点の最初は「何が分かるか」：冒頭の要点の囲み
- 技法の構成：Before/After は #start-plain、何が変わるかは #start-plain の直後の段落、なぜ効くかは #why、効かない場面・やりすぎは #limits

## メインに判断してほしいこと
- 「Claude Code の作者のチームの習慣として紹介」（#why、根拠：弱）は二次の記事の紹介。個人名は出していない。弱すぎるなら削ってよい
- 節 edit-the-request は目次の備考どおり短く、rewind-dont-correct#why に譲った

## 提案
- なし（新しい用語・数値・出典はない）

## 検査の結果
- 1 回目：エラー 0・警告 2（「一回」2 か所）。2 回目：エラー 0・警告 1
- 残した警告：44 行の「一回で決めない」は題名と別名にある言葉をそのまま使った所のため（誤検出）

## 確かめていないこと
- 「2026-11-03 に確かめた版」の Best practices の記述は、束の research/23 §3.1 の写しによる。原文を開いていない
- Before/After の例は作ったもので、Claude で試していない（本文にそう書いた）
- 雛形 follow-up の動作は確かめていない

## 使用量
- 道具の呼び出し 12 回ほど、Web の取得 0 回
