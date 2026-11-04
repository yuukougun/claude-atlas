# tokens 執筆報告

## 書いたファイル
- docs/basics/tokens.md（stub から移動。front matter は sections・sources・stage=draft・updated=2026-11-05 を変更）
- docs/img/tokens/split.svg（英語と日本語の仮の区切りの図。実測ではないと図中と本文に明記）
- data/sources.d/tokens.yml（api-docs-glossary を追加。用語集 Tokens の項を WebFetch で確認）
- 雛形なし（目次の templates が空。数える手段はタブで説明）

## 必ず持つものの対応
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 原理「見せる」を名指す：#effects
- 原因「合っていない」を名指す：#effects
- pitfalls：front matter に値がないため持たない
- 構成（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens → #why → #count → #effects → #misconceptions。関連はテンプレートが出す

## メインに判断してほしいこと
- 原理「見せる」・原因「合っていない」の定義の正本が見当たらず（four-principles は空）、本文は自分の言葉で説明した。正本ができたら合わせる
- アプリでトークン数を数える手段は確認できず「未確認」と書いた
- 倍率・約 30%・3.5 文字は本文に書かず（fact の id が data にないため）、facts-proposal.yml に提案。承認されたら本文に目印を足す場所を used_in に書いた

## 提案
- data/sources.yml 側の追加が要るか：api-docs-glossary は sources.d/tokens.yml に置いた
- 数値は facts-proposal.yml（3 件。3 件目は migration guide 本文を未確認のため status を要確認にした）

## 検査の結果
- 1 回目：エラー 0・警告 3（助詞の重複）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 移行の手引き本文（1〜1.35 倍の記述）は研究資料の写しのみで、一次を開いていない
- 図の区切り（5 つと 7 つ）は実際の tokenizer の出力ではない
- /context がトークン単位で占有量を表示するかは束の記述（inspect-context の要約）に依拠
- 日本語が英語より多めになるかの実測は japanese ページに任せ、書いていない

## 使用量
- 道具の呼び出し 約 18 回、Web の取得 1 回
