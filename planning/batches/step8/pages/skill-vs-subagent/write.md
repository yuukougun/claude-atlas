# write.md：skill-vs-subagent

## 書いたファイル
- `docs/extend/skill-vs-subagent.md`（stubs から mv。front matter は sections・sources・stage=draft・updated=2026-11-05 だけ変えた）
- `snippets/skill-vs-subagent/test-triage.md` と `.expect.yaml`（context: fork のスキル。目次の templates の案）
- `snippets/skill-vs-subagent/release-reviewer.md` と `.expect.yaml`（`skills` で基準を読み込む読み取り専用サブエージェント。分かりやすさのために足した）
- sources.d は作っていない（使った出典 4 つはどれも data/sources.yml にある）

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`（「何ができるか」の 1 文が〜なら A、〜なら B の基準）
- 比較の表（属性は数値ファイルから生成）：`#table`（`compare 読み込みの時期 コンテキストのコスト 入った版`）
- 判断例：`#how-to-choose`（リリース手順・長いテスト出力）、`#combine`（レビューの基準と役割）
- 組み合わせ方：`#combine`
- 確かめ方（共通 §6）：`#combine` の末尾（`/context` で比べる 3 段）
- level：front matter の 任せる

## メインに判断してほしいこと
- 表の列から「強制力」「圧縮で残るか」を外した。subagents の強制力が data で空（注に「書かない」）、圧縮で残るかも null で、表が「未確認」だらけになるため。圧縮は表の下の箇条で書いた。subagents に `survives_compaction`（記録は圧縮の影響を受けない）を入れるなら、列を足せる

## 提案
```yaml
facts-note: 数値の提案はない。
frontmatter: []
```
- 用語集への提案：なし

## 検査の結果
- 書き終えた後：エラー 3（prh：「skill」「subagent」「front matter」）。直した後：エラー 0・警告 3
- 残した警告（no-doubled-joshi）：65 行（生成されたリンクの題名を含む文）、83 行、87 行。長いリンク題名が入る文で、分けると読みにくくなるので残した

## 確かめていないこと
- 雛形 2 つの動作は試していない
- context: fork の挙動（履歴が見えない・本文が依頼になる・agent の既定が general-purpose・既定でバックグラウンド・指針だけの本文は無意味）は、2026-11-05 に公式の skills 文書を 1 回取得して確かめた。取得は先頭の約 10 万字まで。subagent 側の `skills` の挙動も同じ文書の比較表による
- 「スキルもサブエージェントもお願いの層」は、data の注（定義の指示はお願い、道具の制限は仕組み）を踏まえて書いた。道具の制限が機械で効く点は `#combine` で別に書いた
- 「サブエージェントの記録は圧縮の影響を受けない」は data の注による
- 修正の一部（prh と助詞の直し）を、Edit ではなく Bash の Python 置換で行った。ページ全体は Write で書いた

## 使用量
- 道具の呼び出し：約 17 回、Web の取得：1 回、check_page.py：2 回
