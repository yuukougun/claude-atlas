# write.md：manual-only-skills

## 書いたファイル
- docs/extend/manual-only-skills.md（stubs から mv。stage draft、updated 2026-11-05。front matter で変えたキー：sections を足した、sources に cc-docs-skills・cc-docs-features-overview・cc-docs-permissions・cc-docs-best-practices を入れた）
- snippets/manual-only-skills/deploy-skill.md と .expect.yaml（skill、safety true）、deploy-ask.json と .expect.yaml（settings、ask ルール、safety true）
- data/sources.d は新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点（強制力のバッジ）：冒頭の囲みの「強制力」の行。feature 目印でバッジの値を出し、止まる範囲を一言
- 機能の属性のバッジ：テンプレートが出すバッジの列と、冒頭の強制力の行（tracks: skills）
- tracks：front matter の tracks: [skills]
- 1機能1ページ・公式の網羅をしない：全体（キー 2 つの向きの違いまでに絞った。anchor: variants）
- level：front matter の level: 仕組みにする
- 構成の目安：使いどころ＝use／最小の使い方＝minimal（面のタブは置いていない。理由は下）／雛形＝templates／効かない場面・落とし穴＝limits／比べる相手＝compare／判断例＝need-lock
- 古くなった助言：持たない。台帳に該当の行がなく、outdated_advice も空のため

## メインに判断してほしいこと
- 面のタブは、surfaces が claude-code だけなので置かず、本文で「Claude Code のスキルの設定」と書いた
- 束の備考どおり、「sign の言い換えにも読める does-more-than-asked」へは need-lock の末尾で 1 回だけ指し、このページが直接の答えになる場面を狭く書いた

## 提案
- 用語集：特になし
- 数値の提案：なし（本文に数値・版・既定値を手で書いていない）

## 検査の結果
- 1 回目：エラー 2（prh：front matter → フロントマター）・警告 2。2 回目（直した後）：エラー 0・警告 1（助詞「も」の重なり）
- 警告 1 は 2 回目の後に文を直した（「人と Claude のどちらでも呼べる」）。再検査は上限のため流していない

## 確かめていないこと
- 雛形 2 つの動作（実機で動かしていない）。ask ルールの Bash パターン `Bash(./scripts/deploy.sh *)` の書式は、permission-rules のページの書き方と合わせて検証の担当が見てほしい
- 公式の文書（skills、取得 1 回）で確かめたのは、表の 3 行、subagent の事前の読み込みと定期実行の停止、skillOverrides の user-invocable-only の向き。止められた Claude が「人に /deploy を打つよう案内する」挙動の実機の確認はしていない
- 公式の文書の後ろ 19000 字ほどは読んでいない
- アプリ・IDE 拡張・Windows での動作は未確認

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：1 回
