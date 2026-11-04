# inspect-context 執筆報告

## 書いたファイル
- docs/context/inspect-context.md（stub から mv。front matter の変更：stage を draft、updated を 2026-11-05、sources に cc-docs-context-window・cc-docs-commands・cc-docs-how-claude-code-works・cc-docs-best-practices、sections に limits を追加）
- snippets/inspect-context/baseline-note.md と baseline-note.expect.yaml（起動直後の基準値のメモの雛形。目次の templates は「なし」だが、節 baseline で要るので足した）
- docs/img/inspect-context/triage.svg（目次の visual の案：3 区分と片付け方の対応。静的な図）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが tracks（context-window）から出す。本文には書かない。要点の「強制力」は、機能に強制力の属性がないので、「なし。見せるだけ」と手で書いた（値ではなく性質）
- tracks：front matter（context-window）のまま
- level：front matter（任せる）のまま
- 要点（強制力・確認日と版）：冒頭の要点の囲み
- 使いどころ（どの原因を防ぐか）：#reading・#what-to-do（散らかっている）
- 最小の使い方（面のタブ）：surfaces が claude-code のみなのでタブは置かない。#baseline の手順が最小の使い方
- 雛形：#baseline の baseline-note
- 効かない場面・落とし穴：#limits
- 比べる相手：#limits（/usage との使い分けを link。comparison のページは束にない）
- 古くなった助言：台帳の行なし（outdated_advice が空）

## メインに判断してほしいこと
- 節 limits を足した（落とし穴と比べる相手の置き場所）。不要なら外してよい
- 動く図は作らず、公式の Explore the context window へのリンクにした（目次の備考 M8 の「リンクか自作か」の選択）

## 提案
- 数値の提案はなし
- front matter の提案：なし
- 用語集：なし

## 検査の結果
- 1 回目：エラー 0・警告 5（生成された link の題名が長く、sentence-length と助詞の警告）。箇条を分けて直した
- 2 回目：エラー 0・警告 3。残した理由：助詞の重複 2 件は太字の見出し語（「会話が大きい」「大きいことは悪いことではない」）によるもので読みを損なわない。「三つ」の警告 1 件は自分の文の「三つの道具の使い分け」で、検査の後に「道具の使い分け」へ直した（再検査はしていない）

## 確かめていないこと
- `/context all` の引数と全画面表示での折りたたみは commands の文書で確かめたが、実機では動かしていない（WSL の CLI でのカテゴリ名・並びは未確認）
- 内訳のカテゴリ名の一覧は本文に固定していない。実際の画面に出る名前との対応は未確認
- 基準値を取る手順は実践者の記事（束の 6.2）に基づく。取り直しで差が足したものに当たることは観察の想定で、実機で確かめていない
- 「トークン数のほうが割合より比べやすい」は推論で、印を付けた
- 他の OS・IDE 拡張・Desktop の表示は未確認と本文に書いた

## 使用量
- 道具の呼び出し：約 12 回（Read 3・Bash 6・Write 1・ToolSearch 1・WebFetch 2）
- Web の取得：2 回（Explore the context window、Commands）
