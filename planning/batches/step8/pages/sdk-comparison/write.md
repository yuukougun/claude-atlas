# write: sdk-comparison

## 書いたファイル
- `docs/api/sdk-comparison.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を既存の 8 件、sections に `combine`〔組み合わせ方〕を足した）
- `docs/img/sdk-comparison/loop-and-place.svg`（ループの担い手と動く場所の 2 軸の図）
- `planning/batches/step8/pages/sdk-comparison/facts-proposal.yml`
- 雛形と `data/sources.d/sdk-comparison.yml` は置いていない（目次の templates はなし。出典は既存の id だけで足りた）

## 必ず持つものの対応
- 比較の表（`compare` の目印）：`#comparison`（手書きの軸の表と、`compare 面 成熟度` の生成表）
- 判断例：`#examples`（4 件。Client SDK／CLI／Managed Agents／claude.ai ログインの扱い）
- 組み合わせ方（型の構成の目安）：`#combine`
- level：front matter の「仕組みにする」のまま

## メインに判断してほしいこと
- 「第三者の製品が claude.ai のログインやプランの上限を提供することは承認がない限り認められていない」を 2 か所に書いた（出典は Agent SDK overview。束の data の note と 02 §5-9）。公開の方針の文には当たらない（Anthropic の規則の紹介）と判断したが、気になるなら削る
- Managed Agents の単価は本文に書かず、facts-proposal.yml に提案した。承認されたら `#managed-agents` の「費用の面では」の文に fact の目印を足す

## 提案
- data：`facts-proposal.yml`（managed-agents-session-hour-price）
- 用語集：Agent／Environment／Session／Events（Managed Agents の構成要素）は本文で短く定義した。用語集への追加を検討してほしい

## 検査の結果
- 1 回目：エラー 4（prh：sandbox・system prompt・skills）・警告 5。直して 2 回目：エラー 0・警告 2
- 残した警告 2：どちらも `link` の目印が生成する長い題名（節の題名を含む）で文が長くなったもの（要点の「前提」の行と、Agent SDK の箇条）。本文の文は短いので誤検出として残した

## 確かめていないこと
- Managed Agents の構成要素・向く用途・ZDR の対象外は、束の 02 §5-9（確認日 2026-10-29）と data の note に基づく。公式の文書で再確認していない（Web の取得は 0 回）
- CLI を「対話の開発と `claude -p`」と書いたのは、02 §5-9 の使い分け表と headless の note による。インタラクティブな Claude Code の詳細は扱っていない
- 「試作は CLI、製品は SDK」「単純な呼び出しは Client SDK、作業は Agent SDK」は、束の材料から導いた実務上の組み合わせ方で、公式の推奨ではない（推論・実践例なしに近いので、印は付けていない。必要なら検証側で判断してほしい）
- 図の SVG はブラウザで描画を見ていない
- 指す先の節（tool-use-loop など）は、まだ準備中のページが多い（リンクは「準備中」と出る）

## 使用量
- 道具の呼び出し：約 14 回（Read 5・Bash 6・Write 5〔SVG・ページ・報告 2・提案〕・Edit 1 を含む）。Web の取得は 0 回
