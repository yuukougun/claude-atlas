# write.md：caves-when-pushed

## 書いたファイル
- docs/symptoms/caves-when-pushed.md（stubs から mv。front matter：sections に forms・examples・prevent を追加、stage を draft、updated を 2026-11-05、sources を 5 件）
- snippets/caves-when-pushed/hide-preference.txt・fresh-critique.txt と各 .expect.yaml
- data/sources.d は作っていない（sources は data/sources.yml に既にある id だけ）

## メインに判断してほしいこと
- 目次の templates は「なし」だったが、聞き方の雛形 2 つを足した。不要なら外してよい。
- 数値（説得率 84.5%、押し返しの 9%→18% など）は本文に書かず、向きだけ書いた。数値にするなら facts の提案が要る。
- 「お願いの文言では直りにくい」は ELEPHANT 系の材料（束 6.6）によるが、sources に arxiv-2505-13995 を入れていない。入れるなら front matter の提案。

## 提案
```yaml
frontmatter:
  - {id: caves-when-pushed, key: sources, before: [...], after: [..., arxiv-2505-13995], reason: "プロンプトでの緩和がまちまちという記述の出典"}
```

## 検査の結果
- 1 回目：エラー 1（prh：subagent）・警告 16。2 回目（直した後）はこの 1 件を直し、警告を残した（数字の書き方は「3つ」にするとスペースの規則とぶつかるため、漢数字のまま。長文・助詞の警告の多くは link の目印から入る題名の文）。
- 2 回目の最終状態の再実行はしていない（回数の制限）。数字の置き換えを試して戻した。

## 確かめていないこと
- Claude Code の `/clear` と新しい会話の動作、API の履歴を持ち越さない扱いは、束の材料と一般的な理解に基づき、実機では確かめていない。
- 研究の数値の向き（後から追撃のほうが寝返りやすい等）は束の要旨による。一次資料は開いていない。
- 最終の check_page の結果（直後の状態）は流していない。

## 使用量
- 道具の呼び出し：約 12。Web の取得：0。
