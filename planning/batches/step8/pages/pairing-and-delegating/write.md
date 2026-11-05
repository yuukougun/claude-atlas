# write.md：pairing-and-delegating（伴走と委託）

## 書いたファイル
- docs/delegate/pairing-and-delegating.md（stubs から mv。stage draft、updated 2026-11-05、sections に 7 節を追加。ほかのキーは変えていない）
- docs/img/pairing-and-delegating/modes.svg（伴走と委託の対比の図。目次の visual 案どおり static）
- 雛形・出典のファイルは作っていない（目次の templates は「なし」。sources は空のまま）

## 必ず持つものの対応
- 冒頭の要点の「何が分かるか」が最初の項目：冒頭の要点の囲み（level は front matter の「任せる」）
- front matter の principle（握る・確かめる）を本文で名指す：what-it-prevents（「握る」「確かめる」の項）
- front matter の prevents（合っていない）を本文で名指す：what-it-prevents（「合っていない」の項）
- front matter の pitfalls（預けすぎる）を本文で名指す：what-it-prevents（「預けすぎる」の項）。misconceptions でも丸投げに触れた
- 構成の目安（要点→何が起きるか→なぜ→何に効くか→誤解→関連）：what-happens → why-bottleneck-moves → choose・guards-before-delegating → what-it-prevents → misconceptions。関連はテンプレートが出す。two-modes は定義の節として最初に置いた

## メインに判断してほしいこと
- 伴走と委託の 2 分類の出どころは、調査資料 11（p34#143、根拠：中）の実務家の整理だけ。出典の id が束にないので sources は空にし、本文では（根拠：弱）の印を付けて個人名は出していない。出典を足す場合は、元の投稿の登録（check_noai.py での確認を含む）をお願いしたい
- 表の「この辞典の level」の行（伴走＝任せる、委託＝回す）は requirements §3.3 と目次の level_evidence から書いた対応づけ

## 提案
- 用語集：「伴走」「委託」を追加（伴走＝人が途中を見て舵を取る進め方、委託＝完了条件を渡して任せ後で確かめる進め方）。aliases の「丸投げ」は、本文では「完了条件も確かめ方も渡さない任せ方」として別に定義した

```yaml
glossary:
  - {term: 伴走, definition: "人が途中を見ながら、一歩ずつ方向を直して進める協業の形", page: pairing-and-delegating}
  - {term: 委託, definition: "完了条件を渡して任せ、戻ってきた結果を後で確かめる協業の形", page: pairing-and-delegating}
```

## 検査の結果
- `check_page.py` を 2 回流した。最終はエラー 0・警告 5
- 残した警告：75 行（図の代替テキストの読点が 4 つ以上。図の要点を落とさないため）、89 行と 97 行と 106 行（link の目印が道具によって埋めた題名「五つの軸」「計画を承認した後」「投げる前に決める守り」などの助詞・数字表記で、手では直せない）、119 行（「完了条件も確かめ方も」の対句をわざと残した）

## 確かめていないこと
- 本文の機能の挙動（plan mode、背景セッションなど）は、束にある相手ページの要約と指せる節の題名の範囲に収め、一次資料を開いていない。Web の取得は 0 回
- 「判断例」「同じ作業を二通りで進めると」の例は、説明のための想定で、実際のセッションで試していない
- 検査の 2 回目の直しは、Write ではなく Bash（python による文字列置換）で行った。指示の「ページは Write で書く」からのずれである
- SVG の見え方（表示の崩れ）は目で確かめていない
- 誤解の項「伴走なら最後の確かめは要らない」ほか、誤解の例は書き手の整理で、出典はない（推論・実践例なし）

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 6、Write 3 ほか）。Web の取得 0 回
